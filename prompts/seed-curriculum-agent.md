# Agent brief: seed the real one·liners curriculum

You are the **orchestrator**. Your job is to turn the college Drive materials into a clean,
validated, source-traced curriculum dataset for the one·liners app. You will launch smaller
subagents to extract definitions from individual subjects, then validate and merge their
work. **You will not wire the app.** The app owner will do that after reviewing the data.

Work in the existing repository:

```
/Users/abhinav/Projects/ECEDefinitions
```

Create a branch named `seed/real-curriculum` from `main`. Do not push to `main`.
Do not edit `index.html`, `design.md`, the root `README.md`, `manifest.webmanifest`,
`sw.js`, or `assets/`. Only add data and data tooling under `data/` and `scripts/`
(including the allowed `data/README.md` coverage report).

If you have git/gh access, commit the generated data and open a **draft PR** against `main`.
If you do not, leave the branch/worktree in place and report the paths.

---

## 1. Mission

Produce a real, semester-grouped curriculum from the college materials here:

**Drive folder (public, “SNIST (by Vishwak Bhojaraju)”):**

```
https://drive.google.com/drive/folders/1XEQJJ6fjY8OfCSDD8PqQOmTZgQQP3_G6
```

It contains ECE A22 materials organised by semester and subject, plus:

- `A22 ECE-1ST&2ND SYLLABUS.docx` — file id `1AelYd-5qilr2zwKfwPe-VSpvhlMvQgk4`
- `A22-ECE-3RD&4TH SYLLABUS.docx` — file id `1AauDZ2R77O7dsJp-mPMRuMOHrpK5Smm6`
- `ECE COURSE STRUCTRE 2022 BATCH 1 -4TH YEAR.docx` — file id `1AgmornqtRQgE7764lC2tEY8ZYcSNX1-I`

Use the **course structure** for official subject names, codes, semester labels and
course types. Use the **syllabus documents** for unit titles and scope. Use the folder
abbreviations only as hints; the official names win.

The final dataset must:

- group subjects by **semester 1-1 through 4-2** (4-2 is in the syllabus but has no Drive
  folder; include it as an empty/`no_materials` semester),
- preserve the official course name/code,
- give every definition a **source locator** back to a Drive file,
- be accurate, concise, one-line, quiz-ready,
- be valid JSON, validated by a script you write and run.

---

## 2. Non-negotiables

1. **No hallucination.** Every definition and formula must be grounded in the supplied
   materials. If the materials do not support a definition, omit it. Never fill gaps from
   general knowledge, model memory or the open web.
2. **No raw source files in the repo.** Download them only to a temporary work directory
   such as `/tmp/ece-seed-sources/`. Commit only derived JSON, metadata, reports and the
   validator. Do not commit PDFs, PPTX, DOCX, images or copyrighted source text.
3. **No app changes.** Do not touch UI, styles, PWA, the root README or design.md.
4. **Source traceability.** Every definition has one or more `sourceIds` pointing to
   entries in `data/sources.json`, with a page/slide/paragraph locator.
5. **Access is not guaranteed.** Parts of this Drive may require the operator’s signed-in
   Google session. Never bypass permissions. If a source is inaccessible, mark it and
   continue; do not invent content and do not silently drop a whole subject.
6. **Quality over quota.** A smaller accurate set is better than padded low-quality
   entries. Do not duplicate the same idea across units to hit a count.
7. **No UI decisions.** Do not assign colours or write taglines. The app owns visuals.
8. **Definition shape.** One sentence, 8–28 words, standalone, technical, and readable
   without the slide/page. No “as shown above”, “this”, “the following”, author names,
   dates, university names, textbook citations, lab instructions or exam instructions.

---

## 3. What I already verified (2026-10-24)

The link is a shared ECE A22 folder. The root has seven semester folders:

- `ECE 1-1` … `ECE 4-1`
- No `ECE 4-2` folder.
- `ECE 1-1/EP/Unit 1 Quantum Mechanics.pdf` (file id
  `10J_NAUmGwwrvGJWRvn25X9F6hcGTKLNW`) downloaded successfully: a 20-page PDF.
