# Agent brief: build a one·liners collection for `{{TOPIC}}`

**Topic for this run:** `{{TOPIC}}`

You are the **orchestrator**. Your job is to turn one topic into a complete, sourced,
quiz-ready collection in the one·liners data format, by planning the taxonomy, launching one
subagent per subject, verifying their work, merging it, validating it, and reporting
honestly on coverage.

You do **not** wire the app. You produce data.

## Terminology

Use the project's words, not flashcard words.

| Term | Meaning |
| --- | --- |
| **Definition** (or **one-liner**) | The atomic unit: a term, one sentence, and an optional cue. |
| **Subject** | A group of definitions with a shared scope, e.g. Word Parts. |
| **Section** | An optional grouping of subjects inside a collection, e.g. Core or Advanced. |
| **Collection** | A set of subjects for one topic, e.g. Medical Terminology. |
| **Library** | All collections under `data/collections/`. |

Do not call a definition a "card". Do not call a collection a "deck".

---

## 0 · How to invoke this file

The topic is supplied by the user alongside this file. It may be written as:

```
Use prompts/generate-collection-agent.md for: Medical terminology
```

or:

```
TOPIC: AWS Solutions Architect Associate
```

The topic will usually be one row or sub-collection from `DOMAIN-CATALOG.md`. Use that family as a
starting point for scope, but verify the taxonomy and sources yourself.

If the caller also supplies a **scope line** (for example from `COLLECTION-QUEUE.md`), treat
it as authoritative: build the subjects it lists, and do not re-narrow the topic to a single
sub-collection.

Rules:

1. If `{{TOPIC}}` has been replaced with a real topic, use it.
2. If it is still the literal placeholder, use the topic in the user's accompanying message.
3. If neither exists, stop and ask for the topic. Do not guess.
4. Read this entire file before acting. Do not skip the schema or validation sections.
5. Work in the repository root. Before planning, read:
   - `DOMAIN-CATALOG.md` if it exists, for scope hints;
   - `COLLECTION-QUEUE.md` if it exists, for the active order; do not edit it from inside a
     collection run — the caller marks the queue item when the run is accepted;
   - `design.md`, for the visual constraints that affect colors and naming;
   - `prompts/seed-curriculum-agent.md`, for the source-traceability philosophy;
   - one existing `data/subjects/**/*.json`, for a concrete definition example.

If a referenced file does not exist, continue without it. Do not block on missing context.

---

## 1 · Mission

Produce a collection for the topic that contains:

- a bounded scope and audience,
- 1–8 subjects, grouped into 1–3 sections,
- 120–800 definitions, depending on the topic,
- 2–3 `confusables` per definition,
- a source manifest with a locator for every definition,
- a runtime bundle the app can consume,
- a validator that proves the collection is internally consistent,
- a coverage report that states what is missing and why.

The collection must be **useful on day one**: a learner should be able to open it, study a
subject, take a two-way quiz, and feel that the definitions were chosen by someone who knows the
field — not scraped from a glossary.

---

## 2 · What "good" means

A good collection passes five tests:

| Test | Question |
| --- | --- |
| **Scope** | Is it clear who this is for and what it excludes? |
| **Coverage** | Does every subject cover its units, not just its easiest terms? |
| **Quiz viability** | For each definition, are there 2–3 plausible wrong answers in the collection? |
| **Source grounding** | Can a reviewer open the cited locator and find support for the definition? |
| **Restraint** | Is every definition worth learning, or is the collection padded to hit a number? |

A smaller, accurate, well-chosen collection beats a large, generic one. Never pad.

---

## 3 · Non-negotiables

1. **No fabrication.** Every definition must be supported by a cited source. If you cannot
   source it, omit it. Model memory is allowed for *finding* and *judging* sources, never as
   the citation.
2. **No raw source files in the repo.** Download PDFs, slides, and pages to a temporary
   directory such as `/tmp/oneliners-<collection>/`. Commit only derived JSON, metadata, reports,
   and the validator.
3. **No app edits.** Do not edit `index.html`, `design.md`, the root `README.md`,
   `manifest.webmanifest`, `sw.js`, or `assets/`. Data and tooling only.
4. **Source traceability.** Every definition has one or more `sources` entries of the form
   `"<sourceId>#<locator>"`, and every `sourceId` resolves in `sources.json`.
5. **Quality over quota.** Do not duplicate an idea across units to hit a count. Do not
   include a term just because it appears in a source.
6. **One sentence, 8–28 words.** Standalone, technical, readable without the source.
7. **Quiz viability.** Prefer terms with real near-neighbours. If you cannot name two
   plausible wrong answers, the definition is probably not quiz-shaped.
8. **Stable IDs.** Kebab-case, ASCII, deterministic. Re-running the pipeline should produce
   the same IDs.
9. **Honest coverage.** Mark subjects `partial` or `inaccessible` rather than inventing
   content. Report gaps in the README.
10. **No advice.** A medical, legal, or financial collection is a vocabulary collection, not
    professional advice. Include the disclaimer.

---

## 4 · Phase 0 — scope and taxonomy

Do this before launching any extraction subagent. Write the result to
`data/collections/<collection-slug>/plan.json`.

### 4.1 Classify the topic

