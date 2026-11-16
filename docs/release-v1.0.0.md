Atelier UI Agent Kit 1.0.0 provides eight independent UI/UX skills for Codex and
Claude Code, with Portuguese and English guides and four practical work recipes.

- Preserves the original skill content, supporting resources and both restoration catalogs.
- Includes isolated/project installation, backups, HTTPS download and SHA-256 verification.
- Corrects partial replacement rollback, Windows launcher handling and test isolation.
- Adds deterministic packaging and offline CI checks for Windows/Linux on Python 3.10/3.14.

Download the installer for your agent and `uiux-skillpack.zip`, keep them together,
then run `py restaurar_codex.py --somente-uiux` or
`py restaurar_claude.py --somente-uiux`. Add `--dry-run` to preview the destination.
`SHA256SUMS.txt` covers the ZIP, manifest and both installers.

The ZIP's SHA-256 is:
`d4b587421435cb15fb06a89ae8f62a4c02979e881768d5d61f62773325c8b7c0`.

See the guides and validation record in the source for tested behavior and limits.
Full restoration, authenticated agent tasks, external MCP services and frontend
example execution are separate from the isolated installer tests.

Documentação em português: `docs/README.pt-BR.md`. Instale com `--somente-uiux`
para obter apenas as oito skills; a execução sem essa opção restaura um catálogo
mais amplo de ferramentas e integrações.
