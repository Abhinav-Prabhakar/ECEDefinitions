# HVAC Licensing

**Topic:** HVAC licensing for HVAC apprentices and licensing candidates  
**Audience:** HVAC apprentices and licensing candidates  
**Level:** intro · **Jurisdiction:** US · **Spelling:** US · **Language:** en  
**Regulated:** yes  
**Generated:** 2026-10-25

## What this collection is

A vocabulary collection for HVAC/R apprentices and licensing candidates in the US. It covers the five areas licensing exams and entry-level work lean on: the refrigeration cycle, superheat and subcooling, psychrometrics, electrical controls, and codes and safety. It is a vocabulary map of the trade, not a service manual and not a substitute for manufacturer literature or EPA 608 training.

**In scope**

- refrigeration cycle
- superheat and subcooling
- psychrometrics
- electrical controls
- codes and safety

**Out of scope**

- commercial refrigeration design
- hydronics advanced
- controls programming
- equipment sizing software
- installation procedures

**Assumptions**

- US HVAC/R terminology
- focus on definitions and core concepts
- exam-oriented vocabulary

## Totals

- Sections: 1
- Subjects: 5
- Definitions: 206
- Complete subjects: 5
- Partial subjects: 0
- Inaccessible subjects: 0

## Coverage by subject

| Subject | Status | Definitions | Units covered | Sources |
| --- | --- | ---: | ---: | ---: |
| Refrigeration Cycle | complete | 45 | 5/5 | 4 |
| Superheat and Subcooling | complete | 40 | 5/5 | 1 |
| Psychrometrics | complete | 41 | 5/5 | 2 |
| Electrical Controls | complete | 40 | 5/5 | 2 |
| Codes and Safety | complete | 40 | 5/5 | 15 |

## Sources

| ID | Title | Publisher | License | Status |
| --- | --- | --- | --- | --- |
| `acca-manual-j` | ACCA Manual J - Residential Load Calculation | Air Conditioning Contractors of America | ACCA copyright | parsed |
| `acca-manual-n` | ACCA Manual N - Commercial Load Calculation | Air Conditioning Contractors of America | ACCA copyright | parsed |
| `ashrae-15` | ANSI/ASHRAE Standard 15 - Safety Standard for Refrigeration Systems | ASHRAE | ASHRAE copyright | parsed |
| `ashrae-62.1` | ANSI/ASHRAE Standard 62.1 - Ventilation for Acceptable Indoor Air Quality | ASHRAE | ASHRAE copyright | parsed |
| `ashrae-62.2` | ANSI/ASHRAE Standard 62.2 - Ventilation in Residential Buildings | ASHRAE | ASHRAE copyright | parsed |
| `ashrae-glossary` | ASHRAE Terminology (HVAC&R glossary) | ASHRAE | ASHRAE copyright | parsed |
| `ashrae-handbook-fundamentals` | ASHRAE Handbook - Fundamentals | ASHRAE | ASHRAE copyright | parsed |
| `epa-608` | EPA Section 608 - Refrigerant Management Requirements | US Environmental Protection Agency | US Government work (public domain) | parsed |
| `hvac-glossary-acca` | ACCA technical glossary (HVAC terminology) | Air Conditioning Contractors of America | ACCA copyright | parsed |
| `hvac-glossary-rses` | RSES refrigeration and HVAC service glossary | Refrigeration Service Engineers Society | RSES copyright | parsed |
| `icc-imc` | International Mechanical Code | International Code Council | ICC copyright | parsed |
| `nate-glossary` | NATE technician certification glossary | North American Technician Excellence | NATE copyright | parsed |
| `nfpa-54` | NFPA 54 - National Fuel Gas Code | National Fire Protection Association | NFPA copyright | parsed |
| `nfpa-70` | NFPA 70 - National Electrical Code | National Fire Protection Association | NFPA copyright | parsed |
| `nfpa-70e` | NFPA 70E - Standard for Electrical Safety in the Workplace | National Fire Protection Association | NFPA copyright | parsed |
| `osha-1910.132` | OSHA 29 CFR 1910.132 - Personal Protective Equipment | US Occupational Safety and Health Administration | US Government work (public domain) | parsed |
| `osha-1910.134` | OSHA 29 CFR 1910.134 - Respiratory Protection | US Occupational Safety and Health Administration | US Government work (public domain) | parsed |
| `osha-1910.146` | OSHA 29 CFR 1910.146 - Permit-Required Confined Spaces | US Occupational Safety and Health Administration | US Government work (public domain) | parsed |
| `osha-1910.147` | OSHA 29 CFR 1910.147 - Control of Hazardous Energy (Lockout/Tagout) | US Occupational Safety and Health Administration | US Government work (public domain) | parsed |
| `osha-1926.501` | OSHA 29 CFR 1926.501 - Duty to Have Fall Protection | US Occupational Safety and Health Administration | US Government work (public domain) | parsed |
| `osha-hazcom` | OSHA Hazard Communication Standard (29 CFR 1910.1200) | US Occupational Safety and Health Administration | US Government work (public domain) | parsed |
| `rse-glossary` | RSES refrigeration service terminology | Refrigeration Service Engineers Society | RSES copyright | parsed |
| `ul-standards` | UL product safety standards for HVAC/R equipment | UL Standards & Engagement | UL copyright | parsed |

ASHRAE, ACCA, ICC, NFPA, NATE, RSES, and UL publications are copyrighted; no text or tables from them are reproduced or committed here. EPA and OSHA material is US government work and may be reused. Locators are section identifiers so a reviewer can find the supporting passage in the publisher's own reader.

## Gaps

- Commercial refrigeration design, hydronic system design, and controls programming were left out as specialty scope.
- No charging charts, superheat target tables, or equipment-specific values are included. Targets vary by manufacturer and metering device, so a fixed number here would mislead.
- EPA 608 certification categories are referenced, but the exam itself and its refrigerant handling procedures are not taught here.
- ACCA Manual J and Manual N are cited for load concepts only; the full procedures and tables are proprietary.

## Method

- Toolchain: one extraction pass per subject, then an orchestrator merge, cross-subject deduplication, and a derived runtime bundle.
- Source priority: standards bodies and regulators first, then open references, then professional-association glossaries.
- Every definition is paraphrased in one sentence of 8–28 words and carries at least one `sourceId#locator` citation. Locators are article/section identifiers, not page scans.
- Verification: a stratified spot-check was run across every subject and unit for support, paraphrase, accuracy, scope, word count, distractor quality, duplication, and neutrality. Terms that failed were rewritten or replaced.
- `confusables` are real terms that exist elsewhere in this collection, so every definition can generate a two-way quiz with plausible wrong answers.

## Validation

```text
$ python3 scripts/validate-collection.py data/collections/hvac-licensing
VALIDATION PASSED
```

## Wiring

The app consumes `{ id, name, color, dark, defs: [[term, def, formula]] }`. `runtime.json` already has that shape, so no transformation is needed:

```js
const collection = await fetch('data/collections/hvac-licensing/runtime.json').then(r => r.json());
const SUBJECTS = collection.subjects;
```

## Disclaimer

Educational vocabulary only; not HVAC advice or code compliance guidance.
