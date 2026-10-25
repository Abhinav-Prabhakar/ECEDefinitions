"""Diagram family: software, data, AI and security."""

from .base import *


def er_diagram():
    return ''.join([
        rect(22, 38, 74, 56, 2, .5),
        line(22, 52, 96, 52, .4),
        dot(30, 58, 1.5, .9, ACCENT),
        line(36, 58, 84, 58, .26),
        line(30, 70, 78, 70, .26),
        line(30, 82, 66, 82, .26),
        rect(144, 38, 74, 56, 2, .5),
        line(144, 52, 218, 52, .4),
        line(158, 58, 206, 58, .26),
        line(152, 70, 200, 70, .26),
        line(152, 82, 186, 82, .26),
        path('M120 54 L136 68 L120 82 L104 68 Z', .85, color=ACCENT),
        line(96, 68, 104, 68, .5),
        line(136, 68, 138, 68, .5),
        line(100, 63, 100, 73, .5),
        line(138, 68, 144, 61, .5),
        line(138, 68, 144, 68, .5),
        line(138, 68, 144, 75, .5),
        text(59, 32, 'USER', 'middle', .48),
        text(181, 32, 'ORDER', 'middle', .48),
        text(120, 48, 'PLACES', 'middle', .48, 5.6),
        text(101, 60, '1', 'middle', .4, 5.6),
        text(141, 60, 'N', 'middle', .4, 5.6),
    ])


def normalization():
    return ''.join([
        rect(20, 42, 48, 42, 1.5, .5),
        grid(20, 42, 2, 3, 24, 14, .2),
        rect(23, 55, 42, 17, 1, .45, dash='2 3'),
        arrow(70, 63, 86, 63, .45, head=3),
        rect(86, 42, 48, 42, 1.5, .5),
        grid(86, 42, 2, 3, 24, 14, .2),
        line(110, 42, 110, 84, .8, color=ACCENT),
        line(110, 63, 134, 63, .4, dash='2 3'),
        arrow(136, 63, 152, 63, .45, head=3),
        rect(152, 42, 40, 28, 1.5, .5),
        grid(152, 42, 1, 2, 40, 14, .2),
        line(172, 70, 172, 76, .5),
        rect(152, 76, 40, 14, 1.5, .8, color=ACCENT),
        line(152, 83, 192, 83, .3),
        text(44, 102, '1NF', 'middle', .48),
        text(110, 102, '2NF', 'middle', .48),
        text(172, 102, '3NF', 'middle', .48),
    ])


def b_tree():
    return ''.join([
        rect(100, 24, 40, 18, 2, .55),
        line(120, 24, 120, 42, .32),
        rect(50, 62, 44, 18, 2, .5),
        line(72, 62, 72, 80, .32),
        rect(146, 62, 44, 18, 2, .5),
        line(168, 62, 168, 80, .32),
        rect(24, 102, 40, 16, 1.5, .5),
        rect(72, 102, 40, 16, 1.5, .5),
        rect(128, 102, 40, 16, 1.5, .5),
        rect(176, 102, 40, 16, 1.5, .5),
        line(110, 42, 72, 62, .4),
        line(130, 42, 168, 62, .4),
        line(66, 80, 44, 102, .4),
        line(80, 80, 92, 102, .4),
        line(158, 80, 148, 102, .4),
        line(174, 80, 196, 102, .4),
        line(44, 118, 44, 126, .32),
        line(92, 118, 92, 126, .32),
        line(148, 118, 148, 126, .32),
        line(196, 118, 196, 126, .32),
        line(44, 126, 196, 126, .48, dash='2 3'),
        text(92, 34, 'ROOT', 'end', .4),
        text(120, 140, 'LEAVES', 'middle', .4),
    ])


