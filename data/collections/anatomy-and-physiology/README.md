# Anatomy and Physiology

## What this collection is

Topic: Anatomy and physiology for pre-health and allied-health students.
Audience: Pre-health and allied-health students.
Level: intro.
Jurisdiction: global (science).
Spelling: US.

Assumptions:
- Introductory college-level anatomy and physiology.
- US spelling.
- Vocabulary only, not clinical training.
- Some definitions benefit from an accompanying image (see Gaps).

## Totals

- Sections: 1
- Subjects: 6
- Definitions: 285
- Complete subjects: 6
- Partial subjects: 0
- Inaccessible subjects: 0

## Coverage table

| Subject | Status | Definitions | Units covered | Sources |
| --- | --- | --- | --- | --- |
| Cells and Tissues | complete | 45 | 4/4 | 1 |
| Skeletal and Muscular Systems | complete | 50 | 5/5 | 1 |
| Cardiovascular and Respiratory Systems | complete | 55 | 5/5 | 1 |
| Nervous and Endocrine Systems | complete | 50 | 5/5 | 1 |
| Digestive and Urinary Systems | complete | 45 | 4/4 | 1 |
| Homeostasis | complete | 40 | 4/4 | 1 |

## Sources

| ID | Title | Publisher | License | Status |
| --- | --- | --- | --- | --- |
| openstax-anatomy-physiology-2e | Anatomy and Physiology 2e | OpenStax (Rice University) | CC BY-NC-SA 4.0 | parsed |

## Gaps

- Definitions that would benefit from an image: cell structure diagrams, skeletal bones, heart chambers, brain regions, nephron, feedback-loop diagrams. The collection is vocabulary-only; images are not included.
- Advanced pathophysiology, clinical diagnosis, pharmacology, surgical anatomy, and patient-specific advice are excluded by scope.
- Some granular sub-topics (e.g., individual cranial nerves, muscle names, pituitary hormones) were trimmed to keep the collection at the intro level and target count.

## Method

- Toolchain: OpenStax Anatomy and Physiology 2e as the single authoritative source, paraphrased into one-line definitions.
- Source priority: open textbook (OpenStax).
- Verification: spot-check of definitions against cited chapters; confusables normalized to existing collection terms.

## Validation

Command: `python3 scripts/validate-collection.py data/collections/anatomy-and-physiology`
Result: VALIDATION PASSED

## Wiring

```js
const collection = await fetch('data/collections/anatomy-and-physiology/runtime.json').then(r => r.json());
const SUBJECTS = collection.subjects;
```

The app already consumes `{ id, name, color, dark, defs: [[term, def, formula]] }`,
which is exactly what `runtime.json` provides.

## Disclaimer

Educational vocabulary only; not medical advice.
