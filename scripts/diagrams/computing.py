"""Diagram family: computing."""
from .base import *


def _bits(x0, y, seq, h=14, o=.7, color=INK, w=1):
    """Digital waveform from [(width, level), ...]; level 1 is high."""
    pts = []
    x = x0
    for width, level in seq:
        yy = y - h if level else y
        pts.append((x, yy))
        pts.append((x + width, yy))
        x += width
    return path('M' + ' L'.join(f'{px:.1f},{py:.1f}' for px, py in pts), o, w, color=color)


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

def hash_table():
    return ''.join([
        rect(20, 62, 34, 20, 1, .55),
        text(37, 75, 'KEY', o=.6, size=5.6),
        arrow(54, 72, 90, 72, .9, ACCENT, 4),
        amp(72, 63, 'HASH', o=.5),
        rect(92, 30, 40, 92, 1, .6),
        line(92, 53, 132, 53, .35),
        line(92, 76, 132, 76, .35),
        line(92, 99, 132, 99, .35),
        rect(92, 53, 40, 23, 1, .9, color=ACCENT),
        arrow(132, 64.5, 146, 64.5, .6, head=3),
        rect(146, 57, 28, 15, 1, .55),
        arrow(174, 64.5, 184, 64.5, .45, head=3),
        rect(184, 57, 28, 15, 1, .45),
    ])


def heap():
    out = [
        grid(24, 44, 7, 1, 17, 20, .3),
        rect(24, 44, 17, 20, 1, .9, color=ACCENT),
        amp(83, 78, 'ARRAY', o=.45),
    ]
    # binary heap layout of the same seven slots
    pairs = [((178, 32), (158, 62)), ((178, 32), (198, 62)),
             ((158, 62), (146, 94)), ((158, 62), (170, 94)),
             ((198, 62), (186, 94)), ((198, 62), (210, 94))]
    for (x1, y1), (x2, y2) in pairs:
        out.append(line(x1, y1, x2, y2, .35))
    for (x, y) in [(178, 32), (158, 62), (198, 62)]:
        out.append(circle(x, y, 8.5, .55))
    for (x, y) in [(146, 94), (170, 94), (186, 94), (210, 94)]:
        out.append(circle(x, y, 7.5, .4))
    out.append(circle(178, 32, 11, .95, ACCENT, sw=1.2))
    return ''.join(out)


def sorting():
    unsorted = [.6, .3, .85, .2, .7, .45]
    ordered = [.2, .3, .45, .6, .7, .85]
    return ''.join([
        axis(24, 100, 24, 40, .3),
        line(24, 96, 216, 96, .4),
        bars(30, 46, unsorted, 8, 4, 50, .55),
        arrow(108, 62, 136, 62, .9, ACCENT, 4),
        bars(148, 46, ordered, 8, 4, 50, .55, accent_last=True),
        amp(64, 112, 'UNSORTED', o=.45),
        amp(182, 112, 'SORTED', o=.45),
        line(130, 48, 130, 92, .2, 1, '2 4'),
        line(30, 100, 30, 104, .3),
        line(202, 100, 202, 104, .3),
    ])


def recursion_tree():
    edges = [((120, 26), (78, 60)), ((120, 26), (162, 60)),
             ((78, 60), (54, 96)), ((78, 60), (102, 96)),
             ((162, 60), (138, 96)), ((162, 60), (186, 96))]
    out = [line(x1, y1, x2, y2, .35) for (x1, y1), (x2, y2) in edges]
    out += [circle(120, 26, 10, .7), circle(78, 60, 9, .55), circle(162, 60, 9, .55)]
    out += [circle(x, 96, 8, .4) for x in (54, 102, 138, 186)]
    out += [circle(102, 96, 11, .9, ACCENT), circle(138, 96, 11, .9, ACCENT)]
    out += [line(102, 112, 138, 112, .7, 1, '2 3', ACCENT)]
    out += [amp(120, 126, 'REPEAT', o=.55)]
    return ''.join(out)


