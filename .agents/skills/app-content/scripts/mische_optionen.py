# Mischt die Reihenfolge der Antwortoptionen von `single-choice` und `multiple-choice` in allen Seiten, deterministisch je Übungs-Id,
# damit die richtige Option nicht immer zuerst steht (die Vorlage mischt die Optionen nicht selbst).
# Aufruf im Ordner der App: python3 .agents/skills/app-content/scripts/mische_optionen.py [--dry]
# Danach: npx vp check --fix && npx vp build. Erneut aufrufen mischt nicht noch einmal anders: Seiten, deren richtige Option schon
# nicht an erster Stelle steht, bleiben unverändert (Option `--force` mischt trotzdem).
import glob, hashlib, re, sys

DRY = "--dry" in sys.argv
FORCE = "--force" in sys.argv

def perm(n, key, correct_idx):
    """A fixed permutation of range(n) from the key; the first place is never a right option."""
    order = sorted(range(n), key=lambda i: hashlib.sha256(f"{key}:{i}".encode()).hexdigest())
    for shift in range(n):
        o = order[shift:] + order[:shift]
        if o[0] not in correct_idx:
            return o
    return order

changed = 0
for f in sorted(glob.glob("src/*/*.yaml")):
    if f.endswith("chapter.yaml"):
        continue
    lines = open(f, encoding="utf-8").read().split("\n")
    out, i, n = [], 0, len(lines)
    cur_id = None
    while i < n:
        line = lines[i]
        m = re.match(r"^(\s*)(?:- )?id:\s*(\S+)\s*$", line)
        if m:
            cur_id = m.group(2)
        m = re.match(r"^(\s*)options:\s*$", line)
        if not m:
            out.append(line); i += 1; continue
        ind = len(m.group(1))
        out.append(line); i += 1
        entries, cur = [], None
        while i < n:
            l = lines[i]
            em = re.match(r"^(\s*)- text:", l)
            if em and len(em.group(1)) == ind + 2:
                cur = [l]; entries.append(cur); i += 1; continue
            if cur is not None and (l.strip() == "" or len(l) - len(l.lstrip()) > ind + 2):
                cur.append(l); i += 1; continue
            break
        if len(entries) < 2:
            out.extend(l for e in entries for l in e); continue
        correct = {k for k, e in enumerate(entries) if any(re.match(r"^\s*correct:\s*true\s*$", l) for l in e)}
        if not FORCE and 0 not in correct:
            out.extend(l for e in entries for l in e); continue
        order = perm(len(entries), f"{f}:{cur_id}", correct)
        for k in order:
            out.extend(entries[k])
        changed += 1
    if not DRY:
        open(f, "w", encoding="utf-8").write("\n".join(out))
print("gemischt:", changed, "Aufgaben", "(Trockenlauf)" if DRY else "")
