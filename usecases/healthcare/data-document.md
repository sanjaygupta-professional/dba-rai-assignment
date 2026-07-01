# CareBridge Reviewer-Packet Lift — Data Document

> Standalone data-document deliverable for Assignment 1 (per brief §2). The ideation
> document (`ideation.md`) summarizes this; this file is the fuller graded artifact and
> explicitly answers the data-quality bars raised in the 11-July-prep class session:
> **missing data, data leakage, training bias, and recency/relevance.**

**Business problem (one line):** does an AI-assembled decision packet let a licensed UM
nurse review a prior-authorization case faster **without** degrading clinical safety? The
data below is what the throwaway prototype consumes to test that — nothing more.

---

## 1. Data items and their types

Classified by variable type, because the type dictates both cleaning and leakage risk.

| Data item | Type | Structure |
|---|---|---|
| Member ID, plan ID, provider NPI | Categorical (nominal, identifier) | Structured |
| Requested service code (CPT/HCPCS), diagnosis (ICD-10-CM) | Categorical (nominal) | Structured |
| Urgency flag, service line | Categorical (nominal) | Structured |
| Lab values (LOINC-coded) | Numeric (continuous) + date | Structured |
| Rx-claim history (NDC, fill dates) | Categorical + date (discrete) | Structured |
| Physician notes, consult/discharge summaries, imaging report text | **Unstructured free text** | **Unstructured** |
| Medical-necessity policy corpus (+ version ID, effective date) | Text + ordinal version | Semi-structured |
| Historical adjudicated decision / appeal / overturn (**test labels only**) | Categorical (nominal) | Structured |

**Structured vs unstructured split:** the request envelope, labs, and claims (~structured,
clean) are *not* where the AI earns its keep. The two **load-bearing inputs are
unstructured** — free-text clinical notes and the version-drifting policy corpus. Consistent
with the enterprise reality that ~75–80% of decision-relevant content lives in unstructured
text, that is exactly where quality risk concentrates.

---

## 2. Data sources

**Real test data:** the payer's own historical adjudicated PA cases (PHI) — ~500 cases,
structured fields + note PDFs, pulled from the data warehouse under a HIPAA **limited-data-set
agreement**. Sensitivity: **high (PHI)**, handled on-prem only. Retrospective and
already-adjudicated, so zero patient risk.

**Public proxies** (build the throwaway harness with no PHI):

| Source | Proxies for | Access | Sensitivity |
|---|---|---|---|
| MIMIC-IV + MIMIC-IV-Note (PhysioNet) | Real de-identified notes, labs, discharge summaries | Credentialed + CITI + DUA | De-identified, moderate |
| CMS Medicare Coverage Database (NCD/LCD) | Version-dated medical-necessity criteria | Public, mcd.cms.gov | None |
| CMS HCPCS / ICD-10-CM / CPT | Code validation | Public (CPT via AMA license) | None / license |
| Synthea (synthetic FHIR) | End-to-end plumbing + edge cases, no PHI | Local, open-source | None (synthetic) |
| X12 278 samples | PA request/response envelope | WEDI / vendor samples | None |

Proprietary criteria engines (InterQual, MCG) are deliberately excluded so the prototype
carries no licensing dependency.

---

## 3. Data quality

**Cleanliness rating: 3 / 5.** Structured fields (codes, claims, labs) rate ~4–5. The rating
is pulled down by the two inputs that matter most: clinical notes are abbreviation-heavy and
OCR-contaminated where faxed (~2–3), and the policy corpus suffers **version drift** —
overlapping editions where identifying the *applicable* version is itself error-prone (~3).
The 3/5 is deliberately set by what could **fail silently**, not by the average field.

**Missing data.** The design tolerance is the standard ~**15–20% ceiling** for any field we
would impute: above that, imputation fabricates rather than fills. Applied here:
- **Structured fields** (codes, labs, claims): near-complete on adjudicated cases; well inside tolerance.
- **Unstructured evidence:** missingness is the *core clinical signal*, not noise — a missing
  TB screen or absent DMARD-trial note is exactly what the packet must surface as
  "uncertain → PEND," **never impute.** So we do **not** fill missing clinical evidence; we flag it.
- **Screening rule:** any case whose *structured* fields exceed the 15–20% missing ceiling is
  dropped from the 500-case sample rather than imputed, to keep the touch-time signal clean.

---

## 4. Data-leakage check (the sharpest risk here)

Because the prototype **scores recommendations against historical adjudicated outcomes**, leakage
is the failure most likely to produce a flatteringly wrong result. Three guards:

1. **Label leakage (primary risk).** The historical decision/appeal/overturn is the *test
   label* — it must **never** enter packet assembly as an input feature. The RAG+LLM layer sees
   only the evidence and policy that were available *at decision time*; the outcome is revealed
   only at scoring. Any note field that post-dates or references the final determination is
   stripped before assembly.
2. **Inference-time mirror.** Training/development inputs must mirror what is actually available
   at live inference. We use only pre-decision evidence — no post-hoc corrected codes, no
   appeal-stage documents, no downstream chart additions — so measured accuracy is not inflated
   by data that would be absent in production. (This is the elevator-predictive-maintenance
   trap from class, applied: don't train on signals unavailable at inference.)
3. **Temporal split.** Version-pin each case's policy to its *effective-at-decision* edition, so
   the packet is not "graded" against a policy revision that did not exist when the case was decided.

---

## 5. Training / historical-bias check

The dangerous bias is **not** the model inventing prejudice — it is the model **learning
historical denial bias as ground truth.** Because we score against past adjudications, any
demographic skew in historical denials would be silently rewarded as "accuracy."

- **Efficiency benchmark only.** The historical label is used to test *touch-time and
  concordance*, **never** as a fairness benchmark.
- **Stratified reporting.** Report touch-time and concordance by **age band × sex × payer line
  (Medicaid vs commercial)** — as a **directional fairness flag only**, since per-cell N is too
  small for a powered differential test.
- **Style/representation analog.** The résumé-screening lesson (removing explicit gender markers
  was insufficient because language style still encoded it) applies to free-text notes:
  documentation style varies by provider and setting and can proxy for demographics. Any skew
  flag **triggers a powered fairness sub-study** before a pilot — it is not waved through, nor
  falsely "cleared" by an underpowered prototype.

---

## 6. Recency / relevance

- **Policy corpus:** must be the edition **effective at each case's decision date** — stale or
  future policy versions invalidate the criteria mapping. Version-pinning is a hard requirement,
  not a nicety.
- **Clinical evidence:** cases drawn from a recent window (aligned to current criteria) so the
  test reflects today's review reality, not legacy practice patterns. (More data is not better;
  *relevant, current* data is — the 1960s-stock-price lesson.)
- **Code sets:** ICD-10-CM/HCPCS/CPT pinned to the case-year release to avoid anachronistic
  code mismatches.

---

## 7. Governance and sustainment

- **Access:** PHI on-prem/VPC-isolated; only de-identified, structured criterion summaries reach
  the managed LLM. No raw note, name, or MRN in any prompt.
- **Audit:** every assertion, citation, recommendation, and human action written to an immutable,
  access-controlled log.
- **Sustainment (the neglected success factor).** Data quality is not a one-time cleanse. Post-test,
  ownership of policy-version currency and note-quality monitoring must sit with a named data owner;
  without that governance, packet groundedness degrades as policies drift. Flagged now because the
  class session stressed that sustaining quality *after* the project is where most efforts fail.

---

*Companion documents: `ideation.md` (ideation), and the prototype design + metrics within it
(§Prototype Design / §Prototype Metrics).*
