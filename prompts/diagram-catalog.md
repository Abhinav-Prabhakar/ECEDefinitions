# Diagram catalog — 193 shared symbols

Every symbol is 240×150, thin line art, `currentColor` + one accent, theme-safe.
Preview sheets: `scripts/diagrams/_preview_physics.html`, `_preview_electronics.html`,
`_preview_signals.html`, `_preview_computing.html`, `_preview_software.html`,
`_preview_business.html`; the original 57 are in `assets/diagrams.svg`.

## How to choose

Think like an editor, not a decorator. A diagram earns its place when the drawing carries
structure the sentence cannot: a curve, a field, a circuit, a state, a stack, a pipeline,
a geometry, a before/after. It does **not** earn a place when the row is a syntax keyword,
an API name, a policy, a management label, or a definition that is already a complete
sentence.

- Prefer 1 diagram per 3–5 definitions in a visual subject; 1 per 8–15 in a mathematical
  or programming subject; 0–3 in a values/policy subject.
- Do not put the same diagram on more than ~5 rows. If a whole unit shares one idea, use it
  on the 2–3 rows that define the idea, not every row.
- Leave a row without a diagram if the closest symbol would mislead.
- Existing `diagram` keys may be kept or improved; do not remove one unless it is wrong.
- Never add a new id. The sprite is fixed. If a row desperately needs an absent drawing,
  report it; do not approximate with an unrelated symbol.

## Physics, materials, devices

| id | shows |
| --- | --- |
| `matter-wave` | particle with a de Broglie wave, λ |
| `uncertainty` | narrow/wide distributions, Δx vs Δp |
| `particle-box` | infinite well, levels, standing wave |
| `energy-levels` | ladder with one transition |
| `laser-levels` | three-level pump/metastable/lasing |
| `optical-fiber` | core/cladding, TIR zigzag |
| `fiber-na` | acceptance cone at a fiber face |
| `attenuation` | dB vs distance |
| `hysteresis-loop` | B–H loop, saturation |
| `meissner-effect` | field lines expelled |
| `cooper-pair` | two electrons via lattice distortion |
| `polarization-field` | dipoles aligned in E |
| `energy-bands` | valence/conduction bands, Eg |
| `doping-bands` | donor/acceptor levels in the gap |
| `fermi-dirac` | f(E) at two temperatures |
| `hall-effect` | plate with B, I, transverse V_H |
| `led-recombination` | e–h recombination, photon |
| `quantum-well` | levels vs well width |
| `bragg` | planes, rays, spacing d |
| `mo-diagram` | bonding/antibonding orbitals |
| `polymer-chain` | repeat units |
| `aromatic-ring` | benzene ring with π cloud |
| `corrosion-cell` | anode/cathode local cell |
| `crystal-lattice` | unit cell, lattice points |
| `pn-junction` | p/n blocks, depletion band, field |
| `diode-iv` | exponential I–V, knee, breakdown |
| `bjt` | NPN symbol, terminal currents |
| `mosfet` | n-channel enhancement symbol |
| `cmos-cross-section` | gate oxide, wells, substrate |
| `cmos-inverter` | PMOS/NMOS pair, rails |
| `logic-gates` | AND, OR, NOT |
| `d-flipflop` | D flip-flop, clock edge |
| `opamp` | inverting amplifier with feedback |
| `electric-dipole` | ±q charges, field lines, d |
| `d-orbital-splitting` | free ion → t2g/eg, Δ₀ |
| `electrochemical-cell` | anode/cathode, salt bridge |

## Electronics, circuits, VLSI