| Topic type | Structure | Example |
| --- | --- | --- |
| **Exam or certification** | Official blueprint domains become subjects; units are subdomains | AWS SAA, NCLEX, CFA Level I |
| **Academic course** | Syllabus units become subjects or units within one subject | Organic chemistry |
| **Professional field** | Job-task areas become subjects | Product management |
| **Hobby** | Beginner-to-intermediate concept map | Wine, chess, photography |
| **Language** | Grammar and usage concepts, not raw word lists | Japanese, Spanish |
| **General knowledge** | Curated lists by category | World capitals, chemical elements |

### 4.2 Bound the scope

A topic must fit one collection. If it is broader than that, choose the highest-demand entry
point and record the exclusions.

Examples:

| Topic | Do not attempt | Build instead |
| --- | --- | --- |
| Medicine | All of medicine | Medical terminology for pre-health students |
| Law | Every jurisdiction | US legal literacy, federal and general common law |
| Finance | All finance | Corporate finance and accounting fundamentals |
| AI | All of AI | LLM and ML concepts for practitioners |
| Science | All science | Scientific literacy for adults |
| History | All history | 20th-century world history, key events and terms |

State the choice in `scope.includes`, `scope.excludes`, and `scope.assumptions`.

If the topic is a catalog **family** (e.g., "Health & medicine"), do not build the whole
family. Pick the highest-demand sub-collection (e.g., "Medical terminology") as the entry point
and state the choice. The family can become a second collection later.

### 4.3 Set defaults

Use these unless the topic or the user says otherwise. Record every default in `plan.json`.

| Dimension | Default |
| --- | --- |
| Audience | A motivated beginner or early-career practitioner |
| Level | `intro` |
| Jurisdiction | `US` for law, medicine, finance, and trades; `global` for science and tech |
| Spelling | `US` unless the topic is explicitly UK, Indian, Australian, or Canadian |
| Exam version | The current published blueprint; record the year |
| Language variant | The most widely spoken standard (e.g., Latin American Spanish) |
| Units | Official blueprint or syllabus; otherwise a 4–6 part concept map |
| Definition budget | 250–400 standard; 120–250 narrow; 500–800 deep exam collections |

If a wrong default would produce **misleading** data — a law collection with no jurisdiction, an
exam collection with the wrong version, a language collection with the wrong variant — ask **one**
clarifying question and stop. Otherwise proceed and document the assumption.

### 4.4 Design the taxonomy

Aim for 1–8 subjects. Use fewer when the topic is genuinely one subject; do not inflate.

Group subjects into 1–3 sections when the topic has natural levels or parts (for example
`core` / `advanced`, or exam parts). A simple collection has one section, `core`.

- **Exam:** one subject per official domain. Use the domain names verbatim.
- **Course:** one subject per major unit, or one subject with units if the course is small.
- **Field:** one subject per job-task area.
- **Hobby:** one subject per layer of the hobby (e.g., grapes, winemaking, tasting, service).
- **Language:** one subject per concept area (writing system, particles, verb forms,
  politeness, counters), not per vocabulary list.
- **General knowledge:** one subject per list category.

Each subject gets:

- a kebab-case `id`,
- a display `name`,
- a `shortName` of 2–3 words,
- 3–8 `units` with exact titles,
- a target definition count (40–80 standard; 8–20 per unit),
- 2–4 source queries or candidate sources.

### 4.5 Assign colors

Use the palette below, in order, one per subject. Record both the light and dark values.
Do not invent colors.

| Light | Dark |
| --- | --- |
| `#5b6ee1` | `#8a9bff` |
| `#12b3a6` | `#3bd6c7` |
| `#eaa22b` | `#f3b552` |
| `#e0567f` | `#ff7f9f` |
| `#22a06b` | `#4bd399` |
| `#9b6ae0` | `#bb95ff` |
| `#2f80ed` | `#6aa8ff` |
| `#d97706` | `#f0a43c` |
| `#0ea5e9` | `#4cc4f5` |
| `#84cc16` | `#a8e04a` |

### 4.6 Write the plan

`plan.json` is committed. It is the provenance of the scope decision.

Naming rules:

- `collectionId` is the kebab-case slug of the topic, ≤40 characters. Drop exam years unless the
  year is part of the official name. Example: `aws-solutions-architect-associate`.
- If `data/collections/<collectionId>/` already exists, do not overwrite it silently. Stop and ask
  whether to replace it, version it (`-v2`), or merge. The same rule applies to
  `data/collections/index.json`.
- Subject and definition ids are kebab-case ASCII, stable across runs.

```json
{
  "version": 1,
  "topic": "Medical terminology for pre-health students",
  "collectionId": "medical-terminology",
  "type": "course",
  "audience": "Pre-health undergraduates and nursing students",
  "level": "intro",
  "jurisdiction": "US",
  "spelling": "US",
  "language": "en",
  "regulated": true,
  "includes": [
    "prefixes, roots, suffixes and combining forms",
    "major body systems",
    "clinical abbreviations and documentation"
  ],
  "excludes": [
    "diagnosis and treatment protocols",
    "drug dosing",
    "advanced pathology"
  ],
  "assumptions": [
    "US clinical usage",
    "no prior anatomy assumed"
  ],
  "sections": [
    {
      "id": "core",
      "label": "Core",
      "subjects": [
        {
          "id": "word-parts",
          "name": "Word Parts",
          "shortName": "Word parts",
          "units": ["Prefixes", "Roots", "Suffixes", "Combining forms"],
          "targetDefinitions": 48,
          "sourceQueries": [
            "OpenStax medical terminology prefixes roots suffixes",
            "NLM medical terminology glossary"
          ]
        }
      ]
    }
  ],
  "definitionBudget": { "min": 250, "max": 400 },
  "disclaimer": "Educational vocabulary only; not medical advice."
}
```

