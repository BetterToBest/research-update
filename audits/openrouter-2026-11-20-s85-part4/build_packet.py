"""S85 part 4 (Nov 20, 2026): the packet for an outside reading (OpenRouter free tier) of the trace of the opt-in worsening and of the savings change,
before they are published. Reads research-update, compassionism-simulation (branch claude/s85-part4) and compassionism-sim-results (s85-tables-503fa48,
s85-tables2-503fa48, s85-trace-503fa48) checked out side by side. Writes packet.md and request-<tag>.json beside this file."""
import json, os, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__)); RU = os.path.join(HERE, '..', '..'); CS = os.path.join(RU, '..', 'compassionism-simulation'); RS = os.path.join(RU, '..', 'compassionism-sim-results')
rd = lambda *p: open(os.path.join(*p)).read()
TR = json.load(open(os.path.join(RS, 's85-trace-503fa48', 's85-trace-summary.json')))['results']
O = json.load(open(os.path.join(RS, 's85-tables-503fa48', 's85-summary.json')))['results']; N = json.load(open(os.path.join(RS, 's85-tables2-503fa48', 's85-summary.json')))['results']
f = lambda x: '%.2f' % x; ci = lambda s: '%s [%s, %s]' % (f(s['est']), f(s['lo']), f(s['hi']))
prereg = rd(RU, 'prereg', '2026-11-s85-output-per-hour.md').split('\n'); rep = rd(CS, 'dev', 'reports', 's85-output-per-hour.md').split('\n')
def section(lines, start, stop):
    i = [k for k, l in enumerate(lines) if l.startswith(start)][0]; j = [k for k, l in enumerate(lines) if l.startswith(stop) and k > i][0]; return '\n'.join(lines[i:j])
a3 = section(prereg, '### Amendment 3', '### Amendment 4'); a4 = '\n'.join(prereg[[k for k, l in enumerate(prereg) if l.startswith('### Amendment 4')][0]:])
q = section(prereg, '## Questions', '## What is built')
L = ['Trace of the opt-in design with lost jobs (Block A). Per environment, horizon and displacement D: worsening W (basket poverty points, positive = the rise is larger with the programme than without) [95% interval]; part carried by the adults who would take part (W_Part) and by those who would not (W_Non); severity worsening W2 and its take-part part; change in the flat contribution (points of pay, last year); change in the enrolled share in year 19 (points).']
for y in (20, 40):
    for e, en in (('ref', 'Reference'), ('adv', 'Adverse'), ('str', 'Stress')):
        for D in ('0.1', '0.3', '0.5', '0.7'):
            c = TR['%s-%d' % (e, y)]['rel']['jobs'][D]; w = c['F0']
            sh = ' share take-part %d%%' % round(w['share_Part']['est'] * 100) if 'share_Part' in w else ''
            L.append('%s %d y D %s: W %s; W_Part %s; W_Non %s;%s | W2 %s; W2_Part %s | contribution change %s; enrolled change %s | displaced adults below the basket, programme/none %s/%s' % (
                en, y, D, ci(w['W']), ci(w['W_Part']), ci(w['W_Non']), sh, ci(c['F2']['W']), ci(c['F2']['W_Part']), ci(c['tauLast']), ci(c['jnP19']), f(c['ohDBP']['est']), f(c['ohDBN']['est'])))
L.append('\nFull-coverage design, lost jobs, same quantities for contrast (W [interval]; contribution change):')
for y in (20,):
    for e, en in (('ref', 'Reference'), ('adv', 'Adverse'), ('str', 'Stress')):
        for D in ('0.1', '0.3', '0.5', '0.7'):
            c = TR['%s-%d' % (e, y)]['c22']['jobs'][D]; L.append('%s %d y D %s: W %s; contribution change %s' % (en, y, D, ci(c['F0']['W']), ci(c['tauLast'])))
LAB = {'offsets fully': 'F', 'offsets in part': 'P', 'does not offset': 'N', 'worsens': 'W'}
L.append('\nThe savings reading, old stand-in (adult-years below 30 days of basic living, bNAPy) against the preregistered measure (adult-years whose liquid savings cover under three months of need, secM3A): offset share and category per cell, 20 years, lost jobs, D 0.1-0.7.')
for e, en in (('ref', 'Reference'), ('adv', 'Adverse'), ('str', 'Stress')):
    for des, dn in (('c22', 'full coverage'), ('rel', 'opt-in')):
        row = []
        for D in ('0.1', '0.3', '0.5', '0.7'):
            a = O['%s-20' % e]['A'][des]['cells']['%s.jobs' % D]['bNAPy']; b = N['%s-20' % e]['A'][des]['cells']['%s.jobs' % D]['secM3A']
            row.append('D %s: old %.0f%% (%s) -> new %.0f%% (%s)' % (D, a['share']['est'] * 100 if a['share'] else float('nan'), LAB[a['cat']], b['share']['est'] * 100 if b['share'] else float('nan'), LAB[b['cat']]))
        L.append('%s, %s: ' % (en, dn) + '; '.join(row))
