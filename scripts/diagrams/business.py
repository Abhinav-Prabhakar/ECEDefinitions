"""Diagram family: business, strategy and living systems."""

import math

from .base import *

# The preview sheet does not define the theme variable; keep the accent visible
# there while still following the page accent wherever it is set.
ACCENT = 'var(--accent,#5b6ee1)'


# --------------------------------------------------------------------------
# Strategy and markets
# --------------------------------------------------------------------------

def product_lifecycle():
    pts = [
        (32, 120), (46, 118), (58, 112), (70, 100), (82, 84), (94, 68),
        (106, 56), (120, 48), (136, 44), (150, 44), (162, 48), (174, 58),
        (186, 74), (198, 96), (208, 110),
    ]
    return ''.join([
        axis(28, 122, 212, 122, .5),
        axis(28, 122, 28, 32, .45),
        text(30, 28, 'SALES', 'start', .45),
        text(204, 114, 'TIME', 'end', .4),
        line(66, 122, 66, 40, .2, 1, '2 4'),
        line(110, 122, 110, 40, .2, 1, '2 4'),
        line(158, 122, 158, 40, .2, 1, '2 4'),
        curve(pts, .95, ACCENT, w=1.5),
        text(47, 136, 'INTRO', o=.42),
        text(88, 136, 'GROWTH', o=.42),
        text(134, 136, 'MATURITY', o=.42),
        text(186, 136, 'DECLINE', o=.42),
    ])


def cash_flow():
    base = 84
    inflow = [26, 20, 24, 30]
    outflow = [17, 21, 15, 12]
    out = [line(30, base, 210, base, .55)]
    for i in range(4):
        x = 40 + i * 42
        out.append(rect(x, base - inflow[i], 11, inflow[i], 1, .45))
        out.append(rect(x + 14, base, 9, outflow[i], 1, .3))
    out += [
        curve([(32, base), (45, 72), (87, 73), (129, 61), (171, 37)],
              .9, ACCENT, w=1.4),
        dot(171, 37, 2.2, .9, ACCENT),
        text(46, 40, 'INFLOW', 'start', .45),
        text(46, 138, 'OUTFLOW', 'start', .4),
        text(206, 30, 'CUMULATIVE', 'end', .45),
    ]
    return ''.join(out)


def business_model_canvas():
    return ''.join([
        rect(24, 34, 192, 82, 1, .5),
        line(64, 34, 64, 80, .35), line(108, 34, 108, 80, .35),
        line(140, 34, 140, 80, .35), line(178, 34, 178, 80, .35),
        line(64, 57, 108, 57, .3), line(140, 57, 178, 57, .3),
        line(24, 80, 216, 80, .4), line(120, 80, 120, 116, .35),
        text(44, 59, 'PARTNERS', o=.5, ls='.02em'),
        text(86, 47, 'ACTIVITIES', o=.45, ls='.02em'),
        text(86, 72, 'RESOURCES', o=.45, ls='.02em'),
        text(124, 59, 'VALUE', o=.65),
        line(111, 65, 137, 65, .7, 1, None, ACCENT),
        text(159, 72, 'CHANNELS', o=.45, ls='.02em'),
        text(197, 59, 'SEGMENTS', o=.45, ls='.02em'),
        text(72, 100, 'COSTS', o=.5), text(170, 100, 'REVENUE', o=.5),
    ])


def marketing_mix():
    return ''.join([
        circle(120, 78, 10, .9, ACCENT),
        text(120, 80.5, '4PS', o=.65, size=5.6, ls='.04em'),
        arrow(120, 66, 120, 47, .4), arrow(132, 78, 151, 78, .4),
        arrow(120, 90, 120, 108, .4), arrow(108, 78, 89, 78, .4),
        dot(120, 43, 2.2, .7), dot(157, 78, 2.2, .7),
        dot(120, 115, 2.2, .7), dot(83, 78, 2.2, .7),
        text(120, 26, 'PRODUCT', o=.55),
        text(176, 80, 'PRICE', 'start', .55),
        text(120, 134, 'PLACE', o=.55),
        text(64, 80, 'PROMOTION', 'end', .55),
    ])


