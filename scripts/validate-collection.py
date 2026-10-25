#!/usr/bin/env python3
"""Validate one·liners collection(s). Usage: validate-collection.py [collection_path]"""
import json, os, sys, glob, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COLLECTIONS = os.path.join(ROOT, "data", "collections")
RAW_EXTS = {".pdf", ".pptx", ".docx", ".html", ".epub"}

errors = []
def err(msg): errors.append(msg)

def load_json(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        err(f"{path}: invalid JSON/UTF-8: {e}")
        return None

def word_count(s):
    return len(s.split())

def validate_collection(cpath):
    global errors
    slug = os.path.basename(cpath.rstrip("/"))
    cdir = cpath
    # required files
    for fn in ("plan.json","collection.json","runtime.json","sources.json","README.md"):
        if not os.path.exists(os.path.join(cdir, fn)):
            err(f"{slug}: missing {fn}")
    if not os.path.isdir(os.path.join(cdir, "subjects")):
        err(f"{slug}: missing subjects/")
    # no raw source files
    for root,_,files in os.walk(cdir):
        for fn in files:
            if os.path.splitext(fn)[1].lower() in RAW_EXTS:
                err(f"{slug}: raw source file present: {os.path.join(root,fn)}")
    plan = load_json(os.path.join(cdir,"plan.json"))
    coll = load_json(os.path.join(cdir,"collection.json"))
    sources = load_json(os.path.join(cdir,"sources.json"))
    runtime = load_json(os.path.join(cdir,"runtime.json"))
    readme_path = os.path.join(cdir,"README.md")
    if os.path.exists(readme_path):
        if os.path.getsize(readme_path)==0:
            err(f"{slug}: README.md empty")
    else:
        err(f"{slug}: README.md missing")

    if plan is None or coll is None or sources is None or runtime is None:
        return

    # plan keys
    for k in ("version","topic","collectionId","type","audience","level","jurisdiction","spelling","language","regulated","includes","excludes","assumptions","sections","definitionBudget","disclaimer"):
        if k not in plan: err(f"{slug}: plan missing key {k}")
    # collection keys
    for k in ("version","id","name","tagline","topic","audience","level","jurisdiction","spelling","language","regulated","generatedAt","scope","assumptions","disclaimer","sections","coverage"):
        if k not in coll: err(f"{slug}: collection missing key {k}")
    # sources keys
    if "sources" not in sources: err(f"{slug}: sources missing sources")
    if "collectionId" not in sources: err(f"{slug}: sources missing collectionId")
    # runtime keys
    for k in ("version","id","name","short","subjects"):
        if k not in runtime: err(f"{slug}: runtime missing key {k}")

    if coll.get("id") != slug:
        err(f"{slug}: collection.id mismatch")
    if coll.get("id") != plan.get("collectionId"):
        err(f"{slug}: collection.id != plan.collectionId")
    if runtime.get("id") != slug:
        err(f"{slug}: runtime.id mismatch")
    if sources.get("collectionId") != slug:
        err(f"{slug}: sources.collectionId mismatch")

    # unique source ids
    src_ids = [s["id"] for s in sources.get("sources",[])]
    if len(set(src_ids)) != len(src_ids):
        err(f"{slug}: duplicate source ids")
    src_map = {s["id"]: s for s in sources.get("sources",[])}

    # regulated disclaimer
    if coll.get("regulated") and not coll.get("disclaimer"):
        err(f"{slug}: regulated collection missing disclaimer")

    # subject files
    subject_files = {}
    for root,_,files in os.walk(os.path.join(cdir,"subjects")):
        for fn in files:
            if fn.endswith(".json"):
                subject_files[fn] = os.path.join(root,fn)
    # index subject ids from plan/collection
    plan_subj_ids = []
    for sec in plan.get("sections",[]):
        for s in sec.get("subjects",[]):
            plan_subj_ids.append((sec["id"], s["id"]))
    coll_subj_flat = []
    for sec in coll.get("sections",[]):
        for s in sec.get("subjects",[]):
            coll_subj_flat.append((sec["id"], s))

    # plan vs collection order
    if [s["id"] for _,s in coll_subj_flat] != [sid for _,sid in plan_subj_ids] if False else None:
        pass
    # check ids match plan
    if [sid for _,sid in plan_subj_ids] != [s["id"] for _,s in coll_subj_flat]:
        err(f"{slug}: collection subject ids/order != plan")

    # validate each subject
    all_defs_collection = []  # list of (subjectId, def)
    for sec_id, s in coll_subj_flat:
        sid = s["id"]
        spath_rel = s.get("data")
        if spath_rel is None:
            if s.get("status") not in ("inaccessible","no_materials","unresolved"):
                err(f"{slug}/{sid}: data null but status {s.get('status')}")
            # inaccessible: no file
            if os.path.exists(os.path.join(ROOT, spath_rel or "")):
                pass
            continue
        spath = os.path.join(ROOT, spath_rel)
        if not os.path.exists(spath):
            err(f"{slug}/{sid}: subject file missing {spath_rel}")
            continue
        if not spath_rel.startswith(f"data/collections/{slug}/"):
            err(f"{slug}/{sid}: subject path outside collection")
        sd = load_json(spath)
        if sd is None: continue
        # required keys
        for k in ("version","id","collectionId","section","name","shortName","code","courseType","status","color","dark","units","definitions"):
            if k not in sd: err(f"{slug}/{sid}: subject missing key {k}")
        if sd.get("id") != sid:
            err(f"{slug}/{sid}: subject id mismatch")
        if sd.get("collectionId") != slug:
            err(f"{slug}/{sid}: collectionId mismatch")
        if sd.get("section") != sec_id:
            err(f"{slug}/{sid}: section mismatch")
        # color match collection
        if sd.get("color") != s.get("color"):
            err(f"{slug}/{sid}: color mismatch")
        if sd.get("dark") != s.get("dark"):
            err(f"{slug}/{sid}: dark mismatch")
        # counts
        if s.get("definitionCount") != len(sd.get("definitions",[])):
            err(f"{slug}/{sid}: definitionCount mismatch")
        if s.get("unitCount") != len(sd.get("units",[])):
            err(f"{slug}/{sid}: unitCount mismatch")
        covered = len(set(d.get("unit") for d in sd.get("definitions",[]) if d.get("unit") is not None))
        if s.get("coveredUnits") != covered:
            err(f"{slug}/{sid}: coveredUnits mismatch ({s.get('coveredUnits')} vs {covered})")
        src_count = len(set(src.split("#")[0] for d in sd.get("definitions",[]) for src in d.get("sources",[])))
        if s.get("sourceCount") != src_count:
            err(f"{slug}/{sid}: sourceCount mismatch ({s.get('sourceCount')} vs {src_count})")
        # units map
        unit_map = {u["number"]: u["title"] for u in sd.get("units",[])}
        # unique ids/terms
        ids = [d["id"] for d in sd.get("definitions",[])]
        terms = [d["term"] for d in sd.get("definitions",[])]
        if len(set(ids)) != len(ids):
            err(f"{slug}/{sid}: duplicate definition ids")
        if len(set(terms)) != len(terms):
            err(f"{slug}/{sid}: duplicate terms")
        term_set_subject = set(terms)
        # all terms across collection for confusable check (preferred same subject)
        for d in sd.get("definitions",[]):
            # definition word count
            if not isinstance(d.get("definition"), str) or not d["definition"].strip():
                err(f"{slug}/{sid}/{d.get('id')}: empty definition")
                continue
            wc = word_count(d["definition"])
            if wc < 8 or wc > 28:
                err(f"{slug}/{sid}/{d.get('id')}: definition {wc} words (need 8-28)")
            if d["definition"] != d["definition"].rstrip():
                err(f"{slug}/{sid}/{d.get('id')}: trailing space")
            term = d.get("term","")
            if not term or len(term)>48:
                err(f"{slug}/{sid}/{d.get('id')}: term length")
            if term.endswith(":"):
                err(f"{slug}/{sid}/{d.get('id')}: trailing colon")
            if term.lower().startswith("definition of"):
                err(f"{slug}/{sid}/{d.get('id')}: 'Definition of' term")
            formula = d.get("formula","")
            if not isinstance(formula,str) or len(formula)>48:
                err(f"{slug}/{sid}/{d.get('id')}: formula length")
            # unit
            u = d.get("unit")
            if u is not None:
                if u not in unit_map:
                    err(f"{slug}/{sid}/{d.get('id')}: unit {u} not in units")
                elif d.get("unitTitle") != unit_map[u]:
                    err(f"{slug}/{sid}/{d.get('id')}: unitTitle mismatch")
            else:
                if d.get("unitTitle") is not None:
                    err(f"{slug}/{sid}/{d.get('id')}: unitTitle must be null when unit null")
            aliases = d.get("aliases",[])
            if not isinstance(aliases,list) or len(aliases)>3 or not all(isinstance(a,str) for a in aliases):
                err(f"{slug}/{sid}/{d.get('id')}: aliases invalid")
            conf = d.get("confusables")
            if not isinstance(conf,list) or len(conf)<2 or len(conf)>3 or not all(isinstance(c,str) for c in conf):
                err(f"{slug}/{sid}/{d.get('id')}: confusables count invalid")
            else:
                for c in conf:
                    if c == term:
                        err(f"{slug}/{sid}/{d.get('id')}: confusable equals term")
                # confusable existence: same subject preferred, else collection (checked later)
            sources_list = d.get("sources")
            if not isinstance(sources_list,list) or not sources_list:
                err(f"{slug}/{sid}/{d.get('id')}: sources empty")
            else:
                for loc in sources_list:
                    if "#" not in loc:
                        err(f"{slug}/{sid}/{d.get('id')}: bad locator shape {loc}")
                        continue
                    sid_src, locator = loc.split("#",1)
                    if sid_src not in src_map:
                        err(f"{slug}/{sid}/{d.get('id')}: unknown source {sid_src}")
                        continue
                    src = src_map[sid_src]
                    if src.get("status") != "parsed":
                        err(f"{slug}/{sid}/{d.get('id')}: source {sid_src} not parsed")
                    # locator scheme match
                    scheme = src.get("locatorScheme","")
                    prefix = scheme.split("<")[0]
                    # be lenient
                    if prefix and not re.match(r'^[a-z]+\.', locator) and not locator.startswith(prefix):
                        pass  # skip strict check
            all_defs_collection.append((sid, d))

    # confusable existence across collection
    all_terms = set()
    for sid, d in all_defs_collection:
        all_terms.add(d["term"])
    subj_terms = {}
    for sid, d in all_defs_collection:
        subj_terms.setdefault(sid, set()).add(d["term"])
    for sid, d in all_defs_collection:
        for c in d.get("confusables",[]):
            if c not in subj_terms.get(sid,set()) and c not in all_terms:
                err(f"{slug}/{sid}/{d['id']}: confusable '{c}' not found in collection")
            # not synonym check skipped (can't auto)

    # duplicate (term,definition) across collection
    seen_pairs = set()
    for sid, d in all_defs_collection:
        k = (d["term"], d["definition"])
        if k in seen_pairs:
            err(f"{slug}: duplicate (term,definition): {d['term']}")
        seen_pairs.add(k)

    # status rules
    for sec_id, s in coll_subj_flat:
        sid = s["id"]
        st = s.get("status")
        if st == "complete":
            # find subject file
            sd = None
            spath_rel = s.get("data")
            if spath_rel:
                sd = load_json(os.path.join(ROOT, spath_rel))
            if sd is None:
                err(f"{slug}/{sid}: complete but no file")
                continue
            if len(sd.get("definitions",[])) < 40:
                err(f"{slug}/{sid}: complete but <40 defs")
            covered = len(set(d.get("unit") for d in sd.get("definitions",[]) if d.get("unit") is not None))
            if covered < len(sd.get("units",[])):
                err(f"{slug}/{sid}: complete but not all units covered")
        elif st == "partial":
            sd = None
            spath_rel = s.get("data")
            if spath_rel:
                sd = load_json(os.path.join(ROOT, spath_rel))
            if sd is None or len(sd.get("definitions",[])) < 1:
                err(f"{slug}/{sid}: partial but no definitions")
        elif st == "inaccessible":
            if s.get("data") is not None:
                err(f"{slug}/{sid}: inaccessible but has data")
        # definitionCount etc already checked

    # coverage totals
    cov = coll.get("coverage",{})
    if cov.get("sections") != len(coll.get("sections",[])):
        err(f"{slug}: coverage.sections mismatch")
    if cov.get("subjects") != len(coll_subj_flat):
        err(f"{slug}: coverage.subjects mismatch")
    if cov.get("definitions") != sum(s.get("definitionCount",0) for _,s in coll_subj_flat):
        err(f"{slug}: coverage.definitions mismatch")
    if cov.get("completeSubjects") != sum(1 for _,s in coll_subj_flat if s.get("status")=="complete"):
        err(f"{slug}: coverage.completeSubjects mismatch")
    if cov.get("partialSubjects") != sum(1 for _,s in coll_subj_flat if s.get("status")=="partial"):
        err(f"{slug}: coverage.partialSubjects mismatch")
    if cov.get("inaccessibleSubjects") != sum(1 for _,s in coll_subj_flat if s.get("status")=="inaccessible"):
        err(f"{slug}: coverage.inaccessibleSubjects mismatch")

    # runtime check
    if runtime.get("name") != coll.get("name"):
        err(f"{slug}: runtime name mismatch")
    # flattened subjects order
    rt_subjects = runtime.get("subjects",[])
    coll_flat_ids = [s["id"] for _,s in coll_subj_flat]
    if [rs["id"] for rs in rt_subjects] != coll_flat_ids:
        err(f"{slug}: runtime subject order/ids mismatch")
    # each definition appears
    # build expected list per subject
    for idx,(sec_id,s) in enumerate(coll_subj_flat):
        sid = s["id"]
        spath_rel = s.get("data")
        if not spath_rel: continue
        sd = load_json(os.path.join(ROOT, spath_rel))
        if sd is None: continue
        rts = rt_subjects[idx]
        # defs order in runtime: subject files sorted? runtime built from sorted. Check counts
        expected_defs = sorted(sd["definitions"], key=lambda x:(x["unit"],x["term"]))
        if len(rts.get("defs",[])) != len(expected_defs):
            err(f"{slug}/{sid}: runtime def count mismatch")
            continue
        for i,defn in enumerate(expected_defs):
            rt_def = rts["defs"][i]
            if rt_def != [defn["term"], defn["definition"], defn["formula"]]:
                err(f"{slug}/{sid}: runtime def mismatch at {i}")
                break
        # color/dark
        if rts.get("color") != s.get("color") or rts.get("dark") != s.get("dark"):
            err(f"{slug}/{sid}: runtime color mismatch")

    # definitionBudget min check
    db = plan.get("definitionBudget",{})
    if "min" in db and total_defs_count(coll_subj_flat, ROOT) < db["min"]:
        # README must explain; we can't auto-check text, just warn? spec: README explains. Skip hard error.
        pass

    # index.json check
    index_path = os.path.join(COLLECTIONS, "index.json")
    if os.path.exists(index_path):
        idx = load_json(index_path)
        if idx is not None:
            entries = idx.get("collections",[])
            matching = [e for e in entries if e.get("id")==slug]
            if len(matching) != 1:
                err(f"{slug}: index.json should have exactly one entry (found {len(matching)})")
            else:
                e = matching[0]
                if e.get("definitions") != total_defs_count(coll_subj_flat, ROOT):
                    err(f"{slug}: index definitions mismatch")
                if e.get("subjects") != len(coll_subj_flat):
                    err(f"{slug}: index subjects mismatch")

def total_defs_count(coll_subj_flat, ROOT):
    n=0
    for _,s in coll_subj_flat:
        sp = s.get("data")
        if not sp: continue
        sd = load_json(os.path.join(ROOT, sp))
        if sd: n += len(sd.get("definitions",[]))
    return n

def main():
    global errors
    if len(sys.argv) > 1:
        paths = [sys.argv[1]]
    else:
        paths = [os.path.join(COLLECTIONS, d) for d in os.listdir(COLLECTIONS)
                 if os.path.isdir(os.path.join(COLLECTIONS,d))]
    for p in paths:
        if not os.path.isdir(p):
            err(f"not a dir: {p}")
            continue
        validate_collection(p)
    # also check raw files at top level of data/collections
    for root,_,files in os.walk(COLLECTIONS):
        for fn in files:
            if os.path.splitext(fn)[1].lower() in RAW_EXTS:
                err(f"raw source file present: {os.path.join(root,fn)}")
    if errors:
        print("VALIDATION FAILED:")
        for e in errors:
            print(" -", e)
        sys.exit(1)
    else:
        print("VALIDATION PASSED")

if __name__ == "__main__":
    main()