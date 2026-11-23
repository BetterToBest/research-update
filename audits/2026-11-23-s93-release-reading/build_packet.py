"""S93 part 4 (Nov 23, 2026): the packet for two outside readings (checklist item F9) of the release figures and the release text, before the merge that publishes them.
Reads research-update, compassionism-simulation (branch claude/s93-pages) and compassionism-sim-results side by side. page-text.md is the rendered text of the findings page's
v5.9 and central-bank sections on that branch (jsdom; every number as the page prints it). Writes packet-<reader>.json and packet.txt beside this file. Everything sent is public."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__)); RU = os.path.join(HERE, '..', '..'); CS = os.path.join(RU, '..', 'compassionism-simulation'); RS = os.path.join(RU, '..', 'compassionism-sim-results')
rd = lambda *p: open(os.path.join(*p)).read()
lines = lambda f, a, b: ''.join(open(f).readlines()[a - 1:b])
PR = os.path.join(RU, 'prereg', '2026-11-s90-private-price-at-sale.md'); PC = os.path.join(RS, 's93-page-check-50bc51d', 's93-page-check.md')
READERS = {'nemotron': ('nvidia/nemotron-3-ultra-550b-a55b:free', 40000), 'gemma-nvidia': ('google/gemma-4-31b-it', 30000)}
body = """You are an independent reviewer of an economic microsimulation (the Compassionism Simulation: 500 simulated US adults over 20 and 40 years; each programme run is paired by seed with a no-programme run, seeds 1-500; three environments: Reference, Adverse, Stress). Every effect is a programme run minus its no-programme run. A new release changes the main row in three ways (a business price rule now applied in the year of the sale; pay by household type; the child and dependent care credit) and every study on the findings page was rerun on the new engine. Below are: the preregistered release checklist and release-text rules; the release report; the change in the main rows split into its two steps (tables); a summary of the comparison of every figure the page prints, published against release; a decomposition run of the reading that changed most; and the rendered text of the findings page's two release sections. Please answer:
1. Does every statement in the release report and in the page's release note ("This release (v5.9.23 ...)") follow from the tables? Quote any sentence that overstates, understates or misquotes a figure, and give the correct figure.
2. Does the release text do what the preregistration's section G and Amendment 3's G require? What is missing?
3. The supply study's wage reading changed sign at 20 years. Is the decomposition's conclusion (the change comes from the price at the sale) supported by the table given? What else would you check before publishing that sentence?
4. Below full backing, the preregistered swing measure failed and a measure chosen after the failure is used. Is that handled and labelled fairly in the report?
5. In the page text: any figure that contradicts another on the page, any section that mixes engines or versions, any qualifier missing (full backing, intervals, the opt-in design beside the full-coverage design)?
6. Anything in the report or the page that claims more than the runs measured, or reads as advocacy rather than a report of the figures?
7. The three most important changes before publication.
Be concrete; quote the text you refer to.

=== The preregistration: Amendment 2, sections F and G, and Amendment 3, sections F and G ===
""" + lines(PR, 107, 128) + '\n' + lines(PR, 151, 158) + """
=== The release report (dev/reports/s93-release.md) ===
""" + rd(CS, 'dev', 'reports', 's93-release.md') + """
=== The main rows, published against release, the change split into two steps (s93-release-tables-50bc51d/s93-release-tables.md) ===
""" + rd(RS, 's93-release-tables-50bc51d', 's93-release-tables.md') + """
=== Every printed figure, published against release: sections 1-4 of the page check (s93-page-check-50bc51d/s93-page-check.md) ===
""" + lines(PC, 1, 283) + """
=== The decomposition of the wage reading (s93-wage-dec-50bc51d: run.txt and table.md) ===
""" + rd(RS, 's93-wage-dec-50bc51d', 'run.txt') + '\n' + rd(RS, 's93-wage-dec-50bc51d', 'table.md') + """
=== The rendered page text ===
""" + rd(HERE, 'page-text.md')
for name, (model, mt) in READERS.items():
    req = {'model': model, 'messages': [{'role': 'user', 'content': body}], 'temperature': 0.3, 'max_tokens': mt}
    if 'nvidia' in name: req['stream'] = True
    json.dump(req, open(os.path.join(HERE, 'packet-%s.json' % name), 'w'))
open(os.path.join(HERE, 'packet.txt'), 'w').write(body)
print('packet: %d characters' % len(body))
