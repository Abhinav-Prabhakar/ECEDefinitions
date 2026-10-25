#!/usr/bin/env python3
"""Build the shared diagram sprite for one·liners.

Every diagram is thin line art on a 240×150 grid. Strokes inherit currentColor
so the subject accent and the theme flow through without a second palette.
Run: python3 scripts/build-diagrams.py
"""
import os

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


def arrow(x1, y1, x2, y2, o=.65, color=INK, head=4, w=1):
    import math
    a = math.atan2(y2 - y1, x2 - x1)
    h1 = (x2 - head * math.cos(a - .5), y2 - head * math.sin(a - .5))
    h2 = (x2 - head * math.cos(a + .5), y2 - head * math.sin(a + .5))
    return (line(x1, y1, x2, y2, o, w, color=color) +
            path(f'M{h1[0]:.1f} {h1[1]:.1f} L{x2} {y2} L{h2[0]:.1f} {h2[1]:.1f}',
                 o, w, color=color))


def axis(x0, y0, x1, y1, o=.45):
    return arrow(x0, y0, x1, y1, o)


def sine(x0, x1, y, amp, cycles, o=.7, color=INK, dash=None):
    import math
    n = 60
    pts = []
    for i in range(n + 1):
        t = i / n
        pts.append(f'{x0 + (x1 - x0) * t:.1f},{y - amp * math.sin(2 * math.pi * cycles * t):.1f}')
    return path('M' + ' L'.join(pts), o, 1, dash, color)


def amp(x, y, s, o=.5, size=5.6, ls='.12em'):
    """Small uppercase label."""
    return text(x, y, s, o=o, size=size, ls=ls)


# ---------------------------------------------------------------------------
# Electronics
# ---------------------------------------------------------------------------

def pn_junction():
    return ''.join([
        rect(34, 38, 172, 70, 3, .6),
        rect(112, 38, 16, 70, 0, .14, color=ACCENT, fill='currentColor'),
        path('M112 38 V108 M128 38 V108', .8, 1, '3 4', ACCENT),
        text(58, 78, '+', o=.7, size=13, ls='0'),
        text(88, 78, '+', o=.7, size=13, ls='0'),
        text(152, 78, '−', o=.7, size=13, ls='0'),
        text(182, 78, '−', o=.7, size=13, ls='0'),
        text(68, 30, 'P', o=.75, size=9, ls='0'),
        text(176, 30, 'N', o=.75, size=9, ls='0'),
        amp(120, 124, 'DEPLETION'),
        arrow(164, 73, 140, 73, .75, ACCENT),
        amp(192, 76, 'E'),
    ])


def diode_iv():
    return ''.join([
        axis(34, 116, 216, 116, .5), axis(34, 116, 34, 28, .5),
        path('M44 113 C 120 112, 158 108, 174 82 S 190 34, 194 30', .95, 1.5, color=ACCENT),
        path('M34 116 C 24 120, 18 128, 14 138', .55, 1, '3 4'),
        amp(202, 124, 'V'), amp(24, 24, 'I'),
        amp(180, 46, 'KNEE'), amp(22, 142, 'BREAKDOWN', size=5.2),
        dot(34, 116, 2, .5),
    ])


def bjt():
    return ''.join([
        path('M110 44 V106', .8, 1.4),
        path('M110 60 L146 36 L164 26', .8),
        path('M110 90 L146 114 L164 124', .8, color=INK),
        path('M137 109 L149 115 L141 121', .8, color=ACCENT),
        line(74, 75, 110, 75, .8),
        amp(66, 77, 'B'), amp(170, 24, 'C'), amp(170, 130, 'E'),
        circle(128, 75, 48, .22),
        amp(120, 140, 'NPN', o=.35),
    ])


def mosfet():
    return ''.join([
        line(58, 50, 58, 100, .8),
        line(70, 50, 70, 100, .55),
        path('M70 58 H92 M70 75 H92 M70 92 H92', .8),
        path('M92 58 H126 V38', .8), path('M92 92 H126 V112', .8),
        path('M126 38 H164 M126 112 H164', .7),
        path('M118 104 L128 112 L118 120', .7, color=ACCENT),
        amp(48, 78, 'G', o=.6), amp(172, 40, 'D', o=.6), amp(172, 110, 'S', o=.6),
        amp(135, 132, 'N-CHANNEL', o=.4, size=5),
    ])


def opamp():
    return ''.join([
        path('M74 42 L74 108 L150 75 Z', .8),
        line(44, 60, 74, 60, .7), line(44, 90, 74, 90, .7),
        line(150, 75, 190, 75, .7),
        path('M58 60 h12 M64 54 v12', .65),
        path('M58 90 h12', .65),
        path('M150 75 H164 V36 H62 V60', .45, 1, '3 4'),
        rect(98, 28, 28, 16, 2, .6),
        amp(106, 24, 'R'), amp(112, 38, 'F', o=.4),
        amp(36, 62, 'V-'), amp(36, 92, 'V+'), amp(196, 78, 'OUT'),
        amp(120, 128, 'IDEAL OP-AMP', o=.4),
    ])


def cmos_inverter():
    return ''.join([
        line(50, 26, 196, 26, .65), line(50, 124, 196, 124, .65),
        amp(42, 22, 'VDD', o=.6, size=5.2), amp(42, 132, 'GND', o=.6, size=5.2),
        line(86, 44, 86, 66, .8), line(86, 86, 86, 108, .8),
        path('M74 66 H98 M74 74 H98', .9), path('M74 86 H98 M74 94 H98', .9),
        path('M86 44 V26 M86 108 V124', .8),
        circle(104, 70, 2.6, .8), circle(104, 90, 2.6, .8),
        line(38, 78, 74, 78, .9), line(38, 78, 38, 138, .45),
        path('M104 80 H132 V75', .8), line(132, 26, 132, 44, .8),
        amp(28, 70, 'IN', o=.6), amp(140, 78, 'OUT', o=.6),
        amp(120, 140, 'CMOS INVERTER', o=.4, size=5),
    ])


def logic_gates():
    return ''.join([
        # AND
        path('M28 34 H62 A18 18 0 0 1 62 70 H28 Z', .9),
        line(14, 44, 28, 44, .6), line(14, 60, 28, 60, .6),
        line(80, 52, 96, 52, .6), amp(48, 84, 'AND'),
        # OR
        path('M132 34 Q154 34 174 52 Q154 70 132 70 Q146 52 132 34 Z', .9),
        path('M120 34 Q136 52 120 70', .9),
        line(108, 44, 120, 44, .6), line(108, 60, 120, 60, .6),
        line(174, 52, 188, 52, .6), amp(146, 84, 'OR'),
        # NOT
        path('M132 94 L132 132 L162 113 Z', .9),
        line(118, 113, 132, 113, .6), circle(167, 113, 3.2, .9),
        line(174, 113, 188, 113, .6), amp(146, 144, 'NOT'),
    ])


