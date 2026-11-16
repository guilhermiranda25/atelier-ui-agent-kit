"""Release gates: source, archive, metadata and checksums must agree."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]


class DistributionTests(unittest.TestCase):
    def test_archive_matches_complete_source_inventory_and_checksum(self):
        manifest = json.loads((ROOT/'skillpack-manifest.json').read_text(encoding='utf-8'))
        source = {p.relative_to(ROOT).as_posix(): p.read_bytes()
                  for p in (ROOT/'skills').rglob('*') if p.is_file() and '__pycache__' not in p.parts}
        self.assertEqual(set(manifest['files']), set(source))
        with zipfile.ZipFile(ROOT/'uiux-skillpack.zip') as archive:
            self.assertEqual(set(archive.namelist()), set(source) | {'skillpack-manifest.json'})
            self.assertEqual(len(archive.namelist()), len(source)+1)
            self.assertEqual(archive.read('skillpack-manifest.json'), (ROOT/'skillpack-manifest.json').read_bytes())
            for name, data in source.items():
                self.assertEqual(archive.read(name), data)
        for line in (ROOT/'SHA256SUMS.txt').read_text().splitlines():
            digest, name = line.split('  ', 1)
            self.assertEqual(hashlib.sha256((ROOT/name).read_bytes()).hexdigest(), digest)

    def test_builder_is_reproducible_and_detects_changed_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            checkout = Path(tmp)
            for folder in ('skills', 'scripts', '.claude-plugin', '.codex-plugin'):
                shutil.copytree(ROOT/folder, checkout/folder, ignore=shutil.ignore_patterns('__pycache__'))
            for name in ('VERSION', 'plugin.json', 'skillpack-manifest.json', 'restaurar_codex.py', 'restaurar_claude.py'):
                shutil.copy2(ROOT/name, checkout/name)
            command = [sys.executable, str(checkout/'scripts/build_skillpack.py')]
            first = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(first.returncode, 0, first.stdout+first.stderr)
            manifest = json.loads((checkout/'skillpack-manifest.json').read_text(encoding='utf-8'))
            # Canonical string order must not depend on WindowsPath/PosixPath ordering.
            self.assertEqual(list(manifest['files']), sorted(manifest['files']))
            archive = (checkout/'uiux-skillpack.zip').read_bytes()
            second = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(second.returncode, 0, second.stdout+second.stderr)
            self.assertEqual((checkout/'uiux-skillpack.zip').read_bytes(), archive)
            (checkout/'skills/atelier-ui-director/SKILL.md').write_text('changed')
            check = subprocess.run(command+['--check'], capture_output=True, text=True)
            self.assertNotEqual(check.returncode, 0)
            self.assertEqual((checkout/'uiux-skillpack.zip').read_bytes(), archive)


if __name__ == '__main__':
    unittest.main()
