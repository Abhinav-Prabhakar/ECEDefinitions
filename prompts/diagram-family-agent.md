# Diagram family brief

You are adding a **family of concept diagrams** to the one·liners visual library. These are
thin, calm line drawings — the kind of mark you would find in a datasheet, not an
illustration. They will be shown on hover in a subject page and directly in a quiz answer.

You own exactly one file, named in your task prompt, under `scripts/diagrams/`. Do not edit
any other file (not `base.py`, not `build-diagrams.py`, not `assets/diagrams.svg`, not the
data JSONs). Do not run git. Another agent is working on another family in parallel.

---

## 1. The contract

Each family file exports:

```python
from .base import *   # line, path, rect, circle, dot, text, amp, arrow, axis, sine, ...
DIAGRAMS = {
    'my-diagram-id': my_diagram,
    # ...
}

def my_diagram():
    return ''.join([
        line(24, 100, 216, 100, .5),
        circle(120, 75, 30, .7, ACCENT),
        amp(120, 140, 'A SHORT LABEL', o=.4),
    ])
```

Every function returns an SVG **body** string for a 240×150 viewBox. Do not include
`<svg>` or `<symbol>`; the build script wraps it. Do not use external files, images, CSS,
or JavaScript. Do not use `<style>`, `class=`, or ids.

## 2. Visual language

- Canvas **240×150**. Keep 16–24 units of margin. Composition is more important than detail.
- Strokes: **1px**; a single emphasised pair may be **1.3–1.6px**. Fill is normally `none`.
- Colour: `INK` (= `currentColor`, usually ink-3) for structure, `ACCENT`
  (= `var(--accent)`) for the one thing the definition is about. Never use more than one
  accent family. Use opacity, not more colours.
- Labels: uppercase, `text()` / `amp()`, 5.6–6.6px, letter-spacing `.06–.12em`, sparse.
  **No more than 8 labels**, and only labels that earn their place. No sentences.
- Arrowheads small (3–4 units), round caps, round joins.
- Motion is not part of a static symbol. No animation.
- It must read at 280–330px rendered width, in both light and dark themes. Test contrast by
  using only INK/ACCENT and opacity.
- Draw the **idea**, not a screenshot of a slide. A reader who knows the term should
  recognise it in under two seconds.

## 3. What not to do

- No gradients, shadows, rounded card frames, background fills, or decorative dots.
- No tiny 4px labels; no text over lines; no 12-label engineering drawings.
- No fake data or invented units. A sketch of a curve is fine; a precise-looking but wrong
  plot is not.
- No duplicate of an existing id. Check `assets/diagrams.svg` first:
  `grep -o 'id="dg-[^"]*' assets/diagrams.svg`.
- Do not add a diagram that is just a box with the term written inside. The drawing must
  carry structure.

## 4. Existing primitives (`scripts/diagrams/base.py`)

`line(x1,y1,x2,y2,o,w,dash,color)`, `path(d,o,w,dash,color,fill)`,
`rect(x,y,w,h,r,o,dash,color,fill,sw)`, `circle(cx,cy,r,o,color,fill,sw)`,
`dot(cx,cy,r,o,color)`, `text(x,y,s,anchor,o,size,ls,color)`,
`amp(x,y,s,o,size,ls)`, `arrow(x1,y1,x2,y2,o,color,head,w)`, `axis(x0,y0,x1,y1,o)`,
`sine(x0,x1,y,amp,cycles,o,color,dash)`, `curve(points,o,color,dash,w)`,
`bracket(x,y1,y2,label,o,side)`, `bars(x,y,values,w,gap,height,o,accent_last)`,
`grid(x,y,cols,rows,cw,ch,o)`, `box_label(x,y,w,h,label,sub,o,accent)`,
`block_chain(labels,y,x0,x1,gap,h,o,accent)`, `polar_lobe(cx,cy,r,angle0,spread,o,color)`,
`arrow_arc(cx,cy,r,a0,a1,o,color,head)`, `W`, `H`, `INK`, `ACCENT`, `FONT`.

`o` is an opacity hint (helpers multiply by 1.18 and clamp). Use `.3–.6` for structure,
`.7–1` for the emphasised path.

## 5. Test

From the repository root:

```bash
python3 scripts/diagrams/preview.py <family>
```

This writes `scripts/diagrams/_preview_<family>.html`. Open it (a local server is already
available at `http://localhost:8765/` if it is running) and check every drawing at full
size. Then run:

```bash
python3 -c "from scripts.diagrams.<family> import DIAGRAMS; print(len(DIAGRAMS))"
```

You can also render the whole sprite with `python3 scripts/build-diagrams.py` once your
family is merged, but do not edit the main script.

## 6. Report

Return:
- file you changed,
- the list of ids you added (one line each, with a 3–5 word description),
- any requested id you could not draw honestly, and why,
- the preview path and the count.
