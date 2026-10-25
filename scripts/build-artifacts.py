#!/usr/bin/env python3
"""Merge the per-subject artifact fragments and diagram labels into one registry.

Run: python3 scripts/build-artifacts.py
"""
import glob
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARTS = os.path.join(ROOT, 'data', 'artifacts', 'parts')
LABELS = os.path.join(ROOT, 'data', 'artifacts', 'labels.json')
OUT = os.path.join(ROOT, 'data', 'artifacts.json')


def main():
    artifacts = {}
    sources = []
    for path in sorted(glob.glob(os.path.join(PARTS, '*.json'))):
        payload = json.load(open(path, encoding='utf-8'))
        subject = payload.get('subject') or os.path.basename(path)[:-5]
        for key, value in (payload.get('artifacts') or {}).items():
            if key in artifacts:
                raise SystemExit(f'duplicate artifact id {key} in {path}')
            artifacts[key] = value
            sources.append((key, subject, os.path.basename(path)))
    labels = {}
    if os.path.isfile(LABELS):
        labels = json.load(open(LABELS, encoding='utf-8'))

    merged = {
        'version': 1,
        'artifacts': dict(sorted(artifacts.items())),
        'labels': dict(sorted(labels.items())),
    }
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)
        f.write('\n')

    kinds = {}
    for a in artifacts.values():
        kinds[a.get('type', '?')] = kinds.get(a.get('type', '?'), 0) + 1
    print(f'wrote {OUT}: {len(artifacts)} artifacts, {len(labels)} label sets')
    print('  ' + ', '.join(f'{k}={v}' for k, v in sorted(kinds.items())))


if __name__ == '__main__':
    main()
