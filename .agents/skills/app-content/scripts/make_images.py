# Draws the figures of this app into src/images/ (Schemakarten und Zeitachsen). Run from the app folder:
#   python3 .agents/skills/app-content/scripts/make_images.py [name ...]
# Kapitelweise Bilder stehen in bilder_<kapitel>.py im selben Ordner und werden hier geladen.
import os, sys, glob, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
BG = "#f4efe2"; INK = "#333"; LAND = "#e3d9bd"; SEA = "#cfe3f1"; BLUE = "#2c6fd8"; ORANGE = "#d35400"; GREEN = "#138d75"
OUT = "src/images/"

def svg(w, h, title, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img">\n  <title>{title}</title>\n'
            f'  <rect width="{w}" height="{h}" fill="{BG}"/>\n{body}\n</svg>\n')
def text(x, y, t, size=16, anchor="middle", fill=INK, weight="normal"):
    return f'  <text x="{x}" y="{y}" text-anchor="{anchor}" font-family="sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}">{t}</text>\n'
def poly(points, fill=LAND, stroke=INK, sw=2):
    pts = " ".join(f"{x},{y}" for x, y in points)
    return f'  <polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>\n'
def rect(x, y, w, h, fill, stroke=INK, sw=2, rx=6):
    return f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>\n'

IMAGES = {}
def image(f):
    IMAGES[f.__name__.replace("_", "-")] = f; return f

# ---- the lower 48 states as one schematic outline (viewBox 480 x 300), the same on every map of the USA ----
USA48 = [(30,60),(180,60),(250,60),(330,60),(350,72),(380,62),(405,48),(440,25),(452,55),(436,82),(418,112),(404,150),(406,190),
         (416,236),(398,246),(380,208),(346,214),(300,222),(256,240),(236,264),(210,246),(180,236),(140,220),(100,196),(66,166),(44,118)]
def usa_base(sea=True):
    b = ""
    if sea:
        b += '  <rect x="0" y="0" width="480" height="300" fill="#e9f1f7"/>\n'
    b += poly([(0,0),(480,0),(480,60),(330,60),(250,60),(180,60),(30,60),(0,60)], fill="#f0ece0", stroke="none", sw=0)   # Canada strip
    b += poly([(100,196),(140,220),(180,236),(210,246),(236,264),(250,300),(90,300),(90,214)], fill="#f0ece0", stroke="none", sw=0)                          # Mexico strip
    b += poly(USA48, fill=LAND)
    return b
def insets(names=True):
    b = rect(14, 236, 96, 52, "#f4efe2", INK, 2, 4)
    b += poly([(26,262),(48,248),(76,246),(98,256),(84,272),(52,278)], fill=LAND)           # Alaska (schematic)
    b += rect(122, 252, 74, 36, "#f4efe2", INK, 2, 4)
    for cx, cy in [(138,272),(150,268),(164,264),(178,262)]:
        b += f'  <circle cx="{cx}" cy="{cy}" r="4" fill="{LAND}" stroke="{INK}" stroke-width="2"/>\n'   # Hawaii (schematic)
    return b

@image
def usa_schema_natur():
    """Map in the section `neu`: natural features, no countries, oceans, Alaska, Hawaii."""
    b = usa_base() + insets()
    b += '  <path d="M268,70 C272,110 262,150 286,214" fill="none" stroke="#2c6fd8" stroke-width="5" stroke-linecap="round"/>\n'
    b += poly([(338,66),(362,60),(378,72),(358,80)], fill="#a9cfe6", sw=2)
    for x in (130,150,170):
        b += poly([(x-14,150),(x,120),(x+14,150)], fill="#9aa5ad", sw=2)
    b += text(298, 130, "Mississippi", 14, "start", BLUE)
    b += text(212, 100, "Great Plains", 14)
    b += text(150, 170, "Rocky Mountains", 14)
    b += text(350, 52, "Great Lakes", 14)
    b += text(60, 276, "", 12)
    return svg(480, 300, "Schemakarte der USA mit Gebirgen, Flüssen und Seen", b)

@image
def usa_schema_aufgabe():
    """Map for the exercise: no names; the markers come from the page (labelled-figure)."""
    b = usa_base() + insets()
    return svg(480, 300, "Schemakarte der USA ohne Beschriftung", b)

# per chapter figures
for f in sorted(glob.glob(os.path.join(HERE, "bilder_*.py"))):
    spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f); m = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = m; spec.loader.exec_module(m); m.register(sys.modules[__name__])

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    names = sys.argv[1:] or list(IMAGES)
    for n in names:
        open(OUT + n + ".svg", "w", encoding="utf-8").write(IMAGES[n]())
        print("wrote", OUT + n + ".svg")
