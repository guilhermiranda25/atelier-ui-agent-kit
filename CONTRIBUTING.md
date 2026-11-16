# Contributing

Report concrete problems with the relevant skill, installer command, client and
Python version, operating system, expected behavior and a minimal reproduction.
Redact credentials and personal paths from logs. For security issues, see
[SECURITY.md](SECURITY.md).

Keep changes focused. Preserve the eight independent skills, existing CLI flags,
backups and both full-restoration catalogs. Add regression tests for behavioral
fixes. Do not add third-party code or assets without compatible licensing and
attribution. Document optional dependencies rather than installing them by default.

Follow the [maintenance guide](docs/maintenance.md), regenerate release artifacts
when required and run `py -m unittest discover -s tests -v` and
`py scripts/build_skillpack.py --check`. No global installs or agent authentication
are needed for the tests. Review Portuguese and English guides together.

Contribuições em português são bem-vindas. Descreva o problema e a reprodução,
preserve compatibilidade e mantenha os dois guias tecnicamente equivalentes.
Não envie backups, configurações pessoais ou credenciais nos exemplos e logs.