def transaction():
    return ''.join([
        text(38, 51, 'T1', 'end', .48),
        text(38, 83, 'T2', 'end', .48),
        rect(52, 43, 92, 9, 4, .55),
        rect(52, 75, 92, 9, 4, .55),
        dot(52, 47.5, 2, .7),
        dot(52, 79.5, 2, .7),
        dot(144, 47.5, 2.8, .95, ACCENT),
        dot(144, 79.5, 2.8, .95, ACCENT),
        line(52, 28, 52, 104, .28, dash='2 4'),
        line(144, 26, 144, 112, .5, dash='3 4', color=ACCENT),
        axis(24, 126, 214, 126, .38),
        line(72, 126, 72, 122, .28),
        line(104, 126, 104, 122, .28),
        line(136, 126, 136, 122, .28),
        text(52, 21, 'BEGIN', 'middle', .42),
        text(144, 21, 'COMMIT', 'middle', .5),
        text(214, 140, 'TIME', 'end', .42),
    ])


def sql_join():
    return ''.join([
        text(57, 22, 'ORDERS', 'middle', .45),
        rect(20, 30, 76, 46, 1.5, .5),
        line(20, 40, 96, 40, .38),
        line(78, 30, 78, 76, .72, color=ACCENT),
        line(20, 52, 96, 52, .2),
        line(20, 64, 96, 64, .2),
        text(87, 22, 'KEY', 'middle', .45),
        text(165, 22, 'USERS', 'middle', .45),
        rect(144, 30, 76, 46, 1.5, .5),
        line(144, 40, 220, 40, .38),
        line(160, 30, 160, 76, .72, color=ACCENT),
        line(144, 52, 220, 52, .2),
        line(144, 64, 220, 64, .2),
        arrow(87, 76, 113, 96, .5, head=3),
        arrow(153, 76, 127, 96, .5, head=3),
        dot(120, 98, 2.4, .85, ACCENT),
        arrow(120, 98, 120, 106, .6, head=3),
        rect(78, 106, 84, 30, 1.5, .55),
        line(78, 116, 162, 116, .38),
        grid(78, 116, 3, 2, 28, 10, .18),
        text(120, 113, 'JOINED', 'middle', .45, 5.6),
    ])


def cyber_attack():
    return ''.join([
        circle(30, 88, 9, .5),
        dot(30, 88, 2, .85),
        line(116, 26, 116, 122, .28, dash='3 4'),
        curve([(41, 84), (62, 58), (88, 74), (112, 54), (140, 84), (164, 64)],
              .8, ACCENT, dash='3 4'),
        dot(62, 58, 2, .75, ACCENT),
        dot(88, 74, 2, .75, ACCENT),
        dot(112, 54, 2, .75, ACCENT),
        dot(140, 84, 2, .75, ACCENT),
        arrow(164, 64, 184, 74, .8, ACCENT, head=4),
        rect(186, 62, 32, 26, 2, .5),
        line(186, 70, 218, 70, .3),
        line(192, 79, 212, 79, .2),
        text(30, 110, 'ATTACKER', 'middle', .45),
        text(202, 56, 'ASSET', 'middle', .45),
        text(116, 22, 'EDGE', 'middle', .4),
    ])


def encryption():
    return ''.join([
        line(22, 52, 62, 52, .5),
        line(22, 62, 54, 62, .5),
        line(22, 72, 58, 72, .5),
        arrow(66, 62, 84, 62, .45, head=3),
        curve([(90, 78), (95, 50), (100, 74), (105, 48), (110, 76),
               (115, 52), (120, 74), (125, 50), (130, 72)], .85, ACCENT),
        arrow(136, 62, 154, 62, .45, head=3),
        line(160, 52, 200, 52, .5),
        line(160, 62, 192, 62, .5),
        line(160, 72, 196, 72, .5),
        circle(108, 114, 5, .7, ACCENT),
        line(113, 114, 130, 114, .7, ACCENT),
        line(123, 114, 123, 119, .7, ACCENT),
        line(130, 114, 130, 118, .7, ACCENT),
        line(108, 109, 108, 94, .6, dash='2 2', color=ACCENT),
        text(40, 90, 'PLAINTEXT', 'middle', .42),
        text(112, 86, 'CIPHER', 'middle', .42),
        text(108, 136, 'KEY', 'middle', .42),
    ])


