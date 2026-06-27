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

## Repo map

```
EVALUATORS.md            Scoring instrument — 2 evaluators (Sunkad Prototype-Purist
                         + Adversarial CFO/SWAT), Gate-0 checklist, <3 ratchet rule
SCORECARD-GATE1.md       Score matrix + per-domain must-fixes + re-score deltas
rai-assignment-report.html   Self-contained report: process, panel, scores, all 3 ideations
usecases/
  healthcare/  education/  finance/   ideation.md (+ .v1.md pre-harden backups)
source-docs/             Converted assignment brief, course outline, translation template
```

## View the report

Open `rai-assignment-report.html` in a browser. Mermaid prototype diagrams render
via CDN on first open (readable as text if offline).
