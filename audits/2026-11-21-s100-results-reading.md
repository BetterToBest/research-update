# The yardstick study (pay by household type, the care credit): two outside readings before publication (Nov 21, 2026)

**What was sent.** `audits/2026-11-21-s100-results-reading/build_packet.py` builds the packet (80,012 characters, `packet.txt`): the reviewer's seven questions, the preregistration, the full tables file (`s100-tables-e50a3b3/s100-tables.md`) and the report as first written (compassionism-simulation `dev/reports/s100-part-time-dcc.md`, branch `claude/s100-yardstick-report`, first commit). Everything in it is public in the repositories.

**Readers.** The model lists were read again on Nov 21 (OpenRouter: 11 free models; NVIDIA: 33). Two makers other than Claude:
- **Gemma 4 31B (Google).** OpenRouter's free pool refused it at once (429, "temporarily rate-limited upstream", as on Nov 20; `reply-gemma-openrouter-429.json`). The same model on NVIDIA's catalogue then failed at the gateway after 163 seconds without streaming (502; `reply-gemma-nvidia-502.txt`). It answered when streamed (135 seconds, finish "stop", 5,912 characters): `reply-gemma-nvidia.md`, raw stream `reply-gemma-nvidia.sse`.
- **Nemotron 3 Ultra (NVIDIA)** on OpenRouter's free tier (`nvidia/nemotron-3-ultra-550b-a55b:free`, max_tokens 40,000): 406 seconds, finish "stop", 49,884 characters: `reply-nemotron.md` (raw `reply-nemotron.json`).

These are readings, not results and not an economist's review. Each point was checked against the tables and the summary file (`s100-summary.json`) before anything changed.

## Triage

| # | Reader | The reading's point | Checked against | Verdict | What changes |
|---|---|---|---|---|---|
| 1 | both | The figures in sections 2, 4, 5 and 7 follow from the tables (opt-in basket poverty 0.32-0.91, median wealth −$2,531, decision rule 2, the gap verdicts, the bounds) | The tables file | Agreed: neither reader found a misquoted figure there | None |
| 2 | Nemotron | The inflation changes in section 5 have four decimals; the tables file shows three, so 14 cells are "misquoted" | `s100-summary.json`, from which both the tables file and the report are made | Not misquotes: the four-decimal values are the summary file's own, and at three decimals several read 0.000. The report did not say where they came from | Section 5 says the inflation figures come from the summary file at four decimals and that the tables file rounds them to three |
| 3 | both | "No synergy that matters" is a judgement made after seeing the results; the preregistration says only that a synergy is stated where the interval excludes zero | The preregistration's analysis section; the 12 intervals (all at most 0.005 points) | Fair: the measurement was stated, but the label was a judgement word | Sections 2, 6 and 9 and the page: "measurable in 12 of 60 tests ... never larger than 0.005 points, which is negligible"; section 6 says these are stated because their intervals exclude zero |
| 4 | Gemma | Section 2's inflation line ignores the sign | Section 5 tables (both signs occur) | Fair | "in either direction" added |
| 5 | Gemma | "The care credit alone produces no statistically significant change" would be better than "changes nothing that matters" | The credit-alone rows: several changes exclude zero (for example 0.010 points of the share below 30 days, full coverage, Reference, 20 years) | The proposed sentence would be false; the original was a judgement word | Neither: "changes no poverty effect by more than 0.02 points" |
| 6 | both | Pay by household type is a static correction: it sets who has low pay but not a choice of hours; hours that respond to the programme, to taxes or to the cost of care are not modelled; care-paying shares do not respond to the programme | The engine (`ehAdjust`; the labour response acts on yearly pay); the reading note's limits | Fair and partly missing (the reading note had the SNAP hours rule and the form of the elasticities, not the general point) | A limit added in section 8 and on the page |
| 7 | Nemotron | The findings text says "the overall distribution is unchanged", but the bottom tenth is 17% high | Section 4's derived calculation | Fair | "still matches the survey's closely (its bottom tenth is somewhat high, as before)" |
| 8 | Nemotron | "US 11.8%" does not say which US figure (the earlier check used 15.3%) | The preregistration's US figures | Fair | "on the same basis: each adult's own tax unit, full take-up" in the findings text and on the page |
| 9 | Nemotron | "3% to 5% of the effect" overstates the low end; it gives 1.5% | Pairing each cell's change with its own effect: 2.9% (Reference, 40 years) to 4.7% | The reader divided Stress at 40 years' change by Reference at 20 years' effect; the report's "about 3% to 5%" is right | None |
| 10 | Nemotron | The earnings-distribution calculation was not prespecified and should be labelled a calculation | Section 4 | Already labelled ("not in the run's output, so it is a derived calculation") and recorded in the preregistration's dated note | None |
| 11 | both | Rules 2, 4 and 5 are followed; the care credit's reach is compared like for like; the "why" paragraph is fairly labelled and claims nothing unmeasured | The preregistration | Agreed | None |
| 12 | Nemotron | A fuller findings text for a general reader, with "we" and a step-by-step layout | The page's style (third person; Duke's decision named) | Its two substantive points are items 7 and 8; the rest is style | None beyond 7 and 8 |

## What this means

No figure changes. Five wording changes and one new limit, all made before publication (compassionism-simulation PR 181, second commit). Neither reading changes the decision-rule verdict or the recommendation on the main row, which remains Duke's decision.
