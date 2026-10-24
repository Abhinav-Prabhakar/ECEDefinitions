# one·liners — design system

The source of truth for every screen, component, and future addition.
If a new piece of UI does not fit this document, change the document first.

---

## 01 · Idea

A quiet study instrument for ECE. One definition per line. The interface should feel
like a well-printed datasheet: white paper, hairline rules, tiny annotations, and
occasional bursts of subject colour. Information is layered — the headline is visible,
the detail arrives on hover or on demand.

**Feeling:** precise, calm, engineered, a little poetic.
**Not:** dashboard-y, gradient-heavy, neon, card-on-card, decorative for its own sake.

---

## 02 · Principles

1. **White is a material, not a background.** Keep large uninterrupted fields of it.
2. **One hairline is stronger than one border-radius.** Structure comes from 1px rules,
   not boxes.
3. **Replace text with a mark whenever the mark is clearer.** Counts can be ticks.
   Progress can be a stack. A subject can be a motif.
4. **Reveal, don't dump.** Secondary data lives in hover, focus, or an expanded state.
5. **Colour is a subject's identity, not decoration.** Use it in small doses: a dot, a
   node, a 2px bar, a stroke. Never flood a surface.
6. **Motion is a sentence, not a paragraph.** 180–550ms, eased, then still.
7. **Every pixel must earn its place.** When in doubt, remove it.

---

## 03 · Palette

### Ink & paper

| Token | Value | Use |
| --- | --- | --- |
| `--ink` | `#14161a` | primary text, filled actions |
| `--ink-2` | `#5b6270` | body copy, definitions |
| `--ink-3` | `#9aa1ad` | labels, metadata |
| `--ink-4` | `#c3c8d1` | faint annotations, disabled |
| `--hair` | `#e8eaee` | 1px borders, rules, dividers |
| `--hair-2` | `#f2f3f6` | empty graph cells, tracks |
| paper | `#ffffff` | every full surface |

### Subjects (fixed identity)

| Subject | Colour | Id |
| --- | --- | --- |
| Signals & Systems | `#5b6ee1` | `signals` |
| Digital Electronics | `#12b3a6` | `digital` |
| Analog Electronics | `#eaa22b` | `analog` |
| Electromagnetics | `#e0567f` | `em` |
| Communication Systems | `#22a06b` | `comm` |
| Microprocessors | `#9b6ae0` | `micro` |

Derived values from a subject colour `c`:

- `--accent: c`
- `--accent-line: rgba(c, .45)`
- `--accent-tint: rgba(c, .055)`
- Graph cells: `rgba(c, .20 / .38 / .62 / .95)`

### Semantics

| Token | Value | Use |
| --- | --- | --- |
| `--ok` | `#1f9d6b` | correct answer, goal met |
| `--no` | `#d95376` | incorrect answer |
| tints | same colour at 4.5–8% alpha | state backgrounds |

Semantic colours are reserved. Never use them as subject accents.

---

## 04 · Typography

**Inter**, weights **200 / 300 / 400** only. Default body weight 300.
Letter-spacing is always slightly negative on display type, slightly positive on
uppercase micro-labels.

| Role | Size | Weight | Tracking |
| --- | --- | --- | --- |
| Display (home) | `clamp(38px, 6.4vw, 78px)` | 200 | `-.045em` |
| Subject display | `clamp(30px, 5.2vw, 54px)` | 200 | `-.04em` |
| Quiz definition | `clamp(21px, 2.8vw, 30px)` | 200 | `-.028em` |
| Definition term | 15px | 400 | `-.012em` |
| Definition line | 12.5px / 1.62 | 300 | `-.011em` |
| Section label | 10.5px uppercase | 300 | `.24em` |
| Micro label | 9.5–10px uppercase | 300 | `.14–.22em` |
| Numeric readout | 34–56px | 200 | `-.05em`, tabular |

- Numbers always use `font-variant-numeric: tabular-nums`.
- Never use bold for emphasis. Use weight 400, colour, or a rule.
- Sentence case for content. Uppercase only for structural labels.
- Widows and awkward breaks: `text-wrap: balance` on display and quiz text.

---

## 05 · Space, line, shape

