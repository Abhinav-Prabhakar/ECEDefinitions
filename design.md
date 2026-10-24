# one·liners — design system

The source of truth for every screen, component, and future addition.
If a new piece of UI does not fit this document, change the document first.

---

## 01 · Idea

A quiet study instrument for ECE. One definition per line. The interface should feel
like a well-printed datasheet: white paper, hairline rules, tiny annotations, and
occasional bursts of subject colour. Information is layered — the headline is visible,
the detail arrives on hover, focus, or in a deliberate mode.

It is also now a **memory instrument**: every answer updates a per-definition confidence
score that survives reloads. The UI should make that invisible memory visible without
turning the page into a dashboard.

**Feeling:** precise, calm, engineered, a little poetic.
**Not:** dashboard-y, gradient-heavy, neon, card-on-card, confetti of colours,
decorative for its own sake.

---

## 02 · Principles

1. **White is a material, not a background.** Keep large uninterrupted fields of it.
2. **One hairline is stronger than one border-radius.** Structure comes from 1px rules,
   not boxes.
3. **Replace text with a mark whenever the mark is clearer.** Counts can be ticks.
   Progress can be a stack. Memory can be bars.
4. **Reveal, don't dump.** Secondary data lives in hover, focus, or an explicit mode.
5. **Colour is a subject's identity, not decoration.** Use it in small doses: a dot, a
   node, a 2px bar, one filtered heatmap. Never flood a surface with six+ colours.
6. **Motion is a sentence, not a paragraph.** 180–550ms, eased, then still.
7. **Every pixel must earn its place.** When in doubt, remove it.
8. **Scale quietly.** The same components will hold 30 subjects. Prefer filters,
   grouping, and neutral charts over more colour.

---

## 03 · Palette

### Ink & paper

| Token | Value | Use |
| --- | --- | --- |
| `--ink` | `#14161a` | primary text, filled actions |
| `--ink-2` | `#5b6270` | body copy, definitions |
| `--ink-3` | `#9aa1ad` | labels, metadata, mastery stats |
| `--ink-4` | `#c3c8d1` | faint annotations, empty tracks |
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
- Daily stack segments: the subject colour flat.
- Filtered heatmap cells: `rgba(c, .16 / .30 / .48 / .68 / .90)`.

### Neutral heatmap

The activity heatmap is deliberately **monochrome**, so it survives 30 subjects and does
not compete with subject colour:

| Level | Value |
| --- | --- |
| 0 | `#eff1f4` |
| 1 | `rgba(20,22,26,.13)` |
| 2 | `rgba(20,22,26,.26)` |
| 3 | `rgba(20,22,26,.43)` |
| 4 | `rgba(20,22,26,.62)` |

When a subject filter is active, the same four levels use that subject's colour.

### Semantics

| Token | Value | Use |
| --- | --- | --- |
| `--ok` | `#1f9d6b` | correct, goal met, positive mastery |
| `--no` | `#d95376` | incorrect, negative mastery |
| tints | same colour at 4–5% alpha | card state, answer state |

Semantic colours are reserved. Never use them as subject accents.

### Mastery language

Confidence is a number from **0 to 1**:

| Range | Label |
| --- | --- |
| 0 / unseen | `new` |
| `0 < s < .40` | `learning` |
| `.40 ≤ s < .75` | `familiar` |
| `.75 ≤ s < 1` | `solid` |
| `1` | `solid` (100%) |

The UI shows the percentage everywhere, not just the label. A single correct answer adds
`.30`; a wrong answer subtracts `.40`, clamped to `[0,1]`. Four consecutive correct
answers reach 100%.

---

## 04 · Typography

**Inter**, weights **200 / 300 / 400** only. Default body weight 300.
Letter-spacing is slightly negative on display type, slightly positive on uppercase
micro-labels.

