#!/usr/bin/env python3
"""Validate the cold-surface artifact registry (code / table / sequence / derivation)
and the diagram label sets. Exits non-zero on schema or cross-reference errors.

Run all:            python3 scripts/validate-artifacts.py
Validate one:       python3 scripts/validate-artifacts.py --subject problem-solving-using-c
"""
import argparse
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARTS = os.path.join(ROOT, 'data', 'artifacts', 'parts')
LABELS = os.path.join(ROOT, 'data', 'artifacts', 'labels.json')
SPRITE = os.path.join(ROOT, 'assets', 'diagrams.svg')
MERGED = os.path.join(ROOT, 'data', 'artifacts.json')
ID_RE = re.compile(r'^[a-z0-9-]+$')
TYPES = {'code', 'table', 'sequence', 'derivation'}

errors = []


def err(msg):
    errors.append(msg)


def is_str(v, n=200):
    return isinstance(v, str) and 0 < len(v) <= n


def check_highlight(v, limit):
    if v is None:
        return
    vals = v if isinstance(v, list) else [v]
    if not vals or any(not isinstance(x, int) or x < 1 or x > limit for x in vals):
        err(f'bad highlight {v!r} for {limit} lines/rows')


def check_code(key, a):
    if not is_str(a.get('lang'), 16):
        err(f'{key}: code.lang missing')
    lines = a.get('lines')
    if not isinstance(lines, list) or not (1 <= len(lines) <= 16):
        err(f'{key}: code.lines must be 1..16 strings')
        return
    for i, line in enumerate(lines, 1):
        if not isinstance(line, str) or len(line) > 140:
            err(f'{key}: code line {i} missing or >140 chars')
    check_highlight(a.get('highlight'), len(lines))
    out = a.get('output')
    if out is not None and (not isinstance(out, list) or len(out) > 12 or any(not isinstance(x, str) or len(x) > 100 for x in out)):
        err(f'{key}: code.output must be ≤12 strings ≤100 chars')


def check_table(key, a):
    heads = a.get('headers')
    rows = a.get('rows')
    if not isinstance(heads, list) or not (1 <= len(heads) <= 6) or any(not is_str(h, 40) for h in heads):
        err(f'{key}: table.headers must be 1..6 strings')
        return
    if not isinstance(rows, list) or not (1 <= len(rows) <= 18):
        err(f'{key}: table.rows must be 1..18 rows')
        return
    for i, row in enumerate(rows, 1):
        if not isinstance(row, list) or len(row) != len(heads):
            err(f'{key}: table row {i} must have {len(heads)} cells')
            continue
        for cell in row:
            if not isinstance(cell, (str, int, float)) or len(str(cell)) > 100:
                err(f'{key}: table row {i} has a bad cell')
    check_highlight(a.get('highlight'), len(rows))


def check_sequence(key, a):
    actors = a.get('actors')
    steps = a.get('steps')
    if not isinstance(actors, list) or not (2 <= len(actors) <= 4) or any(not is_str(x, 24) for x in actors):
        err(f'{key}: sequence.actors must be 2..4 strings')
        return
    if not isinstance(steps, list) or not (2 <= len(steps) <= 10):
        err(f'{key}: sequence.steps must be 2..10')
        return
    for i, s in enumerate(steps, 1):
        if not isinstance(s, dict):
            err(f'{key}: step {i} not an object')
            continue
        if not isinstance(s.get('from'), int) or not isinstance(s.get('to'), int):
            err(f'{key}: step {i} needs integer from/to')
        elif not (0 <= s['from'] < len(actors) and 0 <= s['to'] < len(actors)):
            err(f'{key}: step {i} actor out of range')
        if not is_str(s.get('label'), 48):
            err(f'{key}: step {i} needs a short label')


def check_derivation(key, a):
    steps = a.get('steps')
    if not isinstance(steps, list) or not (1 <= len(steps) <= 7) or any(not is_str(x, 260) for x in steps):
        err(f'{key}: derivation.steps must be 1..7 strings')
    syms = a.get('symbols')
    if syms is not None:
        if not isinstance(syms, list) or len(syms) > 10:
            err(f'{key}: derivation.symbols must be a list ≤10')
        else:
            for pair in syms:
                if not isinstance(pair, list) or len(pair) != 2 or not is_str(pair[0], 60) or not is_str(pair[1], 100):
                    err(f'{key}: derivation.symbols entries must be [symbol, meaning]')


