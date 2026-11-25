# Bilder von Kapitel 2 (british-or-american): drei einfache Schemabilder, eigene Zeichnung.
# Aufruf: python3 .agents/skills/app-content/scripts/make_images.py be-ae-auto be-ae-klang be-ae-buchstaben
GB_COL = "#2c6fd8"   # britisch: blau
US_COL = "#d35400"   # amerikanisch: orange


def register(m):
    def legend(y=24):
        b = m.rect(20, y - 16, 20, 20, GB_COL, m.INK, 1, 3)
        b += m.text(48, y, "britisch", 16, "start")
        b += m.rect(160, y - 16, 20, 20, US_COL, m.INK, 1, 3)
        b += m.text(188, y, "amerikanisch", 16, "start")
        return b

    @m.image
    def be_ae_auto():
        """Page be-ae-wortschatz, section neu: a car with the front and the back named in both varieties."""
        b = legend()
        b += m.poly([(70, 170), (70, 130), (120, 120), (170, 85), (290, 85), (340, 120), (410, 130), (410, 170)], fill="#e3d9bd")
        b += m.rect(184, 96, 46, 30, "#f4efe2", m.INK, 2, 3)
        b += m.rect(238, 96, 46, 30, "#f4efe2", m.INK, 2, 3)
        for cx in (130, 350):
            b += f'  <circle cx="{cx}" cy="172" r="22" fill="#555" stroke="{m.INK}" stroke-width="2"/>\n'
            b += f'  <circle cx="{cx}" cy="172" r="9" fill="#ccc" stroke="{m.INK}" stroke-width="1"/>\n'
        b += f'  <rect x="68" y="136" width="10" height="14" rx="3" fill="#f7e27a" stroke="{m.INK}" stroke-width="1"/>\n'
        b += f'  <line x1="105" y1="124" x2="105" y2="205" stroke="{m.INK}" stroke-width="2"/>\n'
        b += f'  <line x1="370" y1="126" x2="370" y2="205" stroke="{m.INK}" stroke-width="2"/>\n'
        b += m.text(105, 232, "bonnet", 18, "middle", GB_COL, "bold")
        b += m.text(105, 256, "hood", 18, "middle", US_COL, "bold")
        b += m.text(370, 232, "boot", 18, "middle", GB_COL, "bold")
        b += m.text(370, 256, "trunk", 18, "middle", US_COL, "bold")
        b += m.text(20, 290, "Schemabild, nicht genau nach Maßstab", 14, "start")
        return m.svg(480, 300, "Schemabild eines Autos mit den Wörtern für Motorhaube und Kofferraum", b)

    @m.image
    def be_ae_klang():
        """Page be-ae-aussprache, section neu: three words with the reading aid of both accents."""
        b = legend()
        rows = [("stork", "stohk", "stohrk"), ("ladder", "ladder, latter: verschieden", "ledder, ledder: gleich"), ("grass", "grahss", "gräss")]
        y = 40
        for w, gb, us in rows:
            b += m.rect(20, y, 440, 60, "#f4efe2", m.INK, 2, 6)
            b += m.text(36, y + 36, w if w != "ladder" else "ladder · latter", 20, "start", m.INK, "bold")
            if w == "ladder":
                b += m.text(200, y + 25, "britisch: verschieden", 16, "start", GB_COL)
                b += m.text(200, y + 49, "amerikanisch: gleich", 16, "start", US_COL)
            else:
                b += m.text(200, y + 25, "britisch: " + gb, 16, "start", GB_COL)
                b += m.text(200, y + 49, "amerikanisch: " + us, 16, "start", US_COL)
            y += 70
        # Nichts in den unteren 12 Prozent und rechts unten (Lizenz-Badge der Laufzeit).
        return m.svg(480, 280, "Drei Wörter mit Lesehilfe für die britische und die amerikanische Aussprache", b)

    @m.image
    def be_ae_buchstaben():
        """Page be-ae-schreibung, section neu: four spelling pairs with the changing letters marked."""
        def pair(y, gb_before, gb_mark, gb_after, us_before, us_mark, us_after):
            s = f'  <text x="36" y="{y}" font-family="sans-serif" font-size="20" fill="{GB_COL}" text-anchor="start">{gb_before}<tspan font-weight="bold" text-decoration="underline">{gb_mark}</tspan>{gb_after}</text>\n'
            s += f'  <text x="250" y="{y}" font-family="sans-serif" font-size="20" fill="{US_COL}" text-anchor="start">{us_before}<tspan font-weight="bold" text-decoration="underline">{us_mark}</tspan>{us_after}</text>\n'
            return s
        b = m.text(36, 30, "britisch", 16, "start", GB_COL, "bold") + m.text(250, 30, "amerikanisch", 16, "start", US_COL, "bold")
        b += f'  <line x1="228" y1="40" x2="228" y2="250" stroke="{m.INK}" stroke-width="1" stroke-dasharray="4 4"/>\n'
        b += pair(80, "hon", "ou", "r", "hon", "o", "r")
        b += pair(130, "lit", "re", "", "lit", "er", "")
        b += pair(180, "rea", "lis", "e", "rea", "liz", "e")
        b += pair(230, "can", "cell", "ed", "can", "cel", "ed")
        b += m.text(20, 282, "Die unterstrichenen Buchstaben sind anders.", 14, "start")
        return m.svg(480, 300, "Vier Wortpaare mit markierten Buchstaben, die sich unterscheiden", b)
