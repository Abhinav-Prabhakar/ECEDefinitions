# Fix definitions that give away their own term

You are cleaning up the subject data for **one·liners**, a flashcard/quiz app for ECE
definitions. Work only in `data/subjects/*/*.json`. Do not touch `index.html`, any other
code, `data/curriculum.json` or `data/sources.json`.

## Why

The quiz has two question types:

- **term → definition**: shows a term, the student picks its definition.
- **definition → term**: shows a definition, the student picks its term.

The second type breaks when the definition names its own term. *"A stack is an ordered
collection…"* answers itself. The app now blanks the term out automatically (it shows
*"The ___ is an ordered collection…"*), but that reads awkwardly and doesn't catch every
case. Your job is to rewrite those definitions so they define the term without naming it.

## Your checklist

Run the audit script. Its output is your to-do list:

```bash
python3 scripts/audit-definition-leaks.py --no-echo
```

It prints one block per subject file. Fix every line marked:

| Flag      | Meaning                                                    | Fix |
|-----------|------------------------------------------------------------|-----|
| `SELF`    | Definition contains its own term                           | Rewrite so the term (and its plural/possessive) doesn't appear. |
| `ACRONYM` | Definition spells out an acronym term (DNS → "Domain Name System") | Rewrite to describe what it *does*, without the expansion. |
| `TWIN`    | Two definitions are identical once their terms are hidden  | Add the detail that tells them apart (see example below). |

Then look at the warnings (`echo`), shown when you drop `--no-echo`. These are softer:
all the term's words reappear in the definition in some form (e.g. *Magnetization* →
"…of a magnetized specimen"). Fix them when the rewrite is easy and keeps the meaning.
Skip them when the shared word is unavoidable technical vocabulary.

Work one subject file at a time. The worst files are `cyber-security`,
`python-programming` and `data-structures`; start with those.

## How to rewrite

Keep the existing rules for a definition (from `prompts/seed-curriculum-agent.md`):
one sentence, **8–28 words**, standalone, technical, consistent spelling within the
subject. Also:

1. **Keep the meaning.** Rephrase only; never change what is being defined. Don't add facts
   that aren't in the original sentence or its cited source.
2. **Drop the "X is …" lead-in.** Start with the category instead.
   - Before: `A stack is an ordered collection of homogeneous elements where insertion and deletion occur at one end called top.`
   - After: `An ordered collection of homogeneous elements where insertion and deletion occur only at one end, called the top.`
3. **Don't replace the term with an obvious synonym or a near-copy.** "A last-in-first-out
   list" for *LIFO* or "Protection of integrity" for *Integrity* still gives it away.
   Describe the behaviour or purpose.
   - Before (`DNS`): `Domain Name System: maps host names to IP addresses and vice versa using distributed, hierarchical name servers.`
   - After: `Internet service that maps host names to IP addresses and back using a distributed hierarchy of name servers.`
4. **Mentioning *other* terms is fine.** "An element of a linked list…" is OK for *Node*;
   only the term being defined must not appear.
5. **Twins: add the one distinguishing detail.**
   - Before: `Time for transient to decay in an RL circuit.` / `Time for transient to decay in an RC circuit.`
   - After: `Time for the transient to decay in a circuit of inductance and resistance, equal to inductance divided by resistance.`
     *(The extra detail comes from the entry's own formula, τ=L/R. Only use detail that's in the formula field or the source.)*
6. **Leave everything else alone.** Don't change `id`, `term`, `formula`, `unit`,
   `unitTitle` or `sources`. Don't reorder, add or delete entries. Keep the JSON formatting
   (2-space indent, UTF-8, real Unicode characters).

If a definition genuinely can't be written without the term (rare: e.g. the term is a
single everyday word with no other description), leave it and list it in your final report.

## Done means

1. `python3 scripts/audit-definition-leaks.py --no-echo` ends with
   `0 blocking finding(s)` (or only the entries you listed as impossible).
2. `python3 scripts/validate-seed-data.py` still passes. It checks the 8–28 word rule and
   the schema.
3. `git diff --stat` shows changes only under `data/subjects/`.
4. Commit per semester folder (e.g. `Rewrite self-naming definitions in 3-2 subjects`),
   so the diff is reviewable.

Finish with a short report: how many definitions you rewrote per subject, which `echo`
warnings you skipped and why, and anything you couldn't fix.
