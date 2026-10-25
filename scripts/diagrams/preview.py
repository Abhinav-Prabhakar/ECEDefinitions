#!/usr/bin/env python3
"""Render one diagram family to a local HTML contact sheet.

Usage: python3 scripts/diagrams/preview.py physics
       python3 scripts/diagrams/preview.py all
"""
import importlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.dirname(HERE))

FAMILIES = ['physics', 'electronics', 'signals', 'computing', 'software', 'business', 'extra']


def main():
    which = sys.argv[1] if len(sys.argv) > 1 else 'all'
    mods = FAMILIES if which == 'all' else [which]
    cards = []
    count = 0
    for m in mods:
        mod = importlib.import_module(f'diagrams.{m}')
        for name, fn in mod.DIAGRAMS.items():
            body = fn()
            count += 1
            cards.append(
                f'<figure><svg viewBox="0 0 240 150"><symbol id="dg-{name}">{body}</symbol>'
                f'<use href="#dg-{name}"></use></svg><figcaption>{name}</figcaption></figure>'
            )
    html = f'''<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:Inter;src:url('../../assets/fonts/inter-latin-var.woff2') format('woff2');font-weight:100 700}}
body{{margin:0;padding:34px;background:#fff;font-family:Inter,sans-serif;color:#9aa1ad}}
:root{{--accent:#2f7fc1}}
.grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}}
figure{{margin:0;border:1px solid #e8eaee;border-radius:12px;padding:9px;color:#2f7fc1}}
svg{{display:block;width:100%;height:auto}}
figcaption{{font-size:8px;letter-spacing:.08em;text-transform:uppercase;margin-top:5px;color:#9aa1ad}}
</style></head><body><div class="grid">{''.join(cards)}</div></body></html>'''
    out = os.path.join(HERE, f'_preview_{which}.html')
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'wrote {out} ({count} diagrams)')


if __name__ == '__main__':
    main()