cnt = lambda S, y, des, ms: collections.Counter(LAB[S['%s-%d' % (e, y)]['A'][des]['cells'][k][m]['cat']] for e in ('ref', 'adv', 'str') for k in S['ref-%d' % y]['A'][des]['cells'] for m in ms)
M5 = ['fgt0PY', 'ppovA', 'pov', 'wtMedE', 'medWealthReal']
for y in (20, 40):
    for des, dn in (('c22', 'full coverage'), ('rel', 'opt-in')):
        L.append('Category counts over all 144 tests, %d years, %s: before %s; after %s' % (y, dn, dict(cnt(O, y, des, M5 + ['bNAPy'])), dict(cnt(N, y, des, M5 + ['secM3A']))))
tables = '\n'.join(L)
Q = """You are an independent reviewer of an economic microsimulation (the Compassionism Simulation: 500 simulated US adults over 20 or 40 years; each programme run is paired by seed with a no-programme run; seeds 1-500). Below are: the study's preregistration questions; two amendments written after the main batch (Amendment 3: the savings outcome and the analysis choices, fixed before any table was read; Amendment 4: a trace of one result, fixed before its figures were computed); the report text that is new or changed; and a condensed extract of the numbers behind it. The report's author is an AI and is also the person who made the modelling choices, so you are an independent check. In the "full coverage" design every adult is in the programme; in the "opt-in" design adults choose to join and pay a flat contribution.

Please answer these questions, concretely and with quotation:
1. The trace splits the worsening of basket poverty into the part carried by adults who would take part and the part carried by those who would not, and reads severity beside it. Is that decomposition valid and fairly described? Name any hidden assumption (for example, fixed weights, paired differences, harm-signing, or latent groups that are the same in every run) and say whether it can bias the shares.
2. Does every sentence of the new report text follow from the numbers in the extract? Quote any sentence that overstates, understates or misquotes a figure, and give the correct figure.
3. The report says the pattern fits 'a head count, not depth': more adults just below the poverty line, fewer far below. Is this the only explanation the numbers allow? Name at least two alternative explanations (for example, ceiling or floor effects, selection into the opt-in group, price effects, the baseline poverty rate being lower with the programme so there is more room to rise) and say which extra measurement would tell them apart.
4. The savings reading was changed from a stand-in to the preregistered measure after the supplement was run. Was this handled in a way that could favour the programme or hide an unfavourable result? Is the account of what moved fair (the stand-in offset 97-102% with full coverage; the preregistered measure 66-94%)?
5. 'Worsens' means the programme's cut in poverty is smaller with displacement than without it, not that the programme raises poverty. Is the report clear enough on this for a general reader? Suggest wording if not.
6. Is anything in the extract that a sceptic would flag and the report does not mention?
7. The three most important changes before publication.
Be concrete; quote the text you refer to; say where the packet does not hold what you would need.

=== The preregistration's questions ===
""" + q + """
=== Amendment 3 (savings outcome, Holm family, references, signs) ===
""" + a3 + """
=== Amendment 4 (the trace) ===
""" + a4 + """
=== The report: sections 1 and 2 (what was asked; the answer in short, as changed) ===
""" + section(rep, '## 1.', '## 3.') + """
=== The report: section 4 (displacement and the programme, as changed) ===
""" + section(rep, '## 4.', '## 5.') + """
=== The numbers behind the new text ===
""" + tables + '\n'
# nothing personal goes to an outside service: the author's name becomes a role, with neutral pronouns (CLAUDE.md, outside readings)
Q = Q.replace('Duke asked how', "The framework's author asked how").replace('His view is that', 'Their view is that').replace('That view is his and', 'That view is theirs and')
assert 'duke' not in Q.lower() and '@' not in Q, 'a personal detail is still in the packet'
open(os.path.join(HERE, 'packet.md'), 'w').write(Q)
print('packet.md: %d characters' % len(Q))
