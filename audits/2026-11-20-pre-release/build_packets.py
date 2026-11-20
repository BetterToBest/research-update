"""S94 (Nov 20, 2026): two packets for outside readers, from public files only. The author's name is replaced by a role.
Reads research-update and compassionism-simulation (branch claude/s94-collectives-lending) side by side. Writes packet-prereg.md and packet-gaps.md."""
import os, re
HERE = os.path.dirname(os.path.abspath(__file__)); RU = os.path.join(HERE, '..', '..'); CS = os.path.join(RU, '..', 'compassionism-simulation')
rd = lambda *p: open(os.path.join(*p)).read()
role = lambda t: re.sub(r"\bDuke Johnson\b|\bDuke\b", 'the author', t)
def section(text, start, stop=None):
    i = text.index(start); j = text.index(stop, i + len(start)) if stop else len(text); return text[i:j]
S93 = section(rd(RU, 'PLAN.md'), '### S93 ·', '### S91 ·')
P1 = """You are an independent reviewer of a preregistration for an agent-based economic simulation (the Compassionism Simulation: a guaranteed-income
programme paid in an expiring currency, with community-owned not-for-profit essential businesses, PTFs). You are a different maker's model from the
one that wrote it. Read the design reading, the sources script and the preregistration below, then answer, numbered:
1. Choices that favour the programme without a source, or that are not the cautious reading where the text is silent. Say which reading would be cautious.
2. Values: is each constant correctly derived from the cited source as described (check the arithmetic shown)? Anything mis-sourced or misapplied?
3. Mechanism: anything incoherent in the fund, the pace limit, the failures, the repayment convention, or the charters (accounting, double counting, a share that cannot fall, effects in the no-programme run)?
4. Checks and decision rules: what is missing to catch a defect, or to stop a favourable reading being over-claimed?
5. Missing rows or readings you would add before any run, and rows you would drop.
6. Anything in the author's request (quoted) the design misreads.
Be concrete and short; cite the section you mean. Do not praise. Plain text.

"""
P1 += '=== Claude\'s reading of the design (dev/reports/s94-collectives-lending-reading.md) ===\n' + rd(CS, 'dev', 'reports', 's94-collectives-lending-reading.md')
P1 += '\n=== The sources script and its output (sources/s94_lending.py) ===\n' + rd(CS, 'sources', 's94_lending.py')
P1 += '\n--- output ---\n' + os.popen('python3 -I ' + os.path.join(CS, 'sources', 's94_lending.py')).read()
P1 += '\n=== The preregistration (prereg/2026-11-s94-collectives-lending.md) ===\n' + rd(RU, 'prereg', '2026-11-s94-collectives-lending.md')
open(os.path.join(HERE, 'packet-prereg.md'), 'w').write(role(P1))
P2 = """You are an independent reviewer of an agent-based economic simulation (the Compassionism Simulation) and its findings page, before its next
release. The release makes a corrected price rule the default and regenerates the main figures. The author wants every gap and limitation that
can be addressed fixed before that release. Below: the release step, the current findings-page text, the limits sections of the two latest
studies, and the team's own inventory of open gaps. Answer, numbered:
1. Rank the inventory's items by how much each could change a headline claim or mislead a reader. For each of your top ten, say whether to fix it in the model, fix it in the text, or state it as a limit, and how to verify the fix.
2. Gaps NOT in the inventory that you see in the findings text or the limits (claims without a stated basis, figures resting on design parameters presented as results, missing unfavourable results, comparisons that are not like for like).
3. What the release step itself is missing (checks before publishing, which studies must be rerun on the release engine, what the text must say).
4. Which items are acceptable as stated limits for this release, and why.
Be concrete and short. Do not praise. Plain text.

"""
P2 += '=== The release step (PLAN.md) ===\n' + S93
P2 += '\n=== The findings-page text (dev/reports/s64-findings-page-text.md) ===\n' + rd(CS, 'dev', 'reports', 's64-findings-page-text.md')
P2 += '\n=== The automation study: what it means, and its limits (dev/reports/s85-output-per-hour.md, section 13) ===\n' + section(rd(CS, 'dev', 'reports', 's85-output-per-hour.md'), '## 13.')
P2 += '\n=== The supply study: what it means, and its limits (dev/reports/s82-supply-indexing.md, section 11) ===\n' + section(rd(CS, 'dev', 'reports', 's82-supply-indexing.md'), '## 11.', '## 12.')
P2 += '\n=== The team\'s inventory of open gaps (audits/2026-11-20-release-gaps.md) ===\n' + rd(RU, 'audits', '2026-11-20-release-gaps.md')
open(os.path.join(HERE, 'packet-gaps.md'), 'w').write(role(P2))
print(len(P1), len(P2))