def pki():
    return ''.join([
        rect(24, 92, 56, 34, 2, .5),
        line(24, 102, 80, 102, .38),
        circle(68, 113, 4, .45),
        line(32, 112, 56, 112, .2),
        line(32, 120, 50, 120, .2),
        rect(94, 62, 56, 34, 2, .55),
        line(94, 72, 150, 72, .38),
        circle(138, 83, 4, .45),
        line(102, 82, 126, 82, .2),
        line(102, 90, 120, 90, .2),
        rect(164, 32, 56, 34, 2, .8, color=ACCENT),
        line(164, 42, 220, 42, .42),
        circle(208, 53, 4, .55, ACCENT),
        line(172, 52, 196, 52, .22),
        line(172, 60, 190, 60, .22),
        arrow(80, 96, 94, 84, .5, head=3),
        arrow(150, 66, 164, 54, .5, head=3),
        text(32, 99, 'ROOT CA', 'start', .5, 5.6),
        text(102, 69, 'INTER CA', 'start', .5, 5.6),
        text(172, 39, 'LEAF', 'start', .55, 5.6),
    ])


def firewall():
    return ''.join([
        rect(108, 26, 24, 34, 2, .5),
        rect(108, 86, 24, 38, 2, .5),
        line(108, 38, 132, 38, .28),
        line(108, 50, 132, 50, .28),
        line(108, 98, 132, 98, .28),
        line(108, 110, 132, 110, .28),
        line(120, 26, 120, 38, .24),
        line(114, 38, 114, 50, .24),
        line(126, 98, 126, 110, .24),
        circle(44, 73, 8, .5),
        line(44, 65, 44, 81, .28),
        line(36, 73, 52, 73, .28),
        rect(172, 52, 34, 11, 1.5, .5),
        rect(172, 68, 34, 11, 1.5, .5),
        dot(196, 57.5, 1.5, .6),
        dot(196, 73.5, 1.5, .6),
        arrow(56, 73, 166, 73, .85, ACCENT, head=4),
        arrow(40, 106, 100, 106, .55, head=3),
        line(102, 101, 110, 111, .65),
        line(110, 101, 102, 111, .65),
        text(66, 22, 'UNTRUSTED', 'middle', .42),
        text(189, 22, 'TRUSTED', 'middle', .42),
        text(120, 22, 'FILTER', 'middle', .42),
        text(108, 140, 'DENY', 'middle', .38),
    ])


def cnn():
    return ''.join([
        rect(22, 36, 42, 42, 1.5, .5),
        grid(22, 36, 3, 3, 14, 14, .2),
        rect(36, 50, 14, 14, 1, .85, color=ACCENT),
        arrow(68, 57, 76, 57, .45, head=3),
        rect(78, 36, 42, 42, 1.5, .5),
        grid(78, 36, 3, 3, 14, 14, .2),
        rect(78, 36, 28, 28, 1, .45, dash='2 3'),
        arrow(124, 57, 132, 57, .45, head=3),
        rect(136, 44, 28, 28, 1.5, .5),
        grid(136, 44, 2, 2, 14, 14, .2),
        dot(143, 51, 2, .85, ACCENT),
        arrow(168, 57, 180, 57, .45, head=3),
        dot(188, 44, 2.4, .6),
        dot(188, 58, 2.4, .6),
        dot(188, 72, 2.4, .6),
        line(188, 44, 208, 58, .35),
        line(188, 58, 208, 58, .35),
        line(188, 72, 208, 58, .35),
        dot(210, 58, 2.4, .8),
        text(43, 96, 'IMAGE', 'middle', .42),
        text(99, 96, 'CONV', 'middle', .42),
        text(150, 96, 'POOL', 'middle', .42),
        text(196, 96, 'FC', 'middle', .42),
    ])


