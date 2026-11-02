# Handoff (Nov 2, 2026): S53 done, security outcomes beyond wealth (pilot reported)

## Step status
S53 is **done**. The 50-seed pilot finished (checksums verified; both consumer scripts load it), the plain-words pilot report is written, and the addendum's Amendment 1 lists what the full study adds. S47's S53 line in PLAN.md now carries those additions.

## What shipped
- compassionism-simulation [#67](https://github.com/BetterToBest/compassionism-simulation/pull/67) (squash 5027297): `dev/reports/s53-security.md` (pilot report), `dev/reports/s53-security-tables.md`, `dev/tools/s53_security.py` now prints the Q19 difference in differences (savings that keep up with prices) and, descriptively, shock against no shock. No engine change.
- research-update [#41](https://github.com/BetterToBest/research-update/pull/41) (merge bd2eab9): addendum `prereg/2026-11-security-addendum.md` Amendment 1; PLAN.md (S53 done with findings; S47's S53 line).
- Results: compassionism-sim-results `s53-security-f15eaf6/` (50 seeds, run 41423271435).

## Pilot findings (labelled pilot; not figures of the model)
- The BU makes income falls of any size much rarer for every group under both designs.
- C2.2: months of cover and displacement by price improve for every group, but through lower need. Prices rise about 36% a year under C2.2 too, and median real savings fall by about two thirds.
- Release row: more households under three months of cover (+7 to +17 points), more displaced by price. Non-participants are less secure on almost every savings measure and have more uncovered income falls (decision rule 2: harm).
- Savings that keep up with prices reverse every unfavourable savings result (rule 3: nearly all of it comes from inflation).
- Money-income falls are less often covered under both designs (rule 4). A 10-seed exploratory check, not preregistered, points to a smaller buffer under the release row and to falls in conversion pay under C2.2.
- Results hold under S52's shock (they move by less than one point).

## For S47 (Amendment 1)
- Study P goes to 12 rows per environment: add the C2.2 design and its no-programme run with savings that keep up with prices (`security.js`, `PREREG_ROWS` 12; about 0.85 runner-hours at 500 seeds).
- Two reporting keys under `sec`, with the guard test identical: money-income falls split by cause (wages, conversion pay, other), and uncovered falls that leave the adult below their own cost of living.
- For S54's addendum: `secU25` and `secM3` on both savings readings for every lever row, and in stage 3's no-harm test.

## In flight
- Nothing.

## Decisions waiting
- None new.

## Next step
**S54** (policy levers): S51-S53 are done, and D13 is answered.

## Pitfalls
- Commit trailers: use `Co-Authored-By: Claude <noreply@anthropic.com>` only. This session's first compassionism-simulation commit (branch `claude/s53-security-pilot`) carried a model name. Main is clean because the PR was squash-merged with a clean message. The branch still holds that commit, so Duke may delete the branch. The two stray branches named earlier are still there too.
- Group "chose not to take part" is fixed at the start from each adult's drawn willingness. Under C2.2 everyone gets the BU automatically, so the groups differ little there.
- The months-covered measures are mixed: under C2.2 the lower need dominates. Read them beside `medWealthReal`.