| id | shows |
| --- | --- |
| `node-mesh` | two-loop network, node/mesh arrows |
| `source-transform` | voltage+series R ↔ current || R |
| `rc-charge` | RC charge/discharge, τ |
| `resonance-curve` | amplitude vs frequency, f0 |
| `filter-response` | LP/HP/BP/notch panels |
| `rectifier-waveforms` | AC, half-wave, full-wave |
| `clipper-clamper` | input and clipped/clamped output |
| `bjt-biasing` | voltage-divider bias |
| `mosfet-curves` | output I–V family |
| `opamp-inverting` | inverting amp, virtual ground |
| `opamp-integrator` | capacitor feedback |
| `differential-pair` | matched pair, tail source |
| `current-mirror` | reference + mirror |
| `cmos-layout` | n-well/poly top view |
| `stick-diagram` | inverter stick layers |
| `transmission-gate` | parallel PMOS/NMOS |
| `adc-dac` | staircase / R-2R |
| `pll` | PD → loop filter → VCO |
| `oscillator-loop` | amplifier + LC feedback |
| `power-amp` | class A/B waveforms |
| `regulator` | series pass + reference |
| `s-parameters` | incident/reflected waves |
| `bridge-circuit` | Wheatstone bridge |
| `max-power` | power vs R_L, peak at R_th |
| `series-parallel` | series and parallel pairs |
| `thevenin-equiv` | network → V_th/R_th + load |
| `rlc-transient` | under/over/critical step responses |
| `phasor` | rotating vector, angle, projection |
| `two-port` | V₁/I₁ and V₂/I₂ block |
| `chip-floorplan` | die with CPU/GPU/SRAM/IO |
| `soc-blocks` | CPU/GPU/NPU/DDR/IO interconnect |
| `fpga` | CLB array and routing |
| `asic-flow` | spec → RTL → synthesis → P&R → fab |
| `verification-flow` | UVM testbench hierarchy |

## Signals, DSP, control, communications, EM

| id | shows |
| --- | --- |
| `signal-ops` | shift, scale, reverse |
| `step-impulse` | step and impulse |
| `even-odd` | even + odd decomposition |
| `aliasing` | undersampled sine and alias |
| `quantization` | staircase quantiser |
| `pcm` | sample → quantise → encode |
| `line-coding` | NRZ/RZ/Manchester |
| `eye-diagram` | eye opening, sampling instant |
| `constellation` | BPSK/QPSK/16-QAM |
| `ask-fsk-psk` | three keyed carriers |
| `fm-modulation` | constant envelope, varying frequency |
| `if-filter` | RF/LO/IF, image rejected |
| `antenna-pattern` | polar lobe, beamwidth |
| `antenna-array` | elements and array lobe |
| `link-budget` | TX → path loss → RX |
| `nyquist-plot` | polar curve, −1 point |
| `root-locus` | s-plane branches |
| `pid` | error → P/I/D → plant |
| `state-space` | x' = Ax + Bu |
| `fir-filter` | tapped delay line |
| `iir-filter` | feedback filter |
| `windowing` | rect/Hann/Hamming |
| `multirate` | decimator/interpolator |
| `fft-stages` | 8-point radix-2 flow |
| `fourier` | time waveform + spectrum |
| `sampling` | continuous, samples, reconstruction |
| `convolution` | x(τ), h(t), y(t) |
| `z-plane` | unit circle, pole, zero |
| `bode` | magnitude/phase asymptotes |
| `control-loop` | R→Σ→G→Y with H |
| `gaussian` | bell curve, μ ± σ |
| `am-modulation` | envelope + carrier |
| `qam` | I/Q constellation |
| `superhet` | RF→mixer→IF→demod |
| `dipole` | half-wave dipole, lobes |
| `tx-line` | line, load, standing wave |
| `em-wave` | E and H along z |
| `satellite-link` | earth, satellite, up/downlink |
| `vector-field` | flux and circulation |
| `dft-butterfly` | radix-2 butterfly |

## Computing, systems, networks

