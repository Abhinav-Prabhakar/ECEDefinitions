# Equation & diagram pass — subject brief

You are adding **equations and a small number of diagrams** to one subject file in the
one·liners ECE dataset. The definitions are already written and validated. Do not rewrite
them. This is a notation layer, not a second curriculum.

You own **exactly one file**, given in your task prompt. Do not edit any other file. Do not
run `git`. Do not touch `index.html`, `design.md`, `README.md`, `sw.js`, `assets/`,
`scripts/`, or another subject's JSON. Another agent may be working on the next file.

---

## 1. The two fields

Every definition already has:

```json
{
  "id": "de-broglie-hypothesis",
  "term": "de Broglie hypothesis",
  "definition": "Any moving particle is associated with a matter wave.",
  "formula": "",
  "unit": 1,
  "unitTitle": "Quantum Mechanics",
  "sources": ["ep-unit-1-quantum-mechanics#p.5"]
}
```

- `formula` — **bare inline TeX**, rendered by KaTeX. No `$`, no `$$`, no
  `\begin{...}`/`\end{...}`. Keep it under 140 characters. Empty string when the
  definition has no honest equation.
- `diagram` — optional id from the shared sprite (list below). Add it only when the
  drawing directly depicts the definition. Omit the key otherwise.

Do not add any other keys. Do not change `id`, `term`, `definition`, `unit`,
`unitTitle`, or `sources`. Preserve every existing source locator exactly.

## 2. What deserves an equation

Add a formula when it makes the definition more precise, memorable or testable:

- a defining relation (`\lambda=h/p`, `V=IR`, `f_c=\frac{1}{2\pi RC}`),
- a governing law or transfer function (`H(s)=\frac{\omega_n^2}{s^2+2\zeta\omega_n s+\omega_n^2}`),
- a standard bound, identity or complexity (`T(n)=O(n\log n)`, `\Delta x\,\Delta p\ge \hbar/2`),
- a canonical transform or mapping (`X(k)=\sum_{n=0}^{N-1}x(n)e^{-j2\pi kn/N}`).

Leave `formula` empty for definitions that are genuinely non-quantitative: a policy, a
protocol name, a management concept, a historical experiment, a layer description, a
data-structure operation with no invariant, a programming-language feature. **An invented
or decorative equation is worse than no equation.** Roughly half of the technical
catalogue should end up with one; non-technical subjects may have few or none.

Rules of notation:

- Use LaTeX commands, not Unicode maths: `\lambda`, `\Omega`, `\mu`, `\partial`,
  `\nabla`, `\int`, `\sum`, `\sqrt{}`, `\frac{}{}`, `\mathbf{}`, `\hat{}`, `\overline{}`.
  Degrees are `^{\circ}`. Infinity is `\infty`.
- Subscripts: `V_{BE}`, `I_{DS}`, `E_n` is acceptable but prefer `E_{n}`.
- Multi-letter labels inside maths use `\text{}`: `V_{\text{out}}`, `P_{\text{loss}}`.
- Multiplication: juxtaposition or `\,`; avoid `*`. Use `\cdot` for a visible dot.
- Approximate: `\approx`. Proportional: `\propto`. Defined as: `\equiv`.
- No units inside the formula unless the unit is the point. Keep units in the definition.
- Do not write a sentence inside the formula. One relation, or at most one short chain.
- No `\displaystyle`, no `\begin{aligned}`, no `\tag`, no `\label`, no `\ref`.
- Use `j` for the imaginary unit in signals/electrical subjects; `i` is acceptable in pure
  mathematics when that is the local convention.
- Do not duplicate the same generic formula on ten unrelated rows. The formula must belong
  to this definition.

## 3. Diagrams

The shared sprite lives in `assets/diagrams.svg`; the app injects it once. On the subject
page a diagram is revealed on hover; in a quiz it is shown with the answer. Use them
sparingly: **0–8 per subject**, only when the drawing is the clearest explanation of that
row. Reuse an id across closely related definitions is fine, but do not staple the same
picture to a whole unit.

