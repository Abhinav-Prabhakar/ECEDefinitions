<div align="center">
  <img src="assets/og.png" alt="one·liners — Electronics, in one line." width="100%" />
</div>

<div align="center">

# one·liners

**Electronics, in one line.**

A quiet ECE study instrument: 1,113 real definitions across 24 subjects, grouped by
semester, with a daily practice stack, adaptive two-way quizzes, and a memory of what you
actually know.

<a href="https://abhinav-prabhakar.github.io/ECEDefinitions/">
  <img src="https://img.shields.io/badge/OPEN_THE_APP-live-5b6ee1?style=for-the-badge&logo=githubpages&logoColor=white" alt="Open the live app" />
</a>

<br /><br />

<img src="https://img.shields.io/badge/PWA-offline--ready-14161a?style=flat-square&logo=pwa&logoColor=white" alt="PWA offline ready" />
<img src="https://img.shields.io/badge/dark%20mode-remembered-9b6ae0?style=flat-square" alt="Dark mode" />
<img src="https://img.shields.io/badge/storage-localStorage-5b6ee1?style=flat-square" alt="localStorage" />
<img src="https://img.shields.io/badge/backend-none-22a06b?style=flat-square" alt="No backend" />
<img src="https://img.shields.io/badge/vanilla-HTML%20%C2%B7%20CSS%20%C2%B7%20JS-eaa22b?style=flat-square" alt="Vanilla HTML CSS JS" />
<img src="https://img.shields.io/badge/deploy-GitHub%20Pages-14161a?style=flat-square&logo=github&logoColor=white" alt="GitHub Pages" />

</div>

<p align="center"><sub>Screenshots use sample study data. The app itself starts clean, on your device.</sub></p>

---

## Why this exists

ECE is full of definitions that are one sentence long and three lectures deep. Most study
apps bury them under dashboards. **one·liners** does the opposite: one line per definition,
one deliberate action per day, and a memory layer that stays out of the way until you need it.

White paper, hairline rules, thin type. Subject colour appears only where it carries meaning.
No accounts, no server, no noise.

> **Recognition is not recall.** So the quiz asks in both directions.

---

## Screenshots

<table>
  <tr>
    <td width="50%">
      <img src="assets/screenshot-home-light.png" alt="one·liners home in light mode" width="100%" />
      <p align="center"><sub><strong>Light by default</strong> · today, activity, subject mastery</sub></p>
    </td>
    <td width="50%">
      <img src="assets/screenshot-home-dark.png" alt="one·liners home in dark mode" width="100%" />
      <p align="center"><sub><strong>Dark when you choose it</strong> · remembered across visits</sub></p>
    </td>
  </tr>
</table>

<table>
  <tr>
    <td width="58%">
      <img src="assets/screenshot-subject-light.png" alt="Signals and Systems definitions with per-definition mastery bars" width="100%" />
      <p align="center"><sub><strong>Every definition has a memory.</strong> Hover a row for its mastery; hover again for its formula.</sub></p>
    </td>
    <td width="42%">
      <img src="assets/screenshot-quiz-dark.png" alt="A two-way quiz in dark mode with an explanation" width="100%" />
      <p align="center"><sub><strong>Answers explain themselves.</strong> The cue, the definition, and what you picked.</sub></p>
    </td>
  </tr>
</table>

<div align="center">
  <img src="assets/screenshot-mobile-subject.png" alt="one·liners on a phone" width="310" />
  <p><sub><strong>320 → 1440px.</strong> The same quiet interface, not a crushed desktop.</sub></p>
</div>

---

## The curriculum, by semester

The home page is the A22 map, not a flat list. Subjects sit under their semester — **I Year
· I Semester** through **IV Year · II Semester** — with the official course code, unit
count, and a subject-specific line diagram. Colour is the subject's identity, used in small
doses.

The first shipped batches cover **1-1 through 3-1** (24 subjects, 1,113 definitions). Later
semesters appear as their source material is seeded. The workflow is deliberately boring:

```bash
# 1. subject JSON files arrive under data/subjects/<semester>/
# 2. rebuild the index the app reads
python3 scripts/build-curriculum-index.py
# 3. commit the data and the index
```

The app fetches `data/curriculum.json` at runtime, so a new batch adds a new semester group
without touching the UI. Subjects still being seeded are simply absent — never faked.
Definitions are derived from the SNIST ECE A22 materials; raw source files are not
redistributed.

