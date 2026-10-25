# Pharmacology

## What this collection is

- **Topic:** Pharmacology for nursing and pre-health students
- **Audience:** Nursing and pre-health students
- **Level:** intro
- **Jurisdiction:** US (FDA-approved terminology)
- **Spelling:** US
- **Regulated:** yes (educational vocabulary only; not medical advice)

**Scope includes:** pharmacokinetics; pharmacodynamics; major drug classes; adverse effects and drug interactions; special populations.

**Scope excludes:** drug dosing and patient-specific regimens; prescribing and clinical decision-making; advanced medicinal chemistry; controlled-substance scheduling detail; patient-specific advice.

**Assumptions:** US clinical usage and FDA-approved terminology; introductory level with no prior pharmacology assumed; vocabulary only, not clinical training or prescribing guidance.

## Totals

- Sections: 2
- Subjects: 5
- Definitions: 270
- Complete subjects: 5
- Partial subjects: 0
- Inaccessible subjects: 0

## Coverage table

| Subject | Status | Definitions | Units covered | Sources |
| --- | --- | --- | --- | --- |
| Pharmacokinetics | complete | 52 | 5/5 | 1 |
| Pharmacodynamics | complete | 52 | 5/5 | 3 |
| Major Drug Classes | complete | 62 | 5/5 | 1 |
| Adverse Effects and Drug Interactions | complete | 52 | 5/5 | 3 |
| Special Populations | complete | 52 | 5/5 | 1 |

## Sources

| ID | Title | Publisher | License | Status |
| --- | --- | --- | --- | --- |
| openstax-pharmacology-nurses | Pharmacology for Nurses | OpenStax (Rice University) | CC BY-NC-SA 4.0 | parsed |
| wtcs-nursing-pharmacology | Nursing Pharmacology | WisTech Open (Chippewa Valley Technical College) | CC BY 4.0 | parsed |
| libretexts-essentials-pharmacology | Essentials of Pharmacology | Medicine LibreTexts (University of Illinois Chicago) | CC BY 4.0 | parsed |
| medlineplus-drug-therapy | Drug Therapy | National Library of Medicine (MedlinePlus) | Public domain (US government) | parsed |
| fda-drugsfda-glossary | Drugs@FDA Glossary of Terms | U.S. Food and Drug Administration (FDA) | Public domain (US government) | parsed |
| fda-population-pk | Population Pharmacokinetics: Guidance for Industry | U.S. Food and Drug Administration (FDA) | Public domain (US government) | accessible |

## Gaps

- No inaccessible subjects. All five subjects reached their targets.
- Advanced PK parameters (Cmax, Tmax, AUC, Vd) were excluded as low-value for an intro nursing audience.
- Controlled-substance scheduling detail and patient-specific dosing were excluded by scope.
- FDA population PK guidance was consulted but not cited (no term-level definitions).
- Some confusables were normalized to existing collection terms where the originally named near-neighbour was not itself a defined term.

## Method

- Toolchain: web search and fetch for authoritative open textbooks and government glossaries; manual paraphrase; JSON authoring; `scripts/validate-collection.py`.
- Source priority: open textbooks (OpenStax, WisTech, LibreTexts) and government sources (FDA, MedlinePlus).
- Verification coverage: definitions spot-checked against cited locators during authoring; all subject files validated.

## Validation

Command:

```
python3 scripts/validate-collection.py data/collections/pharmacology
```

Result: VALIDATION PASSED

## Wiring

Load `runtime.json` into the app's `SUBJECTS` array without editing app files:

```js
const collection = await fetch('data/collections/pharmacology/runtime.json').then(r => r.json());
const SUBJECTS = collection.subjects;
```

The app already consumes `{ id, name, color, dark, defs: [[term, def, formula]] }`, which is exactly what `runtime.json` provides.

## Disclaimer

Educational vocabulary only; not medical advice, prescribing guidance, or patient-specific recommendations.