The `sections` array is truncated for readability. A real plan lists every section and
subject, its units, and its target definition count, and the targets add up to the
definition budget.

### 4.7 Stop and check

Before Phase 1, confirm:

- the topic fits one collection;
- the subjects are distinct and non-overlapping;
- each subject has 3–8 units;
- the definition budget is realistic for the available sources;
- every subject has at least one plausible authoritative source;
- the plan does not require a subject you cannot source.

If a subject has no plausible source, remove it from the plan or mark it `inaccessible`.
Do not launch an extraction subagent for it.

---

## 5 · Phase 1 — source and extraction subagents

Launch **one subagent per subject**. Use the `subagent` tool with the `general` agent.
Maximum **5 concurrent**; run in waves if there are more subjects. The cap is on
concurrency, not on the total number of subagents: launch as many as the taxonomy needs.

If a subject is unusually large (more than ~100 definitions), split it into two subagents by unit
range and merge afterwards. Do not split by definition count alone; keep each unit in one
subagent so terminology stays consistent.

### 5.1 What each subagent must do

1. **Find sources.** Use web search and fetch to locate 1–4 authoritative sources for its
   subject. Read them; do not cite search snippets.
2. **Audit access.** Record each source's URL, title, publisher, license, status, and
   locator scheme. If a source is paywalled or unreadable, mark it and find an alternative.
3. **Extract and paraphrase.** Write 40–80 quiz-ready definitions (or the target in the brief)
   covering every unit. Every definition must be supported by a cited locator.
4. **Assign units.** Use the unit number and exact unit title from the plan.
5. **Add confusables.** For each definition, name 2–3 other terms in the subject (or collection) that
   are plausible wrong answers. They must be real terms that will exist in the final collection.
6. **Write only its subject file.** No edits to `plan.json`, `collection.json`, `sources.json`,
   other subjects, the README, or app files.
7. **Report back.** Counts, units covered, sources used, skipped items, access problems, and
   the path written.

### 5.2 What each subagent receives

Use the template in §12. Fill every placeholder. Do not send a subagent a vague instruction
like "write some definitions about pharmacology." Give it the unit list, the definition budget, the
source candidates, the schema, and the rules.

### 5.3 Failure handling

- If a subagent fails or returns invalid JSON, retry **once** with a fresh context and the
  failure report.
- If it still fails, keep any valid definitions it wrote, mark the subject `partial`, and record
  the reason in the coverage report.
- If a subject yields fewer than 20 sourced definitions, mark it `partial`. Do not pad.
- If more than 25% of subjects are inaccessible, produce a partial collection and say so clearly.

### 5.4 What the orchestrator does during this phase

- Launch waves, not all at once.
- Do not extract definitions yourself; your job is to brief, merge, verify, and validate.
- Read each returned file. Do not trust the report alone.
- Reject definitions that are unsourced, padded, duplicated, or not quiz-shaped.

---

## 6 · Phase 2 — verification

After the subject files are merged, launch **two verifier subagents**. Split the subjects
between them. They do not edit files; they return a fix list.

Each verifier checks:

| Check | What to look for |
| --- | --- |
| **Support** | Does the cited locator actually support the definition? |
| **Paraphrase** | Is the definition copied verbatim from the source? |
| **Accuracy** | Is the definition correct, current, and not misleading? |
| **Scope** | Is this the sense of the term used in this collection? |
| **Word count** | Is it 8–28 words? |
| **Term fit** | Does the definition define the term, not an example or formula? |
| **Distractors** | Are the `confusables` real terms, non-synonyms, and plausible? |
| **Duplication** | Is the same term or idea repeated across subjects? |
| **Neutrality** | Does it avoid advice, marketing, and contested claims? |

Verification coverage:

- Collections up to 150 definitions: verify every definition.
- Collections of 150–300 definitions: verify at least 50%, stratified across every subject and unit.
- Collections over 300 definitions: verify at least 30%, stratified, plus every definition in any subject
  marked `partial`.

Verifier output:

```json
{
  "version": 1,
  "collectionId": "medical-terminology",
  "verifier": 1,
  "checked": 84,
  "results": [
    {
      "subjectId": "word-parts",
      "definitionId": "tachycardia",
      "status": "ok",
      "reason": ""
    },
    {
      "subjectId": "word-parts",
      "definitionId": "bradycardia",
      "status": "fix",
      "reason": "Definition says 'slow heart' but the source specifies 'resting rate below 60 bpm'.",
      "suggestedFix": "A resting heart rate below 60 beats per minute."
    }
  ]
}
```

The orchestrator applies fixes, re-sources or removes unsupported definitions, then re-runs the
validator. If a fix changes a term, update every reference to it in `confusables`.

---

## 7 · Phase 3 — merge and derive

Do this only after the subject files pass a first validation pass.