---

## Two directions of recall

Every round mixes both question types, balanced 5/5. You cannot coast on recognition.

| Prompt | You choose | What it trains |
| --- | --- | --- |
| `Convolution` | one of four definitions | term → meaning |
| “The output of an LTI system is the input convolved with its impulse response.” | one of four terms | meaning → term |

- **Adaptive sampling.** The three weakest definitions are guaranteed a slot; the remaining
  slots are weighted toward low mastery.
- **Keyboard complete.** Press <kbd>1</kbd>–<kbd>4</kbd> or <kbd>A</kbd>–<kbd>D</kbd> to
  choose, <kbd>Enter</kbd> for the next question, <kbd>Esc</kbd> to leave, <kbd>r</kbd> to
  repeat a round, <kbd>b</kbd> to go back.
- **Explanations, not just verdicts.** Every answer reveals the canonical definition, a
  formula cue, and — when wrong — the definition of the option you chose.
- **A live memory readout.** The mastery bar moves after every answer, with the delta.

<div align="center">
  <img src="https://img.shields.io/badge/1%20round-10%20questions%20%C2%B7%205%20%2B%205-12b3a6?style=flat-square" alt="10 questions, 5 of each type" />
  <img src="https://img.shields.io/badge/adaptive-3%20weakest%20guaranteed-e0567f?style=flat-square" alt="Adaptive sampling" />
</div>

---

## A memory you can see

Mastery is a single confidence score per definition, stored locally:

| After | Score | Reads as |
| --- | --- | --- |
| no attempts | 0% | `new` |
| 1 correct | 30% | `learning` |
| 2 correct | 60% | `familiar` |
| 3 correct | 90% | `solid` |
| 4 correct | 100% | `solid` |
| a miss | −40% | re-learn |

- **Subject page:** a percentage and a 2px bar on every definition, plus an aggregate rule
  under the subject title. Filter the list by `all · new · learning · solid`.
- **Subject cards:** a tiny bar profile of every definition, the overall remembered %, and
  the solid count.
- **Quiz:** the mastery row updates live after each answer, with a plus or minus delta.
- **Home:** the hero shows the overall remembered percentage; the daily stack and cards
  update as soon as you return from a round.

---

## The day, in one stack

- One stacked bar, one colour per subject, against a daily goal of your choosing
  (default 100; type it or use ±10; clamped 10–999).
- Done / goal, percentage, “left today”, and a seven-day sparkline.
- Hover a segment or its legend row for that subject's count and share of the goal.
- The top six subjects are shown; the rest become one neutral `other` segment. It scales
  to thirty subjects without turning into a rainbow.
- The goal and counts persist across reloads. Today resets at local midnight.

---

## A quieter activity trail

The original six-colour contribution graph was too loud — and would only get louder with
thirty subjects. It is now a **neutral, monochrome heatmap**:

- Intensity is relative to your busiest day in the current view, not a fixed palette.
- Filter by **one** subject to recolour the map in that subject's hue and make the stats
  filter-aware.
- Hover or tap a cell for the date, total, and subject breakdown.
- Answered · day streak · best day.

The heatmap scrolls internally on phones and aligns to the newest week. No fake history,
no seeded cells.

---

## Offline, installable, and calm about it

- **Full PWA:** `manifest.webmanifest`, a service worker, maskable icons, Apple touch icon,
  safe Apple metadata, and a cached app shell. It works offline after the first load.
- **No install dialog inside the app.** Install from the browser/OS UI:
  - **macOS Chrome:** in a normal (non-Incognito) window, use the install icon at the right
    of the address bar (a monitor with a down arrow) or **⋮ → Cast, save, and share →
    Install page as app**. If it is already installed, launch it from `chrome://apps`.
  - **macOS Safari:** **File → Add to Dock**.
  - **iOS Safari:** **Share → Add to Home Screen**.
  - **Android Chrome:** **⋮ → Install app** (or “Add to Home screen”).
  - **Windows/Linux Chrome or Edge:** install icon in the address bar, or the browser's
    **Install app** menu item.
- **Stable app identity:** the manifest uses the unique id `/ECEDefinitions/`, so the
  installation cannot collide with another app on the same origin.
- If you installed a pre-release build from before the id was added, remove that old entry
  from `chrome://apps` and install once more. Progress is stored per origin, so your study
  data is unaffected.
- **Self-hosted Inter** (variable WOFF2) — no external font request, no flash of the wrong
  typeface offline.