def supply_chain():
    return ''.join([
        rect(26, 50, 36, 20, 2, .55), rect(76, 50, 36, 20, 2, .55),
        rect(126, 50, 36, 20, 2, .55), rect(176, 50, 36, 20, 2, .55),
        arrow(62, 60, 74, 60, .5, head=3.5),
        arrow(112, 60, 124, 60, .8, ACCENT, head=3.5),
        arrow(162, 60, 174, 60, .5, head=3.5),
        text(42, 86, 'SUPPLIER', o=.5, ls='0em'),
        text(92, 86, 'MANUFACTURER', o=.5, ls='0em'),
        text(147, 86, 'DISTRIBUTOR', o=.5, ls='0em'),
        text(196, 86, 'CUSTOMER', o=.5, ls='0em'),
        line(194, 100, 44, 100, .35, 1, '3 3'),
        path('M50 97 L44 100 L50 103', .35),
        text(120, 96, 'RETURNS', o=.35),
    ])


def org_structure():
    return ''.join([
        rect(96, 28, 48, 16, 2, .7, color=ACCENT),
        rect(30, 64, 40, 16, 2, .5), rect(100, 64, 40, 16, 2, .5),
        rect(170, 64, 40, 16, 2, .5),
        rect(94, 96, 16, 10, 1, .35), rect(130, 96, 16, 10, 1, .35),
        line(120, 44, 120, 54, .4), line(50, 54, 190, 54, .4),
        line(50, 54, 50, 64, .4), line(120, 54, 120, 64, .4),
        line(190, 54, 190, 64, .4),
        line(120, 80, 120, 88, .35), line(102, 88, 138, 88, .35),
        line(102, 88, 102, 96, .35), line(138, 88, 138, 96, .35),
        text(120, 39, 'CEO', o=.65),
        text(50, 75, 'OPS', o=.5), text(120, 75, 'FINANCE', o=.5),
        text(190, 75, 'SALES', o=.5),
    ])


def swot():
    return ''.join([
        rect(34, 32, 172, 88, 2, .5),
        line(120, 32, 120, 120, .38), line(34, 76, 206, 76, .38),
        text(77, 25, 'HELPFUL', o=.35), text(163, 25, 'HARMFUL', o=.35),
        text(77, 57, 'STRENGTHS', o=.6),
        line(58, 63, 96, 63, .7, 1, None, ACCENT),
        text(163, 57, 'WEAKNESSES', o=.45),
        text(77, 101, 'OPPORTUNITIES', o=.45),
        text(163, 101, 'THREATS', o=.45),
    ])


def porters_five():
    return ''.join([
        rect(98, 62, 44, 24, 2, .8, color=ACCENT),
        rect(92, 28, 56, 18, 2, .5), rect(22, 62, 50, 18, 2, .5),
        rect(168, 62, 50, 18, 2, .5), rect(86, 106, 68, 18, 2, .5),
        arrow(120, 46, 120, 60, .45, head=3), arrow(120, 106, 120, 88, .45, head=3),
        arrow(72, 73, 96, 73, .45, head=3), arrow(168, 73, 144, 73, .45, head=3),
        text(120, 77, 'RIVALRY', o=.7),
        text(120, 40, 'NEW ENTRANTS', o=.5),
        text(47, 73, 'SUPPLIERS', o=.5), text(193, 73, 'BUYERS', o=.5),
        text(120, 117, 'SUBSTITUTES', o=.5),
    ])


def design_thinking():
    cx, cy, r = 120, 82, 40
    angs = [-90, -18, 54, 126, 198]
    labels = ['EMPATHISE', 'DEFINE', 'IDEATE', 'PROTOTYPE', 'TEST']
    out = []
    for a in angs:
        out.append(dot(cx + r * math.cos(math.radians(a)),
                       cy + r * math.sin(math.radians(a)), 2.6, .7))
    for i in range(5):
        a0 = angs[i] + 10
        a1 = angs[(i + 1) % 5] + (360 if i == 4 else 0) - 10
        out.append(arrow_arc(cx, cy, r, math.radians(a0), math.radians(a1),
                             .42, ACCENT, 3))
    for a, label in zip(angs, labels):
        out.append(text(cx + 60 * math.cos(math.radians(a)),
                        cy + 60 * math.sin(math.radians(a)) + 2,
                        label, o=.45))
    return ''.join(out)


