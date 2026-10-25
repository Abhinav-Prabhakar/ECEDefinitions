# one·liners — domain catalog

> What else can be taught one line at a time, and which of those is worth building first.

The current app proves a narrow thing: a term, one sentence, two directions of recall, and a
memory that persists. That unit is not about electronics. It is about **definitional
knowledge** — the vocabulary layer that sits underneath almost every field.

This catalog maps that layer across ~200 collections, grouped into 16 families, then ranks the
ones with the best combination of fit, demand, and buildability.

**Building:** the active subset and build order live in
[`COLLECTION-QUEUE.md`](COLLECTION-QUEUE.md).

---

## 01 · What the format actually teaches

The atomic unit is a pair:

```
term  ↔  one-sentence meaning
```

The quiz asks it in both directions. The memory layer schedules the weak pairs. The daily
goal turns it into a habit. Everything else is presentation.

That means the app is good at exactly one kind of learning:

| It teaches | It does not teach |
| --- | --- |
| Vocabulary and nomenclature | Procedure |
| Distinctions between near-neighbours | Judgment |
| Recall of canonical facts | Derivation |
| The map of a field | The territory |
| Fast recognition of concepts | Fluent application |

This is not a limitation to apologise for. Every profession has a vocabulary wall, and most
people bounce off that wall before they ever reach the interesting part. A one-liner collection is
a ladder over the wall.

---

## 02 · The fit test

A domain is a strong fit when it scores well on seven tests. Score each 1–5.

| Test | Question | Why it matters |
| --- | --- | --- |
| **Glossary density** | Does the field have 100+ named concepts? | Below ~80 definitions, daily practice runs dry. |
| **Canonical answers** | Do experts agree on the definition? | Contested terms make bad quiz keys. |
| **Confusable neighbours** | Can you name three plausible wrong answers? | This is the real quiz test. If distractors are obvious, the round is trivial. |
| **Compression** | Does the meaning fit in 8–28 words? | Long definitions break the one-line promise. |
| **Stakes** | Is someone tested, certified, or judged on this? | Stakes create the daily habit. |
| **Corpus stability** | Will these definitions still be true in three years? | Churn makes the memory layer worthless. |
| **Text sufficiency** | Can it be taught without images, audio, or code? | Every extra medium is a new product. |

**28–35:** build it now.
**20–27:** build it with a format extension.
**Below 20:** it is a different app.

### The distractor test

For any candidate term, write the term and then three wrong definitions a smart beginner
might believe. If you can do that instantly, the domain is quiz-shaped. Medicine, law,
finance, and computer science pass effortlessly. "Great works of art" does not, unless you
add images.

---

## 03 · The catalog

### 1. Software, data & AI

The largest under-served glossary market in the world. Every term is short, every term is
googled, and every term has a cluster of near-neighbours that make excellent distractors.
Definitions are stable, sources are public, and the audience already studies in flashcards.

| Collection | A sample definition | Why it works |
| --- | --- | --- |
| Programming fundamentals | **Closure** — A function bundled with the variables from the scope where it was defined. | Every language interview; high confusion with scope, hoisting, currying. |
| Data structures & algorithms | **Amortized analysis** — Averaging an operation's cost over a sequence of operations rather than a single run. | Interview core; dense confusable set. |
| System design | **Idempotency** — The property that repeating an operation produces the same result as running it once. | Senior interviews; terms are spoken, not drawn. |
| Distributed systems | **CAP theorem** — A distributed system can guarantee only two of consistency, availability, and partition tolerance during a partition. | The canonical example of a one-line idea with three lectures behind it. |
| Databases & SQL | **MVCC** — Multi-version concurrency control: readers see a consistent snapshot without blocking writers. | Backend interviews; every term has a sibling. |
| Operating systems | **Thrashing** — Excessive paging that leaves the CPU with almost no useful work. | Classic exam and interview vocabulary. |
| Networking | **NAT** — Rewriting addresses at a boundary so private hosts share a public address. | CCNA and backend interviews. |
| Web & browser | **CORS** — A browser policy that lets a server declare which origins may read its responses. | Every web developer hits it; badly understood. |
| DevOps & SRE | **Error budget** — The amount of unreliability a service may spend while still meeting its SLO. | Cert and job vocabulary; compact. |
| Cloud certifications | **Availability zone** — An isolated data-centre group within a region, designed to fail independently. | AWS, Azure, and GCP all test the same concepts with different names. |
| Cybersecurity | **Least privilege** — Granting only the permissions needed for a task, and nothing more. | Security+ and CISSP core; endless confusables. |
| Data engineering | **Slowly changing dimension** — A warehouse pattern for tracking how a reference attribute changes over time. | Data-role interviews; jargon-heavy. |
| Machine learning | **Overfitting** — A model learning noise in the training data instead of the underlying pattern. | The single most-asked ML concept. |
| LLMs & generative AI | **RAG** — Retrieval-augmented generation: supplying a model with retrieved documents at answer time. | Huge 2026 demand; definitions still stabilising. |
| Prompt engineering | **Few-shot prompting** — Giving a model a small number of worked examples inside the prompt. | Popular, but volatile; keep the collection short and refresh it. |

**Format needs:** code snippets for some definitions; otherwise text-only.
**Best first collection:** "Software interview glossary" — 300 definitions across six subjects, free sources.

---

### 2. Health & medicine

The highest-stakes vocabulary in the world. Medical language is deliberately built from
prefixes, roots, and suffixes, which makes it unusually teachable one line at a time. It is
also the domain where "recognition is not recall" matters most: a nurse who recognises
"tachycardia" but cannot produce it under pressure is a liability.