- **Theme:** always light by default, even when the OS is dark. Once you choose dark, it
  is remembered in `localStorage` and restored before first paint. `<meta name="theme-color">`
  follows it.
- **Complete metadata:** canonical URL, Open Graph, Twitter card, JSON-LD `WebApplication`,
  favicon set, and a custom social image.

---

## Keyboard first

| Anywhere | |
| --- | --- |
| <kbd>?</kbd> | keyboard shortcuts |
| <kbd>Esc</kbd> | close / go back |
| <kbd>t</kbd> | toggle dark mode |
| <kbd>/</kbd> | find a subject |
| <kbd>j</kbd> | browse subjects |
| <kbd>g</kbd> | jump to the daily goal |

| Subject | |
| --- | --- |
| <kbd>q</kbd> | start a quiz |
| <kbd>/</kbd> | filter definitions |
| <kbd>s</kbd> | study mode |

| Quiz | |
| --- | --- |
| <kbd>1</kbd>–<kbd>4</kbd> or <kbd>A</kbd>–<kbd>D</kbd> | choose an answer |
| <kbd>Enter</kbd> | next question |
| <kbd>r</kbd> | run the round again |
| <kbd>b</kbd> | back to definitions |

All controls are real buttons and inputs, reachable with Tab. Focus is restored when a
sheet closes and held inside an open subject or quiz.

---

## Under the hood

| | |
| --- | --- |
| **Stack** | Static HTML, CSS and vanilla JavaScript. No framework. A stdlib Python script builds the data index. |
| **Data** | `data/curriculum.json` + one file per subject under `data/subjects/<semester>/`. |
| **Storage** | `localStorage` — `oneliners.state.v1` for progress, `oneliners.theme` for the theme. |
| **Offline** | Hand-written service worker; precaches the app shell and every seeded subject file. |
| **Type** | Self-hosted Inter variable font. |
| **Hosting** | GitHub Pages, static. |
| **Privacy** | No accounts, no analytics, no network writes. Progress never leaves the device. |

```js
// What the memory actually looks like
{
  goal: 120,
  mastery: {
    "electronic-devices-and-circuits|Intrinsic semiconductor":
      { attempts: 4, correct: 3, score: 0.9, streak: 2, last: 172… }
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

The footer offers a two-step reset. It clears progress but keeps your theme and goal.

---

## Run it locally

```bash
# A server is required: the app fetches its curriculum data.
python3 -m http.server 8000
# → http://localhost:8000/
```

Opening `index.html` directly blocks the data fetch in most browsers. The live GitHub
Pages build serves everything over HTTPS. There is nothing to install or compile; the
curriculum index is already committed.

---

## Project map

```text
.
├── index.html                        # the entire app
├── design.md                         # the design system / source of truth
├── manifest.webmanifest              # PWA manifest
├── sw.js                             # offline app shell + data cache
├── .nojekyll                         # keep GitHub Pages static
├── data/
│   ├── curriculum.json               # semester index the app loads
│   └── subjects/<semester>/*.json    # one file per subject
├── scripts/
│   └── build-curriculum-index.py     # rebuild curriculum.json from subject files
├── prompts/
│   └── seed-curriculum-agent.md      # source-extraction brief
└── assets/
    ├── icon.svg                      # brand mark
    ├── icon-192.png                  # PWA icon
    ├── icon-512.png                  # PWA icon
    ├── icon-maskable-512.png         # Android adaptive icon
    ├── apple-touch-icon.png          # iOS
    ├── favicon-32.png                # fallback favicon
    ├── og.png                        # social card
    ├── screenshot-*.png              # README images
    └── fonts/
        ├── inter-latin-var.woff2
        └── OFL.txt
```

---

## Design notes

The full system lives in **[`design.md`](design.md)**. The short version:

- White is a material. Hairlines over boxes. Weight 200–400 Inter, never bold.
- Colour is a subject's identity, used in small doses.
- Hover is an information layer; nothing essential hides there.
- Every component must survive thirty subjects without adding colour noise.
- Default light. Remember dark. No install prompt. No backend.

### Credits

Inter by Rasmus Andersson, licensed under the SIL Open Font License 1.1
(see `assets/fonts/OFL.txt`). Built for ECE students who like their definitions in one line.

<div align="center">
  <sub>If this helps you learn something, star the repo. It is a good nudge to keep the trail growing.</sub>
</div>
