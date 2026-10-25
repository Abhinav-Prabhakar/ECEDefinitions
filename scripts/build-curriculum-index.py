#!/usr/bin/env python3
"""Build data/curriculum.json from the subject files under data/subjects/.

The app reads only this index at runtime. Each batch of real curriculum data is a
set of subject JSON files; run this script after adding a batch to make the new
subjects appear on the home page.

Usage:
    python3 scripts/build-curriculum-index.py
"""

from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SUBJECTS_DIR = ROOT / "data" / "subjects"
OUT = ROOT / "data" / "curriculum.json"

SEMESTERS = [
    ("1-1", "I Year · I Semester", 1, 1),
    ("1-2", "I Year · II Semester", 1, 2),
    ("2-1", "II Year · I Semester", 2, 1),
    ("2-2", "II Year · II Semester", 2, 2),
    ("3-1", "III Year · I Semester", 3, 1),
    ("3-2", "III Year · II Semester", 3, 2),
    ("4-1", "IV Year · I Semester", 4, 1),
    ("4-2", "IV Year · II Semester", 4, 2),
]

# Course-structure order. Unknown subjects fall back to alphabetical order.
ORDER = {
    "1-1": [
        "engineering-physics",
        "matrix-algebra-and-calculus",
        "problem-solving-using-c",
    ],
    "1-2": [
        "engineering-chemistry",
        "data-structures",
        "advanced-calculus",
        "electrical-circuits-and-networks-analysis",
    ],
    "2-1": [
        "electronic-devices-and-circuits",
        "signals-and-systems",
        "probability-theory-and-stochastic-process",
        "complex-variable-and-transform-techniques",
        "business-economics-and-financial-analysis",
        "universal-human-values",
        "environmental-science",
    ],
    "2-2": [
        "analog-circuits",
        "digital-logic-design",
        "analog-and-digital-communications",
        "electromagnetic-waves-and-transmission-lines",
        "quantitative-aptitude-and-logical-reasoning",
        "technical-seminar",
        "universal-human-values",
    ],
    "3-1": [
        "digital-signal-processing",
        "ic-applications",
        "antennas-and-wave-propagations",
        "linear-control-systems",
        "artificial-intelligence",
    ],
    "3-2": [
        "microprocessors-and-microcontrollers",
        "vlsi-technology-and-design",
        "microwave-and-optical-communications",
        "cyber-security",
    ],
    "4-1": [
        "advanced-communications-and-networks",
        "internet-of-things-and-applications",
        "computer-networks",
    ],
    "4-2": [],
}

SOURCE = {
    "name": "SNIST ECE A22 materials",
    "driveUrl": "https://drive.google.com/drive/folders/1XEQJJ6fjY8OfCSDD8PqQOmTZgQQP3_G6",
    "syllabusDocs": [
        {"name": "A22 ECE-1ST&2ND SYLLABUS.docx", "fileId": "1AelYd-5qilr2zwKfwPe-VSpvhlMvQgk4"},
        {"name": "A22-ECE-3RD&4TH SYLLABUS.docx", "fileId": "1AauDZ2R77O7dsJp-mPMRuMOHrpK5Smm6"},
        {"name": "ECE COURSE STRUCTRE 2022 BATCH 1 -4TH YEAR.docx", "fileId": "1AgmornqtRQgE7764lC2tEY8ZYcSNX1-I"},
    ],
}


def read_subject(path: Path, semester: str) -> dict | None:
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - we want a useful build warning
        print(f"skip {path}: {exc}", file=sys.stderr)
        return None

    definitions = raw.get("definitions") or []
    if not isinstance(definitions, list) or not definitions:
        print(f"skip {path}: no definitions", file=sys.stderr)
        return None

    units = sorted({
        d.get("unit")
        for d in definitions
        if isinstance(d, dict) and isinstance(d.get("unit"), int)
    })
    sources = {
        str(s).split("#", 1)[0]
        for d in definitions
        if isinstance(d, dict)
        for s in (d.get("sources") or [])
        if s
    }

    subject_id = raw.get("id") or path.stem
    rel = path.relative_to(ROOT).as_posix()
    status = raw.get("status") or "complete"
    if status == "complete" and len(definitions) < 20:
        status = "partial"

    return {
        "id": subject_id,
        "name": raw.get("name") or subject_id.replace("-", " ").title(),
        "shortName": raw.get("shortName") or "",
        "code": raw.get("code") or "",
        "courseType": raw.get("courseType") or "",
        "folderId": raw.get("folderId") or "",
        "folderUrl": raw.get("folderUrl") or "",
        "data": rel,
        "definitionCount": len(definitions),
        "unitCount": len(units),
        "coveredUnits": len(units),
        "status": status,
        "sourceCount": len(sources),
    }


def main() -> int:
    if not SUBJECTS_DIR.is_dir():
        print(f"missing {SUBJECTS_DIR}", file=sys.stderr)
        return 1

    by_semester: dict[str, list[dict]] = {sid: [] for sid, *_ in SEMESTERS}
    for path in sorted(SUBJECTS_DIR.glob("*/*.json")):
        semester = path.parent.name
        if semester not in by_semester:
            print(f"skip {path}: unknown semester folder {semester}", file=sys.stderr)
            continue
        subject = read_subject(path, semester)
        if subject:
            by_semester[semester].append(subject)

    semesters = []
    for sid, label, year, term in SEMESTERS:
        subjects = by_semester[sid]
        rank = {name: i for i, name in enumerate(ORDER.get(sid, []))}
        subjects.sort(key=lambda s: (rank.get(s["id"], len(rank)), s["name"].lower()))

        if not subjects:
            status = "no_materials" if sid == "4-2" else "pending"
        elif all(s["status"] == "complete" for s in subjects):
            status = "complete"
        else:
            status = "partial"

        semesters.append({
            "id": sid,
            "label": label,
            "year": year,
            "term": term,
            "status": status,
            "subjects": subjects,
        })

    all_subjects = [s for sem in semesters for s in sem["subjects"]]
    coverage = {
        "semesters": len(semesters),
        "semestersWithMaterials": sum(1 for sem in semesters if sem["subjects"]),
        "subjects": len(all_subjects),
        "definitions": sum(s["definitionCount"] for s in all_subjects),
        "completeSubjects": sum(1 for s in all_subjects if s["status"] == "complete"),
        "partialSubjects": sum(1 for s in all_subjects if s["status"] == "partial"),
        "inaccessibleSubjects": sum(1 for s in all_subjects if s["status"] == "inaccessible"),
    }

    payload = {
        "version": 1,
        "generatedAt": date.today().isoformat(),
        "source": SOURCE,
        "semesters": semesters,
        "coverage": coverage,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"wrote {OUT.relative_to(ROOT)}: "
        f"{coverage['subjects']} subjects, {coverage['definitions']} definitions, "
        f"{coverage['semestersWithMaterials']} semesters with materials"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
