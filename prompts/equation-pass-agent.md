# Equation & diagram pass — subject brief

You are adding **equations and a small number of diagrams** to one subject file in the
one·liners ECE dataset. The definitions are already written and validated. Do not rewrite
them. This is a notation layer, not a second curriculum.

You own **exactly one file**, given in your task prompt. Do not edit any other file. Do not
run `git`. Do not touch `index.html`, `design.md`, `README.md`, `sw.js`, `assets/`,
`scripts/`, or another subject's JSON. Another agent may be working on the next file.

---

## 1. The two fields

Every definition already has:

```json
{
  "id": "de-broglie-hypothesis",
  "term": "de Broglie hypothesis",
  "definition": "Any moving particle is associated with a matter wave.",
  "formula": "",
  "unit": 1,
  "unitTitle": "Quantum Mechanics",
  "sources": ["ep-unit-1-quantum-mechanics#p.5"]
}
```

- `formula` — **bare inline TeX**, rendered by KaTeX. No `$`, no `$$`, no
  `\begin{...}`/`\end{...}`. Keep it under 140 characters. Empty string when the
  definition has no honest equation.
- `diagram` — optional id from the shared sprite (list below). Add it only when the
  drawing directly depicts the definition. Omit the key otherwise.

Do not add any other keys. Do not change `id`, `term`, `definition`, `unit`,
`unitTitle`, or `sources`. Preserve every existing source locator exactly.

## 2. What deserves an equation

Add a formula when it makes the definition more precise, memorable or testable:

- a defining relation (`\lambda=h/p`, `V=IR`, `f_c=\frac{1}{2\pi RC}`),
- a governing law or transfer function (`H(s)=\frac{\omega_n^2}{s^2+2\zeta\omega_n s+\omega_n^2}`),
- a standard bound, identity or complexity (`T(n)=O(n\log n)`, `\Delta x\,\Delta p\ge \hbar/2`),
- a canonical transform or mapping (`X(k)=\sum_{n=0}^{N-1}x(n)e^{-j2\pi kn/N}`).

Leave `formula` empty for definitions that are genuinely non-quantitative: a policy, a
protocol name, a management concept, a historical experiment, a layer description, a
data-structure operation with no invariant, a programming-language feature. **An invented
or decorative equation is worse than no equation.** Roughly half of the technical
catalogue should end up with one; non-technical subjects may have few or none.

Rules of notation:

- Use LaTeX commands, not Unicode maths: `\lambda`, `\Omega`, `\mu`, `\partial`,
  `\nabla`, `\int`, `\sum`, `\sqrt{}`, `\frac{}{}`, `\mathbf{}`, `\hat{}`, `\overline{}`.
  Degrees are `^{\circ}`. Infinity is `\infty`.
- Subscripts: `V_{BE}`, `I_{DS}`, `E_n` is acceptable but prefer `E_{n}`.
- Multi-letter labels inside maths use `\text{}`: `V_{\text{out}}`, `P_{\text{loss}}`.
- Multiplication: juxtaposition or `\,`; avoid `*`. Use `\cdot` for a visible dot.
- Approximate: `\approx`. Proportional: `\propto`. Defined as: `\equiv`.
- No units inside the formula unless the unit is the point. Keep units in the definition.
- Do not write a sentence inside the formula. One relation, or at most one short chain.
- No `\displaystyle`, no `\begin{aligned}`, no `\tag`, no `\label`, no `\ref`.
- Use `j` for the imaginary unit in signals/electrical subjects; `i` is acceptable in pure
  mathematics when that is the local convention.
- Do not duplicate the same generic formula on ten unrelated rows. The formula must belong
  to this definition.

## 3. Diagrams

The shared sprite lives in `assets/diagrams.svg` (193 symbols). On the subject page a
diagram is revealed on hover; in a quiz it is shown with the answer.

**Read `prompts/diagram-catalog.md` before choosing one.** It lists every id, what it
draws, and the per-subject coverage guide. Use it thoughtfully:

- A diagram must carry structure the sentence cannot: a curve, field, circuit, state,
  stack, pipeline, geometry, before/after.
- Do not put a drawing on a syntax keyword, API name, policy label, management term, or a
  row whose definition is already complete.
- Prefer 1 diagram per 3–5 rows in a visual subject, 1 per 8–15 in maths/programming, and
  0–3 in a values/policy subject. Do not exceed ~40% of any subject.
- Do not reuse one symbol on more than ~5 rows; if a whole unit shares an idea, put it on
  the 2–3 defining rows.
- Keep an existing `diagram` if it is right; replace it only when the catalog has a clearly
  better fit; remove it if it is misleading.
- **Do not invent ids and do not edit the sprite.** If a row truly needs an absent drawing,
  leave it bare and report the gap.

## 4. How to edit

Use a short Python script so nothing else in the file moves. Work from the repository root:

```python
import json
p = 'data/subjects/<sem>/<subject>.json'
d = json.load(open(p, encoding='utf-8'))
by_id = {x['id']: x for x in d['definitions']}
changes = {
  'de-broglie-hypothesis': (r'\lambda=\frac{h}{mv}', None),
  # ...
}
for key, (tex, dg) in changes.items():
    x = by_id[key]
    # keep an existing non-empty formula if you have nothing better; otherwise set it
    x['formula'] = tex
    if dg:
        x['diagram'] = dg
    else:
        x.pop('diagram', None)
with open(p, 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
    f.write('\n')
```

Then run:

```bash
python3 scripts/validate-seed-data.py        # must print VALIDATION OK
node scripts/check-formulas.mjs              # must print FORMULA CHECK OK
```

Both scripts read the whole dataset. They are read-only. If another agent is mid-write on
its own file, a transient JSON error may appear; re-run once. If the error names **your**
file, fix it before finishing.

Before you finish, spot-check three definitions whose equations are non-trivial. A formula
must be dimensionally and physically correct, not merely plausible.

## 5. Report

Return a short report:

- file path you changed,
- number of non-empty formulas and number of diagram assignments,
- formulas left empty because the definition has no honest equation,
- any diagram you wished existed (name + one-line description), if any,
- the final validator outputs.

Do not paste the whole file.