| Collection | A sample definition | Why it works |
| --- | --- | --- |
| Medical terminology | **Tachycardia** — A resting heart rate above 100 beats per minute. | Prefixes and roots make thousands of terms predictable. |
| Anatomy | **Peristalsis** — Wavelike muscle contractions that move contents through a tube. | Text works for function; images needed for location. |
| Physiology | **Preload** — The stretch on the ventricles at the end of filling, before contraction. | Dense, confusable, examined everywhere. |
| Pathology | **Infarction** — Tissue death caused by prolonged loss of blood supply. | Ischemia vs infarction is a perfect quiz pair. |
| Pharmacology | **First-pass metabolism** — Drug breakdown in the liver before it reaches systemic circulation. | Every drug question depends on this vocabulary. |
| Microbiology | **Commensal** — An organism that lives on or in a host without harming it. | Pathogen, commensal, symbiont, opportunist: ideal distractors. |
| Immunology | **Antigen** — Any molecule the immune system can specifically recognise. | Antibody vs antigen is the classic confusion. |
| Nursing | **SBAR** — A structured handoff covering situation, background, assessment, and recommendation. | NCLEX and ward practice; acronym-dense. |
| Emergency & first aid | **AED** — A portable device that analyses a rhythm and delivers a shock to restart the heart. | High public value; short definitions. |
| Nutrition | **Glycemic index** — A ranking of how quickly a carbohydrate food raises blood glucose. | Popular, but contested at the edges; keep to consensus terms. |
| Exercise science | **VO₂ max** — The maximum rate at which the body can use oxygen during intense exercise. | Fitness audience; formula-friendly. |
| Medical coding | **Modifier** — A code suffix that explains why a service differs from the standard procedure. | High willingness to pay; stable rules. |
| Public health & epidemiology | **Incidence** — The number of new cases of a condition in a population over a period. | Incidence vs prevalence is a perfect two-way definition. |
| Veterinary | **Zoonosis** — An infectious disease that can pass from animals to humans. | Underserved, loyal audience. |
| Dentistry | **Caries** — Tooth decay caused by acid produced by bacteria in plaque. | Stable, exam-driven. |
| Physical therapy | **Proprioception** — The sense of body position and movement from internal receptors. | Rehab vocabulary; compact. |

**Format needs:** images for anatomy and dermatology; audio for auscultation later.
**Caution:** keep definitions descriptive, not diagnostic advice.

---

### 3. Law, policy & governance

Law is a vocabulary profession. The first year is largely learning a language, and the bar
exam is a recall marathon. Latin maxims, procedural terms, and doctrinal distinctions are
naturally one-line shaped — and the confusable neighbours are vicious.

| Collection | A sample definition | Why it works |
| --- | --- | --- |
| Legal literacy | **Tort** — A civil wrong that causes harm and grounds liability. | The public understands crime but not tort. |
| 1L core | **Consideration** — Something of value exchanged by each party that makes a promise enforceable. | Contracts is built from a few dozen such terms. |
| Civil procedure | **Res judicata** — A matter already judged cannot be relitigated by the same parties. | Latin terms are memorable and high-stakes. |
| Constitutional law | **Judicial review** — A court's power to invalidate acts that conflict with the constitution. | Every polity has an equivalent; strong collection. |
| Evidence | **Hearsay** — An out-of-court statement offered to prove the truth of what it asserts. | Endlessly examined, endlessly confused. |
| Criminal law | **Mens rea** — The guilty state of mind required for a crime. | Pairs perfectly with actus reus. |
| Intellectual property | **Prior art** — Existing public knowledge that can invalidate a patent. | Tech audience; high demand. |
| Privacy & data protection | **Data minimisation** — Collecting only the personal data necessary for a stated purpose. | GDPR-era professional literacy. |
| Corporate law | **Fiduciary duty** — A legal obligation to act in another party's best interest. | Finance and governance crossover. |
| Employment law | **At-will employment** — A default rule allowing either party to end employment without cause. | Practical, high-search-volume. |
| Tax law | **Basis** — The amount invested in an asset for tax purposes, used to compute gain. | Compact and commonly misunderstood. |
| International law | **Sovereignty** — A state's exclusive authority over its territory and people. | IR and law crossover. |
| Policy & IR | **Deterrence** — Preventing an action by making its expected cost exceed its gain. | Think-tank and exam vocabulary. |

**Format needs:** citations; some definitions benefit from a one-line case name.
**Caution:** definitions are jurisdiction-specific. Label the jurisdiction on every collection.

---

### 4. Money: finance, accounting, economics

Finance is the best "high willingness to pay" vocabulary market after medicine. CFA, CPA,
and Series 7 candidates memorise thousands of terms, and the terms cluster into beautiful
distractor sets: duration/convexity, alpha/beta, deductible/coinsurance.

| Collection | A sample definition | Why it works |
| --- | --- | --- |
| Personal finance | **APR** — The annual cost of borrowing, including fees, expressed as a rate. | Mass audience; APR vs APY is a perfect pair. |
| Accounting | **Accrual** — Recognising revenue or expense when earned or incurred, not when cash moves. | The foundation of every accounting exam. |
| Corporate finance | **WACC** — The weighted average cost of the capital a firm uses to fund itself. | Formula-friendly; interview staple. |
| Financial statements | **Goodwill** — The premium paid above the fair value of identifiable net assets. | Commonly misunderstood; excellent distractors. |
| Investing | **Beta** — A stock's sensitivity to moves in the broader market. | Alpha, beta, Sharpe, drawdown: a natural cluster. |
| Fixed income | **Duration** — The weighted average time to a bond's cash flows, used to measure rate sensitivity. | Convexity sits right beside it. |
| Derivatives | **Strike price** — The price at which an option holder may buy or sell the underlying. | Options vocabulary is compact and exam-heavy. |
| Banking & Series 7 | **Margin call** — A demand to add collateral when account equity falls below the maintenance requirement. | Licensing demand; stable definitions. |
| Real estate | **Cap rate** — Net operating income divided by property value. | Investors and agents both need it. |
| Insurance | **Coinsurance** — The share of a covered loss the insured pays after the deductible. | Deductible, copay, coinsurance, rider: ideal quiz set. |
| Economics | **Opportunity cost** — The value of the best alternative forgone when a choice is made. | The most useful one-liner in the social sciences. |
| Macroeconomics | **Deadweight loss** — Value destroyed because a mutually beneficial transaction does not occur. | Diagram-heavy in textbooks, but text-definable. |
| Crypto & blockchain | **Finality** — The point at which a transaction can no longer be reversed. | Volatile field; keep to protocol-level terms. |
| Behavioral finance | **Loss aversion** — The tendency to feel losses more strongly than equivalent gains. | Popular, stable, crossover with psychology. |

**Format needs:** formulas (the existing `formula` slot already fits), currency-neutral wording.

