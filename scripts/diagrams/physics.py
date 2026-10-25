"""Diagram family: physics.

Thin line art on the shared 240x150 grid. Structure in INK, the one thing the
definition is about in ACCENT. Labels are sparse and uppercase.
"""
from math import exp, radians

from .base import *


# --------------------------------------------------------------- local helpers

def _hspan(x1, x2, y, label='', o=.4, above=True):
    """Dimension line with end ticks and an optional centred label."""
    out = [line(x1, y, x2, y, o),
           line(x1, y - 3.5, x1, y + 3.5, o),
           line(x2, y - 3.5, x2, y + 3.5, o)]
    if label:
        out.append(amp((x1 + x2) / 2, y - 5 if above else y + 9, label, o + .15))
    return ''.join(out)


def _vspan(y1, y2, x, label='', o=.4, side='left', color=INK):
    out = [line(x, y1, x, y2, o, color=color),
           line(x - 3.5, y1, x + 3.5, y1, o, color=color),
           line(x - 3.5, y2, x + 3.5, y2, o, color=color)]
    if label:
        out.append(text(x - 7 if side == 'left' else x + 7, (y1 + y2) / 2 + 2, label,
                        'end' if side == 'left' else 'start', o + .15, color=color))
    return ''.join(out)


def _gauss(cx, base, peak, half, o=.7, color=INK):
    pts = []
    for i in range(25):
        t = -2.6 + 5.2 * i / 24
        pts.append((cx + half * t / 2.6, base - (base - peak) * exp(-t * t / 2)))
    return curve(pts, o, color)


# --------------------------------------------------------------------- quantum

def matter_wave():
    return ''.join([
        line(34, 86, 204, 86, .14, dash='1 4'),
        sine(72, 200, 86, 15, 3, .85, ACCENT),
        circle(54, 86, 5, .9, ACCENT, sw=1.3),
        dot(54, 86, 1.9, .95, ACCENT),
        _hspan(72, 114.7, 52, 'λ', .4),
        arrow(88, 118, 190, 118, .4, head=3.5),
        amp(80, 121, 'p', .5),
    ])


def uncertainty():
    return ''.join([
        line(122, 28, 122, 124, .16, dash='2 4'),
        line(26, 110, 110, 110, .4),
        _gauss(66, 110, 44, 26, .85, ACCENT),
        _hspan(52, 80, 120, 'Δx', .45, above=False),
        line(134, 110, 214, 110, .4),
        _gauss(174, 110, 68, 44, .6),
        _hspan(150, 198, 120, 'Δp', .45, above=False),
        amp(66, 26, 'POSITION', .4),
        amp(174, 26, 'MOMENTUM', .4),
    ])


def particle_box():
    return ''.join([
        line(56, 26, 56, 120, .9),
        line(184, 26, 184, 120, .9),
        line(56, 120, 184, 120, .4),
        axis(44, 118, 44, 30, .3),
        line(56, 108, 96, 108, .5),
        line(56, 84, 96, 84, .4),
        line(56, 60, 96, 60, .3),
        sine(56, 184, 84, 15, 1, .9, ACCENT),
        amp(44, 24, 'E', .45),
        _hspan(56, 184, 132, 'L', .35),
    ])


def energy_levels():
    return ''.join([
        axis(44, 128, 44, 26, .3),
        line(60, 112, 152, 112, .85),
        line(60, 78, 138, 78, .55),
        line(60, 46, 124, 46, .4),
        arrow(168, 46, 168, 78, .9, ACCENT, head=4, w=1.3),
        sine(176, 212, 62, 4, 2.5, .7, ACCENT),
        amp(38, 22, 'E', .45),
        amp(196, 78, 'hν', .5),
    ])


def laser_levels():
    return ''.join([
        line(40, 124, 100, 124, .85),
        line(40, 72, 100, 72, .7),
        line(40, 38, 100, 38, .45),
        arrow(56, 120, 56, 42, .8, ACCENT, head=4, w=1.3),
        arrow(80, 42, 80, 68, .4, head=3),
        arrow(96, 76, 96, 120, .95, ACCENT, head=4, w=1.4),
        sine(110, 190, 58, 4.5, 2.5, .75, ACCENT),
        sine(110, 190, 86, 4.5, 2.5, .5, ACCENT),
        text(32, 42, 'E3', 'end', .5),
        text(32, 76, 'E2', 'end', .5),
        text(32, 128, 'E1', 'end', .5),
        amp(56, 139, 'PUMP', .4),
        amp(202, 74, 'hν', .5),
    ])


