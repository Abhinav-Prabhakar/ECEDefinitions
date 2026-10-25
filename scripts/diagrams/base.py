"""Shared drawing primitives for the one·liners diagram library.

Every symbol is thin line art on a 240×150 grid. Strokes inherit currentColor;
accent strokes use var(--accent), so the theme and the subject hue flow through.
Keep labels sparse, uppercase, and at least 5.6px in the 240-unit viewBox.
"""
import math

W, H = 240, 150
INK = 'currentColor'
ACCENT = 'var(--accent)'
FONT = "'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif"


def line(x1, y1, x2, y2, o=1, w=1, dash=None, color=INK):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
            f'stroke="{color}" stroke-width="{w}" opacity="{min(1, o * 1.18):.3f}"{d}/>')


def path(d, o=1, w=1, dash=None, color=INK, fill='none'):
    da = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<path d="{d}" fill="{fill}" stroke="{color}" stroke-width="{w}" '
            f'opacity="{min(1, o * 1.18):.3f}"{da}/>')


def rect(x, y, w, h, r=2, o=1, dash=None, color=INK, fill='none', sw=1):
    da = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" '
            f'fill="{fill}" stroke="{color}" stroke-width="{sw}" '
            f'opacity="{min(1, o * 1.18):.3f}"{da}/>')


def circle(cx, cy, r, o=1, color=INK, fill='none', sw=1):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" '
            f'stroke="{color}" stroke-width="{sw}" opacity="{min(1, o * 1.18):.3f}"/>')


def dot(cx, cy, r=2.4, o=1, color=INK):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}" opacity="{min(1, o * 1.18):.3f}"/>'


def text(x, y, s, anchor='middle', o=.55, size=6.2, ls='.1em', color=INK):
    o = max(o, .58)
    size = max(size, 5.6)
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="{FONT}" '
            f'font-size="{size}" font-weight="300" letter-spacing="{ls}" '
            f'fill="{color}" opacity="{o}" stroke="none">{s}</text>')


def amp(x, y, s, o=.5, size=5.6, ls='.1em'):
    return text(x, y, s, o=o, size=size, ls=ls)


def arrow(x1, y1, x2, y2, o=.65, color=INK, head=4, w=1):
    a = math.atan2(y2 - y1, x2 - x1)
    h1 = (x2 - head * math.cos(a - .5), y2 - head * math.sin(a - .5))
    h2 = (x2 - head * math.cos(a + .5), y2 - head * math.sin(a + .5))
    return (line(x1, y1, x2, y2, o, w, color=color) +
            path(f'M{h1[0]:.1f} {h1[1]:.1f} L{x2} {y2} L{h2[0]:.1f} {h2[1]:.1f}',
                 o, w, color=color))


def axis(x0, y0, x1, y1, o=.45):
    return arrow(x0, y0, x1, y1, o)


def sine(x0, x1, y, amp, cycles, o=.7, color=INK, dash=None):
    n = 64
    pts = []
    for i in range(n + 1):
        t = i / n
        pts.append(f'{x0 + (x1 - x0) * t:.1f},{y - amp * math.sin(2 * math.pi * cycles * t):.1f}')
    return path('M' + ' L'.join(pts), o, 1, dash, color)


def curve(points, o=.7, color=INK, dash=None, w=1):
    """Smooth-ish polyline from [(x, y), ...]."""
    return path('M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in points), o, w, dash, color)


def wave(points, o=.7, color=INK, dash=None, w=1):
    """Alias for a sampled curve, used for measured responses."""
    return curve(points, o, color, dash, w)


def bracket(x, y1, y2, label, o=.45, side='right'):
    x0 = x
    tick = 3 if side == 'right' else -3
    out = [line(x0, y1, x0, y2, o), line(x0, y1, x0 + tick, y1, o),
           line(x0, y2, x0 + tick, y2, o)]
    if label:
        out.append(text(x0 + (8 if side == 'right' else -8), (y1 + y2) / 2 + 2, label,
                        'start' if side == 'right' else 'end', o, 4.8, '.04em'))
    return ''.join(out)


def bars(x, y, values, w=8, gap=3, height=40, o=.55, accent_last=False):
    out = []
    for i, v in enumerate(values):
        h = max(1, v * height)
        out.append(rect(x + i * (w + gap), y + height - h, w, h, 1, o,
                        color=ACCENT if accent_last and i == len(values) - 1 else INK))
    return ''.join(out)


def grid(x, y, cols, rows, cw, ch, o=.2):
    return ''.join(line(x + c * cw, y, x + c * cw, y + rows * ch, o) for c in range(cols + 1)) + \
           ''.join(line(x, y + r * ch, x + cols * cw, y + r * ch, o) for r in range(rows + 1))


def box_label(x, y, w, h, label, sub='', o=.55, accent=False):
    out = [rect(x, y, w, h, 2, o, color=ACCENT if accent else INK)]
    out.append(text(x + w / 2, y + h / 2 + (2 if sub else 1), label, 'middle', .62, 5.2, '.08em'))
    if sub:
        out.append(text(x + w / 2, y + h / 2 + 9, sub, 'middle', .38, 4.4, '.06em'))
    return ''.join(out)


def block_chain(labels, y=62, x0=24, x1=216, gap=8, h=26, o=.55, accent=-1):
    n = len(labels)
    w = (x1 - x0 - gap * (n - 1)) / n
    out = []
    for i, lab in enumerate(labels):
        x = x0 + i * (w + gap)
        out.append(box_label(x, y, w, h, lab, o=o, accent=(i == accent)))
        if i < n - 1:
            out.append(arrow(x + w, y + h / 2, x + w + gap - 1, y + h / 2, .45, head=3))
    return ''.join(out)


def polar_lobe(cx, cy, r, angle0=0, spread=math.pi, o=.6, color=ACCENT):
    pts = []
    n = 40
    for i in range(n + 1):
        a = angle0 - spread / 2 + spread * i / n
        rr = r * abs(math.cos(a - angle0))
        pts.append(f'{cx + rr * math.cos(a):.1f},{cy + rr * math.sin(a):.1f}')
    return path('M' + ' L'.join(pts), o, 1.2, color=color)


def arrow_arc(cx, cy, r, a0, a1, o=.5, color=ACCENT, head=3):
    pts = []
    n = 16
    for i in range(n + 1):
        a = a0 + (a1 - a0) * i / n
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    out = [curve(pts, o, color, w=1)]
    x1, y1 = pts[-2]
    x2, y2 = pts[-1]
    a = math.atan2(y2 - y1, x2 - x1)
    h1 = (x2 - head * math.cos(a - .5), y2 - head * math.sin(a - .5))
    h2 = (x2 - head * math.cos(a + .5), y2 - head * math.sin(a + .5))
    out.append(path(f'M{h1[0]:.1f} {h1[1]:.1f} L{x2:.1f} {y2:.1f} L{h2[0]:.1f} {h2[1]:.1f}',
                    o, 1, color=color))
    return ''.join(out)
