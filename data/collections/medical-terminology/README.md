# Medical Terminology

## What this collection is

- **Topic:** Medical terminology for pre-health students.
- **Audience:** Pre-health undergraduates and nursing students.
- **Level:** intro
- **Jurisdiction:** US
- **Spelling:** US
- **Regulated:** yes (educational vocabulary only; not medical advice)
- **Assumptions:** US clinical usage; no prior anatomy assumed; vocabulary only, not clinical training.

## Totals

- Sections: 1
- Subjects: 6
- Definitions: 327
- Complete subjects: 6
- Partial subjects: 0
- Inaccessible subjects: 0

## Coverage table

| Subject | Status | Definitions | Units covered | Sources |
| --- | --- | --- | --- | --- |
| Word Parts | complete | 48 | 4/4 | 1 |
| Body Systems | complete | 60 | 6/6 | 1 |
| Clinical Abbreviations | complete | 50 | 6/6 | 4 |
| Documentation | complete | 50 | 5/5 | 5 |
| Diagnostics | complete | 69 | 5/5 | 4 |
| Pharmacology Basics | complete | 50 | 5/5 | 3 |

## Sources

| ID | Title | Publisher | License | Status |
| --- | --- | --- | --- | --- |
| medterm-wtcs | Medical Terminology 2e | WisTech Open | CC BY 4.0 | parsed |
| openstax-anatomy-physiology-2e | Anatomy and Physiology 2e | OpenStax (Rice University) | CC BY-NC-SA 4.0 | parsed |
| medlineplus-appendix-b | MedlinePlus Medical Dictionary: Common Abbreviations | NLM (MedlinePlus) | Public domain (US government) | parsed |
| cdc-infection-control-abbreviations | CDC Infection Control Abbreviations | CDC | Public domain (US government) | parsed |
| joint-commission-do-not-use | Joint Commission Do Not Use Abbreviations List | The Joint Commission | unknown | parsed |
| ismp-error-prone-abbreviations | ISMP List of Error-Prone Abbreviations | ISMP | unknown | parsed |
| cms-medrec-doc | CMS Evaluation and Management Medical Record Documentation | CMS | Public domain (US government) | parsed |
| cms-medrec-maintenance | CMS Medical Record Maintenance and Access Requirements | CMS | Public domain (US government) | parsed |
| ahima-legal-health-record | Fundamentals of the Legal Health Record and Designated Record Set | AHIMA | unknown | parsed |
| ahima-medrec-doc | Best Practices in Medical Record Documentation and Completion | AHIMA | unknown | parsed |
| medlineplus-phr | Personal Health Records | NLM (MedlinePlus) | Public domain (US government) | parsed |
| medlineplus-medical-tests | MedlinePlus Medical Tests | NLM (MedlinePlus) | Public domain (US government) | parsed |
| medlineplus-diagnostic-imaging | MedlinePlus Diagnostic Imaging | NLM (MedlinePlus) | Public domain (US government) | parsed |
| medlineplus-encyclopedia | MedlinePlus Medical Encyclopedia | NLM (MedlinePlus) | Public domain (US government) | parsed |
| nci-dictionary | NCI Dictionary of Cancer Terms | National Cancer Institute | Public domain (US government) | parsed |
| fda-drugsfda-glossary | Drugs@FDA Glossary of Terms | FDA | Public domain (US government) | parsed |
| medlineplus-drug-therapy | MedlinePlus Drug Therapy | NLM (MedlinePlus) | Public domain (US government) | parsed |
| openstax-pharmacology-nurses | Pharmacology for Nurses | OpenStax (Rice University) | CC BY 4.0 | parsed |

## Gaps

- Clinical abbreviations: do-not-use abbreviations (e.g., U, IU, MS) were excluded from the quiz set because they are unsafe; only commonly encountered abbreviations are included.
- Documentation: advanced coding specificity (ICD-10/CPT) is out of scope; covered only as basics.
- Diagnostics: locators are constructed section slugs and were not individually verified against live pages.
- Pharmacology: drug-class coverage is introductory; no dosing or patient-specific guidance is included.
- Confusables were auto-repaired to existing collection terms where the originally proposed term was not present.

## Method

- Toolchain: subagent extraction per subject, merge, validator.
- Source priority: open textbooks and government reference sites.
- Verification coverage: definitions spot-checked against cited locators; confusables validated for existence.

## Validation

Command: `python3 scripts/validate-collection.py data/collections/medical-terminology`
Result: VALIDATION PASSED (exit 0).

## Wiring

```js
const collection = await fetch('data/collections/medical-terminology/runtime.json').then(r => r.json());
const SUBJECTS = collection.subjects;
```

## Disclaimer

Educational vocabulary only; not medical advice.