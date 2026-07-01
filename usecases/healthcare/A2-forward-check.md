# Assignment 2 forward-check — why CareBridge carries

The class notes require the **same business problem** to run through Assignment 1 **and 2**,
where A2 covers **infrastructure, economics, scaling, and business metrics**. This confirms
CareBridge has that runway (it is the selection criterion, not the A1 score):

- **Infrastructure:** clear productionization path — on-prem/VPC PHI boundary + managed LLM for
  de-identified summaries, FHIR/X12 278 integration, policy version-pinning engine, immutable
  audit. A1's prototype deliberately stubs all of this, leaving it as the A2 build story.
- **Economics:** a full Fermi model already exists (build $1.2–2.0M, run $0.25–0.45M, net value
  band by touch-time reduction and human-touch lever). A2 firms these via vendor RFP — the
  scaffolding is in place.
- **Scaling:** prototype (500 retrospective cases, 2 service lines) → pilot → full 390K
  human-reviewed cases/yr across service lines is a natural staged rollout.
- **Prototype → MVP transition (the class framing):** A1 = disposable prototype validating the
  business case; **A2 = the MVP** — first customer-facing, integrated, reproducible, explainable,
  measurable version. The prototype→MVP material from class belongs here, in A2, not retrofitted
  into A1.
- **Continuity of metrics:** A1's touch-time / groundedness / concordance become the MVP's live
  performance SLAs in A2.

**Open group items:** ratify CareBridge as the single problem; assign speakers across A1+A2
(everyone speaks at least once); confirm who does the single group upload by **12 July**.