def dp_table():
    cells = [(0, 3), (1, 2), (2, 1), (3, 0)]
    centers = [(68 + 24 * c, 40 + 20 * r) for c, r in cells]
    out = [grid(56, 30, 5, 4, 24, 20, .28)]
    for c, r in cells:
        out.append(rect(56 + 24 * c, 30 + 20 * r, 24, 20, 0, .9, color=ACCENT))
    out.append(path('M' + ' L'.join(f'{x} {y}' for x, y in centers), .45, 1, '2 3', ACCENT))
    out.append(arrow(34, 100, 56, 100, .5, head=3))
    out.append(dot(68, 100, 2.2, .9, ACCENT))
    out.append(dot(140, 40, 2.2, .7, ACCENT))
    out.append(amp(120, 128, 'DP TABLE', o=.4))
    return ''.join(out)


def kmap():
    out = [grid(68, 38, 4, 4, 24, 20, .3)]
    for i, s in enumerate(['00', '01', '11', '10']):
        out.append(text(80 + i * 24, 32, s, 'middle', .45, 5.6, '.06em'))
        out.append(text(60, 50 + i * 20, s, 'end', .45, 5.6, '.06em'))
    out.append(rect(92, 78, 48, 40, 10, .9, color=ACCENT, sw=1.4))
    for x, y in [(104, 88), (128, 88), (104, 108), (128, 108)]:
        out.append(dot(x, y, 1.9, .85, ACCENT))
    return ''.join(out)


# ---------------------------------------------------------------------------
# Digital building blocks
# ---------------------------------------------------------------------------

def shift_register():
    out = [rect(28 + i * 52, 56, 32, 34, 2, .65) for i in range(4)]
    out += [amp(44 + i * 52, 78, 'D FF', o=.55) for i in range(4)]
    out.append(arrow(16, 73, 28, 73, .9, ACCENT, 3))
    out += [arrow(60 + i * 52, 73, 80 + i * 52, 73, .55, head=3) for i in range(3)]
    out.append(line(24, 108, 220, 108, .45))
    out += [line(44 + i * 52, 90, 44 + i * 52, 108, .4) for i in range(4)]
    out += [line(44 + i * 52, 56, 44 + i * 52, 40, .35) for i in range(3)]
    out += [dot(44 + i * 52, 40, 1.8, .55) for i in range(3)]
    out.append(amp(18, 64, 'IN', o=.55))
    out.append(amp(18, 122, 'CLK', o=.5))
    return ''.join(out)


def counter_timing():
    clk = [(11, lv) for lv in [1, 0] * 8]
    q0 = [(22, lv) for lv in [0, 1, 0, 1, 0, 1, 0, 1]]
    q1 = [(44, lv) for lv in [0, 1, 0, 1]]
    q2 = [(88, lv) for lv in [0, 1]]
    out = [
        _bits(36, 40, clk, 11, .6),
        _bits(36, 64, q0, 11, .7),
        _bits(39, 88, q1, 11, .55),
        _bits(42, 112, q2, 11, .55),
    ]
    for i, name in enumerate(['CLK', 'Q0', 'Q1', 'Q2']):
        out.append(text(30, 43 + i * 24, name, 'end', .55, 5.6, '.06em'))
    out.append(line(124, 28, 124, 120, .7, 1, '3 4', ACCENT))
    out.append(line(130, 28, 130, 120, .7, 1, '3 4', ACCENT))
    out.append(arrow(124, 122, 130, 122, .8, ACCENT, 3))
    out.append(amp(152, 126, 'SKEW', o=.55))
    return ''.join(out)


def state_machine():
    return ''.join([
        circle(62, 94, 16, .65),
        circle(124, 52, 16, .65),
        circle(178, 104, 16, .65),
        arrow(22, 94, 44, 94, .9, ACCENT, 3),
        arrow(76, 84, 110, 64, .9, ACCENT, 3),
        arrow(138, 62, 166, 90, .55, head=3),
        arrow(164, 114, 78, 103, .55, head=3),
        amp(62, 96, 'S0', o=.65),
        amp(124, 54, 'S1', o=.65),
        amp(178, 106, 'S2', o=.65),
        amp(84, 66, '0', o=.5),
        amp(166, 74, '1', o=.5),
        amp(126, 118, '1', o=.5),
    ])


# ---------------------------------------------------------------------------
# Operating systems
# ---------------------------------------------------------------------------