def d_flipflop():
    return ''.join([
        rect(88, 40, 70, 66, 3, .8),
        line(58, 58, 88, 58, .7), line(158, 58, 188, 58, .7),
        line(58, 90, 88, 90, .7),
        path('M88 106 L98 112 L88 118', .7, color=ACCENT),
        amp(50, 60, 'D', o=.6), amp(196, 60, 'Q', o=.6),
        amp(50, 92, 'CLK', o=.6), amp(123, 76, 'D', o=.25, size=12, ls='0'),
        amp(123, 138, 'RISING EDGE', o=.4, size=5),
        path('M58 128 H188', .3, 1, '2 4'),
    ])


def cmos_cross_section():
    return ''.join([
        rect(26, 34, 188, 16, 1, .3, fill='currentColor'),
        rect(26, 50, 188, 34, 1, .5),
        rect(26, 84, 188, 26, 1, .35),
        rect(26, 110, 188, 12, 1, .25, fill='currentColor'),
        path('M74 50 V110 M142 50 V110', .35),
        path('M94 50 V44 M132 50 V44', .5),
        rect(90, 28, 46, 10, 1, .85, color=ACCENT),
        path('M94 44 V50 M132 44 V50', .6, color=ACCENT),
        amp(113, 25, 'GATE', o=.65),
        amp(50, 70, 'NWELL', o=.4), amp(175, 70, 'PWELL', o=.4),
        amp(113, 104, 'SUBSTRATE', o=.5),
        amp(30, 132, 'METAL', o=.35), amp(204, 70, 'OXIDE', o=.35),
    ])


def chip_floorplan():
    return ''.join([
        rect(30, 26, 180, 100, 3, .65),
        rect(42, 38, 64, 40, 2, .5), rect(42, 86, 34, 28, 2, .45),
        rect(84, 86, 22, 28, 2, .35),
        rect(116, 38, 40, 76, 2, .5, color=ACCENT),
        rect(166, 38, 32, 32, 2, .4), rect(166, 78, 32, 36, 2, .35),
        amp(74, 60, 'CPU'), amp(59, 103, 'SRAM'), amp(95, 103, 'IO'),
        amp(136, 78, 'GPU', o=.65), amp(182, 56, 'PLL'), amp(182, 99, 'DSP'),
        path('M42 132 H198', .35, 1, '2 5'),
    ])


def memory_hierarchy():
    rows = [(58, 92, 'REGISTERS', '1 CYCLE'), (42, 108, 'CACHE', '10 CYCLE'),
            (28, 122, 'DRAM', '100 CYCLE'), (16, 138, 'DISK', '10⁶ CYCLE')]
    out = []
    for i, (x, w, name, lat) in enumerate(rows):
        y = 30 + i * 24
        out.append(rect(x, y, w, 16, 2, .55 - i * .07))
        out.append(text(x + 9, y + 10.5, name, 'start', .62, 5.2))
        out.append(text(x + w - 8, y + 10.5, lat, 'end', .35, 4.6))
    out.append(amp(120, 134, 'CAPACITY INCREASES DOWNWARD', o=.32, size=4.8))
    return ''.join(out)


def pipeline():
    stages = ['IF', 'ID', 'EX', 'MEM', 'WB']
    out = []
    for i, s in enumerate(stages):
        x = 24 + i * 39
        out.append(rect(x, 30, 31, 20, 2, .55))
        out.append(amp(x + 15.5, 43, s, .6))
        if i < 4:
            out.append(arrow(x + 31, 40, x + 39, 40, .4, head=3))
    for r in range(4):
        for c in range(5 - r):
            x = 24 + (c + r) * 39
            out.append(rect(x, 66 + r * 16, 31, 10, 1, .3 + (c == r) * .35,
                            color=ACCENT if c == 0 else INK, fill='currentColor' if c == 0 else 'none'))
    out.append(axis(24, 140, 214, 140, .35))
    out.append(amp(216, 142, 'TIME', o=.3, size=4.6))
    return ''.join(out)


def cache_map():
    return ''.join([
        amp(34, 24, 'ADDRESS', o=.4, size=5),
        rect(26, 30, 56, 16, 1, .65), rect(82, 30, 40, 16, 1, .45),
        rect(122, 30, 28, 16, 1, .45),
        amp(54, 41, 'TAG', .6, 4.8), amp(102, 41, 'INDEX', .6, 4.8),
        amp(136, 41, 'OFF', .6, 4.8),
        arrow(102, 48, 102, 72, .45, head=3),
        rect(30, 76, 152, 12, 2, .35), rect(30, 94, 152, 12, 2, .35),
        rect(30, 112, 152, 12, 2, .35),
        amp(106, 84, 'SET 0', o=.35, size=4.6),
        amp(106, 102, 'SET 1', o=.35, size=4.6),
        amp(106, 120, 'SET 2', o=.35, size=4.6),
        rect(30, 76, 44, 12, 2, .8, color=ACCENT),
        amp(200, 80, 'WAY 0', o=.3, size=4.6),
    ])


# ---------------------------------------------------------------------------
# Signals, maths, control
# ---------------------------------------------------------------------------

def fourier():
    return ''.join([
        text(18, 20, 'f(t)', 'start', .55, 6), axis(24, 66, 212, 66, .4),
        sine(24, 212, 66, 16, 3, .3),
        sine(24, 212, 66, 20, 1, 1, ACCENT),
        text(18, 100, '|F|', 'start', .55, 6), axis(24, 136, 212, 136, .4),
        line(58, 136, 58, 104, .95, 1.6), line(116, 136, 116, 120, .6),
        line(174, 136, 174, 128, .45), line(202, 136, 202, 132, .3),
        amp(58, 146, 'f₀', o=.55), amp(116, 146, '3f₀', o=.45),
        amp(120, 20, 'TIME → FREQUENCY', o=.4, size=5.2),
    ])


def sampling():
    import math
    xs = [40, 64, 88, 112, 136, 160, 184, 208]
    def sy(x):
        return 104 - 26 * math.sin(2 * math.pi * 2.2 * (x - 26) / 188)
    return ''.join([
        axis(26, 104, 214, 104, .5), axis(26, 104, 26, 26, .5),
        sine(26, 214, 104, 26, 2.2, .75),
        *[line(x, 104, x, sy(x), .7, 1.4) for x in xs],
        path('M' + ' L'.join(f'{x},{sy(x):.1f}' for x in xs), .4, 1, '2 4', ACCENT),
        *[circle(x, sy(x), 2.2, .95) for x in xs],
        line(40, 118, 64, 118, .4), line(40, 114, 40, 122, .4), line(64, 114, 64, 122, .4),
        amp(52, 112, 'Tₛ', o=.6, size=5),
        amp(120, 136, 'CONTINUOUS · SAMPLES', o=.45, size=5.2),
        amp(220, 108, 't', o=.5, size=6),
    ])