---

### 5. Business, product & marketing

The professional upskilling market. These terms are less "examined" than finance, but they
are spoken in meetings every day, and misusing them is socially costly. The best collections are
the ones attached to a certification or a job interview.

| Collection | A sample definition | Why it works |
| --- | --- | --- |
| Strategy | **Moat** — A durable structural advantage that protects a business's profits. | Every founder and MBA uses it. |
| Product management | **Product-market fit** — Evidence that a market pulls a product faster than the company can supply it. | Interview staple; short and contested just enough. |
| Product discovery | **Jobs to be done** — The progress a customer is trying to make in a particular situation. | The vocabulary of modern product teams. |
| UX & interaction design | **Affordance** — A property of an object that suggests how it should be used. | Affordance vs signifier is a classic confusion. |
| Visual design | **Kerning** — Adjusting the space between individual characters. | Kerning, leading, tracking: perfect distractor trio. |
| Marketing | **Positioning** — The place a brand occupies in a customer's mind relative to alternatives. | High search volume; stable. |
| Growth | **CAC** — Customer acquisition cost: the average cost of winning one new customer. | CAC vs LTV is the canonical pair. |
| Sales | **MEDDIC** — A qualification framework covering metrics, buyer, decision criteria, and process. | Certification-adjacent; acronym-dense. |
| Operations | **Bullwhip effect** — Demand variability amplifying as it moves up a supply chain. | Supply-chain exams and interviews. |
| Supply chain | **Safety stock** — Buffer inventory held to absorb uncertainty in demand or lead time. | Stable, formula-friendly. |
| Project management | **Critical path** — The longest dependent sequence of tasks, which sets the minimum project duration. | PMP core; compact. |
| Agile & scrum | **Velocity** — The amount of work a team completes per iteration, used for forecasting. | Certification demand; definitions vary by framework. |
| People & HR | **Span of control** — The number of direct reports a manager oversees. | Stable, compact, commonly confused. |
| Entrepreneurship & VC | **Runway** — The time a company can operate before it runs out of cash. | Founder literacy; high virality. |
| Consulting | **MECE** — Mutually exclusive, collectively exhaustive: a grouping with no overlap and no gaps. | Case-interview vocabulary. |

**Format needs:** text-only; optional frameworks as `formula`.

---

### 6. Engineering & physical sciences

The natural extension of the current app. Formula-heavy, exam-driven, and full of
near-neighbour terms. The existing `formula` field and the two-way quiz already fit this
family better than any other.

| Collection | A sample definition | Why it works |
| --- | --- | --- |
| Mechanical engineering | **Fatigue** — Failure caused by repeated cyclic loading below the material's ultimate strength. | Stress, strain, fatigue, creep: ideal cluster. |
| Civil engineering | **Bearing capacity** — The maximum load soil can support without failure. | FE/PE exams; stable. |
| Structural engineering | **Moment of inertia** — A section's resistance to bending about an axis. | Formula-friendly; commonly confused with mass moment. |
| Electrical engineering | **Power factor** — Real power divided by apparent power in an AC circuit. | The current app's home turf. |
| Electronics | **Hysteresis** — A lag between cause and effect that depends on the system's history. | Schmitt trigger, magnetic cores, control: one term, many uses. |
| Chemical engineering | **Reflux** — Boiling a liquid and returning the condensed vapour to the column. | Distillation vocabulary; compact. |
| Aerospace | **Angle of attack** — The angle between a wing's chord line and the oncoming airflow. | PPL and aerodynamics; classic confusion with pitch. |
| Materials science | **Annealing** — Heating and slow cooling to soften a metal and relieve internal stress. | Annealing, tempering, quenching: perfect trio. |
| Physics | **Entropy** — A measure of the number of microscopic arrangements consistent with a macroscopic state. | The most misunderstood one-liner in science. |
| Chemistry | **Buffer** — A solution that resists pH change when small amounts of acid or base are added. | Exam staple; short and precise. |
| Organic chemistry | **Nucleophile** — An electron-rich species that donates a pair of electrons to form a bond. | Nucleophile vs electrophile is a perfect definition. |
| Astronomy | **Parsec** — The distance at which one astronomical unit subtends one arcsecond. | Definition is exact and satisfying. |
| Geology | **Subduction** — One tectonic plate sliding beneath another into the mantle. | Stable, visual, exam-friendly. |
| Meteorology | **Dew point** — The temperature to which air must cool to become saturated. | Everyday relevance; commonly confused with humidity. |
| Environmental science | **Albedo** — The fraction of incident light a surface reflects. | Climate literacy; compact. |

**Format needs:** formulas and units. This family is the least work to add.

---

### 7. Math & statistics

Pure math definitions are the most precise content in existence, which makes them ideal
quiz keys. The risk is that the app teaches the label without the skill — but for exam
vocabulary and data literacy, that label is exactly the bottleneck.

| Collection | A sample definition | Why it works |
| --- | --- | --- |
| Calculus | **Gradient** — The vector of partial derivatives that points in the direction of steepest increase. | Compact; used everywhere. |
| Linear algebra | **Eigenvector** — A vector whose direction is unchanged by a linear transformation. | The canonical "one line, three lectures" term. |
| Discrete math | **Bijection** — A one-to-one correspondence between every element of two sets. | Injection, surjection, bijection: perfect trio. |
| Probability | **Conditional probability** — The probability of an event given that another event has occurred. | Base-rate errors are everywhere. |
| Statistics | **p-value** — The probability of data at least as extreme as observed, assuming the null hypothesis is true. | The most misused definition in science. |
| Statistical inference | **Confidence interval** — A range of plausible values for a parameter at a stated coverage probability. | Confidence vs credible interval is a great definition. |
| Regression | **Multicollinearity** — Predictors that are highly correlated, making coefficient estimates unstable. | Practical data-science vocabulary. |
| Causal inference | **Confounder** — A variable that affects both treatment and outcome, creating a spurious association. | The core of modern data literacy. |
| Data literacy | **Survivorship bias** — Drawing conclusions only from the cases that survived a selection process. | Popular, stable, endlessly useful. |
| Number theory | **Coprime** — Two integers whose only positive common divisor is one. | Compact and exact. |
| Topology | **Compact set** — A set for which every open cover has a finite subcover. | Pure-math audience; definitions are canonical. |
| Logic | **Sound argument** — A valid argument whose premises are all true. | Valid vs sound is a classic confusion. |