def paging():
    out = [rect(24, 28 + i * 26, 48, 20, 1, .5) for i in range(4)]
    out += [rect(168, 28 + i * 26, 48, 20, 1, .4) for i in range(4)]
    out += [arrow(72, 38, 168, 90, .9, ACCENT, 3, 1.2),
            arrow(72, 64, 168, 38, .5, head=3),
            arrow(72, 116, 168, 116, .5, head=3)]
    out += [line(72, 90, 104, 90, .45, 1, '3 4'),
            line(108, 86, 114, 94, .45),
            line(108, 94, 114, 86, .45)]
    out.append(text(48, 20, 'VIRTUAL', 'middle', .55, 5.6, '.08em'))
    out.append(text(192, 20, 'PHYSICAL', 'middle', .55, 5.6, '.08em'))
    out.append(text(105, 82, 'UNMAPPED', 'middle', .4, 5.6, '.06em'))
    return ''.join(out)


def segmentation():
    return ''.join([
        rect(28, 30, 64, 30, 1, .6),
        rect(28, 64, 64, 22, 1, .55),
        rect(28, 90, 64, 26, 1, .55),
        rect(148, 30, 64, 30, 1, .6),
        rect(148, 74, 64, 22, 1, .5),
        rect(148, 104, 64, 20, 1, .5),
        amp(60, 48, 'CODE', o=.6),
        amp(60, 78, 'DATA', o=.6),
        amp(60, 106, 'STACK', o=.6),
        amp(180, 20, 'PHYSICAL', o=.45),
        arrow(92, 45, 148, 45, .5, head=3),
        arrow(92, 75, 148, 85, .5, head=3),
        arrow(92, 103, 148, 114, .9, ACCENT, 3, 1.2),
    ])


def disk_layout():
    out = [circle(96, 76, 50, .6), circle(96, 76, 36, .22), circle(96, 76, 22, .22)]
    for a in (0.6, 2.17, 3.74, 5.31):
        out.append(line(96 + 7 * math.cos(a), 76 + 7 * math.sin(a),
                        96 + 50 * math.cos(a), 76 + 50 * math.sin(a), .28))
    out += [line(206, 124, 136, 52, .85, 1.4, color=ACCENT),
            dot(136, 52, 3, .95, ACCENT),
            dot(96, 76, 3, .55),
            dot(206, 124, 2.5, .6)]
    out += [text(96, 20, 'TRACK', 'middle', .45, 5.6, '.08em'),
            text(174, 22, 'SECTOR', 'middle', .45, 5.6, '.08em'),
            text(216, 116, 'ARM', 'end', .5, 5.6, '.08em')]
    out += [line(150, 26, 128, 42, .25)]
    return ''.join(out)


def scheduling():
    return ''.join([
        axis(28, 120, 216, 120, .4),
        *[line(x, 116, x, 124, .35) for x in (52, 88, 124, 160, 196)],
        rect(48, 26, 44, 14, 1, .55),
        rect(74, 52, 50, 14, 1, .5),
        rect(58, 78, 52, 14, 1, .55),
        line(104, 22, 104, 116, .4, 1, '3 4'),
        line(136, 48, 136, 116, .4, 1, '3 4'),
        line(96, 74, 96, 116, .9, 1, '3 4', ACCENT),
        text(20, 37, 'T1', 'start', .5, 5.6, '.06em'),
        text(20, 63, 'T2', 'start', .5, 5.6, '.06em'),
        text(20, 89, 'T3', 'start', .5, 5.6, '.06em'),
        text(206, 134, 'DEADLINE', 'end', .45, 5.6, '.08em'),
    ])


def deadlock():
    return ''.join([
        circle(62, 42, 16, .6),
        circle(166, 108, 16, .6),
        rect(150, 28, 32, 28, 1, .6),
        rect(46, 94, 32, 28, 1, .6),
        arrow(78, 42, 150, 42, .9, ACCENT, 3, 1.2),
        arrow(166, 56, 166, 92, .9, ACCENT, 3, 1.2),
        arrow(150, 108, 78, 108, .9, ACCENT, 3, 1.2),
        arrow(62, 92, 62, 58, .9, ACCENT, 3, 1.2),
        amp(62, 44, 'P1', o=.7),
        amp(166, 110, 'P2', o=.7),
        amp(166, 45, 'R1', o=.65),
        amp(62, 111, 'R2', o=.65),
        dot(174, 50, 1.8, .5),
        dot(70, 116, 1.8, .5),
    ])


