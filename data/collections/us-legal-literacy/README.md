# US Legal Literacy

## What this collection is

- **Topic:** US legal literacy for non-lawyers and first-year law students.
- **Audience:** Non-lawyers and 1L students, with no prior legal training assumed.
- **Level:** intro — general principles, vocabulary, and doctrinal shape, not the rule in any one state.
- **Jurisdiction:** US (federal law and general US common law). State variation is noted only where a
  source makes it the point.
- **Spelling:** US
- **Regulated:** yes (educational vocabulary only; not legal advice)
- **Assumptions:** federal references mean the US Constitution, federal statutes, and the Federal Rules
  unless stated; no state-specific statutory detail; vocabulary and doctrine only, no exam strategy.

Vocabulary only. Every definition is a one-sentence, standalone statement of a term, chosen because a
beginner would otherwise have to stop and look it up.

## Totals

- Sections: 2 (`foundations`, `doctrines`)
- Subjects: 6
- Definitions: 277
- Complete subjects: 6
- Partial subjects: 0
- Inaccessible subjects: 0
- Cues (`formula`): 133 of 277 carry a citation, symbol, or test name

## Coverage table

| Subject | Status | Definitions | Units covered | Sources |
| --- | --- | --- | --- | --- |
| Sources of Law and Courts | complete | 50 | 6/6 | 2 |
| Civil and Criminal Procedure | complete | 48 | 6/6 | 4 |
| Constitutional Rights | complete | 43 | 6/6 | 4 |
| Contracts | complete | 43 | 5/5 | 2 |
| Torts | complete | 45 | 5/5 | 2 |
| Criminal Law | complete | 48 | 5/5 | 2 |

Unit coverage by subject:

- **Sources of Law and Courts** — sources of law; federal courts; state courts; jurisdiction and venue;
  precedent and stare decisis; legal authority and citation.
- **Civil and Criminal Procedure** — commencing a lawsuit; pleadings and motions; discovery; trial and
  judgment; appeals and finality; criminal process stages.
- **Constitutional Rights** — Bill of Rights fundamentals; First Amendment freedoms; due process; equal
  protection; search, seizure, and criminal process rights; incorporation and state action.
- **Contracts** — formation; consideration and capacity; defenses to formation; performance and breach;
  remedies.
- **Torts** — negligence; intentional torts; strict liability and products liability; damages; defenses.
- **Criminal Law** — elements and actus reus; mens rea and culpability; major offenses; defenses;
  punishment and sentencing.

## Sources

| ID | Title | Publisher | License | Status |
| --- | --- | --- | --- | --- |
| usll-wex | Wex: Legal Dictionary and Encyclopedia | Cornell LII | CC BY-NC-SA 2.5 | parsed |
| usll-uscourts-federal-courts | About Federal Courts | Administrative Office of the U.S. Courts | public domain (US government) | parsed |
| usll-frcp | Federal Rules of Civil Procedure | Cornell LII | public domain law text; LII compilation CC BY-NC-SA 2.5 | parsed |
| usll-frcrmp | Federal Rules of Criminal Procedure | Cornell LII | public domain law text; LII compilation CC BY-NC-SA 2.5 | parsed |
| usll-ucc-article-2 | Uniform Commercial Code, Article 2 — Sales | Cornell LII | CC BY-NC-SA 2.5 (LII edition) | parsed |
| usll-doj-justice-101 | Justice 101: Steps in the Federal Criminal Process | US Department of Justice | public domain (US government) | parsed |
| usll-constitution-annotated | Constitution Annotated | Congressional Research Service / Library of Congress | public domain (US government) | parsed |
| usll-lii-constitution-conan | U.S. Constitution Annotated (LII edition) | Cornell LII | CC BY-NC-SA 2.5 | parsed |
| usll-archives-bill-of-rights | Bill of Rights transcript (Amendments I–X) | US National Archives | public domain (US government) | parsed |
| usll-ussc-glossary | Glossary of Federal Sentencing-Related Terms | US Sentencing Commission | public domain (US government) | parsed |
| usll-openstax-business-law-i-essentials-2e | Business Law I Essentials 2e, ch. 6 | OpenStax (Rice University) | CC BY-NC-SA 4.0 | parsed |

All sources are free to read. Two publisher pages were unreliable and were worked around rather than
cited loosely: the National Archives Bill of Rights *landing* page omits the amendment text, so the
transcript URL is cited; and Constitution Annotated essays on constitution.congress.gov sit behind a
Cloudflare challenge, so the three definitions that depend on a single essay cite the LII edition of the
same annotation instead.

## Gaps

**Out of scope by design.** Evidence, intellectual property, privacy, tax, employment, corporate, and
real estate law, administrative rulemaking, and state-specific statutory detail. The queue lists these as
separate collections. No definition gives legal advice or predicts an outcome.

**Terms deliberately left out.**

