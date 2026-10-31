# Handoff (Oct 31, 2026): S35 pilot studies, done

## Step status
S35 **done**. All seven pilots finished (`DONE` in every folder, SHA256SUMS verified), and the pilot report is written.

## What shipped
- compassionism-simulation [#51](https://github.com/BetterToBest/compassionism-simulation/pull/51): `dev/reports/pilot-studies.md` (labelled pilot throughout), tables and every estimate in `dev/runs/pilot-studies/`, written by `dev/tools/pilot_studies.py`, plus decisions in `dev/DECISIONS.md` (S35, Oct 31). No engine change. Merge status: see "In flight".
- Earlier in S35: compassionism-simulation #50 (engine 70d23be), compassionism-sim-results #8 (job script), research-update #18 (preregistration amendment 1).
- Results: compassionism-sim-results `pilot-{a,b,b10,c,d,d10,f}-70d23be`.

## What the pilots show (50 seeds; not headline figures)
- No outcome depends on population size beyond Monte Carlo error (11 of 504 comparisons, 2.2%). The only cases that pass the scale rule come from compounding: cumulative inflation at year 40, whose spread between seeds narrows with size.
- The CCO accounts for 93-97% of the effect. PTF, PTH and SZH are near inert (each between -1.2 and +0.3 points). The material interactions are CCO × CIP: they overlap on the cost of living (-1 to -3 points) and reinforce each other on wealth (up to +5 points).
- With ageing on, the release row makes wealth worse (Reference, year 40: 16.7 points worse). Adults who never join are worse off with the programme.
- Participation: in Reference the detection level is the grid floor (10%). In Adverse and Stress no level qualifies, because the wealth effect goes the wrong way.
- The debt reading lowers families in debt from 21.4% to 14.9% with no programme (SCF: 9.3%). It changes no decision.
- Full batch: about 230 runner-hours, all on Actions, at 2 processes per runner.
- Report section 9 lists what S47 must still add. Some items need a preregistration amendment: write null rather than 0 for keys past the run; the design-neutral BLEI at year 20 in 40-year runs; a yearly-rate reading of inflation; participation levels of 2% and 5%; the wording for hours.

## In flight
- compassionism-simulation #51: checks were running at the end of this session (domtest and guard test take about 15 minutes). If it is still open, the next session merges it once its checks are green.

## Decisions waiting
None. S37 going ahead was a modelling call, recorded in the report (section 8) and in dev/DECISIONS.md.

## Next step
**S37** (community and zone layer), opus, xhigh. The pilots show it is needed: the parts the density argument rests on are inert in the engine, and nothing in the engine depends on population size. If the Hub papers give no mechanism that can be modelled without invented constants, S37 says so and stops.

## Pitfalls
- Pilot files write 0 for keys past the run (`plv_39`, `ppov_39` and others in 20-year rows; `jnP*` in none rows). Never read those as values.
- A 40-year run's first 20 years equal the 20-year run exactly, so year-20 points appear twice. Count them once.
- Core-seconds measured with 4 processes per 4-vCPU runner are about doubled. Plan with runner-hours.
- The results repository is large: clone it with `--filter=blob:none --sparse` and `git sparse-checkout set <folders>` (folder names, not patterns).
