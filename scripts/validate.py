#!/usr/bin/env python3
"""Validate skill metadata and pinned NVIDIA source paths."""

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PINNED_LINK = re.compile(r'https://github\.com/NVIDIA/cuda-rust/blob/([0-9a-f]{40})/([^\s)]+)')
NAME = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*\Z')


def validate(root, source):
    errors = []
    index = root / 'llms.txt'
    if not index.is_file() or not index.read_text().startswith('# '):
        errors.append('llms.txt is missing or has no H1')
    skills = sorted(root.glob('*/SKILL.md'))
    if not skills:
        errors.append('No skills found')
    files = ([index] if index.is_file() else []) + skills
    for skill in skills:
        text = skill.read_text()
        parts = text.split('---\n', 2)
        if len(parts) != 3 or parts[0] != '':
            errors.append(f'{skill}: missing YAML frontmatter')
            continue
        fields = dict(re.findall(r'^(name|description):\s*(.+)$', parts[1], re.MULTILINE))
        name = fields.get('name', '')
        if not NAME.fullmatch(name) or name != skill.parent.name or len(name) > 64:
            errors.append(f'{skill}: invalid skill name')
        description = fields.get('description', '').strip()
        if not description or len(description) > 1024:
            errors.append(f'{skill}: invalid description')
    links = set()
    for file in files:
        links.update(PINNED_LINK.findall(file.read_text()))
    if not links:
        errors.append('No pinned NVIDIA documentation links found')
    if source is not None:
        for rev, path in sorted(links):
            result = subprocess.run(['git', '-C', str(source), 'cat-file', '-e', f'{rev}:{path}'], capture_output=True)
            if result.returncode:
                errors.append(f'Missing NVIDIA source: {rev}:{path}')
    return errors, len(skills), len(links)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, help='local NVIDIA/cuda-rust Git checkout; checks pinned paths')
    args = parser.parse_args()
    errors, skills, links = validate(ROOT, args.source)
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'Validated {skills} skills and {links} pinned links' + (' against source checkout' if args.source else ' (source paths not checked)'))
    return 0


if __name__ == '__main__':
    sys.exit(main())
