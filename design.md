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

### Dark paper

Dark mode is a full second palette, not an inverted filter. It ships with the same
hairline discipline and a slightly lifted surface for panels and cards.

| Token | Value | Use |
| --- | --- | --- |
| `--paper` | `#0d0f13` | full sheets, page |
| `--surface` | `#12151b` | panels, cards, quiz card |
| `--surface-soft` | `#171b22` | keycaps, cue chips |
| `--ink` | `#f0f3f8` | primary text |
| `--ink-2` | `#b2bac5` | definitions, body |
| `--ink-3` | `#7d8794` | metadata, mastery stats |
| `--ink-4` | `#505965` | faint labels, empty tracks |
| `--hair` | `#252a33` | rules, borders |
| `--hair-2` | `#1a1e25` | tracks, empty graph cells |
| `--ok` | `#45d99d` | correct, met |
| `--no` | `#ff7e9e` | incorrect |

- **Default is the device theme**, so the page matches the OS until a choice is made.
- The choice is stored under `oneliners.theme` (`light` / `dark`) and restored before
  first paint by an inline head script. There is no flash of the wrong theme.
- There is no install prompt. With no saved choice the theme follows live OS changes;
  once chosen manually, that choice is remembered.
- A day/night toggle lives in the top bar and in the subject toolbar; `t` toggles it
  anywhere. The subject toolbar hides its toggle only below 380px, where the header
  must keep the title legible.
- Subject colours have a separate dark variant (lighter, more luminous) so accents,
  mastery bars, heatmap filters, and the daily stack remain legible on ink.
- The `<meta name="theme-color">` is updated live to `#0d0f13` or `#ffffff`.
- The neutral heatmap, ring, tooltips, overlays, keycaps, shadows, and semantic tints
  all have dark counterparts. `color-scheme` switches so native selects/scrollbars match.

### Subjects (fixed identity)

Each seeded subject has a fixed light/dark accent and a line-art motif. The app reads
subject identity from `SUBJECT_STYLE`; a subject that is not listed yet receives a
deterministic fallback colour and the generic motif, so a new batch never breaks the
layout. The current seeded set:

| Semester | Subject | Colour | Id |
| --- | --- | --- | --- |
| 1-1 | Engineering Physics | `#6f63d8` | `engineering-physics` |
| 1-1 | Matrix Algebra and Calculus | `#3f6fd8` | `matrix-algebra-and-calculus` |
| 1-1 | Problem Solving using C | `#0f9b8e` | `problem-solving-using-c` |
| 1-2 | Engineering Chemistry | `#c9852a` | `engineering-chemistry` |
| 1-2 | Data Structures | `#2a9668` | `data-structures` |
| 1-2 | Advanced Calculus | `#5966d8` | `advanced-calculus` |
| 1-2 | Electrical Circuits & Networks Analysis | `#d95376` | `electrical-circuits-and-networks-analysis` |
| 2-1 | Electronic Devices and Circuits | `#d97a2b` | `electronic-devices-and-circuits` |
| 2-1 | Signals and Systems | `#2f7fc1` | `signals-and-systems` |
| 2-1 | Probability Theory and Stochastic Process | `#8a5fc4` | `probability-theory-and-stochastic-process` |
| 2-1 | Complex Variable and Transform Techniques | `#5b7fa8` | `complex-variable-and-transform-techniques` |
| 2-1 | Business Economics and Financial Analysis | `#a67c2e` | `business-economics-and-financial-analysis` |
| 2-1 | Environmental Science | `#5d8a3f` | `environmental-science` |
| 2-2 | Analog Circuits | `#cc5c48` | `analog-circuits` |
| 2-2 | Digital Logic Design | `#2a8fa8` | `digital-logic-design` |
| 2-2 | Analog & Digital Communications | `#1f9d78` | `analog-and-digital-communications` |
| 2-2 | Electromagnetic Waves and Transmission Lines | `#b06a9b` | `electromagnetic-waves-and-transmission-lines` |
| 2-2 | Quantitative Aptitude and Logical Reasoning | `#6d7f94` | `quantitative-aptitude-and-logical-reasoning` |
| 2-2 | Universal Human Values | `#8b7a5c` | `universal-human-values` |
| 3-1 | Antennas and Wave Propagations | `#7b6fd8` | `antennas-and-wave-propagations` |
| 3-1 | Linear Control Systems | `#c07a2e` | `linear-control-systems` |
| 3-1 | Artificial Intelligence | `#3f8f6b` | `artificial-intelligence` |
| 3-1 | Digital Signal Processing | `#4f6fd0` | `digital-signal-processing` |
| 3-1 | IC Applications | `#b07a2e` | `ic-applications` |
| 3-2 | Microprocessors and Microcontrollers | `#7a5bc4` | `microprocessors-and-microcontrollers` |
| 3-2 | VLSI Technology and Design | `#2a8fa8` | `vlsi-technology-and-design` |
| 3-2 | Microwave and Optical Communications | `#1f9d78` | `microwave-and-optical-communications` |
| 3-2 | Cyber Security | `#b05454` | `cyber-security` |
| 3-2 | Python Programming | `#3f7fa8` | `python-programming` |
| 4-1 | Advanced Communications and Networks | `#3f6fb0` | `advanced-communications-and-networks` |
| 4-1 | Internet of Things and Applications | `#2a9668` | `internet-of-things-and-applications` |
| 4-1 | Computer Networks | `#5b7fa8` | `computer-networks` |
| 4-1 | Embedded Real Time Operating Systems | `#8a6a3f` | `embedded-real-time-operating-systems` |
| 4-1 | System on Chip Architecture | `#6b5fa8` | `system-on-chip-architecture` |