def quantum_well():
    return ''.join([
        line(40, 120, 206, 120, .3),
        axis(40, 120, 40, 36, .3),
        line(66, 52, 66, 120, .65),
        line(106, 52, 106, 120, .65),
        line(128, 52, 128, 120, .65),
        line(200, 52, 200, 120, .65),
        line(66, 58, 106, 58, .85, w=1.2, color=ACCENT),
        line(66, 80, 106, 80, .35),
        line(128, 86, 200, 86, .85, w=1.2, color=ACCENT),
        line(128, 100, 200, 100, .35),
        amp(40, 30, 'E', .45),
        amp(86, 134, 'a', .45),
        amp(164, 134, '2a', .45),
    ])


def mo_diagram():
    return ''.join([
        line(34, 80, 72, 80, .65),
        line(168, 80, 206, 80, .65),
        line(96, 108, 144, 108, .9, w=1.2, color=ACCENT),
        line(96, 46, 144, 46, .55),
        line(72, 80, 96, 108, .28, dash='2 3'),
        line(72, 80, 96, 46, .28, dash='2 3'),
        line(168, 80, 144, 108, .28, dash='2 3'),
        line(168, 80, 144, 46, .28, dash='2 3'),
        arrow(53, 80, 53, 71, .55, head=2.5),
        arrow(187, 80, 187, 71, .55, head=2.5),
        arrow(113, 108, 113, 99, .55, head=2.5),
        arrow(127, 98, 127, 108, .55, head=2.5),
        amp(120, 120, 'σ', .55),
        amp(120, 38, 'σ*', .5),
    ])


def bragg():
    return ''.join([
        line(28, 62, 212, 62, .5),
        line(28, 96, 212, 96, .5),
        dot(84, 62, 2.2, .45),
        dot(156, 62, 2.2, .45),
        dot(84, 96, 2.2, .45),
        dot(156, 96, 2.2, .45),
        arrow(48, 22, 112, 62, .85, ACCENT, head=3.5),
        arrow(112, 62, 176, 22, .5, head=3.5),
        arrow(84, 66, 132, 96, .5, head=3.5),
        arrow(132, 96, 180, 66, .4, head=3.5),
        arrow_arc(112, 62, 26, radians(180), radians(212), .45, INK, head=2.5),
        _vspan(62, 96, 36, 'd', .4),
        amp(96, 56, 'θ', .5),
    ])


# -------------------------------------------------------------------- optical

def optical_fiber():
    return ''.join([
        line(40, 48, 198, 48, .22),
        line(40, 64, 198, 64, .5),
        line(40, 86, 198, 86, .5),
        line(40, 102, 198, 102, .22),
        line(40, 48, 40, 102, .45),
        line(198, 48, 198, 102, .3),
        path('M40 80 L74 64 L108 86 L142 64 L176 86 L198 68', .85, 1.3, color=ACCENT),
        arrow(20, 80, 38, 80, .5, head=3.5),
        amp(112, 59, 'CLADDING', .4),
        amp(150, 82, 'CORE', .5),
    ])


def fiber_na():
    return ''.join([
        rect(150, 66, 62, 18, 1, .6),
        line(150, 54, 212, 54, .22),
        line(150, 96, 212, 96, .22),
        line(150, 42, 150, 108, .5),
        arrow(58, 36, 148, 72, .8, ACCENT, head=3.5),
        arrow(58, 114, 148, 78, .4, head=3),
        line(46, 75, 148, 75, .3, dash='3 4'),
        arrow_arc(150, 75, 42, radians(180), radians(203), .55, ACCENT, head=2.5),
        amp(118, 68, 'θ', .6),
        amp(66, 30, 'NA', .45),
    ])


