# Nursing and NCLEX

## What this collection is

- **Topic:** Nursing and NCLEX-RN preparation
- **Audience:** NCLEX-RN candidates
- **Level:** intro
- **Jurisdiction:** US (NCLEX-RN 2023 test plan, effective April 2023)
- **Spelling:** US
- **Regulated:** yes (educational vocabulary only; not medical advice)

**Scope includes:** fundamentals of nursing; health assessment; safety and infection control; medical-surgical nursing; maternal and child health; mental health nursing.

**Scope excludes:** drug dosing and patient-specific regimens; prescribing and clinical decision-making; advanced pathophysiology; NCLEX item practice and question banks; state-specific nurse practice act detail.

**Assumptions:** US clinical usage and NCLEX-RN 2023 test plan; introductory level for entry-level RN preparation; vocabulary only, not clinical training or licensure advice.

## Totals

- Sections: 2
- Subjects: 6
- Definitions: 347
- Complete subjects: 6
- Partial subjects: 0
- Inaccessible subjects: 0

## Coverage table

| Subject | Status | Definitions | Units covered | Sources |
| --- | --- | --- | --- | --- |
| Fundamentals of Nursing | complete | 60 | 6/6 | 2 |
| Health Assessment | complete | 56 | 6/6 | 1 |
| Safety and Infection Control | complete | 56 | 6/6 | 2 |
| Medical-Surgical Nursing | complete | 60 | 6/6 | 1 |
| Maternal and Child Health | complete | 59 | 6/6 | 3 |
| Mental Health Nursing | complete | 56 | 6/6 | 1 |

## Sources

| ID | Title | Publisher | License | Status |
| --- | --- | --- | --- | --- |
| cdc-standard-precautions | Standard Precautions for All Patient Care | Centers for Disease Control and Prevention (CDC) | Public domain (US government) | parsed |
| nursingfund-openrn | Nursing Fundamentals 2e | WisTech Open (Open RN) | CC BY 4.0 | parsed |
| nursingfund-openrn-sec | Nursing Fundamentals 2e | WisTech Open (Open RN) | CC BY 4.0 | parsed |
| nursingskills-openrn | Nursing Skills 2e | WisTech Open (Open RN) | CC BY 4.0 | parsed |
| openstax-fundamentals-nursing | Fundamentals of Nursing | OpenStax (Rice University) | CC BY-NC-SA 4.0 | parsed |
| openstax-maternal-newborn-nursing | Maternal Newborn Nursing | OpenStax (Rice University) | CC BY-NC-SA 4.0 | parsed |
| openstax-medical-surgical-nursing | Medical-Surgical Nursing | OpenStax (Rice University) | CC BY-NC-SA 4.0 | parsed |
| openstax-population-health-nurses | Population Health for Nurses | OpenStax (Rice University) | CC BY-NC-SA 4.0 | parsed |
| openstax-psychiatric-mental-health-nursing | Psychiatric-Mental Health Nursing | OpenStax (Rice University) | CC BY-NC-SA 4.0 | parsed |

## Gaps

- No inaccessible subjects. All six subjects reached complete status.
- Pharmacological and Parenteral Therapies content is excluded by scope (covered by the separate Pharmacology collection); medication safety terminology (high-alert medications, rights of administration) is retained here.
- Pediatric illness units draw on Population Health for Nurses rather than a dedicated pediatric nursing text, since no open pediatric nursing textbook was available in the candidate set.
- NCLEX test-plan domains are used as a scope guide, but definition counts are not weighted by blueprint percentages; the collection is a vocabulary map, not a question bank.
- Some confusables were normalized to existing collection terms where the originally named near-neighbour was not itself a defined term.
- Nursing-fundamentals safety chapters are cited under a separate `nursingfund-openrn-sec` source id to keep the `sec.<slug>` locator scheme distinct from the `ch.<n>` scheme used elsewhere in the same book.

## Method

- Toolchain: web search and fetch for authoritative open textbooks (Open RN / WisTech, OpenStax) and government sources (CDC); paraphrase; JSON authoring; `scripts/validate-collection.py`.
- Source priority: open CC-licensed nursing textbooks and government public-health sources.
- Verification coverage: definitions spot-checked against cited locators during authoring; all subject files validated.

## Validation

Command:

```
python3 scripts/validate-collection.py data/collections/nursing-and-nclex
```

Result: VALIDATION PASSED

## Wiring

Load `runtime.json` into the app's `SUBJECTS` array without editing app files:

```js
const collection = await fetch('data/collections/nursing-and-nclex/runtime.json').then(r => r.json());
const SUBJECTS = collection.subjects;
```

The app already consumes `{ id, name, color, dark, defs: [[term, def, formula]] }`, which is exactly what `runtime.json` provides.

## Disclaimer

Educational vocabulary only; not medical advice, clinical training, or licensure guidance.
