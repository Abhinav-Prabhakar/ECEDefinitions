"""Diagram family: signals, systems and communications."""
import math

from .base import *

# The preview sheet does not define the theme variable; keep the accent visible
# there while still following the page accent wherever it is set.
ACCENT = 'var(--accent,#5b6ee1)'


# ---------------------------------------------------------------------------
# local helpers
# ---------------------------------------------------------------------------

def _trace(fn, x0, x1, n=64):
    return curve([(x0 + (x1 - x0) * i / n, fn(i / n)) for i in range(n + 1)])


def _carrier(x0, x1, cy, cycles, amp, phase=0.0, color=INK, o=.7):
    return curve([(x0 + (x1 - x0) * i / 70,
                   cy - amp * math.sin(2 * math.pi * cycles * i / 70 + phase))
                  for i in range(71)], o, color, w=1)


def _label(x, y, s, anchor='middle', o=.5, size=5.6):
    return text(x, y, s, anchor, o, size)


def _xmark(x, y, r=5, o=.8, color=INK):
    return path(f'M{x-r} {y-r} L{x+r} {y+r} M{x+r} {y-r} L{x-r} {y+r}', o, color=color)


# ---------------------------------------------------------------------------
# basic signal operations
# ---------------------------------------------------------------------------

def signal_ops():
    out = []
    for c, kind, lab in [(56, 'shift', 'SHIFT'), (120, 'scale', 'SCALE'),
                         (184, 'reverse', 'REVERSE')]:
        out.append(line(c - 28, 100, c + 28, 100, .28))
        out.append(path(f'M{c-18} 100 L{c-10} 66 L{c+2} 66 L{c+18} 100', .28, 1, '2 3'))
        if kind == 'shift':
            d = f'M{c-8} 100 L{c} 66 L{c+12} 66 L{c+28} 100'
        elif kind == 'scale':
            d = f'M{c-9} 100 L{c-6} 50 L{c+2} 50 L{c+9} 100'
        else:
            d = f'M{c-18} 100 L{c-2} 66 L{c+10} 66 L{c+18} 100'
        out.append(path(d, .8, 1.25, color=ACCENT))
        out.append(amp(c, 120, lab, o=.5))
    return ''.join(out)


def step_impulse():
    return ''.join([
        axis(24, 104, 112, 104, .4),
        line(24, 104, 24, 44, .28),
        axis(132, 104, 216, 104, .4),
        line(132, 104, 132, 44, .28),
        path('M24 104 H68 V52 H108', .85, 1.3),
        arrow(174, 104, 174, 52, .95, ACCENT, 4),
        dot(174, 104, 2, .55),
        amp(66, 122, 'STEP', o=.5),
        amp(174, 122, 'IMPULSE', o=.5),
        amp(110, 112, 'T', o=.35),
        amp(214, 112, 'T', o=.35),
    ])


def even_odd():
    out = []
    c0, c1, c2 = 46, 120, 194
    out.append(line(c0 - 28, 96, c0 + 28, 96, .28))
    out.append(line(c0 - 24, 118, c0 - 24, 50, .38))
    out.append(curve([(c0 - 24, 96), (c0 - 19, 96), (c0 - 16, 62), (c0 - 13, 76),
                      (c0 - 9, 86), (c0 - 4, 92), (c0 + 2, 95), (c0 + 10, 96),
                      (c0 + 26, 96)], .75))
    out.append(line(c1 - 26, 96, c1 + 26, 96, .28))
    out.append(line(c1, 118, c1, 64, .38))
    out.append(curve([(c1 - 26, 96), (c1 - 20, 95), (c1 - 14, 92), (c1 - 8, 86),
                      (c1 - 4, 80), (c1, 78), (c1 + 4, 80), (c1 + 8, 86),
                      (c1 + 14, 92), (c1 + 20, 95), (c1 + 26, 96)], .8, ACCENT))
    out.append(line(c2 - 26, 96, c2 + 26, 96, .28))
    out.append(line(c2, 118, c2, 64, .38))
    out.append(curve([(c2 - 26, 96), (c2 - 18, 96), (c2 - 12, 100), (c2 - 6, 108),
                      (c2 - 2, 113), (c2, 114)], .8, ACCENT))
    out.append(curve([(c2, 78), (c2 + 2, 80), (c2 + 7, 86), (c2 + 13, 92),
                      (c2 + 20, 95), (c2 + 26, 96)], .8, ACCENT))
    out.append(line(c2, 78, c2, 114, .5, 1, '2 3', ACCENT))
    out.append(amp(83, 90, '=', o=.55, size=10, ls='0'))
    out.append(amp(157, 90, '+', o=.55, size=10, ls='0'))
    out.append(amp(c0, 136, 'X(T)', o=.5))
    out.append(amp(c1, 136, 'EVEN', o=.55))
    out.append(amp(c2, 136, 'ODD', o=.55))
    return ''.join(out)


