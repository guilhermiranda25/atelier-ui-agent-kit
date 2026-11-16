# Security

The initial supported release is 1.0.0. Use a versioned release URL and its fixed
SHA-256 digest. An internal file manifest is an integrity check, not a signature
or proof of publisher identity. Review downloaded skills and scripts before use.

Use GitHub's **Report a vulnerability** option if it is available for this
repository. If no private channel is available, open an issue requesting a
private contact without publishing exploit details or credentials. Do not attach
full user configuration or restoration backups.

Installers validate archives before replacing skills and retain previous skill
content for recovery. They cannot guarantee recovery from every disk failure,
concurrent filesystem change or permission problem. They are not a sandbox for
untrusted agent instructions. Full restoration can install external tools and
configure MCP connections; inspect its dry-run separately.

Para relatar uma falha, prefira o canal privado do GitHub quando disponível.
Na ausência dele, solicite contato privado sem expor detalhes exploráveis ou
dados pessoais em uma issue pública.