- `ECE 1-1/EP/Unit 5 Semiconductor Devices.pptx` (file id
  `1-ykCnPHwVU528oREsr8GzpahUkD8XbLD`) downloaded successfully: text-bearing slides
  including diode, PN junction, depletion region, space charge and LED/solar-cell topics.
- The syllabus/course-structure DOCX files downloaded successfully.

**Access caveat:** the root and semester listings are reachable, but some nested subject
folder pages can render empty in a headless browser, and the
`embeddedfolderview?id=…#list` endpoint returns 404 for child folders. The Engineering
Physics folder and two of its files were reachable without auth. Do not
assume an empty-looking nested folder has no files. Use the Drive web UI in a focused
browser tab and, where available, the operator’s authenticated session. If a folder truly
cannot be read, log it as `inaccessible`.

Do a full **access audit before extraction** and write it into the final report. If more
than ~25% of subject folders are inaccessible, produce the partial dataset anyway,
clearly mark coverage, and stop before claiming completeness.

### Practical Drive access playbook

- Root/semester listings: `https://drive.google.com/embeddedfolderview?id=<FOLDER_ID>#list`
  returns static HTML with folder/file titles and ids. This is useful for discovery.
- For nested subject folders, use Playwright/Chrome with a focused tab:
  `https://drive.google.com/drive/folders/<FOLDER_ID>?usp=sharing`.
  Read the rendered rows and links. Do not trust a background tab that has not rendered.
- Direct downloads:
  `https://drive.google.com/uc?export=download&id=<FILE_ID>`
  (add `&confirm=t` for large files). Use a browser user agent.
- `gdown --folder "<folder URL>"` is a useful public-folder fallback if installed.
- Do not use an unauthenticated Drive API key. Do not scrape signed URLs that you do not
  have permission to use.

---

## 4. Semester and subject map

These are the **observed folder abbreviations** mapped to the official A22 names. Verify
each against the syllabus and the folder contents. Treat `?` as unresolved.

| Semester | Folder | Official subject (verify) | Code | Type |
| --- | --- | --- | --- | --- |
| 1-1 | EP | Engineering Physics | 9HC07 | BS |
| 1-1 | MAC | Matrix Algebra and Calculus | 9HC11 | BS |
| 1-1 | PSUC | Problem Solving using C | 9FC01 | ES |
| 1-2 | AC | Advanced Calculus | 9HC12 | BS |
| 1-2 | DS | Data Structures | 9EC01 | ES |
| 1-2 | EC | Engineering Chemistry | 9HC04 | BS |
| 1-2 | ECNA | Electrical Circuits & Networks Analysis | 9AC42 | ES |
| 2-1 | BEFA | Business Economics and Financial Analysis | 9ZC01 | HS |
| 2-1 | CVTT | Complex Variable and Transform Techniques | 9HC14 | BS |
| 2-1 | EDC | Electronic Devices and Circuits | 9CC01 | PC |
| 2-1 | ESE | Environmental Science | 9HC05 | MC |
| 2-1 | PTSP | Probability Theory and Stochastic Process | 9CC03 | BS |
| 2-1 | SS | Signals and Systems | 9CC02 | PC |
| 2-2 | AC | Analog Circuits | 9CC04 | PC |
| 2-2 | ADC | Analog & Digital Communications | 9CC06 | PC |
| 2-2 | DLD | Digital Logic Design | 9CC05 | PC |
| 2-2 | EMTL | Electromagnetic Waves and Transmission Lines | 9C407 | PC |
| 2-2 | QALR | Quantitative Aptitude and Logical Reasoning | 9HC16 | BS |
| 2-2 | TS | Technical Seminar | 9C461 | PW |
| 2-2 | UHV | Universal Human Values | 9HC03 | HS |
| 3-1 | AI | Artificial Intelligence | 9EC41 | MC |
| 3-1 | AWP | Antennas and Wave Propagations | 9C510 | PC |
| 3-1 | DSP | Digital Signal Processing | 9CC08 | PC |
| 3-1 | ICA | IC Applications | 9CC09 | PC |
| 3-1 | LCS | Linear Control Systems | 9AC07 | ES |
| 3-1 | OE-I | Open Elective I | null | OE |
| 3-1 | PE-I | Professional Elective I | null | PE |
| 3-2 | CYS | Cyber Security | 9FC78 | MC |
| 3-2 | MPMC | Microprocessors and Microcontrollers | 9CC15 | PC |
| 3-2 | MWOC | Microwave and Optical Communications | 9C611 | PC |
| 3-2 | OE-II | Open Elective II | null | OE |
| 3-2 | PE-II | Professional Elective II | null | PE |
| 3-2 | PE-III | Professional Elective III | null | PE |
| 3-2 | PP | ? (resolve from contents/course plan) | null | ? |
| 3-2 | VLSITD | VLSI Technology and Design | 9C612 | PC |
| 4-1 | ACN | Advanced Communications and Networks | 9C714 | PC |
| 4-1 | CN | Computer Networks | 9EC05 | ES |
| 4-1 | IOTA | Internet of Things and Applications | 9C713 | PC |
| 4-1 | OE-III | Open Elective III | null | OE |
| 4-1 | PE-IV | Professional Elective IV | null | PE |
| 4-1 | PE-V | Professional Elective V | null | PE |