def aliasing():
    x0, x1, y0, a = 28, 212, 78, 26
    dots = [dot(x0 + (x1 - x0) * k / 10,
                y0 - a * math.sin(2 * math.pi * 7 * k / 10), 2, .55)
            for k in range(11)]
    return ''.join([
        line(24, y0, 216, y0, .18, 1, '2 4'),
        sine(x0, x1, y0, a, 7, .5),
        sine(x0, x1, y0, -a, 3, .9, ACCENT),
        *dots,
        line(30, 26, 44, 26, .5),
        _label(50, 28, 'TRUE', 'start', .45),
        line(30, 38, 44, 38, .9, 1, color=ACCENT),
        _label(50, 40, 'ALIAS', 'start', .5),
        axis(24, 124, 216, 124, .3),
        amp(216, 130, 'T', o=.4),
    ])


def quantization():
    x0, x1 = 34, 206
    levels = [112, 96, 80, 64, 48]
    out = [axis(x0, 120, x1 + 8, 120, .4), axis(x0, 120, x0, 34, .4)]
    out += [line(x0, y, x1, y, .16, 1, '2 4') for y in levels]
    out.append(path(f'M{x0} 118 L{x1} {levels[-1]}', .55))
    out.append(path('M34 112 H68.4 V96 H102.8 V80 H137.2 V64 H171.6 V48 H206',
                    .9, 1.3, color=ACCENT))
    out.append(line(36, 22, 50, 22, .45))
    out.append(_label(56, 24, 'CONTINUOUS', 'start', .42))
    out.append(line(36, 32, 50, 32, .85, 1, color=ACCENT))
    out.append(_label(56, 34, 'QUANTISED', 'start', .48))
    out.append(bracket(210, 96, 112, 'Δ', .4))
    return ''.join(out)


def pcm():
    dots = []
    for t in (.1, .34, .58, .82):
        x = 34 + 42 * t
        dots.append(dot(x, 86 - 14 * math.sin(4 * math.pi * t), 1.8, .75, ACCENT))
    return ''.join([
        line(34, 86, 76, 86, .28),
        sine(34, 76, 86, 14, 2, .55),
        *dots,
        line(98, 90, 142, 90, .28),
        path('M98 90 V80 H109 V70 H120 V60 H131 V50 H142', .8, 1.2),
        path('M162 54 H173 V72 H184 V54 H206', .8, 1.2),
        path('M173 48 V78 M184 48 V78 M195 48 V78', .16, 1, '2 3'),
        amp(56, 112, 'SAMPLE', o=.55),
        amp(120, 112, 'QUANTISE', o=.55),
        amp(184, 112, 'ENCODE', o=.55),
        arrow(82, 66, 94, 66, .4, head=3),
        arrow(146, 66, 158, 66, .4, head=3),
    ])


# ---------------------------------------------------------------------------
# baseband and coded transmission
# ---------------------------------------------------------------------------

