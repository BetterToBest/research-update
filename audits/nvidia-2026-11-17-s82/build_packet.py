#!/usr/bin/env python3
"""S82 (Nov 17, 2026): the packet for an NVIDIA-hosted model's reading of the S82 preregistration before anything is built.
It holds the reviewer's instructions, the preregistration, Claude's reading of the design, and the engine spec's price and essentials sections.
Run from research-update with compassionism-simulation checked out beside it. Writes packet.json (the request body) beside this file."""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
RU = os.path.abspath(os.path.join(HERE, '..', '..'))
SIM = os.path.abspath(os.path.join(RU, '..', 'compassionism-simulation'))
MODEL = sys.argv[1] if len(sys.argv) > 1 else 'nvidia/nemotron-3-ultra-550b-a55b'
def read(p): return open(p, encoding='utf-8').read()
def spec_sections(text, heads):
    out = []
    for h in heads:
        m = re.search(r'^#+ ' + re.escape(h) + r'.*?(?=^#+ |\Z)', text, re.S | re.M)
        if m: out.append(m.group(0).strip())
    return '\n\n'.join(out)
spec = read(os.path.join(SIM, 'MODEL_SPEC.md'))
parts = [
    ('PREREGISTRATION (the file under review)', read(os.path.join(RU, 'prereg', '2026-11-s82-v6-supply-indexing.md'))),
    ("CLAUDE'S READING OF THE DESIGN (plain words, same step)", read(os.path.join(SIM, 'dev', 'reports', 's82-supply-reading.md'))),
    ('ENGINE SPEC EXCERPTS (MODEL_SPEC.md, v5.9)', spec_sections(spec, ['5. Order of events', '6.1 Wages', '6.3 Cost of living', '6.4 BU purchases', '6.12 Financing', '9. Estimands', '14.3 The capacity price rule'])),
]
instructions = """You are an independent methods reviewer with training in macroeconomics and microsimulation. You did not write any of this.
Below is a preregistration for the next version of an agent-based microsimulation of a basic-needs programme (the Compassionism Simulation), plus the modeller's plain-words reading of the programme designer's intent, plus excerpts of the engine's specification.
The study adds, behind switches, (a) a limit on the supply of housing, medical care and food, (b) partial wage indexation, and (c) a delay in indexing the benefit, and reads the effect of each along a curve of how much of the programme's payout is matched by new output ("backing").
The designer worries that a supply limit could act as an arbitrary low ceiling that understates what an efficient economy can provide; outside reviewers worried that without any limit the model's gains below full backing are free. The preregistration tries to answer both.
Please give a critical reading, in plain words, under these headings:
1. Does the supply-limit mechanism in part A answer the reviewers' concern (that below full backing nothing real is given up)? Where does it still leave real goods unlimited, and does that matter?
2. Is the mechanism an arbitrary ceiling, or a fair representation of supply? Are the headroom terms (idle capacity v, above-needs margin m, demand elasticity eta, build speed lambda) well defined, and are the named sources the right ones? Suggest better primary sources with exact table or paper names where you know them; say when you are unsure.
3. The three sharing rules. Are they sensible, is the market rule's linear incidence defensible, and is measuring basket poverty on what households received (money that cannot buy the needs does not count) a fair measure? What could go wrong (for example, artefacts in a headcount measure)?
4. Parts B and C: are the wage catch-up and the benefit delay (monthly 0.125 years, quarterly 0.25, yearly 1, two years) represented correctly in a model with one price level a year?
5. Design, checks, analysis and decision rules: anything missing, any check that would not catch a likely bug, any decision rule that could be gamed or that is unclear.
6. The five most important changes you would make before anything is built, ranked.
Be specific and cite the section of the preregistration. If something is fine, say so briefly. Do not praise; do not summarise the document back."""
body = instructions + '\n\n' + '\n\n'.join('=== ' + t + ' ===\n\n' + x for t, x in parts)
req = {'model': MODEL, 'messages': [{'role': 'user', 'content': body}], 'temperature': 0.3, 'max_tokens': 8000}
json.dump(req, open(os.path.join(HERE, 'packet.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('packet: %d characters, model %s' % (len(body), MODEL))