# --------------------------------------------------------------------------
# Quantitative sketches
# --------------------------------------------------------------------------

def number_line():
    ticks = ''.join(f'M{x} 88 V96' for x in (48, 70, 92, 114, 136, 158, 180, 202))
    return ''.join([
        axis(120, 92, 210, 92, .5), axis(120, 92, 30, 92, .5),
        path(ticks, .35),
        path('M70 74 V66 H136 V74', .55),
        path('M114 106 V112 H202 V106', .35),
        circle(70, 92, 2.6, .6), circle(136, 92, 2.6, .6),
        text(103, 58, 'A', o=.55), text(158, 126, 'B', o=.45),
        dot(170, 92, 3, .9, ACCENT),
        line(170, 88, 170, 60, .55, 1, '1.5 3', ACCENT),
        text(170, 54, 'X', o=.8, color=ACCENT),
    ])


def probability_tree():
    root, n1, n2 = (32, 76), (102, 50), (102, 102)
    leaves = [(182, 28), (182, 66), (182, 86), (182, 124)]
    return ''.join([
        line(*root, *n1, .5), line(*root, *n2, .5),
        line(*n1, *leaves[0], .4), line(*n1, *leaves[1], .4),
        line(*n2, *leaves[2], .4), line(*n2, *leaves[3], .4),
        dot(*root, 2.8, .8), dot(*n1, 2.4, .6), dot(*n2, 2.4, .6),
        dot(*leaves[0], 2, .45), dot(*leaves[1], 2, .45),
        dot(*leaves[2], 2, .45), dot(*leaves[3], 2, .45),
        text(58, 60, 'P', o=.5), text(58, 102, '1-P', o=.45),
        text(138, 32, 'Q', o=.5), text(138, 69, '1-Q', o=.45),
        text(138, 88, 'Q', o=.45), text(138, 121, '1-Q', o=.4),
    ])


def bayes_tree():
    root, n1, n2 = (30, 82), (100, 56), (100, 108)
    leaves = [(176, 40), (176, 76), (176, 90), (176, 126)]
    return ''.join([
        line(*root, *n1, .7, color=ACCENT), line(*root, *n2, .5),
        line(*n1, *leaves[0], .55, color=ACCENT),
        line(*n1, *leaves[1], .4),
        line(*n2, *leaves[2], .4), line(*n2, *leaves[3], .4),
        dot(*root, 2.8, .8), dot(*n1, 2.4, .7), dot(*n2, 2.4, .6),
        dot(*leaves[0], 2.6, .85, ACCENT), dot(*leaves[1], 2, .45),
        dot(*leaves[2], 2, .45), dot(*leaves[3], 2, .45),
        text(30, 24, 'PRIOR', o=.5),
        text(100, 24, 'LIKELIHOOD', o=.5),
        text(176, 24, 'POSTERIOR', o=.8, color=ACCENT),
        text(62, 64, 'P', o=.45), text(62, 100, '1-P', o=.4),
    ])


def venn_3():
    return ''.join([
        circle(102, 60, 27, .55), circle(138, 60, 27, .55),
        circle(120, 88, 27, .55),
        path('M111 62.5 Q112 75 120 80 Q129 75 129 62.5 Q120 60.8 111 62.5 Z',
             .13, 1, None, ACCENT, ACCENT),
        path('M111 62.5 Q112 75 120 80', .7, 1, None, ACCENT),
        path('M120 80 Q129 75 129 62.5', .7, 1, None, ACCENT),
        path('M129 62.5 Q120 60.8 111 62.5', .7, 1, None, ACCENT),
        text(82, 66, 'A', o=.5), text(158, 66, 'B', o=.5),
        text(120, 108, 'C', o=.5),
    ])


# --------------------------------------------------------------------------
# Values, systems and environment
# --------------------------------------------------------------------------