The final data set has **41 subject slots**: 34 with definitions (33 complete/partial plus
Python Programming as unresolved) and 7 no-data stubs. Stubs keep their palette entries for
a future retry but render as quiet `not seeded` annotations, never as empty cards. The 4-2
project semester renders as a single no-material note.

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

The study set is data-driven: `data/curriculum.json` (41 subject slots, 34 with
definitions, 1,575 one-liners), one file per subject under `data/subjects/<semester>/`, and
`data/sources.json` (250 catalogued source files). Every definition keeps its `sources[]`
locators; the hover tooltip shows the first source file and page/slide. Unresolved and
no-material slots are rendered as quiet `not seeded` annotations, never as empty cards.
`4-2` renders as a no-material project-semester note.

Everything else is client-side. The static HTML app uses two localStorage keys:

```
oneliners.state.v1    // goal, mastery, history
oneliners.theme       // "light" | "dark"; default follows the device
```

Shape:

```js
{
  goal: 100,                 // 10–999
  mastery: {
    "electronic-devices-and-circuits|Intrinsic semiconductor": {
      attempts: 4, correct: 3, score: 0.9, streak: 3, last: 172...
    }
  },
  history: {
    "2026-10-24": {
      total: 41,
      subjects: {
        "electronic-devices-and-circuits": 12,
        "signals-and-systems": 9,
        "data-structures": 8
      }
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
- Theme changes are remembered separately from progress; reset progress does not reset theme.
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
64px, translucent paper with 14px blur, hairline bottom. Brand left. Right: daily ring,
a scalable **subjects jump** pill (3×3 dot grid, count), a theme toggle (sun / moon), and
a keyboard `?` button. The theme toggle also appears in the subject toolbar.
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
A section head (`subjects`, the studyable count, and `n not seeded`) and an inline search
with `/` key hint. All **eight semesters** render in A22 order (`1-1` → `4-2`), even when a
semester has no definitions. Each group has a two-digit index, the semester label, and a
quiet `n subjects · n definitions` count. The grid inside a group is 3 → 2 → 1 columns.

Unresolved and no-material slots sit under the grid in a hairline `not seeded` row
(`Technical Seminar · no materials`, `Open Elective I · unresolved`, and so on). `4-2`
renders as a dashed no-material note. Search filters cards and whole semester groups live;
a group disappears when none of its subjects match. Clearing the search restores all eight
groups.

### Subject cards
White, hairline, 16px radius, min-height 196px. A large thin-line motif sits behind the
content at 15% opacity, rising to 32% on hover. Top row: dot, name, a micro line with the
official course code and `n units` (or `partial` / `unresolved`), and overall mastery %.
Bottom row: **one thin vertical bar per definition**, height and opacity scaled by that
definition's mastery (4px baseline when new), and `solid/total solid`. The bars form a tiny
memory profile for the subject. Hovering the bar strip reveals the overall summary. No fake
mini-contribution graph remains.

### Subject page
Full-screen white sheet that rises 18px and fades in. Sticky toolbar: back, subject,
filter, study-eye.

- Hero: name, a context line (`semester · code · coverage · n sources`, with
  `partial · 3/6 units` where coverage is incomplete), `n one-liners`, a 180px mastery rule
  filled to the overall %, `x% remembered`, a `quiz yourself` pill with a `q` keycap, and a
  20-tick daily strip.
- `focus` filters: `all · new · learning · solid` with counts. They combine with the
  text filter; the visible count reads `x of n`. An empty view offers a one-click clear.
- Definitions are a chronological rail: 1px line, 9px hollow nodes, term 400, definition
  300. Each row has a right rail: the **mastery percentage** above a 2px 94px bar.
  Hovering the row swaps the percentage for the formula and fills the node; the tooltip
  adds the source file and page/slide locator.
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
Hairline surface pills for graph cells, week bars, card mastery ticks, definition rails,
and quiz ticks. The activity heatmap and daily stack use richer floating cards described
above. Tooltips never take pointer events, and never contain the only copy of important
information.

### PWA shell
- `manifest.webmanifest` — standalone display, scope `./`, light launch colours, 192/512
  icons, a maskable 512, and install screenshots (wide home, wide quiz, narrow phone).
- `sw.js` — precaches the app shell (`index.html`, manifest, icons, Inter), the curriculum
  index, `data/sources.json`, and every subject file listed in `data/curriculum.json`. It
  uses network-first navigation with a cached-index fallback, network-first curriculum
  JSON (so a new batch appears immediately online, with a cached fallback offline), and
  stale-while-revalidate for same-origin assets. It works fully offline after one visit.
- **No install dialog is ever shown.** No `beforeinstallprompt` handler exists. Installation
  is left to the browser/OS menu. The manifest has the stable id `/ECEDefinitions/` so it
  cannot collide with another app on the same origin; macOS Chrome exposes install from the
  omnibox or **⋮ → Cast, save, and share → Install page as app**.
- **Self-hosted Inter** (variable WOFF2) so typography survives offline and there is no
  third-party font request. OFL text ships with it.
- Metadata: canonical URL, Open Graph 1200×630 image, Twitter large card, JSON-LD
  `WebApplication`, favicon set, Apple touch icon and standalone metadata, `msapplication`
  tile colour.
- `<meta name="theme-color">` follows the active theme (`#ffffff` / `#0d0f13`). Theme is
  restored by an inline head script before first paint.
