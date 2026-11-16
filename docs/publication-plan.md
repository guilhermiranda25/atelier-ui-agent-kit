# Publication plan — 1.0.0

Source: the supplied package, inspected on Windows on 2026-11-16. The GitHub
repository was empty, with no default branch or remote refs. Preserve all eight
skills, their standalone resources, both restoration catalogs and compatibility
manifests. Use `main` for the initial publication.

1. Record the initial audit and run the existing offline tests before edits.
2. Correct proven installer/test problems with regression tests: Windows test
   isolation, partial-copy rollback, malformed manifests and unsafe archive names.
   Keep the two standalone installers independently usable.
3. Add a deterministic package builder and CI checks for source/archive/checksum
   consistency. Test Python 3.10 and 3.14 on Windows and Linux without global installs.
4. Keep the root README short. Add complete Portuguese and English guides,
   practical examples, maintenance instructions and an honest validation record.
   Preserve the original technical references and examples.
5. Validate manifests with the installed Claude CLI; test marketplace installation
   in an isolated configuration. Verify documented commands against CLI help and
   official documentation. Do not run full restoration or authenticated agent tasks.
6. Review the diff, tracked file inventory, licenses, links and sensitive data.
   Commit, push, tag and publish the validated ZIP and checksums as v1.0.0.
   Download the published assets again and verify their hashes and installation.

Review focus: replacement failures must restore all prior files; invalid ZIPs and
manifests must fail before touching skills; tests must never use the real home;
source files, manifests and release bytes must agree; distinguish validated
installation from untested agent execution and optional integrations.

Execution proceeds inline under the user's explicit authorization for the full
publication flow. No routine approval gates or redesign of the original skills.
