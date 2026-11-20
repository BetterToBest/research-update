"""S85 part 3 (Nov 20, 2026): the packet for an NVIDIA-hosted model's reading of the output-per-hour results, before they are published as findings.
Reads research-update, compassionism-simulation (branch claude/s85-tables) and compassionism-sim-results (s85-tables-503fa48) checked out side by side.
Writes packet.json beside this file."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__)); RU = os.path.join(HERE, '..', '..'); CS = os.path.join(RU, '..', 'compassionism-simulation')
RS = os.path.join(RU, '..', 'compassionism-sim-results', 's85-tables-503fa48')
MODEL = 'nvidia/nemotron-3-ultra-550b-a55b'
rd = lambda *p: open(os.path.join(*p)).read()
S = json.load(open(os.path.join(RS, 's85-summary.json')))['results']
PK = ['fgt0PY', 'ppovA', 'pov', 'wtMedE', 'medWealthReal', 'bNAPy']
f = lambda x, d=2: ('%.' + str(d) + 'f') % x
L = ['Block A (headline cells), 20 years. Per cell and reading: cost with no programme / cost with the programme / offset [95% interval] / offset share / category after Holm (48 tests).']
for e in ['ref', 'adv', 'str']:
    for des in ['c22', 'rel']:
        L.append('== %s, %s design' % ({'ref': 'Reference', 'adv': 'Adverse', 'str': 'Stress'}[e], {'c22': 'full coverage', 'rel': 'opt-in'}[des]))
        for cell, v in S['%s-20' % e]['A'][des]['cells'].items():
            parts = []
            for k in PK:
                c = v[k]; d = 0 if k in ('wtMedE', 'medWealthReal') else 2
                parts.append('%s: %s / %s / %s [%s, %s] / %s / %s' % (k, f(c['cN']['est'], d), f(c['cP']['est'], d), f(c['off']['est'], d), f(c['off']['lo'], d), f(c['off']['hi'], d),
                                                                    f(c['share']['est']) if c['share'] else 'none given', c['cat']))
            L.append('  D %s %s | ' % tuple(cell.rsplit('.', 1)) + ' | '.join(parts))
        E = S['%s-20' % e]['A'][des]['eff']
        L.append('  programme effects (programme minus no programme): ' + '; '.join('%s: basket poverty %s, wealth poverty %s, median wealth %s, inflation %s' % (
            n.split('.', 2)[2], f(E[n]['fgt0PY']['est']), f(E[n]['ppovA']['est']), f(E[n]['wtMedE']['est'], 0), f(E[n]['endoAnn']['est'] * 100, 3)) for n in E))
L.append('\nBlock E (the backing produced), 20 years: per row, programme inflation (points a year) [interval], category, produced share % over the run.')
for e in ['ref', 'adv', 'str']:
    for des in ['c22', 'rel']:
        Q = S['%s-20' % e]['Q4'][des]
        L.append('== %s %s: ' % (e, des) + '; '.join('%s %s [%s, %s] %s %s' % (n.split('.', 2)[2], f(r['infl']['est'], 1), f(r['infl']['lo'], 1), f(r['infl']['hi'], 1), r['cat'], f(r['A']['est'], 1)) for n, r in sorted(Q['rows'].items())))
        L.append('   break-even m: ' + '; '.join('%s %s' % (k, b['est']) for k, b in Q['be'].items()))
tables = '\n'.join(L)
body = """You are an independent reviewer of an economic microsimulation (the Compassionism Simulation: 500 simulated US adults over 20 and 40 years; each programme run is paired by seed with a no-programme run, seeds 1-500). Below are a study's preregistration (with three amendments; the third was written after the batch finished but before any table was read), the checks file, a condensed extract of the results tables, and the modeller's plain-words report, which is about to be published with a short text for the project's findings page. Read the report against the tables and the preregistration, and answer:
1. Does every statement in the report follow from the tables? Quote any sentence that overstates, understates or misquotes a figure, and give the correct figure.
2. Does the report follow the preregistration's decision rules: rule 2's categories; rule 3 (no category for the advocate's words; every 'does not offset' or 'worsens' cell named in the same section as any favourable statement); rule 4 (the stress readings labelled); rule 5 (any headline at full backing carries the produced share and its inflation in the same paragraph); rule 6 (free time always split secure and insecure); rule 7 (interactions)? Name each place it does not.
3. Amendment 3 fixed several choices after the batch finished (the savings outcome's substitute and a supplementary run; Holm over 48 tests; the D 0 references; the signs; check 7 as an inspection). Could any of them favour the programme or let a result be chosen after seeing it?
4. The opt-in design 'worsens' displacement's cost to basket poverty in many lost-jobs cells while still cutting poverty overall. Is the report's description of this fair? What mechanisms in such a model could cause it, and what should be inspected?
5. The backing produced: is the report's conclusion (the programme's own work matches 5-18% of the payout; inflation 18-82 points a year; no break-even share of work on the grid) stated fairly, neither too strongly nor too weakly? Is anything missing a sceptical macroeconomist would raise?
6. Is the findings-page text (section 14) a fair summary for a general reader? Suggest a corrected version if not.
7. The three most important changes before publication.
Be concrete; quote the text you refer to.

=== The preregistration (with Amendments 1-3) ===
""" + rd(RU, 'prereg', '2026-11-s85-output-per-hour.md') + """
=== The checks file ===
""" + rd(RS, 's85-checks.md')[:6000] + """
=== Condensed results tables (from s85-summary.json) ===
""" + tables + """
=== The report ===
""" + rd(CS, 'dev', 'reports', 's85-output-per-hour.md')
req = {'model': MODEL, 'messages': [{'role': 'user', 'content': body}], 'temperature': 0.3, 'max_tokens': 40000, 'stream': True}
json.dump(req, open(os.path.join(HERE, 'packet.json'), 'w'))
print('packet: %d characters, model %s' % (len(body), MODEL))
