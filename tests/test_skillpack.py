"""Self-contained offline tests for bundled restoration, integrity and path security."""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT=Path(__file__).resolve().parents[1]
SHA=hashlib.sha256((ROOT/'uiux-skillpack.zip').read_bytes()).hexdigest()
SLUGS=('atelier-ui-director','atelier-ui-research','atelier-ui-design-system','atelier-ui-marketing',
       'atelier-ui-product','atelier-ui-motion','atelier-ui-assets','atelier-ui-audit')

class SkillpackTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base=Path(self.tmp.name)
        self.home=self.base/'home';self.home.mkdir()
        self.project=self.base/'projeto com espaços e acentos'
    def run_tool(self,agent='claude',*extra):
        env=os.environ.copy();env['HOME']=str(self.home);env['USERPROFILE']=str(self.home)
        env['CLAUDE_CONFIG_DIR']=str(self.home/'.claude')
        env['CODEX_HOME']=str(self.home/'.codex')
        env['PYTHONUTF8']='1'
        env.pop('UIUX_SKILL_URL',None);env.pop('UIUX_SKILL_SHA256',None)
        command=[sys.executable,str(ROOT/f'restaurar_{agent}.py'),'--somente-uiux',
                 '--uiux-escopo','projeto','--uiux-projeto',str(self.project),*extra]
        return subprocess.run(command,text=True,encoding='utf-8',capture_output=True,env=env,timeout=30)
    def test_claude_and_codex_install(self):
        for name,folder in [('claude','.claude'),('codex','.agents')]:
            p=self.run_tool(name,'--uiux-sha256',SHA)
            self.assertEqual(p.returncode,0,p.stdout+p.stderr)
            root=self.project/folder/'skills'
            for slug in SLUGS:
                self.assertTrue((root/slug/'SKILL.md').is_file())
            self.assertEqual(len(list(root.glob('atelier-ui-*/SKILL.md'))),8)
    def test_dry_run_does_not_write(self):
        p=self.run_tool('claude','--dry-run')
        self.assertEqual(p.returncode,0,p.stdout+p.stderr)
        self.assertFalse(self.project.exists())
        self.assertEqual(list(self.home.iterdir()),[])
    def test_user_scope_respects_temporary_profile(self):
        for agent, folder in [('claude', '.claude'), ('codex', '.agents')]:
            p=self.run_tool(agent, '--uiux-escopo', 'usuario')
            self.assertEqual(p.returncode,0,p.stdout+p.stderr)
            root=self.home/folder/'skills'
            self.assertEqual(len(list(root.glob('atelier-ui-*/SKILL.md'))),8)
            self.assertFalse(self.project.exists())
    def test_wrong_digest_fails_closed(self):
        p=self.run_tool('claude','--uiux-sha256','0'*64)
        self.assertEqual(p.returncode,2,p.stdout+p.stderr)
        self.assertFalse((self.project/'.claude'/'skills'/'atelier-ui-director').exists())
    def test_reinstall_backs_up_old_skill(self):
        self.assertEqual(self.run_tool().returncode,0)
        mark=self.project/'.claude'/'skills'/'atelier-ui-director'/'local-personal-note.txt'
        mark.write_text('preserve backup')
        p=self.run_tool()
        self.assertEqual(p.returncode,0,p.stdout+p.stderr)
        backups=list(self.home.glob('restauracao-agentes/claude-*/uiux-previous/atelier-ui-director/local-personal-note.txt'))
        self.assertEqual(len(backups),1)
        self.assertEqual(backups[0].read_text(),'preserve backup')
        self.assertFalse(mark.exists())
    def test_rejects_path_traversal(self):
        malicious=self.base/'evil.zip'
        with zipfile.ZipFile(malicious,'w') as z:
            z.writestr('../injected.txt','evil')
            z.writestr('skillpack-manifest.json','{}')
        p=self.run_tool('claude','--uiux-origem',str(malicious))
        self.assertEqual(p.returncode,2,p.stdout+p.stderr)
        self.assertFalse((self.base/'injected.txt').exists())
        self.assertFalse((self.project/'.claude'/'skills'/'atelier-ui-director').exists())
    def test_rejects_symlink_zip(self):
        import stat
        malicious=self.base/'symlink.zip'
        with zipfile.ZipFile(malicious,'w') as z:
            i=zipfile.ZipInfo('skills/atelier-ui-director/evil-link')
            i.create_system=3
            i.external_attr=(stat.S_IFLNK|0o777)<<16
            z.writestr(i,'../../anywhere')
            z.writestr('skillpack-manifest.json','{}')
        p=self.run_tool('codex','--uiux-origem',str(malicious))
        self.assertEqual(p.returncode,2,p.stdout+p.stderr)
    def test_expected_manifest_is_consistent(self):
        obj=json.loads((ROOT/'skillpack-manifest.json').read_text())
        self.assertEqual(set(obj['skills']),set(SLUGS))
        for path,digest in obj['files'].items():
            self.assertEqual(hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),digest)
    def test_modules_compile(self):
        for script in ('restaurar_claude.py','restaurar_codex.py','scripts/check_contrast.py','scripts/audit_structure.py'):
            p=subprocess.run([sys.executable,'-m','py_compile',str(ROOT/script)],capture_output=True,text=True)
            self.assertEqual(p.returncode,0,p.stderr)

if __name__=='__main__':unittest.main()