def transformer():
    return ''.join([
        rect(44, 112, 14, 14, 1.5, .5),
        rect(86, 112, 14, 14, 1.5, .5),
        rect(128, 112, 14, 14, 1.5, .5),
        rect(170, 112, 14, 14, 1.5, .5),
        line(51, 112, 66, 96, .3),
        line(93, 112, 98, 96, .3),
        line(135, 112, 142, 96, .3),
        line(177, 112, 174, 96, .3),
        rect(36, 74, 168, 22, 2, .8, color=ACCENT),
        text(120, 88.5, 'SELF-ATTENTION', 'middle', .46, 5.6),
        arrow(120, 74, 120, 64, .5, head=3),
        rect(64, 42, 112, 22, 2, .55),
        text(120, 56.5, 'FEED-FORWARD', 'middle', .46, 5.6),
        line(80, 42, 51, 34, .3),
        line(106, 42, 93, 34, .3),
        line(134, 42, 135, 34, .3),
        line(160, 42, 177, 34, .3),
        rect(44, 20, 14, 14, 1.5, .5),
        rect(86, 20, 14, 14, 1.5, .5),
        rect(128, 20, 14, 14, 1.5, .5),
        rect(170, 20, 14, 14, 1.5, .5),
        text(120, 140, 'TOKENS', 'middle', .42),
        text(216, 30, 'OUT', 'end', .42),
    ])


def gradient_descent():
    pts = [(x, 104 - .0095 * (x - 123) ** 2) for x in range(38, 209, 6)]
    steps = [(66, 73.1), (88, 92.4), (104, 100.6), (114, 103.2)]
    out = [
        axis(32, 26, 32, 126, .4),
        axis(32, 126, 214, 126, .4),
        curve(pts, .55),
    ]
    out += [dot(x, y, 2.2, .85, ACCENT) for x, y in steps]
    out += [arrow(steps[i][0], steps[i][1], steps[i + 1][0], steps[i + 1][1],
                  .75, ACCENT, head=3) for i in range(3)]
    out += [line(x, y, x, 126, .2, dash='2 3') for x, y in steps[1:]]
    out += [
        text(32, 20, 'LOSS', 'middle', .42),
        text(214, 142, 'PARAM', 'end', .42),
        text(123, 118, 'MIN', 'middle', .4),
    ]
    return ''.join(out)


def confusion_matrix():
    return ''.join([
        rect(66, 34, 108, 84, 2, .55),
        line(120, 34, 120, 118, .45),
        line(66, 76, 174, 76, .45),
        text(93, 58, 'TP', 'middle', .7),
        text(147, 58, 'FP', 'middle', .5),
        text(93, 100, 'FN', 'middle', .5),
        text(147, 100, 'TN', 'middle', .7),
        line(66, 34, 174, 118, .55, dash='3 4', color=ACCENT),
        text(120, 26, 'PREDICTED', 'middle', .42),
        text(58, 78, 'ACTUAL', 'end', .42),
        line(66, 118, 66, 124, .28),
        line(174, 118, 174, 124, .28),
    ])


def roc_curve():
    return ''.join([
        axis(36, 120, 36, 28, .4),
        axis(36, 120, 214, 120, .4),
        line(36, 60, 42, 60, .28),
        line(36, 90, 42, 90, .28),
        line(80, 120, 80, 114, .28),
        line(120, 120, 120, 114, .28),
        line(160, 120, 160, 114, .28),
        line(36, 120, 214, 28, .22, dash='3 4'),
        curve([(36, 120), (48, 84), (62, 60), (82, 44), (110, 34),
               (150, 29), (214, 28)], .85, ACCENT),
        text(36, 22, 'TPR', 'middle', .42),
        text(214, 136, 'FPR', 'end', .42),
        text(150, 64, 'AUC', 'middle', .42),
    ])


