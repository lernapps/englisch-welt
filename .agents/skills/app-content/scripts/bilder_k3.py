# Bilder von Kapitel 3 (Wie die USA entstanden): Schemakarten mit Schiffen und Wagenzügen, Zeitachsen, Schema der drei Gewalten.
# Alle Karten sind Schemakarten, nicht genau nach Maßstab. Aufruf über make_images.py (lädt diese Datei).

def register(m):
    BG, LAND, SEA, INK = m.BG, m.LAND, m.SEA, m.INK
    BLUE, ORANGE, GREEN = m.BLUE, m.ORANGE, m.GREEN

    def line(x1, y1, x2, y2, color=INK, sw=3, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        return f'  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}" stroke-linecap="round"{d}/>\n'

    def path(d, color=INK, sw=3, dash=None, fill="none"):
        da = f' stroke-dasharray="{dash}"' if dash else ""
        return f'  <path d="{d}" fill="{fill}" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"{da}/>\n'

    def circle(x, y, r, fill=BG, stroke=INK, sw=2):
        return f'  <circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>\n'

    def ship(x, y, s=1.0, color="#8a5a2b"):
        """Segelschiff (Schema), Mitte unten bei (x, y)."""
        b = m.poly([(x - 26 * s, y - 12 * s), (x + 26 * s, y - 12 * s), (x + 16 * s, y), (x - 16 * s, y)], fill=color)
        b += line(x, y - 12 * s, x, y - 44 * s, INK, 2)
        b += m.poly([(x + 2 * s, y - 42 * s), (x + 2 * s, y - 16 * s), (x + 22 * s, y - 16 * s)], fill="#fffaf0", sw=2)
        b += m.poly([(x - 2 * s, y - 38 * s), (x - 2 * s, y - 16 * s), (x - 18 * s, y - 16 * s)], fill="#fffaf0", sw=2)
        return b

    def wagon(x, y, s=1.0):
        """Planwagen (Schema), Mitte unten bei (x, y)."""
        b = path(f"M{x - 18 * s},{y - 10 * s} Q{x},{y - 34 * s} {x + 18 * s},{y - 10 * s}", INK, 2, None, "#fffaf0")
        b += m.rect(x - 18 * s, y - 12 * s, 36 * s, 8 * s, "#8a5a2b", INK, 2, 2)
        b += circle(x - 10 * s, y - 2 * s, 5 * s, "#fffaf0")
        b += circle(x + 10 * s, y - 2 * s, 5 * s, "#fffaf0")
        return b

    def train(x, y, s=1.0):
        """Eisenbahn (Schema), Mitte unten bei (x, y)."""
        b = m.rect(x - 24 * s, y - 20 * s, 34 * s, 14 * s, "#6b6b6b", INK, 2, 2)
        b += m.rect(x + 12 * s, y - 28 * s, 14 * s, 22 * s, "#4a4a4a", INK, 2, 2)
        b += circle(x - 14 * s, y - 2 * s, 5 * s, "#fffaf0")
        b += circle(x + 2 * s, y - 2 * s, 5 * s, "#fffaf0")
        b += circle(x + 19 * s, y - 2 * s, 5 * s, "#fffaf0")
        return b

    # ---------- Atlantik-Karte: Europa rechts, Nordamerika links ----------
    def atlantik(named=True):
        b = f'  <rect x="0" y="0" width="480" height="300" fill="{SEA}"/>\n'
        b += m.poly([(0, 0), (150, 0), (170, 40), (140, 86), (156, 130), (120, 170), (130, 220), (70, 300), (0, 300)], fill=LAND)   # Nordamerika
        b += m.poly([(480, 0), (372, 0), (356, 50), (380, 92), (350, 130), (372, 170), (360, 230), (400, 300), (480, 300)], fill="#ebe2c5")  # Europa
        return b

    @m.image
    def mayflower_karte():
        """Section `neu`: route of the Mayflower (schematic), names of places."""
        b = atlantik()
        b += path("M366,150 C300,130 240,150 150,112", ORANGE, 4, "10 8")
        b += ship(290, 154, 1.0)
        b += m.text(420, 170, "England", 16, "middle", INK, "bold")
        b += line(366, 150, 410, 82, ORANGE, 4, "10 8")
        b += circle(410, 82, 6, ORANGE)
        b += m.text(430, 62, "Leiden", 16, "middle", INK, "bold")
        b += circle(366, 150, 6, ORANGE)
        b += circle(150, 112, 6, ORANGE)
        b += m.text(96, 100, "Cape Cod", 16, "middle", INK, "bold")
        b += m.text(70, 200, "New England", 16, "middle", INK)
        return m.svg(480, 300, "Schemakarte: Schiffsroute über den Atlantik", b)

    @m.image
    def mayflower_karte_aufgabe():
        """Exercise map: the same sea, no names; markers come from the page (labelled-figure)."""
        b = atlantik()
        b += path("M366,150 C300,130 240,150 150,112", ORANGE, 4, "10 8")
        b += ship(290, 154, 1.0)
        b += circle(366, 150, 6, ORANGE)
        b += circle(150, 112, 6, ORANGE)
        return m.svg(480, 300, "Schemakarte ohne Beschriftung: Meer, zwei Küsten, Schiffsroute", b)

    # ---------- Einwanderung: Schiffe nach New York ----------
    @m.image
    def einwanderung_karte():
        b = atlantik()
        b += path("M372,100 C300,90 230,120 170,140", ORANGE, 4, "10 8")
        b += path("M372,180 C300,190 240,170 170,146", ORANGE, 4, "10 8")
        b += ship(282, 112, 0.9)
        b += ship(282, 198, 0.9)
        b += circle(166, 142, 7, ORANGE)
        b += m.rect(56, 160, 108, 52, "#fffaf0", INK, 2, 6)
        b += m.text(110, 182, "New York", 16, "middle", INK, "bold")
        b += m.text(110, 202, "Ellis Island", 14, "middle", INK)
        b += line(110, 160, 112, 148, INK, 2)
        b += m.text(420, 150, "Europe", 16, "middle", INK, "bold")
        b += m.text(250, 262, "Atlantic Ocean", 16, "middle", BLUE)
        return m.svg(480, 300, "Schemakarte: Schiffe von Europa nach New York", b)

    # ---------- Westen: USA mit Wagenzug, Eisenbahn, Umsiedlung ----------
    @m.image
    def westen_karte():
        b = m.usa_base()
        # Wagenzug-Weg von Missouri nach Oregon
        b += path("M286,150 C250,140 200,120 160,96 C120,80 90,76 64,80", ORANGE, 4, "10 8")
        # Eisenbahn 1869 von Omaha nach Kalifornien
        b += path("M282,120 C240,122 180,134 120,150 C90,156 60,150 44,146", INK, 4, "2 6")
        b += wagon(180, 120, 1.0)
        b += train(150, 150, 0.9)
        # Umsiedlung der Native Americans von Osten nach Westen
        b += path("M380,200 C350,196 320,190 290,196 C262,200 240,200 220,196", BLUE, 4)
        b += m.poly([(214, 190), (230, 190), (222, 206)], fill=BLUE, stroke=BLUE, sw=1)
        b += m.text(112, 52 + 4, "Oregon", 14, "middle", INK, "bold")
        b += m.text(300, 138, "Missouri", 14, "middle", INK, "bold")
        b += m.text(86, 176, "California", 14, "middle", INK, "bold")
        b += m.text(316, 184, "east of the Mississippi", 14, "middle", BLUE)
        b += m.text(246, 92, "Black Hills", 14, "middle", INK)
        b += m.insets()
        return m.svg(480, 300, "Schemakarte der USA mit Wagenweg, Eisenbahn und Umsiedlungsweg", b)

    # ---------- Zeitachsen: wachsen von Halt zu Halt (nur Jahreszahlen, keine Lösungen) ----------
    EVENTS = {
        1: [1607, 1620, 1621],
        2: [1892],
        3: [1773, 1775, 1776],
        4: [1803, 1830, 1862, 1869, 1890],
        5: [1789],
    }
    ORDER = [1, 2, 3, 4, 5]

    def axis(upto):
        """Axis 1600 to 1900; events of earlier stops grey, of this stop orange. `upto` = page number 1..5."""
        x0, x1 = 30, 450
        def X(year): return x0 + (year - 1600) * (x1 - x0) / 300
        b = line(x0, 150, x1, 150, INK, 4)
        for y in (1600, 1700, 1800, 1900):
            b += line(X(y), 140, X(y), 160, INK, 3)
            b += m.text(X(y), 188, str(y), 16, "middle", INK, "bold")
        seen = []
        for p in ORDER:
            if p > upto: break
            for y in EVENTS[p]:
                seen.append((y, p == upto))
        ups = 0
        for y, now in sorted(seen):
            fill = ORANGE if now else "#9aa5ad"
            lv = 120 - (ups % 3) * 22
            b += line(X(y), 150, X(y), lv, fill, 2)
            b += circle(X(y), lv, 8, fill, INK, 2)
            ups += 1
        return b

    for n in ORDER:
        def mk(n=n):
            def f():
                b = axis(n)
                if n == 1: b += ship(120, 262, 1.0)
                if n == 2: b += ship(380, 262, 1.0)
                if n == 3: b += ship(250, 262, 1.0)
                if n == 4: b += wagon(250, 258, 1.2) + train(330, 258, 1.1)
                if n == 5: b += m.rect(210, 224, 60, 40, "#fffaf0", INK, 2, 4) + m.text(240, 250, "USA", 16, "middle", INK, "bold")
                return m.svg(480, 300, f"Zeitachse der USA von sechzehnhundert bis neunzehnhundert, Halt {n}", b)
            f.__name__ = f"zeitachse_usa_{n}"
            return f
        m.image(mk())

    # ---------- Schema der drei Gewalten ----------
    @m.image
    def politik_gewalten():
        b = ""
        b += m.rect(160, 220, 160, 50, "#fffaf0", INK, 2, 6)           # Verfassung als Sockel
        # Kongress (links): zwei Häuser
        b += m.rect(20, 70, 120, 100, LAND, INK, 2, 8)
        b += m.rect(34, 100, 44, 56, "#fffaf0", INK, 2, 3)
        b += m.rect(84, 100, 44, 56, "#fffaf0", INK, 2, 3)
        # Präsident (Mitte)
        b += m.rect(180, 40, 120, 100, "#d9ead3", INK, 2, 8)
        b += circle(240, 76, 14, "#fffaf0")
        b += m.poly([(214, 128), (240, 96), (266, 128)], fill="#fffaf0")
        # Gerichtshof (rechts): Waage
        b += m.rect(340, 70, 120, 100, "#f6d8d0", INK, 2, 8)
        b += line(400, 96, 400, 150, INK, 3)
        b += line(366, 106, 434, 106, INK, 3)
        b += m.poly([(356, 130), (378, 130), (367, 112)], fill="#fffaf0")
        b += m.poly([(422, 130), (444, 130), (433, 112)], fill="#fffaf0")
        # Pfeile (Kontrolle)
        b += line(140, 108, 180, 90, INK, 3, "6 6")
        b += line(300, 90, 340, 108, INK, 3, "6 6")
        b += line(100, 170, 190, 220, INK, 2)
        b += line(240, 140, 240, 220, INK, 2)
        b += line(400, 170, 300, 220, INK, 2)
        return m.svg(480, 300, "Schema der drei Gewalten der USA", b)