def file_system():
    return ''.join([
        rect(24, 22, 48, 20, 1, .55),
        rect(24, 64, 48, 20, 1, .55),
        arrow(48, 42, 48, 64, .45, head=3),
        rect(104, 52, 44, 46, 1, .65),
        arrow(72, 74, 104, 74, .9, ACCENT, 3),
        rect(172, 36, 40, 18, 1, .4),
        rect(172, 62, 40, 18, 1, .4),
        rect(172, 88, 40, 18, 1, .4),
        arrow(148, 62, 172, 45, .5, head=3),
        arrow(148, 75, 172, 71, .5, head=3),
        arrow(148, 88, 172, 97, .5, head=3),
        dot(140, 62, 1.8, .5),
        dot(140, 75, 1.8, .5),
        dot(140, 88, 1.8, .5),
        amp(48, 35, 'DIR', o=.6),
        amp(48, 77, 'FILE', o=.6),
        amp(126, 76, 'INODE', o=.6),
    ])


# ---------------------------------------------------------------------------
# Networks
# ---------------------------------------------------------------------------

def ip_packet():
    return ''.join([
        rect(24, 58, 192, 32, 1, .65),
        line(52, 58, 52, 90, .45),
        line(78, 58, 78, 90, .45),
        line(100, 58, 100, 90, .45),
        line(124, 58, 124, 90, .45),
        rect(124, 58, 92, 32, 1, .9, color=ACCENT),
        amp(38, 77, 'VER', o=.6),
        amp(65, 77, 'LEN', o=.6),
        amp(89, 77, 'TTL', o=.6),
        amp(112, 77, 'PROTO', o=.6),
        amp(170, 77, 'PAYLOAD', o=.65),
        line(24, 52, 124, 52, .5),
        line(24, 48, 24, 52, .5),
        line(124, 48, 124, 52, .5),
        amp(74, 44, 'HEADER', o=.45),
    ])


def routing():
    nodes = {'S': (32, 108), 'A': (76, 50), 'B': (96, 104),
             'C': (148, 44), 'D': (166, 96), 'T': (212, 64)}
    edges = [('S', 'A'), ('S', 'B'), ('A', 'B'), ('A', 'C'),
             ('B', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'T'), ('D', 'T')]
    shortest = [('S', 'B'), ('B', 'D'), ('D', 'T')]
    out = [line(nodes[a][0], nodes[a][1], nodes[b][0], nodes[b][1], .28) for a, b in edges]
    out += [line(nodes[a][0], nodes[a][1], nodes[b][0], nodes[b][1], .95, 1.6, color=ACCENT)
            for a, b in shortest]
    out += [circle(x, y, 4.2, .55) for x, y in nodes.values()]
    out += [circle(32, 108, 6.5, .9, ACCENT), circle(212, 64, 6.5, .9, ACCENT)]
    out += [amp(24, 122, 'S', o=.6), amp(218, 56, 'T', o=.6)]
    return ''.join(out)


def csma():
    return ''.join([
        axis(28, 126, 216, 126, .35),
        *[line(x, 122, x, 130, .3) for x in (52, 88, 124, 160, 196)],
        rect(44, 37, 40, 14, 1, .55),
        rect(58, 61, 26, 14, 1, .5),
        rect(70, 85, 14, 14, 1, .5),
        rect(112, 37, 40, 14, 1, .6),
        rect(88, 61, 34, 12, 0, .4, dash='3 3'),
        rect(92, 85, 42, 12, 0, .4, dash='3 3'),
        line(80, 54, 88, 62, .9, 1.2, color=ACCENT),
        line(88, 54, 80, 62, .9, 1.2, color=ACCENT),
        text(22, 48, 'A', 'start', .55, 5.6, '.06em'),
        text(22, 72, 'B', 'start', .55, 5.6, '.06em'),
        text(22, 96, 'C', 'start', .55, 5.6, '.06em'),
        amp(148, 67, 'BACKOFF', o=.45),
    ])


# ---------------------------------------------------------------------------
# Computer architecture
# ---------------------------------------------------------------------------

