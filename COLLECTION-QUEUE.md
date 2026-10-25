# one·liners collection build queue

The active subset of [`DOMAIN-CATALOG.md`](DOMAIN-CATALOG.md), ordered for execution with
[`prompts/generate-collection-agent.md`](prompts/generate-collection-agent.md).

Work top to bottom. One collection at a time. When an item is done, move it to
**Completed** — the queue should get shorter as the library grows.

Status: `[ ]` queued · `[~]` in progress · `[x]` done · `[!]` blocked.

---

## How to work the queue

1. Read `prompts/generate-collection-agent.md` once. Treat it as fixed.
2. Pick the first unchecked item in **Queue**.
3. Change `[ ]` to `[~]` and add the start date if you want a visible claim.
4. Run the prompt with that item's **Topic** and **Scope**. For example:

   ```text
   Use prompts/generate-collection-agent.md for: Medical terminology
   Scope: word parts; body systems; clinical abbreviations; documentation; diagnostics;
   pharmacology basics.
   ```

5. Verify the **Definition of done** below.
6. Move the item to **Completed** with the date, collection path, and definition count.
7. If blocked, change it to `[!]` and add a one-line reason. Do not delete it.
8. Do not rebuild a completed collection unless the user asks for a new version.

**Concurrency:** process one collection at a time. The collection prompt already runs up to
five extraction subagents in parallel; running two collections at once makes the merge and
index updates fight each other.

---

## Definition of done

- `data/collections/<slug>/` contains `plan.json`, `collection.json`, `runtime.json`,
  `sources.json`, `README.md`, and `subjects/*.json`.
- `python3 scripts/validate-collection.py data/collections/<slug>` exits 0.
- `runtime.json` matches the authoring definitions exactly: same terms, definitions, cues, and order.
- `data/collections/index.json` includes the collection with correct counts.
- The README states coverage, sources, gaps, and assumptions.
- No app files were changed and no raw source files were committed.
- A `collection/<slug>` branch and draft PR exist if git and `gh` are available.

If the collection is honestly partial, keep it in the queue as `[!]` until the user accepts
it. Do not move a partial collection to Completed just to clear the line.

---

## Queue

### Software

- [x] **Software interview glossary** — `software-interview-glossary`
  - Scope: programming fundamentals; data structures and algorithms; system design;
    databases and SQL; operating systems and networking; web and browser.
  - Audience: mid-level software engineer interview candidates.
  - Target: 6 subjects, 300–400 definitions.

### Medical

- [x] **Medical terminology** — `medical-terminology`
  - Scope: word parts; body systems; clinical abbreviations; documentation; diagnostics;
    pharmacology basics.
  - Audience: pre-health undergraduates and nursing students.
  - Target: 6 subjects, 280–360 definitions.


- [ ] **Pathology** — `pathology`
  - Scope: cell injury and adaptation; inflammation and repair; neoplasia; hemodynamics;
    systems pathology.
  - Audience: medical and allied-health students.
  - Target: 5 subjects, 220–300 definitions.

- [ ] **Medical coding and billing** — `medical-coding-and-billing`
  - Scope: ICD-10-CM and PCS; CPT; modifiers and bundling; claims and reimbursement.
  - Audience: medical coding and revenue-cycle trainees.
  - Target: 4 subjects, 160–220 definitions.

### Trades and licenses

- [ ] **Electrical licensing (NEC)** — `electrical-licensing-nec`
  - Scope: conductors and wiring methods; overcurrent protection; grounding and bonding;
    GFCI and AFCI; load calculations.
  - Audience: electrician apprentices and journeyman exam candidates.
  - Target: 5 subjects, 200–260 definitions.

- [ ] **HVAC licensing** — `hvac-licensing`
  - Scope: refrigeration cycle; superheat and subcooling; psychrometrics; electrical
    controls; codes and safety.
  - Audience: HVAC apprentices and licensing candidates.
  - Target: 5 subjects, 180–240 definitions.

- [ ] **Plumbing licensing** — `plumbing-licensing`
  - Scope: supply systems; drain-waste-vent; traps and vents; backflow and fixtures; code.
  - Audience: plumbing apprentices and journeyman exam candidates.
  - Target: 5 subjects, 180–240 definitions.