1. **Deduplicate.** Remove exact duplicates of `(term, definition)` across the collection. If the
   same term appears in two subjects with different meanings, qualify the term
   (e.g., `Duration (finance)`) and keep both only if both are in scope.
2. **Normalize.** Sort definitions by `unit`, then `term`. Sort sections by plan order,
   and subjects within each section by plan order. Sort sources by `id`. Use 2-space JSON,
   UTF-8, LF, trailing newline.
3. **Build `collection.json`.** Compute counts and coverage from the subject files. Never
   hand-maintain counts.
4. **Build `sources.json`.** Merge the per-subject source lists. Deduplicate by `id`.
   Resolve conflicting metadata in favor of the publisher's own page.
5. **Build `runtime.json`.** Derive it from the subject files. Do not hand-edit it.
6. **Build `README.md`.** Use the coverage template in §8.6.
7. **Update `data/collections/index.json`.** Read the existing index, replace the entry with the
   same `id`, add the new entry, sort by `name`. Do not drop other collections.
8. **Run the validator.** Fix every error before delivery.

---

## 8 · Output contract

### Format lineage

The definition schema is the ECE seed schema: `term`, `definition`, `formula`, `unit`,
`unitTitle`, `sources`. The container is generalized from a degree programme to a collection:
`section` replaces `semester`, and `sections` replaces `semesters`. `runtime.json`
is the exact `SUBJECTS` shape the app already uses. If a consumer still expects the ECE
keys, map `section → semester` and `sections → semesters` at load time; do not
duplicate the data.

Create this tree. Do not create files outside it, except the shared validator.

```text
data/collections/
  index.json
  <collection-slug>/
    plan.json
    collection.json
    runtime.json
    sources.json
    README.md
    subjects/
      <subject-slug>.json
scripts/
  validate-collection.py
```

### 8.1 `collection.json`

```json
{
  "version": 1,
  "id": "medical-terminology",
  "name": "Medical Terminology",
  "tagline": "Medicine, in one line.",
  "topic": "Medical terminology for pre-health students",
  "audience": "Pre-health undergraduates and nursing students",
  "level": "intro",
  "jurisdiction": "US",
  "spelling": "US",
  "language": "en",
  "regulated": true,
  "generatedAt": "2026-10-24",
  "scope": {
    "includes": ["prefixes, roots, suffixes", "body systems", "clinical abbreviations"],
    "excludes": ["diagnosis", "treatment protocols", "drug dosing"]
  },
  "assumptions": ["US clinical usage", "no prior anatomy assumed"],
  "disclaimer": "Educational vocabulary only; not medical advice.",
  "sections": [
    {
      "id": "core",
      "label": "Core",
      "subjects": [
        {
          "id": "word-parts",
          "name": "Word Parts",
          "shortName": "Word parts",
          "code": null,
          "courseType": "core",
          "color": "#5b6ee1",
          "dark": "#8a9bff",
          "data": "data/collections/medical-terminology/subjects/word-parts.json",
          "definitionCount": 48,
          "unitCount": 4,
          "coveredUnits": 4,
          "status": "complete",
          "sourceCount": 2
        }
      ]
    }
  ],
  "coverage": {
    "sections": 1,
    "subjects": 1,
    "definitions": 48,
    "completeSubjects": 1,
    "partialSubjects": 0,
    "inaccessibleSubjects": 0
  }
}
```

The `sections` array is truncated for readability. A real collection lists every section and
subject, and `coverage` is the sum of those subjects.

Rules:

- `id` is the kebab-case slug of the topic, unique across `data/collections/`.
- `tagline` follows the pattern `"<Field>, in one line."` Keep it short.
- `sections` may contain 1–3 entries. A simple collection has one section, `core`.
- `code` and `courseType` are optional; use `null` and `"core"` for non-course topics.
- `regulated` is `true` for medical, legal, and financial collections; it requires a non-empty
  `disclaimer`.
- `status` is one of `complete`, `partial`, `inaccessible`, `no_materials`, `unresolved`.
- `complete` means all units covered and at least 40 definitions.
- `partial` means at least one definition but fewer than 40, or missing units.
- `inaccessible` means no usable source; no subject file.
- `data` is `null` for subjects with no file.
- Counts must match the subject files exactly.

### 8.2 Subject file

`data/collections/<collection-slug>/subjects/<subject-slug>.json`

```json
{
  "version": 1,
  "id": "word-parts",
  "collectionId": "medical-terminology",
  "section": "core",
  "name": "Word Parts",
  "shortName": "Word parts",
  "code": null,
  "courseType": "core",
  "status": "complete",
  "color": "#5b6ee1",
  "dark": "#8a9bff",
  "units": [
    { "number": 1, "title": "Prefixes" },
    { "number": 2, "title": "Roots" },
    { "number": 3, "title": "Suffixes" },
    { "number": 4, "title": "Combining forms" }
  ],
  "definitions": [
    {
      "id": "tachycardia",
      "term": "Tachycardia",
      "definition": "A resting heart rate above 100 beats per minute.",
      "formula": "",
      "unit": 1,
      "unitTitle": "Prefixes",
      "aliases": ["tachy-"],
      "confusables": ["bradycardia", "arrhythmia", "palpitation"],
      "sources": ["medterm-openstax#ch.3"]
    }
  ]
}
```

Rules:

- `id` is unique within the collection; `term` is unique within the subject.
- `units` is the canonical unit list for the subject. `unit` and `unitTitle` on each definition
  must match it.
- `aliases` is optional; 0–3 alternative names or acronyms.
- `confusables` is required; 2–3 terms that exist in the same subject (preferred) or the
  same collection. They must not include the definition itself and must not be synonyms.
- `sources` has at least one locator.
- Definitions are sorted by `unit`, then `term`.

### 8.3 `sources.json`

```json
{
  "version": 1,
  "collectionId": "medical-terminology",
  "generatedAt": "2026-10-24",
  "sources": [
    {
      "id": "medterm-openstax",
      "title": "Medical Terminology for Healthcare Professions",
      "publisher": "OpenStax",
      "url": "https://openstax.org/details/books/medical-terminology",
      "type": "textbook",
      "license": "CC BY 4.0",
      "accessed": "2026-10-24",
      "status": "parsed",
      "locatorScheme": "ch.<n>",
      "notes": ""
    }
  ]
}
```

Rules:

- `id` is unique, lower-case, ASCII, stable: `<collection>-<slug>` or
  `<collection>-<subject>-<slug>`.
- `status` is one of `parsed`, `accessible`, `paywalled`, `inaccessible`, `needs_ocr`,
  `skipped`.
- Only `parsed` sources may be cited by definitions. `accessible` means verified but not used.
- `license` is the actual license if known; use `"unknown"` if not. Prefer CC, public
  domain, government, and open-textbook sources.
- `locatorScheme` is one of the schemes in §10.3.
- Do not store full source text, PDFs, or HTML in the repo.

### 8.4 `runtime.json`

This is the bundle the app can load directly. It mirrors the existing `SUBJECTS` shape.

```json
{
  "version": 1,
  "id": "medical-terminology",
  "name": "Medical Terminology",
  "short": "Med term",
  "subjects": [
    {
      "id": "word-parts",
      "name": "Word Parts",
      "short": "Word parts",
      "color": "#5b6ee1",
      "dark": "#8a9bff",
      "defs": [
        ["Tachycardia", "A resting heart rate above 100 beats per minute.", ""]
      ]
    }
  ]
}
```

Rules:

- `defs` is an array of `[term, definition, formula]`.
- `subjects` flattens sections in order, then subjects in order. The app currently
  consumes a flat array; section grouping lives in `collection.json`.
- Order and content must match the subject files exactly.
- `short` is the collection's short label, 2–3 words.
- `dark` is the dark-mode color from the palette.
- The runtime bundle is derived; never hand-edit it.

### 8.5 `data/collections/index.json`

```json
{
  "version": 1,
  "generatedAt": "2026-10-24",
  "collections": [
    {
      "id": "medical-terminology",
      "name": "Medical Terminology",
      "tagline": "Medicine, in one line.",
      "path": "data/collections/medical-terminology",
      "subjects": 1,
      "definitions": 48,
      "generatedAt": "2026-10-24"
    }
  ]
}
```

Merge, do not replace. Sort by `name`.

### 8.6 `README.md`

A human coverage report, not marketing. Include:

1. **What this collection is.** Topic, audience, level, jurisdiction, assumptions.
2. **Totals.** Sections, subjects, definitions, complete/partial/inaccessible counts.
3. **Coverage table.** One row per subject: status, definitions, units covered, sources.
4. **Sources.** ID, title, publisher, license, status.
5. **Gaps.** Missing units, inaccessible sources, terms skipped and why.
6. **Method.** Toolchain, source priority, verification coverage.
7. **Validation.** The exact command and result.
8. **Wiring.** A short note showing how to load `runtime.json` into the app's `SUBJECTS`
   array, without editing the app in this task. For example:

   ```js
   const collection = await fetch('data/collections/<collection-slug>/runtime.json').then(r => r.json());
   const SUBJECTS = collection.subjects;
   ```

   The app already consumes `{ id, name, color, dark, defs: [[term, def, formula]] }`,
   which is exactly what `runtime.json` provides.
9. **Disclaimer.** Required for medical, legal, and financial collections.

---

## 9 · Definition rules

### 9.1 The definition

- One sentence, 8–28 words.
- Standalone: readable without the source, the slide, or the previous definition.
- Define the thing, not its formula, history, or an example.
- If the honest definition is shorter than 8 words, add the essential distinguishing
  clause, not filler.
- Use the present tense.
- Prefer the pattern "A [category] that [distinguishing feature]."
- Avoid "this", "above", "as shown", "the following", "etc.", "various", "often",
  "usually", "can be", "refers to", "is when".
- No author names, dates, URLs, textbook citations, exam instructions, lab steps, or
  marketing.
- No advice, diagnosis, or recommendation.
- No invented mnemonics or memory tricks. The app derives explanations from the definition
  and formula.

### 9.2 The term

- Canonical name, ≤48 characters, no trailing colon, no "Definition of".
- Preserve acronyms and conventional capitalization (`MOSFET`, `PN junction`, `CMRR`,
  `Fourier transform`).
- Title case for named concepts; sentence case for generic descriptive terms. Be consistent
  within a subject.
- Use the spelling convention recorded in `plan.json`; do not mix US, UK, and Indian
  spellings in the same collection.
- If a term has multiple senses, qualify it in the term (e.g., `Duration (finance)`).
- Do not use ordinals in IDs.

