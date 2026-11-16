# Atelier UI Agent Kit — English guide

[Home](../README.md) · [Português](README.pt-BR.md) · [Examples](../examples/README.en.md)

## What the kit provides

Atelier UI Agent Kit is a collection of eight skills and workflows for frontend
projects built with AI coding agents. It provides UI/UX knowledge, implementation
guidance, quality criteria, references and small supporting tools. The aim is to
help an agent understand an interface, make deliberate design decisions and
implement improvements while preserving existing behavior.

It is not an interface generation service, a ready-made component library or a
replacement for your development stack. Execution depends on the agent's tools
and permissions. Skill instructions are primarily in Portuguese, with English
discovery descriptions; the user documentation is available in both languages.

Author: [Guilherme Miranda](https://github.com/guilhermiranda25). Version: 1.0.0.

## The eight skills

| Skill | Purpose and trigger | Typical work and example |
| --- | --- | --- |
| `atelier-ui-director` | Lead a new project or a substantial redesign | Inspect the frontend, establish a brief, propose distinct directions and coordinate delivery. Example: a company website with its own visual identity. |
| `atelier-ui-research` | Evaluate references before adding external resources | Compare licensing, compatibility, dependencies and maintenance. Example: decide whether to adapt an existing selector or adopt a third-party component. |
| `atelier-ui-design-system` | Establish or consolidate visual foundations | Define semantic tokens, typography, themes, states and component contracts. Example: align forms across product modules. |
| `atelier-ui-marketing` | Build public-facing pages | Develop messaging, editorial composition, credible evidence, calls to action and mobile layouts. Example: a consulting firm's landing page. |
| `atelier-ui-product` | Improve task-oriented applications | Plan navigation, filters, tables, forms, permissions and interface states. Example: an operations dashboard or course platform. |
| `atelier-ui-motion` | Use movement to communicate change | Specify transitions, feedback, timing and accessible fallbacks. Example: a drawer that preserves focus and respects reduced motion. |
| `atelier-ui-assets` | Select a coherent visual vocabulary | Curate icons, images, illustrations, fonts and palettes with provenance and optimization. Example: consistent icons without unnecessary bundle growth. |
| `atelier-ui-audit` | Assess an interface before and after changes | Review screenshots, keyboard access, contrast, states, responsive behavior, performance and available tests. Example: diagnose mobile checkout regressions. |

Each folder under `skills/` contains its own `SKILL.md` and supporting resources.
Load only what the task needs. A typical workflow is director → design-system →
marketing or product → motion/assets as needed → audit. Use research when choosing
external resources. For an existing application, begin with audit to establish a baseline.

## Design principles

Visual identity should follow the product, its content and its users. The skills
favor original composition, considered typography, clear hierarchy, consistent
components and microinteractions that communicate state. Avoiding *AI slop* means
questioning stock solutions applied without context: identical heroes, card grids
and effects repeated across unrelated products.

Visual quality and engineering quality belong together. Semantic markup,
accessibility, responsive layouts, visible focus, contrast, performance and
maintainability are part of the design. Desktop and mobile should feel coherent,
with priorities adapted to the device. Preserve APIs, permissions and business
rules. Animation must not obstruct reading or replace functional feedback.

## Start from a clean setup

1. Install Python 3.10 or newer. On Windows, check `py --version`.
2. Install Git if you want to clone the repository; check `git --version`.
3. If needed, install and authenticate your agent using the official
   [Codex](https://developers.openai.com/codex/quickstart) or
   [Claude Code](https://code.claude.com/docs/en/setup) setup instructions.
   Installing only these skills does not require an agent CLI, Node.js or Git.
4. Get the source and enter the directory:

```powershell
git clone https://github.com/guilhermiranda25/atelier-ui-agent-kit.git
cd atelier-ui-agent-kit
```

You can also extract the release source archive or download its assets. Keep the
installer and `uiux-skillpack.zip` together. The portable ZIP contains the skills
and manifest, not the installers; both Python scripts are separate release assets
and are included in the repository. On Linux/macOS, replace `py` with `python3`.
The broader restoration workflow targets Windows.

## Codex installation and usage

Preview the destination, then install:

```powershell
py restaurar_codex.py --somente-uiux --dry-run
py restaurar_codex.py --somente-uiux
```

The default user-wide location is `%USERPROFILE%\.agents\skills\atelier-ui-*`.
These skills are available across projects. In the installer, `CODEX_HOME`
controls the CLI configuration location, not this skills destination.

For a single project:

```powershell
py restaurar_codex.py --somente-uiux --uiux-escopo projeto --uiux-projeto "C:\projects\my-app" --dry-run
py restaurar_codex.py --somente-uiux --uiux-escopo projeto --uiux-projeto "C:\projects\my-app"
```

This writes to `<project>\.agents\skills\`. Without `--uiux-projeto`, project
scope uses the current directory. Supply the path so you do not accidentally
install into the kit's clone. A missing project directory can be created.
Open a new Codex session in your project and inspect the installed files:

```powershell
Get-ChildItem "$env:USERPROFILE\.agents\skills\atelier-ui-*\SKILL.md"
# For project scope:
Get-ChildItem "C:\projects\my-app\.agents\skills\atelier-ui-*\SKILL.md"
```

Ask in the conversation: `Use atelier-ui-audit to review this frontend`. Clients
with explicit skill selection may also accept `$atelier-ui-audit`. Discovery and
UI behavior vary by version; see the [official skills guide](https://developers.openai.com/codex/skills).
The kit does not rely on a terminal command named `codex install-skill`.
`.codex-plugin/plugin.json` is a retained compatibility overlay, not a plugin
installation verified across all Codex clients. Use the Python installer as the primary method.

## Claude Code installation and usage

```powershell
py restaurar_claude.py --somente-uiux --dry-run
py restaurar_claude.py --somente-uiux

# Alternatively, install for one project:
py restaurar_claude.py --somente-uiux --uiux-escopo projeto --uiux-projeto "C:\projects\my-app" --dry-run
py restaurar_claude.py --somente-uiux --uiux-escopo projeto --uiux-projeto "C:\projects\my-app"
```

The user destination is `%USERPROFILE%\.claude\skills\`, or
`%CLAUDE_CONFIG_DIR%\skills\` when configured. Project scope writes to
`<project>\.claude\skills\`. Restart the session, inspect the `SKILL.md` files
with `Get-ChildItem` and request a skill by name. Agent authentication is separate.

### Alternative: marketplace plugin

Choose this method instead of copying the same skills with the Python installer:

```powershell
claude plugin marketplace add guilhermiranda25/atelier-ui-agent-kit
claude plugin install atelier-ui@atelier-ui-marketplace --scope user
```

For project scope, run from your project and use `--scope project`. The manifests
and installation flow were checked with Claude Code 2.1.325. The
[validation record](validation.md) distinguishes local and remote checks.
Plugin skills use a namespace, such as `/atelier-ui:atelier-ui-audit`; inspect
discovery in your installed client. The validator's missing-icon warning concerns
public directory submission and did not prevent this marketplace installation.

Copying skills, registering a plugin and configuring an MCP server are different
operations. The isolated installer neither registers a plugin nor configures MCPs.

## Conversation examples

```text
Use atelier-ui-director, atelier-ui-marketing and atelier-ui-audit to build a
landing page for an architecture consultancy. Develop a distinct editorial
identity, use verifiable content and responsive components, and add subtle
microinteractions. Do not require paid components.
```

```text
Use atelier-ui-product and atelier-ui-design-system to build a dashboard using
the existing data and API contracts. Prioritize indicators with units and time
context, filters, tables and readable charts. Audit keyboard and mobile use.
```

```text
Use atelier-ui-audit to diagnose this React application. Then improve hierarchy,
forms and navigation with atelier-ui-product. Preserve routes, business rules
and APIs. Validate existing flows before and after the changes.
```

```text
Use atelier-ui-design-system to inventory the project's styles and consolidate
semantic tokens, typography, spacing and component contracts. Migrate one
representative screen, record the decisions and check all its states.
```

```text
Use atelier-ui-audit to review accessibility and responsive behavior on the main
routes. Check focus, keyboard access, contrast, zoom and mobile overflow.
Report evidence and severity, fix the issues and rerun the affected checks.
```

```text
Use atelier-ui-motion to improve button feedback and existing drawer transitions.
Respect prefers-reduced-motion, preserve focus and keyboard access, and avoid
layout shifts. Measure what the environment allows and report the limits.
```

The [four worked scenarios](../examples/README.en.md) include goals, recommended
skills, prompts, expected outcomes and validation criteria. They are adaptable
recipes, not four finished applications shipped in the package.

## Releases, remote installation and integrity

The [GitHub repository](https://github.com/guilhermiranda25/atelier-ui-agent-kit)
is the official source. [Release v1.0.0](https://github.com/guilhermiranda25/atelier-ui-agent-kit/releases/tag/v1.0.0)
provides the ZIP, both installers, the manifest and `SHA256SUMS.txt`.
Once you have an installer from the clone or release assets, it can fetch the ZIP:

```powershell
py restaurar_codex.py --somente-uiux --uiux-url "https://github.com/guilhermiranda25/atelier-ui-agent-kit/releases/download/v1.0.0/uiux-skillpack.zip" --uiux-sha256 "d4b587421435cb15fb06a89ae8f62a4c02979e881768d5d61f62773325c8b7c0"
py restaurar_claude.py --somente-uiux --uiux-url "https://github.com/guilhermiranda25/atelier-ui-agent-kit/releases/download/v1.0.0/uiux-skillpack.zip" --uiux-sha256 "d4b587421435cb15fb06a89ae8f62a4c02979e881768d5d61f62773325c8b7c0"
```

Or set environment variables for the current PowerShell session:

```powershell
$env:UIUX_SKILL_URL = "https://github.com/guilhermiranda25/atelier-ui-agent-kit/releases/download/v1.0.0/uiux-skillpack.zip"
$env:UIUX_SKILL_SHA256 = "d4b587421435cb15fb06a89ae8f62a4c02979e881768d5d61f62773325c8b7c0"
py restaurar_codex.py --somente-uiux
# Clear them to use the local package again:
Remove-Item Env:UIUX_SKILL_URL
Remove-Item Env:UIUX_SKILL_SHA256
```

Command-line values override environment variables. `--uiux-origem` selects a
local ZIP or directory and takes precedence over the URL. With no explicit source,
URL or environment settings, the installer uses the adjacent ZIP, then falls back
to `skills/` with a manifest. The external digest verifies a ZIP, not a directory;
the internal manifest verifies file hashes in either case.

```powershell
Get-FileHash .\uiux-skillpack.zip -Algorithm SHA256
```

Compare a manual download against the trusted release checksum. An external
pinned digest identifies the expected bytes. The internal manifest detects
inconsistency but does not authenticate the source on its own. Downloading without
a digest remains supported for compatibility; always supply one in automation.
Update the URL and digest together. `--dry-run` only prints the plan; it does not
download the archive or validate its contents.

## Backups, recovery and updates

Only the eight `atelier-ui-*` directories are replaced. Existing content is copied
to `~/restauracao-agentes/<agent>-<timestamp>/uiux-previous/` first. That report
directory also contains `resultado.json` and `LEIA-ME.txt`. Exit code 2 means
there are pending issues. There is no previous backup for a newly installed skill.
Unrelated skills remain in place.

To recover a customization, close the agent and copy the skill's directory from
`uiux-previous/` back to its destination. To return to a known release, reinstall
that release's ZIP with its matching digest. On replacement failure, the installer
attempts to restore the previous content. Disk or permission failures can also
prevent recovery; inspect the retained backup if that happens. Do not publish
full-restoration reports or backups, which may contain personal configuration.

Update a clone without overwriting local work:

```powershell
git status --short
git pull --ff-only
py scripts/build_skillpack.py --check
py restaurar_codex.py --somente-uiux --dry-run
py restaurar_codex.py --somente-uiux
# Or for Claude:
py restaurar_claude.py --somente-uiux
```

Review the changelog and version first. For reproducible installs, use a clean
checkout at a published tag (`git switch --detach v1.0.0`) or a versioned release
URL and fixed digest. Avoid `latest` URLs in critical automation. Update both
environment variables or clear them to use the clone's ZIP. Restart the agent
after installation. Local changes to the eight skills are replaced, with backups.

If you use the Claude plugin, update through its manager instead of duplicating
the installation with Python:

```powershell
claude plugin marketplace update atelier-ui-marketplace
claude plugin update atelier-ui@atelier-ui-marketplace
```

## Full restoration is a separate operation

```powershell
py restaurar_codex.py --dry-run
py restaurar_claude.py --dry-run
# Run only if you want the full restoration catalog:
py restaurar_codex.py
py restaurar_claude.py
```

Without `--somente-uiux`, these scripts also restore the previous catalog of
plugins, skills, tools and MCP connections. They may install or update CLIs,
npm/pip dependencies and browser tooling. Besides Python, they require Git and
Node.js 22.20+. Some integrations need local programs and subsequent authentication.
The catalog consults external sources that can change. See `--help` for
`--sem-ferramentas`, `--manter-cli` and `--sem-uiux`. This broader workflow is
preserved but was not executed for this publication.

## Eleven independent UI/UX references

| Reference | Role in the kit |
| --- | --- |
| [21st.dev](https://21st.dev) | Component, pattern and theme research |
| [Designeer](https://designeer.xyz) | Composition and visual direction references |
| [React Bits](https://reactbits.dev) | Animation and React component patterns |
| [Magic UI](https://magicui.design) | Animated components and marketing interfaces |
| [Uiverse](https://uiverse.io) | Small HTML/CSS components and interaction states |
| [Hairline UI](https://hairlineui.com) | Component, template and interface references |
| [Lucide](https://lucide.dev) | Consistent functional iconography |
| [unDraw](https://undraw.co) | Contextual illustrations |
| [Shots](https://shots.so) | Presenting your own screenshots in mockups |
| [Coolors](https://coolors.co) | Exploring palettes for color tokens |
| [Fontshare](https://fontshare.com) | Typography research and hierarchy |

These are independent services, with no affiliation to the kit. Their libraries,
components and assets are not bundled. Materials remain subject to their own
licenses; free access does not authorize unrestricted redistribution. See
[sources and rights](sources-and-rights.md) and [optional integrations](integrations.md).
The supplied examples do not require paid components.

## Troubleshooting and limits

| Symptom | What to check |
| --- | --- |
| `py` is unavailable | Install Python, check `python --version` and use the correct executable. Use `python3` on Linux/macOS. |
| Launcher looks for a missing `python3.exe` | Use the current installer; `py -3.14` is an alternative if that version is installed. |
| A skill is missing | Check scope, destination and the eight `SKILL.md` files. Start a fresh session in the correct project and inspect your client's skill discovery. |
| Duplicate skills | Avoid installing the same skill globally, per project and as a plugin in the same agent. |
| Digest or manifest mismatch | Check the version, URL, environment variables and checksum. Do not bypass the error; fetch the trusted release again. |
| ZIP not found | Keep it beside the installer or provide a URL and digest; a local source directory requires its manifest. |
| Download failure | Check networking, proxy, TLS certificates and the asset URL. Do not disable TLS validation. |
| Permission error or locked files | Close processes holding the files and verify write access to the destination and backup directory. |

The installers do not execute archive contents. They reject traversal, input
symlinks, duplicates, unsafe Windows filenames and oversized inputs. Skills still
contain instructions: review their source. Contrast and structure scripts are
advisory, not WCAG certification or SAST. React and Playwright examples need the
consumer project's stack and routes. See [validation](validation.md) for evidence
and [maintenance](maintenance.md) for the release process.
