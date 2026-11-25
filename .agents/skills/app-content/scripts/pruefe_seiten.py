# Checks all pages: (1) no Hörsatz appears (nearly) word for word elsewhere on its page, (2) words not in the Grundwortschatz
# (gw.json: word -> level, made from https://lernapps.net/apps/map/englisch/grundwortschatz/), (3) mistakes per item.
# Run from the app folder: python3 .agents/skills/app-content/scripts/pruefe_seiten.py [gw.json]
import re, sys, json, glob, yaml
GW = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else {}
def norm(t): return re.findall(r"[a-z']+", t.lower().replace("’", "'"))
def strings(o, skip=()):
    if isinstance(o, dict):
        for k, v in o.items():
            if k in skip: continue
            yield from strings(v, skip)
    elif isinstance(o, list):
        for v in o: yield from strings(v, skip)
    elif isinstance(o, str): yield o
def sentences(t):
    for p in re.split(r"(?<=[.!?])\s+|\n|\|", re.sub(r"[\[\]()]", " ", t)): 
        w = norm(p)
        if len(w) >= 3: yield w
bad = 0
for f in sorted(glob.glob("src/*/*.yaml")):
    if f.endswith("chapter.yaml"): continue
    d = yaml.safe_load(open(f, encoding="utf-8"))
    if not isinstance(d, dict): continue
    if "recap" in d: continue
    hear = []
    def walk(o):
        if isinstance(o, dict):
            if o.get("type") == "speaking-task":
                for i in o["items"]: hear.append(i["text"])
            if o.get("type") == "language-task":
                for i in o.get("items", []):
                    if "audio" in i: hear.append(i.get("target") or i.get("source"))
            for v in o.values(): walk(v)
        elif isinstance(o, list):
            for v in o: walk(v)
    walk(d)
    # all other strings, without audio file names
    def others(o):
        if isinstance(o, dict):
            if o.get("type") == "speaking-task": return
            if "audio" in o: 
                return
            for k, v in o.items():
                if k in ("id", "image", "type", "source", "licence", "url"): continue
                yield from others(v)
        elif isinstance(o, list):
            for v in o: yield from others(v)
        elif isinstance(o, str): yield o
    pool = [w for s in others(d["blocks"]) for w in sentences(s)]
    pool += [norm(s) for s in others(d["blocks"]) if len(norm(s)) >= 3]
    for h in hear:
        hw = set(norm(h))
        for p in pool:
            ps = set(p)
            if hw and len(hw & ps) / len(hw | ps) >= 0.8 and len(p) <= len(hw) + 3:
                print(f"{f}: Hörsatz zu ähnlich: {h!r} ~ {' '.join(p)!r}"); bad += 1; break
    if GW:
        txt = " ".join(s for s in strings(d["blocks"], skip=("id", "image", "source", "licence", "url", "audio", "type", "alt")))
        eng = set()
        for m in re.finditer(r"[A-Za-z']+", txt): eng.add(m.group(0).lower())
        unk = sorted(w for w in eng if w not in GW and w.rstrip("s") not in GW and w.rstrip("es") not in GW and len(w) > 2 and re.fullmatch(r"[a-z']+", w))
        print(f"{f}: nicht in der Liste (englische und deutsche Wörter gemischt, nur ansehen): {len(unk)}")
print("fertig, Funde:", bad)