| Role | Size | Weight | Tracking |
| --- | --- | --- | --- |
| Display (home) | `clamp(38px, 6.4vw, 78px)` | 200 | `-.045em` |
| Subject display | `clamp(30px, 5.2vw, 54px)` | 200 | `-.04em` |
| Quiz definition | `clamp(21px, 2.8vw, 30px)` | 200 | `-.028em` |
| Quiz term (word prompt) | `clamp(30px, 4.4vw, 46px)` | 200 | `-.04em` |
| Definition term | 15px | 400 | `-.012em` |
| Definition line | 12.5px / 1.62 | 300 | `-.011em` |
| Explanation copy | 11.2–12px / 1.6 | 300 | `-.005em` |
| Section label | 10.5px uppercase | 300 | `.24em` |
| Micro label | 8–10px uppercase | 300 | `.1–.2em` |
| Numeric readout | 40–58px | 200 | `-.05em`, tabular |

- Numbers always use `font-variant-numeric: tabular-nums`.
- Never use bold for emphasis. Use weight 400, colour, or a rule.
- Sentence case for content. Uppercase only for structural labels.
- Display and quiz text use `text-wrap: balance`.

---

## 05 · Space, line, shape

- Page max-width **1180px**; reading column **880px**; quiz column **900px**.
- Horizontal padding: `clamp(20px, 4vw, 48px)`.
- Spacing scale: **4 · 8 · 12 · 16 · 20 · 24 · 32 · 40 · 48 · 64**.
- Radii: **2.5px** graph cells, **8px** tooltips, **11–12px** list rows, **16–18px**
  panels/cards, **20px** quiz card, **99px** pills.
- Borders are always **1px**. Shadows are almost invisible:
  `0 22px 48px -34px rgba(20,22,26,.30)` at most.
- No gradients on paper. Gradients only inside a subject-coloured mark if needed.
- Icons: 1–1.3px stroke, round caps, 24×24 viewBox, never filled except tiny dots.

---

## 06 · Motion

| Token | Value |
| --- | --- |
| Standard ease | `cubic-bezier(.22, 1, .36, 1)` |
| Micro (hover, tooltip) | 160–350ms |
| Surface (page, card) | 400–700ms |
| Ambient (motif, scan) | 9–22s, linear or sine |
| Stagger | 13–70ms per index, capped |

- Animate **opacity + transform** primarily, with `border-color`, `background`,
  `stroke-dashoffset`, and mastery bar `width`.
- Definitions rise 9px and fade in, 24ms apart.
- Heatmap cells scale from .35 with a diagonal stagger (initial build only).
- Mastery bars and the daily stack animate their width when data changes.
- No bounce, no spring overshoot, no parallax.
- All ambient motion stops under `prefers-reduced-motion: reduce`; score count-up is
  replaced with the final number.

---

## 07 · Data & persistence

Everything is client-side. The static HTML app uses one localStorage key:

```
oneliners.state.v1
```

Shape:

```js
{
  goal: 100,                 // 10–999
  mastery: {
    "signals|Convolution": {
      attempts: 4, correct: 3, score: 0.9, streak: 3, last: 172...
    }
  },
  history: {
    "2026-10-24": {
      total: 41,
      subjects: { signals: 12, comm: 9, digital: 8 }
    }
  }
}
```

- `score` is the mastery value. `attempts` / `correct` are for hover details and cards.
- Every answer updates the definition score, today's subject count, today's total, and
  writes to localStorage.
- History older than ~405 days is pruned.
- The daily goal is persisted; changing it updates the stack, scale, ring and heatmap.
- Today's counts reset naturally by date key at local midnight; a 30-second interval
  re-renders across the boundary.
- Reset clears mastery and history but preserves the chosen goal. The footer action is
  two-step: `reset progress` → `click again to erase`.
- `storage` events from another tab reload the state and refresh the UI.
- No backend, no accounts, no network writes.

### Derived statistics

- **Daily stack:** today's subject counts, sorted descending, top six + `other`.
- **Streak:** consecutive days ending today (or yesterday if today is empty) with ≥1
  answer. Filter-aware on the activity panel.