**Format needs:** formulas and symbols; some definitions need a diagram (geometry, topology).

---

### 8. Life & earth sciences

Biology is a vocabulary explosion: thousands of named structures, processes, and
relationships, most of them definable in one sentence. It is also the most visual science,
so the text-only collections should stay on function and process rather than structure.

| Collection | A sample definition | Why it works |
| --- | --- | --- |
| Cell biology | **Apoptosis** — Programmed cell death carried out by a controlled molecular sequence. | Apoptosis vs necrosis is a perfect pair. |
| Genetics | **Epistasis** — One gene masking or modifying the effect of another gene. | Dense, exam-heavy, confusable. |
| Molecular biology | **Transcription** — Copying a DNA sequence into RNA. | Central dogma vocabulary. |
| Microbiology | **Gram-positive** — Bacteria that retain the crystal-violet stain because of a thick peptidoglycan wall. | Stable and precise. |
| Ecology | **Keystone species** — A species whose removal disproportionately reshapes its ecosystem. | Popular science; strong examples. |
| Ecology | **Trophic cascade** — Predator effects rippling down through a food web. | One-line idea with a famous story. |
| Evolution | **Sympatric speciation** — Speciation without geographic separation. | Allopatric vs sympatric: ideal distractors. |
| Botany | **Transpiration** — Water loss from plants through stomata, driving upward flow. | Compact and process-shaped. |
| Neuroscience | **Action potential** — A brief electrical impulse created by ion flow across a neuron's membrane. | High demand; compact. |
| Biochemistry | **Denaturation** — Loss of a protein's functional shape from heat, pH, or chemical stress. | Everyday relevance. |
| Oceanography | **Thermohaline circulation** — Global deep-ocean flow driven by differences in temperature and salinity. | Stable, systems-level. |
| Climate science | **Radiative forcing** — The change in Earth's energy balance caused by a factor such as greenhouse gas concentration. | Policy-relevant; definitions are stable. |

**Format needs:** images for anatomy, taxonomy, and cell structure.

---

### 9. Psychology & social sciences

Psychology is the most popular non-vocational subject in the catalog. Its terminology is
short, its biases are viral, and its intro-course canon is stable. The clinical and
neuroscience edges need more care, but the core is ideal.

| Collection | A sample definition | Why it works |
| --- | --- | --- |
| Intro psychology | **Negative reinforcement** — Removing an unpleasant stimulus to increase a behaviour. | The most commonly confused term in the field. |
| Cognitive biases | **Confirmation bias** — Seeking and favouring information that confirms existing beliefs. | Shareable, memorable, stable. |
| Cognitive psychology | **Working memory** — The limited system that holds and manipulates information during a task. | Compact and foundational. |
| Developmental psychology | **Object permanence** — The understanding that objects continue to exist when out of sight. | One-line idea, famous experiment. |
| Social psychology | **Bystander effect** — Less help is offered as the number of witnesses grows. | Viral and exam-friendly. |
| Clinical psychology | **Compulsion** — A repetitive behaviour performed to reduce distress from an obsession. | Obsession vs compulsion: perfect pair. |
| Sociology | **Anomie** — A condition of normlessness in which social expectations break down. | Classic term; compact. |
| Anthropology | **Ethnography** — The description of a culture based on sustained fieldwork. | Stable and precise. |
| Political science | **Federalism** — A system that divides power between a central government and regional units. | Civics literacy; high search volume. |
| International relations | **Deterrence** — Preventing an action by making its expected cost exceed its gain. | Compact and widely used. |
| Criminology | **Recidivism** — Reoffending by a person who has already been convicted. | Policy-relevant; stable. |
| Education | **Scaffolding** — Temporary support that is gradually removed as a learner gains competence. | Teacher training; compact. |
| Linguistics | **Phoneme** — The smallest sound unit that can distinguish meaning in a language. | Phoneme vs morpheme: ideal pair. |
| Rhetoric | **Straw man** — Refuting a weakened version of an opponent's argument instead of the actual one. | Public literacy; viral. |

**Format needs:** text-only for the core; images for neuroscience and development.

---

### 10. Humanities & culture

Humanities collections are less about stakes and more about cultural fluency. They work best as
"dinner-party literacy": the terms that let you follow a conversation about a film, a
painting, or a novel. The two-way quiz is surprisingly good here because the terms are
distinctive and the definitions are compact.

| Collection | A sample definition | Why it works |
| --- | --- | --- |
| Art history | **Chiaroscuro** — Strong contrast between light and dark used to model form. | Short, distinctive, image-friendly. |
| Art history | **Readymade** — An ordinary manufactured object presented as art. | One-line idea with a big argument behind it. |
| Film studies | **Mise-en-scène** — Everything placed within the frame, including sets, lighting, and blocking. | Film literacy; commonly misused. |
| Film studies | **Diegetic sound** — Sound that exists within the world of the film. | Diegetic vs non-diegetic: perfect pair. |
| Literary terms | **Synecdoche** — A part standing for the whole, or the whole for a part. | Synecdoche vs metonymy: the classic confusion. |
| Literary terms | **Bildungsroman** — A novel about a character's formative growth. | Distinctive and compact. |
| Philosophy | **Categorical imperative** — Act only on maxims you could will to become universal law. | One-line idea, huge tradition. |
| Philosophy | **Qualia** — The subjective feel of an experience. | Short and contested in a productive way. |
| Religion & mythology | **Eschatology** — The study of final things, such as death, judgment, and the end of the world. | Compact and cross-cultural. |
| History | **Marshall Plan** — American aid that financed Western European reconstruction after the Second World War. | Event-plus-significance fits one line. |
| Classics | **Stoicism** — A philosophy that treats virtue as the only good and emotions as judgments to examine. | Popular revival; stable core. |
| Architecture | **Cantilever** — A beam or slab supported at only one end. | Visual, precise, commonly confused with overhang. |
| Music history | **Counterpoint** — The art of combining independent melodic lines that sound harmonious together. | Compact and exam-friendly. |
| Fashion | **Bias cut** — Cutting fabric at 45 degrees so it drapes and stretches. | Distinctive and visual. |
| Design | **Negative space** — The empty area around and between subjects in a composition. | Universal design literacy. |

