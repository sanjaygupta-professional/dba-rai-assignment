# Product

## Register

product

## Users

Utilization-management professionals at a US health payer, three personas in one app:
- UM nurse (Maya): works a queue of prior-auth cases, verifies AI-prepared evidence packets, approves/pends/routes. Long shifts, repetitive verification work; speed and one-click evidence checking matter most.
- Medical director: reviews routed/conflict cases, the only role that can deny. Needs clinical judgment context fast.
- Operations executive: glances at live queue/decision/flow metrics.
Secondary audience right now: a doctoral review panel evaluating this as a working prototype on a laptop.

## Product Purpose

CareBridge prepares prior-authorization decisions: rules gate the queue, an LLM pipeline maps case evidence to pinned policy criteria with verbatim citations, humans make every decision. The AI can never deny care. The prototype proves one hypothesis: an evidence packet with built-in explanations makes review faster and trustable. Success = a reviewer can verify any AI claim in one click.

## Brand Personality

Precise, calm, trustworthy. A clinical operations console that reads as serious production software — Linear/Raycast lineage: crisp type, tight spacing, restrained color where status is the only thing that glows. Dark ops-console theme: deep warm charcoal surfaces, high-contrast case data.

## Anti-references

- Student-assignment aesthetic: no course names, group numbers, cohort labels, assignment dates anywhere in the UI.
- Generic healthcare SaaS: white + teal, rounded friendly blobs, stock-photo warmth.
- AI-slop dashboard: purple gradients, glassmorphism, gradient orbs, hero-metric cards, identical icon-card grids.
- Bloomberg-terminal coldness: dense is good, hostile is not.

## Design Principles

1. The packet is the explanation — evidence, citations, and policy versions are first-class UI, never buried in modals.
2. Status is the only spectacle — color signals case state (met/uncertain/conflict, approve/pend/route); everything else stays quiet.
3. Human authority is visible — approve/pend/route affordances read as deliberate human acts; denial paths visibly belong to the medical director.
4. Dense but legible — one screen per persona, no scrolling theatrics, numbers align, type hierarchy does the work.
5. Production-grade restraint — if it would look at home in Linear, it ships; if it looks like a demo, it does not.

## Accessibility & Inclusion

WCAG AA contrast on dark surfaces (4.5:1 body text). Status never encoded by color alone — always paired with a label or glyph. Respect prefers-reduced-motion. Keyboard focus visible.