def decision_tree():
    return ''.join([
        rect(106, 22, 28, 18, 2, .55),
        line(120, 22, 120, 40, .32),
        rect(58, 64, 28, 16, 2, .5),
        line(72, 64, 72, 80, .3),
        rect(154, 64, 28, 16, 2, .5),
        line(168, 64, 168, 80, .3),
        circle(40, 110, 5, .75, ACCENT),
        circle(96, 110, 5, .45),
        circle(144, 110, 5, .45),
        circle(200, 110, 5, .45),
        line(113, 40, 72, 64, .5, color=ACCENT),
        line(127, 40, 168, 64, .35),
        line(65, 80, 44, 107, .55, color=ACCENT),
        line(79, 80, 92, 107, .35),
        line(161, 80, 148, 107, .35),
        line(175, 80, 196, 107, .35),
        text(97, 55, 'X1', 'middle', .4, 5.6),
        text(145, 55, 'X1', 'middle', .4, 5.6),
        text(46, 98, 'X2', 'end', .4, 5.6),
        text(88, 98, 'X2', 'start', .4, 5.6),
    ])


def kmeans():
    return ''.join([
        circle(64, 54, 4.5, .9, ACCENT),
        circle(162, 52, 4.5, .9, ACCENT),
        circle(110, 106, 4.5, .9, ACCENT),
        dot(48, 42, 2.2, .55),
        dot(78, 40, 2.2, .55),
        dot(86, 60, 2.2, .55),
        dot(52, 68, 2.2, .55),
        dot(146, 38, 2.2, .55),
        dot(178, 36, 2.2, .55),
        dot(188, 56, 2.2, .55),
        dot(152, 64, 2.2, .55),
        dot(94, 92, 2.2, .55),
        dot(128, 90, 2.2, .55),
        dot(136, 110, 2.2, .55),
        dot(100, 116, 2.2, .55),
        line(48, 42, 64, 54, .35, dash='2 3', color=ACCENT),
        line(188, 56, 162, 52, .35, dash='2 3', color=ACCENT),
        line(136, 110, 110, 106, .35, dash='2 3', color=ACCENT),
        text(120, 138, 'CENTROIDS', 'middle', .42),
    ])


def svm():
    return ''.join([
        line(58, 112, 182, 52, .85, color=ACCENT),
        line(53.6, 103, 177.6, 43, .3, dash='3 4'),
        line(62.4, 121, 186.4, 61, .3, dash='3 4'),
        dot(66, 86, 2.2, .55),
        dot(82, 76, 2.2, .55),
        dot(100, 82, 2.2, .55),
        dot(112, 68, 2.2, .55),
        dot(88, 118, 2.2, .55),
        dot(106, 120, 2.2, .55),
        dot(132, 88, 2.2, .55),
        dot(144, 112, 2.2, .55),
        circle(100, 82, 3.6, .8, ACCENT),
        circle(132, 88, 3.6, .8, ACCENT),
        text(204, 34, 'MARGIN', 'end', .42),
    ])


def nlp_pipeline():
    return ''.join([
        line(22, 52, 58, 52, .5),
        line(22, 62, 50, 62, .5),
        line(22, 72, 54, 72, .5),
        arrow(62, 62, 74, 62, .42, head=3),
        rect(78, 57, 10, 10, 1.5, .5),
        rect(92, 57, 10, 10, 1.8, .85, color=ACCENT),
        rect(106, 57, 10, 10, 1.5, .5),
        arrow(118, 62, 130, 62, .42, head=3),
        bars(134, 50, [.4, .8, .6, 1], 4, 2, 24, .5),
        arrow(160, 62, 172, 62, .42, head=3),
        rect(174, 46, 30, 28, 2, .55),
        line(180, 54, 198, 54, .26),
        line(180, 62, 198, 62, .26),
        line(180, 70, 198, 70, .26),
        arrow(206, 62, 218, 62, .5, head=3),
        text(40, 98, 'TEXT', 'middle', .42),
        text(97, 98, 'TOKENS', 'middle', .42),
        text(145, 98, 'EMBED', 'middle', .42),
        text(189, 98, 'MODEL', 'middle', .42),
        text(212, 86, 'OUT', 'middle', .42),
    ])


