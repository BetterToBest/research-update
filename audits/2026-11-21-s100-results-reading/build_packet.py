"""S100 part 2 (Nov 21, 2026): the packet for two outside readings (OpenRouter free tier) of the yardstick study's results, before publication.
Reads research-update, compassionism-simulation (branch claude/s100-yardstick-report) and compassionism-sim-results (s100-tables-e50a3b3) side by side.
Writes packet-<reader>.json beside this file. Everything sent is public in the repositories."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__)); RU = os.path.join(HERE, '..', '..'); CS = os.path.join(RU, '..', 'compassionism-simulation')
RS = os.path.join(RU, '..', 'compassionism-sim-results', 's100-tables-e50a3b3')
rd = lambda *p: open(os.path.join(*p)).read()
READERS = {'nemotron': ('nvidia/nemotron-3-ultra-550b-a55b:free', 40000), 'gemma': ('google/gemma-4-31b-it:free', 30000)}
body = """You are an independent reviewer of an economic microsimulation (the Compassionism Simulation: 500 simulated US adults over 20 and 40 years; each programme run is paired by seed with a no-programme run, seeds 1-500). Every effect it reports is a programme run minus a no-programme run (the yardstick). The study below tested two additions to the yardstick: pay by household type from the Current Population Survey (so that low pay falls where it does in the US, which is how the model represents part-time work), and the child and dependent care credit. Below are the study's preregistration (written before the run), the full tables (produced by a tool written before any result was read) and the report. Please answer:
1. Does every statement in the report follow from the tables? Quote any sentence that overstates, understates or misquotes a figure, and give the correct figure from the tables.
2. Does the report follow the preregistration's decision rules: rule 2 (the yardstick reading, judged on EITC reach only, not on any programme effect); rule 4 (every change whose Holm-adjusted interval excludes zero stated in whichever direction, the rest as no measurable change, the bounds printed beside the main reading); rule 5 (the care credit's mean reported as a gap)?
3. Three choices were made after the batch finished and are stated in the report: the overall earnings distribution (asked in Question 1) is read as a calculation from the engine's four distributions, since the run did not output it; the care credit's reach is compared at take-up as measured; and 12 interaction intervals that exclude zero are called "no synergy that matters" because none exceeds 0.005 points. Could any of them favour a reading or the programme, or let a result be chosen after seeing it?
4. Is pay by household type a sound way to bring part-time work into the yardstick, as a sceptical labour economist would judge it? What does it miss that matters for the programme's effects?
5. The report's "why" paragraph in section 5 is labelled an interpretation. Is it fair, and does the report claim more than it measured anywhere else?
6. Is the findings-page text (section 9) a fair summary for a general reader? Suggest a corrected version if not.
7. The three most important changes before publication.
Be concrete; quote the text you refer to.

=== The preregistration ===
""" + rd(RU, 'prereg', '2026-11-s100-part-time-dcc.md') + """
=== The tables (s100-tables.md) ===
""" + rd(RS, 's100-tables.md') + """
=== The report ===
""" + rd(CS, 'dev', 'reports', 's100-part-time-dcc.md')
for name, (model, mt) in READERS.items():
    req = {'model': model, 'messages': [{'role': 'user', 'content': body}], 'temperature': 0.3, 'max_tokens': mt}
    json.dump(req, open(os.path.join(HERE, 'packet-%s.json' % name), 'w'))
open(os.path.join(HERE, 'packet.txt'), 'w').write(body)
print('packet: %d characters' % len(body))