| id | shows |
| --- | --- |
| `hash-table` | buckets and chained keys |
| `heap` | array + heap tree |
| `sorting` | unsorted → sorted bars |
| `recursion-tree` | repeated call tree |
| `dp-table` | filled grid |
| `kmap` | 4-variable map, group |
| `shift-register` | DFF chain |
| `counter-timing` | clock/Q waveforms, skew |
| `state-machine` | FSM bubbles |
| `paging` | virtual → physical frames |
| `segmentation` | segments in both spaces |
| `disk-layout` | platter/tracks/sectors |
| `scheduling` | Gantt + deadline |
| `deadlock` | resource graph cycle |
| `file-system` | inode/directory tree |
| `ip-packet` | header + payload |
| `routing` | graph with shortest path |
| `csma` | contention/backoff timeline |
| `dma` | CPU/memory/DMA/device |
| `interrupt-flow` | device → PIC → vector → ISR |
| `uart-frame` | start/data/parity/stop |
| `i2c-bus` | SDA/SCL start/address/ACK |
| `spi-bus` | MOSI/MISO/SCLK/CS |
| `pipeline` | IF/ID/EX/MEM/WB + stagger |
| `cache-map` | tag/index/offset, sets |
| `memory-hierarchy` | registers → cache → DRAM → disk |
| `memory-layout` | text/data/BSS/heap/stack |
| `stack-queue` | stack top, queue front/rear |
| `linked-list` | nodes and next pointers |
| `binary-tree` | tree with highlighted node |
| `graph-search` | frontier and path |
| `osi-stack` | seven layers |
| `tcp-handshake` | SYN / SYN-ACK / ACK |
| `process-states` | new/ready/run/wait/exit |
| `rtos-timeline` | periodic tasks, deadlines |
| `iot-layers` | device/edge/cloud |
| `neural-net` | three layers |
| `cnn` | image → conv → pool → FC |
| `transformer` | tokens → attention → FF |
| `image-pipeline` | pixel → blur → edge → mask |

## Software, data, AI, security

| id | shows |
| --- | --- |
| `er-diagram` | entities, relationship, cardinality |
| `normalization` | 1NF → 2NF → 3NF |
| `b-tree` | balanced index |
| `transaction` | begin/commit timeline |
| `sql-join` | two tables joined |
| `cyber-attack` | attacker → asset path |
| `encryption` | plaintext/key/ciphertext |
| `pki` | root → intermediate → leaf |
| `firewall` | trusted/untrusted zones |
| `gradient-descent` | loss valley steps |
| `confusion-matrix` | TP/FP/FN/TN |
| `roc-curve` | ROC + AUC |
| `decision-tree` | feature splits |
| `kmeans` | clusters/centroids |
| `svm` | margin between classes |
| `nlp-pipeline` | text → tokens → embed → model |
| `ml-pipeline` | data → features → train → deploy |
| `big-data` | ingest → store → process → serve |

## Business, environment, values, aptitude

| id | shows |
| --- | --- |
| `supply-demand` | demand/supply crossing |
| `break-even` | cost/revenue lines, BEP |
| `product-lifecycle` | intro/growth/maturity/decline |
| `cash-flow` | inflow/outflow + cumulative |
| `design-thinking` | five-stage loop |
| `business-model-canvas` | nine-block canvas |
| `marketing-mix` | 4Ps |
| `supply-chain` | supplier → customer |
| `org-structure` | hierarchy |
| `swot` | 2×2 |
| `porters-five` | five forces |
| `number-line` | intervals and a point |
| `probability-tree` | two-stage tree |
| `bayes-tree` | prior → likelihood → posterior |
| `venn` | two sets |
| `venn-3` | three sets |
| `values-circle` | self/family/society/nature |
| `harmony-orders` | nested orders |
| `waste-hierarchy` | reduce→dispose pyramid |
| `energy-pyramid` | trophic levels |
| `environmental-pathway` | source → pathway → receptor |
| `carbon-cycle` | atmosphere/plants/ocean/soil |
| `water-cycle` | evaporation/rain/runoff |

## Subject targets

| subject type | target rows with diagrams | examples |
| --- | --- | --- |
| visual physics/devices | 25–40% | Engineering Physics, EDC, Analog Circuits, EM |
| signals/comms/DSP | 20–35% | Signals, ADC, DSP, Antennas, Microwave |
| circuits/electronics | 20–35% | Circuits, Analog, IC Applications, VLSI |
| computer systems/networks | 15–30% | COA, OS, CN, Microprocessors, Embedded |
| data/software/AI | 10–20% | DS, DBMS, AI, Python/Java (lower end) |
| mathematics | 5–15% | Matrix, Calculus, CVTT, Probability |
| programming | 3–10% | C, Java, Python, Embedded C |
| management/humanities | 3–12% | BEFA, Entrepreneurship, Product, UHV |

These are guides, not quotas. A subject at the low end with every diagram earned is better
than one at the high end padded with generic boxes.