### 9.3 The cue

`formula` is a general cue slot, ≤48 characters, Unicode not LaTeX. Use it for:

- a formula (`F = AUC_oral / AUC_IV`),
- a code signature (`map(fn, xs) → list`),
- a symbol (`V₁`, `δ(t)`),
- a notation (`I–V–vi–IV`),
- a pronunciation (`/tækiˈkɑːrdiə/`),
- a canonical citation (`42 U.S.C. § 1983`).

Leave it empty if there is no useful cue. Do not invent a formula or notation.

### 9.4 The confusables

For each definition, ask: "If this term were the question, which three other terms would a smart
beginner plausibly confuse it with?" Those are the confusables.

- 2–3 per definition.
- Real terms that exist in the same subject (preferred) or collection.
- Not synonyms.
- Not the term itself.
- Plausible but wrong.
- If you cannot find two, the definition may be too isolated to quiz well. Replace it with a term
  from a denser cluster; do not ship a definition with zero confusables.

### 9.5 What to include

Prefer terms that are:

- foundational prerequisites,
- high-frequency in the source,
- commonly tested or used on the job,
- confusable with other terms,
- stable across editions and years.

### 9.6 What to exclude

- Headings, slide titles, and section labels.
- Examples, derivations, and worked problems.
- Author names, dates, URLs, and citations as definitions.
- Generic nouns and low-value vocabulary.
- Brand names, unless the brand *is* the concept (e.g., `Kubernetes`).
- People's names, unless the eponym is the term (e.g., `Poisson's ratio`).
- Dates, unless the date is the term (e.g., `Treaty of Westphalia`).
- Lab procedures and equipment instructions.
- Exam instructions and question-bank items.
- Anything you cannot source.

---

## 10 · Source rules

### 10.1 Source priority

1. **Official blueprint or syllabus.** Exam domains, unit titles, scope, and version.
2. **Standards bodies and regulators.** NIST, ISO, IEEE, NEC, GDPR, FDA, FAA, etc.
3. **Open textbooks and university course notes.** CC-licensed where possible.
4. **Professional association glossaries.** Stable and authoritative.
5. **Official product documentation.** For cloud, software, and tools.
6. **Reputable encyclopedias.** Use as a finding aid; cite the underlying source when
   possible.
7. **Wikipedia.** Acceptable for orientation, not as the only source for a contested or
   high-stakes definition.

Avoid content farms, SEO listicles, AI-generated summaries, leaked exam dumps, and
unattributed flashcard sites.

### 10.2 Access audit

For every source, record:

- URL, title, publisher, type;
- license;
- access date;
- status (`parsed`, `accessible`, `paywalled`, `inaccessible`, `needs_ocr`, `skipped`);
- locator scheme;
- a note if access failed.

If a source is paywalled or unreadable, mark it and find an alternative. Never cite a source
you did not read.

### 10.3 Locator schemes

| Source type | Locator | Example |
| --- | --- | --- |
| PDF | `p.<n>` | `medterm-openstax#p.42` |
| Textbook chapter | `ch.<n>` | `medterm-openstax#ch.3` |
| Web section | `sec.<slug>` or `h.<n>` | `nist-glossary#sec.zero-trust` |
| Slides | `slide.<n>` | `lecture-3#slide.12` |
| DOCX | `para.<n>` or `sec.<slug>` | `syllabus#sec.unit-2` |
| Standard clause | `cl.<n>` | `nec-2023#cl.210.8` |
| Video | `t.<seconds>` | `talk#t.412` |
| Statute or case | `sec.<n>` or `case.<slug>` | `usc-42#sec.1983` |

Use 1-based numbering. The locator must be specific enough that a reviewer can find the
supporting passage in under a minute. Choose **one** scheme per source and use it
consistently; do not mix `sec.` and `h.` within the same source.

### 10.4 Paraphrase, do not copy

Definitions are facts; the sentences expressing them can be copyrighted. Write the
one-liner yourself. A short technical phrase may be unavoidable, but do not copy a full
sentence from a textbook. The verifier checks for verbatim overlap.

### 10.5 No raw sources in the repo

Download to `/tmp/oneliners-<collection>/`. Commit only derived JSON, metadata, reports, and the
validator. Do not commit PDFs, PPTX, DOCX, HTML, images, or transcripts.

---

## 11 · Topic-specific guidance

### 11.1 Exams and certifications

- Use the current official blueprint. Record the version and year in `plan.json` and
  `collection.json`.
- Map each official domain to a subject. Use the domain names verbatim.
- Weight definition counts roughly by blueprint percentage, but never pad a thin domain.
- Do not use leaked questions or dumps. Definitions are not questions.
- Include a `blueprint` block in `collection.json` if the exam publishes weights.

### 11.2 Academic courses

- Use the syllabus units as the unit list.
- Cover every unit that has usable material.
- If a unit has no usable source, mark it in the README rather than inventing definitions.
- Keep the level explicit (intro, advanced).

### 11.3 Professional fields

- Use the language practitioners actually use, including acronyms.
- Organize by job-task area, not by textbook chapter.
- Include the terms a new hire is expected to know in the first month.

### 11.4 Hobbies

- Aim at the beginner-to-intermediate enthusiast, not the expert.
- Include the terms needed to follow conversations, read reviews, and avoid embarrassing
  mistakes.