def convolution():
    return ''.join([
        rect(22, 38, 50, 58, 2, .5), path('M28 78 H66', .9),
        path('M28 78 V48 H66 V78', .35, 1, '2 3'),
        amp(47, 112, 'x(τ)', o=.6),
        amp(84, 70, '∗', o=.75, size=13, ls='0'),
        rect(94, 38, 50, 58, 2, .5),
        path('M100 48 C 112 48, 118 78, 138 78', .95, 1.3, ACCENT),
        amp(119, 112, 'h(t)', o=.6),
        amp(156, 70, '→', o=.75, size=11, ls='0'),
        rect(168, 38, 50, 58, 2, .5),
        path('M174 78 C 182 78, 192 58, 212 52', .95, 1.3),
        amp(193, 112, 'y(t)', o=.6),
    ])


def z_plane():
    return ''.join([
        circle(120, 75, 44, .65, ACCENT),
        line(58, 75, 182, 75, .3), line(120, 18, 120, 132, .3),
        path('M120 18 l-3 5 M120 18 l3 5', .3), path('M182 75 l-5 -3 M182 75 l-5 3', .3),
        path('M156 62 l-9 9 M147 62 l9 9', .8, 1.4),
        circle(86, 58, 5, .8),
        dot(120, 75, 2, .3),
        amp(120, 142, 'UNIT CIRCLE', o=.35, size=4.8),
        amp(164, 58, 'POLE', o=.4, size=4.6), amp(84, 48, 'ZERO', o=.4, size=4.6),
        amp(186, 78, 'Re', o=.35, size=4.6), amp(124, 14, 'Im', o=.35, size=4.6),
        path('M120 75 L156 62', .35, 1, '2 3'),
    ])


def bode():
    return ''.join([
        axis(30, 66, 212, 66, .35), axis(30, 66, 30, 22, .35),
        axis(30, 136, 212, 136, .35), axis(30, 136, 30, 96, .35),
        path('M34 56 H92 L184 116', .9, 1.4, color=ACCENT),
        path('M34 128 H92 C 112 128, 112 118, 132 118 S 152 108, 184 106', .6),
        path('M92 66 V22', .3, 1, '2 4'), path('M92 136 V96', .3, 1, '2 4'),
        amp(92, 18, 'ωc', o=.4, size=4.8), amp(92, 148, 'ωc', o=.4, size=4.8),
        amp(214, 68, 'dB', o=.3, size=4.6), amp(214, 138, 'φ', o=.3, size=4.6),
        amp(20, 44, 'A', o=.35, size=5), amp(20, 116, '0', o=.35, size=5),
    ])


def control_loop():
    return ''.join([
        circle(62, 64, 10, .8),
        path('M56 58 L68 70 M68 58 L56 70', .6),
        line(26, 64, 52, 64, .7),
        arrow(72, 64, 104, 64, .6),
        rect(104, 48, 50, 32, 2, .75),
        arrow(154, 64, 202, 64, .6),
        path('M196 64 V112 H62 V74', .5, 1, '3 4'),
        rect(126, 102, 34, 20, 2, .45),
        amp(129, 43, 'G(s)', o=.55), amp(143, 116, 'H(s)', o=.45),
        amp(18, 66, 'R', o=.5), amp(208, 66, 'Y', o=.5),
        amp(120, 140, 'NEGATIVE FEEDBACK', o=.3, size=4.8),
    ])


def gaussian():
    return ''.join([
        axis(28, 118, 214, 118, .35),
        path('M34 118 C 64 118, 78 30, 120 30 S 176 118, 206 118', .9, 1.4, color=ACCENT),
        path('M84 118 C 92 88, 100 58, 120 58 C 140 58, 148 88, 156 118', .35, 1, '2 3'),
        line(120, 118, 120, 30, .3, 1, '3 4'),
        amp(120, 132, 'μ', o=.45), amp(84, 132, '−σ', o=.3, size=4.6),
        amp(156, 132, '+σ', o=.3, size=4.6),
        amp(36, 132, 'x', o=.3, size=4.6),
        amp(196, 44, '68%', o=.35, size=4.6),
    ])


def matrix_transform():
    return ''.join([
        line(46, 118, 202, 118, .35), line(46, 118, 46, 26, .35),
        path('M46 118 L94 118 L94 70 L46 70 Z', .3, 1, '3 4'),
        path('M46 118 L146 118 L178 66 L78 66 Z', .55),
        arrow(46, 118, 106, 118, .9, ACCENT), arrow(46, 118, 74, 82, .9, ACCENT),
        amp(106, 128, 'e₁', o=.55), amp(66, 78, 'e₂', o=.55),
        amp(150, 44, 'A', o=.4, size=10, ls='0'),
        path('M86 44 H154', .3, 1, '2 4'),
        amp(120, 140, 'LINEAR MAP', o=.3, size=4.8),
    ])


# ---------------------------------------------------------------------------
# Communications
# ---------------------------------------------------------------------------

def am_modulation():
    return ''.join([
        axis(24, 112, 216, 112, .35), axis(24, 112, 24, 30, .35),
        line(24, 76, 216, 76, .22, 1, '2 4'),
        path('M26 76 C 42 40, 58 40, 74 76 S 106 112, 122 76 S 154 40, 170 76 S 202 112, 214 76', .8, 1.2, color=ACCENT),
        sine(26, 214, 76, 34, 8, .3),
        amp(120, 134, 'ENVELOPE · CARRIER', o=.35, size=4.8),
        amp(220, 114, 't', o=.3, size=4.6),
    ])


def qam():
    pts = []
    for x in [66, 102, 138, 174]:
        for y in [108, 79, 50, 21]:
            pts.append(dot(x, y, 2.4, .55))
    return ''.join([
        axis(120, 130, 120, 16, .4), axis(48, 75, 206, 75, .4),
        *pts,
        dot(138, 50, 4, 1, ACCENT),
        path('M138 75 V50 M120 50 H138', .6, 1, '2 3', ACCENT),
        amp(120, 144, 'I', o=.5, size=5.4), amp(210, 78, 'Q', o=.5, size=5.4),
        amp(120, 12, '16-QAM', o=.4, size=5.2),
    ])