**Format needs:** images for art, architecture, and fashion; audio for music.

---

### 11. Test prep & school

This is the largest market by audience and the most crowded by competition. The opportunity
is not another vocabulary app; it is a **better-shaped** collection for exams whose concepts are
poorly served by existing flashcards.

| Collection | What it covers | Why it works |
| --- | --- | --- |
| SAT / ACT | Grammar rules, math concepts, rhetorical terms | Massive audience; concept collection beats raw vocab. |
| GRE / GMAT | Quant concepts, logic, argument terms | High willingness to pay; compact definitions. |
| LSAT | Logical reasoning fallacies, argument structure | The test is literally definitional reasoning. |
| MCAT | Biology, biochemistry, psychology, sociology | Huge corpus; dense vocabulary. |
| USMLE | Pathology, pharmacology, physiology | Highest stakes; highest willingness to pay. |
| NCLEX / TEAS / HESI | Nursing concepts, labs, safety | Certification-driven; stable. |
| CPA / CFA / Series 7 | Accounting, finance, securities | Professional licensing; high LTV. |
| PMP / CSM / Six Sigma | Project and process vocabulary | Corporate training budgets. |
| AWS / Azure / GCP | Cloud concepts and service names | Fast-growing; definitions change by provider. |
| Security+ / CISSP / CCNA / A+ | Security and networking | Certification factories; underserved by good design. |
| Bar exam / MPRE | Doctrinal terms and procedure | Enormous corpus; jurisdiction-specific. |
| FE / PE | Engineering fundamentals | Formula-heavy; the current engine already fits. |
| AP / IB / A-level / GCSE | Biology, chemistry, physics, psychology, history | School-scale audience; yearly refresh. |
| JEE / NEET / UPSC / CA | Indian entrance and professional exams | Hundreds of millions of candidates; huge underserved market. |
| Real estate / insurance / CDL / FAA | Licensing vocabularies | Local, stable, high-stakes. |

**Format needs:** exam-specific collections, progress transfer, and a "syllabus coverage"
view. This is where the app's collection/section structure earns its keep.

---

### 12. Trades, licenses & safety

The most under-served high-stakes market in the catalog. Electricians, HVAC technicians,
plumbers, welders, pilots, and sailors all carry a vocabulary that is taught in
apprenticeships, tested in licensing exams, and almost never turned into a good study app.

| Collection | A sample definition | Why it works |
| --- | --- | --- |
| Electrical | **Ampacity** — The maximum current a conductor can carry safely under stated conditions. | Licensing exam core; stable. |
| Electrical | **GFCI** — A device that trips when current leaks to ground. | GFCI vs AFCI: perfect pair. |
| Electrical | **Derating** — Reducing a component's rated capacity for real-world conditions. | Commonly misunderstood. |
| HVAC | **Superheat** — The temperature of refrigerant vapour above its boiling point. | Superheat vs subcooling: the technician's core distinction. |
| HVAC | **SEER** — Seasonal energy efficiency ratio: cooling output divided by energy input over a season. | Compact and exam-friendly. |
| Plumbing | **Trap seal** — The water in a trap that blocks sewer gas from entering a building. | One-line idea, practical stakes. |
| Plumbing | **Backflow preventer** — A device that stops contaminated water from reversing into a clean supply. | Safety-critical; stable. |
| Welding | **Duty cycle** — The percentage of a ten-minute period a welder can run at a given amperage. | Compact and commonly misunderstood. |
| Welding | **Penetration** — The depth to which weld metal fuses into the base material. | Visual, but text-definable. |
| Automotive | **Oversteer** — When a car turns more sharply than the driver intends, because the rear loses grip. | Enthusiast and technician crossover. |
| Solar | **Net metering** — Crediting a customer for electricity exported to the grid. | Policy-dependent; label the region. |
| Food safety | **Danger zone** — The temperature range in which bacteria multiply fastest. | ServSafe core; universal. |
| Cosmetology | **Developer** — A peroxide solution that opens the hair cuticle and activates colour. | Licensing exam; stable. |
| Aviation | **V₁** — The speed beyond which a takeoff can no longer be safely aborted. | PPL/ATP core; high stakes. |
| Aviation | **Density altitude** — Pressure altitude adjusted for temperature, indicating how the aircraft will perform. | The classic "why did the plane struggle on a hot day" term. |
| Sailing | **Apparent wind** — The wind felt on a moving boat, combining true wind and boat speed. | RYA/ASA core; compact. |
| Sailing | **Close-hauled** — Sailing as close to the wind as the boat can efficiently point. | Perfect one-line seamanship term. |
| Scuba | **Decompression stop** — A pause at depth to let dissolved nitrogen leave the body safely. | Safety-critical; stable. |
| Climbing | **Crux** — The hardest section of a climb. | Short, spoken, viral. |
| Trucking / CDL | **GVWR** — The maximum safe total weight of a vehicle including cargo. | Licensing core; stable. |

**Format needs:** images for some equipment; otherwise text-only.
**Why it is a good business:** these audiences are large, loyal, and poorly served by
consumer study apps.

---

### 13. Hobbies with deep vocabularies

Hobby collections are the most fun to build and the easiest to share. They rarely have exam
stakes, but they have something almost as good: **social stakes**. Using the wrong word at
a wine bar or a chess club is embarrassing.

