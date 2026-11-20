# S85: an outside reading of the results, before publication (Nov 20, 2026)

**What was sent.** `audits/nvidia-2026-11-20-s85-results/build_packet.py` builds the packet (119,191 characters). It holds the reviewer's instructions (seven questions), the preregistration with Amendments 1-3 (items 1-10), the checks file, a condensed extract of the tables (block A at 20 years: every cell's costs, offset, share and category in all six readings, with the programme's effects; block E at 20 years: every row's inflation, category and produced share, and the break-even m), and the report as on compassionism-simulation branch `claude/s85-tables` at `e75736b`.

**Model.** The model list was read again on Nov 20 (33 models). Nemotron 3 Ultra (`nvidia/nemotron-3-ultra-550b-a55b`, temperature 0.3). The first attempt (max_tokens 16,000) spent its whole budget reasoning and returned no answer (`finish_reason` "length"; kept in `nemotron/attempt1/`). The second (max_tokens 40,000) finished with "stop" and 32,265 characters of answer: `nemotron/reply_content.md` (word for word), `reply_reasoning.md`, `stream.txt`.

It is a reading, not a result. Each point was checked against the full tables (`s85-tables-503fa48/s85-summary.json`) before anything changed. The packet held the 20-year tables of blocks A and E only, so several points marked "not verifiable" are the packet's limit, not the report's; those figures were rechecked against the full tables.

## Triage

| # | The reading's point | Checked against | Verdict | What changes |
|---|---|---|---|---|
| 1 | Yearly wealth poverty's offset is 59-87%, not 59-93%; median wealth's 14-24%, not 13-40% | Block A, both forms: lost jobs 59-87% and 13-24%, shorter hours 85-93% and 18-40% | The report's ranges are right across both forms (the reviewer read lost jobs only), but the sentence did not say so | The sentence names "across both forms" and gives each form's median-wealth range |
| 2 | "136 in part, 8 fully" cannot be verified from the category table's shorthand | The per-cell codes: 136 P and 8 F at 20 years | Right count; the table's shorthand ("PPPPPF then PPPPPP in every other cell") was unclear and its key did not say each six-letter group is one cell | Every cell spelled out; the key explains the groups |
| 3 | "48-69 points a year at 20 years" is not Reference's range (48-63) | Block E, main reading: Reference 48.0-62.7, Adverse 54.2-69.4, Stress 53.2-69.2 | Right range across the three environments, not said | "across the three environments" added; the findings text gives Reference's 48-63 beside it |
| 4 | "18-82 across everything" is wrong; the maximum is 70.5 | 20 years: 17.7-70.5; 40 years: up to 82.2 (Stress, full coverage, main reading) | The 82 is a 40-year figure; the sentence did not name the horizon | "18-71 at 20 years, up to 82 at 40" in sections 2, 4, 7 and 13 |
| 5 | Displacement raises inflation by 2.6-5.4 points, not 1-14 | At 50%, 20 years: 2.4-5.4; across 30-70% and both horizons: 1.3-14.0 | Both right for their scope; the report did not name it | "1-8 points at 20 years and up to 14 at 40"; section 7: "2 to 5 points at 50% at 20 years (up to 9 at 40)" |
| 6 | "A fifth to two fifths of the fall in wealth" overstates (13-24%) | 13-40% across forms; 13-24% with lost jobs | Correct: "a fifth" is above the low end | "13-40% (13-24% with lost jobs)" in sections 13 and 14 |
| 7 | "At most about a sixth" understates 18% | Largest produced share 17.5% (main reading) | Correct in spirit | "at most 18%" |
| 8 | The take-home's "$18,746 and $30,874" are ambiguous; then found consistent (the offset) | Block D: change in the programme's effect on median wealth | Right figures, unclear words | "the programme's effect on median wealth grows by" |
| 9 | 48% of the dividend paid looks wrong (54% x 19/20 = 51%) | The dividend grows with displacement, so the unpaid last year is its largest share | The figure is right | Brief reason added in section 6 |
| 10 | Add macro caveats: no central-bank response, the quantity price rule, no general equilibrium | The engine's price rule and the study's rows (no `cb` switch) | Correct and missing | A limit added in section 13: the inflation figures measure the size of the unbacked money, not a forecast of prices |
| 11 | The opt-in "worsens" description is fair; inspect a decomposition (counting effect, financing, selection) | The report's inspection (Adverse, seeds 1-100) | Agreed | Already listed as the next step's full trace |
| 12 | Amendment 3's choices do not favour the programme (Holm over 48 is stricter; references and signs fixed before reading) | The amendment | Agreed | None |
| 13 | Decision rules 2-7 are followed | The report | Agreed | None |
| 14 | The findings text omits limits (no central bank, savings pending) | Section 14 | Partly: a page text is short by design, and the report's limits section holds them | Horizon named ("Figures are for 20 years"); ranges corrected as above |
| 15 | The backing measure is narrow; m has no empirical basis; y_K may not apply to the providers' reinvestment | The preregistration's limits | Already stated (m a design parameter, project hours only, the cautious side) | None |
