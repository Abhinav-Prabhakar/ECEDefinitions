"""Diagram family: imaging and RF specifics."""
from .base import *


def histogram():
    bars = [8, 18, 34, 52, 64, 58, 40, 24, 12]
    out = [axis(28, 120, 214, 120, .45), axis(28, 120, 28, 24, .45)]
    bw = 17
    for i, v in enumerate(bars):
        out.append(rect(32 + i * (bw + 3), 120 - v, bw, v, 1, .35))
    pts = []
    total = sum(bars)
    run = 0
    for i, v in enumerate(bars):
        run += v
        pts.append((32 + i * (bw + 3) + bw / 2, 120 - 96 * run / total))
    out.append(curve(pts, .9, ACCENT, w=1.3))
    out.append(amp(120, 136, 'HISTOGRAM · CDF', o=.4, size=5))
    return ''.join(out)


def convolution_2d():
    out = []
    for r in range(5):
        for c in range(5):
            x, y = 34 + c * 17, 34 + r * 17
            on = 1 <= r <= 3 and 1 <= c <= 3
            out.append(rect(x, y, 15, 15, 1, .55 if on else .22,
                            color=ACCENT if on else INK,
                            fill='currentColor' if on else 'none'))
    out.append(arrow(126, 74, 154, 74, .5, head=3))
    for r in range(3):
        for c in range(3):
            out.append(rect(162 + c * 15, 56 + r * 15, 13, 13, 1, .5))
    out.append(amp(120, 130, 'KERNEL · NEIGHBOURHOOD', o=.4, size=5))
    out.append(amp(190, 114, 'OUT', o=.35, size=4.4))
    return ''.join(out)


def edge_detection():
    out = [
        axis(28, 78, 214, 78, .35), axis(28, 78, 28, 24, .35),
    ]
    for r in range(3):
        for c in range(6):
            x, y = 44 + c * 24, 30 + r * 14
            dark = c >= 3
            out.append(rect(x, y, 22, 12, 1, .55 if dark else .25,
                            fill='currentColor' if dark else 'none'))
    out.append(arrow(112, 86, 112, 116, .45, head=3))
    out.append(path('M32 116 V104 H108 V92 H124 V84 H212', .9, 1.4, color=ACCENT))
    out.append(line(108, 116, 108, 92, .3, 1, '2 4'))
    out.append(amp(120, 134, 'INTENSITY STEP → GRADIENT', o=.4, size=5))
    return ''.join(out)


def smith_chart():
    import math
    out = [
        circle(120, 75, 50, .55),
        line(62, 75, 178, 75, .3), line(120, 17, 120, 133, .3),
    ]
    # constant-resistance circles, clipped roughly inside the unit circle
    for r in [.25, .5, 1, 2, 4]:
        cx = 120 + 50 * (r / (1 + r))
        rr = 50 / (1 + r)
        out.append(circle(cx, 75, rr, .22))
    # a few reactance arcs
    for k in [.5, 1, 2]:
        out.append(path(f'M120 75 A {50 * k} {50 * k} 0 0 1 120 {75 - 50 * k}', .2))
        out.append(path(f'M120 75 A {50 * k} {50 * k} 0 0 0 120 {75 + 50 * k}', .2))
    out.append(dot(146, 55, 3, 1, ACCENT))
    out.append(circle(120, 75, math.hypot(146 - 120, 55 - 75), .5, ACCENT, 'none', 1))
    out.append(line(120, 75, 146, 55, .6, 1, '2 3', ACCENT))
    out.append(amp(120, 144, 'SMITH CHART · Γ', o=.4, size=5))
    return ''.join(out)


def waveguide():
    return ''.join([
        rect(44, 38, 152, 72, 2, .7),
        path('M44 74 H196', .3, 1, '2 4'),
        *[path(f'M{x} 38 V110', .3) for x in [70, 96, 122, 148, 174]],
        sine(58, 182, 74, 26, 1.5, .9),
        arrow(44, 128, 196, 128, .45, ACCENT, 3),
        amp(120, 140, 'RECTANGULAR WAVEGUIDE · TE₁₀', o=.4, size=4.6),
        amp(120, 26, 'b', o=.4, size=4.4),
        amp(208, 76, 'a', o=.4, size=4.4),
    ])


DIAGRAMS = {
    'histogram': histogram,
    'convolution-2d': convolution_2d,
    'edge-detection': edge_detection,
    'smith-chart': smith_chart,
    'waveguide': waveguide,
}
