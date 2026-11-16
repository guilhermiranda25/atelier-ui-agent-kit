#!/usr/bin/env python
"""Build deterministic release artifacts, or verify them without writing files."""
import argparse
import hashlib
import io
import json
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def encoded(obj):
    return (json.dumps(obj, ensure_ascii=False, indent=2) + '\n').encode('utf-8')


def build(check=False):
    version = (ROOT/'VERSION').read_text().strip()
    if not re.fullmatch(r'\d+\.\d+\.\d+', version):
        raise ValueError('VERSION must contain a semantic version')
    manifest = json.loads((ROOT/'skillpack-manifest.json').read_text(encoding='utf-8'))
    paths = sorted((p for p in (ROOT/'skills').rglob('*')
                    if p.is_file() and '__pycache__' not in p.parts),
                   key=lambda p: p.relative_to(ROOT).as_posix())
    if any(p.is_symlink() for p in (ROOT/'skills').rglob('*')):
        raise ValueError('Symlinks are not distributable')
    names = {p.parent.name for p in paths if p.name == 'SKILL.md'}
    if names != set(manifest['skills']) or len(names) != 8:
        raise ValueError('Expected exactly the original eight skills')
    files = {p.relative_to(ROOT).as_posix(): p.read_bytes() for p in paths}
    for slug in manifest['skills']:
        text = files[f'skills/{slug}/SKILL.md'].decode('utf-8')
        if not text.startswith(f'---\nname: {slug}\n') or '\ndescription: ' not in text:
            raise ValueError(f'Invalid skill metadata: {slug}')
    manifest['version'] = version
    manifest['files'] = {name: hashlib.sha256(data).hexdigest() for name, data in files.items()}
    artifacts = {'skillpack-manifest.json': encoded(manifest)}
    stream = io.BytesIO()
    # ZIP_STORED avoids differences between zlib versions across operating systems.
    with zipfile.ZipFile(stream, 'w', compression=zipfile.ZIP_STORED) as archive:
        for name, data in sorted({**files, **artifacts}.items()):
            info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    artifacts['uiux-skillpack.zip'] = stream.getvalue()
    for name in ('plugin.json', '.claude-plugin/plugin.json', '.codex-plugin/plugin.json'):
        obj = json.loads((ROOT/name).read_text(encoding='utf-8'))
        obj['version'] = version
        artifacts[name] = encoded(obj)
    checksum_names = ('uiux-skillpack.zip', 'skillpack-manifest.json', 'restaurar_codex.py', 'restaurar_claude.py')
    artifacts['SHA256SUMS.txt'] = ''.join(
        hashlib.sha256(artifacts[name] if name in artifacts else (ROOT/name).read_bytes()).hexdigest()
        + '  ' + name + '\n' for name in checksum_names).encode('ascii')
    stale = []
    for name, data in artifacts.items():
        path = ROOT/name
        if check:
            if not path.is_file() or path.read_bytes() != data:
                stale.append(name)
        else:
            path.write_bytes(data)
    if stale:
        raise ValueError('Stale distribution artifacts: ' + ', '.join(stale))
    print(('Verified' if check else 'Built') + ' Atelier UI Agent Kit ' + version)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail on stale artifacts; do not write anything')
    args = parser.parse_args()
    try:
        build(args.check)
    except (ValueError, OSError, KeyError) as error:
        parser.exit(1, str(error) + '\n')
