# Maintenance and releases

[English guide](README.en.md) · [Guia em português](README.pt-BR.md)

## Source of truth

`skills/` is the editable source. Keep the eight skills independently usable;
their embedded scripts and assets intentionally duplicate small standalone
examples. Do not remove those copies merely to deduplicate the repository.
`VERSION` owns the release number. `scripts/build_skillpack.py` propagates it to
the distribution manifest and all three plugin manifests, calculates file hashes,
builds the portable ZIP and writes `SHA256SUMS.txt`.

The ZIP has fixed timestamps, sorted entries and stored bytes rather than
platform-dependent compression, so repeated builds are byte-identical. The
manifest's date is the release date: update it deliberately for a new release.
The ZIP contains skills and its integrity manifest; it does not contain the two
independent installers. Those are released separately with their own checksums.

Each installer remains a standalone file so users can restore from a remote URL
without installing a Python package. The `BEGIN/END ATELIER UI INSTALLER` blocks
must stay synchronized. Preserve both full-restoration catalogs. They are broader
than this kit and must not run in CI.

## Version policy

- Patch: compatible corrections to guidance, documentation or installer behavior.
- Minor: additive workflows or compatible capabilities.
- Major: incompatible CLI changes, removed skills or changed installation contracts.

Never replace an existing release's bytes under the same version. Publish a new
version, keep old assets available and update URLs and digests together. Installed
skills have no dependency on GitHub; GitHub is the distribution and update source.

## Prepare a release

Work in a clean clone. Review the change and update `VERSION`, the manifest date,
`CHANGELOG.md`, examples and guides as needed. Do not edit the generated file-hash
inventory manually.

```powershell
py scripts/build_skillpack.py
py scripts/build_skillpack.py --check
py -m unittest discover -s tests -v
claude plugin validate .claude-plugin/plugin.json
claude plugin validate .claude-plugin/marketplace.json
git diff --check
git status --short
```

Check the two language guides for matching technical information. If the archive
changes, update their pinned digest and release URLs. Review all staged files for
private configuration, credentials and backups. Avoid publishing `resultado.json`,
`.env`, `.agent-restore/` or `restauracao-agentes/` from a user's machine.

Commit and push without force. Wait for the Windows/Linux Python matrix to pass
on the exact commit, then tag that commit and publish its artifacts. Example for
the initial release (do not rerun against an existing tag):

```powershell
git tag -a v1.0.0 -m "Atelier UI Agent Kit 1.0.0"
git push origin v1.0.0
gh release create v1.0.0 uiux-skillpack.zip SHA256SUMS.txt skillpack-manifest.json restaurar_codex.py restaurar_claude.py --verify-tag --title "Atelier UI Agent Kit 1.0.0" --notes-file docs/release-v1.0.0.md
```

After publication, download the assets, verify every listed hash and perform
isolated installations from the published HTTPS URL. Confirm that the tag resolves
to the tested commit. Test a remote Claude marketplace installation in a temporary
configuration if that route is documented. Record evidence and remaining limits.

CI is a status check, not branch protection by itself. Require its matrix jobs in
GitHub repository rules if your account supports that policy; the workflow does
not change security settings or claim to prevent administrators bypassing checks.

## Maintenance notes in Portuguese

Edite as skills originais e a versão em `VERSION`; gere os artefatos com o script
acima. Atualize data do manifesto, changelog, documentação e hashes fixos dos
exemplos. O comando `--check` não grava: falha se fonte, ZIP, manifesto, versões ou
checksums divergirem. Valide o commit exato no CI, publique uma nova tag e mantenha
os assets anteriores. Para atualizar outra máquina, use `git pull --ff-only` e
reinstale, ou escolha uma release com URL e hash fixos. Não execute a restauração
completa para simplesmente atualizar o Atelier UI.