Container folders are **not subjects**:

- `Assignments`
- `Notes`
- `Model Papers`
- `Previous Year Questions` / `Previous Year Question Papers` / `PYQs`

Use their contents as additional sources for the semester's subjects. For elective folders,
resolve the actual elective name from the folder contents and the elective tables in the
course structure. If the specific name cannot be verified, keep the generic name and mark
`status: "unresolved"`; do not invent an elective name.

4-2 has no Drive folder. Include it in the semester index with `status: "no_materials"` and
no subjects (or project-only note). Do not invent project content.

### Known folder ids (verify; observed 2026-10-24)

```text
Root                       1XEQJJ6fjY8OfCSDD8PqQOmTZgQQP3_G6
1-1                        1-2oFJX_ZI18GVFE-dpLY9czuDklrCCcM
1-2                        1--pNxwIWkZkbBSA4-6fHm0hZU__YaudI
2-1                        1-D3QV1ci36PCidOVmgc1aaK18L65D9GW
2-2                        1--WB71_GzzE_IExRI7CA99CQo0zwyNu9
3-1                        19bEweSP3SJz7MtKMi4vp2zMbvq7PJXBN
3-2                        1sT088DO4Xu0vVJqZAnNpoHLJG2IAnlet
4-1                        1zwukoqikA-Sm_y0Q_RVyIZL1zVjHRPKq

1-1/EP                     1-tjYwn0uyOM9CqeULd6YB6vHY-IlDdDc
1-1/MAC                    1-mWpn3WSll2yrWeDpFkwxLV0Xbj7RCd7
1-1/PSUC                   1-egOoW7h-t0EtDliqwVKpaI46GeEDWN2
1-2/AC                     1-eZM2w1kbF2fIbyA-tgw8AySj_vDD9Zw
1-2/DS                     1-ZENmdzP9mHdOvaGe63MvqA9mJurNz-7
1-2/EC                     1-YjSHrTK5bu-lgYXO6QT6H2iAxmRyIyF
1-2/ECNA                   1-UUZvdXEatKQixSn03iLvhLyuPv_pJTg
2-1/BEFA                   11NvDSB758iAX9D3EKOlfnOY3zvNzJOy_
2-1/CVTT                   12SERVHOAs_x6yHb19FbD_voR3KwBTAhd
2-1/EDC                    12PUYxKQWBux-2V6QDwTwRF3Lrlo38r4H
2-1/ESE                    12MieKCmLsZhrD3G_WgNsR8qQrGnf04nR
2-1/PTSP                   1293DShlPm0UJix1_SqCmAV5hKkBG3NKj
2-1/SS                     127z2rzz9eUmniBzfa0hwdKVrSFQLyY5N
2-2/AC                     1--dXq7BMH5wBDHyUFDxU-llB4nMaLypV
2-2/ADC                    1-3M2IAu2BzU8JY6v1HYC96pxUT5lK7NE
2-2/DLD                    1-5AcRmfVBVIvFB7GnABlRQlUfxNQLtXp
2-2/EMTL                   1-6I1xovYDsSxfYgsschy-FcCu5DLWZBc
2-2/QALR                   1-7ATdVsabh6QrBhovp7zOZp77KcGP11h
2-2/TS                     1xHnOkZOY3UWU4ilOl10QY0PoM8Sk8Blg
2-2/UHV                    1-DL2HLO0-QVB9tUbbrf06X59PJjKqmvb
3-1/AI                     15PUsow0log9o_jCmY2OwYl_o4cLs5ppZ
3-1/AWP                    1PwOdpM1sxnNK5OyzsAJ5-hW7b-bHsGxF
3-1/DSP                    1nLbYpitSRXGeI2BchP9BmcswOQirv4LD
3-1/ICA                    16ombVhb6YLWRNt3WQ7Yf7iJzZQHRWDAk
3-1/LCS                    1fRWPy3V1bMnl4amsOhTeOvM4Ra5iRj3X
3-1/OE-I                   1R7ins8vZhgDN_t7Q8njP6-XnknI-zQNq
3-1/PE-I                   1R6EZzlUWi-p2EKjNlq-6HvUiUtmHImap
3-2/CYS                    1hov_jUcf0Zy2K-CJkFboCHwH8kFVDyke
3-2/MPMC                   1ja783fNGAuoP9gRxtvzCqxrXNUDX7vpO
3-2/MWOC                   18ef3701IoNh_jhCRGX012jOFnorpejTm
3-2/OE-II                  1DiUP1tDLNRDAWd0WflkiXvgX4DxxCV8R
3-2/PE-II                  1OjNejp_C2FeGffJvxpfKmOA9ut74moHi
3-2/PE-III                 1c07MEduWqTD3XqGGj-36vv3rBCpFRrdp
3-2/PP                     1TbCKnWWIMcdAuvJsO-DNCDk0VZI2yWLu
3-2/VLSITD                 1QCzsKSV2gp_IjYXLEirUw_SUg8v_oNrN
4-1/ACN                    1jIpX-aHZt3vyhHMkZoLcuV8Ntr0bOy5o
4-1/CN                     1wyUHctxgd6_sN-1Ik_00kpbf58fqHSQR
4-1/IOTA                   1L8P5v5PIlwiAodMCdZmqdEsWg2cjvYLV
4-1/OE-III                 1xXXwdMmxosGY6hwTKG4Up-UHFhe_QNOp
4-1/PE-IV                  1kecqObpSdxgTDP0JbzrswXfzaiWLDOQr
4-1/PE-V                   1arVAiVCv0eOiwsK7Db6Q4NDBCRdssMS1
```

