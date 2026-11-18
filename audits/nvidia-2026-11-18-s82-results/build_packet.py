#!/usr/bin/env python3
"""S82 part 3b (Nov 18, 2026): the packet for an NVIDIA-hosted model's reading of the S82 results, the plain-words report and the findings-page text.
It holds the reviewer's instructions; the preregistration's questions, outcomes, analysis, decision rules and Amendments 5-6; the checks; the tables of
questions 1 and 2 at 20 years; the report; and the findings page's new section as rendered. Run from research-update with compassionism-simulation
checked out beside it (branch claude/s82-part3b-report). Writes packet.json (the request body, streaming) beside this file."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
RU = os.path.join(HERE, '..', '..')
CS = os.path.join(RU, '..', 'compassionism-simulation')
MODEL = 'nvidia/nemotron-3-ultra-550b-a55b'


def read(p): return open(p, encoding='utf-8').read()


def lines(p, a, b): return ''.join(open(p, encoding='utf-8').readlines()[a - 1:b])


PR = os.path.join(RU, 'prereg', '2026-11-s82-v6-supply-indexing.md')
parts = [
    ('The preregistration: questions (lines 22-33)', lines(PR, 22, 33)),
    ('The preregistration: design, outcomes, analysis, checks, decision rules, reporting, limits (lines 82-160)', lines(PR, 82, 160)),
    ('The preregistration: Amendments 5 and 6 (from line 327)', lines(PR, 327, 400)),
    ('The checks, as run', read(os.path.join(CS, 'dev', 'runs', 's82-batch', 's82-checks.md'))),
    ('Question 1 tables, 20 years', read(os.path.join(CS, 'dev', 'runs', 's82-batch', 's82-q1-supply.md'))[:60000]),
    ('Question 2 tables, 20 years', read(os.path.join(CS, 'dev', 'runs', 's82-batch', 's82-q2-wages.md'))[:40000]),
    ('The plain-words report (dev/reports/s82-supply-indexing.md)', read(os.path.join(CS, 'dev', 'reports', 's82-supply-indexing.md'))),
    ('The findings page: the new section and the replaced note, as rendered (text only)', read(os.path.join(HERE, 'findings-section.txt'))),
]
instructions = """You are an independent methods reviewer with training in macroeconomics, microsimulation and research design. You did not write any of this.

Below are a preregistered simulation study's decision rules, its checks, two of its result tables, the plain-words report written from them, and the text
written for the public findings page. Read them as a sceptical referee would, before publication. Answer under these headings, in plain words, at most
2,500 words in all:

1. Claims that do not follow. Any sentence in the report or the findings-page text that the tables or the decision rules do not support, or that
   overstates them. Quote the sentence and the cell it should rest on.
2. Unfavourable results left out or played down. Anything in the tables that the report or the page should say and does not, or says too softly.
3. The supply limit. The report says the limit as built moves only basket poverty, because the money a cut leaves unspent goes to other goods and the
   cut moves no price. Is that limit stated clearly and prominently enough? Does it undermine the statement that the results "hold under a supply limit"?
4. The wage readings. Is the report's reading of the partial wage indexation results (worse than no programme at no backing when half is never made up)
   correct and fairly framed? Anything implausible in those numbers that suggests a defect rather than a result?
5. The ageing reading withheld (Amendment 6). Is withholding it the right call under the preregistration? Is the reason sound?
6. Arithmetic. Any figure in the report that differs from the tables given.
7. Anything else a referee would ask before this is published.

Say where you are unsure. Do not invent figures that are not in the material."""
body = instructions + '\n\n' + '\n\n'.join('=== ' + t + ' ===\n\n' + x for t, x in parts)
req = {'model': MODEL, 'messages': [{'role': 'user', 'content': body}], 'temperature': 0.3, 'max_tokens': 24000, 'stream': True}
json.dump(req, open(os.path.join(HERE, 'packet.json'), 'w'), ensure_ascii=False)
print('packet: %d characters, model %s' % (len(body), MODEL))
