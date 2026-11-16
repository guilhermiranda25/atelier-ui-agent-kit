# Atelier UI Agent Kit

Eight complementary skills for frontend work with coding agents: visual direction,
component research, design systems, marketing, product interfaces, motion, assets
and quality audits. Created by [Guilherme Miranda](https://github.com/guilhermiranda25).

Oito skills de UI/UX para orientar agentes de programação na criação e manutenção
de interfaces com identidade, acessibilidade e qualidade técnica. O kit reúne
conhecimento, critérios e ferramentas auxiliares; não é um serviço de geração de interfaces.

**[Guia completo em português](docs/README.pt-BR.md)** · **[Complete English guide](docs/README.en.md)**

## Install / Instalar

Requires Python 3.10+; Git is needed for cloning. Open PowerShell:

```powershell
git clone https://github.com/guilhermiranda25/atelier-ui-agent-kit.git
cd atelier-ui-agent-kit

# Preview / Simular
py restaurar_codex.py --somente-uiux --dry-run

# Choose your agent / Escolha seu agente
py restaurar_codex.py --somente-uiux
py restaurar_claude.py --somente-uiux
```

These commands install only the eight skills. Installing both is useful if you
use both agents. They do not install a CLI, register plugins or configure MCPs.
On Linux/macOS, replace `py` with `python3`.

## Skills

| Skill | Purpose / Objetivo |
| --- | --- |
| `atelier-ui-director` | Brief and visual direction / Briefing e direção visual |
| `atelier-ui-research` | References and licenses / Referências e licenças |
| `atelier-ui-design-system` | Tokens, typography and components / Tokens, tipografia e componentes |
| `atelier-ui-marketing` | Landing pages and public websites / Landing pages e sites públicos |
| `atelier-ui-product` | Dashboards, forms and applications / Dashboards, formulários e aplicações |
| `atelier-ui-motion` | Functional motion / Movimento funcional |
| `atelier-ui-assets` | Icons, imagery, palettes and fonts / Ícones, imagens, paletas e fontes |
| `atelier-ui-audit` | Visual, responsive and technical QA / Validação visual, responsiva e técnica |

Start a conversation with your agent:

```text
Use atelier-ui-audit to inspect this frontend, then atelier-ui-design-system
and atelier-ui-product to improve it. Preserve routes, business rules and APIs.
Validate keyboard navigation, mobile layouts and the project's existing tests.
Report which checks you actually ran.
```

## Guides / Guias

- [Português: instalação, uso, atualização e problemas comuns](docs/README.pt-BR.md)
- [English: installation, usage, updates and troubleshooting](docs/README.en.md)
- [Exemplos em português](examples/README.pt-BR.md) · [Examples in English](examples/README.en.md)
- [Release assets and checksums](https://github.com/guilhermiranda25/atelier-ui-agent-kit/releases/tag/v1.0.0)
- [Maintenance and releases](docs/maintenance.md) · [Validation record](docs/validation.md)
- [Optional integrations](docs/integrations.md) · [References and rights](docs/sources-and-rights.md)
- [Changelog](CHANGELOG.md) · [Contributing](CONTRIBUTING.md) · [Security](SECURITY.md)

## Scope and license

Skills remain usable offline after installation. Research and optional integrations
may require network access, tools, accounts or separate licenses. No third-party
component libraries, fonts or illustrations are bundled. The original kit is
[MIT licensed](LICENSE); independent reference services retain their own terms.
Client behavior depends on its version. The validation record distinguishes
installer tests from agent execution and optional integrations.