def line_coding():
    return ''.join([
        path('M114.5 26 V142 M147 26 V142 M179.5 26 V142', .14, 1, '2 4'),
        path('M82 64 H212 M82 100 H212 M82 136 H212', .1, 1, '1 4'),
        path('M82 38 H114.5 V64 H147 V38 H212', .55),
        path('M82 74 H98.25 V100 H147 V74 H163.25 V100 H179.5 V74 H195.75 V100 H212',
             .55),
        path('M82 110 H98.25 V136 H130.75 V110 H163.25 V136 H179.5 V110 H195.75 V136 H212',
             .85, 1.2, color=ACCENT),
        _label(76, 60, 'NRZ', 'end', .5),
        _label(76, 96, 'RZ', 'end', .5),
        _label(76, 132, 'MANCHESTER', 'end', .55),
    ])


def eye_diagram():
    out = [line(48, 46, 196, 46, .5), line(48, 104, 196, 104, .5)]

    def tr(xc, up):
        y0, y1 = (104, 46) if up else (46, 104)
        pts = []
        for i in range(49):
            x = 48 + 148 * i / 48
            t = .5 + .5 * math.tanh((x - xc) / 6)
            pts.append((x, y0 + (y1 - y0) * t))
        return curve(pts, .55)

    out += [tr(88, True), tr(88, False), tr(156, True), tr(156, False)]
    out.append(line(122, 34, 122, 118, .7, 1, '2 3', ACCENT))
    out.append(amp(122, 130, 'SAMPLE', o=.55))
    out.append(amp(139, 78, 'EYE', o=.4))
    out.append(axis(40, 118, 204, 118, .28))
    out.append(amp(210, 122, 'T', o=.35))
    return ''.join(out)


def constellation():
    out = []
    for c, label in [(54, 'BPSK'), (120, 'QPSK'), (186, '16-QAM')]:
        out.append(line(c - 21, 72, c + 21, 72, .28))
        out.append(line(c, 51, c, 93, .28))
        out.append(amp(c, 112, label, o=.45))
    out.append(dot(42, 72, 2.6, .7))
    out.append(dot(66, 72, 2.6, .7))
    for dx, dy in [(-9, -9), (-9, 9), (9, -9), (9, 9)]:
        out.append(dot(120 + dx, 72 + dy, 2.4, .85, ACCENT))
    for dx in (-10.5, -3.5, 3.5, 10.5):
        for dy in (-10.5, -3.5, 3.5, 10.5):
            out.append(dot(186 + dx, 72 + dy, 1.8, .6))
    return ''.join(out)


def ask_fsk_psk():
    x0, x1 = 74, 214
    bw = (x1 - x0) / 3
    out = []
    rows = [('ASK', 40), ('FSK', 76), ('PSK', 112)]
    for lab, cy in rows:
        out.append(line(70, cy, 218, cy, .15, 1, '2 4'))
        out.append(_label(64, cy + 2, lab, 'end', .55))
    for i in range(3):
        a, b = x0 + i * bw, x0 + (i + 1) * bw
        out.append(_carrier(a, b, 40, 3, 11 if i != 1 else 3, color=ACCENT, o=.75))
        out.append(_carrier(a, b, 76, 3 if i != 1 else 5, 10, color=ACCENT, o=.75))
        out.append(_carrier(a, b, 112, 3, 10, math.pi if i == 1 else 0,
                            color=ACCENT, o=.75))
    out.append(path(f'M{x0+bw:.1f} 26 V126 M{x0+2*bw:.1f} 26 V126', .15, 1, '2 4'))
    return ''.join(out)