def load_fragments(subject=None):
    out = {}
    for path in sorted(glob.glob(os.path.join(PARTS, '*.json'))):
        if subject and os.path.basename(path) != f'{subject}.json':
            continue
        payload = json.load(open(path, encoding='utf-8'))
        for key, value in (payload.get('artifacts') or {}).items():
            if key in out:
                err(f'duplicate artifact id {key}')
            out[key] = value
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--subject')
    args = ap.parse_args()
    subject = args.subject

    artifacts = load_fragments(subject)
    if not subject and os.path.isfile(MERGED):
        merged = json.load(open(MERGED, encoding='utf-8'))
        # The merged file must be a superset of fragments; if it exists, validate it too.
        for key in merged.get('artifacts', {}):
            if key not in artifacts:
                artifacts[key] = merged['artifacts'][key]

    for key, a in artifacts.items():
        if not ID_RE.match(key) or '--' not in key:
            err(f'{key}: artifact id must be <subject>--<definition>')
            continue
        t = a.get('type')
        if t not in TYPES:
            err(f'{key}: bad type {t!r}')
            continue
        if a.get('title') is not None and not is_str(a['title'], 70):
            err(f'{key}: title too long')
        if a.get('note') is not None and not is_str(a['note'], 180):
            err(f'{key}: note too long')
        allowed = {'type', 'title', 'note'}
        allowed |= {'lang', 'lines', 'highlight', 'output'} if t == 'code' else set()
        allowed |= {'headers', 'rows', 'highlight', 'align'} if t == 'table' else set()
        allowed |= {'actors', 'steps'} if t == 'sequence' else set()
        allowed |= {'steps', 'symbols'} if t == 'derivation' else set()
        extra = set(a) - allowed
        if extra:
            err(f'{key}: extra keys {sorted(extra)}')
        if t == 'code':
            check_code(key, a)
        elif t == 'table':
            check_table(key, a)
        elif t == 'sequence':
            check_sequence(key, a)
        elif t == 'derivation':
            check_derivation(key, a)

    # Cross-reference definitions.
    subject_files = sorted(glob.glob(os.path.join(ROOT, 'data', 'subjects', '*', '*.json')))
    used = {}
    for path in subject_files:
        payload = json.load(open(path, encoding='utf-8'))
        sid = payload.get('id')
        if subject and sid != subject:
            continue
        for d in payload.get('definitions', []):
            aid = d.get('artifact')
            if not aid:
                continue
            if not isinstance(aid, str) or not ID_RE.match(aid):
                err(f'{sid}/{d.get("term")}: bad artifact id {aid!r}')
                continue
            if not aid.startswith(f'{sid}--'):
                err(f'{sid}/{d.get("term")}: artifact id must start with {sid}--')
            if aid not in artifacts:
                err(f'{sid}/{d.get("term")}: unknown artifact {aid!r}')
            used[aid] = used.get(aid, 0) + 1

    if not subject:
        for aid in artifacts:
            if aid not in used:
                err(f'{aid}: artifact is not referenced by a definition')
        for aid, n in used.items():
            if n > 1:
                err(f'{aid}: referenced by {n} definitions')

    # Labels.
    labels = {}
    if os.path.isfile(LABELS):
        labels = json.load(open(LABELS, encoding='utf-8'))
    sprite = open(SPRITE, encoding='utf-8').read() if os.path.isfile(SPRITE) else ''
    diagram_ids = set(re.findall(r'<symbol id="dg-([^"]+)"', sprite))
    for did, rows in labels.items():
        if diagram_ids and did not in diagram_ids:
            err(f'labels/{did}: diagram id not in sprite')
            continue
        if not isinstance(rows, list) or not (3 <= len(rows) <= 10):
            err(f'labels/{did}: need 3..10 labels')
            continue
        seen = set()
        for r in rows:
            if not isinstance(r, dict) or not isinstance(r.get('x'), (int, float)) or not isinstance(r.get('y'), (int, float)):
                err(f'labels/{did}: each label needs numeric x/y')
                continue
            if not (0 <= r['x'] <= 240 and 0 <= r['y'] <= 150):
                err(f'labels/{did}: point outside 240×150')
            if not is_str(r.get('label'), 36):
                err(f'labels/{did}: bad label')
            elif r['label'].lower() in seen:
                err(f'labels/{did}: duplicate label {r["label"]!r}')
            else:
                seen.add(r['label'].lower())

    kinds = {}
    for a in artifacts.values():
        kinds[a.get('type', '?')] = kinds.get(a.get('type', '?'), 0) + 1
    print(f'artifacts={len(artifacts)} labels={len(labels)} ' +
          ' '.join(f'{k}={v}' for k, v in sorted(kinds.items())))
    if errors:
        print(f'ARTIFACT VALIDATION FAILED: {len(errors)} problem(s)')
        for e in errors:
            print(' -', e)
        return 1
    print('ARTIFACT VALIDATION OK')
    return 0


if __name__ == '__main__':
    sys.exit(main())
