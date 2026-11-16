# Changelog

## 1.0.0 ? 2026-11-16

Initial public release by Guilherme Miranda.

- Preserves eight original UI/UX skills, their supporting resources, examples and both full-restoration catalogs.
- Adds complete Portuguese and English installation/usage guides and four practical work recipes.
- Supports isolated user/project installation, local or HTTPS archives, SHA-256 verification and previous-skill backups.
- Fixes partial-copy and partial-deletion rollback, malformed manifest handling and Windows filename aliases.
- Corrects Windows test isolation and Python launcher compatibility; isolated installation backs up only replaced skills.
- Quotes the assets skill's description for valid YAML metadata without changing its workflow.
- Adds centralized VERSION, deterministic packaging, release checksums and an offline Windows/Linux Python 3.10/3.14 CI matrix.
- Validates Claude plugin/marketplace manifests and isolated marketplace installation.

Validation: 18 offline tests passed locally on Windows with Python 3.14.6. See
[validation record](docs/validation.md) and GitHub Actions for exact scope and
remote results. Full restoration, authenticated agent tasks, third-party MCPs
and frontend examples were not executed.

Documenta??o em portugu?s e ingl?s, instru??es de atualiza??o e limites de
compatibilidade est?o nos guias. A licen?a MIT cobre o conte?do autoral;
refer?ncias independentes mant?m seus pr?prios termos.