Container ids for 1-1: Assignments `1-wNyMzVjSwhfX4-Mv5aMnZbcDZYO6VFu`, Model Papers
`1-k_qClZ7rZBaZ4sBJZGIMkdLJCOZOPP5`. 1-2: Model Papers
`1-QT-upBL0qqGTDclDgiqRjIGb6VmPP2q`, Notes `1-NUD4zw9mIuAVnkUpmfYEjLjmiBDmeNV`.

---

## 5. Output contract

Create this tree (no other app files):

```text
data/
  curriculum.json                       # aggregate index the app will load
  subjects/
    1-1/
      engineering-physics.json          # one subject file
      matrix-algebra-and-calculus.json
      problem-solving-using-c.json
    1-2/
      advanced-calculus.json
      ...
    2-1/ ...
    2-2/ ...
    3-1/ ...
    3-2/ ...
    4-1/ ...
  sources.json                          # source manifest / access audit
  README.md                             # human coverage report
scripts/
  validate-seed-data.py                 # dependency-free validator
```

Do **not** create a data file for a subject with zero definitions; instead put a subject
stub in `curriculum.json` with `"status": "inaccessible"` or `"no_materials"` and
`"data": null`. The app can choose how to show it. Every subject with ≥1 definition must
have a file and a `data` path.

