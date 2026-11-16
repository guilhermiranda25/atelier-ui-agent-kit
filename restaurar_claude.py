#!/usr/bin/env python
"""Restauracao independente de plugins, skills e MCPs para Windows.

Uso: py restaurar_claude.py
Somente pacote Atelier UI: py restaurar_claude.py --somente-uiux
Instalacao remota: --uiux-url URL_HTTPS --uiux-sha256 SHA256
Plano sem alterar nada: py restaurar_claude.py --dry-run
Somente plugins/skills/MCPs: py restaurar_claude.py --sem-ferramentas

Requer Python 3.10+, Git e Node.js 22.20+. A CLI do agente e instalada por npm
se estiver ausente; uma CLI existente e atualizada, salvo --manter-cli.
Inclui os catalogos recomendados em 06/11/2026. Busca as versoes oferecidas
pelas fontes na execucao. Nao garante disponibilidade futura dos repositorios.
Nao inclui frontend-design da Anthropic. Nao migra o inventario de outra IA.
Nao remove instalacoes anteriores, aceita EULAs, autentica contas nem altera
permissoes/sandbox, modelos de IA ou AGENTS.md. Credenciais precisam de novo login.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

TARGET = "claude"
EXCLUDED = {"frontend-design"}

# Catalogo de restauracao, independente de existir uma instalacao anterior.
CATALOG = [
    ("anthropics/claude-plugins-official", "claude-plugins-official", [
        "superpowers", "context7", "serena", "security-guidance",
        "code-simplifier", "code-review", "typescript-lsp", "pyright-lsp",
        "microsoft-docs",
    ]),
    ("trailofbits/skills", "trailofbits", [
        "differential-review", "insecure-defaults", "property-based-testing",
    ]),
    ("data-goblin/power-bi-agentic-development", "power-bi-agentic-development", [
        "semantic-models", "pbip", "reports", "custom-visuals", "tabular-editor", "pbi-desktop",
    ]),
    ("microsoft/skills-for-fabric", "fabric-collection", ["powerbi-authoring"]),
    ("officetuning/skill-library", "officetuning", ["data-analyst-advisor"]),
]
STANDALONE = [
    ("anthropics/skills", ["webapp-testing"]),
    ("vercel-labs/agent-skills", ["vercel-react-best-practices"]),
    ("supabase/agent-skills", ["supabase-postgres-best-practices"]),
    ("datacoolie/powerbi-skills", ["*"]),
    ("microsoft/playwright-cli", ["*"]),
]
SOURCES = [
    "https://learn.chatgpt.com/docs/cli/reference",
    "https://code.claude.com/docs/en/plugins/cli-reference",
    "https://code.claude.com/docs/en/setup",
    "https://github.com/vercel-labs/skills",
    "https://github.com/data-goblin/power-bi-agentic-development",
    "https://github.com/microsoft/skills-for-fabric",
    "https://docs.sqlbi.com/dax-formatter/mcp-http",
    "https://docs.daxlib.org/user-guide/mcp/install",
    "https://docs.21st.dev/mcp",
    "https://hairlineui.com/ui/mcp",
]


def read_json(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8-sig"))
    except (OSError, ValueError, UnicodeError):
        return None


def parse_json(output):
    decoder = json.JSONDecoder()
    # Procura JSON completo, ignorando um eventual aviso textual anterior.
    for i, c in enumerate(output):
        if c in "[{":
            try:
                obj, end = decoder.raw_decode(output[i:])
                if not output[i + end:].strip():
                    return obj
            except ValueError:
                pass
    return None


def refresh_path():
    home = Path.home()
    entries = [str(home / ".local" / "bin"), str(home / "AppData" / "Roaming" / "npm")]
    if os.name == "nt":
        import winreg
        for key, sub in [(winreg.HKEY_CURRENT_USER, "Environment"),
                         (winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment")]:
            try:
                with winreg.OpenKey(key, sub) as reg:
                    entries.extend(os.path.expandvars(winreg.QueryValueEx(reg, "Path")[0]).split(os.pathsep))
            except OSError:
                pass
    entries.extend(os.environ.get("PATH", "").split(os.pathsep))
    os.environ["PATH"] = os.pathsep.join(dict.fromkeys(x for x in entries if x))


@dataclass
class Result:
    code: int
    output: str = ""

    @property
    def ok(self):
        obj = parse_json(self.output)
        failed = isinstance(obj, dict) and (obj.get("outcome") == "failed" or bool(obj.get("errors")))
        return self.code == 0 and not failed


# BEGIN ATELIER UI INSTALLER — bundled code for independent restoration.
UIUX_SKILL_NAMES = (
    "atelier-ui-director", "atelier-ui-research", "atelier-ui-design-system",
    "atelier-ui-marketing", "atelier-ui-product", "atelier-ui-motion",
    "atelier-ui-assets", "atelier-ui-audit",
)

def uiux_skill_install(args, destination, backups, script_dir):
    """Install only this kit's eight skills; no code from a bundle is executed.

    Result: (success: bool, count: int, detail: str). Rejects untrusted ZIP paths,
    symlinks, duplicate names, decompression bombs, bad checksums and bad manifests.
    """
    import hashlib
    import io
    import stat
    import tempfile
    import urllib.request
    import zipfile
    from pathlib import PurePosixPath

    maximum_zip_bytes = 16 * 1024 * 1024
    maximum_file_bytes = 2 * 1024 * 1024
    maximum_unpack_bytes = 30 * 1024 * 1024
    script_dir = Path(script_dir)
    raw_source = getattr(args, "uiux_origem", None)
    remote_url = getattr(args, "uiux_url", None) or os.environ.get("UIUX_SKILL_URL", "")
    expected_sha = getattr(args, "uiux_sha256", None) or os.environ.get("UIUX_SKILL_SHA256", "")
    source = None
    if raw_source:
        source = Path(raw_source).expanduser()
    elif remote_url:
        source = None
    elif (script_dir / "uiux-skillpack.zip").is_file():
        source = script_dir / "uiux-skillpack.zip"
    elif (script_dir / "skills").is_dir():
        source = script_dir / "skills"
    else:
        return False, 0, "uiux-skillpack.zip ausente: forneca --uiux-origem ou --uiux-url (ou UIUX_SKILL_URL)."

    if expected_sha and not re.fullmatch(r"[0-9a-fA-F]{64}", expected_sha):
        return False, 0, "SHA-256 invalido: informe 64 caracteres hexadecimais."
    if remote_url and source is None:
        from urllib.parse import urlsplit
        parts = urlsplit(remote_url)
        if parts.scheme != "https" or not parts.hostname or parts.username or parts.password:
            return False, 0, "Somente URLs HTTPS publicas sem credenciais sao aceitas."
    if getattr(args, "dry_run", False):
        origin = str(source) if source else remote_url
        return True, len(UIUX_SKILL_NAMES), f"PLANO: instalar skills no destino {destination}; origem {origin}; nada gravado."

    try:
        files = {}
        manifest_bytes = None
        if source is not None and source.is_dir():
            skill_folder = source / "skills" if (source / "skills").is_dir() else source
            mf = skill_folder.parent / "skillpack-manifest.json"
            if not mf.is_file():
                raise ValueError("Manifest de integridade ausente para pasta local")
            manifest_bytes = mf.read_bytes()
            for slug in UIUX_SKILL_NAMES:
                folder = skill_folder / slug
                if not folder.is_dir() or folder.is_symlink():
                    raise ValueError(f"Skill obrigatoria ausente/nao confiavel: {slug}")
                for p in folder.rglob("*"):
                    if p.is_symlink():
                        raise ValueError(f"Symlink nao permitido: {p}")
                    if p.is_file():
                        data = p.read_bytes()
                        if len(data) > maximum_file_bytes:
                            raise ValueError("Arquivo de skill excede 2MB")
                        files[f"skills/{slug}/{p.relative_to(folder).as_posix()}"] = data
        else:
            if source is not None:
                if not source.is_file():
                    raise FileNotFoundError(f"Arquivo nao encontrado: {source}")
                if source.stat().st_size > maximum_zip_bytes:
                    raise ValueError("ZIP excede 16MB")
                zipped = source.read_bytes()
            else:
                req = urllib.request.Request(remote_url, headers={"User-Agent": "AtelierUI-SkillInstaller/1.0"})
                with urllib.request.urlopen(req, timeout=25) as response:
                    if urlsplit(response.geturl()).scheme != "https":
                        raise ValueError("Redirect para URL insegura")
                    zipped = response.read(maximum_zip_bytes + 1)
                if len(zipped) > maximum_zip_bytes:
                    raise ValueError("Download excede 16MB")
            if expected_sha and hashlib.sha256(zipped).hexdigest() != expected_sha.lower():
                raise ValueError("SHA-256 do ZIP nao corresponde ao esperado")
            total = 0
            with zipfile.ZipFile(io.BytesIO(zipped)) as z:
                infos = z.infolist()
                if len(infos) > 350:
                    raise ValueError("Muitos arquivos no ZIP")
                for item in infos:
                    name = item.filename
                    if "\\" in name or "\x00" in name:
                        raise ValueError("Nome invalido no ZIP")
                    path = PurePosixPath(name)
                    if path.is_absolute() or ".." in path.parts or any(":" in piece for piece in path.parts):
                        raise ValueError("Path traversal bloqueado")
                    mode = (item.external_attr >> 16) & 0o170000
                    if mode == stat.S_IFLNK:
                        raise ValueError("Symlink bloqueado no ZIP")
                    if item.is_dir():
                        continue
                    if item.file_size > maximum_file_bytes:
                        raise ValueError("Arquivo de skill acima de 2MB")
                    total += item.file_size
                    if total > maximum_unpack_bytes:
                        raise ValueError("Descompressao acumulada excede 30MB")
                    # Accept either root/skills/... or skills/...; nothing else is installed.
                    parts = path.parts
                    if parts and parts[-1] == "skillpack-manifest.json":
                        if manifest_bytes is not None:
                            raise ValueError("Manifest duplicado")
                        manifest_bytes = z.read(item)
                    elif "skills" in parts:
                        idx = parts.index("skills")
                        if len(parts) < idx + 3:
                            continue
                        if parts[idx + 1] not in UIUX_SKILL_NAMES:
                            continue
                        normalized = "/".join(parts[idx:])
                        if normalized in files:
                            raise ValueError("Caminho duplicado no ZIP")
                        files[normalized] = z.read(item)
        if manifest_bytes is None:
            raise ValueError("skillpack-manifest.json ausente")
        manifest = json.loads(manifest_bytes.decode("utf-8"))
        if not isinstance(manifest, dict):
            raise ValueError("Manifest deve ser objeto JSON")
        if manifest.get("package") != "atelier-ui" or manifest.get("skills") != list(UIUX_SKILL_NAMES):
            raise ValueError("Identidade ou skills nao correspondem ao pacote esperado")
        declared = manifest.get("files")
        if not isinstance(declared, dict) or set(declared) != set(files):
            raise ValueError("Inventario de arquivos difere do manifest")
        portable_paths = set()
        reserved = {"CON", "PRN", "AUX", "NUL", "CONIN$", "CONOUT$"}
        reserved.update(f"{kind}{number}" for kind in ("COM", "LPT") for number in "123456789???")
        for relative, data in files.items():
            path = PurePosixPath(relative)
            if (path.is_absolute() or ".." in path.parts or "\\" in relative
                    or any(piece.endswith((".", " ")) or
                           piece.split(".")[0].upper() in reserved or
                           any(ord(c) < 32 or c in '<>:"|?*' for c in piece)
                           for piece in path.parts)):
                raise ValueError("Caminho nao portavel bloqueado")
            portable = relative.casefold()
            if portable in portable_paths:
                raise ValueError("Caminho duplicado sem diferenca de maiusculas")
            portable_paths.add(portable)
            if hashlib.sha256(data).hexdigest() != declared.get(relative):
                raise ValueError(f"Hash de arquivo invalido: {relative}")
        for slug in UIUX_SKILL_NAMES:
            text = files.get(f"skills/{slug}/SKILL.md", b"").decode("utf-8")
            if not text.startswith("---\nname: " + slug + "\n") or "\ndescription: " not in text:
                raise ValueError(f"Skill com frontmatter invalido: {slug}")
        if sum(map(len, files.values())) > maximum_unpack_bytes:
            raise ValueError("Volume excede limite")
        destination = Path(destination).expanduser()
        backups = Path(backups).expanduser()
        destination.mkdir(parents=True, exist_ok=True)
        backups.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix="atelier-ui-stage-", dir=str(destination.parent)) as tmp:
            stage = Path(tmp)
            for relative, data in files.items():
                rel = PurePosixPath(relative)
                out = stage.joinpath(*rel.parts[1:])
                out.parent.mkdir(parents=True, exist_ok=True)
                out.write_bytes(data)
            # Refuse to overwrite unrecognized symlinks; preserve existing files with backups.
            for slug in UIUX_SKILL_NAMES:
                target = destination / slug
                if target.is_symlink() or (target.exists() and not target.is_dir()):
                    raise ValueError(f"Destino nao e pasta regular: {target}")
                if target.exists():
                    previous = backups / slug
                    if previous.exists():
                        raise ValueError(f"Backup ja existe: {previous}")
                    shutil.copytree(target, previous, symlinks=True)
            completed = []
            try:
                for slug in UIUX_SKILL_NAMES:
                    target = destination / slug
                    completed.append(slug)
                    if target.exists():
                        shutil.rmtree(target)
                    shutil.move(str(stage / slug), str(target))
            except Exception:
                for slug in completed:
                    target = destination / slug
                    if target.is_dir():
                        shutil.rmtree(target)
                for slug in UIUX_SKILL_NAMES:
                    target = destination / slug
                    previous = backups / slug
                    if previous.is_dir() and not target.exists():
                        shutil.copytree(previous, target, symlinks=True)
                raise
        return True, len(UIUX_SKILL_NAMES), f"Skills instaladas em {destination}; backup em {backups}."
    except (ValueError, OSError, UnicodeError, zipfile.BadZipFile, json.JSONDecodeError) as e:
        return False, 0, f"Falha de validacao/instalacao UIUX: {type(e).__name__}: {e}"
# END ATELIER UI INSTALLER


class Restore:
    def __init__(self, args):
        self.args = args
        self.target = TARGET
        self.agent_id = "codex" if TARGET == "codex" else "claude-code"
        self.home = Path.home()
        env_key = "CODEX_HOME" if TARGET == "codex" else "CLAUDE_CONFIG_DIR"
        self.config_root = Path(os.environ.get(env_key, self.home / (".codex" if TARGET == "codex" else ".claude")))
        self.skills_root = self.home / ".agents" / "skills" if TARGET == "codex" else self.config_root / "skills"
        self.work = self.home / ".agent-restore" / TARGET
        self.out = self.home / "restauracao-agentes" / (TARGET + "-" + datetime.now().strftime("%Y%m%d-%H%M%S-%f"))
        self.items = []
        self.installed = {}
        self.audit_notes = []

    def note(self, name, status, detail=""):
        if self.args.dry_run:
            print(f"[PLANO] {name}: {status} {detail}", flush=True)
            return
        self.items.append({"item": name, "status": status, "detalhe": detail})
        print(f"[{status}] {name}" + (": " + detail if detail else ""), flush=True)

    def run(self, argv, capture=True):
        if self.args.dry_run:
            print("[PLANO] " + subprocess.list2cmdline([str(x) for x in argv]), flush=True)
            return Result(0)
        exe = shutil.which(str(argv[0]))
        if not exe:
            return Result(127, "Executavel nao encontrado: " + str(argv[0]))
        try:
            p = subprocess.run([exe, *map(str, argv[1:])], cwd=self.work, check=False,
                               encoding="utf-8", errors="replace", text=True,
                               stdout=subprocess.PIPE if capture else None,
                               stderr=subprocess.STDOUT if capture else None)
            return Result(p.returncode, p.stdout or "")
        except OSError as e:
            return Result(126, type(e).__name__ + ": " + str(e))

    def failure(self, name, result, stage="FALHA"):
        # Comandos conhecidos nao incluem tokens. Guardar so o resumo e exit code.
        obj = parse_json(result.output)
        code = obj.get("failureCode", "") if isinstance(obj, dict) else ""
        self.note(name, stage, f"Exit {result.code}" + ("; " + str(code) if code else "") + "; consulte erros.txt.")
        if not self.args.dry_run:
            with (self.out / "erros.txt").open("a", encoding="utf-8") as f:
                f.write(f"\n{name}\n{result.output[-6000:]}\n")

    def prepare(self):
        if not self.args.dry_run:
            self.out.mkdir(parents=True, exist_ok=False)
            if self.args.somente_uiux:
                # The isolated installer backs up only the eight skills it replaces.
                refresh_path()
                return True
            self.work.mkdir(parents=True, exist_ok=True)
            for name in ("config.toml", "settings.json"):
                src = self.config_root / name
                if src.is_file():
                    shutil.copy2(src, self.out / (name + ".backup"))
            if TARGET == "claude":
                src = self.home / ".claude.json"
                if src.is_file():
                    shutil.copy2(src, self.out / "claude.json.backup")
            if self.skills_root.is_dir():
                shutil.copytree(self.skills_root, self.out / "skills-backup", symlinks=True)
        refresh_path()
        if self.args.dry_run or self.args.somente_uiux:
            return True
        missing = [x for x in ("node", "npm", "npx", "git") if not shutil.which(x)]
        if missing:
            self.note("Pre-requisitos", "PENDENTE", "Faltam no PATH: " + ", ".join(missing))
            print("Instale Git e Node.js 22.20+; no Windows:")
            print("winget install --id Git.Git -e")
            print("winget install --id OpenJS.NodeJS.LTS -e")
            print("Depois abra outro terminal e execute este arquivo novamente.")
            return False
        v = self.run(["node", "--version"])
        nums = re.findall(r"\d+", v.output)
        if not v.ok or tuple(map(int, (nums + ["0", "0"])[:2])) < (22, 20):
            self.note("Node.js", "PENDENTE", "Instale Node.js 22.20+ e tente novamente.")
            return False
        return True

    def bootstrap_cli(self):
        exists = shutil.which(self.target)
        if not exists or not self.args.manter_cli:
            if TARGET == "claude" and exists:
                cmd = ["claude", "update"]
            else:
                package = "@openai/codex@latest" if TARGET == "codex" else "@anthropic-ai/claude-code@latest"
                cmd = ["npm", "install", "-g", package]
            r = self.run(cmd, False)
            refresh_path()
            if not r.ok:
                self.failure("Instalar/atualizar CLI", r)
                if not exists:
                    return False
        r = self.run([self.target, "plugin", "--help"])
        if not r.ok:
            self.failure("Suporte a plugins na CLI", r)
            return False
        self.note(self.target, "CLI_DISPONIVEL")
        return True

    def plugins(self):
        for repo, fallback_market, names in CATALOG:
            result = self.run([self.target, "plugin", "marketplace", "add", repo, "--json"])
            obj = parse_json(result.output)
            market = (obj.get("marketplaceName") or obj.get("marketplace") or fallback_market) if isinstance(obj, dict) else fallback_market
            refresh_cmd = "upgrade" if TARGET == "codex" else "update"
            refreshed = self.run([self.target, "plugin", "marketplace", refresh_cmd, market, "--json"])
            if not result.ok and not refreshed.ok:
                self.failure("Marketplace " + fallback_market, refreshed)
                continue
            if not refreshed.ok:
                self.failure("Atualizacao do marketplace " + market, refreshed, "PENDENTE")
            for name in names:
                if name in EXCLUDED:
                    continue
                plugin_id = name + "@" + market
                args = [self.target, "plugin", "add" if TARGET == "codex" else "install", plugin_id]
                if TARGET == "claude":
                    args += ["--scope", "user"]
                args += ["--json"]
                r = self.run(args)
                if TARGET == "claude":
                    # Atualiza inclusive plugins que ja estavam instalados.
                    update = self.run(["claude", "plugin", "update", plugin_id, "--scope", "user", "--json"])
                    if update.ok:
                        r = update
                    elif r.ok:
                        self.failure("Atualizacao " + plugin_id, update, "PENDENTE")
                if r.ok:
                    data = parse_json(r.output)
                    path = data.get("installedPath") or data.get("installPath") if isinstance(data, dict) else None
                    self.installed[name] = {"market": market, "path": path}
                    self.note(plugin_id, "PLUGIN_REGISTRADO", "Componentes sujeitos a compatibilidade e confianca no agente.")
                else:
                    self.failure(plugin_id, r)

    def skills(self):
        for repo, names in STANDALONE:
            allowed = [n for n in names if n not in EXCLUDED]
            # A origem Anthropic nunca recebe wildcard: frontend-design nao entra.
            if repo == "anthropics/skills":
                allowed = [n for n in allowed if n != "*"]
            if not allowed:
                continue
            args = ["npx", "--yes", "skills@latest", "add", repo]
            for name in allowed:
                args += ["--skill", name]
            args += ["-a", self.agent_id, "-g", "--copy", "-y"]
            r = self.run(args, False)
            if r.ok:
                self.note(repo, "SKILLS_INSTALADAS")
            else:
                self.failure(repo, r)

    def uiux(self):
        if self.args.uiux_escopo == "projeto":
            base = Path(self.args.uiux_projeto or os.getcwd()).expanduser().resolve()
            dest = base / (".claude" if TARGET == "claude" else ".agents") / "skills"
        else:
            dest = self.skills_root
        ok, count, detail = uiux_skill_install(
            self.args, dest, self.out / "uiux-previous", Path(__file__).resolve().parent
        )
        if ok:
            self.note("Atelier UI / UX", "PLANO" if self.args.dry_run else "SKILLS_INSTALADAS", detail)
        else:
            self.note("Atelier UI / UX", "PENDENTE", detail)

    def bundled_mcp(self, plugin_name, marker):
        if plugin_name not in self.installed:
            return False
        item = self.installed[plugin_name]
        candidates = []
        if item["path"]:
            candidates.append(Path(item["path"]))
        cached = self.config_root / "plugins" / "cache" / item["market"] / plugin_name
        if cached.is_dir():
            candidates += sorted([p for p in cached.iterdir() if p.is_dir()],
                                 key=lambda p: p.stat().st_mtime, reverse=True)[:1]
        for root in candidates:
            paths = [root / ".mcp.json", root / "mcp.json"]
            for manifest in (root / "plugin.json", root / ".claude-plugin" / "plugin.json", root / ".codex-plugin" / "plugin.json"):
                data = read_json(manifest)
                if isinstance(data, dict):
                    cfg = data.get("mcpServers")
                    if isinstance(cfg, dict) and marker.lower() in json.dumps(cfg).lower():
                        return True
                    if isinstance(cfg, str):
                        candidate = (root / cfg).resolve()
                        if root.resolve() in candidate.parents:
                            paths.append(candidate)
            for path in paths:
                data = read_json(path)
                if data and marker.lower() in json.dumps(data).lower():
                    return True
        return False

    def mcp(self):
        specs = [
            ("context7", "https://mcp.context7.com/mcp", None, "context7", "context7"),
            ("microsoft-learn", "https://learn.microsoft.com/api/mcp", None, "microsoft-docs", "learn.microsoft.com"),
            ("powerbi-modeling", None, ["npx", "-y", "@microsoft/powerbi-modeling-mcp@latest", "--start"], "powerbi-authoring", "powerbi-modeling-mcp"),
            ("DaxFormatter", "https://api.daxformatter.com/mcp", None, None, None),
            ("daxlib", None, ["npx", "-y", "@daxlib/mcp", "--start"], None, None),
            ("hairline-ui", "https://hairlineui.com/api/mcp", None, None, None),
        ]
        for name, url, command, plugin_name, marker in specs:
            if plugin_name and self.bundled_mcp(plugin_name, marker):
                self.note(name, "MCP_NO_PLUGIN", plugin_name + "; validar em /mcp.")
                continue
            if not self.args.dry_run:
                exists = self.run([self.target, "mcp", "get", name])
                if exists.ok:
                    self.note(name, "JA_CONFIGURADO", "Configuracao existente preservada.")
                    continue
            if TARGET == "codex":
                args = ["codex", "mcp", "add", name] + (["--url", url] if url else ["--", *command])
            else:
                args = ["claude", "mcp", "add", "--scope", "user"]
                args += ["--transport", "http", name, url] if url else [name, "--", *command]
            r = self.run(args)
            if r.ok:
                self.note(name, "MCP_REGISTRADO", "Conexao e autenticacao nao testadas por este instalador.")
            else:
                self.failure(name, r)
        if "serena" not in self.installed:
            self.note("Serena", "PENDENTE", "Plugin nao registrado; requer configuracao por projeto.")

    def tools(self):
        if self.args.sem_ferramentas:
            return
        commands = [
            ("TypeScript, Python LSP e Playwright CLI", ["npm", "install", "-g", "typescript-language-server", "typescript", "pyright", "@playwright/cli@latest"]),
            ("PBIR Tools e Playwright Python", [sys.executable, "-m", "pip", "install", "--upgrade", "pbir-cli", "playwright"]),
            ("Chromium para testes", [sys.executable, "-m", "playwright", "install", "chromium"]),
        ]
        for label, args in commands:
            r = self.run(args, False)
            if r.ok:
                self.note(label, "FERRAMENTA_INSTALADA")
            else:
                self.failure(label, r)

    def finish(self):
        if self.args.dry_run:
            print("\nPlano concluido. Nada foi instalado, atualizado ou gravado.")
            return 0
        notes = [
            "Atelier UI: 8 skills autorais, sem copiar bibliotecas/imagens/fontes de terceiros.",
            "frontend-design da Anthropic nao foi incluido. Uma instalacao anterior nao e removida.",
            "O catalogo esta embutido neste arquivo e funciona sem uma instalacao anterior de Claude/Codex.",
            "Uma execucao futura consulta as fontes atuais; pacotes removidos ou renomeados geram pendencias.",
            "PLUGIN_REGISTRADO/MCP_REGISTRADO nao significam validacao funcional nem garantia de qualidade.",
            "Logins, chaves privadas, aceite de EULA e confianca dos hooks precisam ser resolvidos no agente.",
            "Hooks, agentes, mods e integracao LSP podem funcionar de modo diferente em Codex e Claude.",
            "Security Guidance/Code Review podem depender de Claude e gerar consumo adicional.",
            "Ha sobreposicao entre Microsoft, Data Goblin, OfficeTuning e Datacoolie; use o fluxo adequado por tarefa.",
            "Tabular Editor/te e Power BI Desktop precisam ser instalados separadamente quando necessarios.",
            "DAX Lib: Windows x64 e compatibilidade >=1702. Nenhuma UDF/modelo e alterado neste script.",
            "MCPs e dependencias podem precisar de autenticacao/configuracao especifica depois da instalacao.",
        ]
        pending = sum(x["status"] in ("FALHA", "PENDENTE") for x in self.items)
        report = {"agente": TARGET, "catalogo": "2026-11-06", "pendencias": pending,
                  "itens": self.items, "observacoes": notes, "fontes": SOURCES}
        (self.out / "resultado.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
        lines = ["RESTAURACAO " + TARGET.upper(), "", "Pendencias: " + str(pending), ""]
        lines += [f"{r['status']}: {r['item']} - {r['detalhe']}" for r in self.items]
        lines += ["", "OBSERVACOES", ""] + notes
        lines += ["", "Reinicie o agente e confira plugins, skills e /mcp.", "Erros: consulte erros.txt quando existente."]
        (self.out / "LEIA-ME.txt").write_text("\n".join(lines), encoding="utf-8")
        print(f"\nRelatorio e backup: {self.out}\nPendencias: {pending}. Reinicie {TARGET} apos conferir o relatorio.")
        return 2 if pending else 0


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--dry-run", action="store_true", help="Mostrar comandos sem executar ou gravar nada.")
    p.add_argument("--somente-uiux", action="store_true", help="Instalar apenas as skills Atelier UI, sem depender de Node/Git/CLI.")
    p.add_argument("--sem-uiux", action="store_true", help="Nao instalar as skills Atelier UI nesta execucao.")
    p.add_argument("--uiux-origem", help="Pasta com manifest+skills ou ZIP local do pacote UIUX.")
    p.add_argument("--uiux-url", help="URL HTTPS do uiux-skillpack.zip em GitHub Release ou arquivo direto.")
    p.add_argument("--uiux-sha256", help="SHA256 opcional, fortemente recomendado para download remoto.")
    p.add_argument("--uiux-escopo", choices=("usuario", "projeto"), default="usuario", help="Instalacao global ou no repositorio do projeto.")
    p.add_argument("--uiux-projeto", help="Pasta do projeto ao usar --uiux-escopo projeto.")
    p.add_argument("--sem-ferramentas", action="store_true", help="Pular dependencias npm/pip/Chromium.")
    p.add_argument("--manter-cli", action="store_true", help="Nao atualizar a CLI se ela ja existir.")
    args = p.parse_args(argv)
    if args.somente_uiux and args.sem_uiux:
        p.error("--somente-uiux e --sem-uiux nao podem ser usados juntos.")
    if sys.version_info < (3, 10):
        p.error("Use Python 3.10 ou superior.")
    r = Restore(args)
    try:
        ready = r.prepare()
        if not args.sem_uiux:
            r.uiux()
        if args.somente_uiux or not ready:
            return r.finish()
        if not r.bootstrap_cli():
            return r.finish()
        r.plugins()
        r.skills()
        r.tools()
        r.mcp()
        return r.finish()
    except KeyboardInterrupt:
        r.note("Execucao interrompida", "PENDENTE", "Pode executar o mesmo arquivo novamente.")
        r.finish()
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
