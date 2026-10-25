# Artifact pass — cold surfaces for the remaining definitions

You are adding **one optional artifact** to definitions that are better served by a code
surface, a spec table, a sequence, or a derivation than by another diagram. The artifact
layer is already rendered by the app; you provide data only.

Read `prompts/diagram-catalog.md` for the existing visual layer and this brief for the new
one. You own the subject JSON(s) and fragment file(s) named in your task prompt. Do not
edit `index.html`, `design.md`, `README.md`, `assets/`, `scripts/`, `data/artifacts.json`,
`data/artifacts/labels.json`, or another subject.

---

## 1. What is an artifact?

A cold surface is a plain, read-only panel:

- **code** — an idiomatic 3–12 line specimen, one highlighted line, optional output.
- **table** — a bitfield/register/comparison/truth/access table, one highlighted row.
- **sequence** — 2–4 actors and 3–8 ordered steps (protocol, transaction, schedule).
- **derivation** — 2–5 numbered LaTeX steps plus a symbol table.

It is not a second definition. It must add the thing the sentence cannot show: the actual
syntax, the wire format, the order of operations, or the algebra between the formula and
the result.

## 2. Fragment format

Each subject has one fragment:

`data/artifacts/parts/<subject-id>.json`

```json
{
  "subject": "problem-solving-using-c",
  "artifacts": {
    "problem-solving-using-c--pointer": {
      "type": "code",
      "lang": "c",
      "title": "pointer arithmetic",
      "lines": [
        "int x = 42;",
        "int *p = &x;",
        "printf(\"%d\\n\", *p);"
      ],
      "highlight": [2],
      "output": ["42"],
      "note": "p stores the address of x; *p reads the value at that address."
    }
  }
}
```

In the subject JSON, add **only** the matching key to the definition:

```json
"artifact": "problem-solving-using-c--pointer"
```

Keys are additive. Do not change `term`, `definition`, `formula`, `diagram`, `unit`,
`unitTitle`, `id` or `sources`. Do not remove an existing `diagram` or `formula`.

### Artifact ID

`<subject-id>--<definition-id>`

The subject id is the file's `id` field. The definition id is the definition's `id` field.
The prefix must match exactly. One artifact per definition; one definition per artifact.

## 3. Type schemas

### code

```json
{
  "type": "code",
  "lang": "c",
  "title": "short title ≤ 70 chars",
  "lines": ["line 1", "line 2"],
  "highlight": [2],
  "output": ["optional", "lines"],
  "note": "one sentence ≤ 180 chars"
}
```

- `lines` 1–16, each ≤ 140 chars. Use spaces, not tabs. Do not use `...` inside syntax
  that would be misleading; a shortened example is fine if it is still valid.
- `highlight` is a line number or array of line numbers (1-based).
- `lan`: use one of `c`, `java`, `python`, `sql`, `verilog`, `systemverilog`, `arm`,
  `bash`, `js`, `text`, `pseudo`.
- `output` is optional. Only include real output for a deterministic snippet.
- No code execution, no `$` shell markers, no shell prompts.

### table

```json
{
  "type": "table",
  "title": "TCP header",
  "headers": ["field", "bits"],
  "rows": [["source port", "16"], ["destination port", "16"]],
  "highlight": 2,
  "note": "one sentence"
}
```

- 1–6 columns, 1–18 rows, each cell ≤ 100 chars.
- `highlight` is one row number (1-based), optional.
- Use it for bitfields, register maps, state tables, truth tables, comparisons, access
  matrices, and short implementation tables. Do **not** paste an entire datasheet.
- Put units in the header or cell. Keep numbers tabular.

### sequence

```json
{
  "type": "sequence",
  "title": "TCP connection open",
  "actors": ["client", "server"],
  "steps": [
    {"from": 0, "to": 1, "label": "SYN"},
    {"from": 1, "to": 0, "label": "SYN + ACK"},
    {"from": 0, "to": 1, "label": "ACK"}
  ],
  "note": "one sentence"
}
```