### `data/curriculum.json`

```json
{
  "version": 1,
  "generatedAt": "2026-10-24",
  "source": {
    "name": "SNIST ECE A22 materials",
    "driveUrl": "https://drive.google.com/drive/folders/1XEQJJ6fjY8OfCSDD8PqQOmTZgQQP3_G6",
    "syllabusDocs": [
      { "name": "A22 ECE-1ST&2ND SYLLABUS.docx", "fileId": "1AelYd-5qilr2zwKfwPe-VSpvhlMvQgk4" },
      { "name": "A22-ECE-3RD&4TH SYLLABUS.docx", "fileId": "1AauDZ2R77O7dsJp-mPMRuMOHrpK5Smm6" },
      { "name": "ECE COURSE STRUCTRE 2022 BATCH 1 -4TH YEAR.docx", "fileId": "1AgmornqtRQgE7764lC2tEY8ZYcSNX1-I" }
    ]
  },
  "semesters": [
    {
      "id": "1-1",
      "label": "I Year · I Semester",
      "year": 1,
      "term": 1,
      "status": "complete",
      "subjects": [
        {
          "id": "engineering-physics",
          "name": "Engineering Physics",
          "shortName": "EP",
          "code": "9HC07",
          "courseType": "BS",
          "folderId": "1-tjYwn0uyOM9CqeULd6YB6vHY-IlDdDc",
          "folderUrl": "https://drive.google.com/drive/folders/1-tjYwn0uyOM9CqeULd6YB6vHY-IlDdDc",
          "data": "data/subjects/1-1/engineering-physics.json",
          "definitionCount": 42,
          "unitCount": 6,
          "coveredUnits": 5,
          "status": "complete",
          "sourceCount": 8
        }
      ]
    }
  ],
  "coverage": {
    "semesters": 8,
    "subjects": 0,
    "definitions": 0,
    "completeSubjects": 0,
    "partialSubjects": 0,
    "inaccessibleSubjects": 0
  }
}
```

- Semester ids and labels: `1-1` → “I Year · I Semester”, `1-2` → “I Year · II Semester”,
  `2-1` → “II Year · I Semester”, `2-2` → “II Year · II Semester”, `3-1` → “III Year · I
  Semester”, `3-2` → “III Year · II Semester”, `4-1` → “IV Year · I Semester”, `4-2` →
  “IV Year · II Semester”.
- Include all 8 semesters. `4-2` is `{ "id":"4-2", ... "status":"no_materials", "subjects":[] }`.
- Subject ids: globally unique kebab-case slug of the official name (e.g.
  `engineering-physics`). If two official names collide, suffix the semester (`-1-2`).
  Never use the folder abbreviation as the id.
- Subject `status` values: `complete`, `partial`, `inaccessible`, `no_materials`,
  `unresolved`.
  - `complete`: all source units covered, ≥20 definitions.
  - `partial`: ≥1 definition but fewer sources/units; explain in `data/README.md`.
  - `inaccessible`: the folder/source could not be read; no definitions.
  - `no_materials`: no folder/materials at all (4-2).
  - `unresolved`: elective name could not be established; definitions may still exist.
- `definitionCount` must equal the array length. `unitCount` = number of distinct units in
  the syllabus; `coveredUnits` = distinct units in the definitions.
- The index must be generated from the subject files, not hand-maintained. The validator
  checks consistency.

### Subject file: `data/subjects/<semester>/<subject-id>.json`

```json
{
  "version": 1,
  "id": "engineering-physics",
  "semester": "1-1",
  "name": "Engineering Physics",
  "shortName": "EP",
  "code": "9HC07",
  "courseType": "BS",
  "folderId": "1-tjYwn0uyOM9CqeULd6YB6vHY-IlDdDc",
  "folderUrl": "https://drive.google.com/drive/folders/1-tjYwn0uyOM9CqeULd6YB6vHY-IlDdDc",
  "status": "complete",
  "definitions": [
    {
      "id": "quantum-mechanics",
      "term": "Quantum mechanics",
      "definition": "The branch of physics that describes matter and radiation using quantised energy states and probabilistic wavefunctions.",
      "formula": "E = hν",
      "unit": 1,
      "unitTitle": "Quantum Mechanics",
      "sources": [
        "ep-u1-quantum-mechanics#p.4",
        "ep-u5-semiconductor-devices#slide.3"
      ]
    }
  ]
}
```

