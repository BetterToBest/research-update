# Outside reading of the swing-measure amendment (Nov 21, 2026)

What was read: section C of Amendment 2 and Amendment 5 of `prereg/2026-11-s90-private-price-at-sale.md`, as committed (public), with the tool `dev/tools/s90_swing_growth.js` (compassionism-simulation, first version) and its output, and the original measure's output at full backing. Reader: `nvidia/nemotron-3-ultra-550b-a55b:free` on OpenRouter (free tier; 4,201 tokens in, 3,657 out). The packet and the answer are in `audits/2026-11-21-s93-amendment5-reading/`. The reading came after the growth-change measure was computed at backed shares 0 and 0.5 and before it was used.

## Triage (Claude, with what was checked)

| # | Point | Severity it gave | Verdict | What was done |
|---|---|---|---|---|
| 1 | "About 40-50% a year in every run" rests on seed 1 of two environments | should fix | Agreed | The growth over every seed, environment and backed share is now computed from the saved series and published: mean 42-50% at no backing, 21-27% at half backing (compassionism-sim-results `s93-belowfull-69e8953`) |
| 2 | The new measure changes the construct (growth-rate volatility, not dollar volatility); a steady 40% growth with small wobbles would pass | must fix | Partly. Counting steady growth as swing is the defect being corrected: the question (S90) is the two-year alternation, not growth. A check in dollars with the trend removed is a fair guard against a measure that suits the answer | Added a sensitivity measure (the original measure on BU spent divided by its fitted log-linear trend), committed before it was computed. It agrees: ratios 0.11-0.29 below full backing |
| 3 | Post hoc: say why this measure, require a sensitivity check, justify the fallback, adjust for the choice | must fix | (a), (b) agreed; (c) not taken: the fallback uses S92's own series on the same measure, not the original measure's figure, and it was not triggered; (d) no test statistic is computed, so there is nothing to adjust; the choice is disclosed instead | The reason (the simplest measure that is 0 for any steady growth rate; the swing is an alternation of the growth rate) and the sensitivity check are in the amendment; the release text must say the measure was chosen after the original failed |
| 4 | The fallback threshold is uncalibrated for the new measure | should fix | Not taken | Same as 3(c): computed on the same measure from S92's series (3.9%, 3.9%, 2.3%); not triggered (every lagged figure is 25-39%) |
| 5 | The new measure is not shown at full backing | should fix | Agreed | Both measures computed at full backing on the release row and on S92's rows: growth-change measure at the sale 0.06-0.09 of lagged, sensitivity 0.12-0.14; the original measure there holds (F2) |
| 6 | "Seen" covers 2 of 60 cells; say so in the release text | minor | Agreed | The amendment's "Seen" paragraph states it; the release text will repeat it |

No figure was changed. The verdict on section C1 is decided by the growth-change measure, as Amendment 5 fixed before the reading; the sensitivity measure agrees with it.
