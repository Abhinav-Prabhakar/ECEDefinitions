#!/usr/bin/env python3
"""Dependency-free validator for the seeded one·liners curriculum dataset.

Checks schema, counts, cross-references and quality rules described in
prompts/seed-curriculum-agent.md §9. Exits non-zero on the first cluster of
errors (all errors are reported).
"""
import json, os, re, sys

REPO=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DAT=os.path.join(REPO,'data')
CUR=os.path.join(DAT,'curriculum.json')
SRC=os.path.join(DAT,'sources.json')
errors=[]

def err(msg):
    errors.append(msg)

def word_count(s):
    return len(re.findall(r"\S+", s))

def main():
    if not os.path.isfile(CUR): err("curriculum.json missing"); print(errs()); return 1
    raw=open(CUR,encoding='utf-8').read()
    try: cur=json.loads(raw)
    except Exception as e: err(f"curriculum.json not valid JSON: {e}"); print(); return 1
    raw2=open(SRC,encoding='utf-8').read()
    try: srcs=json.loads(raw2)
    except Exception as e: err(f"sources.json not valid JSON: {e}"); print(); return 1

    # exact top-level keys
    if set(cur.keys())!={"version","generatedAt","source","semesters","coverage"}:
        err(f"curriculum.json top-level keys: {sorted(cur.keys())}")
    if set(srcs.keys())!={"version","generatedAt","sources"}:
        err(f"sources.json top-level keys: {sorted(srcs.keys())}")
    if cur.get("version")!=1: err("curriculum version != 1")
    if srcs.get("version")!=1: err("sources version != 1")

    expected_semesters=["1-1","1-2","2-1","2-2","3-1","3-2","4-1","4-2"]
    sems=cur.get("semesters",[])
    if [s.get("id") for s in sems]!=expected_semesters:
        err(f"semester order: {[s.get('id') for s in sems]}")
    LABELS={"1-1":"I Year · I Semester","1-2":"I Year · II Semester","2-1":"II Year · I Semester",
            "2-2":"II Year · II Semester","3-1":"III Year · I Semester","3-2":"III Year · II Semester",
            "4-1":"IV Year · I Semester","4-2":"IV Year · II Semester"}
    for s in sems:
        if LABELS.get(s.get("id"))!=s.get("label"): err(f"semester {s.get('id')} label {s.get('label')!r}")
        if s.get("year") is None or s.get("term") is None: err(f"semester {s.get('id')} year/term missing")

    # sources cross-ref
    src_ids={}
    for st in srcs.get("sources",[]):
        sid=st.get("id")
        if not sid or not re.fullmatch(r"[a-z0-9-]+", sid): err(f"bad source id {sid!r}"); continue
        if sid in src_ids: err(f"duplicate source id {sid}")
        src_ids[sid]=st
        if st.get("status") not in ("downloaded","parsed","inaccessible","needs_ocr","skipped"):
            err(f"source {sid} bad status {st.get('status')!r}")
        if st.get("subjectId") and sems and st.get("semester") not in expected_semesters:
            err(f"source {sid} bad semester {st.get('semester')}")

    subj_ids=set()
    counts={"subjects":0,"definitions":0,"complete":0,"partial":0,"stub":0}
    per_sem={}
    for sem in sems:
        sid_list=[]
        for sub in sem.get("subjects",[]):
            need={"id","name","shortName","code","courseType","folderId","folderUrl","data","definitionCount","unitCount","coveredUnits","status","sourceCount"}
            if need-set(sub.keys()): err(f"subject {sub.get('id')}: missing key(s) {sorted(need-set(sub.keys()))}")
            if set(sub.keys())-need: err(f"subject {sub.get('id')}: extra keys {sorted(set(sub.keys())-need)}")
            sid=sub["id"]
            sid_list.append(sid)
            if sid in subj_ids: err(f"duplicate subject id {sid}")
            subj_ids.add(sid)
            counts["subjects"]+=1
            status=sub["status"]
            has_data=sub["data"] is not None
            if status not in ("complete","partial","inaccessible","no_materials","unresolved"):
                err(f"subject {sid}: bad status {status!r}")
            if not has_data and status not in ("inaccessible","no_materials","unresolved"):
                err(f"subject {sid}: data is null for status {status}")
            if has_data and status=="complete" and sub["definitionCount"]<20:
                err(f"subject {sid}: complete with <20 defs")
            if has_data and sub["definitionCount"]==0 and status not in ("unresolved",):
                err(f"subject {sid}: data file but 0 defs")
            if not has_data and sub["definitionCount"]!=0:
                err(f"subject {sid}: stub with {sub['definitionCount']} defs")
            path=os.path.join(REPO, sub["data"]) if sub["data"] else None
            if sub["data"]:
                if not os.path.isfile(path): err(f"subject {sid}: data path missing {sub['data']}")
                else:
                    d=json.load(open(path,encoding='utf-8'))
                    if d.get("id")!=sid: err(f"subject file id mismatch {sid} vs {d.get('id')}")
                    if d.get("status") not in ("complete","partial","unresolved","inaccessible") and len(d.get("definitions",[]))==0:
                        pass
                    check_defs(sid, d, src_ids)
                    counts["definitions"]+=len(d["definitions"])
                    if len(d["definitions"])!=sub["definitionCount"]:
                        err(f"subject {sid}: definitionCount {sub['definitionCount']} != {len(d['definitions'])}")
            if status in ("complete","partial"): counts[status]+=1
            else: counts["stub"]+=1
        if sem["id"]=="4-2":
            if sem.get("status")!="no_materials": err("semester 4-2 must be no_materials")
            if sem.get("subjects"): err("semester 4-2 must have no subjects")
        else:
            if sid_list and len(set(sid_list))!=len(sid_list): err(f"semester {sem['id']}: duplicate subject entries")
        per_sem[sem["id"]]=sem.get("status")

    cov=cur.get("coverage",{})
    if cov.get("subjects")!=counts["subjects"]: err(f"coverage.subjects {cov.get('subjects')} != {counts['subjects']}")
    if cov.get("definitions")!=counts["definitions"]: err(f"coverage.definitions {cov.get('definitions')} != {counts['definitions']}")
    if cov.get("completeSubjects")!=counts["complete"]: err(f"coverage.completeSubjects mismatch")
    if cov.get("partialSubjects")!=counts["partial"]: err(f"coverage.partialSubjects mismatch")
    if cov.get("semesters")!=len(sems): err("coverage.semesters mismatch")

    print(f"semesters={len(sems)} subjects={counts['subjects']} definitions={counts['definitions']} complete={counts['complete']} partial={counts['partial']} stubs={counts['stub']}")
    if errors:
        print(f"VALIDATION FAILED: {len(errors)} problem(s)")
        for e in errors: print(" -", e)
        return 1
    print("VALIDATION OK")
    return 0