def attenuation():
    return ''.join([
        axis(36, 122, 214, 122, .3),
        axis(36, 122, 36, 30, .3),
        line(36, 44, 198, 108, .95, w=1.4, color=ACCENT),
        line(36, 78, 120, 78, .22, dash='2 4'),
        line(120, 78, 120, 122, .22, dash='2 4'),
        amp(28, 24, 'dB', .45),
        amp(208, 134, 'L', .45),
        amp(62, 47, 'α', .5),
    ])


# -------------------------------------------------------------------- magnetic

def hysteresis_loop():
    return ''.join([
        axis(120, 78, 120, 24, .3),
        axis(120, 78, 210, 78, .3),
        path('M52 118 C72 116 112 110 120 102 C128 94 136 88 150 78 '
             'C164 68 174 56 188 38', .75),
        path('M188 38 C168 40 128 46 120 54 C112 62 104 68 90 78 '
             'C76 88 66 100 52 118', .95, 1, color=ACCENT),
        line(188, 38, 197, 38, .3),
        line(43, 118, 52, 118, .3),
        dot(120, 54, 2, .8),
        dot(150, 78, 2, .8),
        amp(120, 20, 'B', .45),
        amp(212, 90, 'H', .4),
        text(112, 51, 'BR', 'end', .45),
        amp(150, 92, 'HC', .45),
    ])


def meissner_effect():
    return ''.join([
        path('M36 46 C66 46 70 24 96 24 L144 24 C172 24 174 46 196 46', .45),
        path('M36 66 C60 66 66 36 96 36 L144 36 C176 36 180 66 196 66', .35),
        path('M36 86 C60 86 66 116 96 116 L144 116 C176 116 180 86 196 86', .35),
        path('M36 106 C66 106 70 128 96 128 L144 128 C172 128 174 106 196 106', .45),
        arrow(196, 46, 207, 46, .45, head=3),
        arrow(196, 66, 207, 66, .35, head=3),
        arrow(196, 86, 207, 86, .35, head=3),
        arrow(196, 106, 207, 106, .45, head=3),
        rect(88, 48, 64, 56, 2, .9, color=ACCENT, sw=1.3),
        amp(36, 36, 'B', .5),
        text(120, 81, 'B = 0', 'middle', .55),
    ])


def cooper_pair():
    return ''.join([
        line(40, 38, 200, 38, .2, dash='1 4'),
        dot(48, 38, 2.4, .45),
        dot(72, 38, 2.4, .45),
        dot(96, 44, 2.4, .6),
        dot(120, 50, 2.4, .7),
        dot(144, 44, 2.4, .6),
        dot(168, 38, 2.4, .45),
        dot(192, 38, 2.4, .45),
        circle(96, 94, 6.5, .85, ACCENT, sw=1.2),
        circle(146, 94, 6.5, .85, ACCENT, sw=1.2),
        text(96, 96, '−', 'middle', .6, 8),
        text(146, 96, '−', 'middle', .6, 8),
        path('M98 87 C106 76 112 64 120 56', .35, dash='2 3', color=ACCENT),
        path('M144 87 C136 76 130 64 122 56', .35, dash='2 3', color=ACCENT),
        text(196, 28, 'LATTICE', 'end', .4),
        amp(121, 114, '2e−', .45),
    ])


def polarization_field():
    return ''.join([
        line(48, 40, 48, 112, .85),
        line(192, 40, 192, 112, .85),
        arrow(56, 50, 184, 50, .3, head=3),
        arrow(56, 114, 184, 114, .3, head=3),
        circle(73, 73, 2.2, .6),
        line(75, 72, 91, 68, .8, color=ACCENT),
        circle(111, 65, 2.2, .6),
        line(113, 64, 129, 60, .8, color=ACCENT),
        circle(151, 75, 2.2, .6),
        line(153, 74, 169, 70, .8, color=ACCENT),
        circle(89, 103, 2.2, .6),
        line(91, 102, 107, 98, .8, color=ACCENT),
        circle(155, 99, 2.2, .6),
        line(157, 98, 173, 94, .8, color=ACCENT),
        text(36, 84, '+', 'middle', .6, 9),
        text(204, 84, '−', 'middle', .6, 9),
        amp(120, 36, 'E', .5),
    ])