- Page max-width **1180px**; reading column **880px**; quiz column **900px**.
- Horizontal padding: `clamp(20px, 4vw, 48px)`.
- Spacing scale: **4 · 8 · 12 · 16 · 20 · 24 · 32 · 40 · 48 · 64**.
- Radii: **2.5px** graph cells, **8px** tooltips, **11–12px** list rows, **16–18px**
  panels/cards, **99px** pills.
- Borders are always **1px**. Shadows are almost invisible:
  `0 22px 48px -34px rgba(20,22,26,.30)` at most.
- No gradients on paper. Gradients only inside a subject-coloured mark if needed.
- Icons: 1–1.3px stroke, round caps, 24×24 viewBox, never filled except tiny dots.

---

## 06 · Components

### Top bar
64px, translucent white with 14px blur, hairline bottom. Brand left; daily ring and six
subject dots right. Dots are 7px, scale on hover, reveal a name pill.

### Panels
White, 1px hairline, radius 18px, generous padding. A panel head pairs an uppercase
label with a control or legend. Never nest panels.

### Hero
Display title left, one metadata line. On wide screens, a faint 440×260 signal trace sits
top-right: three hairline curves, six subject-coloured nodes, and a coloured comet
travelling each curve. It hides below 980px.

### Contribution graph
53 weeks × 7 days, 16px cells at full width (responsive down to 7px), 3px gap, 2.5px
radius. One cell = one subject, alpha encodes volume. Cells animate in with a diagonal
stagger. Hovering the legend isolates one subject; hovering a cell reveals a hairline
tooltip. Clicking a cell opens its subject. The graph scrolls inside its panel on phones.

### Subject card
White, hairline, 16px radius, min-height 196px. A large thin-line motif sits behind the
content at 15% opacity, rising to 32% on hover. Bottom row: a 26×7 micro-graph (5px
cells) in the subject colour and the definition count. A 1px accent rule draws in along
the bottom.

### Daily progress stack
The day's questions as one continuous stacked bar — one segment per subject, 2px white
gaps, height 28px, radius 3px. The remaining part of the goal is a track with a faint
diagonal hairline hatch.

- Left readout: `done / goal` (200 weight), `left today`, `%` pill, 7-day sparkline.
- Right: the stack, a 0–25–50–75–goal scale, and a six-subject legend with counts.
- Hover/focus a segment **or its legend row**: siblings fade to 26%, the segment lifts
  2px, and a floating card reports subject, count, share of goal, and a mini bar.
- Clicking a segment opens that subject.
- Goal is editable inline (typed or ±10). Default 100. Clamp 10–999. The top-bar ring
  and all readouts update live.
- Over-goal: bar caps at 100%, label reads `goal met · +n`, percentage may exceed 100%.
- No segment labels on the bar itself. The only text inside the chart is the scale.

### Subject page
Full-screen white sheet that rises 18px and fades in. Sticky toolbar: back, subject,
filter, study-eye. Hero: name, meta, then a `quiz yourself` pill and a 20-tick daily
strip. Definitions are a chronological rail: 1px line, 9px hollow nodes, term 400,
definition 300. Hover shifts the row 10px, fills the node, draws a 19px connector, and
reveals the formula at right. Study mode hides definitions until hover.

### Quiz
A separate fixed sheet, layered above the subject page. Same paper, more air.

- Sticky header: back, subject + `quiz` pill, `03 / 10` counter.
- Ten 2px progress ticks. Answered ticks turn `--ok`/`--no`; current tick is accent and
  3px tall. Hovering a tick reveals what happened on that question.
- Card: 1px hairline, radius 20px, 24–44px padding, near-invisible shadow.
- Eyebrow `identify the term` + question index. Definition in 200 weight.
- Four options in a 2×2 grid. Letter chip + term + empty mark slot. Hover lifts 2px,
  tints the border, fills the letter chip with accent.
- Answered: correct row turns `--ok` with a hand-drawn check; wrong row turns `--no` with
  a cross; other rows fade to 45%. A reveal row appears with the verdict, the formula,
  and `next`. The card border takes the semantic tint.
- Keyboard: `1–4` answer, `Enter` next, `Esc` leave. A micro hint sits below the card.
- Background: subject motif at 7% and a very faint engineering grid, plus one slow scan
  line. Nothing else moves.
- Results: 168px thin ring, 1.4px stroke, animated dash offset; score counts up over
  ~700ms; accuracy; a 10-tick answer ribbon (hover for detail); two pill actions; one
  quiet sentence.