- 120–250 definitions is usually enough.
- Note which definitions would benefit from an image.

### 11.5 Languages

- Prefer grammar and usage concepts over raw word lists.
- Terms may be in the target language; definitions in English.
- Put IPA or a pronunciation hint in `formula` when useful.
- Record the language variant in `plan.json`.
- If the user explicitly asks for vocabulary, use example sentences in the definition and
  note that audio is needed for a complete experience.

### 11.6 General knowledge

- Use authoritative lists: government sources, scientific bodies, standards organizations.
- Avoid facts that change frequently (sports records, pop culture rankings).
- 100–300 definitions is usually enough.
- Accept that this is a lower-stakes collection; do not over-engineer it.

### 11.7 Fast-moving fields

For AI, crypto, cloud, and other fields where terms churn:

- Date the collection and record the source versions.
- Prefer concepts that are stable at the protocol or definitional level over product names
  that may be renamed.
- Re-verify every definition against the current official documentation.
- Add `"volatile": true` to `plan.json` and a review date to the README.
- Keep the collection shorter and more precise; a stale definition is worse than a missing one.

---

## 12 · Subagent brief template

Copy this into each extraction subagent. Fill every placeholder. Do not shorten it.

> You are building one subject of a one·liners collection.
>
> **Collection:** `<collection name>` (`<collection id>`)
> **Topic:** `<topic>`
> **Audience:** `<audience>`
> **Level:** `<level>`
> **Jurisdiction / standard:** `<jurisdiction>`
> **Spelling:** `<US|UK|IN>`
> **Subject:** `<subject name>` (`<subject id>`)
> **Section:** `<section id>`
> **Output:** write exactly `<data/collections/<collection>/subjects/<subject>.json>`.
> **Do not edit any other file.**
>
> **Units:**
> `<numbered unit list>`
>
> **Target:** `<n>` definitions, 8–20 per unit. Quality over count. If a unit is genuinely thin,
> write fewer than 8 definitions for it rather than padding. If you cannot reach `<min>` sourced,
> quiz-viable definitions, stop at what you have and report it; do not pad.
>
> **Source candidates:** `<queries or URLs>`
>
> **Task:**
> 1. Find and read 1–4 authoritative sources for this subject. Record each source's URL,
>    title, publisher, license, status, and locator scheme in your report. If you have no
>    web access and no sources were supplied, stop and report; do not write from memory.
> 2. Extract and paraphrase quiz-ready one-line definitions covering every unit.
> 3. For each definition, assign `unit`, `unitTitle`, and 2–3 `confusables` that will exist in the
>    final collection.
> 4. Write the subject JSON in the exact schema below.
> 5. Report counts, units covered, sources used, skipped items, and access problems.
>
> **Schema:**
>
> ```json
> {
>   "version": 1,
>   "id": "<subject id>",
>   "collectionId": "<collection id>",
>   "section": "<section id>",
>   "name": "<subject name>",
>   "shortName": "<short name>",
>   "code": null,
>   "courseType": "core",
>   "status": "complete",
>   "color": "<color>",
>   "dark": "<dark color>",
>   "units": [{ "number": 1, "title": "<unit title>" }],
>   "definitions": [
>     {
>       "id": "<kebab-case>",
>       "term": "<term>",
>       "definition": "<one sentence, 8-28 words>",
>       "formula": "<cue or empty>",
>       "unit": 1,
>       "unitTitle": "<unit title>",
>       "aliases": [],
>       "confusables": ["<term>", "<term>"],
>       "sources": ["<sourceId>#<locator>"]
>     }
>   ]
> }
> ```
>
> **Rules:**
> - Every definition must be supported by a cited source. No model-memory-only definitions.
> - If you cannot find a usable source for the subject, do not write definitions; report the
>   subject as inaccessible.
> - Set `status` to `complete` only if you covered every unit and met the target; otherwise
>   set it to `partial` and explain why in your report.
> - One sentence, 8–28 words; standalone; no "this", "above", "as shown", "etc.".
> - `term` ≤48 characters, no trailing colon, no "Definition of".
> - `formula` ≤48 characters, Unicode not LaTeX; empty if none.
> - `unit` and `unitTitle` must match the subject's `units` list.
> - `confusables` must be real terms that will exist in the final collection; 2–3 per definition; not
>   synonyms; not the term itself.
> - Deduplicate terms within the subject.
> - Exclude headings, examples, derivations, author names, dates, URLs, exam instructions,
>   lab steps, and low-value nouns.
> - Paraphrase; do not copy sentences from the source.
> - Do not download or commit raw source files. Use `/tmp/oneliners-<collection>/`.
> - Do not edit any file other than your subject JSON.
>
> **Report back:**
> - definitions written, per unit;
> - a machine-readable `sources` array with `id`, `title`, `publisher`, `url`, `type`,
>   `license`, `accessed`, `status`, and `locatorScheme` for every source you read;
> - terms skipped and why;
> - access or extraction problems;
> - the path written.

For a subject with no accessible source, do not launch an extraction subagent. Mark it
`inaccessible` in the plan and report.

---

## 13 · Validator requirements

Write `scripts/validate-collection.py` with no non-standard-library dependencies. It must accept
a collection path and validate every collection under `data/collections/` by default. It must exit non-zero on
any error.