def superhet():
    return ''.join([
        rect(22, 46, 38, 28, 2, .55), rect(76, 46, 34, 28, 2, .65),
        rect(126, 46, 46, 28, 2, .55), rect(188, 46, 30, 28, 2, .55),
        arrow(60, 60, 76, 60, .4, head=3), arrow(110, 60, 126, 60, .4, head=3),
        arrow(172, 60, 188, 60, .4, head=3),
        amp(41, 63, 'RF', .55), amp(93, 63, 'MIX', .55),
        amp(149, 63, 'IF', .55), amp(203, 63, 'DEM', .55),
        rect(78, 104, 30, 18, 2, .45),
        amp(93, 116, 'LO', .5, 4.8),
        arrow(93, 104, 93, 78, .5, head=3),
        amp(120, 140, 'SUPERHETERODYNE', o=.3, size=4.8),
    ])


def dipole():
    return ''.join([
        line(120, 34, 120, 116, .85, 1.5, color=ACCENT),
        dot(120, 75, 2.5, .8),
        path('M120 34 C 74 34, 60 62, 60 75 C 60 88, 74 116, 120 116', .4),
        path('M120 34 C 166 34, 180 62, 180 75 C 180 88, 166 116, 120 116', .4),
        path('M120 34 C 96 34, 88 60, 88 75 C 88 90, 96 116, 120 116', .22, 1, '2 3'),
        path('M120 34 C 144 34, 152 60, 152 75 C 152 90, 144 116, 120 116', .22, 1, '2 3'),
        line(120, 126, 120, 144, .35, 1, '2 3'),
        amp(120, 28, 'λ/2', o=.35, size=4.8),
        amp(196, 78, 'E', o=.35), amp(120, 140, 'FEED', o=.3, size=4.4),
    ])


def tx_line():
    return ''.join([
        line(24, 62, 216, 62, .8), line(24, 94, 216, 94, .8),
        rect(28, 52, 10, 52, 1, .55), rect(202, 52, 10, 52, 1, .55),
        path('M206 62 V94', .95, 1.6, color=ACCENT),
        path('M24 112 C 52 92, 82 132, 112 112 S 172 92, 202 112 S 236 132, 236 112', .55, 1, '2 3'),
        amp(33, 46, 'SOURCE', o=.4, size=5.2), amp(207, 46, 'LOAD', o=.4, size=5.2),
        amp(120, 136, 'STANDING WAVE', o=.4, size=5.2),
    ])


def em_wave():
    return ''.join([
        arrow(28, 76, 216, 76, .45),
        sine(30, 210, 48, 20, 1.4, .9, ACCENT),
        sine(30, 210, 104, 20, 1.4, .6, INK, '3 4'),
        line(30, 48, 30, 104, .25, 1, '1 4'),
        amp(120, 20, 'E'), amp(120, 134, 'H'),
        amp(190, 88, 'z', o=.5, size=5.4),
        amp(120, 76, 'IN PHASE', o=.35, size=5),
    ])


# ---------------------------------------------------------------------------
# Computer science and networks
# ---------------------------------------------------------------------------

def osi_stack():
    layers = ['APPLICATION', 'PRESENTATION', 'SESSION', 'TRANSPORT',
              'NETWORK', 'DATA LINK', 'PHYSICAL']
    out = []
    for i, name in enumerate(layers):
        y = 16 + i * 17
        out.append(rect(52, y, 136, 13, 1, .6 - i * .02,
                        color=ACCENT if i == 3 else INK))
        out.append(text(120, y + 9, name, 'middle', .72, 6.2, '.07em'))
    out.append(amp(30, 80, '7', o=.25, size=10, ls='0'))
    out.append(amp(120, 142, 'LAYERS', o=.3, size=4.6))
    return ''.join(out)


def tcp_handshake():
    return ''.join([
        line(60, 22, 60, 132, .45), line(180, 22, 180, 132, .45),
        amp(60, 16, 'CLIENT', o=.55, size=5.4), amp(180, 16, 'SERVER', o=.55, size=5.4),
        arrow(60, 40, 180, 40, .75, ACCENT, 4), amp(120, 34, 'SYN', o=.6, size=5.2),
        arrow(180, 68, 60, 68, .75, ACCENT, 4), amp(120, 62, 'SYN + ACK', o=.6, size=5.2),
        arrow(60, 96, 180, 96, .75, ACCENT, 4), amp(120, 90, 'ACK', o=.6, size=5.2),
        amp(120, 124, 'THREE-WAY OPEN', o=.4, size=5.2),
    ])


def process_states():
    return ''.join([
        circle(46, 42, 14, .55), circle(120, 42, 15, .55),
        circle(194, 42, 14, .55), circle(120, 108, 15, .55),
        circle(46, 108, 14, .55),
        amp(46, 44, 'NEW', .55, 4.4), amp(120, 44, 'READY', .65, 4.4),
        amp(194, 44, 'RUN', .55, 4.4), amp(120, 110, 'WAIT', .55, 4.4),
        amp(46, 110, 'EXIT', .5, 4.4),
        arrow(60, 42, 104, 42, .45, head=3), arrow(135, 42, 180, 42, .45, head=3),
        arrow(120, 57, 120, 92, .45, head=3), arrow(106, 100, 58, 52, .35, head=3),
        arrow(180, 34, 136, 34, .35, head=3),
        circle(120, 42, 15, .8, ACCENT),
        amp(128, 132, 'SCHEDULER', o=.3, size=4.6),
    ])


def linked_list():
    out = []
    for i in range(4):
        x = 28 + i * 48
        out.append(rect(x, 52, 40, 34, 3, .6))
        out.append(line(x + 26, 52, x + 26, 86, .4))
        out.append(dot(x + 33, 69, 2, .5))
        if i < 3:
            out.append(arrow(x + 40, 69, x + 48, 69, .45, head=3))
    out.append(arrow(28, 69, 18, 69, .3, head=3))
    out.append(amp(18, 60, 'HEAD', o=.35, size=4.4))
    out.append(amp(120, 108, 'DATA · NEXT', o=.3, size=4.6))
    out.append(circle(228, 69, 4, .4))
    out.append(path('M225 66 L231 72 M231 66 L225 72', .4))
    out.append(amp(232, 84, 'NULL', o=.3, size=4.4))
    return ''.join(out)


def binary_tree():
    return ''.join([
        line(120, 30, 76, 66, .45), line(120, 30, 164, 66, .45),
        line(76, 66, 48, 104, .35), line(76, 66, 104, 104, .35),
        line(164, 66, 136, 104, .35), line(164, 66, 192, 104, .35),
        circle(120, 30, 11, .75), circle(76, 66, 10, .6), circle(164, 66, 10, .6),
        circle(48, 104, 9, .4), circle(104, 104, 9, .4),
        circle(136, 104, 9, .4), circle(192, 104, 9, .4),
        circle(76, 66, 15, .8, ACCENT),
        amp(120, 34, '8', .65, 5), amp(76, 70, '4', .7, 5), amp(164, 70, '12', .6, 5),
        amp(48, 108, '2', .45, 4.6), amp(104, 108, '6', .45, 4.6),
        amp(136, 108, '10', .45, 4.6), amp(192, 108, '14', .45, 4.6),
        amp(120, 134, 'BINARY SEARCH TREE', o=.3, size=4.6),
    ])


