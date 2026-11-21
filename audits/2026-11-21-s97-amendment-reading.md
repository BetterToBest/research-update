# Outside reading of the release-rerun amendment (Nov 21, 2026)

What was read: Amendment 2 of `prereg/2026-11-s90-private-price-at-sale.md` (the release's reruns and checks), with the whole preregistration and the plan's S97 text, as committed on branch `claude/s97-release-reruns` (public). Reader: `nvidia/nemotron-3-ultra-550b-a55b:free` on OpenRouter (the NVIDIA catalogue's call failed upstream the same minute). One request; temperature 0.3; 40,000 output tokens allowed. The reader was asked for gaps in the rerun list, checks that cannot fail, anything favouring the programme, the below-full-backing test, and ambiguities. Its answer is a reading, not a result.

## Triage (Claude, with what was checked)

| # | Point | Severity it gave | Verdict | What was done |
|---|---|---|---|---|
| 1 | `r2FreezePair` is missing from the rerun table; the grep for `sp` covered only some jobs | must fix | Partly. `r2FreezePair` is the row builder the jobs share, not a study, so there is nothing to add. The grep's scope was worth stating: `s85.js` and `s94.js` set `sp` only to add `vAt: 'sale'` (checked) | Scope stated in Terms |
| 2 | "Per cell" is not defined for the supply study's paired change | should fix | Agreed | C3: a cell is one base row (backed share) in one environment and horizon, 30 per outcome |
| 3 | At no backing the premium is zero, so the half-the-swing rule fails spuriously | must fix | Its reason is wrong: `bizPremPerBU` (index.html) depends on the conversion rate and the business tax rates, not on the backed share, so the rule acts at every share. Its safeguard is sound anyway: a halving test cannot pass where there is no swing to halve | C1: where the lagged measure is no larger than S92's at-sale measure, the condition is at-sale ≤ lagged |
| 4 | F2 does not name the seeds of the swing comparison | should fix | Agreed | Seeds 1-20, 500 adults, 20 years, three environments |
| 5 | F9's readers, "source opened" and the triage are vague | should fix | Agreed | Language models from makers other than Anthropic and each other; triage file per reading; a point that would change a figure is acted on only after its data file or code is checked |
| 6 | G quotes S92's range rather than the release figures | should fix | Agreed | G states F1's release figures |
| 7 | "Naming each engine" could be met by a field no reader sees | minor | Agreed | F8: in text a reader sees |
| 8 | E does not say which fields are excluded | minor | Agreed | E compares each seed's value of each key under `rows`; `_meta`, timing and log files not compared |
| 9 | A2 is a gate, not a defect check | minor | Agreed; no change needed | None |
| 10 | D3 may fail on a known engine change | minor | Agreed in part: a failure must stop the read either way | D: a failure by design gets a dated amendment naming it before anything is read |

Nothing the reader raised concerned a figure; no figure exists yet for this amendment.