Definition field rules:

- `id`: stable slug of the canonical term; unique within the subject. Don’t use ordinals.
  If two different terms collide, append a short parenthetical slug (e.g.
  `power-amplifier-class-a`).
- `term`: canonical course term, ≤ 48 characters, no trailing colon, no “Definition of”.
  Preserve acronyms and conventional capitalisation (`MOSFET`, `PN junction`, `CMRR`,
  `Fourier transform`). Title case for named concepts; sentence case for generic
  descriptive terms, consistent within a subject.
- `definition`: one sentence, 8–28 words, standalone. Define the thing, not its formula or
  an example. Use Indian/British spelling where the course does (`quantisation`,
  `polarisation`, `characteristic`), and be consistent.
- `formula`: optional. Empty string if none. ≤ 48 characters. Use real Unicode
  (subscripts, Greek, arrows, √) not LaTeX. Do not invent a formula.
- `unit`: integer 1–6 where the source/syllabus identifies it, otherwise `null`.
- `unitTitle`: from the syllabus; if absent, the source section title; otherwise `null`.
- `sources`: one or more locator strings `"<sourceId>#<locator>"`.
  - PDF: `p.4` (1-based page).
  - PPTX: `slide.7` (1-based slide).
  - DOCX: `para.12` or `section.Unit-I`.
  - A definition must not cite an inaccessible source.
- No `cue`/mnemonic invented by you. The app derives its explanation from the definition
  and formula. You may include a source-supported standard formula as `formula`.
- Do not include headings, slide titles, author names, dates, URLs, textbook references,
  “Applications:”, “Course outcomes”, or generic “Introduction” items as definitions.

### `data/sources.json`

```json
{
  "version": 1,
  "generatedAt": "2026-10-24",
  "sources": [
    {
      "id": "ep-u1-quantum-mechanics",
      "semester": "1-1",
      "subjectId": "engineering-physics",
      "driveFileId": "10J_NAUmGwwrvGJWRvn25X9F6hcGTKLNW",
      "name": "Unit 1 Quantum Mechanics.pdf",
      "folderPath": "ECE 1-1/EP/Unit 1 Quantum Mechanics.pdf",
      "mimeType": "application/pdf",
      "fileType": "pdf",
      "viewUrl": "https://drive.google.com/file/d/10J_NAUmGwwrvGJWRvn25X9F6hcGTKLNW/view",
      "downloadUrl": "https://drive.google.com/uc?export=download&id=10J_NAUmGwwrvGJWRvn25X9F6hcGTKLNW",
      "status": "downloaded",
      "sha256": "…",
      "locatorScheme": "p.<n>"
    }
  ]
}
```

- `status`: `downloaded`, `parsed`, `inaccessible`, `needs_ocr`, `skipped`.
- Include every file you inspected, including inaccessible ones, with the HTTP status or
  Drive error. Do not include raw file contents.
- `sourceId` is unique, lower-case, ASCII, stable.
- `sha256` is recommended for dedupe/provenance. If not computed, omit it consistently.
- The subject definitions’ source ids must exist here. The validator checks this.

### `data/README.md`

A human coverage report, not a marketing README:

- totals: semesters, subjects, definitions, complete/partial/inaccessible counts;
- a table per semester: subject, status, definitions, units covered, sources used;
- access gaps: folder/file, error (403/404/needs auth), what was attempted;
- extraction gaps: units with no definitions, skipped duplicate/low-quality slides, OCR
  needed;
- a short “method” section naming the toolchain and source-priority rules;
- a note: “This dataset is derived from the SNIST ECE A22 materials; raw source files are
  not redistributed.”

---

## 6. Source priority and extraction

For each subject:

1. **Syllabus / course structure** — official name, code, course type, unit titles,
   scope, electives. Use this to validate the folder mapping.