- The subject toolbar hides its theme toggle below 380px to protect the title; the top-bar
  toggle and the `t` shortcut remain.

---

## 09 · Keyboard map

| Context | Keys |
| --- | --- |
| Anywhere | `?` shortcuts · `Esc` close/back · `t` toggle theme |
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

Definitions are one sentence, ≤ 28 words, present tense, no filler.
Formula glyphs are short and real (`h(t)`, `V = IR`, `δ = √(2/ωμσ)`).

---

## 14 · Scope & build rules

- Static HTML/CSS/JS. No frameworks, no backend. A stdlib Python script builds the
  curriculum index; the app itself has no runtime build step.
- Ships as a PWA: manifest, offline service worker, maskable icons and complete social
  metadata. Any change to a precached asset requires a service-worker cache bump.
- No install prompts, no OS-theme override, no analytics, no third-party runtime requests.
- State lives in localStorage only. No network writes, no accounts.
- Curriculum is loaded from `data/curriculum.json`; every data-bearing subject has a file
  under `data/subjects/<semester>/`, and `data/sources.json` holds the source manifest.
  `scripts/build-curriculum-index.py` rebuilds the index from those files while preserving
  unresolved/no-material stubs and syllabus unit counts; `scripts/validate-seed-data.py`
  checks the final dataset. `SUBJECT_STYLE` maps known identities; unknown subjects get a
  deterministic fallback colour and the generic motif. Anything subject-coloured must
  degrade gracefully at 30+ subjects: top-six stacking, neutral heatmap, one filter, and
  stubs as annotations rather than cards.
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
- [ ] Works in both themes, with all dynamic colours re-rendered on toggle.
- [ ] Works offline, and any new asset is added to the service-worker cache list.
