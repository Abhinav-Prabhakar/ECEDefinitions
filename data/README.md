# Seed Curriculum Data — Coverage Report

Machine-generated seed data for the one·liners app, extracted from the
[SNIST ECE A22 materials](https://drive.google.com/drive/folders/1XEQJJ6fjY8OfCSDD8PqQOmTZgQQP3_G6)
Google Drive folder. This is a coverage report, not marketing copy.

- **Semesters:** 8 (1-1 … 4-2)
- **Subjects:** 41 (33 with data, 8 stubs)
- **Definitions:** 1575, all with ≥1 source locator (`p.N`, `slide.N`, `para.N`)
- **Sources catalogued:** 250 (`data/sources.json`), all downloaded; 0 inaccessible
- **Status spread:** 26 complete · 7 partial · 6 unresolved elective/PP stubs · 1 no-materials stub · 1 empty semester
- **Validator:** `python3 scripts/validate-seed-data.py` → `VALIDATION OK`
  (41 subjects / 1575 definitions / 26-7-8)

Everything below derives from the college's own course files. **No raw source
files are redistributed in this repository** — only definitions, formulas,
locators and the source manifest. See the "not redistributing" note at the end.

---

## Totals

| Sem | Definitions | Subjects with data | Complete | Partial | Stubs |
|-----|------------:|-------------------:|---------:|--------:|------:|
| 1-1 | 113 | 3 | 2 | 1 | 0 |
| 1-2 | 189 | 4 | 4 | 0 | 0 |
| 2-1 | 299 | 6 | 6 | 0 | 0 |
| 2-2 | 275 | 7 | 6 | 0 | 1 |
| 3-1 | 237 | 5 | 4 | 1 | 2 |
| 3-2 | 249 | 5 | 3 | 1 | 3+1* |
| 4-1 | 213 | 5 | 1 | 4 | 1 |
| 4-2 | 0 | 0 | 0 | 0 | — (entire semester `no_materials`) |
| **Σ** | **1575** | **33** | **26** | **7** | **8** |

\* Python Programming is counted here as a data subject (40 defs); its
`status` is `unresolved` because the folder name does not identify the subject
unambiguously.

Complete = ≥20 definitions and ≥6 covered units.

## Per-semester table

### 1-1 · I Year I Semester
| Subject | Code | Status | Defs | Units | Sources |
|---|---|---|---:|---:|---:|
| Engineering Physics | 9HC07 | complete | 60 | 6/6 | 8 |
| Matrix Algebra and Calculus | 9HC11 | partial | 5 | 1/6 | 1 |
| Problem Solving using C | 9FC01 | complete | 48 | 6/6 | 6 |

### 1-2 · I Year II Semester
| Subject | Code | Status | Defs | Units | Sources |
|---|---|---|---:|---:|---:|
| Advanced Calculus | 9HC12 | complete | 50 | 6/6 | 7 |
| Data Structures | 9EC01 | complete | 48 | 6/6 | 6 |
| Electrical Circuits & Networks Analysis | 9AC42 | complete | 50 | 6/6 | 6 |
| Engineering Chemistry | 9HC04 | complete | 41 | 6/6 | 6 |

### 2-1 · II Year I Semester
| Subject | Code | Status | Defs | Units | Sources |
|---|---|---|---:|---:|---:|
| Business Economics and Financial Analysis | 9ZC01 | complete | 50 | 6/6 | 5 |
| Complex Variable and Transform Techniques | 9HC14 | complete | 47 | 6/6 | 9 |
| Electronic Devices and Circuits | 9CC01 | complete | 50 | 6/6 | 8 |
| Environmental Science | 9HC05 | complete | 48 | 6/6 | 6 |
| Probability Theory and Stochastic Process | 9CC03 | complete | 47 | 6/6 | 6 |
| Signals and Systems | 9CC02 | complete | 57 | 6/6 | 9 |

### 2-2 · II Year II Semester
| Subject | Code | Status | Defs | Units | Sources |
|---|---|---|---:|---:|---:|
| Analog & Digital Communications | 9CC06 | complete | 50 | 6/6 | 6 |
| Analog Circuits | 9CC04 | complete | 50 | 6/6 | 10 |
| Digital Logic Design | 9CC05 | complete | 47 | 6/6 | 6 |
| Electromagnetic Waves and Transmission Lines | 9C407 | complete | 53 | 6/6 | 7 |
| Quantitative Aptitude and Logical Reasoning | 9HC16 | complete | 40 | 6/6 | 6 |
| Universal Human Values | 9HC03 | complete | 35 | 6/6 | 6 |
| Technical Seminar | 9C461 | no_materials | 0 | — | — |

### 3-1 · III Year I Semester
| Subject | Code | Status | Defs | Units | Sources |
|---|---|---|---:|---:|---:|
| Antennas and Wave Propagations | 9C510 | complete | 49 | 6/6 | 4 |
| Artificial Intelligence | 9EC41 | complete | 50 | 6/6 | 6 |
| Digital Signal Processing | 9CC08 | partial | 37 | 3/6 | 3 |
| IC Applications | 9CC09 | complete | 50 | 6/6 | 5 |
| Linear Control Systems | 9AC07 | complete | 51 | 6/6 | 6 |
| Open Elective I | — | unresolved | 0 | — | — |
| Professional Elective I | — | unresolved | 0 | — | — |

### 3-2 · III Year II Semester
| Subject | Code | Status | Defs | Units | Sources |
|---|---|---|---:|---:|---:|
| Cyber Security | 9FC78 | complete | 50 | 6/6 | 6 |
| Microprocessors and Microcontrollers | 9CC15 | complete | 59 | 6/6 | 5 |
| Microwave and Optical Communications | 9C611 | complete | 50 | 6/6 | 8 |
| Python Programming | 8FC22 | unresolved | 40 | 3/6 | 3 |
| VLSI Technology and Design | 9C612 | partial | 50 | 5/6 | 6 |
| Open Elective II | — | unresolved | 0 | — | — |
| Professional Elective II | — | unresolved | 0 | — | — |
| Professional Elective III | — | unresolved | 0 | — | — |

### 4-1 · IV Year I Semester
| Subject | Code | Status | Defs | Units | Sources |
|---|---|---|---:|---:|---:|
| Advanced Communications and Networks | 9C714 | partial | 43 | 3/6 | 3 |
| Computer Networks | 9EC05 | complete | 50 | 6/6 | 7 |
| Embedded Real Time Operating Systems | 9C731 | partial | 40 | 4/6 | 5 |
| Internet of Things and Applications | 9C713 | partial | 40 | 3/6 | 3 |
| System on Chip Architecture | 9C835 | partial | 40 | 3/6 | 3 |
| Open Elective III | — | unresolved | 0 | — | — |

### 4-2 · IV Year II Semester
No material was published in the Drive folder for 4-2; the semester is present
in `curriculum.json` with an empty subject list.

---

## Access gaps

Every file listed in `data/sources.json` was downloaded successfully — there
are **no 403/404/needs-auth gaps** to report. Remaining gaps are availability
gaps in the Drive folder itself:

| Gap | Location | What was attempted / state |
|---|---|---|
| Semester 4-2 | `ECE 4-2` folder | Folder contains no subject material; semester seeded as empty. |
| Technical Seminar (2-2) | `ECE 2-2/TS` | Folder exists but holds no extractable material; stub with `data: null`. |
| Elective slots OE-I, PE-I, OE-II, PE-II, PE-III, OE-III | 3-1, 3-2, 4-1 | Folders exist, but the folder names alone do not say which elective each batch takes; left `unresolved` with `data: null`. App owner can resolve from a batch timetable and name the subjects. |
| "PP" folder (3-2) | `ECE 3-2/PP` | Contains three "Python Programming" decks (code 8FC22 per course structure). Resolved as Python Programming but marked `unresolved` because the folder abbreviation alone is ambiguous. Units 1–3 extracted; units 4–6 had no decks. |
| Matrix Algebra & Calculus (1-1) | `ECE 1-1/MAC` | Only one usable deck (Unit 4); 5 definitions, unit 4 only. |

## Extraction gaps (units with no definitions)

| Subject | Covered | Missing units and why |
|---|---|---|
| Matrix Algebra and Calculus (1-1) | 1/6 | Only Unit-4 deck published in the folder. |
| Digital Signal Processing (3-1) | 3/6 | Units 4-6 exist only as question papers, which are excluded as definition sources. |
| VLSI Technology and Design (3-2) | 5/6 | No deck/handout with unit-6 content in the folder. |
| Python Programming (3-2) | 3/6 | Folder contains decks only for units 1-3. |
| Advanced Communications and Networks (4-1) | 3/6 | Units 4-6 decks not published in the folder. |
| Internet of Things and Applications (4-1) | 3/6 | Material covers units 1-3 only. |
| Embedded RTOS (4-1) | 4/6 | Units 5-6 not published (only ERTOS intro + Unix/RTS decks). |
| System on Chip Architecture (4-1) | 3/6 | Material covers units 1-3 only. |

Skipped as definition sources (per brief): model/previous question papers and
question banks — they are catalogued in `sources.json` but never cited by a
definition.

## Locator verification

Definition sources are verified mechanically against the files they cite:

- **1293/1575 (82%)** definitions have a locator whose cited page/slide literally
  contains the term's tokens ("token-verified").
- During verification, **123 locators pointed at the wrong page/slide**
  (conversion slide drift between `.ppt` → `.pptx`, or extractor miscounts).
  These were automatically relocated to the nearest page containing the term.
- **167 definitions** cite pages with no text layer (scanned PDFs or image
  slides) — "blank". These cannot be machine-verified cheaply; they were spot
  checked by OCR (below).
- **98 additional definitions** are "weak": the term tokens do not literally
  appear on the cited page (paraphrased decks, or the def is sourced from a
  unit/section header page). The wording was derived from those files during
  extraction.

Per-subject blank/weak counts (`ok / weak / blank`):

| Subject | ok | weak | blank |
|---|---:|---:|---:|
| advanced-calculus | 0 | 13 | 37 |
| analog-circuits | 9 | 0 | 41 |
| digital-signal-processing | 0 | 0 | 37 |
| complex-variable-and-transform-techniques | 8 | 17 | 22 |
| microwave-and-optical-communications | 30 | 20 | 0 |
| electromagnetic-waves-and-transmission-lines | 34 | 1 | 18 |
| signals-and-systems | 30 | 17 | 10 |
| quantitative-aptitude-and-logical-reasoning | 29 | 11 | 0 |
| universal-human-values | 34 | 1 | 0 |
| computer-networks | 42 | 8 | 0 |
| internet-of-things-and-applications | 33 | 7 | 0 |
| linear-control-systems | 48 | 1 | 2 |
| data-structures | 47 | 1 | 0 |
| electronic-devices-and-circuits | 49 | 1 | 0 |
| antennas-and-wave-propagations | 48 | 1 | 0 |
| ic-applications | 44 | 6 | 0 |
| digital-logic-design | 45 | 2 | 0 |
| cyber-security | 49 | 1 | 0 |
| microprocessors-and-microcontrollers | 53 | 6 | 0 |
| system-on-chip-architecture | 39 | 1 | 0 |

(Subjects with 100% ok are omitted.)

**OCR spot-check of scanned files:** 30 sampled (source, term, page) triples
across the scanned-PDF subjects (advanced-calculus, analog-circuits, DSP, CVTT,
MWOC, SOCA, UHV, QALR) were rendered and OCR'd with Tesseract. 12 confirmed the
term tokens literally; in a further ~7 the wire-of-page content matched the
term topically (e.g. the "conservative field" page contains "there exists a
scalar potential φ such that F = ∇φ") but handwriting-grade OCR noise hides
the literal tokens; 4 sampled pages are cover/blank scans. The handwritten
decks (e.g. `AC Unit 6.pdf`, 45 pages of handwriting) could not be OCR-verified
at all; their locators rest on the extraction pass and are documented as
unverified rather than silently dropped.

## Method

- Course structure and syllabus docx files define subject names, codes,
  semester labels, unit titles and course types; Drive folder layout decides
  semester placement.
- Files downloaded to a local cache, hashed (sha256 in `sources.json`), parsed
  with python-pptx (pptx), PyMuPDF (pdf) and LibreOffice conversions for
  legacy `.ppt` decks. The raw files are **not** part of this repository.
- Extraction priority: instructor unit decks > consolidated notes/question
  collections > question banks (never cited) > question papers (never cited).
- Every definition: one sentence 8-28 words, one source id + pinpoint locator,
  source must belong to the same subject in `sources.json`.
- A locator-audit script recomputed every citation against the parsed file
  text; wrong-pinpoint locators were auto-relocated; the residual
  blank/weak classes are reported above instead of being hidden.

## Decisions for the app owner

1. **ESE and UHV folder placement kept as-is** (Environmental Science in 2-1,
   Universal Human Values in 2-2) to match the Drive folder layout, even
   though the official course structure lists UHV in 3-1/ESE elsewhere.
   Change in one place (`curriculum.json` semesters array) if the official
   order should win.
2. **"PP" folder** resolved as *Python Programming* (8FC22) but left
   `unresolved` for confirmation; material for units 4-6 is missing entirely.
3. **Elective singletons resolved:** PE-IV → *Embedded Real Time Operating
   Systems* (9C731), PE-V → *System on Chip Architecture* (9C835). The other
   multi-candidate elective folders (OE-I/PE-I/OE-II/PE-II/PE-III/OE-III) stay
   `unresolved` stubs; fill them in `curriculum.json` when the batch timetable
   is known.
4. **PTSP Bayes theorem / total probability** cite the unit-1 outline slide
   (`ptsp-unit-1-ptsp#slide.20`) because the material contains no statement
   slide for these theorems; treat as section-level sourcing.
5. **Locator scheme honours the file type** (`slide.N` for decks incl. legacy
   converted `.ppt`, `p.N` for PDFs, `para.N` for docx and reference-question
   files). Definitions frontend should present locator strings verbatim.
6. **Scanned/handwritten decks are shown as unverified** (blank class) rather
   than dropped; a human pass over the ~167 blank-confidence citations in
   analog-circuits, advanced-calculus, DSP and EMTL is the highest-value
   follow-up.

## Not redistributing raw source files

This dataset derives facts (definitions, formulas) from the SNIST ECE A22
Drive materials and cites every fact back to a pinpoint locator
(`data/sources.json` → Drive file ids and URLs). The raw PDFs/PPTs
themselves are **not committed** to this repository; users reach the source
through the `viewUrl`/`downloadUrl` on each source entry.