# ------------------------------------------------------------------- solid state

def energy_bands():
    return ''.join([
        rect(36, 34, 156, 22, 1.5, .13, fill=INK),
        rect(36, 94, 156, 22, 1.5, .13, fill=INK),
        line(56, 38, 62, 52, .3),
        line(88, 38, 94, 52, .3),
        line(120, 38, 126, 52, .3),
        line(152, 38, 158, 52, .3),
        line(56, 98, 62, 112, .3),
        line(88, 98, 94, 112, .3),
        line(120, 98, 126, 112, .3),
        line(152, 98, 158, 112, .3),
        _vspan(56, 94, 206, '', .6, side='right', color=ACCENT),
        text(198, 78, 'Eg', 'end', .6, color=ACCENT),
        amp(114, 28, 'CONDUCTION', .4),
        amp(114, 130, 'VALENCE', .4),
    ])


def doping_bands():
    return ''.join([
        rect(36, 30, 156, 20, 1.5, .2, fill=INK),
        rect(36, 100, 156, 20, 1.5, .2, fill=INK),
        line(60, 66, 104, 66, .55, dash='3 3', color=ACCENT),
        line(132, 88, 176, 88, .5, dash='3 3'),
        arrow(82, 66, 82, 51, .8, ACCENT, head=3),
        arrow(154, 99, 154, 89, .7, ACCENT, head=3),
        amp(114, 24, 'CONDUCTION', .4),
        amp(114, 134, 'VALENCE', .4),
        text(54, 70, 'D', 'end', .5),
        text(182, 92, 'A', 'start', .5),
    ])


def fermi_dirac():
    return ''.join([
        axis(32, 118, 208, 118, .3),
        axis(32, 118, 32, 30, .3),
        path('M32 44 L110 44 C116 44 117 58 118 80 C119 102 122 116 130 116 L200 116',
             .55, 1, dash='3 4'),
        path('M32 48 C82 48 106 46 120 78 C134 110 158 114 200 114', 1, 1.4, color=ACCENT),
        line(120, 44, 120, 118, .22, dash='2 4'),
        amp(28, 24, 'f(E)', .45),
        amp(204, 134, 'E', .45),
        amp(120, 134, 'Ef', .5),
        amp(86, 38, 'T = 0', .4),
        amp(176, 94, 'T > 0', .4),
    ])


def hall_effect():
    return ''.join([
        rect(50, 46, 140, 64, 2, .7),
        text(84, 81, '×', 'middle', .7, 8),
        text(120, 81, '×', 'middle', .7, 8),
        text(156, 81, '×', 'middle', .7, 8),
        arrow(62, 96, 176, 96, .75, head=4, w=1.2),
        text(120, 62, '+', 'middle', .6, 10),
        text(120, 106, '−', 'middle', .6, 10),
        line(198, 58, 198, 104, .9, color=ACCENT),
        line(198, 58, 202, 58, .9, color=ACCENT),
        line(198, 104, 202, 104, .9, color=ACCENT),
        text(207, 84, 'VH', 'start', .6, color=ACCENT),
        text(70, 84, 'B', 'end', .5),
        text(182, 100, 'I', 'start', .5),
    ])


def led_recombination():
    return ''.join([
        line(44, 44, 150, 44, .8),
        line(44, 100, 150, 100, .8),
        dot(78, 44, 3, .9, ACCENT),
        arrow(78, 50, 78, 94, .85, ACCENT, head=3.5, w=1.3),
        circle(78, 100, 4, .75),
        sine(104, 190, 66, 5, 2.5, .8, ACCENT),
        _vspan(44, 100, 36, '', .35),
        text(28, 76, 'Eg', 'end', .45),
        text(87, 41, 'e−', 'start', .45),
        text(68, 112, 'h+', 'middle', .45),
        text(196, 58, 'hν', 'end', .5),
    ])


# --------------------------------------------------------------------- matter