def fm_modulation():
    pts = []
    n = 140
    for i in range(n + 1):
        t = i / n
        ph = 2 * math.pi * 10 * t - 3.0 * math.sin(2 * math.pi * t)
        pts.append((30 + 184 * t, 78 - 22 * math.sin(ph)))
    return ''.join([
        line(28, 78, 212, 78, .15, 1, '2 4'),
        path('M28 56 H214 M28 100 H214', .28, 1, '3 4'),
        curve(pts, .85, ACCENT, w=1.15),
        amp(120, 44, 'CONSTANT ENVELOPE', o=.4),
        sine(32, 212, 120, 4, 1, .3),
        amp(60, 110, 'MODULATING', o=.35),
        axis(28, 132, 214, 132, .3),
        amp(218, 136, 'T', o=.4),
        amp(34, 32, 'FM', o=.55),
    ])


# ---------------------------------------------------------------------------
# radio and antennas
# ---------------------------------------------------------------------------

def if_filter():
    return ''.join([
        line(30, 44, 210, 44, .3),
        line(100, 44, 100, 22, .8),
        line(148, 44, 148, 24, .3, 1, '2 3'),
        line(30, 82, 210, 82, .3),
        line(124, 82, 124, 58, .8),
        line(30, 118, 210, 118, .3),
        line(76, 118, 76, 94, .95, 1.4, color=ACCENT),
        line(148, 118, 148, 102, .25, 1, '2 3'),
        path('M143 97 L153 107', .55),
        _label(26, 38, 'RF', 'start', .5),
        _label(26, 76, 'LO', 'start', .5),
        _label(26, 112, 'IF', 'start', .55),
        amp(148, 18, 'IMAGE', o=.42),
        amp(216, 121, 'F', o=.35),
    ])


def antenna_pattern():
    cx, cy, r = 120, 118, 76
    lobe = []
    for i in range(49):
        a = -math.pi + math.pi * i / 48
        rr = r * math.cos(a + math.pi / 2) ** 2
        lobe.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    half = .57
    rad = r * math.cos(half) ** 2
    return ''.join([
        line(36, cy, 204, cy, .16, 1, '2 4'),
        line(36, cy - 4, 36, cy, .3),
        line(204, cy - 4, 204, cy, .3),
        curve(lobe, .85, ACCENT, w=1.1),
        line(cx, cy, cx - rad * math.sin(half), cy - rad * math.cos(half), .25, 1, '3 4'),
        line(cx, cy, cx + rad * math.sin(half), cy - rad * math.cos(half), .25, 1, '3 4'),
        arrow_arc(cx, cy, 54, -math.pi / 2 - half, -math.pi / 2 + half, .45, INK, 3),
        amp(cx, 52, 'HPBW', o=.5),
        amp(cx, 140, 'MAIN LOBE', o=.42),
        dot(cx, cy, 2.2, .5),
    ])


def antenna_array():
    out = [line(32, 116, 88, 116, .4)]
    for x in (32, 46, 60, 74, 88):
        out.append(line(x, 96, x, 116, .7))
    out.append(dot(60, 116, 1.8, .5))
    out.append(path('M32 124 V132 M46 124 V132', .3))
    out.append(line(32, 128, 46, 128, .3))
    out.append(amp(39, 141, 'D', o=.45))

    cx, cy, r = 166, 118, 64

    def petal(ang, half, rad, o, color=INK):
        pts = []
        for i in range(21):
            d = -half + 2 * half * i / 20
            rr = rad * math.exp(-(d / (half * .5)) ** 2)
            pts.append((cx + rr * math.cos(ang + d), cy + rr * math.sin(ang + d)))
        return curve(pts, o, color, w=1)

    out.append(petal(-math.pi / 2, .62, r, .85, ACCENT))
    out.append(line(cx, 44, cx, 118, .16, 1, '2 4'))
    out.append(petal(-math.pi / 2 - .9, .36, 26, .4))
    out.append(petal(-math.pi / 2 + .9, .36, 26, .4))
    out.append(amp(60, 146, 'ELEMENTS', o=.42))
    out.append(amp(166, 146, 'MAIN LOBE', o=.42))
    return ''.join(out)