- **Best day:** max daily total, filter-aware.
- **Remembered:** average mastery across all definitions (0% when untouched).
- **Solid count:** definitions with mastery ≥ .75.
- **Adaptive rounds:** the three weakest definitions are always included in a 10-question
  quiz; the remaining slots are weighted toward low mastery. The round is shuffled, and
  question types stay balanced 5/5.

---

## 08 · Components

### Top bar
64px, translucent white with 14px blur, hairline bottom. Brand left. Right: daily ring,
a scalable **subjects jump** pill (3×3 dot grid, count), and a keyboard `?` button.
The old six nav dots are gone — the design must survive 30 subjects. The subjects jump
scrolls to the subject index and focuses its search on pointer devices.

### Hero
Display title left, live metadata line: definitions, subjects, overall remembered %,
today's count. On wide screens, a faint 440×260 signal trace sits top-right: three
hairline curves, six subject-coloured nodes, and a coloured comet per curve. Hidden
below 980px.

### Daily progress stack
Today's questions as one continuous stacked bar — one segment per subject, 2px white
gaps, height 28px, radius 3px. The remaining goal is a track with a faint diagonal
hairline hatch.

- Segments are sorted by count. **Top six subjects only**; the rest become one neutral
  `other` segment. This is the 30-subject rule.
- Left readout: `done / goal` (200 weight), `left today`, `%` pill, 7-day sparkline.
- Right: the stack, a 0–25–50–75–goal scale, and an active-subject legend with counts
  (plus `+n more`).
- Hover/focus a segment or its legend row: siblings fade to 26%, the segment lifts 2px,
  and a floating card reports subject, count, share of goal, and a mini bar. The `other`
  card lists the grouped subjects.
- Clicking a subject segment opens its subject.
- Empty state: hatched track, `nothing logged today — open a subject below`.
- The goal is editable inline (typed or ±10). Default 100. Clamp 10–999.
- Over-goal: bar caps at 100%, label reads `goal met · +n`, percentage may exceed 100%.
- The top-bar ring is now a single graphite progress arc (green when the goal is met),
  not a six-colour wheel. Subject colour belongs to the stack, not the ring.

### Activity heatmap
53 weeks × 7 days, 16px cells at full width (responsive down to 7px), 3px gap,
2.5px radius. This is a **neutral** GitHub-style tracker:

- Intensity is relative to the busiest filtered day (max-scaling). It never becomes a
  confetti of subject colours.
- A subject filter (native select, styled to hairline) recolours the heatmap in that
  subject's hue and makes the stats filter-aware. With 30 subjects this remains one
  control, not a legend of 30 colours.
- A `less → more` legend of four neutral swatches updates to the filtered hue.
- Hovering/tapping a cell opens a floating card: date, total, and up to four subject
  rows with dots. `+n more` covers the rest.
- Stats: answered, day streak, best day. Empty state: `the trail starts with one answer`
  and a `pick a subject →` text action.
- On narrow screens the heatmap scrolls internally and starts aligned to the most recent
  week, so today is visible immediately.

### Subject index
A section head (`subjects`, visible/total count) and an inline search with `/` key hint.
The grid is 3 → 2 → 1 columns. The search filters card visibility live and shows a quiet
empty line when nothing matches.

### Subject cards
White, hairline, 16px radius, min-height 196px. A large thin-line motif sits behind the
content at 15% opacity, rising to 32% on hover. Top row: dot, name, overall mastery %.
Bottom row: **one thin vertical bar per definition**, height and opacity scaled by that
definition's mastery (4px baseline when new), and `solid/total solid`. The bars form a
tiny memory profile for the subject. Hovering the bar strip reveals the overall summary.
No fake mini-contribution graph remains.

### Subject page
Full-screen white sheet that rises 18px and fades in. Sticky toolbar: back, subject,
filter, study-eye.

- Hero: name, `n one-liners`, a 180px mastery rule filled to the overall %, `x%
  remembered`, a `quiz yourself` pill with a `q` keycap, and a 20-tick daily strip.