### Controls
Round icon buttons: 34px, hairline, 50% hover shift. Pills: 36–38px, 11px uppercase,
`.12em` tracking. Inputs: no box, 1px bottom rule only; focus recolours the rule and
widens a search field by 60px. Focus is always visible.

### Tooltips
White, 1px hairline, 8px radius, 10.5px, soft shadow, `translateY(-4px)` on entry.
They never take pointer events and never carry essential information.

---

## 07 · Motion

| Token | Value |
| --- | --- |
| Standard ease | `cubic-bezier(.22, 1, .36, 1)` |
| Micro (hover, tooltip) | 180–350ms |
| Surface (page, card) | 400–550ms |
| Ambient (motif, scan) | 9–22s, linear or sine |
| Stagger | 13–70ms per index, capped |

- Animate **opacity + transform** only, with the occasional `border-color` and
  `stroke-dashoffset`.
- Definitions rise 9px and fade in, 26ms apart.
- Graph cells scale from .35, diagonal stagger.
- No bounce, no spring overshoot, no parallax.
- Ambient motion must be ignorable. All of it stops under
  `prefers-reduced-motion: reduce`.

---

## 08 · Hover disclosure

Hover is a first-class information layer:

- graph cell → subject, volume
- legend → isolate subject in the graph
- progress segment → subject count, share, mini bar
- quiz tick → what happened on that question
- definition → formula
- top-bar ring → `done / goal today`

Nothing hidden on hover may be required for the primary task. Touch devices get the
same information through always-visible counts or tap equivalents.

---

## 09 · Responsive

Breakpoints: **1140 / 1040 / 980 / 960 / 900 / 820 / 700 / 620 / 600 / 520 / 380px**.

- 3 subject columns → 2 → 1.
- Daily panel 230px readout + chart → single column; readout becomes one row.
- Quiz options 2 → 1; formulas wrap; hint hides on small screens.
- Hero signal trace hides below 980px. Top-bar ring hides below 600px.
- Subject page definitions lose the right-hand formula below 700px.
- Page remains usable at 320px without horizontal scroll (graphs scroll internally).

---

## 10 · Accessibility

- Contrast: body `--ink-2` on white (7.3:1), labels `--ink-3` only at ≥10px and never for
  essential copy. Accent text only where ≥3:1.
- Every interactive element is a real `button`/`input`, keyboard reachable, with
  `:focus-visible` (1px ink outline, 3px offset).
- Tooltips are supplementary; values are also in the DOM or accessible name.
- Icons are `aria-hidden`; controls carry `aria-label`.
- Motion honours reduced-motion. Colour is never the only signal for correctness —
  check/cross marks and text accompany it.

---

## 11 · Voice

Terse, technical, warm. Lowercase structural labels (`today`, `activity`, `quiz`).
No exclamation marks. No motivational poster copy. A quiet line at the end of a quiz is
allowed: *every miss is a definition worth re-reading*.

Definitions are one sentence, ≤ 24 words, present tense, no filler.
Formula glyphs are short and real (`h(t)`, `V = IR`, `δ = √(2/ωμσ)`).

---

## 12 · Scope & build rules

- Frontend only. Static HTML/CSS/JS. No backend, no network calls, no persistence layer
  beyond the tab's memory.
- Mock data lives in clear constants (`SUBJECTS`, `DAILY`) so it can be wired later.
- No frameworks, no build step. Fonts from Google Fonts only.
- Every future component: reuse the tokens above, reuse `.panel`, `.leg`, `.tip`,
  `.back`, `.btn` patterns. Do not introduce a second visual language.
- Before adding a new element, ask: can this be a line, a dot, a tick, or a hover?

---

## 13 · New component checklist

- [ ] Uses existing tokens (no new colours except a documented semantic).
- [ ] One accent per surface; white space preserved.
- [ ] 1px rules, not heavy borders.
- [ ] Micro-label uppercase + tracking; content sentence case.
- [ ] Motion 180–550ms with the standard ease; reduced-motion safe.
- [ ] Secondary data revealed on hover/focus, not dumped.
- [ ] Keyboard reachable; focus visible; labels present.
- [ ] Responsive at 320 / 620 / 960px.
- [ ] Counts are tabular; numbers align.
- [ ] Nothing decorative that does not carry meaning.