def link_budget():
    return ''.join([
        rect(24, 54, 42, 28, 2, .6),
        amp(45, 71, 'TX', o=.6),
        rect(174, 54, 42, 28, 2, .6),
        amp(195, 71, 'RX', o=.6),
        path('M90 88 V50 M90 50 L82 40 M90 50 L98 40', .65),
        path('M150 88 V50 M150 50 L142 40 M150 50 L158 40', .65),
        line(66, 68, 90, 68, .5),
        line(150, 68, 174, 68, .5),
        path('M96 52 Q 106 68 96 84', .3, 1, ACCENT),
        path('M104 46 Q 118 68 104 90', .45, 1, ACCENT),
        path('M112 40 Q 130 68 112 96', .6, 1, ACCENT),
        amp(120, 26, 'PATH LOSS', o=.5),
    ])


def nyquist_plot():
    return ''.join([
        axis(36, 80, 208, 80, .35),
        axis(120, 136, 120, 24, .35),
        path('M200 80 C 172 80 164 42 126 42 C 92 42 68 58 78 84 '
             'C 86 104 118 110 150 98', .9, 1.2, color=ACCENT),
        path('M145 93 L152 97 L146 102', .85, 1, color=ACCENT),
        _xmark(86, 80, 5, .9),
        dot(200, 80, 2, .5),
        _label(210, 84, 'RE', 'start', .4),
        _label(124, 20, 'IM', 'start', .4),
        amp(96, 72, '−1', o=.6),
    ])


def root_locus():
    return ''.join([
        axis(32, 86, 208, 86, .32),
        axis(118, 136, 118, 26, .32),
        _xmark(92, 64, 5, .75),
        _xmark(92, 108, 5, .75),
        circle(174, 64, 4.5, .8),
        circle(174, 108, 4.5, .8),
        path('M92 64 C 118 50 146 54 174 64', .7, 1.2, color=ACCENT),
        path('M92 108 C 118 122 146 118 174 108', .7, 1.2, color=ACCENT),
        path('M132 52 L140 55 L133 60', .6, 1, color=ACCENT),
        path('M132 120 L140 117 L133 112', .6, 1, color=ACCENT),
        _label(210, 90, 'RE', 'start', .4),
        _label(122, 22, 'IM', 'start', .4),
    ])


# ---------------------------------------------------------------------------
# system blocks
# ---------------------------------------------------------------------------

def pid():
    return ''.join([
        circle(44, 61, 9, .65),
        path('M38 55 L50 67 M50 55 L38 67', .55),
        amp(20, 65, 'R', o=.5),
        arrow(24, 61, 35, 61, .5, head=3),
        rect(72, 28, 34, 18, 2, .55),
        rect(72, 52, 34, 18, 2, .55),
        rect(72, 76, 34, 18, 2, .55),
        amp(89, 40, 'P', o=.6),
        amp(89, 64, 'I', o=.6),
        amp(89, 88, 'D', o=.6),
        path('M62 61 V37 M62 61 V85 M62 37 H72 M62 61 H72 M62 85 H72', .45),
        path('M106 37 H120 M106 61 H120 M106 85 H120 M120 37 V85', .45),
        dot(120, 61, 2, .5),
        arrow(120, 61, 134, 61, .5, head=3),
        rect(134, 47, 52, 28, 2, .6),
        amp(160, 64, 'G', o=.6),
        arrow(186, 61, 210, 61, .5, head=3),
        amp(218, 65, 'Y', o=.5),
        path('M196 61 V112 H44 V72', .35, 1, '3 4'),
        path('M40 77 L44 71 L48 77', .45),
        amp(36, 80, '−', o=.5),
    ])


