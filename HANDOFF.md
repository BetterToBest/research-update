# Handoff (Nov 1, 2026): S13 outside audits, first pass, done

## Step status
S13's first pass is **done**: the Grok audit (I5) is triaged and the engine was audited against its own specification. Confirmed bugs are fixed behind a switch, and the study page's "What would have to be true" panel is corrected. The second pass (on the release) comes after S7.

## What shipped
- research-update [#29](https://github.com/BetterToBest/research-update/pull/29): `audits/grok-i5-triage.md` (18 items: 2 valid before the freeze, the rest addressed, later steps or turned down) and the S47 checklist in PLAN.md.
- compassionism-simulation [#59](https://github.com/BetterToBest/compassionism-simulation/pull/59): `dev/reports/s13-engine-audit.md` (E1-E18, the panel review). Switch `AUD`, row option `au`, off by default (guard test and SNAP rule check identical; lineage proof recorded): `au: true` = `gate` (wage-bonus BLEI gate in year-0 prices), `sg` (graded spending on all cash income), `fbs` (octave score in year-0 dollars); `wOut` = wages follow outside inflation (a reading). The study panel text is corrected via `dev/tools/study_data.py`.

## What the audit found (probes, 50 and 20 paired seeds)
- No accounting, draw-count or estimand error. The three corrections move the release row's effect by a few tenths of a point on basket poverty and 0.6-0.8 points on BLEI; no headline changes direction.
- Wages ignore the 2% outside inflation in Adverse and Stress (E5). With `wOut`, Adverse no-programme basket poverty falls from 66% to 52%, and the "too little wealth" penalty shrinks by about a third.
- **Biggest finding (E6):** the headline needs wages to keep up in full, within the year, with the programme's own ~51%/year inflation. At 95% indexation the Reference fall in basket poverty is 22 points instead of 30. At 75%, the programme raises basket poverty everywhere. It hardly matters if every dollar is backed (no programme inflation).
- MODEL_SPEC.md (v5.3) and ODD.md (v5.2) describe an older model (E1). The release charges every earner a flat contribution of about 2.8% for the PTF/PTH price cuts (E2). The spec says it has none.
- Study panel: BLEI poverty rises in Stress (the panel said it falls); the damping constant acts on outside inflation only (wording chosen with d201/d213 was wrong, corrected; flagged for Duke).

## In flight
Nothing.

## Decisions waiting
None new. The S47 recommendations (main rows with `au: true`; `wOut`, a `wIdx` sweep, FBS50, both other backing readings; 0.593 re-derived; specs written for the frozen model) are Claude's modelling choices, landed as amendments at the freeze.

## Next step
**S50** (second, independent implementation of the release row), opus, xhigh. It waits on S13, now done. Then S47.

## Pitfalls
- `wIdx` and the backing reading interact: sweep them together in S47, or the E6 result reads worse than the every-dollar-backed reading shows.
- `au` changes the no-programme run slightly in Adverse and Stress (the gate correction applies to both runs). Run both rows of a pair with the same `au`.
- The Grok share link is read through `https://grok.com/rest/app-chat/share_links/<id>` (the page itself is script-built).
- `gh` has no valid token here; the GitHub tools work for pull requests.
