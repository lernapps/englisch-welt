# Bilder von Kapitel 1 (hello-america): Schemakarten, nicht genau nach Maßstab. Geladen von make_images.py.
#   python3 .agents/skills/app-content/scripts/make_images.py usa-schema-staedte kanada-schema kanada-schema-aufgabe

OTHER = "#f0ece0"  # Nachbarländer


def register(m):
    # ---- Kanada als ein grober Umriss (viewBox 480 x 300), Norden oben ----
    CANADA = [(62, 164), (54, 134), (72, 106), (88, 74), (130, 54), (200, 50), (270, 52), (330, 54), (372, 66), (404, 58),
              (432, 78), (440, 106), (426, 128), (444, 150), (458, 178), (430, 190), (402, 182), (380, 176), (334, 172),
              (270, 168), (200, 164), (120, 164)]
    HUDSON = [(246, 100), (278, 92), (302, 102), (306, 126), (294, 146), (270, 144), (252, 126)]
    ISLANDS = [[(150, 30), (190, 22), (206, 38), (170, 44)], [(214, 26), (262, 18), (292, 34), (240, 42)],
               [(330, 20), (372, 14), (394, 38), (366, 50)], [(448, 118), (468, 110), (474, 130), (454, 140)]]
    ALASKA = [(14, 34), (80, 28), (90, 70), (80, 102), (56, 90), (30, 96), (14, 70)]

    def canada_base():
        b = '  <rect x="0" y="0" width="480" height="300" fill="#e9f1f7"/>\n'
        b += m.poly([(0, 164), (62, 164), (120, 164), (200, 164), (270, 168), (334, 172), (380, 176), (402, 182), (430, 190),
                     (458, 178), (480, 178), (480, 300), (0, 300)], fill=OTHER, stroke="none", sw=0)  # USA
        b += m.poly(ALASKA, fill=OTHER)
        b += m.poly(CANADA, fill=m.LAND)
        for isl in ISLANDS:
            b += m.poly(isl, fill=m.LAND)
        b += m.poly(HUDSON, fill="#e9f1f7")
        return b

    def dot(x, y, r=5, fill="#d35400"):
        return f'  <circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{m.INK}" stroke-width="2"/>\n'

    @m.image
    def kanada_schema():
        """Erklärbild: Kanada mit Nachbarn und drei grossen Städten, Ottawa als Hauptstadt."""
        b = canada_base()
        b += m.text(200, 118, "Canada", 20, "middle", m.INK, "bold")
        b += m.text(200, 232, "USA", 18, "middle", m.INK, "bold")
        def leader(x1, y1, x2, y2):
            return f'  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{m.INK}" stroke-width="1.5"/>\n'
        b += dot(70, 156)
        b += m.text(78, 146, "Vancouver", 14, "start")
        # drei Städte im Südosten: Beschriftungen unten in den USA, mit Linien
        b += leader(350, 174, 338, 196) + leader(400, 160, 420, 198)
        b += dot(350, 174, 4, "#555")
        b += m.text(340, 212, "Toronto", 14, "end")
        b += dot(400, 160, 4, "#555")
        b += m.text(440, 214, "Montreal", 14, "end")
        b += m.poly([(374, 130), (377, 138), (385, 138), (379, 143), (381, 151), (374, 146), (367, 151), (369, 143), (363, 138), (371, 138)],
                    fill="#d35400", sw=2)
        b += m.text(358, 140, "Ottawa", 15, "end", m.INK, "bold")
        return m.svg(480, 300, "Schemakarte von Kanada mit Nachbarn und drei Städten", b)

    @m.image
    def kanada_schema_aufgabe():
        """Aufgabenbild: drei Meere als Markierungen (Namen kommen aus der Seite, labelled-figure)."""
        b = canada_base()
        return m.svg(480, 300, "Schemakarte von Kanada ohne Beschriftung", b)

    # ---- USA mit New York, Washington, D.C. und Chicago ----
    @m.image
    def usa_schema_staedte():
        b = m.usa_base() + m.insets()
        b += '  <circle cx="424" cy="92" r="6" fill="#d35400" stroke="#333" stroke-width="2"/>\n'
        b += '  <circle cx="408" cy="124" r="6" fill="#d35400" stroke="#333" stroke-width="2"/>\n'
        b += '  <circle cx="338" cy="100" r="5" fill="#555" stroke="#333" stroke-width="2"/>\n'
        b += m.text(412, 82, "New York", 15, "end", m.INK, "bold")
        b += m.text(396, 146, "Washington, D.C.", 15, "end", m.INK, "bold")
        b += m.text(330, 118, "Chicago", 14, "end")
        b += m.text(290, 24, "Canada", 14)
        return m.svg(480, 300, "Schemakarte der USA mit New York, Washington, D.C. und Chicago", b)

    # ---- Stundenplan eines Tages an Jaydens High School (Beispiel, ohne Uhrzeiten) ----
    @m.image
    def schule_stundenplan():
        rows = [("Homeroom", "#fff4d6"), ("First period", "#e3d9bd"), ("Second period", "#e3d9bd"), ("Lunch", "#d7ecd9"),
                ("Third period · music (elective)", "#cfe3f1"), ("Fourth period", "#e3d9bd"), ("After school: sports practice", "#f7d9c4")]
        b = m.text(240, 24, "Jaydens Schultag (Beispiel)", 18, "middle", m.INK, "bold")
        y = 36
        for label, fill in rows:
            b += m.rect(30, y, 420, 28, fill, m.INK, 2, 6)
            b += m.text(46, y + 20, label, 16, "start")
            y += 33
        return m.svg(480, 300, "Stundenplan eines Tages mit Homeroom, vier Unterrichtsstunden, Mittagessen und Sporttraining", b)