def state_space():
    return ''.join([
        amp(18, 67, 'U', o=.5),
        arrow(24, 63, 34, 63, .5, head=3),
        rect(34, 50, 36, 26, 2, .55),
        amp(52, 66, 'B', o=.6),
        arrow(70, 63, 83, 63, .5, head=3),
        circle(92, 63, 9, .65),
        path('M92 58 V68 M87 63 H97', .5),
        arrow(101, 63, 116, 63, .5, head=3),
        rect(116, 50, 40, 26, 2, .6),
        amp(136, 66, '1/S', o=.6),
        arrow(156, 63, 206, 63, .5, head=3),
        amp(212, 67, 'X', o=.5),
        path('M198 63 V109 H156', .35, 1, '3 4'),
        path('M122 109 H92 V72', .35, 1, '3 4'),
        rect(122, 100, 34, 18, 2, .5),
        amp(139, 113, 'A', o=.6),
        path('M88 77 L92 71 L96 77', .45),
        amp(108, 56, 'Ẋ', o=.4),
    ])


def fir_filter():
    return ''.join([
        arrow(20, 42, 52, 42, .5, head=3),
        rect(54, 30, 28, 24, 2, .55),
        rect(92, 30, 28, 24, 2, .55),
        rect(130, 30, 28, 24, 2, .55),
        amp(68, 46, 'Z⁻¹', o=.5, size=5.6, ls='.04em'),
        amp(106, 46, 'Z⁻¹', o=.5, size=5.6, ls='.04em'),
        amp(144, 46, 'Z⁻¹', o=.5, size=5.6, ls='.04em'),
        line(82, 42, 92, 42, .45),
        line(120, 42, 130, 42, .45),
        line(158, 42, 166, 42, .45),
        dot(40, 42, 2, .6),
        dot(87, 42, 2, .6),
        dot(125, 42, 2, .6),
        dot(163, 42, 2, .6),
        path('M40 42 V104 M87 42 V104 M125 42 V104 M163 42 V104', .35),
        _label(45, 84, 'H₀', 'start', .5),
        _label(92, 84, 'H₁', 'start', .5),
        _label(130, 84, 'H₂', 'start', .5),
        _label(168, 84, 'H₃', 'start', .5),
        line(40, 104, 190, 104, .5),
        arrow(190, 104, 200, 104, .55, head=3),
        amp(208, 108, 'Y', o=.5),
    ])


def iir_filter():
    return ''.join([
        amp(14, 56, 'X', o=.5),
        arrow(20, 52, 39, 52, .5, head=3),
        circle(48, 52, 9, .65),
        path('M42 46 L54 58 M54 46 L42 58', .5),
        line(57, 52, 78, 52, .55),
        rect(78, 38, 28, 28, 2, .55),
        amp(92, 56, 'Z⁻¹', o=.5, size=5.6, ls='.04em'),
        line(106, 52, 122, 52, .55),
        rect(122, 38, 28, 28, 2, .55),
        amp(136, 56, 'Z⁻¹', o=.5, size=5.6, ls='.04em'),
        line(150, 52, 190, 52, .55),
        arrow(190, 52, 200, 52, .55, head=3),
        amp(206, 56, 'Y', o=.5),
        dot(114, 52, 2, .6),
        dot(158, 52, 2, .6),
        path('M114 52 V100 H108', .4),
        rect(74, 91, 34, 18, 2, .45),
        amp(91, 104, 'A₁', o=.55, size=5.6, ls='.04em'),
        path('M74 100 H48', .4),
        path('M158 52 V128 H108', .4),
        rect(74, 119, 34, 18, 2, .45),
        amp(91, 132, 'A₂', o=.55, size=5.6, ls='.04em'),
        path('M74 128 H48 V62', .4),
        path('M44 67 L48 61 L52 67', .45),
    ])


# ---------------------------------------------------------------------------
# transforms and multirate
# ---------------------------------------------------------------------------

