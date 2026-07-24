# Offline packet pipeline (option C — precomputed-real)

Runs BEFORE demo day. Generates genuine AI packets; demo site stays static.

## Flow
1. `cases/` — 5 synthetic PA cases (Synthea-style clinical notes + rx claims + labs), 2 service lines.
2. `policies/` — public criteria proxies (CMS NCD/LCD style, version-pinned).
3. `run.md` — for each case: retrieval over policy corpus → LLM criterion-mapping with span
   citations → met/unmet/uncertain/conflict status → groundedness check per assertion.
4. Output: packet JSON in the exact schema embedded in `../prototype/index.html` (`CASES` array).
   Replace the seeded array with pipeline output; UI unchanged.

## Honesty rule
Until this pipeline runs, prototype packets are seeded samples IN THE SAME SCHEMA (footer says so).
After it runs, the deck claim "nothing on screen is hand-written" becomes true — do not present
that claim before the swap.

Target: run Mon–Tue 27–28 Jul.