2. **Notes and unit PPTs/PDFs** — primary sources for definitions, formulas and unit
   context. Prefer the cleanest source. The first slide often names the unit; subsequent
   slides define terms.
3. **Model papers / previous-year questions** — use only to prioritise which terms matter
   and to spot obvious coverage gaps. A question paper is not a definition source; never
   invent a definition from a question alone.
4. **Assignments** — supplementary examples; generally not a definition source.
5. **Labs** — exclude lab procedures and equipment instructions.

Extraction rules:

- PPTX: use `python-pptx` if available; otherwise unzip `ppt/slides/slideN.xml` and extract
  `<a:t>` text and notes. Preserve slide numbers. Ignore decorative text, footers, slide
  numbers, and author names.
- PDF: use a text-layer extractor (`pdftotext`, PyMuPDF, pdfplumber). If a PDF has no text
  layer, mark `needs_ocr`; OCR only if you have a reliable local OCR workflow. Never OCR
  a low-quality scan and guess.
- DOCX: `python-docx` or unzip `word/document.xml`; preserve section/paragraph locators.
- Read the **course syllabus** for each subject; it tells you the units and what is in
  scope. Do not add a definition just because a word appears in a diagram.
- Prefer explicit “X is …” definitions and bold/heading terms. A single term may appear in
  multiple units; dedupe and merge with the best definition and all relevant source
  locators.
- Formulas: take them from the source and normalize the glyphs. If the formula is only an
  image, skip it unless you can read it confidently; do not describe an unread formula in
  prose as if it were exact.
- Keep a **per-subject decisions log** (counts and skipped items) in the subagent report;
  the orchestrator aggregates the important gaps into `data/README.md`.

---

## 7. Orchestration plan

Use a central orchestration pass and isolated subject subagents.

### Phase 0 — Inventory and access audit

1. Read the syllabus/course-structure DOCX files.
2. Crawl the Drive root, all seven semester folders, every subject folder, and the
   container folders.
3. Build a machine-readable work plan: semester, subject, official name/code/type, folder
   id/url, source files with ids/names/types, and access status.
4. Download all accessible source files to `/tmp/ece-seed-sources/<semester>/<subject>/`.
5. Extract the relevant syllabus unit list and (if possible) the elective tables into
   per-subject briefs.
6. Write `data/sources.json` and a preliminary access audit (you can update it later).
7. Do not start extraction until the inventory is settled.

### Phase 1 — Subject subagents

Launch **one subagent per subject with usable sources**, maximum **5 concurrently**. Each
receives:

- the subject metadata and output path,
- its local source directory and source ids,
- the relevant syllabus/unit titles,
- the exact schema and definition rules,
- the required report format.

Subagents write only their own subject JSON. They never edit `curriculum.json`,
`sources.json`, `data/README.md`, or app files. If they fail, retry once with a fresh
context; if still failing, return a failure report and let the orchestrator mark `partial`.

Do not over-provision subagents for subjects with no accessible sources. Mark those stubs
and move on.

### Phase 2 — Merge

1. Read every subject file. Validate per-subject schema and source references.
2. Deduplicate terms within each subject by normalized term + meaning.
3. Build `curriculum.json` from the subject files; compute counts/coverage; include
   empty/unresolved subjects as stubs.
4. Write `data/README.md` (coverage + access gaps).
5. Run `scripts/validate-seed-data.py` until it passes.
6. Spot-check at least **10% of definitions** (minimum 30 across the dataset) against the
   cited source locators. Fix unsupported or misleading entries. If a source is missing,
   remove the definition rather than guessing.

### Phase 3 — Delivery

- Commit only `data/` and `scripts/validate-seed-data.py`. No raw sources.
- Commit in logical chunks (inventory/access audit, per-semester subject files, aggregate +
  validator) and push the branch frequently.
- Open a draft PR titled `Seed real curriculum data from SNIST A22 materials` with:
  - definitions/subjects/semesters counts,
  - access gaps,
  - validation command/result,
  - explicit note that the app was not wired.