- `focus` filters: `all · new · learning · solid` with counts. They combine with the
  text filter; the visible count reads `x of n`. An empty view offers a one-click clear.
- Definitions are a chronological rail: 1px line, 9px hollow nodes, term 400, definition
  300. Each row has a right rail: the **mastery percentage** above a 2px 94px bar.
  Hovering the row swaps the percentage for the formula and fills the node.
- On mobile the rail becomes a full-width mastery line under the definition, with the
  percentage at right; the formula is desktop-only.
- Study mode hides definitions until hover (existing behaviour, `s` shortcut).
- Filtering or searching after a quiz that changed mastery re-evaluates the visible set.

### Quiz
A separate fixed sheet, layered above the subject page. Same paper, more air.
10 questions per round, **two question types, balanced 5/5**. Sampling is adaptive: the
three weakest definitions are guaranteed a slot and the rest are weighted toward low
mastery (communicated by the quiz CTA tooltip and the shortcuts note):

1. **term → definition:** the term is displayed large; choose the matching definition
   from four full-width definition rows.
2. **definition → term:** the definition is displayed; choose the term from four rows.

- The eyebrow shows the direction (`term → definition`), the question index, and the
  sticky header shows `03 / 10`.
- Ten 2px progress ticks. Answered ticks turn `--ok`/`--no`; the current tick is accent
  and 3px tall. Hovering a tick reveals the type and result.
- Card: 1px hairline, radius 20px, 24–42px padding, near-invisible shadow.
- Four options with letter chips. Hover lifts 2px, tints the border, fills the chip.
- Answered: correct row gets `--ok` + hand-drawn check; the chosen wrong row gets `--no`
  + cross; others fade to 42%.
- **Explanation block** appears below a hairline:
  - verdict (`correct` / `not quite`) + `That's <term>` / `It's <term>`
  - `why` row: the canonical one-line definition + a `cue` formula chip
  - `your pick` row on misses: the chosen term and its definition, for direct comparison
  - mastery row: current %, animated bar, and `+30%` / `−40%` delta.
- Every option carries `aria-keyshortcuts`; letters and digits both answer.
- Results: 168px thin ring, animated dash offset, count-up score, accuracy, correct
  count, round mastery delta, a 10-tick answer ribbon (hover for term + type), and two
  pill actions with `r` / `b` keycaps. One quiet sentence.
- Background: subject motif at 7%, a very faint 48px engineering grid, one slow scan
  line. Nothing else moves.

### Shortcuts overlay
A white 530px dialog over a white blur. Sections for anywhere / subject / quiz. Hairline
rows, keycaps (`kbd`) at right. `?` opens and closes, `Esc` closes, focus is placed on
the close button and Tab is held inside. Reachable from the top bar and the footer.

### Footer
`progress stays on this device` left; `keyboard` and two-step `reset progress` right.
No account, no cloud.

### Tooltips
Hairline white pills for graph cells, week bars, card mastery ticks, definition rails,
and quiz ticks. The activity heatmap and daily stack use richer floating cards described
above. Tooltips never take pointer events, and never contain the only copy of important
information.

---

## 09 · Keyboard map

| Context | Keys |
| --- | --- |
| Anywhere | `?` shortcuts · `Esc` close/back |
| Home | `/` find subject · `j` subjects · `g` daily goal |
| Subject | `q` quiz · `/` filter · `s` study mode · `Esc` back |
| Quiz | `1–4` / `A–D` answer · `Enter` next · `Esc` leave |
| Results | `r` repeat · `b` back to definitions |

All controls are real buttons/inputs and reachable by Tab. Keycaps are shown next to the
relevant actions so shortcuts are discoverable, not folklore.

---

## 10 · Empty states

