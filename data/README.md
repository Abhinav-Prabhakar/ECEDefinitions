# Seed Curriculum Data — Coverage Report

Curriculum data for the one·liners app. Definitions come first from the
[SNIST ECE A22 materials](https://drive.google.com/drive/folders/1XEQJJ6fjY8OfCSDD8PqQOmTZgQQP3_G6)
Google Drive folder; units the folder does not cover were filled from the official
A22 syllabus topics using cited web sources. This is a coverage report, not marketing copy.

- **Semesters:** 8 (1-1 … 4-2)
- **Subjects:** 52 (51 complete, 1 stub: Technical Seminar) — includes the 17 elective options below
- **Definitions:** 2,773, all with ≥1 source locator — 1,948 from Drive files, 825 from web sources
- **Sources catalogued:** 587 (`data/sources.json`): 298 Drive files, 289 web pages (`kind: "web"`)
- **Validator:** `python3 scripts/validate-seed-data.py` → `VALIDATION OK`
- **Formula check:** `node scripts/check-formulas.mjs` → `FORMULA CHECK OK`
- **Leak audit:** `python3 scripts/audit-definition-leaks.py --no-echo` → 0 blocking findings
- **Notation layer:** 1,662 definitions carry a bare-LaTeX `formula`; 624 carry a `diagram`
  id from the shared 198-symbol sprite. Coverage is deliberately uneven (physics/devices
  high, programming/management/values low). See `prompts/diagram-catalog.md`.

**No raw source files are redistributed in this repository** — only definitions,
formulas, locators and the source manifest. See the note at the end.

---

## Totals

| Sem | Definitions | Subjects with data | Complete | Stubs |
|-----|------------:|-------------------:|---------:|------:|
| 1-1 | 156 | 3 | 3 | 0 |
| 1-2 | 189 | 4 | 4 | 0 |
| 2-1 | 299 | 6 | 6 | 0 |
| 2-2 | 275 | 6 | 6 | 1 |
| 3-1 | 622 | 11 | 11 | 0 |
| 3-2 | 787 | 14 | 14 | 0 |
| 4-1 | 445 | 7 | 7 | 0 |
| 4-2 | 0 | 0 | 0 | — (no taught courses) |
| **Σ** | **2,773** | **51** | **51** | **1** |

Complete = every syllabus unit has definitions.

**Notation on those definitions:** 1,662 carry an equation, 624 carry one of 198 diagram
symbols, and 431 carry a cold surface — 92 code, 186 spec tables, 40 sequences and 113
derivations. 15 diagrams also carry hand-marked label points for the figure → label quiz.
Artifacts live under `data/artifacts/parts/` and are merged into `data/artifacts.json` by
`scripts/build-artifacts.py`; they never change the definition text.

## Per-semester table

### 1-1 · I Year · I Semester
| Subject | Code | Status | Defs | Units | Sources | Web-sourced defs |
|---|---|---|---:|---:|---:|---:|
| Engineering Physics | 9HC07 | complete | 60 | 6/6 | 8 | 0 |
| Matrix Algebra and Calculus | 9HC11 | complete | 48 | 6/6 | 22 | 43 |
| Problem Solving using C | 9FC01 | complete | 48 | 6/6 | 6 | 0 |

### 1-2 · I Year · II Semester
| Subject | Code | Status | Defs | Units | Sources | Web-sourced defs |
|---|---|---|---:|---:|---:|---:|
| Advanced Calculus | 9HC12 | complete | 50 | 6/6 | 7 | 0 |
| Data Structures | 9EC01 | complete | 48 | 6/6 | 6 | 0 |
| Electrical Circuits & Networks Analysis | 9AC42 | complete | 50 | 6/6 | 6 | 0 |
| Engineering Chemistry | 9HC04 | complete | 41 | 6/6 | 6 | 0 |

### 2-1 · II Year · I Semester
| Subject | Code | Status | Defs | Units | Sources | Web-sourced defs |
|---|---|---|---:|---:|---:|---:|
| Business Economics and Financial Analysis | 9ZC01 | complete | 50 | 6/6 | 5 | 0 |
| Complex Variable and Transform Techniques | 9HC14 | complete | 47 | 6/6 | 9 | 0 |
| Electronic Devices and Circuits | 9CC01 | complete | 50 | 6/6 | 8 | 0 |
| Environmental Science | 9HC05 | complete | 48 | 6/6 | 6 | 0 |
| Probability Theory and Stochastic Process | 9CC03 | complete | 47 | 6/6 | 6 | 0 |
| Signals and Systems | 9CC02 | complete | 57 | 6/6 | 9 | 0 |

### 2-2 · II Year · II Semester
| Subject | Code | Status | Defs | Units | Sources | Web-sourced defs |
|---|---|---|---:|---:|---:|---:|
| Analog & Digital Communications | 9CC06 | complete | 50 | 6/6 | 6 | 0 |
| Analog Circuits | 9CC04 | complete | 50 | 6/6 | 10 | 0 |
| Digital Logic Design | 9CC05 | complete | 47 | 6/6 | 6 | 0 |
| Electromagnetic Waves and Transmission Lines | 9C407 | complete | 53 | 6/6 | 7 | 0 |
| Quantitative Aptitude and Logical Reasoning | 9HC16 | complete | 40 | 6/6 | 6 | 0 |
| Universal Human Values | 9HC03 | complete | 35 | 6/6 | 6 | 0 |
| Technical Seminar | 9C461 | no_materials | 0 | 0/0 | 0 | 0 |

### 3-1 · III Year · I Semester
| Subject | Code | Status | Defs | Units | Sources | Web-sourced defs |
|---|---|---|---:|---:|---:|---:|
| Antennas and Wave Propagations | 9C510 | complete | 49 | 6/6 | 4 | 0 |
| Artificial Intelligence | 9EC41 | complete | 50 | 6/6 | 6 | 0 |
| Digital Signal Processing | 9CC08 | complete | 64 | 6/6 | 17 | 27 |
| IC Applications | 9CC09 | complete | 50 | 6/6 | 5 | 0 |
| Linear Control Systems | 9AC07 | complete | 51 | 6/6 | 6 | 0 |
| Basics of Entrepreneurship *(Open Elective I)* | 9ZC22 | complete | 49 | 6/6 | 6 | 0 |
| Programming in Java *(Open Elective I)* | 9EC42 | complete | 60 | 6/6 | 22 | 60 |
| Artificial Neural Networks *(Professional Elective I)* | 9C517 | complete | 54 | 6/6 | 17 | 54 |
| CMOS Analog IC Design *(Professional Elective I)* | 9C518 | complete | 64 | 6/6 | 16 | 31 |
| Computer Organization and Architecture *(Professional Elective I)* | 9C519 | complete | 79 | 6/6 | 9 | 0 |
| Software Defined Radio *(Professional Elective I)* | 9C516 | complete | 52 | 6/6 | 10 | 52 |

### 3-2 · III Year · II Semester
| Subject | Code | Status | Defs | Units | Sources | Web-sourced defs |
|---|---|---|---:|---:|---:|---:|
| Cyber Security | 9FC78 | complete | 50 | 6/6 | 6 | 0 |
| Microprocessors and Microcontrollers | 9CC15 | complete | 59 | 6/6 | 5 | 0 |
| Microwave and Optical Communications | 9C611 | complete | 50 | 6/6 | 8 | 0 |
| Python Programming | 8FC22 | complete | 67 | 6/6 | 11 | 27 |
| VLSI Technology and Design | 9C612 | complete | 61 | 6/6 | 11 | 11 |
| Advanced Entrepreneurship *(Open Elective II)* | 9ZC23 | complete | 57 | 6/6 | 6 | 0 |
| Database Systems Concepts *(Open Elective II)* | 9FC79 | complete | 67 | 6/6 | 16 | 67 |
| Digital Image Processing *(Professional Elective II)* | 9C621 | complete | 56 | 6/6 | 24 | 56 |
| Embedded C Programming *(Professional Elective II)* | 9C623 | complete | 34 | 6/6 | 6 | 0 |
| Satellite Communication *(Professional Elective II)* | 9C620 | complete | 55 | 6/6 | 21 | 55 |
| VLSI Physical Design *(Professional Elective II)* | 9C622 | complete | 60 | 6/6 | 11 | 25 |
| Ad Hoc and Wireless Sensor Networks *(Professional Elective III)* | 9C724 | complete | 55 | 6/6 | 19 | 55 |
| Design Verification using SystemVerilog *(Professional Elective III)* | 9C726 | complete | 63 | 6/6 | 24 | 63 |
| Embedded System Design using ARM *(Professional Elective III)* | 9C727 | complete | 53 | 6/6 | 6 | 0 |

### 4-1 · IV Year · I Semester
| Subject | Code | Status | Defs | Units | Sources | Web-sourced defs |
|---|---|---|---:|---:|---:|---:|
| Advanced Communications and Networks | 9C714 | complete | 70 | 6/6 | 12 | 27 |
| Computer Networks | 9EC05 | complete | 50 | 6/6 | 7 | 0 |
| Embedded Real Time Operating Systems | 9C731 | complete | 58 | 6/6 | 13 | 18 |
| Internet of Things and Applications | 9C713 | complete | 67 | 6/6 | 17 | 27 |
| System on Chip Architecture | 9C835 | complete | 67 | 6/6 | 9 | 27 |
| Operating Systems Concepts *(Open Elective III)* | 9EC43 | complete | 68 | 6/6 | 21 | 68 |
| Product and Services *(Open Elective III)* | 9ZC24 | complete | 65 | 6/6 | 11 | 32 |

### 4-2 · IV Year · II Semester
No taught courses: the A22 course structure lists only project work for 4-2, and the Drive folder is empty.

---

## Elective options

Each elective slot folder holds several options; every option is its own subject
in the slot's semester, with an `elective` field (e.g. `"Professional Elective I"`)
in both its `curriculum.json` entry and its data file. The validator was
extended to accept that optional key on curriculum entries.

| Slot | Option (folder) | Full name | Code | Name confirmed from |
|---|---|---|---|---|
| OE-I (3-1) | BOE | Basics of Entrepreneurship | 8ZC22 | A22 CSE open-elective table ([PDF](https://sreenidhi.edu.in/wp-content/uploads/2024/02/A22-Regulation-CSE-I-to-II-year-complete.pdf), p.8) lists it in the Entrepreneurship stream; the BOE decks teach entrepreneurship, business models, finance, teams and marketing |
| OE-I (3-1) | JAVA | Programming in Java | 9EC42 | resolved from the A22 open-elective lists and syllabus during the web fill-in; folder is empty, so all units are web-sourced |
| PE-I (3-1) | ANN | Artificial Neural Networks | 9C517 | A22 ECE 3rd/4th syllabus (PE-I list) |
| PE-I (3-1) | CMOS | CMOS Analog IC Design | 9C518 | A22 ECE syllabus; deck title "Introduction to Analog IC Design" |
| PE-I (3-1) | COA | Computer Organization and Architecture | 9C519 | A22 ECE syllabus; decks titled "Computer Organization and Architecture" |
| PE-I (3-1) | SDR | Software Defined Radio | 9C516 | A22 ECE syllabus (PE-I list) |
| OE-II (3-2) | AE | Advanced Entrepreneurship | 8ZC23 | deck title slide "ADVANCED ENTREPRENEURSHIP"; A22 CSE open-elective table |
| OE-II (3-2) | DBSC | Database Systems Concepts | 9FC79 | resolved from the A22 open-elective lists and syllabus during the web fill-in; folder is empty, so all units are web-sourced |
| PE-II (3-2) | DIP | Digital Image Processing | 9C621 | A22 ECE syllabus (PE-II list) |
| PE-II (3-2) | ECP | Embedded C Programming | 9C623 | A22 ECE syllabus; deck title slide |
| PE-II (3-2) | SC | Satellite Communication | 9C620 | A22 ECE syllabus: the only "SC" option in the PE-II list; empty folder |
| PE-II (3-2) | VLSIPD | VLSI Physical Design | 9C622 | A22 ECE syllabus (PE-II list) |
| PE-III (3-2) | AWSN | Ad hoc and Wireless Sensor Networks | 9C724 | A22 ECE syllabus (PE-III list) |
| PE-III (3-2) | DVSV | Design Verification using System Verilog | 9C726 | A22 ECE syllabus (PE-III list) |
| PE-III (3-2) | ESD | Embedded System Design using ARM | 9C727 | A22 ECE syllabus; the decks cover ARM (older slide header reads "Embedded System Design", code 7C724) |
| OE-III (4-1) | OSC | Operating Systems Concepts | 9EC43 | resolved from the A22 open-elective lists and syllabus during the web fill-in; folder is empty, so all units are web-sourced |
| OE-III (4-1) | P&S | Product and Services | 8ZC24 | deck title slide "Product & Services"; A22 CSE open-elective table |

Notes:

- The A22 ECE syllabus ([3rd & 4th year docx](https://drive.google.com/file/d/1AauDZ2R77O7dsJp-mPMRuMOHrpK5Smm6/view))
  lists 9C516–9C519 as PE-I (III-I), 9C620–9C623 as PE-II (III-II) and
  9C724–9C727 as PE-III (**IV-I**). The Drive keeps PE-III under 3-2, so it stays
  there; move it in `curriculum.json` if the official order should win.
- The entrepreneurship codes (8ZC22–8ZC24) are from the A22 CSE course structure,
  where the same stream is listed as OE-I/II/III in 3-2/4-1/4-2. The A22 ECE
  syllabus only lists ECE-offered open electives (9CC36–9CC38), none of which is a
  Drive option. Semester placement follows the Drive folders.
- Locators on the new subjects were checked mechanically: every cited slide/page
  contains the term's tokens or enough of the definition's wording.
- Unit titles for the entrepreneurship/product decks (BOE, AE, P&S) come from
  the deck headers; where a deck has no title the `unitTitle` is `null`.

## Web-sourced units

The Drive folder does not cover every unit. Where it doesn't, definitions were written
from the official A22 syllabus topics for that unit and cited to web pages that were
opened and read (`kind: "web"` in `sources.json`, locators like `#section-name`).
Most are Wikipedia; the rest are vendor and language documentation (Oracle Java,
Python, NumPy, pandas, Matplotlib), ChipVerify, IETF and the SNIST site.

| Subject | Units with web-sourced definitions |
|---|---|
| Ad Hoc and Wireless Sensor Networks | 1, 2, 3, 4, 5, 6 |
| Advanced Communications and Networks | 4, 5, 6 |
| Artificial Neural Networks | 1, 2, 3, 4, 5, 6 |
| CMOS Analog IC Design | 1, 2, 3, 4, 5, 6 |
| Database Systems Concepts | 1, 2, 3, 4, 5, 6 |
| Design Verification using SystemVerilog | 1, 2, 3, 4, 5, 6 |
| Digital Image Processing | 1, 2, 3, 4, 5, 6 |
| Digital Signal Processing | 1, 2, 3 |
| Embedded Real Time Operating Systems | 5, 6 |
| Internet of Things and Applications | 4, 5, 6 |
| Matrix Algebra and Calculus | 1, 2, 3, 5, 6 |
| Operating Systems Concepts | 1, 2, 3, 4, 5, 6 |
| Product and Services | 4, 5, 6 |
| Programming in Java | 1, 2, 3, 4, 5, 6 |
| Python Programming | 4, 5, 6 |
| Satellite Communication | 1, 2, 3, 4, 5, 6 |
| Software Defined Radio | 1, 2, 3, 4, 5, 6 |
| System on Chip Architecture | 4, 5, 6 |
| VLSI Physical Design | 3, 4, 5, 6 |
| VLSI Technology and Design | 4 |

Remaining gaps:

| Gap | State |
|---|---|
| Technical Seminar (2-2) | Seminar course with no taught content; kept as a stub with `data: null`. |
| Semester 4-2 | Project semester: the course structure lists no theory courses and the Drive folder is empty. |

Skipped as definition sources: model/previous question papers and question banks.
They are catalogued in `sources.json` but never cited.

## Locator verification

Drive-sourced definitions are verified mechanically against the files they cite
(figures below are from the original 1,575-definition seed pass):

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
- Units with no Drive material: syllabus topic list → reputable pages actually
  opened → one-line paraphrases, cited as `<web-source-id>#<section>`.
- Every definition: one sentence 8-28 words, never containing its own term, one source id + pinpoint locator,
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
2. **"PP" folder** is Python Programming (8FC22); units 4–6 had no decks and were
   web-sourced, so the subject is now complete.
3. **Elective singletons resolved:** PE-IV → *Embedded Real Time Operating
   Systems* (9C731), PE-V → *System on Chip Architecture* (9C835). The six
   multi-option folders (OE-I, PE-I, OE-II, PE-II, PE-III, OE-III) are imported
   as one subject per option; see "Elective options" below.
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
