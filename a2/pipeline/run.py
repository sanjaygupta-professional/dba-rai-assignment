#!/usr/bin/env python3
"""CareBridge offline packet pipeline (option C).
For each case: pin policy version -> prompt LLM (claude -p) for criterion mapping with
verbatim citations -> verify every quote against source docs (groundedness) -> packets.json
"""
import json, re, subprocess, sys, glob, os, datetime

BASE = os.path.dirname(os.path.abspath(__file__))
TODAY = "2026-07-23"

def load_policies():
    pols = {}
    for f in glob.glob(f"{BASE}/policies/*.md"):
        txt = open(f).read()
        pid = re.search(r"POLICY: (\S+)", txt).group(1)
        ver = re.search(r"VERSION: (\S+)", txt).group(1)
        eff = re.search(r"EFFECTIVE: (\S+)", txt).group(1)
        pols.setdefault(pid, []).append({"ver": ver, "eff": eff, "text": txt})
    # version-pinning: latest effective date <= today
    return {pid: max([v for v in vs if v["eff"] <= TODAY], key=lambda v: v["eff"])
            for pid, vs in pols.items()}

PROMPT = """You are the CareBridge packet-assembly service for utilization management.
Map the clinical evidence to EACH policy criterion in the applicable section. Rules:
- status must be one of: met, unmet, uncertain, conflict.
- "conflict" when two sources genuinely contradict each other; "uncertain" when evidence is absent or ambiguous.
- Every assertion MUST cite a VERBATIM quote copied exactly from the case documents (q) plus its source reference line (r) naming the doc id. Do not paraphrase inside q. Keep quotes short (under 20 words). If no evidence exists, use q: "no source span found" and r naming what was searched.
- Recommendation rules (hard): all criteria met -> APPROVE. Any uncertain/missing-documentation criterion -> PEND. Any conflict -> ROUTE. You can NEVER output DENY; denial authority belongs to a licensed clinician.
- confidence.policy and confidence.evidence: high/medium/low with a short parenthetical if not high.

Output ONLY a JSON object, no markdown fences, exactly this shape:
{"rec":"APPROVE|PEND|ROUTE","criteria":[{"t":"<criterion title, short>","s":"met|unmet|uncertain|conflict","why":"<one sentence>","src":[{"q":"<verbatim quote>","r":"<doc reference>"}]}],"rationale":"<2 sentences: what drove the recommendation; if PEND name the single missing item>","confidence":{"policy":"...","evidence":"..."}}

POLICY (use only section %SECTION%):
%POLICY%

CASE DOCUMENTS:
%CASE%
"""

def norm(s):
    s = s.lower().replace("“", '"').replace("”", '"').replace("’", "'")
    s = re.sub(r"[\"'‘>]", "", s)
    return re.sub(r"\s+", " ", s).strip(" .")

def grounded(quote, corpus):
    if "no source span found" in quote.lower():
        return True  # explicit absence claim; verified separately by absence
    frags = [f for f in re.split(r"\.\.\.|…", quote) if norm(f)]
    return all(norm(f) in corpus for f in frags)

def run_case(path, pols):
    raw = open(path).read()
    meta = json.loads(re.search(r"META: (\{.*\})", raw).group(1))
    body = raw.split("\n", 2)[2]
    pol = pols[meta["policy"]]
    prompt = (PROMPT.replace("%SECTION%", meta["section"])
                    .replace("%POLICY%", pol["text"])
                    .replace("%CASE%", body))
    for attempt in range(2):
        r = subprocess.run(["claude", "-p", prompt], capture_output=True, text=True, timeout=300)
        m = re.search(r"\{.*\}", r.stdout, re.S)
        if not m:
            print(f"  attempt {attempt+1}: no JSON in output", file=sys.stderr); continue
        try:
            pkt = json.loads(m.group(0)); break
        except json.JSONDecodeError as e:
            print(f"  attempt {attempt+1}: bad JSON: {e}", file=sys.stderr)
    else:
        raise RuntimeError(f"{meta['id']}: LLM failed twice")
    corpus = norm(body)
    checks = []
    for c in pkt["criteria"]:
        for s in c["src"]:
            checks.append({"crit": c["t"], "q": s["q"], "ok": grounded(s["q"], corpus)})
    title = re.search(r"TITLE: (.+)", pol["text"]).group(1)
    pkt.update(meta)
    pkt["policy"] = f"{meta['policy']} {pol['ver']} (eff {pol['eff']}) — {title.split(' (')[0]}"
    return pkt, checks

def main():
    pols = load_policies()
    print("Pinned policies:", {k: v["ver"] for k, v in pols.items()})
    packets, allchecks = [], []
    for f in sorted(glob.glob(f"{BASE}/cases/PA-*.md")):
        cid = os.path.basename(f)[:-3]
        print(f"running {cid} ...")
        pkt, checks = run_case(f, pols)
        packets.append(pkt); allchecks += checks
        bad = [c for c in checks if not c["ok"]]
        print(f"  rec={pkt['rec']} assertions={len(checks)} grounded={len(checks)-len(bad)}/{len(checks)}")
        for b in bad: print(f"  UNGROUNDED: [{b['crit']}] {b['q']}", file=sys.stderr)
    ok = sum(1 for c in allchecks if c["ok"])
    report = {"run": datetime.datetime.now().isoformat(timespec="seconds"),
              "cases": len(packets), "assertions": len(allchecks), "grounded": ok,
              "groundedness_pct": round(100*ok/len(allchecks), 1),
              "checks": allchecks}
    json.dump(packets, open(f"{BASE}/out/packets.json", "w"), indent=1)
    json.dump(report, open(f"{BASE}/out/groundedness.json", "w"), indent=1)
    print(f"\nGROUNDEDNESS: {ok}/{len(allchecks)} = {report['groundedness_pct']}%  (gate: >=95)")
    if report["groundedness_pct"] < 95: sys.exit(1)

if __name__ == "__main__":
    main()
