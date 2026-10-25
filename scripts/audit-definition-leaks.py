#!/usr/bin/env python3
"""Find definitions that break the "definition -> term" quiz.

Flags, per subject in data/subjects/*/*.json:
  SELF     the definition contains its own term ("A stack is ...")
  ACRONYM  the definition spells out an acronym term ("Domain Name System" for DNS)
  TWIN     two definitions read the same once their terms are blanked out
  ECHO     (warning only) every word of the term shows up in the definition,
           possibly in another form ("Magnetization" -> "magnetized")

Usage:
  python3 scripts/audit-definition-leaks.py              # all subjects
  python3 scripts/audit-definition-leaks.py data-structures cyber-security
  python3 scripts/audit-definition-leaks.py --no-echo    # hide warnings

Exit code is 1 while any SELF, ACRONYM or TWIN finding remains.
"""
import glob, json, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILLER = {"of", "and", "for", "the", "a", "an", "in", "to", "on", "by", "with", "&"}
STOP = set("a an the of in to and or for by with on at as is are be its it from that which "
           "this between per into than when where each one two their used using".split())


def variants(term):
    out = set()
    def add(v):
        v = re.sub(r"^(the|a|an)\s+", "", v.strip(), flags=re.I)
        if len(re.sub(r"\W", "", v)) >= 2:
            out.add(v)
    base = re.sub(r"\s*\([^)]*\)\s*", " ", term).strip()
    add(term); add(base); add(re.sub(r"'s\b", "", base))
    for p in re.findall(r"\(([^)]*)\)", term):
        add(p)
    return sorted(out, key=len, reverse=True)


def acronym_hit(term, definition):
    for ac in set(re.findall(r"\b[A-Z][A-Z0-9]{1,6}\b", term)):
        words = re.findall(r"[\w][\w'’-]*|&", definition)
        for i in range(len(words)):
            k = j = 0
            j = i
            while j < len(words) and k < len(ac):
                w = words[j]
                if w[0] == ac[k]:
                    k += 1; j += 1
                elif k > 0 and w.lower() in FILLER:
                    j += 1
                else:
                    break
            if k == len(ac) and j - i >= 2:
                return " ".join(words[i:j])
    return None


def mask(term, definition):
    text = definition
    hit = acronym_hit(term, text)
    if hit:
        text = text.replace(hit, "___", 1)
    for v in variants(term):
        pat = r"[\s-]+".join(map(re.escape, re.split(r"[\s-]+", v)))
        text = re.sub(rf"(?<!\w){pat}(?:'s|’s|es|s)?(?!\w)", "___", text, flags=re.I)
    return text


def stem(w):
    return re.sub(r"(ization|isation|ation|ance|ence|ity|ing|ion|ies|es|s)$", "", w)


def twin_key(text):
    words = re.findall(r"[\w]+", text.lower())
    return " ".join(w for w in words if w not in ("a", "an", "the"))


def tokens(text):
    return {stem(w) for w in re.findall(r"\w+", text.lower()) if len(w) > 2 and w not in STOP}


def main(argv):
    show_echo = "--no-echo" not in argv
    wanted = {a for a in argv if not a.startswith("--")}
    files = sorted(glob.glob(os.path.join(REPO, "data", "subjects", "*", "*.json")))
    hard = warn = 0
    for path in files:
        data = json.load(open(path, encoding="utf-8"))
        sid = data.get("id", os.path.basename(path)[:-5])
        if wanted and sid not in wanted:
            continue
        defs = data.get("definitions", [])
        lines = []
        masked = {}
        for d in defs:
            t, df = d["term"], d["definition"]
            m = mask(t, df)
            masked[d["id"]] = m
            ac = acronym_hit(t, df)
            if ac:
                lines.append(f"  ACRONYM {d['id']}: spells out \"{ac}\"\n           {df}")
            elif m != df:
                lines.append(f"  SELF    {d['id']}: names its own term\n           {df}")
            elif show_echo:
                tw = {stem(w) for w in re.findall(r"\w+", re.sub(r"\([^)]*\)", "", t).lower())
                      if len(w) > 2 and w not in STOP}
                if tw and tw <= tokens(df):
                    lines.append(f"  echo    {d['id']}: term words reappear\n           {df}")
                    warn += 1
        for i, a in enumerate(defs):
            ka = twin_key(masked[a["id"]])
            for b in defs[i + 1:]:
                if ka and ka == twin_key(masked[b["id"]]):
                    lines.append(f"  TWIN    {a['id']} <-> {b['id']}: same definition once terms are blanked\n"
                                 f"           {a['definition']}\n           {b['definition']}")
        hard += sum(1 for l in lines if not l.startswith("  echo"))
        if lines:
            rel = os.path.relpath(path, REPO)
            print(f"\n{rel}  ({len(defs)} definitions)")
            print("\n".join(lines))
    print(f"\n{hard} blocking finding(s), {warn} warning(s).")
    return 1 if hard else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
