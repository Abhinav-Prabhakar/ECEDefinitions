"""Diagram family: electronics.

Thin-line concept marks for circuits, devices and systems.  Every symbol is a
240x150 body of primitives; structure is INK, the one idea is ACCENT.
"""
import math

from .base import *

# The standalone preview sheet does not define --accent; fall back to the
# inherited ink so accent marks still render there.  The site defines the
# token, so the real accent is used wherever it matters.
ACCENT = 'var(--accent, currentColor)'


# --------------------------------------------------------------------------
# component helpers
# --------------------------------------------------------------------------

def res_h(cx, cy, w=22, h=4, o=.5, color=INK):
    x0, x1 = cx - w / 2, cx + w / 2
    xa, xb = x0 + w * .14, x1 - w * .14
    pts = [(x0, cy), (xa, cy)]
    n = 6
    for i in range(n):
        x = xa + (xb - xa) * (i + .5) / n
        pts.append((x, cy + (h if i % 2 else -h)))
    pts += [(xb, cy), (x1, cy)]
    return curve(pts, o, color, w=1)


def res_v(cx, cy, h=22, w=4, o=.5, color=INK):
    y0, y1 = cy - h / 2, cy + h / 2
    ya, yb = y0 + h * .14, y1 - h * .14
    pts = [(cx, y0), (cx, ya)]
    n = 6
    for i in range(n):
        y = ya + (yb - ya) * (i + .5) / n
        pts.append((cx + (w if i % 2 else -w), y))
    pts += [(cx, yb), (cx, y1)]
    return curve(pts, o, color, w=1)


