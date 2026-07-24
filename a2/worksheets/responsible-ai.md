# Responsible AI worksheet — owner: Ashish (edit every cell you disagree with)

Defaults from A1's DARWIN-R surface (`usecases/healthcare/ideation.md` §RAI). Brief demands:
productivity gain, engagement (enabler not replacer), and per-stakeholder responsibility
(professor's Tonality example). **Edit, not create** — but own every answer in Q&A.

## 1. Productivity gain (brief asks first)

Default: 35–45% reviewer touch-time reduction (A1 primary hypothesis) → $1.43M gross annual
labor saving at 35%. NOT headcount removal — capacity release: nurses move from evidence
assembly to clinical judgment, backlog and TAT shrink (3.5 days → target <1 day on clean cases).

## 2. Enabler, not replacer (brief asks explicitly)

- AI's most adverse action is pend/route — it structurally CANNOT deny. Authority stays licensed.
- Nurse remains decision-owner; packet converts her assembly minutes into judgment minutes.
- Engagement mechanics: reviewers co-design the packet layout; overturn/disagreement button on
  every packet (her disagreement is training signal, not insubordination); publish the
  touch-time savings back to the team as capacity, not as a quota increase.
- Career story: UM nurses move up the judgment ladder (complex cases, audits, appeals), not out.

## 3. Stakeholder responsibility grid (professor's Tonality pattern — do the same)

| Stakeholder | Their responsibility question | How CareBridge answers it |
|---|---|---|
| Developers | Is the model importing racial/gender/geographic bias from historical denials? | Historical labels = efficiency benchmark only, never fairness benchmark; stratified reporting by age band × sex × payer line; flags trigger a powered fairness sub-study |
| End users (UM nurses) | Can I trust and verify what it claims? | Every assertion cited to source span, met/unmet/uncertain; groundedness ≥95% hard stop |
| Medical director | Do I still own every denial? | By design: AI cannot deny; route-for-review is its ceiling |
| Internal regulators / compliance | What data is masked, what is tracked? | PHI on-prem only; de-identified summaries out; immutable audit log of every assertion + human action |
| External regulators (CMS/state) | Is there a defensible record per adverse decision? | Packet + audit trail = the explanation artifact, per decision |
| Sponsors / managers | Is saved time real, and is the team engaged? | Powered touch-time endpoint; engagement mechanics above; capacity redeployment plan |
| Members / patients | Am I safer or worse off? | Overturn proxy ≤5% guardrail; groundedness veto; no automated denial ever |

## 5 anticipated Q&A cards

1. Bias source here? → not the model inventing bias; the model LEARNING historical denial bias as truth. Mitigation: label ≠ fairness benchmark.
2. What if nurses game it / rubber-stamp? → disagreement is measured (overturn proxy); rubber-stamping shows up as concordance anomaly.
3. Jobs? → capacity release, not headcount cut; judgment ladder story.
4. Who is accountable for a wrong denial? → the medical director — structurally unchanged from today.
5. Fairness proven? → No — flagged honestly: N=500 is underpowered per subgroup; powered fairness study gates the pilot.
