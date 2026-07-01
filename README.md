# Responsible AI — Assignment 1 (Ideation, Prototype & Data)

DBA / Golden Gate University via UpGrad · **Cohort 8, Group 8**
Course: *Responsible AI — Building AI Systems That Truly Deliver Value* (DARWIN framework)
Instructor: Prof. Dr. Venkatesh Sunkad

## What this is

Assignment 1 deliverables plus the full **build-and-evaluation process** behind them.
Three business problems were ideated in parallel, scored against an adversarial
evaluator panel, hardened against must-fix findings, and re-scored.

The central discipline the course grades on: **a prototype is not a product** —
quick, disposable, fail-fast, validates the *business case* (not the technology),
and tests 1–2 falsifiable hypotheses with reproducible measurement.

## The three use cases

| Domain | Problem | Shared pattern |
|--------|---------|----------------|
| **Healthcare** | CareBridge reviewer-packet lift | AI prepares, the human owns the adverse decision |
| **Education** | GradeAssist LLM pre-grading | Instructor owns the grade |
| **Finance** | Credit decision co-pilot | Underwriter owns the decline |

## Scores (out of 50)

| Use case | Gate-1 | Hardened |
|----------|:------:|:--------:|
| Healthcare | 46 | **48** |
| Education | 46 | **46** |
| Finance | 44 | 44 *(not yet hardened)* |

## Assignment submission (converges to one problem)

The brief requires **one business problem per group**, carried through Assignment 1 **and 2**.
The three above were a *selection funnel* (ideate → score → harden → rank); the graded
submission converges to **Healthcare — CareBridge**, chosen for its Assignment-2 runway
(infrastructure / economics / scaling), not just its A1 score. The other two stay in the
report as the funnel that chose it.

The two required standalone documents:
- **Ideation document** → `usecases/healthcare/ideation.md`
- **Data document** → `usecases/healthcare/data-document.md` *(hits the 11-July-prep data bars: missing-%, leakage, training-bias, recency)*

Presentation: live from `rai-assignment-report.html` (Healthcare section). If the portal
requires an uploaded `.pptx`, export that section to PDF/PPT — confirm the format with the group.
A2 runway note: `usecases/healthcare/A2-forward-check.md`. Deadline: **12 July**.

## Repo map

```
EVALUATORS.md            Scoring instrument — 2 evaluators (Sunkad Prototype-Purist
                         + Adversarial CFO/SWAT), Gate-0 checklist, <3 ratchet rule
SCORECARD-GATE1.md       Score matrix + per-domain must-fixes + re-score deltas
rai-assignment-report.html   Self-contained report: process, panel, scores, all 3 ideations
explainer.html            Visual scroll-based deep-dive (7 frames) — between the video and the report
usecases/
  healthcare/  education/  finance/   ideation.md (+ .v1.md pre-harden backups)
source-docs/             Converted assignment brief, course outline, translation template
```

## View the report

Open `rai-assignment-report.html` in a browser. Mermaid prototype diagrams render
via CDN on first open (readable as text if offline).

## View the explainer

Open `explainer.html` for a visual, scroll-based deep-dive — the middle layer
between the 75-second video and the full report. Seven frames cover the thesis,
the prototype discipline, the three use cases, the shared pattern, the build
process, the evaluator panel, and the final scores.