Available ids (viewBox 240×150, thin line art, theme-aware):

| id | what it shows | good for |
| --- | --- | --- |
| `pn-junction` | p/n blocks, depletion band, field | junction, depletion region, barrier potential, diode |
| `diode-iv` | exponential I–V curve with knee | diode, forward/reverse bias, cut-in, breakdown |
| `bjt` | NPN symbol with terminal currents | BJT regions, emitter/collector/base, current gain |
| `mosfet` | n-channel enhancement symbol | MOSFET, channel, threshold, gate control |
| `opamp` | inverting amplifier with feedback | op-amp, virtual ground, feedback, gain |
| `cmos-inverter` | PMOS/NMOS pair, VDD/GND | CMOS inverter, logic family, static power |
| `logic-gates` | AND, OR, NOT symbols | gates, Boolean realisation, combinational logic |
| `d-flipflop` | D flip-flop block with clock edge | flip-flop, latch, clocking, setup/hold |
| `cmos-cross-section` | gate oxide, wells, substrate | CMOS process, lithography layers, gate stack |
| `chip-floorplan` | die with CPU/GPU/SRAM/IO blocks | floorplanning, SoC, physical design, partitioning |
| `memory-hierarchy` | registers → cache → DRAM → disk | memory hierarchy, locality, latency |
| `pipeline` | IF/ID/EX/MEM/WB and staggered rows | pipelining, hazards, throughput, speedup |
| `cache-map` | address tag/index/offset and sets | cache mapping, associativity, tag/index |
| `fourier` | time waveform and spectrum | Fourier series/transform, harmonics, spectrum |
| `sampling` | continuous wave, samples, reconstruction | sampling, Nyquist, aliasing, discrete time |
| `convolution` | x(τ), h(t), y(t) panels | convolution, impulse response, LTI output |
| `z-plane` | unit circle, pole, zero | z-transform, ROC, stability, poles/zeros |
| `bode` | magnitude and phase asymptotes | Bode plot, cutoff, roll-off, phase margin |
| `control-loop` | R→Σ→G→Y with H feedback | feedback, closed loop, plant, error |
| `gaussian` | bell curve with μ and ±σ | normal distribution, PDF, confidence, noise |
| `matrix-transform` | unit square mapped to a parallelogram | matrix, linear transformation, basis, eigen idea |
| `am-modulation` | envelope and carrier | AM, modulation index, envelope, carrier |
| `qam` | I/Q constellation | QAM, constellation, I/Q, digital modulation |
| `superhet` | RF→mixer→IF→demod chain | superheterodyne, mixer, IF, receiver |
| `dipole` | half-wave dipole and lobes | antenna, radiation pattern, dipole, beamwidth |
| `tx-line` | line, load, standing wave | transmission line, reflection, VSWR, impedance |
| `em-wave` | E and H waves along z | EM wave, propagation, polarization, phase |
| `osi-stack` | seven protocol layers | OSI, layer, encapsulation, protocol stack |
| `tcp-handshake` | SYN / SYN-ACK / ACK | TCP, connection setup, handshake, reliability |
| `process-states` | new/ready/run/wait/exit | process state, scheduler, context switch |
| `linked-list` | nodes and next pointers | linked list, node, pointer, traversal |
| `binary-tree` | binary tree with a highlighted node | tree, BST, traversal, height, search |
| `graph-search` | graph with frontier and path | graph, BFS/DFS, frontier, traversal, shortest path |
| `dft-butterfly` | radix-2 butterfly | DFT, FFT, butterfly, twiddle factor |
| `neural-net` | three layers of neurons | perceptron, hidden layer, backprop, network |
| `image-pipeline` | pixel → blur → edge → mask | image processing, filtering, edge detection |
| `satellite-link` | earth, satellite, uplink/downlink | satellite, link budget, transponder, orbit |
| `iot-layers` | device/edge/cloud bands | IoT architecture, gateway, edge, cloud |
| `soc-blocks` | CPU/GPU/NPU/DDR/IO on a die | SoC, interconnect, accelerator, heterogeneous |
| `rtos-timeline` | periodic tasks and deadlines | scheduling, deadline, period, real-time task |
| `supply-demand` | demand and supply crossing | demand, supply, equilibrium, elasticity |
| `break-even` | cost/revenue lines and BEP | fixed cost, variable cost, break-even, profit |
| `carbon-cycle` | atmosphere/plants/ocean/soil loop | carbon cycle, greenhouse, sequestration |
| `water-cycle` | evaporation, cloud, rain, runoff | water cycle, precipitation, runoff, evaporation |
| `venn` | two sets and intersection | set, union/intersection, Venn, inclusion |
| `electric-dipole` | ±q charges, field lines, separation d | electric dipole, dipole moment, polarization |
| `eigen-directions` | unit square, mapped parallelogram, invariant axes | eigenvalue, eigenvector, diagonalization, basis |
| `memory-layout` | text/data/BSS/heap/stack address map | storage class, scope, process memory, stack/heap |
| `stack-queue` | stack with top, queue with front/rear and wrap | stack, queue, circular queue, LIFO/FIFO |
| `d-orbital-splitting` | free-ion level → t₂g/eg with Δ₀ | crystal field, CFSE, d-orbital splitting |
| `electrochemical-cell` | anode/cathode, salt bridge, electron flow | galvanic cell, EMF, Nernst, electrode potential |
| `series-parallel` | series and parallel resistor pairs | series, parallel, equivalent resistance |
| `thevenin-equiv` | network → V_th/R_th with load | Thevenin, Norton, equivalent source |
| `rlc-transient` | under/over/critically damped step responses | damping, transient, RLC response |
| `phasor` | rotating vector, angle φ, projection | phasor, phase, AC, impedance angle |
| `vector-field` | closed surface flux and boundary circulation | divergence, curl, Gauss, Stokes, line integral |
| `two-port` | two-port block with V₁/I₁ and V₂/I₂ | two-port, Z/Y/H/ABCD parameters |