def ml_pipeline():
    return ''.join([
        rect(24, 52, 30, 24, 1.5, .5),
        grid(24, 52, 2, 2, 15, 12, .2),
        arrow(56, 64, 64, 64, .42, head=3),
        bars(66, 48, [.35, .7, .5, .9], 5, 2, 28, .5),
        arrow(95, 64, 102, 64, .42, head=3),
        curve([(106, 48), (112, 53), (118, 57), (124, 60), (130, 63)], .55),
        arrow(132, 64, 142, 64, .42, head=3),
        circle(154, 64, 10, .5),
        path('M149 64 L153 69 L160 58', .8, color=ACCENT),
        arrow(166, 64, 180, 64, .42, head=3),
        rect(184, 58, 24, 18, 1.5, .5),
        arrow(196, 58, 196, 38, .75, ACCENT, head=4),
        text(39, 96, 'DATA', 'middle', .42),
        text(80, 96, 'FEATURES', 'middle', .42),
        text(117, 96, 'TRAIN', 'middle', .42),
        text(154, 96, 'EVAL', 'middle', .42),
        text(196, 96, 'DEPLOY', 'middle', .42),
    ])


def big_data():
    return ''.join([
        arrow(24, 50, 44, 62, .45, head=3),
        arrow(24, 64, 44, 64, .45, head=3),
        arrow(24, 78, 44, 66, .45, head=3),
        line(46, 52, 46, 76, .55),
        arrow(48, 64, 60, 64, .42, head=3),
        path('M64 52 A12 4 0 1 1 88 52 A12 4 0 1 1 64 52', .5),
        line(64, 52, 64, 76, .4),
        line(88, 52, 88, 76, .4),
        path('M64 76 A12 4 0 0 0 88 76', .4),
        arrow(90, 64, 102, 64, .42, head=3),
        dot(118, 48, 2.2, .55),
        dot(106, 74, 2.2, .55),
        dot(130, 74, 2.2, .55),
        line(118, 48, 106, 74, .3),
        line(118, 48, 130, 74, .3),
        line(106, 74, 130, 74, .3),
        arrow(136, 64, 172, 64, .42, head=3),
        rect(176, 46, 34, 24, 1.5, .55),
        line(186, 70, 186, 76, .35),
        line(178, 76, 194, 76, .35),
        dot(193, 56, 1.8, .9, ACCENT),
        text(36, 102, 'INGEST', 'middle', .42),
        text(76, 102, 'STORE', 'middle', .42),
        text(118, 102, 'PROCESS', 'middle', .42),
        text(193, 102, 'SERVE', 'middle', .42),
    ])


DIAGRAMS = {
    'er-diagram': er_diagram,
    'normalization': normalization,
    'b-tree': b_tree,
    'transaction': transaction,
    'sql-join': sql_join,
    'cyber-attack': cyber_attack,
    'encryption': encryption,
    'pki': pki,
    'firewall': firewall,
    'cnn': cnn,
    'transformer': transformer,
    'gradient-descent': gradient_descent,
    'confusion-matrix': confusion_matrix,
    'roc-curve': roc_curve,
    'decision-tree': decision_tree,
    'kmeans': kmeans,
    'svm': svm,
    'nlp-pipeline': nlp_pipeline,
    'ml-pipeline': ml_pipeline,
    'big-data': big_data,
}