def crystal_lattice():
    return ''.join([
        rect(66, 54, 76, 54, 0, .7),
        rect(98, 30, 76, 54, 0, .28),
        line(66, 54, 98, 30, .4),
        line(142, 54, 174, 30, .4),
        line(66, 108, 98, 84, .4),
        line(142, 108, 174, 84, .4),
        dot(66, 54, 2.3, .55),
        dot(142, 54, 2.3, .55),
        dot(66, 108, 2.3, .55),
        dot(142, 108, 2.3, .55),
        dot(98, 30, 2.3, .4),
        dot(174, 30, 2.3, .4),
        dot(98, 84, 2.3, .4),
        dot(174, 84, 2.3, .4),
        _hspan(66, 142, 116, 'a', .35, above=False),
    ])


def polymer_chain():
    return ''.join([
        path('M28 80 L50 96 L72 80 L94 96 L116 80 L138 96 L160 80 L182 96 L204 80', .8, 1.1),
        dot(28, 80, 2.2, .4),
        dot(50, 96, 2.2, .45),
        dot(72, 80, 2.2, .45),
        dot(94, 96, 2.2, .5),
        dot(116, 80, 2.2, .5),
        dot(138, 96, 2.2, .5),
        dot(160, 80, 2.2, .45),
        dot(182, 96, 2.2, .45),
        dot(204, 80, 2.2, .4),
        line(94, 58, 94, 110, .5, color=ACCENT),
        line(138, 58, 138, 110, .5, color=ACCENT),
        line(94, 58, 99, 58, .5, color=ACCENT),
        line(94, 110, 99, 110, .5, color=ACCENT),
        line(138, 58, 133, 58, .5, color=ACCENT),
        line(138, 110, 133, 110, .5, color=ACCENT),
        line(72, 80, 72, 68, .3),
        line(160, 80, 160, 68, .3),
        amp(116, 54, 'n', .5),
    ])


def aromatic_ring():
    pts = [(120, 44), (151.2, 62), (151.2, 98), (120, 116), (88.8, 98), (88.8, 62)]
    d = 'M' + ' L'.join(f'{x} {y}' for x, y in pts) + ' Z'
    return ''.join([
        path(d, .85, 1.1),
        circle(120, 80, 21, .75, ACCENT, sw=1.1),
        *[dot(x, y, 2.1, .45) for x, y in pts],
        text(120, 83, 'π', 'middle', .6, 8),
    ])


def corrosion_cell():
    return ''.join([
        line(24, 96, 216, 96, .75),
        line(24, 120, 216, 120, .35),
        line(36, 112, 44, 120, .22),
        line(100, 112, 108, 120, .22),
        line(196, 112, 204, 120, .22),
        line(60, 96, 96, 96, .9, w=1.5, color=ACCENT),
        line(144, 96, 180, 96, .85, w=1.2),
        arrow(84, 108, 156, 108, .5, head=3.5),
        path('M148 96 C158 86 170 86 178 96', .55, color=ACCENT),
        arrow_arc(120, 86, 44, radians(180), radians(352), .55, ACCENT, head=3.5),
        amp(78, 134, 'ANODE', .45),
        amp(162, 134, 'CATHODE', .45),
        amp(120, 26, 'ELECTROLYTE', .4),
        text(196, 82, 'RUST', 'end', .45),
        amp(120, 115, 'e−', .4),
    ])


# ------------------------------------------------------------------- registry

DIAGRAMS = {
    'matter-wave': matter_wave,
    'uncertainty': uncertainty,
    'particle-box': particle_box,
    'energy-levels': energy_levels,
    'laser-levels': laser_levels,
    'optical-fiber': optical_fiber,
    'fiber-na': fiber_na,
    'attenuation': attenuation,
    'hysteresis-loop': hysteresis_loop,
    'meissner-effect': meissner_effect,
    'cooper-pair': cooper_pair,
    'polarization-field': polarization_field,
    'energy-bands': energy_bands,
    'doping-bands': doping_bands,
    'fermi-dirac': fermi_dirac,
    'hall-effect': hall_effect,
    'led-recombination': led_recombination,
    'quantum-well': quantum_well,
    'bragg': bragg,
    'mo-diagram': mo_diagram,
    'polymer-chain': polymer_chain,
    'aromatic-ring': aromatic_ring,
    'corrosion-cell': corrosion_cell,
    'crystal-lattice': crystal_lattice,
}
