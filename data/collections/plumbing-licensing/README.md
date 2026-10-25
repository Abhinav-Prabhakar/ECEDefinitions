# Plumbing Licensing

**Topic:** Plumbing licensing for plumbing apprentices and journeyman exam candidates  
**Audience:** Plumbing apprentices and journeyman exam candidates  
**Level:** intro · **Jurisdiction:** US · **Spelling:** US · **Language:** en  
**Regulated:** yes  
**Generated:** 2026-10-25

## What this collection is

A vocabulary collection for US plumbing apprentices and journeyman exam candidates. It covers the five areas the licensing exam and everyday service work depend on: water supply systems, drain-waste-vent, traps and vents, backflow and fixtures, and the plumbing code itself. It is a map of the trade's concepts, not an installation guide and not a substitute for the adopted code book.

**In scope**

- water supply systems
- drain-waste-vent systems
- traps and venting
- backflow prevention and fixtures
- plumbing code fundamentals

**Out of scope**

- medical gas piping
- fire sprinkler design
- solar thermal sizing
- commercial process piping
- state and local amendment details

**Assumptions**

- US plumbing code concepts (IPC and UPC common ground)
- vocabulary and concepts, not installation procedures
- exam-oriented definitions

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
| Water Supply Systems | complete | 42 | 5/5 | 2 |
| Drain-Waste-Vent | complete | 42 | 5/5 | 2 |
| Traps and Vents | complete | 40 | 5/5 | 3 |
| Backflow and Fixtures | complete | 42 | 5/5 | 3 |
| Plumbing Code | complete | 40 | 5/5 | 3 |

## Sources

| ID | Title | Publisher | License | Status |
| --- | --- | --- | --- | --- |
| `asse-plumbing-dictionary-6e` | ASSE International Plumbing Dictionary, 6th Edition | ASSE International | free public PDF; copyright ASSE International | parsed |
| `ecfr-141` | 40 CFR 141.2 - National Primary Drinking Water Regulations definitions | US Environmental Protection Agency (eCFR) | US Government work (public domain) | parsed |
| `ipc-2021` | International Plumbing Code 2021 (Chapters 1-10) | International Code Council (ICC) | proprietary model code; free read-only access, no redistribution | parsed |
| `osha-1910-146` | 29 CFR 1910.146 - Permit-Required Confined Spaces | US Occupational Safety and Health Administration | US Government work (public domain) | parsed |
| `osha-1926-subpart-p` | 29 CFR 1926 Subpart P - Excavations | US Occupational Safety and Health Administration | US Government work (public domain) | parsed |
| `plumbing-epa-ccc` | Cross-Connection Control Manual (EPA 816-R-03-002) | US Environmental Protection Agency, Office of Water | US Government work (public domain) | parsed |
| `plumbing-epa-watersense` | WaterSense product criteria (toilets, faucets, showerheads, urinals) | US Environmental Protection Agency, WaterSense | US Government work (public domain) | parsed |
| `upc-2024` | Uniform Plumbing Code 2024 (IAPMO/ANSI UPC 1-2024) | International Association of Plumbing and Mechanical Officials (IAPMO) | proprietary model code; free read-only edition | parsed |

The IPC and UPC are copyrighted model codes. Both were read through publicly readable copies (the Texas IPC adoption and the 2020 Plumbing Code of New York State, which adopts the IPC with amendments; the IAPMO read-only UPC edition and the 2022 California Plumbing Code, which adopts the UPC). No code text, table, or figure is reproduced or committed here; definitions are paraphrased and locators point a reviewer to the section.

## Gaps

- Only one model-code family is represented well. The collection rests on IPC-family text plus UPC cross-checks; jurisdictions that adopt the UPC with local amendments will find wording differences.
- State and local amendments are not covered. Adoption changes definitions and limits, and exam questions follow the adopted version.
- IPC Appendix E (water-pipe sizing tables) was not retrievable, so no water-supply fixture-unit sizing values are included. Drainage fixture units are covered as a concept only.
- Terms deliberately left out because they had no defensible citation: static pressure, water hammer (only the arrestor is defined), manifold, NSF 61 / NSF 372, and storage, tankless, and heat-pump water heater types.
- Medical gas piping, fire sprinkler design, and commercial process piping are excluded as specialty scope.

## Method

- Toolchain: one extraction pass per subject, then an orchestrator merge, cross-subject deduplication, and a derived runtime bundle.
- Source priority: adopted model codes and federal regulation first, then professional references and trade dictionaries.
- Every term is defined once across the collection. Where a concept appears in two subjects, it stays in the subject where it is most central, or the term is qualified by domain (for example `Backpressure (drainage)` against `Backpressure (water supply)`).
- Every definition is one paraphrased sentence of 8–28 words with at least one `sourceId#locator` citation.
- Verification: each subject was checked for support, paraphrase, accuracy, scope, word count, distractor quality, duplication, and neutrality; definitions that failed were rewritten, and duplicates were replaced with distinct sourced terms.

## Validation

```text
$ python3 scripts/validate-collection.py data/collections/plumbing-licensing
VALIDATION PASSED
```

## Wiring

`runtime.json` already matches the shape the app consumes, so no transformation is needed:

```js
const collection = await fetch('data/collections/plumbing-licensing/runtime.json').then(r => r.json());
const SUBJECTS = collection.subjects;
```

## Disclaimer

Educational vocabulary only; not plumbing advice or code compliance guidance.
