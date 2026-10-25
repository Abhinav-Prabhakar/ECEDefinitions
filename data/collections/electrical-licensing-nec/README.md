# Electrical Licensing (NEC)

**Topic:** Electrical licensing (NEC) for electrician apprentices and journeyman exam candidates  
**Audience:** Electrician apprentices and journeyman exam candidates  
**Level:** intro · **Jurisdiction:** US · **Spelling:** US · **Language:** en  
**Regulated:** yes  
**Generated:** 2026-10-25

## What this collection is

A vocabulary collection for US electrician apprentices and journeyman exam candidates. It covers the five highest-yield areas of the National Electrical Code that appear on licensing exams: conductors and wiring methods, overcurrent protection, grounding and bonding, GFCI and AFCI, and load calculations. It is a map of the code's concepts, not a substitute for the codebook and not a how-to for any installation.

**In scope**

- conductors and wiring methods
- overcurrent protection
- grounding and bonding
- GFCI and AFCI
- load calculations

**Out of scope**

- motor control and advanced automation
- renewable energy systems
- communication and low-voltage specialty codes
- state amendments beyond core NEC
- design project solutions

**Assumptions**

- US NEC (current published edition as commonly tested)
- focus on definitions and core concepts
- exam-oriented vocabulary
- electrical safety concepts only (no codebook excerpts copied verbatim)

## Totals

- Sections: 1
- Subjects: 5
- Definitions: 220
- Complete subjects: 5
- Partial subjects: 0
- Inaccessible subjects: 0

## Coverage by subject

| Subject | Status | Definitions | Units covered | Sources |
| --- | --- | ---: | ---: | ---: |
| Conductors and Wiring Methods | complete | 48 | 5/5 | 1 |
| Overcurrent Protection | complete | 40 | 5/5 | 1 |
| Grounding and Bonding | complete | 47 | 5/5 | 1 |
| GFCI and AFCI | complete | 40 | 5/5 | 1 |
| Load Calculations | complete | 45 | 5/5 | 1 |

## Sources

| ID | Title | Publisher | License | Status |
| --- | --- | --- | --- | --- |
| `nec-2023` | NFPA 70, National Electrical Code (Article 100 definitions and referenced articles) | National Fire Protection Association (NFPA) | proprietary (free read-only access via NFPA) | parsed |

NFPA 70 is a copyrighted standard. It is free to read in NFPA's own reader after registration, but no code text, tables, or figures are reproduced or committed here. Definitions are paraphrased from the concepts; locators point a reviewer to the clause.

## Gaps

- State and local amendments are not covered. The NEC is a model code; your jurisdiction adopts it with local changes, and exam questions follow the adopted version.
- Article numbers and section numbers shift between editions. Locators name the article or section by topic so they stay findable across editions, but always check the edition your exam names.
- Motor control, hazardous locations, health-care facilities, and renewable-energy articles were deliberately left out as specialty scope.
- No worked calculation examples are included. Load-calculation definitions describe what a term means, not how to run a service calculation.

## Method

- Toolchain: one extraction pass per subject, then an orchestrator merge, cross-subject deduplication, and a derived runtime bundle.
- Source priority: standards bodies and regulators first, then open references, then professional-association glossaries.
- Every definition is paraphrased in one sentence of 8–28 words and carries at least one `sourceId#locator` citation. Locators are article/section identifiers, not page scans.
- Verification: a stratified spot-check was run across every subject and unit for support, paraphrase, accuracy, scope, word count, distractor quality, duplication, and neutrality. Terms that failed were rewritten or replaced.
- `confusables` are real terms that exist elsewhere in this collection, so every definition can generate a two-way quiz with plausible wrong answers.

## Validation

```text
$ python3 scripts/validate-collection.py data/collections/electrical-licensing-nec
VALIDATION PASSED
```

## Wiring

The app consumes `{ id, name, color, dark, defs: [[term, def, formula]] }`. `runtime.json` already has that shape, so no transformation is needed:

```js
const collection = await fetch('data/collections/electrical-licensing-nec/runtime.json').then(r => r.json());
const SUBJECTS = collection.subjects;
```

## Disclaimer

Educational vocabulary only; not electrical advice or code compliance guidance.
