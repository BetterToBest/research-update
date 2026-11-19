"""S90 (Nov 18, 2026): the packet for an NVIDIA-hosted model's reading of the S90 finding, fix and preregistration.
Reads research-update and compassionism-simulation (branch claude/s90-private-price-at-sale) checked out side by side. Writes packet.json beside this file."""
import json, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); RU = os.path.join(HERE, '..', '..'); CS = os.path.join(RU, '..', 'compassionism-simulation')
MODEL = 'nvidia/nemotron-3-ultra-550b-a55b'
rd = lambda *p: open(os.path.join(*p)).read()
dec = rd(CS, 'dev', 'DECISIONS.md'); dec = dec[dec.index('## S90 (Nov 18, 2026)'):]
diff = subprocess.run(['git', '-C', CS, 'diff', 'origin/main...HEAD', '--', 'index.html'], capture_output=True, text=True).stdout
esp = rd(CS, 'dev', 'reports', 'v5-1-private-esp-correction.md')
body = """You are an independent reviewer of an economic microsimulation (the Compassionism Simulation). Read the material below and answer under these headings:
1. Is the diagnosis right? Does the evidence show that the private businesses' lagged price, and not something else, causes the two-year swing?
2. Is calling it a defect (not a reading of the design) justified by the design text quoted?
3. Is the fix correct? Check the algebra of the at-sale price (vK, the per-adult cut with a budget limit, the advance and its repayment, the share of BU attributed to private businesses), and the code diff. Name any case where it double-counts, loses money, or departs from the design.
4. Is anything the fix changes not covered by the preregistration's outcomes or checks?
5. Are the preregistration's decision rules sound and fixed before the run? Anything that could let a result be chosen after seeing it?
6. Is the plain-words report accurate and fair to the evidence (no overclaiming)?
7. The three most important changes you would make.
Be concrete; quote the text you refer to.

=== The plain-words report ===
""" + rd(CS, 'dev', 'reports', 's90-private-price-at-sale.md') + """
=== The decision record ===
""" + dec + """
=== The earlier design note that the fix relies on (Oct 2, 2026) ===
""" + esp + """
=== The preregistration of the rerun ===
""" + rd(RU, 'prereg', '2026-11-s90-private-price-at-sale.md') + """
=== The engine diff (index.html) ===
""" + diff
req = {'model': MODEL, 'messages': [{'role': 'user', 'content': body}], 'temperature': 0.3, 'max_tokens': 16000, 'stream': True}
json.dump(req, open(os.path.join(HERE, 'packet.json'), 'w'))
print('packet: %d characters, model %s' % (len(body), MODEL))