- 2–4 actors, 3–8 steps. Labels ≤ 48 chars.
- Use for handshakes, transactions, scheduling, pipelines, cache coherence, interrupt
  paths, and protocol exchanges.
- Do not use it for a simple list; that is a table.

### derivation

```json
{
  "type": "derivation",
  "title": "particle in an infinite well",
  "steps": [
    "E_{n}=\\frac{n^{2}h^{2}}{8mL^{2}}",
    "\\psi_{n}(x)=\\sqrt{\\frac{2}{L}}\\sin\\!\\left(\\frac{n\\pi x}{L}\\right)"
  ],
  "symbols": [
    ["n", "principal quantum number"],
    ["L", "well width"]
  ],
  "note": "one sentence"
}
```

- 2–5 steps, each bare inline TeX (no `$`, no `\begin{}`/`\end{}`), ≤ 260 chars.
- 0–8 symbols, each `[symbol, meaning]`; symbol may be TeX (e.g. `P_{r}`).
- Use only when the steps genuinely derive or connect the formula on the row. Do not
  number the same formula twice or pad with algebra that is not used.

## 4. Where artifacts help

Work from the **bare rows** first: definitions with no `formula` and no `diagram`, or where
the existing formula/diagram is not the mode the student needs.

| subject type | preferred artifacts | examples |
| --- | --- | --- |
| C / Java / Python / Embedded C | code, table | storage class, pointer, decorator, interface, bit mask, register map |
| SystemVerilog / VLSI / ARM | code, sequence, table | constraint, assertion, clocking block, register map, pipeline, bus transfer |
| DBMS | code, table, sequence | SQL join, trigger, B-tree, transaction schedule, normalization |
| OS / RTOS / COA | table, sequence, code | scheduling, page replacement, PCB, pipeline, interrupt, cache |
| Networks / IoT / Cyber | table, sequence, code | packet header, handshake, routing, attack tree, certificate chain |
| AI / ML | code, table, derivation | search tree, backprop, confusion matrix, Bayes, gradient step |
| Signals / DSP / Control / Comms | derivation, table | transform pair, filter design, link budget, modulation table |
| Circuits / EDC / Analog / IC | table, derivation | operating regions, register map, bias table, design equation |
| Math / Physics / Chemistry | derivation | Taylor, residues, Fermi level, Bragg, Nernst |
| Management / Product / UHV / Environment | table, sequence | canvas, 2×2, stakeholder map, value chain, decision tree |

Do not add an artifact to every row. Use the catalog’s judgement:

- Programming: 6–12 artifacts per subject, only for syntax/API/structure rows where a
  snippet is clearer than prose.
- Systems/hardware/networks: 6–10 per subject.
- Math/physics/engineering: 4–8 per subject.
- Management/humanities: 3–6 per subject, and 0–3 for UHV.

These are ceilings, not quotas. A smaller, sharper set is better. Do not repeat the same
artifact on multiple definitions; if a table applies to a family, use it on the row that
defines the table.

## 5. Workflow

1. Read the subject JSON and list its bare definitions.
2. Choose the artifacts that genuinely help.
3. Write/merge the fragment with Python (preserve existing entries):
   ```python
   import json
   p = 'data/artifacts/parts/<subject>.json'
   try: payload = json.load(open(p, encoding='utf-8'))
   except FileNotFoundError: payload = {'subject': '<subject>', 'artifacts': {}}
   payload.setdefault('artifacts', {}).update({...})
   json.dump(payload, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
   ```
4. Add the `artifact` keys to the definitions with a second script.
5. Validate:
   ```bash
   python3 scripts/validate-artifacts.py --subject <subject>
   node scripts/check-artifact-formulas.mjs data/artifacts/parts/<subject>.json
   python3 scripts/validate-seed-data.py
   ```
   The last command reads the whole dataset; if it mentions another subject, re-run once.
   Do not run `scripts/build-artifacts.py` — the orchestrator merges the fragments.
6. Report the file(s), counts by type, and the validator output.

Do not touch the merged `data/artifacts.json` or the labels file.
