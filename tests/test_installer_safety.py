"""Exercise both independent installers without using the real user profile."""
import argparse
import importlib.util
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def load(agent):
    spec = importlib.util.spec_from_file_location('restore_' + agent, ROOT / f'restaurar_{agent}.py')
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class InstallerSafetyTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)

    def install(self, module, source=None):
        args = argparse.Namespace(uiux_origem=str(source) if source else None,
                                  uiux_url=None, uiux_sha256=None, dry_run=False)
        with patch.dict('os.environ', {'UIUX_SKILL_URL': '', 'UIUX_SKILL_SHA256': ''}):
            return module.uiux_skill_install(args, self.base/'dest', self.base/'backup', ROOT)

    def test_partial_copy_failure_restores_every_old_skill(self):
        for agent in ('claude', 'codex'):
            with self.subTest(agent=agent), tempfile.TemporaryDirectory() as tmp:
                self.base = Path(tmp)
                module = load(agent)
                for slug in module.UIUX_SKILL_NAMES:
                    old = self.base/'dest'/slug
                    old.mkdir(parents=True)
                    (old/'local.txt').write_text(slug)
                original_move = shutil.move
                calls = []

                def failing_move(src, dst):
                    calls.append(dst)
                    if len(calls) == 2:
                        Path(dst).mkdir()
                        (Path(dst)/'partial.txt').write_text('partial copy')
                        raise OSError('simulated disk failure')
                    return original_move(src, dst)

                with patch.object(module.shutil, 'move', side_effect=failing_move):
                    ok, _, _ = self.install(module)
                self.assertFalse(ok)
                for slug in module.UIUX_SKILL_NAMES:
                    target = self.base/'dest'/slug
                    self.assertEqual((target/'local.txt').read_text(), slug)
                    self.assertEqual([p.name for p in target.iterdir()], ['local.txt'])

    def test_non_object_manifest_fails_without_writing_skills(self):
        for agent in ('claude', 'codex'):
            source = self.base/f'{agent}.zip'
            with zipfile.ZipFile(source, 'w') as archive:
                archive.writestr('skillpack-manifest.json', '[]')
            ok, _, _ = self.install(load(agent), source)
            self.assertFalse(ok)
            self.assertFalse((self.base/'dest').exists())

    def test_windows_aliases_and_reserved_names_are_rejected(self):
        for agent in ('claude', 'codex'):
            for suffix in ('CON.txt', 'note.', 'note ', 'a<.txt', 'a|.txt', 'NOTE.md'):
                with self.subTest(agent=agent, suffix=suffix):
                    source = self.base/'unsafe.zip'
                    with zipfile.ZipFile(ROOT/'uiux-skillpack.zip') as original:
                        manifest = json.loads(original.read('skillpack-manifest.json'))
                        payloads = {name: original.read(name) for name in manifest['files']}
                    # Case-insensitive duplicate and Win32 aliases must fail on Linux too.
                    import hashlib
                    for name in ('note.md', suffix):
                        path = 'skills/atelier-ui-director/' + name
                        payloads[path] = b'example'
                        manifest['files'][path] = hashlib.sha256(b'example').hexdigest()
                    with zipfile.ZipFile(source, 'w') as archive:
                        for name, data in payloads.items():
                            archive.writestr(name, data)
                        archive.writestr('skillpack-manifest.json', json.dumps(manifest))
                    ok, _, _ = self.install(load(agent), source)
                    self.assertFalse(ok)
                    self.assertFalse((self.base/'dest').exists())

    def test_isolated_install_does_not_copy_unrelated_configuration(self):
        for agent in ('claude', 'codex'):
            module = load(agent)
            home = self.base/agent
            config = home/('.claude' if agent == 'claude' else '.codex')
            config.mkdir(parents=True)
            (config/'settings.json').write_text('{"private": true}')
            unrelated = home/'.agents'/'skills'/'unrelated'
            unrelated.mkdir(parents=True)
            (unrelated/'private.txt').write_text('private')
            args = argparse.Namespace(dry_run=False, somente_uiux=True)
            key = 'CLAUDE_CONFIG_DIR' if agent == 'claude' else 'CODEX_HOME'
            with patch.object(module.Path, 'home', return_value=home), patch.dict('os.environ', {key: str(config)}):
                restore = module.Restore(args)
                self.assertTrue(restore.prepare())
            self.assertEqual(list(restore.out.iterdir()), [])
            self.assertFalse(restore.work.exists())

    def test_partial_delete_failure_restores_old_skill(self):
        for agent in ('claude', 'codex'):
            with self.subTest(agent=agent), tempfile.TemporaryDirectory() as tmp:
                self.base = Path(tmp)
                module = load(agent)
                old = self.base/'dest'/'atelier-ui-director'
                old.mkdir(parents=True)
                (old/'one.txt').write_text('one')
                (old/'two.txt').write_text('two')
                original_remove = shutil.rmtree
                failed = False

                def failing_remove(path, *args, **kwargs):
                    nonlocal failed
                    if Path(path) == old and not failed:
                        failed = True
                        (old/'one.txt').unlink()
                        raise OSError('simulated partial delete')
                    return original_remove(path, *args, **kwargs)

                with patch.object(module.shutil, 'rmtree', side_effect=failing_remove):
                    ok, _, _ = self.install(module)
                self.assertFalse(ok)
                self.assertEqual((old/'one.txt').read_text(), 'one')
                self.assertEqual((old/'two.txt').read_text(), 'two')

    def test_corrupt_and_tampered_archives_fail_before_installation(self):
        for agent in ('claude', 'codex'):
            for kind in ('not-zip', 'missing-manifest', 'bad-file-hash', 'duplicate', 'oversized-file'):
                with self.subTest(agent=agent, kind=kind):
                    source = self.base/'invalid.zip'
                    if kind == 'not-zip':
                        source.write_bytes(b'not a zip')
                    else:
                        with zipfile.ZipFile(ROOT/'uiux-skillpack.zip') as original:
                            payloads = {name: original.read(name) for name in original.namelist()}
                        path = 'skills/atelier-ui-director/SKILL.md'
                        if kind == 'missing-manifest':
                            del payloads['skillpack-manifest.json']
                        elif kind == 'bad-file-hash':
                            payloads[path] += b'changed'
                        elif kind == 'oversized-file':
                            payloads[path] = b'x' * (2*1024*1024+1)
                        with zipfile.ZipFile(source, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
                            for name, data in payloads.items():
                                archive.writestr(name, data)
                            if kind == 'duplicate':
                                import warnings
                                with warnings.catch_warnings():
                                    warnings.simplefilter('ignore', UserWarning)
                                    archive.writestr(path, payloads[path])
                    ok, _, _ = self.install(load(agent), source)
                    self.assertFalse(ok)
                    self.assertFalse((self.base/'dest').exists())

    def test_unrelated_skill_survives_successful_installation(self):
        module = load('codex')
        old = self.base/'dest'/'another-skill'
        old.mkdir(parents=True)
        (old/'notes.txt').write_text('keep')
        self.assertTrue(self.install(module)[0])
        self.assertEqual((old/'notes.txt').read_text(), 'keep')


if __name__ == '__main__':
    unittest.main()