- [ ] **Welding certification** — `welding-certification`
  - Scope: processes; joints and positions; welding symbols; defects and inspection;
    metallurgy and safety.
  - Audience: welding students and certification candidates.
  - Target: 5 subjects, 160–220 definitions.

- [ ] **Aviation (PPL)** — `aviation-ppl`
  - Scope: aerodynamics; aircraft systems; weather; navigation; regulations; human factors.
  - Audience: private pilot licence candidates (FAA).
  - Target: 6 subjects, 260–340 definitions.

- [ ] **Real estate licensing** — `real-estate-licensing`
  - Scope: property and ownership; contracts and agency; finance; valuation; law and
    practice.
  - Audience: state real estate pre-licensing candidates (US).
  - Target: 5 subjects, 200–260 definitions. Note state-specific variations.

- [ ] **Insurance licensing** — `insurance-licensing`
  - Scope: policy basics; life and health; property and casualty; underwriting and claims;
    regulation.
  - Audience: state insurance licensing candidates (US).
  - Target: 5 subjects, 200–260 definitions.

- [ ] **Solar installation** — `solar-installation`
  - Scope: PV fundamentals; site and array design; inverters and storage; NEC and net
    metering.
  - Audience: solar installers and entry-level designers.
  - Target: 4 subjects, 140–200 definitions.

### Law

- [ ] **US legal literacy** — `us-legal-literacy`
  - Scope: sources of law and courts; contracts; torts; criminal law; constitutional
    rights; procedure.
  - Audience: non-lawyers and first-year law students.
  - Target: 6 subjects, 240–300 definitions.

- [ ] **Contracts** — `contracts`
  - Scope: formation; consideration and defenses; performance and breach; remedies; UCC
    Article 2.
  - Audience: 1L students and business professionals.
  - Target: 5 subjects, 200–260 definitions.

- [ ] **Torts** — `torts`
  - Scope: negligence; intentional torts; strict liability; damages; defenses.
  - Audience: 1L students and legal literacy learners.
  - Target: 5 subjects, 180–240 definitions.

- [ ] **Criminal law** — `criminal-law`
  - Scope: elements and mens rea; major offenses; defenses; procedure; sentencing.
  - Audience: 1L students and criminal justice students.
  - Target: 5 subjects, 200–260 definitions.

- [ ] **Evidence** — `evidence`
  - Scope: relevance; hearsay; privileges and witnesses; burdens and exhibits.
  - Audience: law students and bar exam candidates.
  - Target: 4 subjects, 160–220 definitions.

- [ ] **Intellectual property** — `intellectual-property`
  - Scope: copyright; patent; trademark; trade secret; licensing and infringement.
  - Audience: founders, creators, and law students.
  - Target: 5 subjects, 200–260 definitions.

- [ ] **Privacy and data protection** — `privacy-and-data-protection`
  - Scope: GDPR; CCPA and CPRA; data minimisation and consent; cross-border transfers and
    incident response.
  - Audience: privacy, security, and product professionals.
  - Target: 4 subjects, 160–220 definitions.

---

## Completed

Move finished items here. Keep the date, collection path, and definition count so the
library has a history.

| Date | Topic | Collection path | Definitions | Notes |
| --- | --- | --- | --- | --- |
| 2026-10-25 | Software interview glossary | data/collections/software-interview-glossary | 356 | PR #1 draft |
| 2026-10-25 | Medical terminology | data/collections/medical-terminology | 327 | validation passed |
| 2026-10-25 | Anatomy and physiology | data/collections/anatomy-and-physiology | 285 | PR #3 draft |
| 2026-10-25 | Pharmacology | data/collections/pharmacology | 270 | validation passed; PR draft |
| 2026-10-25 | Nursing and NCLEX | data/collections/nursing-and-nclex | 347 | validation passed |

---

## Notes

- **The catalog is the menu; this file is the order.** Add new items from
  `DOMAIN-CATALOG.md` only when the user asks.
- **One collection, one branch.** Do not mix two collections in the same `collection/<slug>`
  branch.
- **Do not fork the prompt per collection.** If a collection needs a rule change, fix the
  prompt for everyone and note it here.
- **Partial is allowed; silent is not.** A `[!]` item with a clear reason is better than a
  completed item with invented definitions.
- **Delete nothing on a hunch.** Completed and blocked items are the audit trail.
