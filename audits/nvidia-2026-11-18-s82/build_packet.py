#!/usr/bin/env python3
"""S82 part 2b (Nov 18, 2026): the packet for an NVIDIA-hosted model's full reading of the S82 preregistration with its three amendments, before the dry run.
It holds the reviewer's instructions, the preregistration as it stands, and the engine code of the supply limit and of the study's reporting keys (v5.9.18).
Run from research-update with compassionism-simulation checked out beside it. Writes packet.json (the request body, streaming) beside this file."""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
RU = os.path.abspath(os.path.join(HERE, '..', '..'))
SIM = os.path.abspath(os.path.join(RU, '..', 'compassionism-simulation'))
MODEL = sys.argv[1] if len(sys.argv) > 1 else 'mistralai/mistral-large-4-1t-a52b'
def read(p): return open(p, encoding='utf-8').read()
html = read(os.path.join(SIM, 'index.html'))
a = html.index("/* S82 (Nov 17, 2026; research-update"); b = html.index("function prSec(")
code = html[a:b]
parts = [
    ('PREREGISTRATION WITH AMENDMENTS 1-3 (the file under review)', read(os.path.join(RU, 'prereg', '2026-11-s82-v6-supply-indexing.md'))),
    ('ENGINE CODE (index.html, v5.9.18): the supply limit (sl) and the study reporting keys (s82)', code),
]
instructions = """You are an independent methods reviewer with training in macroeconomics, microsimulation and research design. You did not write any of this.
Below is a preregistration for the next version of an agent-based microsimulation of a basic-needs programme (the Compassionism Simulation), with three dated amendments made before any run for results, and the engine code that implements the essentials supply limit and the study's reporting keys.
Amendment 2 fixed the supply limit's headroom values from opened sources: in medical care and food there is no idle capacity and no above-needs use, so those sectors are met only by new capacity at a building speed that is a design parameter. Amendment 3 adds a sweep of that building speed (0, 0.1, 0.25, 0.5, 1) and the strict bound on a finer grid of backed shares, writes down the reporting keys as built, and says how the assumptions screen is run in the Stress environment and with the weighted wealth tail.
Please give a critical reading, in plain words, under these headings:
1. Amendments 1-3 as a whole: does any of them change the study in a way that could be read as fitting the design to a result? Is each change justified and dated before results?
2. The sourced values in Amendment 2: are the conversions to shares of needs consumption sound? Any mistake in units, coverage or interpretation (vacancy against its long-run mean, occupancy, BEA housing services against the needs line, RAND elasticity, the Wheaton et al. building speed)?
3. The strict-bound sweep in Amendment 3: is the grid sensible, is "the slowest building speed at which a result holds" a fair summary, and is anything missing (for example a sweep of housing's values, or of the price response theta)?
4. The engine code: any bug you can see in slStep, slCut, slNew (including lam), s82Year or s82Res: wrong timing, a quantity counted twice or missed, a division that can go wrong, ranks or fifths computed wrongly, weights misapplied, or a key that does not measure what the comment says.
5. Question 7 (the screen): is holding the contribution's base at wages in the tail block, and reading the other two bases in the no-tail block, a fair answer to the stated problem?
6. Checks and decision rules: any check that would not catch a likely bug; any decision rule that is unclear or could be gamed.
7. The five most important changes you would make before the dry run, ranked.
Be specific and cite the section or the function. If something is fine, say so briefly. Do not praise; do not summarise the document back. Write your answer in full; keep your private reasoning short."""
body = instructions + '\n\n' + '\n\n'.join('=== ' + t + ' ===\n\n' + x for t, x in parts)
req = {'model': MODEL, 'messages': [{'role': 'user', 'content': body}], 'temperature': 0.3, 'max_tokens': 16000, 'stream': True}
json.dump(req, open(os.path.join(HERE, 'packet.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('packet: %d characters, model %s' % (len(body), MODEL))