| Collection | A sample definition | Why it works |
| --- | --- | --- |
| Wine | **Tannin** — A bitter, astringent compound from grape skins, seeds, and oak that gives red wine structure. | The gateway term for wine literacy. |
| Wine | **Terroir** — The combined effect of soil, climate, and tradition on a wine's character. | Short, contested, endlessly discussed. |
| Coffee | **Extraction** — The process of dissolving soluble compounds from coffee grounds into water. | The core variable in brewing. |
| Coffee | **Channeling** — Water finding a path of least resistance through the coffee bed, causing uneven extraction. | Distinctive and diagnostic. |
| Tea | **Oxidation** — The enzymatic browning that turns green tea leaves toward black tea. | The organising variable of tea styles. |
| Beer | **IBU** — International Bitterness Units: a measure of isomerised alpha acids in beer. | Compact and commonly misunderstood. |
| Cocktails | **Dry shake** — Shaking a cocktail without ice to emulsify ingredients before chilling. | Precise, practical, one line. |
| Cooking | **Maillard reaction** — Browning caused by amino acids and sugars reacting under heat. | The most useful cooking term. |
| Baking | **Autolyse** — Resting flour and water before adding yeast to develop gluten. | Distinctive and practical. |
| Gardening | **Bolting** — A plant flowering prematurely, usually in response to heat or stress. | Compact and diagnostic. |
| Foraging | **Mycorrhizal** — A fungus living in symbiosis with plant roots. | Essential for safe foraging. |
| Birding | **Lifer** — A species seen for the first time by a birder. | Cultural vocabulary; viral. |
| Chess | **Zugzwang** — A position where any move worsens the player's position, but passing is not allowed. | The most elegant one-liner in games. |
| Poker | **Pot odds** — The ratio of the current pot to the cost of calling. | Compact and genuinely useful. |
| Bridge | **Finesse** — A play that relies on a favourable position of an opponent's honour definition. | Niche but loyal. |
| Photography | **Reciprocity failure** — Loss of effective exposure at very long or very short shutter speeds. | The term that separates enthusiasts from beginners. |
| Music production | **Gain staging** — Setting levels through a signal chain to preserve headroom and avoid noise. | Practical and compact. |
| Watches | **Complication** — Any watch function beyond simple timekeeping. | Short, precise, enthusiast-friendly. |
| Cars | **Differential** — A gear set that lets driven wheels turn at different speeds. | The classic "what does this part do" term. |
| F1 | **Undercut** — Pitting earlier than a rival to gain track position on fresher tyres. | Trendy, compact, social. |
| Film photography | **Bracketing** — Shooting the same scene at several exposures to choose the best later. | Practical and stable. |

**Format needs:** images for wine labels, coffee gear, plants, and watches.

---

### 14. Sports & games

Sports vocabulary is a natural fit: short terms, passionate audiences, and constant
commentary that assumes you already know the words. The two-way quiz works especially well
for tactics and rules, where the term is spoken but rarely defined.

| Collection | A sample definition | Why it works |
| --- | --- | --- |
| Cricket | **Googly** — A leg-spinner's delivery that turns the opposite way from the expected direction. | Cricket's vocabulary is a whole language. |
| Cricket | **LBW** — Leg before wicket: a dismissal when the ball would have hit the stumps but struck the batter's leg first. | Rules-heavy; ideal quiz. |
| Football / soccer | **Gegenpressing** — Counter-pressing immediately after losing the ball. | Modern tactical vocabulary. |
| Football / soccer | **xG** — Expected goals: the probability that a given shot becomes a goal. | Stats literacy; compact. |
| Baseball | **WAR** — Wins above replacement: a single estimate of a player's total value. | Sabermetrics gateway. |
| Baseball | **Balk** — An illegal pitching motion that deceives baserunners. | Notoriously confusing; great definition. |
| Basketball | **True shooting percentage** — A shooting efficiency metric that accounts for twos, threes, and free throws. | Compact and modern. |
| Tennis | **Let** — A serve that clips the net and lands in, which is replayed. | Simple, precise. |
| Golf | **Handicap** — A numerical measure of a golfer's potential ability. | Widely used, widely misunderstood. |
| F1 | **DRS** — Drag reduction system: an adjustable rear wing that reduces drag for overtaking. | Trendy; short. |
| Running | **Lactate threshold** — The intensity above which blood lactate rises faster than it can be cleared. | Fitness literacy; compact. |
| Climbing | **Onsight** — Climbing a route first try with no prior beta. | Cultural vocabulary; viral. |
| Chess | **Fork** — A single piece attacking two or more enemy pieces at once. | The first tactic every player learns. |
| MTG | **Trample** — Excess combat damage that carries over to the defending player. | Keyword-dense game; perfect collection. |
| D&D | **Opportunity attack** — A reaction triggered when a creature leaves an enemy's reach. | Rules vocabulary; loyal audience. |
| Esports | **Meta** — The dominant strategy set in a game at a given time. | Cross-game term; compact. |

**Format needs:** images for positions and tactics; otherwise text-only.
**Caution:** trademarked game terms are fine to describe, but do not imply endorsement.

---

### 15. Languages

The biggest learning market in the world, and the most commoditised. Raw vocabulary is
already solved by Anki and Duolingo. The differentiated collections are the ones that teach the
**concepts** of a language rather than a word list.

| Collection | A sample definition | Why it works |
| --- | --- | --- |
| Spanish grammar | **Subjunctive** — A verb mood expressing doubt, desire, or unreality rather than fact. | The wall every learner hits. |
| French grammar | **Passé composé** — A past tense formed with an auxiliary verb and a past participle. | Compact and exam-friendly. |
| German grammar | **Dative case** — The case marking an indirect object or certain prepositions. | Case systems are definition-dense. |
| Japanese | **Particle** — A small word that marks the grammatical role of the phrase before it. | The core of Japanese syntax. |
| Japanese | **Keigo** — The polite register used in formal and business settings. | Cultural literacy; compact. |
| Mandarin | **Tone** — A pitch contour that changes a syllable's meaning. | The first concept every learner needs. |
| Mandarin | **Radical** — A component that hints at a character's meaning or pronunciation. | Makes the writing system tractable. |
| Korean | **Honorific** — A grammatical form that raises the status of the person addressed or discussed. | Compact and culturally central. |
| Arabic | **Root** — A three-consonant skeleton from which related words are formed. | The organising idea of Arabic morphology. |
| Linguistics | **Code-switching** — Alternating between languages or registers within a conversation. | Popular and compact. |
| Etymology | **Cognate** — A word related to another by descent from a common ancestor. | Cross-language literacy. |
| Idioms | **False friend** — A word that looks similar in two languages but means something different. | Endlessly useful; viral. |

**Format needs:** audio and pronunciation (IPA). Without audio, this is a reading-only collection.
**Verdict:** build it as a grammar-concepts collection, not as a vocabulary collection.

---

### 16. General knowledge & list knowledge