def windowing():
    def win(fn, h):
        return curve([(62 + 116 * i / 48, 112 - h * fn(i / 48)) for i in range(49)], .8)
    return ''.join([
        axis(34, 112, 210, 112, .35),
        path('M62 112 V52 H178 V112', .25, 1, '2 3'),
        win(lambda t: .5 - .5 * math.cos(2 * math.pi * t), 58),
        curve([(62 + 116 * i / 48,
                112 - 52 * (.54 - .46 * math.cos(2 * math.pi * i / 48)))
               for i in range(49)], .55, INK, '3 4'),
        line(34, 24, 48, 24, .35, 1, '2 3'),
        _label(54, 26, 'RECT', 'start', .42),
        line(34, 33, 48, 33, .9, 1, color=ACCENT),
        _label(54, 35, 'HANN', 'start', .5),
        line(34, 42, 48, 42, .45, 1, '3 4'),
        _label(54, 44, 'HAMMING', 'start', .42),
    ])


def multirate():
    return ''.join([
        line(26, 72, 78, 72, .18),
        path('M30 72 L40 56 H62 L72 72', .55),
        arrow(72, 64, 84, 64, .35, head=3),
        rect(84, 52, 30, 22, 2, .55),
        amp(99, 67, '↓2', o=.6, size=5.8, ls='.02em'),
        arrow(114, 64, 126, 64, .35, head=3),
        line(122, 72, 214, 72, .18),
        path('M122 72 L132 54 H202 L212 72', .85, 1.2, color=ACCENT),

        line(26, 126, 78, 126, .18),
        path('M30 126 L40 110 H62 L72 126', .55),
        arrow(72, 118, 84, 118, .35, head=3),
        rect(84, 106, 30, 22, 2, .55),
        amp(99, 121, '↑2', o=.6, size=5.8, ls='.02em'),
        arrow(114, 118, 126, 118, .35, head=3),
        line(122, 126, 220, 126, .18),
        path('M126 126 L134 112 H150 L158 126', .3, 1, '2 3'),
        path('M158 126 L164 112 H186 L192 126', .9, 1.2, color=ACCENT),
        path('M192 126 L198 112 H216 L222 126', .3, 1, '2 3'),
        amp(205, 142, 'IMAGE', o=.4),
    ])


def fft_stages():
    ys = [20 + 14.5 * i for i in range(8)]
    out = [path(''.join(f'M36 {y:.1f} H204 ' for y in ys), .12)]
    cols = [40, 88, 144, 200]
    pairs = [
        ([(0, 1), (2, 3), (4, 5), (6, 7)], cols[0], cols[1]),
        ([(0, 2), (1, 3), (4, 6), (5, 7)], cols[1], cols[2]),
        ([(0, 4), (1, 5), (2, 6), (3, 7)], cols[2], cols[3]),
    ]
    for prs, xl, xr in pairs:
        xm = (xl + xr) / 2
        for a, b in prs:
            ya, yb = ys[a], ys[b]
            out.append(line(xl, ya, xr, yb, .3))
            out.append(line(xl, yb, xr, ya, .3))
    for j, x in enumerate(cols):
        for y in ys:
            out.append(dot(x, y, 1.6, .5, ACCENT if j == 3 else INK))
    out.append(amp(120, 140, '8-POINT FFT', o=.4))
    return ''.join(out)


DIAGRAMS = {
    'signal-ops': signal_ops,
    'step-impulse': step_impulse,
    'even-odd': even_odd,
    'aliasing': aliasing,
    'quantization': quantization,
    'pcm': pcm,
    'line-coding': line_coding,
    'eye-diagram': eye_diagram,
    'constellation': constellation,
    'ask-fsk-psk': ask_fsk_psk,
    'fm-modulation': fm_modulation,
    'if-filter': if_filter,
    'antenna-pattern': antenna_pattern,
    'antenna-array': antenna_array,
    'link-budget': link_budget,
    'nyquist-plot': nyquist_plot,
    'root-locus': root_locus,
    'pid': pid,
    'state-space': state_space,
    'fir-filter': fir_filter,
    'iir-filter': iir_filter,
    'windowing': windowing,
    'multirate': multirate,
    'fft-stages': fft_stages,
}