- Report back with the branch/PR, counts, and anything the app owner must decide
  (electives, 4-2, inaccessible folders).

---

## 8. Subagent brief template

Give each subject subagent a prompt equivalent to this (fill the placeholders):

> You are extracting definitions for exactly one subject in the one·liners curriculum.
>
> **Subject:** `<official name>` (`<semester>`), code `<code>`, folder `<shortName>`.
> **Output:** write `<data/subjects/<semester>/<subject-id>.json>` only.
> **Sources (local):** `<paths>`; source ids in `<sources.json entries>`.
> **Syllabus units:** `<unit titles / scope>`.
>
> **Task:** read every supplied source carefully and extract quiz-ready one-line
> definitions for this subject. Aim for 30–50 high-quality definitions (or 20–30 when the material is thin), covering every
> unit that has usable material. Quality and traceability matter more than count.
>
> **Rules:**
> - Every definition must be supported by a source locator; no general knowledge.
> - One sentence, 8–28 words; standalone; no “this”, “above”, author names, dates, URLs,
>   exam instructions, lab steps, or textbook citations.
> - `term` is the canonical course term, ≤48 chars, no trailing colon; `id` is a stable
>   slug; `formula` is optional, from the source, ≤48 chars, Unicode not LaTeX.
> - Assign `unit` (1–6) and `unitTitle` from the syllabus when identifiable.
> - Dedupe terms; prefer the clearest source; merge source locators.
> - Exclude generic headings, examples, derivations, and low-value nouns.
> - Output exactly the subject JSON schema. Do not edit any other file. Do not download or
>   commit raw files. Do not use web search or model memory for definitions.
>
> **Report back:** counts, units covered, sources used, definitions skipped and why, any
> access/extraction problems, and the path written.

For a subject with no accessible sources, do not launch an extraction subagent; mark a
stub and record the reason.

---

## 9. Validation & acceptance

Write `scripts/validate-seed-data.py` with no non-stdlib dependencies and run it. It must
check:

- valid JSON and exact required keys;
- all 8 semester ids present, ordered 1-1, 1-2, 2-1, 2-2, 3-1, 3-2, 4-1, 4-2;
- unique subject ids across the dataset; every subject file path resolves; index counts
  match the file;
- unique definition ids and terms within each subject;
- definition word count 8–28; term ≤48 chars; formula ≤48 chars or empty;
- `unit` integer 1–6 or null; `unitTitle` string or null;
- every source locator prefix exists in `data/sources.json` and has status not
  `inaccessible` for cited definitions;
- no definition cites a source from a different subject (unless the source is shared in
  that semester and explicitly mapped; prefer not);
- no empty definition text; no trailing spaces; no duplicate `(term, definition)`;
- subjects with `status: complete` have ≥20 definitions; partial subjects have ≥1 and are
  counted; inaccessible/no_materials subjects have no data file;
- the coverage totals are internally consistent.

Acceptance gate:

- validator exits 0;
- all files are UTF-8 JSON;
- no raw source files in the git diff;
- no app files changed;
- the dataset includes all accessible semester/subject materials and honestly marks gaps;
- the PR description contains counts, the validation command and the access gaps.

Do not relax the validator to hide missing data. Fix the data or mark the subject partial.

---

## 10. Stop conditions

Stop and report instead of guessing if:

- the Drive link or a large portion of nested folders requires authentication and cannot
  be accessed;
- the syllabus/course structure is unavailable and the official names/units cannot be
  established;
- a PDF requires OCR and no reliable OCR is available;
- the same folder contains conflicting materials that cannot be reconciled from the
  syllabus;
- the extraction would require inventing definitions to reach a target count.

A partial, honest dataset is acceptable. Fabricated data is not.

---

## 11. Final response expected

Report:

1. Branch/PR URL.
2. Definitions / subjects / semesters count.
3. Coverage per semester (a compact table).
4. Access gaps and unresolved electives/4-2.
5. Validator command and result.
6. Confirmation that no app files were changed and no raw source files were committed.
7. Any decisions the app owner needs to make before wiring.

The app owner will wire the data after reviewing this. Do not start that work.