- `Concurrence` (the act-and-intent requirement) — no accessible authoritative source turned up; written
  from no source would be fabrication, so it is absent.
- `Bail`, `Nolo contendere`, `Motion to suppress`, `Speedy trial`, `Presentence report`, `Work product`,
  `Subpoena`, `Docket` — read and sourced during extraction, cut to keep units at 8–10 definitions.
- `Trespass to land`, `Conversion`, `Wrongful death`, `Loss of consortium`, `Gross negligence` — read and
  sourced, cut from Torts for the same reason.
- `Novation`, `Assignment`, `Accord and satisfaction`, `Frustration of purpose`, `Battle of the forms`
  (§ 2-207), `Unjust enrichment`, `Reformation`, `Cover`, `Incidental damages` — read and sourced, cut
  from Contracts.
- `Arson`, `Rape`, `Kidnapping`, `Extortion`, `Forgery`, `Embezzlement`, `Fraud`, `Solicitation`,
  `Accessory`, `Three strikes` — read and sourced, cut from Criminal Law.
- `Bluebook`, `Shepardize`, `KeyCite` — brand or product names; no free authoritative entry.

**Deliberate overlap between subjects.** `Assault`, `Battery`, `Self-defense`, `Defense of others`, and
`Proximate cause` appear in both Torts and Criminal Law, with definitions scoped to civil versus criminal
liability. `Duress (contract law)` / `Duress (criminal law)` and `Strict liability` (tort) /
`Strict liability crime` are qualified so the two senses are never confused. Other duplicates found at
merge time were removed rather than qualified: `Supremacy Clause` and `Sovereign immunity` live in Sources
of Law and Torts; `Removal`, `Remand`, and `Res judicata` live in Procedure; `Mitigation of damages` and
`Nominal damages` live in Torts.

**Source coverage limits.** uscourts.gov deep links for trial and appellate procedure returned 404s, so
the criminal-process stages cite the Department of Justice's Justice 101 guide and the Federal Rules
instead. Wex has no entry for some terms (`risk-utility test`, `design defect`, `concurrence`); where the
content sits inside a parent entry, the locator names the in-entry heading on that page.

## Method

- **Toolchain:** the collection was planned from `DOMAIN-CATALOG.md` and `COLLECTION-QUEUE.md`, built by one
  extraction pass per subject, merged, and validated with `scripts/validate-collection.py`.
- **Source priority:** official government text and rules first (Federal Rules, UCC, US Code material,
  National Archives, USSC), then LII Wex and the LII edition of Constitution Annotated, then open
  textbooks. OpenStax *American Government 2e* was **not** used: the current OpenStax terms prohibit
  ingestion into large language models, so it was dropped rather than cited.
- **Paraphrase:** every definition was written from what the source says, not copied. Verbatim overlap was
  checked during verification.
- **Verification:** automated checks ran over all 277 definitions (word count, sentence count, banned
  phrasing, term length, cue length, unit/unitTitle match, confusable existence and self-reference,
  locator shape and scheme, duplicate terms and pairs, runtime equality, counts, index entry). Every cited
  source page was then fetched independently (203 pages) and each definition was scored for keyword
  overlap against its cited page; the 24 lowest-scoring definitions were read against the fetched text by
  hand. **60 definitions (22%) received a full line-by-line support and paraphrase check** across all six
  subjects and all 33 units. That clears the 30-definition acceptance gate but is **below the 50%
  verification target** in the collection brief: the two planned verifier passes could not run because the
  subagent quota was exhausted, so the remaining definitions were checked mechanically and by citation
  resolution only. Raising coverage to 50% is the first follow-up task for this collection.
- **Fixes applied after verification:** one unsupported clause removed (`Burglary`'s nighttime-element
  claim, not stated by the cited entry), and three single-source citations repointed to a resolvable
  edition of the same annotation.

## Validation

```bash
python3 scripts/validate-collection.py data/collections/us-legal-literacy
```

Result: `VALIDATION PASSED` (exit 0).

No app files were changed. No raw source files (PDF/HTML/DOCX) were committed; downloads stayed in
`/tmp/oneliners-us-legal-literacy/`.

## Wiring

The runtime bundle is derived from the subject files and matches the app's existing `SUBJECTS` shape:

```js
const collection = await fetch('data/collections/us-legal-literacy/runtime.json').then(r => r.json());
const SUBJECTS = collection.subjects; // [{ id, name, short, color, dark, defs: [[term, def, formula]] }]
```

Section grouping (`Foundations` / `Core doctrines`) lives in `collection.json`; the app can ignore it.

## Review

Law changes, but the vocabulary here is doctrinal and stable. Re-check the procedure and constitutional
subjects against the current Federal Rules and Supreme Court terms annually, and re-read the `Burglary`
and qualified-`Duress` definitions first if state law diverges.

## Disclaimer

Educational vocabulary only; not legal advice. Definitions state general US principles and are not a
substitute for advice from a licensed attorney in the relevant jurisdiction.
