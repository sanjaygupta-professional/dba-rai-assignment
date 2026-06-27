# Gate 1 Scorecard — Ideation Packages (adversarial panel)

Panel: Gate 0 (completeness) + Evaluator A "Sunkad" (Prototype Purist) + Evaluator B "Adversarial CFO" (SWAT). Harsh-grader mode; scored by 3 independent subagents that did not author the docs. Ratchet: PASS only if every A/B dimension >= 3 and Gate 0 has no FAIL.

## Score matrix

| Dim | Healthcare | Education | Finance |
|-----|:---:|:---:|:---:|
| Gate 0 | PASS | PASS | PASS |
| A1 prototype-not-product | 5 | 5 | 5 |
| A2 right-tool / no LLM-overuse | 5 | 5 | 5 |
| A3 focused 1-2 hypotheses | 5 | 4 | **3** |
| A4 fail-fast design | 5 | 4 | 4 |
| A5 validates business case | 5 | 5 | 5 |
| B1 sharp value | 5 | 5 | 4 |
| B2 defensible Fermi ROI | **3** | 4 | 4 |
| B3 distinct business metric | **3** | 5 | 5 |
| B4 precise technical metric | 5 | 5 | 4 |
| B5 specific kill threshold | 5 | 4 | 5 |
| **Lowest dim** | **3** | **4** | **3** |
| **A subtotal /25** | 25 | 23 | 22 |
| **B subtotal /25** | 21 | 23 | 22 |
| **Total /50** | 46 | 46 | 44 |
| **Verdict** | PASS | PASS | PASS |

## Read

- **Education — highest floor.** No dimension below 4; A and B balanced (23/23). Cleanest ROI, strongest standalone money case, fairness as a first-class kill gate.
- **Healthcare — purest prototype, thinnest money.** Sunkad gave straight 5s (best A subtotal) — the explicit CareBridge step-back is the standout narrative move. But B2/B3 = 3: touch-time estimate is circular and cost basis cites the old CareBridge deck; business vs technical metric are the same measurement in two units. Honest about its own thinness, which the panel credited.
- **Finance — solid, lowest.** Exemplary kill thresholds and tool-fit, but A3 = 3 (three bundled clauses, underpowered for all at once) and the cost denominator + "500k apps/yr = mid-size regional" scale mismatch make the $1.14M net read reverse-engineered.

## Two weaknesses SHARED by all three (cross-cutting — fix once, apply everywhere)

1. **Hypothesis bundling.** Each crams accuracy + time + fairness into "one" hypothesis. Sunkad's A3 lens. Fix: name ONE primary, statistically-powered endpoint (the time/value metric) and explicitly demote the others to guardrail/secondary.
2. **Statistical underpower.** Every kill threshold is sharper than the N behind it can fire — healthcare overturn proxy, education ESL gap (N≈20) and N=2 graders, finance ±1pp non-inferiority and 4/5ths at N=300. Fix: add a power calc / minimum-detectable-effect, or demote unsupported kills to "directional red flag -> investigate," not a hard gate.

## Domain-specific top must-fix (each)

- **Healthcare:** break the circular touch-time back-check (anchor D=14 min to an external time-motion study or a 10-case stopwatch pre-read); replace "Product report Table 21/midpoint" with an external/bottom-up cost basis or explicit ranges; make the business metric (projected $ net value, lever B ranged 50-70%) genuinely distinct from instrumentation minutes.
- **Education:** the flagship fairness kill (ESL gap > 0.5) is measured on ~20 essays — CI dwarfs the threshold; power it or demote it. Define how "gold" is built and report its own reliability (QWK 0.70 vs a 0.6-0.7 noisy ruler). Add graders beyond N=2 and cite the 12-min / $30-hr baseline.
- **Finance:** decompose line J ($0.45M) and reconcile the scale mismatch (500k apps = large lender, not mid-size — relabel or cut volume ~5x, which roughly halves the headline benefit); state achievable MDE / power at N=300; unbundle the hypothesis into one primary + guardrails.

## Recommendation

All three clear Gate 1; none is blocked. If/when down-selecting ONE to present:
- **Education** if the priority is a self-contained, defensible money case with the lowest risk of a grader poking a hole.
- **Healthcare** if the priority is the strongest *prototype-discipline narrative* (the CareBridge step-back directly demonstrates "prototype != product") — accept that the money case needs the must-fixes to survive a CFO.
- **Finance** is the weakest of the three as written, mainly on the reverse-engineered cost side.

Next: either (a) apply the cross-cutting + domain must-fixes to harden all three, then run the Gate-3 independent-model review; or (b) proceed to presentation assembly on the chosen use case(s).

---

# Gate 1 RE-SCORE after hardening (2026-06-26)

Healthcare + Education hardened against the panel must-fixes, then re-scored fresh by independent adversarial subagents (Finance left as v1). Originals preserved as `usecases/<domain>/ideation.v1.md`.

## Delta

| Dim | Healthcare v1 -> hardened | Education v1 -> hardened |
|-----|:---:|:---:|
| A1 | 5 -> 5 | 5 -> 5 |
| A2 | 5 -> 5 | 5 -> 5 |
| A3 | 5 -> 5 | 4 -> 4 (substance fixed: compound -> single powered endpoint) |
| A4 | 5 -> 5 | 4 -> 4 |
| A5 | 5 -> 5 | 5 -> 5 |
| B1 | 5 -> 5 | 5 -> 5 |
| B2 | **3 -> 4** (circular touch-time deleted; cost basis now bottom-up) | 4 -> 4 (2->4 graders + crossover; baselines now measured pre-read) |
| B3 | **3 -> 4** (business metric now $ net-value band, distinct from minutes) | 5 -> 4 (new nit: 60% accept-target "indicative") |
| B4 | 5 -> 5 | 5 -> 5 (noisy-gold circularity retired; reference reliability reported) |
| B5 | 5 -> 5 | **4 -> 5** (fairness honestly demoted to powered gate, MDE math shown) |
| **Total /50** | **46 -> 48** | **46 -> 46** (flat number, worst problems resolved) |

Verdict: both PASS. Healthcare's two caps cleared with genuine (not cosmetic) fixes -> now the top-scored package. Education flat numerically but its two *worst* prior weaknesses (underpowered fairness kill, circular gold ruler) are resolved; a softer new nit (B3) replaced them.

## Shared residual (both) — a feature, not a bug, but a Q&A talking point

Both hardened prototypes now correctly say: the headline ROI number and even the kill threshold ride on a **baseline that must be measured first** (healthcare's 10-case stopwatch pre-read for touch-time D; education's 1-hr per-grader scratch-time pre-read). A CFO cannot quote the final number *today* — but that is exactly the prototype mindset (measure the baseline before betting), so frame it as discipline, not a defect. Residual risks the panel flagged:
- **Healthcare:** the 25% kill line is derived from the un-measured D=14; if the pre-read returns D~11, breakeven climbs toward ~27% and the kill line is mis-set until measured. Overturn demoted to directional flag means the $35K test proceeds on speed+groundedness alone — groundedness is assertion-level, so decision-level anchoring harm is deferred to the powered follow-up.
- **Education:** "adequately powered" depends on SD~3min only confirmed in the pre-read; mild scope creep (classical A/B + crossover + pre-read + IRB slice) risks the 2-week window.
