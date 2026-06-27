# RAI Assignment 1 — Evaluator Panel & Quality Ratchet

**Course:** Responsible AI: Building AI Systems That Truly Deliver Value (Cohort 8, Dr. Venkatesh Sunkad)
**Assignment:** Slot 1 — Ideation, Prototype, Data
**Group:** 8 (Etuhoko, Kumar, Gupta, Thejeswarareddy, Reddimasu) — *confirm*

Purpose: keep us honest at every milestone so the final deliverables are high-quality, not just complete. Two standing evaluators + a mechanical gate score every milestone. An independent AI model joins on the final pass only. The **ratchet** blocks advancing while any dimension scores below 3.

---

## The Ratchet Rule (non-negotiable)

At each gate, every evaluator scores its dimensions **1–5**.

- **Any dimension < 3 -> BLOCKED.** Cannot advance until remediated and re-scored.
- Record every score in the scorecard. No verbal "looks good."
- A dimension is "fixed" only when the same evaluator re-scores it >= 3 against the *changed* artifact — not against a promise to change it.

Rationale: depth and insight are graded ("aesthetics not important"). The ratchet forces depth at each step instead of a last-minute scramble.

---

## Evaluator A — "Professor Sunkad" (Prototype Purist)

Models the actual grader's worldview, straight from the June 21 lecture. Most predictive evaluator of the grade.

**Binary kill-question (ask first):** *"Did you build a product and call it a prototype?"*
If yes -> A1 auto-capped below 3. Stop and re-scope.

| Dim | Scores | 1 (fail) | 5 (pass) |
|-----|--------|----------|----------|
| **A1** | Prototype-not-product | Polished, end-to-end, production-shaped; can't be thrown away | Quick, dirty, disposable; discard tomorrow with no loss |
| **A2** | Right tool for the job | AI/LLM forced where automation/analytics/formula fits | Solution type matches Section-1 category; AI only where it earns its place |
| **A3** | Focused hypothesis | Tests everything; sprawling | Tests **1-2** sharp hypotheses, nothing more |
| **A4** | Fail-fast design | No way to fail; success guaranteed | Clear, fast fail condition revealing a missing core value |
| **A5** | Validates business case, not tech | Proves "the tech works" | Proves (or disproves) the **business value** exists |

---

## Evaluator B — "Adversarial CFO" (SWAT / So-What)

Forces business value, falsifiability, defensible ROI. Catches the second failure mode: impressive tech, no money.

**Binary kill-question (ask first):** *"If this works perfectly, does the business make or save money — and can you prove the number?"*

| Dim | Scores | 1 (fail) | 5 (pass) |
|-----|--------|----------|----------|
| **B1** | So-What value clarity (SWAT not SWOT) | Vague "improve experience" | Sharp goal tied to revenue/cost |
| **B2** | ROI defensibility | Round numbers, no derivation | Explicit Fermi math, traceable assumptions (cf. lecture's $60k-per-1% build-up) |
| **B3** | Business metric defined | Conflated with technical metric | Distinct metric proving value delivered (e.g., does intervention help; same-day vs next-day) |
| **B4** | Technical metric defined | Hand-wave "accuracy" | Precise, reproducible (precision/recall, measurable target) |
| **B5** | Falsifiability | No threshold could kill it | A specific number/threshold that would end the idea |

---

## Gate 0 — Completeness Checklist (mechanical, every gate)

Binary pass/fail. Run before A and B so they don't waste attention on missing pieces.

- [ ] Section 1: nature-of-problem category marked + one-sentence solution type
- [ ] Section 1.1: business goal + specific problem (success/failure def, timeframe, scope, metrics)
- [ ] Section 2: end users + how they use output + envisioned workflow
- [ ] Section 3: current state + current accuracy + **quantified** ROI
- [ ] Section 4: specific data named + cleanliness rating (1-5) + deployment model
- [ ] Data Document exists with **named, real** sources
- [ ] Prototype diagram present
- [ ] Written justification: **why prototype, not product**
- [ ] **Both** business AND technical metrics stated
- [ ] Every quantitative claim has a source or stated assumption

Any unchecked box -> BLOCKED.

---

## Gates (when the panel runs)

| Gate | Trigger | Who runs |
|------|---------|----------|
| **Gate 1** | Ideation doc (Sections 1-4) drafted | Gate 0 -> A -> B |
| **Gate 2** | Prototype diagram + metrics drafted | Gate 0 -> A -> B (B hard on business *and* technical metrics) |
| **Gate 3 (Final)** | Full draft + presentation assembled | Gate 0 -> A -> B -> Independent model -> Q&A simulator |

**Independent model (Final only):** dispatch Gemini and/or Codex (via /ai-pair or research-trio) to score the final draft against the A+B rubric *independently* — blind to our scores — then diff against ours. Breaks the author's blind spots. Anything they flag <3 re-enters the ratchet.

**Q&A simulator (Final only):** generate the 3 hardest questions a skeptical examiner asks in the 3-min Q&A; we must have answers before submitting.

---

## Scorecard (fill at each gate)

### Gate 1 — Ideation doc (scored 2026-06-26, adversarial panel)
**HEALTHCARE** — Gate0 PASS | A 5/5/5/5/5 | B 5/3/3/5/5 | lowest 3 | **PASS** (B2/B3 must-fix)
**EDUCATION** — Gate0 PASS | A 5/5/4/4/5 | B 5/4/5/5/4 | lowest 4 | **PASS** (underpowered kills)
**FINANCE**  — Gate0 PASS | A 5/5/3/4/5 | B 4/4/5/4/5 | lowest 3 | **PASS** (A3 bundling, cost denominator)
See SCORECARD-GATE1.md for justifications + per-domain must-fixes.
**RE-SCORE after hardening (Healthcare+Education):** Healthcare 46->**48** (B2,B3 3->4, caps cleared); Education 46->46 (B5 4->5 fairness powered-gate, worst problems fixed). Both PASS. Finance left at v1 (44). See SCORECARD-GATE1.md delta. Originals saved as ideation.v1.md.
 Cross-cutting fixes: (1) unbundle hypotheses -> 1 primary powered endpoint; (2) power calc / demote unsupported kill thresholds.

### Gate 2 — Prototype + metrics
| Evaluator | Dimension scores (1-5) | Min | Status |
|-----------|------------------------|-----|--------|
| Gate 0 | _/10 boxes | — | [ ] |
| A (Sunkad) | A1_ A2_ A3_ A4_ A5_ | _ | [ ] |
| B (CFO) | B1_ B2_ B3_ B4_ B5_ | _ | [ ] |
| **Advance?** | | | [ ] BLOCKED / [ ] PASS |

### Gate 3 — Final
| Evaluator | Dimension scores (1-5) | Min | Status |
|-----------|------------------------|-----|--------|
| Gate 0 | _/10 boxes | — | [ ] |
| A (Sunkad) | A1_ A2_ A3_ A4_ A5_ | _ | [ ] |
| B (CFO) | B1_ B2_ B3_ B4_ B5_ | _ | [ ] |
| Independent (Gemini/Codex) | _summary | _ | [ ] |
| Q&A simulator | _3 hardest Qs answered? | — | [ ] |
| **Submit?** | | | [ ] BLOCKED / [ ] SHIP |
