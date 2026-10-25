# Software Interview Glossary

A one·liners collection for mid-level software engineer interview candidates.

## What this collection is

- **Topic:** Software interview glossary — programming fundamentals; data structures and algorithms; system design; databases and SQL; operating systems and networking; web and browser.
- **Audience:** Mid-level software engineer interview candidates.
- **Level:** intro.
- **Jurisdiction / standard:** global (vendor-neutral concepts).
- **Spelling:** US.
- **Regulated:** no (no disclaimer required).

### Scope

Includes: programming fundamentals (types, scope, functions, closures, control flow, memory, paradigms); data structures and algorithms (complexity, core structures, trees and graphs, hashing, sorting, design techniques); system design (scalability, reliability, consistency, partitioning, caching, messaging, operations); databases and SQL (relational model, keys, querying, transactions, indexes, NoSQL); operating systems and networking (processes, scheduling, memory, storage, synchronization, network models and protocols); web and browser (HTTP, rendering, DOM, security policies, storage, web APIs).

Excludes: language-specific syntax and library APIs; vendor product names and cloud service catalogues; coding-puzzle solutions and worked interview questions; machine learning, data engineering and LLM vocabulary (separate collections); hiring process, behavioural interview and career advice.

### Assumptions

- Terms are defined at the level a mid-level engineer is expected to explain in an interview.
- Definitions follow widely used, vendor-neutral meanings; language-specific senses are noted in the term when they differ.
- US spelling throughout.
- Sources are free to read. The NIST Dictionary of Algorithms and Data Structures (xlab.nist.gov/dads) was unreachable during the access audit and is not used; OpenDSA and Wikipedia cover that subject instead.

## Totals

- Sections: 1
- Subjects: 6
- Definitions: 356
- Complete subjects: 6
- Partial subjects: 0
- Inaccessible subjects: 0

## Coverage table

| Subject | Status | Definitions | Units covered | Sources |
| --- | --- | --- | --- | --- |
| Programming Fundamentals | complete | 49 | 6/6 | python-glossary, mdn-glossary |
| Data Structures and Algorithms | complete | 68 | 7/7 | opendsa, wikipedia-algorithms |
| System Design | complete | 61 | 6/6 | aws-glossary, sre-book |
| Databases and SQL | complete | 65 | 6/6 | postgres-glossary, postgres-docs, mongodb-glossary |
| Operating Systems and Networking | complete | 60 | 7/7 | ostep, nist-glossary, rfc3022, rfc768 |
| Web and Browser | complete | 53 | 6/6 | mdn-glossary |

## Sources

| ID | Title | Publisher | License | Status |
| --- | --- | --- | --- | --- |
| python-glossary | Python Glossary | Python Software Foundation | PSF License | parsed |
| mdn-glossary | MDN Web Docs Glossary | MDN Web Docs (Mozilla) | CC BY-SA 2.5 | parsed |
| opendsa | OpenDSA | OpenDSA Project (Virginia Tech) | MIT License | parsed |
| wikipedia-algorithms | Wikipedia articles on algorithms and data structures | Wikimedia Foundation | CC BY-SA 4.0 | parsed |
| aws-glossary | AWS Glossary | Amazon Web Services | unknown | parsed |
| sre-book | Site Reliability Engineering | Google | CC BY-NC-ND 4.0 | parsed |
| postgres-glossary | PostgreSQL Glossary (Appendix M) | PostgreSQL Global Development Group | PostgreSQL License | parsed |
| postgres-docs | PostgreSQL Documentation | PostgreSQL Global Development Group | PostgreSQL License | parsed |
| mongodb-glossary | MongoDB Manual Glossary | MongoDB, Inc. | CC BY-NC-SA 3.0 Unported | parsed |
| ostep | Operating Systems: Three Easy Pieces | Arpaci-Dusseau and Arpaci-Dusseau (University of Wisconsin-Madison) | unknown (no explicit license on site) | parsed |
| nist-glossary | NIST CSRC Glossary | NIST (US government) | public domain (US government work) | parsed |
| rfc3022 | RFC 3022: Traditional IP Network Address Translator | IETF | RFC license | parsed |
| rfc768 | RFC 768: User Datagram Protocol | IETF | unknown (no copyright statement) | parsed |

## Gaps

- **NIST DADS unreachable:** The NIST Dictionary of Algorithms and Data Structures (xlab.nist.gov/dads) was unreachable during the access audit, so it is not cited. OpenDSA and Wikipedia cover the data-structures subject instead.
- **OSTEP chapter PDFs not machine-readable:** Chapter numbers and titles were confirmed from the table of contents; chapter body text was not directly fetched, so OSTEP citations are chapter-level only.
- **NIST term slugs:** Several NIST glossary slugs (ip_address, mac_address, subnet, socket, ethernet) returned 404 and are not cited; those terms were sourced from other allowed sources or omitted.
- **NoSQL terms:** Normalization/normal forms, "NoSQL" itself, key-value store and document store are not defined in the read sources, so they are omitted rather than invented.
- **System design gaps:** CAP theorem, horizontal/vertical scaling, failover, redundancy, message broker, SLO nines and generic architecture terms were not found as entries in the read sources and are omitted.
- **UDP:** NIST had no definition for UDP, so it is sourced from RFC 768.
- **Language-specific terms:** CPython, GIL, PEP and similar are omitted; definitions aim to be vendor- and language-neutral.

## Method

- Toolchain: webfetch for sources; manual paraphrase; JSON authoring; `scripts/validate-collection.py` for validation.
- Source priority: official documentation and open textbooks first (Python docs, MDN, PostgreSQL, AWS, RFCs), then open textbooks (OpenDSA, OSTEP), then government glossaries (NIST), then encyclopedias (Wikipedia) for orientation only.
- Verification coverage: all 356 definitions were checked against their cited locators during authoring; confusables validated to exist within the same subject.

## Validation

```
python3 scripts/validate-collection.py data/collections/software-interview-glossary
```

Result: exits 0 (VALIDATION PASSED).

## Wiring

Load the runtime bundle into the app's `SUBJECTS` array without editing the app:

```js
const collection = await fetch('data/collections/software-interview-glossary/runtime.json').then(r => r.json());
const SUBJECTS = collection.subjects;
```

The app already consumes `{ id, name, color, dark, defs: [[term, def, formula]] }`, which is exactly what `runtime.json` provides.

## Disclaimer

Not applicable (non-regulated collection).