The most viral family, and the weakest on stakes. These collections are "trivia with a memory
layer": capitals, elements, constellations, dog breeds. They will not make anyone a
professional, but they make an excellent daily habit and a great acquisition channel.

| Collection | A sample definition | Why it works |
| --- | --- | --- |
| World capitals | **Canberra** — The capital of Australia, chosen as a compromise between Sydney and Melbourne. | Perennial quiz content. |
| Chemical elements | **Tungsten** — The metal with the highest melting point, used in filaments and cutting tools. | Compact and surprising. |
| SI units | **Candela** — The SI unit of luminous intensity. | Short and precise. |
| Greek alphabet | **Sigma** — The eighteenth letter of the Greek alphabet, used for sums and standard deviation. | Cross-disciplinary literacy. |
| NATO alphabet | **Alfa** — The code word for the letter A in the NATO phonetic alphabet. | Instantly useful. |
| Constellations | **Orion** — A prominent equatorial constellation containing the belt and Betelgeuse. | Visual and memorable. |
| Greek & Roman gods | **Hermes** — The Greek messenger god, associated with travel, trade, and thieves. | Cultural literacy. |
| Phobias | **Agoraphobia** — Fear of places or situations where escape might be difficult. | Commonly misunderstood. |
| Collective nouns | **Murder** — The collective noun for a group of crows. | Pure delight; highly shareable. |
| Dog breeds | **Basenji** — A Central African breed known for not barking. | Distinctive and compact. |
| Gemstones | **Cabochon** — A gem cut with a smooth, domed top and no facets. | Precise and visual. |
| Cloud types | **Cumulonimbus** — A towering vertical cloud associated with thunderstorms. | Everyday meteorology. |
| Rock types | **Obsidian** — Volcanic glass formed when lava cools too quickly to crystallise. | Compact and vivid. |
| Wine regions | **Bordeaux** — A French region known for blended red wines based on Cabernet Sauvignon and Merlot. | Gateway to wine geography. |
| Space missions | **Apollo 11** — The first crewed mission to land humans on the Moon. | Historical anchor. |

**Format needs:** images for flags, breeds, constellations, and gemstones.
**Verdict:** excellent top-of-funnel, weak retention. Use it to acquire users, not to define
the product.

---

## 04 · The shortlist

Twenty collections, scored on four dimensions. **Fit** combines corpus, stability, distractor
density, and text-only teachability. **Demand** combines audience size, stakes, and
willingness to pay. **Competition** is inverted: 5 means crowded, 1 means open. **Data**
means how easy it is to build a traceable, accurate corpus.

| # | Collection | Fit | Demand | Competition | Data | Angle |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Software interview glossary | 5 | 5 | 3 | 5 | The largest audience with the worst-designed incumbents. |
| 2 | Statistics & data literacy | 5 | 5 | 2 | 5 | Every profession needs it; almost nobody teaches the vocabulary well. |
| 3 | Medical terminology | 5 | 5 | 3 | 4 | Prefix-root-suffix structure makes it uniquely scalable. |
| 4 | Finance & accounting certs | 5 | 5 | 3 | 4 | High willingness to pay; stable definitions. |
| 5 | Cloud & DevOps certs | 4 | 5 | 3 | 5 | Certification-driven; public docs; fast refresh. |
| 6 | Cybersecurity certs | 4 | 5 | 3 | 4 | Security+ and CISSP are vocabulary exams in disguise. |
| 7 | Nursing & NCLEX | 5 | 5 | 3 | 3 | High stakes, loyal audience, weak consumer tooling. |
| 8 | Law & 1L | 4 | 4 | 3 | 3 | Latin maxims and doctrinal pairs are perfect definitions. |
| 9 | Psychology & biases | 4 | 4 | 3 | 4 | Viral, stable, and a natural bridge to daily practice. |
| 10 | Trades & licensing | 4 | 4 | 1 | 3 | The most under-served high-stakes market. |
| 11 | Product, marketing & strategy | 4 | 4 | 4 | 4 | Corporate upskilling; strong B2B angle. |
| 12 | Engineering (all disciplines) | 5 | 3 | 3 | 4 | The current engine already fits; easiest expansion. |
| 13 | Test prep vocabulary | 5 | 5 | 5 | 4 | Huge but commoditised; only enter with a sharper format. |
| 14 | Languages (grammar concepts) | 4 | 5 | 5 | 4 | Massive market; differentiate on concepts, not word lists. |
| 15 | Music theory | 4 | 3 | 3 | 4 | Passionate audience; compact, stable terms. |
| 16 | History & civics | 4 | 4 | 3 | 4 | Event-plus-significance fits one line surprisingly well. |
| 17 | Aviation & sailing | 4 | 3 | 2 | 3 | High-stakes licensing with almost no good study apps. |
| 18 | Chess & poker | 3 | 3 | 3 | 3 | Cultural vocabulary; great retention, low stakes. |
| 19 | Wine, coffee & tea | 3 | 2 | 2 | 3 | Premium hobby audience; image-heavy. |
| 20 | General knowledge | 3 | 4 | 4 | 4 | Top-of-funnel virality, not a core product. |

### If you only build three

1. **Software interview glossary.** Largest reachable audience, free canonical sources, and
   the incumbents are ugly. It also proves the app can handle a non-STEM-exam corpus.
2. **Statistics & data literacy.** The most universally useful collection in the catalog, and the
   one with the least good competition. It crosses every profession.
3. **Medical terminology.** The best demonstration of the format's real power: a huge,
   structured, high-stakes vocabulary that rewards daily practice.

### If you want a defensible niche

Trades and licensing. Electricians, HVAC technicians, plumbers, pilots, and sailors are
large audiences with real exams, stable vocabularies, and almost no well-designed study
tools. The collections are cheap to build and the competition is asleep.

### If you want virality

General knowledge, chess, wine, and cognitive biases. These are the collections people send to
friends. They will not pay the bills on their own, but they fill the top of the funnel.

---

## 05 · What each domain needs from the format

The current definition is `term`, `definition`, `formula`. That is enough for ECE and for most of
the catalog. The exceptions are predictable:

| Extension | Domains | Why |
| --- | --- | --- |
| **Formula / units** | Engineering, physics, chemistry, finance, statistics | Already supported in the `formula` cue; keep measurement units there. |
| **Code snippet** | Programming, data, DevOps | A definition of `map()` is weaker without its signature. |
| **Pronunciation / audio** | Languages, medicine, aviation | The term must be sayable, not just recognisable. |
| **Image / diagram** | Anatomy, art, architecture, biology, geography | Some terms are visual before they are verbal. |
| **Symbol / notation** | Math, logic, music | The glyph is part of the meaning. |
| **Citation / jurisdiction** | Law, policy, standards | A definition without its jurisdiction is misleading. |
| **Example sentence** | Languages, rhetoric, writing | Shows the term in use. |
| **Confusables** | Everywhere | Powers better distractors and a "compare" mode. |
| **Collection / subject tag** | Test prep, certifications | Already handled by the file hierarchy; no extra field needed. |

### A generic definition

```json
{
  "id": "bioavailability",
  "term": "Bioavailability",
  "definition": "The fraction of a dose that reaches systemic circulation unchanged.",
  "formula": "F = AUC_oral / AUC_IV",
  "unit": 3,
  "unitTitle": "Pharmacokinetics",
  "aliases": [],
  "confusables": ["half-life", "volume-of-distribution", "clearance"],
  "sources": ["textbook#p.42"]
}
```

The `confusables` field is the highest-leverage addition. The current quiz picks distractors
from the same subject; explicit confusables make every round feel authored rather than
random.

### A generic taxonomy

The current `semester → subject → unit → definition` hierarchy already generalises:

```
domain        medicine
collection    USMLE Step 1
section       core
subject       pharmacology
unit          pharmacokinetics
definition    bioavailability
```

Rename `semester` to `section` in the data layer, treat the whole curriculum as a
collection, keep the UI label configurable, and the whole catalog fits the existing engine.
The daily goal, heatmap, mastery bars, and adaptive sampling are already domain-agnostic.

---

## 06 · Where this format is weak

Be honest about the boundary. These are the domains that look attractive and are not:

| Weak fit | Why | What would fix it |
| --- | --- | --- |
| Radiology, dermatology, histology | Diagnosis is visual pattern recognition. | Image-based definitions with a reveal. |
| Surgery, driving, welding, cooking | The skill is procedural, not verbal. | Video or simulation; not this app. |
| Mathematical proof | Knowing the definition is not the same as constructing the argument. | Worked derivations, not one-liners. |
| Legal case analysis | The skill is applying doctrine to facts. | Case briefs and issue-spotting drills. |
| Clinical decision-making | Judgment under uncertainty. | Cases and vignettes. |
| Negotiation, management, sales | Behavioural skill. | Role-play and feedback. |
| Rapidly changing tooling | Definitions churn monthly. | Short, dated collections with a refresh cadence. |
| Contested science | Experts disagree on the definition. | Present the disagreement, not a single key. |
| Pronunciation-first language learning | Text alone teaches the wrong thing. | Audio and speech practice. |
| Programming fluency | Knowing "closure" does not mean you can use one. | Code challenges alongside the collection. |

The pattern: **one-liners teach the map, not the driving.** That is fine. Most people need
the map first.

---

## 07 · Packaging the catalog

Do not build thirty apps. Build one library with collections.

- **One brand, many collections.** `one·liners — Electronics, in one line.` becomes
  `one·liners — Medicine, in one line.` The pattern is the product.
- **One memory, many collections.** A single mastery store, a single daily goal, a single
  heatmap. Switching collections should not reset the habit.
- **A collection is a JSON file plus a source manifest.** That is already the shape of the ECE
  seed work. It makes community contributions and review possible.
- **A collection page is a landing page.** `one·liners/medicine` can rank for "medical terminology
  practice" without a separate app.
- **Free core, paid certification packs.** The free collection builds the habit; the exam pack
  captures the willingness to pay.
- **Source traceability is the moat.** Anyone can generate definitions with a model. Very
  few can show the page, slide, or standard behind every definition. The ECE seed pipeline is
  already the right instinct; make it the rule for every collection.

### A suggested library structure

```
data/collections/
  software-interview-glossary/
  system-design/
  cloud-certifications/
  medical-terminology/
  pharmacology/
  nursing-and-nclex/
  accounting/
  investing/
  real-estate-licensing/
  us-legal-literacy/
  contracts/
  electrical-licensing-nec/
  hvac-licensing/
  aviation-ppl/
  film/
  philosophy/
  wine/
```

Each folder is a collection with `plan.json`, `collection.json`, `runtime.json`,
`sources.json`, and a `subjects/` directory. Each subject has units and definitions. The app
can load `data/collections/index.json` instead of a single curriculum.

---

## 08 · Sourcing and licensing notes

- **Prefer official glossaries and standards.** NIST, MDN, Kubernetes docs, AWS docs, ISO,
  exam-board syllabi, and professional bodies publish stable definitions.
- **Paraphrase, do not copy.** Definitions are facts, but the sentences expressing them can
  be copyrighted. Write the one-liner yourself and cite the source.
- **Never copy question banks.** Exam questions are protected and often licensed
  exclusively. Definitions are not the same as questions.
- **Label jurisdiction and version.** Law, tax, insurance, and cloud certifications change
  by jurisdiction and year.
- **Respect trademarks.** Game terms, brand names, and certification names can be described
  nominatively, but do not imply affiliation.
- **Add a disclaimer** for medical, legal, and financial collections: educational vocabulary, not
  professional advice.
- **Refresh cadence.** Stable collections (anatomy, music theory) can last years. Volatile collections
  (AI tooling, crypto, cloud) need a dated review.

---

## 09 · The one-paragraph answer

The format generalises to any field with a large, stable, examinable vocabulary and a dense
set of near-neighbours. The strongest markets are software and data, medicine and nursing,
finance and accounting, law, cloud and cybersecurity, and the trades — all high-stakes, all
glossary-shaped, all poorly served by beautiful software. Psychology, statistics, product,
and engineering are strong second-wave collections. Languages and test prep are huge but crowded;
enter them only with a sharper format or a specific exam. Hobbies and general knowledge are
the acquisition layer, not the product. Build the library, not the app: one memory, many
collections, every definition traceable to a source.