def dma():
    return ''.join([
        rect(28, 26, 58, 32, 2, .6),
        rect(152, 26, 62, 32, 2, .6),
        rect(86, 90, 68, 28, 2, .7),
        rect(28, 94, 42, 24, 2, .55),
        line(24, 74, 216, 74, .5),
        line(57, 58, 57, 74, .45),
        line(183, 58, 183, 74, .45),
        path('M120 90 V74 H183 V58', .9, 1.3, color=ACCENT),
        arrow(70, 102, 86, 102, .5, head=3),
        arrow(86, 110, 70, 110, .35, head=3),
        amp(57, 46, 'CPU', o=.65),
        amp(183, 46, 'MEM', o=.65),
        amp(120, 108, 'DMA', o=.7),
        amp(49, 109, 'DEV', o=.6),
    ])


def interrupt_flow():
    return ''.join([
        rect(24, 34, 50, 24, 2, .6),
        rect(100, 34, 52, 24, 2, .6),
        rect(100, 78, 52, 14, 0, .4),
        rect(100, 92, 52, 14, 0, .9, color=ACCENT),
        rect(100, 106, 52, 14, 0, .4),
        rect(176, 86, 42, 24, 2, .65),
        arrow(74, 46, 100, 46, .9, ACCENT, 3),
        arrow(126, 58, 126, 78, .45, head=3),
        arrow(152, 99, 176, 99, .9, ACCENT, 3),
        amp(49, 49, 'DEV', o=.65),
        amp(126, 49, 'PIC', o=.65),
        amp(197, 101, 'ISR', o=.65),
        amp(87, 38, 'IRQ', o=.5),
        amp(126, 134, 'VECTOR TABLE', o=.45),
    ])


def uart_frame():
    data = [1, 0, 1, 1, 0, 0, 1, 0]
    levels = [0] + data + [0, 1]
    seq = [(6, 1)] + [(15.8, lv) for lv in levels] + [(6, 1)]
    out = [_bits(27, 74, seq, 13, .75)]
    out += [line(33 + i * 15.8, 54, 33 + i * 15.8, 78, .22) for i in range(1, 11)]
    out += [line(33, 74, 48.8, 74, .95, 1.5, color=ACCENT),
            line(33, 61, 33, 74, .95, 1.5, color=ACCENT)]
    out += [text(40.9, 92, 'START', 'middle', .6, 5.6, '.06em'),
            text(112, 104, 'DATA', 'middle', .55, 5.6, '.08em'),
            text(183, 104, 'PARITY', 'middle', .55, 5.6, '.06em'),
            text(198.9, 92, 'STOP', 'middle', .6, 5.6, '.06em')]
    return ''.join(out)


def i2c_bus():
    scl = [(22, 1)] + [(7.5, 0), (7.5, 1)] * 10 + [(10, 1)]
    sda = [(20, 1), (17, 0)] + [(15, lv) for lv in [1, 0, 1, 0, 1, 1]] + \
          [(15, 0), (15, 0), (25, 1)]
    return ''.join([
        _bits(30, 104, scl, 12, .6),
        _bits(30, 64, sda, 12, .75),
        line(50, 30, 50, 120, .35, 1, '3 4', ACCENT),
        line(110, 30, 110, 120, .25, 1, '3 4'),
        line(172, 30, 172, 120, .25, 1, '3 4'),
        line(50, 64, 50, 76, .95, 1.5, color=ACCENT),
        text(24, 58, 'SDA', 'start', .6, 5.6, '.06em'),
        text(24, 98, 'SCL', 'start', .6, 5.6, '.06em'),
        amp(57, 26, 'START', o=.55),
        amp(119, 26, 'ADDR', o=.45),
        amp(182, 26, 'ACK', o=.55),
    ])


def spi_bus():
    return ''.join([
        rect(28, 54, 50, 40, 2, .65),
        rect(162, 54, 50, 40, 2, .65),
        arrow(78, 62, 162, 62, .95, ACCENT, 3),
        arrow(162, 76, 78, 76, .45, head=3),
        arrow(78, 90, 162, 90, .45, head=3),
        arrow(78, 104, 162, 104, .45, head=3),
        amp(120, 57, 'MOSI', o=.6),
        amp(120, 71, 'MISO', o=.5),
        amp(120, 85, 'SCLK', o=.5),
        amp(120, 99, 'CS', o=.5),
        amp(53, 75, 'MASTER', o=.65),
        amp(187, 75, 'SLAVE', o=.65),
    ])