If none of these fits, leave the diagram out. **Do not invent new ids and do not edit the
sprite.** If a subject clearly needs a new diagram, report it instead of adding the key.

## 4. How to edit

Use a short Python script so nothing else in the file moves. Work from the repository root:

```python
import json
p = 'data/subjects/<sem>/<subject>.json'
d = json.load(open(p, encoding='utf-8'))
by_id = {x['id']: x for x in d['definitions']}
changes = {
  'de-broglie-hypothesis': (r'\lambda=\frac{h}{mv}', None),
  # ...
}
for key, (tex, dg) in changes.items():
    x = by_id[key]
    # keep an existing non-empty formula if you have nothing better; otherwise set it
    x['formula'] = tex
    if dg:
        x['diagram'] = dg
    else:
        x.pop('diagram', None)
with open(p, 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
    f.write('\n')
```

Then run:

```bash
python3 scripts/validate-seed-data.py        # must print VALIDATION OK
node scripts/check-formulas.mjs              # must print FORMULA CHECK OK
```

Both scripts read the whole dataset. They are read-only. If another agent is mid-write on
its own file, a transient JSON error may appear; re-run once. If the error names **your**
file, fix it before finishing.

Before you finish, spot-check three definitions whose equations are non-trivial. A formula
must be dimensionally and physically correct, not merely plausible.

## 5. Report

Return a short report:

- file path you changed,
- number of non-empty formulas and number of diagram assignments,
- formulas left empty because the definition has no honest equation,
- any diagram you wished existed (name + one-line description), if any,
- the final validator outputs.

Do not paste the whole file.