def graph_search():
    nodes = [(44, 48), (92, 30), (92, 76), (142, 50), (190, 30), (190, 82), (142, 108)]
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4), (3, 5), (3, 6), (5, 6)]
    out = []
    for a, b in edges:
        out.append(line(nodes[a][0], nodes[a][1], nodes[b][0], nodes[b][1], .28))
    for i, (x, y) in enumerate(nodes):
        out.append(circle(x, y, 9, .6))
    out.append(circle(44, 48, 14, .8, ACCENT))
    out.append(circle(92, 30, 14, .45, ACCENT, 'none', 1))
    out.append(circle(92, 76, 14, .45, ACCENT, 'none', 1))
    out.append(path('M44 48 L92 30 L142 50 L190 82', .7, 1, '2 3', ACCENT))
    out.append(amp(120, 134, 'FRONTIER', o=.3, size=4.6))
    return ''.join(out)


def dft_butterfly():
    return ''.join([
        dot(42, 44), dot(42, 106), dot(198, 44), dot(198, 106),
        path('M42 44 L104 44 L150 62 L198 62', .6),
        path('M42 106 L104 106 L150 88 L198 88', .6),
        path('M104 44 L150 88', .45, 1, '2 3'),
        path('M104 106 L150 62', .45, 1, '2 3'),
        dot(150, 62, 2.4, .8, ACCENT), dot(150, 88, 2.4, .8, ACCENT),
        amp(78, 36, '+', o=.5, size=9, ls='0'),
        amp(78, 98, '−', o=.5, size=9, ls='0'),
        amp(166, 54, 'W', o=.55, size=5),
        amp(120, 132, 'RADIX-2 BUTTERFLY', o=.3, size=4.6),
        amp(42, 126, 'x₀', o=.4, size=4.8), amp(42, 22, 'x₁', o=.4, size=4.8),
    ])


def neural_net():
    layers = [(56, [38, 75, 112]), (120, [30, 58, 86, 114]), (184, [54, 96])]
    out = []
    for li in range(2):
        for ya in layers[li][1]:
            for yb in layers[li + 1][1]:
                out.append(line(layers[li][0], ya, layers[li + 1][0], yb, .24))
    for li, (x, ys) in enumerate(layers):
        for y in ys:
            out.append(circle(x, y, 8, .7))
    out.append(circle(56, 75, 8, 1, ACCENT))
    out.append(circle(184, 54, 8, 1, ACCENT))
    out.append(amp(120, 136, 'INPUT · HIDDEN · OUTPUT', o=.4, size=5.2))
    return ''.join(out)


def image_pipeline():
    out = []
    for i in range(4):
        x = 24 + i * 54
        out.append(rect(x, 42, 40, 40, 2, .45))
        for r in range(3):
            for c in range(3):
                o = .12 + .1 * ((r * 3 + c + i) % 4)
                out.append(rect(x + 5 + c * 10, 47 + r * 10, 8, 8, 1, o,
                                color=INK, fill='currentColor' if (r + c + i) % 3 == 0 else 'none'))
        if i < 3:
            out.append(arrow(x + 40, 62, x + 54, 62, .4, head=3))
    labels = ['PIXEL', 'BLUR', 'EDGE', 'MASK']
    for i, s in enumerate(labels):
        out.append(amp(44 + i * 54, 96, s, o=.35, size=4.6))
    out.append(amp(120, 124, 'IMAGE → FEATURES', o=.3, size=4.6))
    return ''.join(out)


def satellite_link():
    return ''.join([
        path('M22 132 C 72 112, 168 112, 218 132', .55),
        rect(108, 22, 24, 16, 2, .8, color=ACCENT),
        path('M120 38 V54 M120 54 L110 64 M120 54 L130 64', .5),
        path('M120 54 L120 70', .35, 1, '2 3'),
        arrow(84, 70, 110, 40, .45, ACCENT, 3),
        arrow(156, 40, 182, 70, .45, ACCENT, 3),
        rect(64, 78, 18, 12, 1, .45), rect(158, 78, 18, 12, 1, .45),
        line(73, 90, 73, 116, .35), line(167, 90, 167, 116, .35),
        amp(73, 124, 'EARTH', o=.35, size=4.6), amp(167, 124, 'GATEWAY', o=.35, size=4.6),
        amp(120, 12, 'UPLINK · DOWNLINK', o=.3, size=4.4),
    ])


def iot_layers():
    rows = [('CLOUD', 22, 196, 'ANALYTICS'), ('EDGE', 46, 148, 'GATEWAY'),
            ('DEVICE', 70, 100, 'SENSORS')]
    out = []
    for name, y, w, sub in rows:
        x = 120 - w / 2
        out.append(rect(x, y, w, 20, 2, .55))
        out.append(text(x + 9, y + 13, name, 'start', .6, 4.8))
        out.append(text(x + w - 9, y + 13, sub, 'end', .32, 4.4))
        out.append(arrow(120, y + 20, 120, y + 24, .35, head=3))
    out.append(amp(120, 108, 'PUBLISH · FILTER · STORE', o=.3, size=4.6))
    return ''.join(out)


def soc_blocks():
    return ''.join([
        rect(26, 26, 188, 100, 3, .6),
        rect(38, 38, 48, 34, 2, .55), rect(38, 80, 48, 34, 2, .4),
        rect(96, 38, 44, 76, 2, .45), rect(150, 38, 52, 30, 2, .4),
        rect(150, 78, 52, 36, 2, .4),
        path('M86 62 H96 M140 62 H150 M86 94 H96 M140 94 H150', .65, 1.3, color=ACCENT),
        amp(62, 58, 'CPU'), amp(62, 100, 'GPU'), amp(118, 80, 'NPU'),
        amp(176, 56, 'DDR'), amp(176, 100, 'IO'),
        amp(120, 140, 'INTERCONNECT', o=.3, size=4.6),
    ])


def rtos_timeline():
    return ''.join([
        axis(28, 122, 214, 122, .35),
        *[line(x, 118, x, 126, .3) for x in [52, 88, 124, 160, 196]],
        line(28, 36, 214, 36, .18), line(28, 68, 214, 68, .18),
        line(28, 100, 214, 100, .18),
        *[rect(x, 28, 24, 14, 1, .5) for x in [34, 70, 106, 142, 178]],
        *[rect(x, 60, 32, 14, 1, .45) for x in [50, 94, 138, 182]],
        *[rect(x, 92, 16, 14, 1, .55, color=ACCENT) for x in [34, 50, 66, 82, 98, 114, 130, 146, 162, 178, 194]],
        amp(22, 38, 'T1', o=.35, size=4.4), amp(22, 70, 'T2', o=.35, size=4.4),
        amp(22, 102, 'T3', o=.35, size=4.4),
        amp(120, 140, 'PERIODIC TASKS · DEADLINES', o=.3, size=4.4),
    ])


