# Validation record — 1.0.0

Date: 2026-11-16. Local environment: Windows, Python 3.14.6, Codex CLI 0.169.0
and Claude Code 2.1.325. No full restoration or global dependency installation
was performed for publication. Installation tests use temporary profiles/projects.

## Initial audit

- The supplied directory was accessible. It was not a Git checkout. The authorized
  GitHub repository was empty and had no default branch or refs at inspection.
- All eight original skills, 29 skill files, their references/assets/scripts,
  two standalone restorers, four manifests, examples, MIT license and changelog
  were present. The original ZIP matched its file manifest and checksum.
- The initial eight-test suite had one failure on Windows: backup assertions
  looked under `HOME`, while Python used `USERPROFILE`. This also meant the
  initial tests wrote restoration reports/backups outside their temporary home.
  Those runtime files were not part of the package and are not published.
- The original ZIP's SHA-256 was
  `ce3b5fe5c6da87c6503dea2779198be8fb0e91752a105426ec21f673717e668e`.
- Repeated small resources are intentional: installed skills need their own
  scripts/assets. All original skill content is retained; the assets skill's
  description was quoted to make its YAML metadata valid. Its instructions
  were not replaced. The helper scripts, including their skill-local copies, also
  received the same Windows-compatible shebang fix; their bodies are unchanged.
  The distribution was rebuilt after these corrections.

## Corrections and checks

| Area | Evidence |
| --- | --- |
| Offline suite | `py -m unittest discover -s tests -v`: 18 tests passed locally on Windows/Python 3.14.6. |
| Installation | Both agents install eight skills into temporary project paths containing spaces and accents. |
| Isolation | Tests set `HOME`, `USERPROFILE` and both configuration roots. Isolated restoration no longer copies unrelated user configuration/skills. |
| Backup/recovery | Reinstallation retains previous local files; injected partial copy and partial deletion failures restore previous skill content. |
| Input validation | Wrong digest, non-object manifest, corrupt ZIP, missing manifest, altered files, duplicate entries, oversized files, traversal, symlinks and unsafe Windows names are rejected. |
| Dry-run | Does not write the project or temporary home. Actual `py restaurar_*.py --somente-uiux --dry-run` commands execute on Windows. Dry-run is a plan, not archive verification. |
| Compatibility | Standalone installers compile. Windows launcher issue corrected by using `python` in their shebang. Existing flags and full restoration catalogs retained. |
| Distribution | `py scripts/build_skillpack.py --check`; tests compare full source/ZIP inventory, file bytes and every listed checksum. Repeated builds produce identical bytes and stale source is detected without modifying artifacts. |
| Claude manifests | `claude plugin validate` accepts both plugin and marketplace. Missing-icon warning relates to public directory submission. |
| Local marketplace | Registration and installation succeeded in a temporary Claude configuration; eight `SKILL.md` files found in its cache. |
| CI | Workflow runs package checks and the offline suite on Windows/Linux with Python 3.10 and 3.14. Remote run results are available in GitHub Actions after push. |

Both helper commands were also executed on Windows: the contrast checker returned
21.00:1 for black/white, and the advisory structural scanner found zero matches
in the reference examples. These checks do not establish application accessibility.

## Review boundaries

Source and archive inventories were inspected for private configuration, credentials,
personal backups and unexpected binaries. No credentials or personal backup files
were identified in the distribution. This is a source review, not a guarantee that
every possible secret pattern or filesystem race has been ruled out. Runtime
reports from full restoration can contain personal configuration: do not publish them.

Official Codex skill documentation and installed CLI help were consulted for
installation guidance. Claude marketplace commands were checked with local help
and the [official marketplace guide](https://code.claude.com/docs/en/plugin-marketplaces).
Codex user/project skill locations are documented in the
[official skills guide](https://developers.openai.com/codex/skills).

The eleven reference URLs were reviewed. Most returned their expected pages;
Designeer could not be retrieved by the research tool, Coolors returned HTTP 403,
and Fontshare exposed a JavaScript shell. These are limitations of this link review,
not proof those services are unavailable. Third-party terms must be checked again
when selecting a specific component, font or illustration.

## Not established by these tests

- Authenticated Codex/Claude task execution, automatic skill selection or UI quality
  on a real consuming application.
- Codex plugin registration through the compatibility manifest.
- Full restoration of the historical catalog, third-party CLI installation,
  authentication or live MCP calls.
- Running the React/TypeScript/Playwright examples, browser rendering, WCAG
  compliance or measured frontend performance. No frontend application is bundled.
- Complete Windows compatibility across all versions, junction/reparse-point and
  concurrent filesystem scenarios, or guaranteed recovery from disk/permission failures.

A passing Linux run alone does not establish Windows compatibility. The matrix
provides additional evidence for the specific OS/Python combinations it executes.
See release assets for the final distribution checksums and GitHub Actions for
the status of the tagged commit.

## Resumo em português

As oito skills e os dois catálogos originais foram preservados. A suíte inicial
revelou falha de isolamento no Windows; ela foi corrigida junto com rollback
parcial, validação de manifesto e nomes de arquivo. Os 18 testes locais passaram.
O marketplace local instalou as oito skills em configuração temporária. A execução
autenticada dos agentes, restauração completa, MCPs e exemplos frontend não foi
realizada. Consulte Actions e a release para a evidência remota do commit publicado.
