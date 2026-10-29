# refine.ink audits: triage

Two AI-generated reviews from refine.ink, kept in the claude.ai Project "Better To Best Research":

- 13 comments on the CCO-PTF mechanism-design paper (ids A01-A13);
- 132 comments on the compendium of papers, dated Oct 10, 2025 (ids B001-B132; two of the Project's files hold these same 132 comments).

The audits are useful but not authoritative: each comment is checked before anything changes.

## Oct 28, 2026 presence check (planning chat)

`python3 -I presence_check.py <research-hub checkout> --csv triage.csv` searches every Hub page, PDF and JSON file for the passage each comment quotes. Result: 128 of 145 passages are still on the live Hub, 32 of them only in the PDFs. "Present" says nothing yet about whether the critique is right; step S29 judges each one, recomputes the arithmetic in `recompute.py`, and writes `triage.md`.

Spot checks so far (Claude's recomputation, to be confirmed in S29):

| Comment | Passage | Check |
|---|---|---|
| B025, B050 | multiplier 1/(1 - c(1 - t) + m) = 2.86 | 1.95 with the printed values: audit right |
| B031 | half-life 4.1 years | 3.72 with the discrete formula shown; 4.08 continuous: audit right |
| B001, B053 | poverty converges below 5% | the printed steady states are 11.8% and 7.4%: audit right |
| B002 | elasticity -0.71 | midpoint elasticity -1.60: audit right |
| B103, B127 | "15 percentage point" (85% to 98%) | 13 points: audit right |
| B032 | $3T is 14% of 2023 GDP | about 11%: audit right |
| B009 | $1.52T total | the table sums to $4,616B: audit right |
| B097 | NPV $1,847 | the printed formula gives $2,046; the audit's explanation gives $1,832: both off |
| B093 | $82,000 median wealth | an input in data/optimal-parameters.json, reported elsewhere as a result: traced in S30 |

## Oct 29, 2026 triage (S29)

Done. `triage.md` has the summary, the valid live items by severity and the PDF-only list; `triage.csv` has one row per comment (where it is on the Hub, verdict, severity, correction). `recompute.py` reruns every arithmetic point (64 checks). `triage.py <research-hub checkout>` reruns the presence check and rebuilds `triage.csv`, `triage.md` (below its marker) and `../corrections-additions.md`. All spot checks above are confirmed except B053 and B097: on B053 the audit's own explanation is also wrong, and on B097 its explanation gives $1,832 (see triage.md).
