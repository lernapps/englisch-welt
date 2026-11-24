# Bilder von Kapitel 5 (englisch-weltweit): Schemakarten Australiens und die Abstandszonen. Wird von make_images.py geladen.
# Alle Karten sind Schemakarten, nicht genau nach Maßstab; Lage nach den geöffneten Quellen (en.wikipedia Australia).
import math


def register(m):
    # Australien: Längen- und Breitengrade grob in den viewBox 480 x 300 umgerechnet (nur Schema).
    def ll(lon, lat):
        return (round(40 + (lon - 112) * 7.0), round(28 + (-lat - 9) * 7.0))

    MAINLAND = [
        (142.5, -10.7), (143.5, -14), (145.3, -15.5), (146, -17), (146.8, -19.3), (149.2, -21.1), (150.8, -23.4),
        (153.2, -25), (153.1, -27.5), (153.6, -28.6), (151.3, -33.8), (150, -37.5), (146.4, -39.1), (144.8, -38.3),
        (141.6, -38.3), (139.5, -36.7), (138.5, -35.3), (137.7, -33.1), (136, -34.8), (134, -32.8), (131, -31.5),
        (126, -32.3), (124, -33.5), (121.5, -33.9), (118, -35), (115.1, -34.3), (115.7, -32), (114.9, -29.5),
        (113.5, -26.2), (114.2, -22.2), (116.5, -20.6), (119, -20), (121.5, -19), (122.3, -17.5), (123.5, -16.8),
        (125.5, -14.2), (127, -13.5), (129.5, -14.9), (130, -12.4), (131.8, -11.5), (133, -11.7), (136.8, -12.3),
        (135.8, -14.5), (136.7, -15.8), (139, -17.2), (140.8, -17.5), (141.5, -15.5), (141.6, -13),
    ]
    TASMANIA = [(144.7, -40.7), (148.3, -40.9), (148, -42.8), (147, -43.6), (145.9, -43.3), (145, -42)]

    def au_base():
        b = '  <rect x="0" y="0" width="480" height="300" fill="#e9f1f7"/>\n'
        b += m.poly([(150, 0), (480, 0), (480, 22), (330, 20), (230, 8), (150, 14)], fill="#f0ece0", stroke="none", sw=0)  # Inseln im Norden (Schema)
        b += m.poly([ll(*p) for p in MAINLAND], fill=m.LAND)
        b += m.poly([ll(*p) for p in TASMANIA], fill=m.LAND)
        return b

    @m.image
    def australien_schema_natur():
        """Karte im Abschnitt `neu`: Hauptstadt, zwei große Städte, Gebirge, Riff, Tasmanien."""
        b = au_base()
        # Great Dividing Range: Gebirgszeichen entlang der Ostseite, etwas im Landesinneren
        for lon, lat in [(143.4, -16.2), (145.0, -20), (147.0, -24.3), (148.6, -28.2), (148.9, -31.6)]:
            x, y = ll(lon, lat)
            b += m.poly([(x - 9, y + 7), (x, y - 8), (x + 9, y + 7)], fill="#9aa5ad", sw=2)
        # Great Barrier Reef: gestrichelte Linie vor der Nordostküste
        pts = [ll(144.0, -12.6), ll(145.9, -15), ll(148.0, -18.4), ll(150.4, -21.6), ll(153.0, -24.1)]
        d = "M" + " L".join(f"{x},{y}" for x, y in pts)
        b += f'  <path d="{d}" fill="none" stroke="#138d75" stroke-width="5" stroke-dasharray="2 8" stroke-linecap="round"/>\n'
        # Städte
        sx, sy = ll(151.2, -33.9)
        mx, my = ll(144.96, -37.8)
        cx, cy = ll(149.1, -35.3)
        for x, y in [(sx, sy), (mx, my)]:
            b += f'  <circle cx="{x}" cy="{y}" r="5" fill="{m.INK}"/>\n'
        b += (f'  <polygon points="{cx},{cy-9} {cx+3},{cy-3} {cx+9},{cy-3} {cx+4},{cy+2} {cx+6},{cy+9} {cx},{cy+5} {cx-6},{cy+9} {cx-4},{cy+2} '
              f'{cx-9},{cy-3} {cx-3},{cy-3}" fill="{m.ORANGE}" stroke="{m.INK}" stroke-width="1.5"/>\n')
        b += m.text(sx + 12, sy - 4, "Sydney", 14, "start")
        b += m.text(cx - 14, cy - 2, "Canberra", 14, "end", m.ORANGE, "bold")
        b += m.text(mx - 10, my + 5, "Melbourne", 14, "end")
        b += m.text(ll(147.2, -27.5)[0] - 20, ll(147.2, -27.5)[1] + 4, "Great Dividing Range", 14, "end")
        b += m.text(ll(149.2, -17.0)[0], ll(149.2, -17.0)[1], "Great Barrier Reef", 14, "start", m.GREEN)
        b += m.text(ll(148.9, -42.0)[0], ll(148.9, -42.0)[1] + 4, "Tasmania", 14, "start")
        return m.svg(480, 300, "Schemakarte Australiens mit Hauptstadt, Städten, Gebirge, Riff und Tasmanien", b)

    @m.image
    def australien_schema_aufgabe():
        """Karte für die Übung: keine Namen; die Markierungen kommen von der Seite (labelled-figure)."""
        return m.svg(480, 300, "Schemakarte Australiens ohne Beschriftung", au_base())

    @m.image
    def abstandszonen():
        """Vier Abstandszonen nach Hall (en.wikipedia Proxemics) als Ringe um eine Person, nicht maßstabsgetreu."""
        b = '  <rect x="0" y="0" width="480" height="300" fill="#f4efe2"/>\n'
        cx, cy = 150, 150
        for r, fill in [(128, "#e9f1f7"), (96, "#dcebf5"), (64, "#cfe3f1"), (32, "#b9d6ec")]:
            b += f'  <circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{m.INK}" stroke-width="2"/>\n'
        b += f'  <circle cx="{cx}" cy="{cy}" r="8" fill="{m.INK}"/>\n'
        rows = [("intimate", "bis etwa 0,5 m", 32, -60, 50), ("personal", "etwa 0,5 bis 1,2 m", 64, -30, 115),
                ("social", "etwa 1,2 bis 3,7 m", 96, 10, 180), ("public", "mehr als 3,7 m", 128, 40, 245)]
        for name, dist, r, deg, ty in rows:
            a = math.radians(deg)
            x1, y1 = cx + r * math.cos(a), cy + r * math.sin(a)
            b += f'  <line x1="{x1:.0f}" y1="{y1:.0f}" x2="304" y2="{ty - 5}" stroke="{m.INK}" stroke-width="1.5"/>\n'
            b += f'  <circle cx="{x1:.0f}" cy="{y1:.0f}" r="3" fill="{m.INK}"/>\n'
            b += m.text(312, ty, name, 16, "start", m.INK, "bold")
            b += m.text(312, ty + 18, dist, 14, "start")
        return m.svg(480, 300, "Vier Abstandszonen als Ringe um eine Person", b)