# ---------------------------------------------------------------------------
# Non-ECE subjects still benefit from one honest diagram.
# ---------------------------------------------------------------------------

def supply_demand():
    return ''.join([
        axis(44, 118, 206, 118, .35), axis(44, 118, 44, 26, .35),
        path('M62 38 L188 112', .8), path('M62 112 L188 38', .8, color=ACCENT),
        circle(120, 75, 3.2, 1, ACCENT),
        path('M120 75 V118 M44 75 H120', .3, 1, '2 4'),
        amp(120, 132, 'Q', o=.3, size=4.6), amp(32, 75, 'P', o=.3, size=4.6),
        amp(172, 32, 'S', o=.35, size=4.8), amp(64, 32, 'D', o=.35, size=4.8),
        amp(120, 68, 'E', o=.5, size=4.6),
    ])


def break_even():
    return ''.join([
        axis(40, 118, 208, 118, .35), axis(40, 118, 40, 24, .35),
        line(40, 96, 200, 96, .35, 1, '2 3'),
        path('M40 108 L200 40', .7),
        path('M40 84 L200 76', .45, 1, '3 4'),
        circle(128, 76, 3, 1, ACCENT),
        path('M128 76 V118 M40 76 H128', .3, 1, '2 4'),
        amp(120, 132, 'UNITS', o=.3, size=4.4), amp(28, 72, '₹', o=.3, size=5),
        amp(128, 68, 'BEP', o=.5, size=4.4),
        amp(188, 34, 'REVENUE', o=.3, size=4.4),
        amp(188, 104, 'COST', o=.3, size=4.4),
    ])


def carbon_cycle():
    return ''.join([
        circle(120, 76, 48, .3),
        circle(120, 76, 30, .22),
        dot(120, 28, 4, .7), dot(168, 76, 4, .55), dot(120, 124, 4, .55),
        dot(72, 76, 4, .55),
        arrow(126, 28, 164, 64, .45, ACCENT, 3),
        arrow(168, 82, 130, 120, .4, ACCENT, 3),
        arrow(114, 124, 76, 88, .4, ACCENT, 3),
        arrow(72, 70, 112, 34, .4, ACCENT, 3),
        amp(120, 16, 'ATMOSPHERE', o=.4, size=4.4),
        amp(188, 78, 'PLANTS', o=.35, size=4.4),
        amp(120, 140, 'SOIL', o=.35, size=4.4),
        amp(50, 78, 'OCEAN', o=.35, size=4.4),
    ])


def water_cycle():
    return ''.join([
        circle(44, 38, 11, .55), *[line(44 + 12 * __import__('math').cos(a), 38 + 12 * __import__('math').sin(a),
                                        44 + 17 * __import__('math').cos(a), 38 + 17 * __import__('math').sin(a), .35)
                                   for a in [0, .8, 1.6, 2.4, 3.2, 4.0, 4.8, 5.6]],
        path('M104 58 C 100 46, 116 44, 120 54 C 128 44, 142 50, 138 60 C 150 58, 152 70, 138 72 H106 C 96 72, 96 60, 104 58 Z', .6),
        path('M66 116 C 96 92, 150 92, 184 116', .65),
        arrow(58, 62, 92, 76, .4, ACCENT, 3), amp(70, 84, 'EVAPORATION', o=.3, size=4.2),
        *[arrow(116 + i * 9, 78, 108 + i * 9, 104, .4, ACCENT, 3) for i in range(3)],
        amp(154, 96, 'RAIN', o=.3, size=4.2),
        path('M184 116 C 168 124, 120 136, 78 122', .5, 1, '2 3'),
        amp(120, 142, 'RUNOFF', o=.3, size=4.2),
        amp(120, 30, 'WATER CYCLE', o=.3, size=4.6),
    ])


def venn():
    return ''.join([
        circle(94, 74, 40, .55), circle(146, 74, 40, .55),
        path('M120 44 C 138 56, 138 92, 120 104 C 102 92, 102 56, 120 44 Z', .7, 1.2, color=ACCENT),
        amp(76, 78, 'A', o=.5, size=6, ls='0'), amp(164, 78, 'B', o=.5, size=6, ls='0'),
        amp(120, 78, 'A∩B', o=.5, size=4.6),
        amp(120, 132, 'SET LOGIC', o=.3, size=4.6),
    ])


def electric_dipole():
    return ''.join([
        line(50, 76, 190, 76, .3, 1, '3 4'),
        dot(50, 76, 6, .9, ACCENT), dot(190, 76, 6, .9, ACCENT),
        text(50, 79, '−', o=.9, size=10, ls='0'), text(190, 79, '+', o=.9, size=10, ls='0'),
        path('M190 70 C 170 30, 70 30, 50 70', .55),
        path('M190 82 C 170 122, 70 122, 50 82', .55),
        path('M190 76 C 168 56, 72 56, 50 76', .3, 1, '2 4'),
        text(120, 96, 'd', o=.45, size=5.6, ls='.08em'),
        amp(120, 24, 'ELECTRIC DIPOLE', o=.4, size=5.2),
        amp(214, 79, 'p', o=.45),
    ])


def eigen_directions():
    return ''.join([
        line(34, 116, 206, 116, .3), line(34, 116, 34, 26, .3),
        path('M34 116 L96 116 L96 54 L34 54 Z', .25, 1, '3 4'),
        path('M34 116 L126 116 L164 62 L72 62 Z', .5),
        arrow(34, 116, 154, 30, .85, ACCENT),
        arrow(34, 116, 196, 116, .85, ACCENT),
        path('M34 116 L104 66', .35, 1, '2 4'),
        path('M34 116 L90 116', .35, 1, '2 4'),
        amp(162, 24, 'v₁'), amp(198, 122, 'v₂'),
        amp(120, 140, 'EIGEN-DIRECTIONS', o=.35, size=5),
        amp(166, 54, 'A', o=.4, size=6, ls='0'),
    ])


def memory_layout():
    return ''.join([
        rect(52, 18, 104, 14, 1, .45), rect(52, 34, 104, 14, 1, .45),
        rect(52, 50, 104, 14, 1, .45), rect(52, 66, 104, 14, 1, .45),
        rect(52, 96, 104, 16, 1, .45),
        text(104, 28, 'TEXT', o=.65, size=5.4, ls='.12em'), text(104, 44, 'DATA', o=.65, size=5.4, ls='.12em'),
        text(104, 60, 'BSS', o=.65, size=5.4, ls='.12em'), text(104, 76, 'HEAP', o=.65, size=5.4, ls='.12em'),
        text(104, 107, 'STACK', o=.65, size=5.4, ls='.12em'),
        arrow(170, 68, 170, 90, .55, ACCENT, 3),
        arrow(170, 111, 170, 92, .55, ACCENT, 3),
        amp(120, 136, 'LOW → HIGH ADDRESS', o=.35, size=4.6),
        amp(190, 80, '↓'), amp(190, 104, '↑'),
    ])