def values_circle():
    return ''.join([
        circle(112, 74, 44, .3), circle(112, 74, 33, .4),
        circle(112, 74, 22, .5),
        circle(112, 74, 11, .85, ACCENT),
        text(112, 38, 'NATURE', o=.42),
        text(112, 49, 'SOCIETY', o=.45),
        text(112, 60, 'FAMILY', o=.5),
        text(112, 71, 'SELF', o=.6),
        dot(112, 74, 1.8, .5),
        text(112, 136, 'VALUES', o=.35),
    ])


def harmony_orders():
    arcs = []
    for r, o in ((68, .45), (52, .55), (36, .65), (20, .95)):
        arcs.append(path(f'M{120 - r} 118 A{r} {r} 0 0 1 {120 + r} 118',
                         o, 1.4 if r == 20 else 1,
                         None, ACCENT if r == 20 else INK))
    return ''.join([
        *arcs,
        line(26, 118, 214, 118, .4),
        text(120, 44, 'IV', o=.4),
        text(120, 60, 'III', o=.45),
        text(120, 76, 'II', o=.5),
        text(120, 92, 'I', o=.7, color=ACCENT),
        text(120, 138, 'ORDERS', o=.45),
    ])


def waste_hierarchy():
    left = lambda y: 42 + (y - 34) * (56 / 84)
    right = lambda y: 198 - (y - 34) * (56 / 84)
    ys = (50.8, 67.6, 84.4, 101.2)
    out = [path('M42 34 H198 L142 118 H98 Z', .45)]
    out.append(line(42, 34, 198, 34, .9, 1.4, None, ACCENT))
    for y in ys:
        out.append(line(left(y), y, right(y), y, .35))
    for label, y in (('REDUCE', 45), ('REUSE', 62), ('RECYCLE', 79),
                     ('RECOVER', 96), ('DISPOSE', 113)):
        out.append(text(120, y, label, o=.5))
    return ''.join(out)


def energy_pyramid():
    return ''.join([
        rect(45, 96, 150, 16, 1, .45),
        rect(66, 74, 108, 16, 1, .5),
        rect(85, 52, 70, 16, 1, .55),
        rect(97, 30, 46, 16, 1, .6),
        line(66, 90, 45, 96, .3), line(174, 90, 195, 96, .3),
        line(85, 68, 66, 74, .3), line(155, 68, 174, 74, .3),
        line(97, 46, 85, 52, .3), line(143, 46, 155, 52, .3),
        arrow(28, 112, 28, 26, .35, head=3),
        text(30, 138, 'ENERGY', 'start', .4),
        text(120, 106, 'PRODUCERS', o=.5),
        text(120, 84, 'PRIMARY', o=.5),
        text(120, 62, 'SECONDARY', o=.5),
        text(120, 40, 'TERTIARY', o=.5),
    ])


def environmental_pathway():
    return ''.join([
        rect(24, 62, 32, 24, 2, .55),
        text(40, 76, 'SOURCE', o=.5, ls='.04em'),
        path('M58 66 Q66 74 58 82', .4),
        path('M58 60 Q72 74 58 88', .22),
        sine(72, 152, 74, 9, 2, .85, ACCENT, '4 3'),
        arrow(152, 74, 166, 74, .85, ACCENT, head=3.5),
        rect(168, 58, 44, 32, 2, .6),
        dot(190, 74, 2.6, .8, ACCENT),
        text(112, 58, 'PATHWAY', o=.4),
        text(190, 102, 'RECEPTOR', o=.5),
    ])


DIAGRAMS = {
    'product-lifecycle': product_lifecycle,
    'cash-flow': cash_flow,
    'design-thinking': design_thinking,
    'business-model-canvas': business_model_canvas,
    'marketing-mix': marketing_mix,
    'supply-chain': supply_chain,
    'org-structure': org_structure,
    'swot': swot,
    'porters-five': porters_five,
    'number-line': number_line,
    'probability-tree': probability_tree,
    'bayes-tree': bayes_tree,
    'venn-3': venn_3,
    'values-circle': values_circle,
    'harmony-orders': harmony_orders,
    'waste-hierarchy': waste_hierarchy,
    'energy-pyramid': energy_pyramid,
    'environmental-pathway': environmental_pathway,
}
