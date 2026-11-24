# Figures of chapter 4 `freiheit-gleichheit` (Schemakarten und Schaubilder, selbst gezeichnet). Loaded by make_images.py.
#   python3 .agents/skills/app-content/scripts/make_images.py buergerkrieg-schema buergerkrieg-aufgabe demokratie-schema montgomery-bus-schema migration-vergleich

# the Confederate states as one schematic area inside the outline of the lower 48 (480 x 300)
CONF = [(196, 168), (290, 150), (340, 150), (404, 150), (406, 190), (416, 236), (398, 246), (380, 208), (346, 214),
        (300, 222), (256, 240), (236, 264), (210, 246), (180, 236), (196, 200)]
SITES = {"fort-sumter": (396, 184), "richmond": (384, 152), "gettysburg": (378, 118), "vicksburg": (281, 192)}


def register(m):
    def dot(x, y):
        return f'  <circle cx="{x}" cy="{y}" r="6" fill="{m.ORANGE}" stroke="{m.INK}" stroke-width="2"/>\n'

    def arrow(x1, y1, x2, y2, w=3):
        """A line with a small head at (x2, y2); heads point right, left, down or up."""
        b = f'  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{m.INK}" stroke-width="{w}"/>\n'
        if x2 > x1: head = [(x2, y2), (x2 - 12, y2 - 7), (x2 - 12, y2 + 7)]
        elif x2 < x1: head = [(x2, y2), (x2 + 12, y2 - 7), (x2 + 12, y2 + 7)]
        elif y2 > y1: head = [(x2, y2), (x2 - 7, y2 - 12), (x2 + 7, y2 - 12)]
        else: head = [(x2, y2), (x2 - 7, y2 + 12), (x2 + 7, y2 + 12)]
        return b + m.poly(head, fill=m.INK, stroke=m.INK, sw=1)

    def war_map(names):
        b = m.usa_base()
        b += m.poly(CONF, fill="#e6b9a0")
        b += '  <path d="M268,70 C272,110 262,150 286,214" fill="none" stroke="#2c6fd8" stroke-width="5" stroke-linecap="round"/>\n'
        for x, y in SITES.values(): b += dot(x, y)
        if names:
            b += m.text(230, 104, "Union", 18, "middle", m.INK, "bold")
            b += m.text(330, 176, "Confederacy", 16, "middle", m.INK, "bold")
            b += m.text(388, 108, "Gettysburg", 14, "end")
            b += m.text(374, 148, "Richmond", 14, "end")
            b += m.text(388, 206, "Fort Sumter", 14, "end")
            b += m.text(270, 197, "Vicksburg", 14, "end")
        return b

    @m.image
    def buergerkrieg_schema():
        """Section `neu` of sklaverei-buergerkrieg: the two sides and four places of the war (names)."""
        return m.svg(480, 300, "Schemakarte der USA im Bürgerkrieg: Union im Norden, Konföderation im Süden, vier Orte", war_map(True))

    @m.image
    def buergerkrieg_aufgabe():
        """Exercise map of sklaverei-buergerkrieg: the same places, no names (markers come from the page)."""
        return m.svg(480, 300, "Schemakarte der USA im Bürgerkrieg ohne Beschriftung", war_map(False))

    @m.image
    def demokratie_schema():
        """Section `neu` of gesellschaft-politik: a schematic of representative democracy."""
        b = m.rect(20, 40, 150, 60, "#e3edf7") + m.text(95, 78, "Citizens", 18, "middle", m.INK, "bold")
        b += m.rect(310, 40, 150, 60, "#f7e8d8") + m.text(385, 64, "Elected", 18, "middle", m.INK, "bold")
        b += m.text(385, 86, "representatives", 18, "middle", m.INK, "bold")
        b += m.rect(310, 170, 150, 60, "#e1f0e8") + m.text(385, 208, "Laws", 18, "middle", m.INK, "bold")
        b += arrow(170, 70, 308, 70) + m.text(240, 60, "vote for", 16)
        b += arrow(385, 100, 385, 168) + m.text(440, 140, "make", 16)
        b += f'  <line x1="310" y1="200" x2="95" y2="200" stroke="{m.INK}" stroke-width="3"/>\n'
        b += arrow(95, 200, 95, 102) + m.text(200, 192, "apply to everyone", 16)
        b += m.rect(20, 250, 440, 38, "#f4efe2", m.INK, 2, 4) + m.text(240, 275, "In between: meet, protest, write petitions", 16)
        return m.svg(480, 300, "Schema der repräsentativen Demokratie", b)

    @m.image
    def montgomery_bus_schema():
        """Section `neu` of buergerrechtsbewegung: the seats of a Montgomery bus under segregation (1955)."""
        b = m.rect(20, 40, 440, 110, "#f4efe2", m.INK, 3, 14)
        x0, size, gap = 36, 19, 2
        cols = [("#dfe9f5", 5), ("#ece6d3", 8), ("#f0dede", 5)]
        x = x0
        for fill, n in cols:
            for i in range(n):
                for y in (62, 104):
                    b += m.rect(x + i * (size + gap), y, size, size, fill, m.INK, 2, 3)
            x += n * (size + gap) + 6
        b += m.text(20, 24, "front of the bus", 14, "start") + m.text(460, 24, "back of the bus", 14, "end")
        b += m.text(95, 172, "Front", 16, "middle", m.INK, "bold") + m.text(95, 192, "10 seats", 14) + m.text(95, 212, "reserved for", 14) + m.text(95, 232, "white riders", 14)
        b += m.text(240, 172, "Middle", 16, "middle", m.INK, "bold") + m.text(240, 192, "16 seats", 14) + m.text(240, 212, "not reserved,", 14) + m.text(240, 232, "but still separated", 14)
        b += m.text(388, 172, "Back", 16, "middle", m.INK, "bold") + m.text(388, 192, "10 seats", 14) + m.text(388, 212, "reserved for", 14) + m.text(388, 232, "Black riders", 14)
        return m.svg(480, 260, "Schema der Sitzreihen eines Busses in Montgomery", b)

    @m.image
    def migration_vergleich():
        """Section `neu` of migration-heute: share of foreign-born residents, UK and USA (numbers with year)."""
        b = f'  <line x1="40" y1="34" x2="40" y2="236" stroke="{m.INK}" stroke-width="2"/>\n'
        unit = 20.0  # px per percentage point
        for p in (0, 5, 10, 15, 20):
            x = 40 + p * unit
            b += f'  <line x1="{x}" y1="236" x2="{x}" y2="244" stroke="{m.INK}" stroke-width="2"/>\n'
            b += m.text(x, 266, f"{p} %", 14)
        b += m.text(48, 28, "United Kingdom, 2021 to 2022 censuses", 16, "start", m.INK, "bold")
        b += m.rect(40, 38, 16 * unit, 40, m.BLUE, m.INK, 2, 3) + m.text(40 + 16 * unit - 10, 65, "16 %", 18, "end", "#fff", "bold")
        b += m.text(48, 100, "10.7 million people born abroad", 14, "start")
        b += m.text(48, 140, "United States, January 2025", 16, "start", m.INK, "bold")
        b += m.rect(40, 150, 15.8 * unit, 40, m.ORANGE, m.INK, 2, 3) + m.text(40 + 15.8 * unit - 10, 177, "15.8 %", 18, "end", "#fff", "bold")
        b += m.text(48, 212, "53.3 million people born abroad", 14, "start")
        return m.svg(480, 280, "Balkendiagramm: Anteil der im Ausland Geborenen im Vereinigten Königreich und in den USA", b)