def stack_queue():
    return ''.join([
        rect(32, 34, 32, 78, 2, .55),
        *[line(32, 34 + i * 15.6, 64, 34 + i * 15.6, .25) for i in range(1, 5)],
        rect(32, 34, 32, 15.6, 2, .8, color=ACCENT),
        text(48, 45, 'A', o=.75, size=6, ls='0'),
        arrow(84, 38, 70, 38, .65, ACCENT, 3),
        arrow(70, 64, 84, 64, .65, ACCENT, 3),
        amp(98, 36, 'PUSH', o=.45, size=4.2, ls='.04em'), amp(98, 66, 'POP', o=.45, size=4.2, ls='.04em'),
        amp(48, 130, 'STACK', o=.5, size=5),
        rect(124, 58, 84, 26, 2, .5),
        *[line(124 + i * 21, 58, 124 + i * 21, 84, .25) for i in range(1, 4)],
        text(136, 74, 'A', o=.6, size=5.4, ls='0'), text(157, 74, 'B', o=.6, size=5.4, ls='0'),
        text(178, 74, 'C', o=.6, size=5.4, ls='0'),
        arrow(136, 52, 136, 58, .6, ACCENT, 3), arrow(196, 52, 196, 58, .6, ACCENT, 3),
        amp(136, 46, 'FRONT', o=.45, size=4.2), amp(196, 46, 'REAR', o=.45, size=4.2),
        amp(166, 130, 'QUEUE', o=.5, size=5),
        path('M206 84 C 222 74, 222 68, 208 60', .4, 1, '2 3', ACCENT),
        amp(224, 92, 'WRAP', o=.35, size=4.2),
        amp(120, 18, 'LINEAR STRUCTURES', o=.3, size=4.6),
    ])


def d_orbital_splitting():
    return ''.join([
        axis(48, 118, 48, 26, .4),
        *[line(36, 118 - i * 14, 52, 118 - i * 14, .2) for i in range(1, 7)],
        line(84, 52, 164, 52, .6, 1.4),
        line(84, 78, 140, 78, .8, 1.4, color=ACCENT),
        line(140, 78, 196, 78, .8, 1.4, color=ACCENT),
        line(84, 104, 140, 104, .8, 1.4, color=ACCENT),
        line(140, 104, 196, 104, .8, 1.4, color=ACCENT),
        amp(170, 48, 'FREE ION', o=.4, size=4.6),
        amp(170, 74, 'e_g', o=.55, size=5.2),
        amp(170, 100, 't_{2g}', o=.55, size=5.2),
        path('M214 78 V104', .45, 1, '2 3'),
        path('M210 78 l4 -3 M210 104 l4 3', .45),
        amp(228, 92, 'Δ₀', o=.5, size=5),
        amp(120, 140, 'OCTAHEDRAL FIELD', o=.3, size=4.6),
    ])


def electrochemical_cell():
    return ''.join([
        path('M42 62 V112 H102 V62', .55),
        path('M138 62 V112 H198 V62', .55),
        line(42, 74, 102, 74, .3), line(138, 74, 198, 74, .3),
        line(72, 50, 72, 112, .8, 1.3, color=ACCENT),
        line(168, 50, 168, 112, .8, 1.3),
        path('M72 50 H106 V34 H134 V50 H168', .5),
        circle(120, 34, 8, .6),
        text(120, 37, 'V', o=.6, size=6, ls='0'),
        path('M102 80 H138', .5, 1, '2 3'),
        amp(120, 92, 'SALT BRIDGE', o=.4, size=4.2),
        amp(72, 128, 'ANODE', o=.4, size=4.4), amp(168, 128, 'CATHODE', o=.4, size=4.4),
        arrow(72, 58, 168, 58, .55, ACCENT, 3),
        amp(120, 54, 'e⁻', o=.5, size=4.8),
        amp(120, 146, 'GALVANIC CELL', o=.3, size=4.6),
    ])


def series_parallel():
    return ''.join([
        amp(58, 24, 'SERIES', o=.4, size=4.6),
        line(24, 46, 38, 46, .7), rect(38, 38, 26, 16, 1, .7),
        line(64, 46, 88, 46, .7), rect(88, 38, 26, 16, 1, .7),
        line(114, 46, 128, 46, .7),
        amp(51, 48, 'R₁', o=.5, size=4.4), amp(101, 48, 'R₂', o=.5, size=4.4),
        amp(76, 68, 'R_eq=R₁+R₂', o=.5, size=4.6),
        amp(178, 24, 'PARALLEL', o=.4, size=4.6),
        line(144, 46, 158, 46, .7), line(158, 34, 158, 58, .7),
        rect(158, 28, 26, 14, 1, .7), rect(158, 50, 26, 14, 1, .7),
        line(184, 34, 198, 34, .7), line(184, 58, 198, 58, .7),
        line(198, 34, 198, 58, .7), line(198, 46, 214, 46, .7),
        amp(170, 38, 'R₁', o=.45, size=4.2), amp(170, 60, 'R₂', o=.45, size=4.2),
        amp(179, 80, 'R_eq=R₁R₂/(R₁+R₂)', o=.45, size=4.2),
    ])


def thevenin_equiv():
    return ''.join([
        rect(24, 40, 72, 62, 3, .55),
        text(60, 66, 'LINEAR', o=.55, size=5, ls='.1em'), text(60, 78, 'NETWORK', o=.55, size=5, ls='.1em'),
        line(96, 54, 122, 54, .7), line(96, 88, 122, 88, .7),
        dot(122, 54, 2.5, .6), dot(122, 88, 2.5, .6),
        amp(114, 112, 'a', o=.4), amp(114, 36, 'b', o=.4),
        arrow(130, 71, 154, 71, .5, ACCENT, 3),
        line(162, 54, 162, 88, .7), rect(154, 60, 16, 22, 1, .7, color=ACCENT),
        line(162, 54, 206, 54, .7), line(162, 88, 206, 88, .7),
        rect(190, 46, 16, 16, 1, .6), line(198, 46, 198, 36, .5),
        amp(162, 46, 'R_th', o=.55, size=4.2), amp(198, 34, 'LOAD', o=.35, size=4),
        amp(120, 124, 'THEVENIN EQUIVALENT', o=.35, size=4.6),
        amp(86, 112, 'V_th', o=.45, size=4.4),
    ])


