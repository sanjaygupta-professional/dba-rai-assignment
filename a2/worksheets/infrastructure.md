# Infrastructure worksheet — owner: Thejas (edit every number you disagree with)

Defaults below come from the A1 Fermi model (`usecases/healthcare/ideation.md` §3) and the
professor's A2 brief. Your job: **edit, not create.** Anything you leave untouched you must
still be able to defend in Q&A.

## 1. CPU or GPU — and why

Brief demands: state CPU or GPU for prototype/MVP, justify, address cost–latency trade-off.

**Default position (edit):**
- **Prototype:** CPU-only. Batch, retrospective, zero latency requirement. Packet assembly for
  500 historical cases is an overnight batch job. CPU inference on a small model (or managed
  API) is the cost lever the brief itself names.
- **MVP:** hybrid. On-prem GPU (1–2× L40S/A10 class) ONLY for the PHI-side embedding +
  retrieval over raw notes; managed LLM API for de-identified criterion summaries.
  PA adjudication SLA is measured in **hours/days, not milliseconds** → real-time GPU serving
  is unjustifiable. Delayed/batch processing is the honest answer.

## 2. Fermi sizing (do the arithmetic aloud in Q&A)

- Volume: 390K human-reviewed cases/yr ≈ **1,500/working day** ≈ 190/hr in an 8-h day.
- Per case: ~30 pages notes ≈ 40K tokens in, packet ~2K tokens out.
- Daily tokens: 1,500 × 42K ≈ **63M tokens/day**.
- Managed API at ~$3/M in + $15/M out (edit to current pricing): ≈ $200–250/day ≈ **$60–75K/yr**
  → matches A1 run-cost line ($40–80K managed LLM). Sanity ✓
- Embedding GPU: 63M tokens/day ÷ ~10K tokens/s on one mid GPU ≈ 1.75 GPU-hours/day → **one GPU
  is idle 90% of the day** → right-size or share. Say this — it shows you did the math.
- Development time estimate (brief asks): prototype 3–4 wk (A1); MVP build 2–3 quarters,
  $1.2–2.0M (A1 bottom-up decomposition).

## 3. LLM vs small model (brief asks explicitly)

**Default:** prototype/MVP = existing managed LLM (fastest to validate). Final deployed system:
evaluate distilled/quantized small model (7–8B class, LoRA-tuned on criterion-mapping) for the
de-identified reasoning step once volumes justify — breakeven ≈ when annual API spend exceeds
the ~$90–180K/yr MLOps FTE cost of self-hosting. Hybrid stays: deterministic checks are
rules/RPA, never a model.

## 4. Real-time vs batch vs delayed (brief asks)

Default: **delayed/near-line** — packet ready before the nurse opens the case (queue-ahead),
not on-click. Batch overnight for non-urgent; expedited queue (<1 h) for urgent PAs. Justify
via SLA: standard PA TAT is 3.5 business days.

## 5 anticipated Q&A cards (answer aloud at rehearsal, no slides)

1. Why not GPU everywhere? → latency budget is hours; GPU buys speed we don't need, at 5–10× cost.
2. How many GPUs at full scale? → show §2 arithmetic; ~1, mostly idle → shared/right-sized.
3. Why managed LLM if PHI? → PHI never leaves boundary; only de-identified criterion summaries go out.
4. What breaks at 10× volume? → API rate limits + embedding throughput; both scale linearly with $.
5. Cost per case? → ~$0.15–0.20 AI cost vs $10.50 nurse labor → 2% overhead on the thing it saves 35% of.