- **Today:** hatched empty track, `0 / goal`, `nothing logged today — open a subject below`.
- **Activity:** neutral empty grid + `the trail starts with one answer` + `pick a subject →`.
- **Cards:** all mastery bars at baseline, `0%`, `0/n solid`.
- **Subject:** mastery rule at 0%, `new` on every definition rail.
- **Filters:** `nothing in view` with a clear action.
- **Search:** `no subject by that name`.

Never seed fake study history. The UI must look intentional at zero.

---

## 11 · Responsive

Breakpoints: **1140 / 1040 / 980 / 960 / 900 / 820 / 700 / 680 / 620 / 600 / 520 / 380px**.

- 3 subject columns → 2 → 1.
- Daily panel 236px readout + chart → single column; readout becomes one row.
- Heatmap keeps its 53-week internal scroll; aligns to the newest week on narrow screens.
- Activity controls wrap; the less/more legend hides below 680.
- Quiz definition options are 1 column always; term options 2 → 1 at 700; explanation
  labels stack above copy at 520.
- Subject page definition formula hides at 700; mastery bar moves under the line.
- Hero trace hides below 980; top-bar ring hides below 600; nav label hides below 820.
- Top-bar subjects count hides below 380; definition counts hide below 380.
- Page remains usable at 320px without horizontal page scroll.

---

## 12 · Accessibility

- Contrast: body `--ink-2` on white; labels `--ink-3` at ≥9px, not for essential copy.
  Accent text only where contrast permits.
- Every interactive element is a real `button`/`input`/`select`, keyboard reachable,
  with `:focus-visible` (1px ink outline, 3px offset).
- Focus is restored to the trigger when the subject or quiz closes. Tab cycles within
  the open subject/quiz sheet; the shortcuts dialog keeps focus on its close control.
- Quiz options expose numeric and letter shortcuts through `aria-keyshortcuts`.
- Explanations sit in an `aria-live="polite"` region; the result block is visible.
- Tooltips are supplementary; values are also in the DOM or accessible names.
- Icons are `aria-hidden`; controls carry `aria-label`; filter state uses `aria-pressed`.
- Heatmap cells are decorative; the stats and tooltip carry the data. The filter is a
  native select.
- Color is never the only signal for correctness: check/cross, words, and mastery
  percentages accompany it.
- Motion honours reduced-motion. Score count-up is skipped when reduced.

---

## 13 · Voice

Terse, technical, warm. Lowercase structural labels (`today`, `activity`, `focus`,
`quiz`). No exclamation marks. No motivational poster copy. One quiet line at the end of
a quiz is allowed: *every miss is a definition worth re-reading*.

Definitions are one sentence, ≤ 24 words, present tense, no filler.
Formula glyphs are short and real (`h(t)`, `V = IR`, `δ = √(2/ωμσ)`).

---

## 14 · Scope & build rules

- Static HTML/CSS/JS. No frameworks, no build step, no backend.
- State lives in localStorage only. No network writes, no accounts.
- Data constants are clear (`SUBJECTS`) so more subjects can be added without layout
  changes. Anything subject-coloured must degrade gracefully at 30 subjects:
  top-six stacking, neutral heatmap, one filter.
- Reuse tokens and patterns: `.panel`, `.leg`, `.tip`, `.back`, `.btn`, `.filter`,
  `.mbar`, `.mticks`. Do not introduce a second visual language.
- Before adding a new element, ask: can this be a line, a dot, a tick, or a hover?

---

## 15 · New component checklist

- [ ] Uses existing tokens (no new colours except a documented semantic).
- [ ] One accent per surface; white space preserved.
- [ ] 1px rules, not heavy borders.
- [ ] Micro-label uppercase + tracking; content sentence case.
- [ ] Motion 160–700ms with the standard ease; reduced-motion safe.
- [ ] Secondary data revealed on hover/focus, not dumped.
- [ ] Keyboard reachable; focus visible; labels present.
- [ ] Responsive at 320 / 390 / 620 / 960px.
- [ ] Counts are tabular; numbers align.
- [ ] Scales to 30 subjects without adding colour noise.
- [ ] Persists or reads state through the documented store, never ad-hoc keys.