def rlc_transient():
    import math
    under = []
    over = []
    for i in range(61):
        x = 40 + i * 2.6
        t = i / 60
        under.append(f'{x:.1f},{86 - 34 * math.exp(-3.2 * t) * math.cos(9 * t):.1f}')
        over.append(f'{x:.1f},{86 - 34 * math.exp(-2.6 * t):.1f}')
    return ''.join([
        axis(40, 86, 210, 86, .35), axis(40, 86, 40, 26, .35),
        path('M' + ' L'.join(under), .9, 1.3, ACCENT),
        path('M' + ' L'.join(over), .55, 1, '3 4'),
        path(f'M40 52 C 80 52, 100 78, 130 82 S 190 86, 210 86', .5, 1, '2 3'),
        amp(176, 38, 'UNDER', o=.45, size=4.2), amp(176, 62, 'OVER', o=.35, size=4.2),
        amp(120, 108, 'STEP RESPONSE', o=.35, size=4.6),
        amp(212, 88, 't', o=.4, size=5),
    ])


def phasor():
    return ''.join([
        circle(112, 76, 44, .35),
        line(56, 76, 182, 76, .3), line(112, 18, 112, 134, .3),
        arrow(112, 76, 148, 44, .85, ACCENT),
        path('M132 76 A 20 20 0 0 0 126 63', .45),
        amp(128, 68, 'φ', o=.5, size=5),
        line(148, 44, 148, 76, .3, 1, '2 3'), line(112, 44, 148, 44, .3, 1, '2 3'),
        text(118, 40, 'V_m', 'start', .45, 4.6),
        amp(150, 40, 'V', o=.5), amp(186, 79, 'Re', o=.35, size=4.4),
        amp(116, 14, 'Im', o=.35, size=4.4),
        sine(112, 210, 76, 22, 1), 
        amp(160, 116, 'PROJECTION', o=.35, size=4.4),
    ])


def vector_field():
    return ''.join([
        path('M52 76 C 52 42, 92 28, 124 34 C 164 42, 188 62, 182 88 C 176 116, 140 128, 104 122 C 68 116, 52 102, 52 76 Z', .6),
        *[arrow(52 + 20 * __import__('math').cos(a), 76 + 20 * __import__('math').sin(a),
                52 + 44 * __import__('math').cos(a), 76 + 44 * __import__('math').sin(a), .45, INK, 3)
          for a in [0, .7, 1.4, 2.1, 2.8, 3.5, 4.2, 4.9, 5.6]],
        path('M120 76 C 112 48, 136 30, 158 46 C 176 60, 166 84, 146 92 C 128 100, 112 92, 120 76 Z', .5, 1, '3 4', ACCENT),
        arrow(140, 62, 154, 52, .8, ACCENT, 3),
        amp(120, 140, 'FLUX · CIRCULATION', o=.35, size=4.6),
    ])


def two_port():
    return ''.join([
        rect(72, 42, 96, 66, 3, .6),
        line(32, 58, 72, 58, .7), line(32, 92, 72, 92, .7),
        line(168, 58, 208, 58, .7), line(168, 92, 208, 92, .7),
        arrow(74, 58, 90, 58, .45, ACCENT, 3), arrow(150, 58, 166, 58, .45, ACCENT, 3),
        arrow(90, 92, 74, 92, .45, INK, 3), arrow(166, 92, 150, 92, .45, INK, 3),
        text(120, 72, 'TWO-PORT', o=.6, size=5.4, ls='.1em'),
        text(120, 84, 'NETWORK', o=.5, size=5.4, ls='.1em'),
        amp(44, 52, 'V₁', o=.45, size=4.6), amp(44, 104, 'I₁', o=.45, size=4.6),
        amp(196, 52, 'V₂', o=.45, size=4.6), amp(196, 104, 'I₂', o=.45, size=4.6),
        amp(120, 130, 'PORT RELATIONS', o=.3, size=4.6),
    ])


DIAGRAMS = {
    'pn-junction': pn_junction,
    'diode-iv': diode_iv,
    'bjt': bjt,
    'mosfet': mosfet,
    'opamp': opamp,
    'cmos-inverter': cmos_inverter,
    'logic-gates': logic_gates,
    'd-flipflop': d_flipflop,
    'cmos-cross-section': cmos_cross_section,
    'chip-floorplan': chip_floorplan,
    'memory-hierarchy': memory_hierarchy,
    'pipeline': pipeline,
    'cache-map': cache_map,
    'fourier': fourier,
    'sampling': sampling,
    'convolution': convolution,
    'z-plane': z_plane,
    'bode': bode,
    'control-loop': control_loop,
    'gaussian': gaussian,
    'matrix-transform': matrix_transform,
    'am-modulation': am_modulation,
    'qam': qam,
    'superhet': superhet,
    'dipole': dipole,
    'tx-line': tx_line,
    'em-wave': em_wave,
    'osi-stack': osi_stack,
    'tcp-handshake': tcp_handshake,
    'process-states': process_states,
    'linked-list': linked_list,
    'binary-tree': binary_tree,
    'graph-search': graph_search,
    'dft-butterfly': dft_butterfly,
    'neural-net': neural_net,
    'image-pipeline': image_pipeline,
    'satellite-link': satellite_link,
    'iot-layers': iot_layers,
    'soc-blocks': soc_blocks,
    'rtos-timeline': rtos_timeline,
    'supply-demand': supply_demand,
    'break-even': break_even,
    'carbon-cycle': carbon_cycle,
    'water-cycle': water_cycle,
    'venn': venn,
    'electric-dipole': electric_dipole,
    'eigen-directions': eigen_directions,
    'memory-layout': memory_layout,
    'stack-queue': stack_queue,
    'd-orbital-splitting': d_orbital_splitting,
    'electrochemical-cell': electrochemical_cell,
    'series-parallel': series_parallel,
    'thevenin-equiv': thevenin_equiv,
    'rlc-transient': rlc_transient,
    'phasor': phasor,
    'vector-field': vector_field,
    'two-port': two_port,
}


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out = os.path.join(root, 'assets', 'diagrams.svg')
    symbols = []
    for name, fn in DIAGRAMS.items():
        symbols.append(f'<symbol id="dg-{name}" viewBox="0 0 {W} {H}">{fn()}</symbol>')
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" width="0" height="0" '
        'style="position:absolute;overflow:hidden" aria-hidden="true">'
        '<defs>' + ''.join(symbols) + '</defs></svg>'
    )
    with open(out, 'w', encoding='utf-8') as f:
        f.write(svg + '\n')
    print(f'wrote {out} ({len(DIAGRAMS)} diagrams, {len(svg)} bytes)')


if __name__ == '__main__':
    main()