def res_box(a, b, L=17, W=7.5, o=.45, color=INK):
    x1, y1 = a
    x2, y2 = b
    dx, dy = x2 - x1, y2 - y1
    ln = math.hypot(dx, dy)
    ux, uy = dx / ln, dy / ln
    px, py = -uy, ux
    cx, cy = (x1 + x2) / 2, (y1 + y2) / 2
    pts = [(cx + ux * L / 2 + px * W / 2, cy + uy * L / 2 + py * W / 2),
           (cx + ux * L / 2 - px * W / 2, cy + uy * L / 2 - py * W / 2),
           (cx - ux * L / 2 - px * W / 2, cy - uy * L / 2 - py * W / 2),
           (cx - ux * L / 2 + px * W / 2, cy - uy * L / 2 + py * W / 2)]
    return path('M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in pts) + ' Z', o, color=color)


def res_arm(a, b, L=17, W=7.5, o=.45, color=INK):
    ax, ay = a
    bx, by = b
    ln = math.hypot(bx - ax, by - ay)
    ux, uy = (bx - ax) / ln, (by - ay) / ln
    p1 = (ax + ux * (ln - L) / 2, ay + uy * (ln - L) / 2)
    p2 = (ax + ux * (ln + L) / 2, ay + uy * (ln + L) / 2)
    return (line(ax, ay, p1[0], p1[1], o, color=color) +
            res_box(a, b, L, W, o, color) +
            line(p2[0], p2[1], bx, by, o, color=color))


def cap_h(cx, cy, half=7, gap=2.6, o=.55, color=INK):
    return (line(cx - half, cy - gap / 2, cx + half, cy - gap / 2, o, color=color) +
            line(cx - half, cy + gap / 2, cx + half, cy + gap / 2, o, color=color) +
            line(cx - half, cy, cx - half - 6, cy, o, color=color) +
            line(cx + half, cy, cx + half + 6, cy, o, color=color))


def cap_v(cx, cy, half=7, gap=2.6, o=.55, color=INK):
    return (line(cx - gap / 2, cy - half, cx - gap / 2, cy + half, o, color=color) +
            line(cx + gap / 2, cy - half, cx + gap / 2, cy + half, o, color=color) +
            line(cx, cy - half, cx, cy - half - 6, o, color=color) +
            line(cx, cy + half, cx, cy + half + 6, o, color=color))


def ind_v(cx, cy, h=20, o=.55, color=INK):
    r = h / 8
    d = f'M{cx},{cy - h / 2} ' + ''.join(f'a{r},{r} 0 0 1 0,{2 * r} ' for _ in range(4))
    return path(d, o, 1.1, color=color)


def gnd(cx, cy, w=14, o=.42, color=INK):
    return (line(cx, cy, cx, cy + 4, o, color=color) +
            line(cx - w / 2, cy + 4, cx + w / 2, cy + 4, o, color=color) +
            line(cx - w / 3, cy + 8, cx + w / 3, cy + 8, o, color=color) +
            line(cx - w / 6, cy + 12, cx + w / 6, cy + 12, o, color=color))


def battery_v(cx, cy, o=.55, color=INK):
    return (line(cx, cy - 9, cx, cy - 4, o, color=color) +
            line(cx - 7, cy - 4, cx + 7, cy - 4, o, color=color) +
            line(cx - 4, cy + 1, cx + 4, cy + 1, o, color=color) +
            line(cx, cy + 1, cx, cy + 9, o, color=color))


def opamp(cx, cy, w=70, h=54, o=.55, color=INK):
    x0, x1 = cx - w / 2, cx + w / 2
    return path(f'M{x0},{cy - h / 2} L{x1},{cy} L{x0},{cy + h / 2} Z', o, color=color)


def npn(cx, cy, r=14, face=1, o=.5, color=INK):
    bar = cx - 5 * face
    out = [circle(cx, cy, r, o, color),
           line(bar, cy - 7, bar, cy + 7, o, 1.2, color=color),
           line(bar, cy, bar - 15 * face, cy, o, color=color),
           line(bar, cy - 3, cx + 5 * face, cy - 8, o, color=color),
           line(cx + 5 * face, cy - 8, cx + 5 * face, cy - r - 2, o, color=color),
           line(bar, cy + 3, cx + 5 * face, cy + 8, o, color=color),
           line(cx + 5 * face, cy + 8, cx + 5 * face, cy + r + 2, o, color=color)]
    ax, ay = cx + 1 * face, cy + 6
    out.append(arrow(ax, ay - 2, ax + 2 * face, ay + 2, o, color, 3))
    return ''.join(out)


def nmos(cx, cy, face=1, o=.5, color=INK, hot=False):
    gx = cx - 6 * face
    ch = ACCENT if hot else color
    return (line(cx, cy - 10, cx, cy + 10, .8 if hot else o, 1.5 if hot else 1.2, color=ch) +
            line(gx, cy - 7, gx, cy + 7, o, color=color) +
            line(gx, cy, gx - 12 * face, cy, o, color=color) +
            line(cx, cy - 10, cx, cy - 20, o, color=color) +
            line(cx, cy + 10, cx, cy + 20, o, color=color) +
            arrow(cx, cy + 17, cx, cy + 11, o, color, 2.6))


def fet_h(cx, cy, gate='down', p=False, o=.5, color=INK, hot=False):
    gy = cy + 6 if gate == 'down' else cy - 6
    sgn = 1 if gate == 'down' else -1
    ch = ACCENT if hot else color
    out = [line(cx - 10, cy, cx + 10, cy, .8 if hot else o, 1.5 if hot else 1.2, color=ch),
           line(cx - 22, cy, cx - 10, cy, o, color=color),
           line(cx + 10, cy, cx + 22, cy, o, color=color),
           line(cx - 7, gy, cx + 7, gy, o, color=color)]
    if p:
        bc = gy + 2.5 * sgn
        out.append(circle(cx, bc, 2.2, o, color))
        out.append(line(cx, bc + 2.2 * sgn, cx, gy + 9 * sgn, o, color=color))
    else:
        out.append(line(cx, gy, cx, gy + 9 * sgn, o, color=color))
    return ''.join(out)


def _trace(fn, x0, x1, y, amp, cycles=1, n=64, color=INK):
    pts = []
    for i in range(n + 1):
        t = i / n
        pts.append((x0 + (x1 - x0) * t, y - amp * fn(2 * math.pi * cycles * t)))
    return curve(pts, .75, color)


# --------------------------------------------------------------------------
# 1. node-mesh
# --------------------------------------------------------------------------

def node_mesh():
    return ''.join([
        line(42, 45, 70, 45, .5), line(90, 45, 150, 45, .5),
        line(170, 45, 198, 45, .5), line(42, 112, 198, 112, .5),
        line(42, 45, 42, 69, .5), line(42, 87, 42, 112, .5),
        line(198, 45, 198, 112, .5),
        line(120, 45, 120, 71, .5), line(120, 91, 120, 112, .5),
        battery_v(42, 78, .5),
        res_h(80, 45, 20, 3.6, .5), res_h(160, 45, 20, 3.6, .5),
        res_v(120, 81, 20, 3.6, .5),
        dot(120, 45, 2.2, .8, ACCENT),
        arrow(137, 32, 125, 43, .7, ACCENT, 3.5),
        arrow_arc(80, 80, 17, .6, 5.3, .4, color=ACCENT),
        arrow_arc(160, 80, 17, .6, 5.3, .4, color=ACCENT),
        amp(81, 83, 'M1', .5), amp(161, 83, 'M2', .5),
        amp(142, 34, 'N', .5, 5.6, '.08em'),
    ])


# --------------------------------------------------------------------------
# 2. source-transform
# --------------------------------------------------------------------------

def source_transform():
    return ''.join([
        line(30, 48, 52, 48, .5), line(76, 48, 96, 48, .5),
        line(30, 108, 96, 108, .5),
        line(30, 48, 30, 69, .5), line(30, 87, 30, 108, .5),
        battery_v(30, 78, .5),
        res_h(64, 48, 24, 3.6, .5),
        line(96, 48, 106, 48, .5), line(96, 108, 106, 108, .5),
        dot(106, 48, 1.8, .55), dot(106, 108, 1.8, .55),
        line(146, 48, 166, 48, .5), line(190, 48, 210, 48, .5),
        line(146, 108, 210, 108, .5),
        line(210, 48, 210, 108, .5),
        line(146, 48, 146, 70, .5), line(146, 86, 146, 108, .5),
        circle(146, 78, 8, .55),
        arrow(146, 84, 146, 72, .7, INK, 3.5),
        res_h(178, 48, 24, 3.6, .5),
        dot(136, 48, 1.8, .55), dot(136, 108, 1.8, .55),
        arrow(113, 78, 132, 78, .7, ACCENT, 4),
        amp(22, 82, 'V', .45, 5.6, '.08em'),
        amp(158, 82, 'I', .45, 5.6, '.08em'),
    ])


# --------------------------------------------------------------------------
# 3. rc-charge
# --------------------------------------------------------------------------

def rc_charge():
    x0, xa, base, top = 52, 130, 112, 50
    tau = 26.0
    pts = []
    for i in range(31):
        t = i / 30 * 3
        pts.append((x0 + t * tau, base - (base - top) * (1 - math.exp(-t))))
    start = pts[-1][1]
    for i in range(1, 31):
        t = i / 30 * 3
        pts.append((xa + t * tau, start + (base - start) * (1 - math.exp(-t))))
    return ''.join([
        axis(x0, 118, 216, 118, .4), axis(x0, 118, x0, 32, .4),
        line(x0, top, 212, top, .28, dash='3 4'),
        line(x0 + tau, 118, x0 + tau, 74, .3, dash='3 4'),
        curve(pts, .85, ACCENT, w=1.3),
        dot(x0 + tau, base - (base - top) * .632, 2.2, .75, ACCENT),
        amp(44, 38, 'V', .45, 5.6, '.08em'),
        amp(212, 130, 't', .45, 5.6, '.08em'),
        text(x0 + tau, 133, '\u03c4', 'middle', .55, 6.2, '.04em', ACCENT),
    ])


# --------------------------------------------------------------------------
# 4. resonance-curve
# --------------------------------------------------------------------------

def resonance_curve():
    x0, x1, base, top = 52, 206, 118, 32
    f0 = .5
    sharp, broad = [], []
    for i in range(81):
        r = i / 80 * 1.05
        x = x0 + (x1 - x0) * (r / 1.05)
        sharp.append((x, base - (base - top) / (1 + ((r - f0) / .045) ** 2)))
        broad.append((x, base - (base - top) * .55 / (1 + ((r - f0) / .14) ** 2)))
    xf = x0 + (x1 - x0) * (f0 / 1.05)
    return ''.join([
        axis(x0, base, x1, base, .4), axis(x0, base, x0, top, .4),
        curve(broad, .3, INK, dash='3 4'),
        curve(sharp, .9, ACCENT, w=1.4),
        line(xf, base, xf, top + 4, .25, dash='2 4'),
        amp(44, 38, 'A', .45, 5.6, '.08em'),
        text(xf, 131, 'f0', 'middle', .5, 6.2, '.04em', ACCENT),
    ])


# --------------------------------------------------------------------------
# 5. filter-response
# --------------------------------------------------------------------------

def filter_response():
    panels = [
        (40, 72, 'lp', 'LOW'),
        (136, 72, 'hp', 'HIGH'),
        (40, 120, 'bp', 'BAND'),
        (136, 120, 'notch', 'NOTCH'),
    ]
    out = []
    for px, base, kind, name in panels:
        w, h = 72, 32
        top = base - h
        out += [line(px, base, px + w, base, .3), line(px, base, px, top, .3)]
        pts = []
        for i in range(25):
            t = i / 24
            if kind == 'lp':
                g = 1 / math.sqrt(1 + (t / .34) ** 2)
            elif kind == 'hp':
                g = (t / .34) / math.sqrt(1 + (t / .34) ** 2)
            elif kind == 'bp':
                g = math.exp(-((t - .52) / .19) ** 2)
            else:
                g = 1 - .93 * math.exp(-((t - .52) / .11) ** 2)
            pts.append((px + t * w, base - 2 - g * (h - 5)))
        out.append(curve(pts, .8, ACCENT, w=1.2))
        out.append(amp(px + w / 2, base + 11, name, .45))
    return ''.join(out)


# --------------------------------------------------------------------------
# 6. rectifier-waveforms
# --------------------------------------------------------------------------

def rectifier_waveforms():
    x0, x1 = 58, 204

    def hw(p):
        return max(0.0, math.sin(p))

    return ''.join([
        line(x0, 48, x1, 48, .22, dash='2 4'),
        _trace(math.sin, x0, x1, 48, 13, 2, 80),
        line(x0, 86, x1, 86, .22, dash='2 4'),
        _trace(hw, x0, x1, 86, 13, 2, 80),
        line(x0, 124, x1, 124, .22, dash='2 4'),
        _trace(lambda p: abs(math.sin(p)), x0, x1, 124, 13, 2, 80, ACCENT),
        amp(34, 51, 'AC', .45), amp(34, 89, 'HW', .45), amp(34, 127, 'FW', .45),
    ])


# --------------------------------------------------------------------------
# 7. clipper-clamper
# --------------------------------------------------------------------------

def clipper_clamper():
    return ''.join([
        line(62, 44, 200, 44, .22, dash='2 4'),
        _trace(math.sin, 62, 200, 44, 12, 2, 80),
        line(62, 84, 200, 84, .22, dash='2 4'),
        _trace(lambda p: max(-.5, min(.5, math.sin(p))), 62, 200, 84, 24, 2, 80, ACCENT),
        line(62, 124, 200, 124, .22, dash='2 4'),
        _trace(lambda p: 1 + math.sin(p), 62, 200, 124, 10, 2, 80, ACCENT),
        amp(34, 47, 'IN', .45), amp(34, 87, 'CLIP', .45), amp(34, 127, 'CLAMP', .45),
    ])


# --------------------------------------------------------------------------
# 8. bjt-biasing
# --------------------------------------------------------------------------

def bjt_biasing():
    return ''.join([
        line(100, 30, 205, 30, .5),
        res_v(100, 44.5, 29, 3.6, .5),
        line(100, 59, 100, 78, .5),
        res_v(100, 91.5, 27, 3.6, .5),
        gnd(100, 105, 13),
        line(40, 78, 59, 78, .5),
        cap_h(72, 78, 7, 2.6, .55),
        line(85, 78, 100, 78, .5),
        line(100, 78, 136, 78, 1.2, color=ACCENT),
        dot(100, 78, 2.0, .8, ACCENT),
        npn(155, 78, 15, 1, .5),
        res_v(160, 43, 26, 3.6, .5),
        line(160, 56, 160, 62, .5),
        res_v(160, 105, 14, 3.6, .5),
        line(160, 94, 160, 98, .5),
        gnd(160, 112, 12),
        line(160, 62, 184, 62, .5),
        cap_h(191, 62, 7, 2.6, .55),
        line(198, 62, 208, 62, .5),
        dot(160, 62, 1.8, .55),
        amp(201, 24, 'VCC', .5),
        amp(169, 41, 'RC', .45, 5.6, '.08em'),
        amp(169, 106, 'RE', .45, 5.6, '.08em'),
        amp(36, 72, 'IN', .45, 5.6, '.08em'),
        amp(208, 55, 'OUT', .45, 5.6, '.08em'),
    ])


# --------------------------------------------------------------------------
# 9. mosfet-curves
# --------------------------------------------------------------------------

def mosfet_curves():
    x0, y0, x1, yt = 52, 118, 208, 32
    levels = [(.30, .42), (.48, .55), (.66, .7), (.84, .92)]
    out = [axis(x0, y0, x1, y0, .4), axis(x0, y0, x0, yt, .4)]
    for k, (sat, o) in enumerate(levels):
        pts = []
        for i in range(26):
            v = i / 25 * 3
            pts.append((x0 + (x1 - x0) * v / 3.15,
                        y0 - (y0 - yt) * sat * v / (v + .28)))
        if k == 3:
            out.append(curve(pts, .9, ACCENT, w=1.4))
        else:
            out.append(curve(pts, .42 + k * .06))
    out += [amp(44, 38, 'ID', .45), amp(200, 131, 'VDS', .45)]
    return ''.join(out)


# --------------------------------------------------------------------------
# 10. opamp-inverting
# --------------------------------------------------------------------------

def opamp_inverting():
    return ''.join([
        opamp(135, 75, 70, 54, .55),
        line(36, 63, 52, 63, .5),
        res_h(65, 63, 26, 3.6, .5),
        line(78, 63, 100, 63, .5),
        dot(92, 63, 2.2, .8, ACCENT),
        line(92, 63, 92, 70, .35, 1, dash='2 3', color=ACCENT),
        line(92, 63, 92, 30, .5),
        res_h(145, 30, 26, 3.6, .5),
        line(92, 30, 132, 30, .5), line(158, 30, 198, 30, .5),
        line(198, 30, 198, 75, .5),
        line(198, 75, 170, 75, .5),
        line(170, 75, 208, 75, .5),
        dot(198, 75, 1.8, .55),
        line(100, 87, 84, 87, .5), line(84, 87, 84, 92, .5), gnd(84, 92, 12),
        amp(145, 23, 'RF', .45, 5.6, '.08em'),
        amp(65, 55, 'R1', .45, 5.6, '.08em'),
        amp(38, 56, 'VIN', .45, 5.6, '.08em'),
        text(92, 78, '0V', 'middle', .55, 5.6, '.08em', ACCENT),
        amp(208, 68, 'VOUT', .45, 5.6, '.08em'),
        amp(108, 60, '\u2212', .4, 6.2, '.04em'),
        amp(108, 92, '+', .4, 6.2, '.04em'),
    ])


# --------------------------------------------------------------------------
# 11. opamp-integrator
# --------------------------------------------------------------------------

def opamp_integrator():
    return ''.join([
        opamp(135, 75, 70, 54, .55),
        line(36, 63, 52, 63, .5),
        res_h(65, 63, 26, 3.6, .5),
        line(78, 63, 100, 63, .5),
        dot(92, 63, 1.8, .55),
        line(92, 63, 92, 30, .5),
        line(92, 30, 132, 30, .5),
        cap_h(145, 30, 8, 2.6, .85, ACCENT),
        line(158, 30, 198, 30, .5),
        line(198, 30, 198, 75, .5),
        line(198, 75, 170, 75, .5),
        line(170, 75, 208, 75, .5),
        dot(198, 75, 1.8, .55),
        line(100, 87, 84, 87, .5), line(84, 87, 84, 92, .5), gnd(84, 92, 12),
        text(145, 20, 'C', 'middle', .55, 6.2, '.06em', ACCENT),
        amp(65, 55, 'R', .45, 5.6, '.08em'),
        amp(38, 56, 'VIN', .45, 5.6, '.08em'),
        amp(208, 68, 'VOUT', .45, 5.6, '.08em'),
        amp(108, 60, '\u2212', .4, 6.2, '.04em'),
        amp(108, 92, '+', .4, 6.2, '.04em'),
    ])


# --------------------------------------------------------------------------
# 12. differential-pair
# --------------------------------------------------------------------------

def differential_pair():
    return ''.join([
        line(65, 32, 195, 32, .5),
        line(100, 32, 100, 40, .5), line(160, 32, 160, 40, .5),
        res_v(100, 49, 18, 3.6, .5),
        res_v(160, 49, 18, 3.6, .5),
        line(75, 76, 60, 76, .5), line(185, 76, 200, 76, .5),
        npn(95, 76, 14, 1, .5), npn(165, 76, 14, -1, .5),
        line(100, 58, 100, 62, .5), line(160, 58, 160, 62, .5),
        line(100, 90, 100, 98, .5), line(160, 90, 160, 98, .5),
        line(100, 98, 160, 98, .5),
        line(130, 98, 130, 101, .5),
        circle(130, 108, 7, .7, ACCENT),
        arrow(130, 102, 130, 114, .8, ACCENT, 3.5),
        gnd(130, 115, 12),
        amp(199, 27, 'VCC', .5),
        amp(140, 111, 'I0', .45, 5.6, '.08em'),
        amp(56, 80, '+', .45, 6.2, '.04em'),
        amp(204, 80, '\u2212', .45, 6.2, '.04em'),
    ])


# --------------------------------------------------------------------------
# 13. current-mirror
# --------------------------------------------------------------------------

def current_mirror():
    return ''.join([
        nmos(90, 78, -1, .5), nmos(155, 78, 1, .5),
        line(106, 78, 139, 78, .5),
        line(90, 58, 90, 46, .5), line(90, 46, 122, 46, .5),
        line(122, 46, 122, 78, .5),
        arrow(90, 28, 90, 44, .7, ACCENT, 3.5),
        line(155, 58, 155, 34, .5),
        arrow(155, 34, 176, 34, .65, INK, 3.5),
        line(70, 112, 170, 112, .5),
        line(90, 98, 90, 112, .5), line(155, 98, 155, 112, .5),
        gnd(120, 112, 12),
        dot(122, 78, 1.6, .5),
        amp(84, 26, 'IREF', .5, 5.6, '.08em'),
        text(182, 37, 'IOUT', 'start', .45, 5.6, '.08em'),
    ])


# --------------------------------------------------------------------------
# 14. cmos-layout
# --------------------------------------------------------------------------

def cmos_layout():
    return ''.join([
        rect(66, 38, 108, 34, 1, .3, dash='3 4'),
        rect(78, 46, 84, 18, 1, .4),
        rect(78, 86, 84, 18, 1, .4),
        line(118, 40, 118, 112, .85, 1.5, color=ACCENT),
        line(80, 30, 150, 30, .5),
        line(88, 30, 88, 55, .5),
        line(80, 118, 150, 118, .5),
        line(88, 118, 88, 95, .5),
        line(144, 55, 144, 95, .5),
        line(144, 76, 178, 76, .5),
        dot(88, 55, 1.9, .6), dot(144, 55, 1.9, .6),
        dot(88, 95, 1.9, .6), dot(144, 95, 1.9, .6),
        text(62, 44, 'N WELL', 'end', .45, 5.6, '.08em'),
        text(154, 27, 'VDD', 'start', .45, 5.6, '.08em'),
        text(154, 121, 'GND', 'start', .45, 5.6, '.08em'),
        text(110, 80, 'POLY', 'end', .5, 5.6, '.08em'),
        text(184, 79, 'OUT', 'start', .45, 5.6, '.08em'),
    ])


# --------------------------------------------------------------------------
# 15. stick-diagram
# --------------------------------------------------------------------------

def stick_diagram():
    return ''.join([
        line(80, 42, 200, 42, .55, 1.4),
        line(80, 116, 200, 116, .55, 1.4),
        line(80, 58, 160, 58, .4, 1.1, dash='4 3'),
        line(80, 100, 160, 100, .4, 1.1, dash='4 3'),
        line(120, 50, 120, 106, .85, 1.5, color=ACCENT),
        line(88, 42, 88, 58, .55),
        line(88, 100, 88, 116, .55),
        line(150, 58, 150, 100, .55),
        line(150, 79, 198, 79, .55),
        dot(88, 58, 1.9, .6), dot(88, 100, 1.9, .6),
        dot(150, 58, 1.9, .6), dot(150, 100, 1.9, .6),
        dot(150, 79, 1.9, .6),
        text(74, 38, 'VDD', 'end', .45, 5.6, '.08em'),
        text(74, 112, 'GND', 'end', .45, 5.6, '.08em'),
        text(124, 50, 'POLY', 'start', .55, 5.6, '.08em'),
        text(74, 54, 'DIFF', 'end', .4, 5.6, '.08em'),
        text(204, 74, 'OUT', 'start', .45, 5.6, '.08em'),
    ])


# --------------------------------------------------------------------------
# 16. transmission-gate
# --------------------------------------------------------------------------

def transmission_gate():
    return ''.join([
        line(34, 75, 44, 75, .5),
        dot(44, 75, 1.9, .55),
        line(44, 75, 72, 52, .5),
        line(44, 75, 72, 96, .5),
        line(72, 52, 78, 52, .5), line(72, 96, 78, 96, .5),
        fet_h(100, 52, 'up', True, .55, hot=True),
        fet_h(100, 96, 'down', False, .55, hot=True),
        line(122, 52, 156, 75, .5),
        line(122, 96, 156, 75, .5),
        line(156, 75, 204, 75, .5),
        dot(156, 75, 1.9, .55),
        text(30, 71, 'IN', 'end', .45, 5.6, '.08em'),
        text(208, 71, 'OUT', 'end', .45, 5.6, '.08em'),
        amp(100, 33, 'C', .5, 5.6, '.08em'),
        amp(100, 118, 'CN', .5, 5.6, '.08em'),
    ])


# --------------------------------------------------------------------------
# 17. adc-dac
# --------------------------------------------------------------------------

def adc_dac():
    pts = [(44, 106)]
    for k in range(8):
        x = 44 + k * 10.5
        y = 106 - k * 8
        pts += [(x + 1.5, y), (x + 10, y)]
    return ''.join([
        line(44, 118, 132, 118, .3), line(44, 34, 44, 118, .3),
        curve(pts, .85, ACCENT, w=1.3),
        text(44, 132, '3 BIT', 'start', .45, 5.6, '.08em'),
        arrow(134, 60, 146, 60, .5, INK, 3.5),
        line(148, 60, 158, 60, .5),
        res_h(166, 60, 16, 3.2, .5),
        line(174, 60, 187, 60, .5),
        res_h(195, 60, 16, 3.2, .5),
        line(203, 60, 214, 60, .5),
        line(148, 60, 148, 68, .5), res_v(148, 76, 16, 3.2, .5),
        line(148, 84, 148, 92, .5),
        line(179, 60, 179, 68, .5), res_v(179, 76, 16, 3.2, .5),
        line(179, 84, 179, 92, .5),
        line(142, 92, 186, 92, .4),
        gnd(164, 92, 11),
        arrow(214, 60, 214, 42, .6, INK, 3.5),
        amp(198, 106, 'R-2R', .45, 5.6, '.08em'),
    ])


# --------------------------------------------------------------------------
# 18. pll
# --------------------------------------------------------------------------

def pll():
    return ''.join([
        arrow(20, 70, 36, 70, .6, INK, 3.5),
        rect(38, 56, 47, 28, 2, .5),
        rect(95, 56, 47, 28, 2, .5),
        rect(153, 56, 47, 28, 2, .5),
        line(85, 70, 94, 70, .5), line(142, 70, 152, 70, .5),
        arrow(200, 70, 218, 70, .6, INK, 3.5),
        path('M176,84 L176,112 L62,112 L62,85', .75, 1.2, color=ACCENT),
        arrow(62, 92, 62, 85, .75, ACCENT, 3.5),
        amp(61, 73, 'PD', .55), amp(118, 73, 'LF', .55), amp(176, 73, 'VCO', .55),
        amp(24, 62, 'IN', .45, 5.6, '.08em'),
    ])


# --------------------------------------------------------------------------
# 19. oscillator-loop
# --------------------------------------------------------------------------

def oscillator_loop():
    return ''.join([
        path('M92,48 L148,72 L92,96 Z', .55),
        line(50, 72, 92, 72, .5),
        line(148, 72, 186, 72, .5),
        dot(76, 72, 1.8, .55), dot(186, 72, 1.8, .55),
        line(186, 72, 186, 34, .5),
        line(186, 34, 76, 34, .5),
        arrow(76, 34, 76, 70, .75, ACCENT, 3.5),
        line(186, 72, 186, 80, .5),
        line(178, 80, 196, 80, .5),
        line(178, 80, 178, 84, .5), ind_v(178, 94, 20, .55),
        line(178, 104, 178, 108, .5),
        line(196, 80, 196, 84, .5), cap_v(196, 93, 7, 2.6, .55),
        line(196, 100, 196, 108, .5),
        line(178, 108, 196, 108, .5), line(187, 108, 187, 114, .5),
        gnd(187, 114, 12),
        amp(112, 76, 'A', .55, 6.2, '.06em'),
        text(170, 97, 'L', 'end', .45, 5.6, '.08em'),
        text(204, 97, 'C', 'start', .45, 5.6, '.08em'),
        text(68, 60, '+', 'middle', .7, 6.4, '.04em', ACCENT),
    ])


# --------------------------------------------------------------------------
# 20. power-amp
# --------------------------------------------------------------------------

def power_amp():
    def half(p):
        s = math.sin(p)
        if abs(s) < .24:
            return 0.0
        return math.copysign(abs(s) - .24, s) / .76

    return ''.join([
        line(36, 76, 112, 76, .25, dash='2 4'),
        _trace(math.sin, 40, 108, 76, 22, 1.5, 60),
        line(130, 76, 206, 76, .25, dash='2 4'),
        _trace(half, 134, 202, 76, 22, 1.5, 80, ACCENT),
        amp(76, 44, 'CLASS A', .45),
        amp(168, 44, 'CLASS B', .45),
    ])


# --------------------------------------------------------------------------
# 21. regulator
# --------------------------------------------------------------------------

def regulator():
    return ''.join([
        line(30, 48, 78, 48, .5),
        rect(78, 34, 64, 28, 2, .5),
        text(110, 51, 'SERIES PASS', 'middle', .6, 5.6, '.08em'),
        line(142, 48, 210, 48, .5),
        line(110, 62, 110, 72, .5),
        path('M96,96 L124,96 L110,72 Z', .75, color=ACCENT),
        line(56, 104, 66, 104, .5),
        path('M66,99 L66,109 L74,104 Z', .5),
        line(74, 99, 74, 109, .5),
        line(74, 104, 100, 104, .5), line(100, 104, 100, 96, .5),
        line(185, 48, 185, 74, .5), res_v(185, 82, 16, 3.6, .5),
        line(185, 90, 185, 104, .5),
        line(185, 104, 120, 104, .5), line(120, 104, 120, 96, .5),
        dot(185, 104, 1.6, .5),
        res_v(185, 111, 14, 3.4, .5), gnd(185, 118, 12),
        text(34, 42, 'VIN', 'start', .45, 5.6, '.08em'),
        text(206, 42, 'VOUT', 'end', .45, 5.6, '.08em'),
        text(48, 108, 'REF', 'end', .5, 5.6, '.08em'),
    ])


# --------------------------------------------------------------------------
# 22. s-parameters
# --------------------------------------------------------------------------

def s_parameters():
    return ''.join([
        rect(100, 50, 40, 50, 2, .45),
        line(38, 75, 100, 75, .5),
        line(140, 75, 202, 75, .5),
        arrow(54, 66, 96, 66, .75, ACCENT, 3.5),
        arrow(96, 84, 54, 84, .6),
        arrow(186, 66, 144, 66, .75, ACCENT, 3.5),
        arrow(144, 84, 186, 84, .6),
        amp(54, 60, 'A1', .5, 5.6, '.06em'),
        amp(54, 94, 'B1', .5, 5.6, '.06em'),
        text(186, 60, 'A2', 'end', .5, 5.6, '.06em'),
        text(186, 94, 'B2', 'end', .5, 5.6, '.06em'),
        amp(120, 78, '2-PORT', .45, 5.6, '.08em'),
    ])


# --------------------------------------------------------------------------
# 23. bridge-circuit
# --------------------------------------------------------------------------

def bridge_circuit():
    T, R, B, L = (120, 32), (188, 75), (120, 118), (52, 75)
    return ''.join([
        res_arm(T, L), res_arm(T, R), res_arm(L, B), res_arm(R, B),
        line(52, 75, 113, 75, .5), line(127, 75, 188, 75, .5),
        circle(120, 75, 7, .55),
        line(117, 81, 123, 70, .55),
        path('M120,32 L120,22 L30,22 L30,66 M30,84 L30,128 L120,128 L120,118', .5),
        battery_v(30, 75, .55),
        text(120, 94, 'G', 'middle', .55, 6.2, '.06em', ACCENT),
        text(42, 84, 'E', 'start', .45, 5.6, '.08em'),
    ])


# --------------------------------------------------------------------------
# 24. max-power
# --------------------------------------------------------------------------

def max_power():
    x0, x1, y0, yt = 52, 200, 116, 32
    span = 3.6
    pts = []
    for i in range(61):
        r = i / 60 * span
        p = 4 * r / (1 + r) ** 2
        pts.append((x0 + (x1 - x0) * r / span, y0 - (y0 - yt - 10) * p))
    xp = x0 + (x1 - x0) / span
    return ''.join([
        axis(x0, y0, 208, y0, .4), axis(x0, y0, x0, yt, .4),
        curve(pts, .9, ACCENT, w=1.4),
        line(xp, y0, xp, yt + 9, .28, dash='2 4'),
        dot(xp, yt + 10, 2.2, .8, ACCENT),
        amp(44, 38, 'P', .45, 5.6, '.08em'),
        amp(197, 131, 'RL', .45, 5.6, '.08em'),
        text(xp, 131, 'RTH', 'middle', .5, 5.6, '.08em', ACCENT),
        text(xp + 8, 32, 'PMAX', 'start', .4, 5.6, '.08em'),
    ])


DIAGRAMS = {
    'node-mesh': node_mesh,
    'source-transform': source_transform,
    'rc-charge': rc_charge,
    'resonance-curve': resonance_curve,
    'filter-response': filter_response,
    'rectifier-waveforms': rectifier_waveforms,
    'clipper-clamper': clipper_clamper,
    'bjt-biasing': bjt_biasing,
    'mosfet-curves': mosfet_curves,
    'opamp-inverting': opamp_inverting,
    'opamp-integrator': opamp_integrator,
    'differential-pair': differential_pair,
    'current-mirror': current_mirror,
    'cmos-layout': cmos_layout,
    'stick-diagram': stick_diagram,
    'transmission-gate': transmission_gate,
    'adc-dac': adc_dac,
    'pll': pll,
    'oscillator-loop': oscillator_loop,
    'power-amp': power_amp,
    'regulator': regulator,
    's-parameters': s_parameters,
    'bridge-circuit': bridge_circuit,
    'max-power': max_power,
}