# ---------------------------------------------------------------------------
# Hardware design flow
# ---------------------------------------------------------------------------

def fpga():
    out = [rect(x, y, 22, 17, 1, .5) for x in (70, 102, 134) for y in (32, 58, 84)]
    out += [rect(34, y, 11, 12, 1, .45) for y in (34, 86)]
    out += [rect(195, y, 11, 12, 1, .45) for y in (34, 86)]
    out += [line(45, 40, 70, 40, .35), line(45, 92, 70, 92, .35),
            line(156, 40, 195, 40, .35), line(156, 92, 195, 92, .35)]
    out += [line(58, 53, 168, 53, .2), line(58, 79, 168, 79, .2),
            line(97, 22, 97, 114, .2), line(129, 22, 129, 114, .2)]
    out.append(path('M45 92 H60 V79 H168 V92 H195', .95, 1.3, color=ACCENT))
    out += [amp(81, 43, 'CLB', o=.5), amp(39, 30, 'IO', o=.45)]
    return ''.join(out)


def asic_flow():
    return ''.join([
        rect(24, 52, 32, 28, 2, .55),
        rect(64, 52, 32, 28, 2, .6),
        rect(104, 52, 32, 28, 2, .6),
        rect(144, 52, 32, 28, 2, .9, color=ACCENT),
        rect(184, 52, 32, 28, 2, .55),
        amp(40, 69, 'SPEC', o=.6),
        amp(80, 69, 'RTL', o=.6),
        amp(120, 69, 'SYNTH', o=.6),
        amp(160, 69, 'P&R', o=.7),
        amp(200, 69, 'FAB', o=.6),
        arrow(56, 66, 64, 66, .45, head=3),
        arrow(96, 66, 104, 66, .45, head=3),
        arrow(136, 66, 144, 66, .45, head=3),
        arrow(176, 66, 184, 66, .45, head=3),
        path('M160 80 V106 H120', .45, 1, '3 4'),
        arrow(120, 106, 120, 80, .45, head=3),
        amp(146, 116, 'TIMING', o=.4),
    ])


def verification_flow():
    return ''.join([
        rect(92, 16, 56, 15, 2, .65),
        rect(92, 40, 56, 15, 2, .65),
        rect(92, 64, 56, 15, 2, .65),
        rect(58, 94, 48, 15, 2, .55),
        rect(134, 94, 48, 15, 2, .55),
        rect(92, 118, 56, 15, 2, .9, color=ACCENT, sw=1.3),
        line(120, 31, 120, 40, .4),
        line(120, 55, 120, 64, .4),
        line(106, 79, 82, 94, .4),
        line(134, 79, 158, 94, .4),
        line(82, 109, 102, 118, .4),
        line(158, 109, 138, 118, .4),
        amp(120, 26, 'TEST', o=.6),
        amp(120, 50, 'ENV', o=.6),
        amp(120, 74, 'AGENT', o=.6),
        amp(82, 104, 'DRIVER', o=.55),
        amp(158, 104, 'MONITOR', o=.55),
        amp(120, 128, 'DUT', o=.8),
    ])


DIAGRAMS = {
    'hash-table': hash_table,
    'heap': heap,
    'sorting': sorting,
    'recursion-tree': recursion_tree,
    'dp-table': dp_table,
    'kmap': kmap,
    'shift-register': shift_register,
    'counter-timing': counter_timing,
    'state-machine': state_machine,
    'paging': paging,
    'segmentation': segmentation,
    'disk-layout': disk_layout,
    'scheduling': scheduling,
    'deadlock': deadlock,
    'file-system': file_system,
    'ip-packet': ip_packet,
    'routing': routing,
    'csma': csma,
    'dma': dma,
    'interrupt-flow': interrupt_flow,
    'uart-frame': uart_frame,
    'i2c-bus': i2c_bus,
    'spi-bus': spi_bus,
    'fpga': fpga,
    'asic-flow': asic_flow,
    'verification-flow': verification_flow,
}
