# Electrical licensing (NEC)

**Topic:** Electrical licensing (NEC) for electrician apprentices and journeyman exam candidates  
**Audience:** Electrician apprentices and journeyman exam candidates  
**Level:** intro  
**Jurisdiction:** US  
**Spelling:** US  
**Language:** en  
**Regulated:** true  

## Totals
- Sections: 1 (core)
- Subjects: 5
- Definitions: (to be updated)
- Complete/partial/inaccessible: (to be updated)

## Coverage table
(To be populated after extraction)

## Sources
(To be populated from subject reports)

## Gaps
(To be populated)

## Method
- Toolchain: subagent extraction per subject + orchestrator merge/verify/validate
- Source priority: NFPA 70 (NEC) related authoritative glossaries/standards references
- Verification: spot-check against cited locators per validator requirements

## Validation
- Command: `python3 scripts/validate-collection.py data/collections/electrical-licensing-nec`
- Result: (pending)

## Wiring
```js
const collection = await fetch('data/collections/electrical-licensing-nec/runtime.json').then(r => r.json());
const SUBJECTS = collection.subjects;
```
The app already consumes `{ id, name, color, dark, defs: [[term, def, formula]] }`, which is exactly what `runtime.json` provides.

## Disclaimer
Educational vocabulary only; not electrical advice or code compliance guidance.