def check_defs(sid, d, src_ids):
    seen_ids=set(); seen_terms=set(); seen_td=set()
    subject_sources=set()
    for st in src_ids.values():
        if st.get("subjectId")==sid and st.get("status") in ("downloaded","parsed"):
            subject_sources.add(st["id"])
    for i,defn in enumerate(d.get("definitions",[])):
        keys={"id","term","definition","formula","unit","unitTitle","sources"}
        if keys-set(defn.keys()): err(f"{sid} def#{i}: missing {sorted(keys-set(defn.keys()))}")
        if set(defn.keys())-keys: err(f"{sid} def#{i}: extra keys {sorted(set(defn.keys())-keys)}")
        term=defn.get("term","")
        text=defn.get("definition","")
        if len(term)>48: err(f"{sid} def#{i}: term too long ({len(term)})")
        if term.rstrip() and term!=term.rstrip(): err(f"{sid} def#{i}: trailing space in term")
        wc=word_count(text)
        if not (8<=wc<=28): err(f"{sid} def#{i} '{term}': word count {wc}")
        if text.endswith(" ") or text!=text.strip(): err(f"{sid} def#{i}: definition not stripped")
        f=defn.get("formula","")
        if len(f)>48: err(f"{sid} def#{i} '{term}': formula too long")
        u=defn.get("unit")
        if u is not None and (not isinstance(u,int) or not(1<=u<=6)): err(f"{sid} def#{i} '{term}': bad unit {u!r}")
        ut=defn.get("unitTitle")
        if ut is not None and not (isinstance(ut,str) and ut.strip()): err(f"{sid} def#{i} '{term}': bad unitTitle")
        if not isinstance(defn.get("sources"),list) or not defn.get("sources"):
            err(f"{sid} def#{i} '{term}': no sources"); continue
        for loc in defn["sources"]:
            if "#" not in loc: err(f"{sid} def#{i}: bad locator {loc!r}"); continue
            srcid, locpart = loc.split("#",1)
            if srcid not in src_ids:
                err(f"{sid} def#{i} '{term}': unknown source {srcid}"); continue
            st=src_ids[srcid]
            if st.get("status") in ("inaccessible",):
                err(f"{sid} def#{i} '{term}': cites inaccessible source {srcid}")
            if st.get("subjectId")!=sid:
                err(f"{sid} def#{i} '{term}': source {srcid} belongs to {st.get('subjectId')}")
            mm=re.fullmatch(r"p\.\d+", locpart) or re.fullmatch(r"slide\.\d+", locpart) or re.fullmatch(r"para\.\d+", locpart)
            if not mm: err(f"{sid} def#{i} '{term}': locator {locpart!r} not p.N / slide.N / para.N")
        if defn["id"] in seen_ids: err(f"{sid}: dup definition id {defn['id']}")
        if term.lower() in seen_terms: err(f"{sid}: dup term '{term}'")
        td=(term.lower(), text.lower())
        if td in seen_td: err(f"{sid}: dup (term, definition) '{term}'")
        seen_ids.add(defn["id"]); seen_terms.add(term.lower()); seen_td.add(td)

if __name__=="__main__":
    sys.exit(main())
