import sys, pathlib
S=pathlib.Path('/home/user/compassionism-simulation'); R=pathlib.Path('/home/user/research-update')
def lines(p,a=None,b=None):
    t=p.read_text().split('\n'); return '\n'.join(t[(a-1 if a else 0):(b if b else None)])
prompt=(R/'audits/2026-11-17-release-audit-prompt.md').read_text()
body=prompt[prompt.index('\n---\n')+5:]
body=body.replace('Your role: [REPLACE THIS LINE, see the note above the line]',
 'Your role: an independent public economist with experience of large cash-transfer programmes and cooperative provision. Answer every part evenly.')
body=body.replace('**Please open the files.** For every finding, name the file and section you read. If you could not open a file, say so and do not guess its contents. At end, list every file you actually opened.','')
body=body.replace('**Please open the files.**','**You cannot browse: the files you need are pasted below, after the questions, each under a FILE heading.** Where the prompt names a file that is not pasted, say you could not read it and do not guess its contents.')
files=[
 ('compassionism-simulation/dev/reports/s64-round2-overview.md', lines(S/'dev/reports/s64-round2-overview.md')),
 ('compassionism-simulation/dev/reports/s64-findings-page-text.md', lines(S/'dev/reports/s64-findings-page-text.md')),
]+[(f'compassionism-simulation/dev/reports/s64-round2-{q}.md', lines(S/f'dev/reports/s64-round2-{q}.md')) for q in ['q1-main-effects','q2-robustness','q3-interactions','q4-backing','q5-financed','q6-distribution','q7-work']]+[
 ('compassionism-simulation/MODEL_SPEC.md, section 6.12 (lines 158-160)', lines(S/'MODEL_SPEC.md',158,160)),
 ('compassionism-simulation/MODEL_SPEC.md, section 14 (lines 325-427)', lines(S/'MODEL_SPEC.md',325,427)),
 ('compassionism-simulation/dev/reports/s68-round2-spec-tests.md', lines(S/'dev/reports/s68-round2-spec-tests.md')),
 ('compassionism-simulation/dev/reports/s69-independent-implementation/REPORT.md', lines(S/'dev/reports/s69-independent-implementation/REPORT.md')),
 ('compassionism-simulation/dev/packets/s69-brief.md', lines(S/'dev/packets/s69-brief.md')),
 ('compassionism-simulation/dev/reports/s70-screen.md, sections "In short" to "The decision rules" (lines 1-65)', lines(S/'dev/reports/s70-screen.md',1,65)),
 ('compassionism-simulation/dev/reports/s81-suite-weighted.md', lines(S/'dev/reports/s81-suite-weighted.md')),
 ('compassionism-simulation/ECONOMIST-REVIEW.md', lines(S/'ECONOMIST-REVIEW.md')),
 ('research-update/prereg/2026-11-s63-round2-freeze.md, lines 1-122 (before the amendments)', lines(R/'prereg/2026-11-s63-round2-freeze.md',1,122)),
 ('research-update/audits/2026-11-09-simulation-audit.md', lines(R/'audits/2026-11-09-simulation-audit.md')),
 ('research-update/audits/2026-11-13-simulation-audit.md, summary and status of the Nov 9 findings (lines 13-27, 127-139)', lines(R/'audits/2026-11-13-simulation-audit.md',13,27)+'\n...\n'+lines(R/'audits/2026-11-13-simulation-audit.md',127,139)),
 ('research-update/audits/2026-11-14-d23-backing-and-main-row.md', lines(R/'audits/2026-11-14-d23-backing-and-main-row.md')),
]
out=body+'\n\n# The files\n'+''.join(f'\n\n===== FILE: {n} =====\n\n{t}' for n,t in files)
p=pathlib.Path(sys.argv[1]); p.write_text(out); print(len(out), 'chars;', len(files),'files')