Check:

**Files and JSON**

- Every required file exists and parses as UTF-8 JSON: `plan.json`, `collection.json`, every
  subject file, `sources.json`, and `runtime.json`. `README.md` exists and is non-empty.
- No raw source files (`.pdf`, `.pptx`, `.docx`, `.html`, `.epub`) anywhere under
  `data/collections/`.
- `plan.json`, `collection.json`, subject files, `sources.json`, and `runtime.json` have the
  required keys.

**Identity and counts**

- `collection.id` matches the folder name and is unique in `index.json`.
- `collection.json` section and subject ids match `plan.json`, in the same order.
- Subject ids are unique across the collection; definition ids are unique within a subject; terms are
  unique within a subject.
- Every subject file path resolves and lives under the collection folder.
- `definitionCount`, `unitCount`, `coveredUnits`, and `sourceCount` match the subject file.
- `coverage.sections` matches the number of sections in `collection.json`.
- `coverage` totals match the sum of the subject files.
- `index.json` entries match the collection's counts.

**Definitions**

- `definition` is a non-empty string, 8–28 words, no trailing spaces.
- `term` is 1–48 characters, no trailing colon, no "Definition of".
- `formula` is a string of at most 48 characters.
- `unit` is an integer present in `units`, or `null`.
- `unitTitle` matches the unit title for that number, or `null`.
- `aliases` is an array of 0–3 strings.
- `confusables` is an array of 2–3 strings, each of which exists as a term in the same
  subject (preferred) or the same collection; none equals the definition's own term.
- No duplicate `(term, definition)` within the collection.
- No definition cites a source from a different collection.

**Sources**

- Every `sources` entry has a valid `sourceId#locator` shape.
- Every `sourceId` exists in `sources.json`.
- The cited source's `status` is `parsed`.
- The locator scheme matches the source's `locatorScheme`.
- No definition cites an `inaccessible`, `paywalled`, or `skipped` source.
- Source ids are unique.

**Runtime**

- `runtime.json` has the same collection id and name.
- Every subject in `collection.json` appears in `runtime.json`, in flattened section order.
- Every definition appears in `runtime.json` as `[term, definition, formula]`, in the same order,
  with identical strings.
- No extra or missing definitions.

**Quality gates**

- A subject marked `complete` has at least 40 definitions and covers every unit.
- A subject marked `partial` has at least one definition and a reason in the README.
- A subject marked `inaccessible` has no subject file.
- The collection meets the `definitionBudget.min` declared in `plan.json`; if it does not, the README
  explains why and the affected subjects are marked `partial`.
- If `regulated` is `true`, `disclaimer` is non-empty.

Do not relax the validator to hide missing data. Fix the data or mark the subject partial.

---

## 14 · Acceptance gate

The collection is done only when all of these are true:

- `python3 scripts/validate-collection.py data/collections/<collection-slug>` exits 0.
- Every subject file is valid UTF-8 JSON with the required keys.
- Every definition has at least one source locator that resolves to a `parsed` source.
- At least 30 definitions, or 20% of the collection (whichever is greater), have been spot-checked
  against their cited locators.
- The runtime bundle matches the authoring data exactly.
- The README states totals, coverage, sources, gaps, and assumptions.
- No app files were changed.
- No raw source files were committed.
- The final response includes the validation command and result.

If the collection cannot meet these, deliver a partial collection and say exactly what is missing.

---

## 15 · Stop conditions

Stop and report instead of guessing if:

- the topic is missing or cannot be interpreted;
- the topic is so broad that any collection would be misleading, and no reasonable entry point
  can be chosen;
- a jurisdiction, exam version, or language variant is essential and cannot be defaulted;
- more than 25% of the planned subjects have no accessible source;
- the available sources are too thin to reach the minimum definition count without padding;
- a source requires OCR and no reliable OCR is available;
- two authoritative sources conflict on a definition and the conflict cannot be resolved by
  scoping;
- the work would require copying a copyrighted question bank or a long verbatim passage.

A partial, honest collection is acceptable. Fabricated data is not.

---

## 16 · Delivery

If git is available:

1. Create a branch named `collection/<collection-slug>`.
2. Commit in logical chunks: plan, subject files, merge, validator, index.
3. Do not push to `main`.
4. Open a draft PR titled `Add <collection name> collection` if `gh` is available.
5. Include the counts, coverage, sources, validation command, and gaps in the PR body.

If git is not available, leave the files in place and report the paths.

### Final response

Report:

1. Collection path and branch/PR URL, if any.
2. Topic, audience, level, jurisdiction, and assumptions.
3. Sections, subjects, and definition counts.
4. Coverage table by subject: status, definitions, units covered, sources.
5. Sources used, with licenses and status.
6. Gaps: missing units, inaccessible sources, skipped terms, partial subjects.
7. The exact validation command and result.
8. Confirmation that no app files were changed and no raw sources were committed.
9. One wiring note: how to load `runtime.json` into the app's `SUBJECTS` array.
10. Anything the app owner must decide before wiring.

---

## 17 · The one-sentence rule

If you remember nothing else: **a collection is a map of a field, not a dump of its glossary.**
Choose the terms a learner needs to stop feeling lost, source every one of them, make every
one of them quiz-able, and say honestly what you left out.
