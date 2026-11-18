# S82: an outside reading of the results, the report and the findings-page text (Nov 18, 2026)

**What was sent.** `audits/nvidia-2026-11-18-s82-results/build_packet.py` builds the packet (164,258 characters):
- the reviewer's instructions (seven headings);
- the preregistration's questions, design, outcomes, analysis, checks, decision rules, reporting and limits, with Amendments 5 and 6;
- the checks as run;
- the tables of questions 1 and 2 at 20 years (trimmed to fit);
- the report `dev/reports/s82-supply-indexing.md` as first written (compassionism-simulation `6b83d34`);
- the findings page's new section as rendered (text only).

The other tables (questions 3-6, and 40 years) were left out for length. All are published in compassionism-simulation `dev/runs/s82-batch/` and compassionism-sim-results `s82-tables-aa2a4e0`.

**Model.** Nemotron 3 Ultra (`nvidia/nemotron-3-ultra-550b-a55b`; NVIDIA API catalogue, model list read again on Nov 18: 32 models), max_tokens 24,000, streamed. It finished (`finish_reason` "stop"; 33,803 characters of answer, 1,101 of reasoning). Word for word: `nvidia-2026-11-18-s82-results/nemotron/reply_content.md`, `reply_reasoning.md`, `stream.txt`.

It is a reading, not a result. Every point below was checked against the tables before anything changed.

## Triage

| # | The reading's point | Checked against | Verdict | What changed |
|---|---|---|---|---|
| 1 | "Every primary result holds under the sourced limit" implies a real test for all six readings; for five it passes by construction (§1.1, §3.2, §7.2) | the checks' NOTE (36 of 36 supply rows equal the base row in those keys) | **Confirmed** (wording) | The report's summary and the page now say the one real test is basket poverty; the other readings pass by construction |
| 2 | The page shows wealth only for the supply limit; under wages never made up, wealth breaks even at low backing too (§2.10) | `s82-breakeven.json`: median real wealth, weighted, 0.08 (20 years) and 0.75 (40 years), Reference | **Confirmed** | The page prints both, from the file |
| 3 | The wage readings never made up should be framed as bounds (§7.3) | the preregistration: wage readings are design parameters, unsourced | **Partly confirmed.** No source says they are extreme, so they are not called "extreme". They are the pessimistic end of the range swept | Report §5 and the page say so |
| 4 | "Restricted" is a policy reading (halved values), not a measurement of today's policies (§7.6) | Amendment 1; the design-reading note | **Confirmed** (wording) | Labelled "a policy reading" in the report's table and on the page |
| 5 | The surge protocol is not modelled, so the shortages may be overstated (§7.11) | the preregistration's limits | **Confirmed** (wording) | Report limit 8 says so |
| 6 | The building-speed sweep assumes costless capacity (§7.12) | the preregistration's limits | **Confirmed** (wording) | Report limit 9: a physical sweep, not a fiscal one |
| 7 | The page says "below the cost of living"; the outcome is basket poverty (§1.2) | the page's own label ("Cost of living (basket poverty)") | Not confirmed, but clarified | "(basket poverty)" added to the line |
| 8 | 40-year figures and questions 3-6 cannot be verified (§1.3-1.8, §7.1) | the full tables | Not confirmed: left out of the packet for length; every figure was checked against the published tables | none |
| 9 | Holm over six readings against the preregistration's four (§7.16) | Analysis; the tool's header; `dev/DECISIONS.md` "S82 part 3b" | Not confirmed: outcomes 3 and 4 are each read two ways, so Holm over six is the cautious side, as recorded | none |
| 10 | The market's rule 1.51% / 0.16-0.17% has no environment (§1.6) | report §8 | Not confirmed: the sentence opens "Adverse and Stress have the same shape" | none |
| 11 | The page text is cut off mid-sentence (§7.22) | the packet | Not confirmed: the packet's text excerpt stopped there; the page is whole (`check_round2.js`, `domtest.js` 162 pass) | none |
| 12 | Inflation's 5-point share in Stress given as 0.892 (§1.10) | Stress break-even 0.899 | The reading's own slip; the report's "0.88-0.90" stands | none |
| 13 | The ageing reading's withholding is right under the preregistration and the reason is sound (§5) | Amendment 6 | Agreed | none |
| 14 | No arithmetic error in the figures it could check (§6) | — | Agreed | none |

No figure changed. The wording changes are compassionism-simulation `08ec090` (pull request 158).
