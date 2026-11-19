"""S85 part 1 (Nov 19, 2026): the packet for an NVIDIA-hosted model's reading of the S85 preregistration, before any build or run.
Reads research-update and compassionism-simulation (branch claude/s85-output-reading) checked out side by side. Writes packet.json beside this file."""
import json, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); RU = os.path.join(HERE, '..', '..'); CS = os.path.join(RU, '..', 'compassionism-simulation')
MODEL = 'nvidia/nemotron-3-ultra-550b-a55b'
rd = lambda *p: open(os.path.join(*p)).read()
spec = rd(CS, 'MODEL_SPEC.md')
def sec(title):  # one ### section of MODEL_SPEC, up to the next heading of level 2 or 3
    i = spec.index(title); j = min([k for k in (spec.find('\n## ', i + 1), spec.find('\n### ', i + 1)) if k > 0]); return spec[i:j]
spec_parts = '\n'.join(sec(t) for t in ('### 6.1 Wages', '### 6.5 Project hiring', '### 6.7 Essential-service providers', '### 6.11 Labour response',
                                       '### 6.12 Financing, new money and prices', '### 12.1 Job loss and re-employment'))
body = """You are an independent reviewer of an economic microsimulation (the Compassionism Simulation: 500 simulated US adults over 20 and 40 years, a programme run against a paired no-programme run). Below are a study's preregistration, written before any code is built or run, the modeller's plain-words reading of the design it models, the sources it opened, and the model specification sections it builds on. Answer under these headings:
1. Is the economics of the new mechanism sound? In particular: output kept while paid hours fall; the dividend of automated work going to owners; the pass-through of the gain to wages; the programme's own work valued at pay over the labour share. Name anything that double counts, leaks, or contradicts the existing price rule.
2. Is reading the displacement levels (10%, 30%, 50%, 70% of paid hours, net of new work) as the preregistration does fair to the sources quoted? Is the consistency check (implied output per remaining hour against the forecasts) right?
3. Is the 'backing produced' computation (M_t) a fair test of whether the programme's own work backs its payout? What would make it biased for or against the programme?
4. Are the outcomes, the offset categories and the decision rules sound and fixed before the run? Anything that could let a result be chosen after seeing it?
5. What is missing that a sceptical labour or macro economist would expect (for example a demand shortfall, prices falling with automation, reallocation into new work, hours tied to occupation)? Say which omissions bias the result and in which direction.
6. Are the sources used correctly? Flag any figure that is misquoted or used beyond what the source supports.
7. The three most important changes you would make before the build.
Be concrete; quote the text you refer to.

=== The preregistration ===
""" + rd(RU, 'prereg', '2026-11-s85-output-per-hour.md') + """
=== The modeller's reading of the design (plain words, written before the build) ===
""" + rd(CS, 'dev', 'reports', 's85-output-reading.md') + """
=== The sources opened ===
""" + rd(CS, 'sources', 's85_output.md') + """
=== Model specification, the sections the study builds on ===
""" + spec_parts
req = {'model': MODEL, 'messages': [{'role': 'user', 'content': body}], 'temperature': 0.3, 'max_tokens': 16000, 'stream': True}
json.dump(req, open(os.path.join(HERE, 'packet.json'), 'w'))
print('packet: %d characters, model %s' % (len(body), MODEL))
