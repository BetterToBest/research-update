# Preregistration: the participation margin and yearly movement in and out of the labour force (S73)

Committed Nov 14, 2026 by S73, before the engine change and before any run. Engine: compassionism-simulation at commit `e7b329c` (main, S72 merged). The changes land on branch `claude/s73-participation`, off by default (guard test identical). The engine commit of the pilot is recorded in an amendment before the pilot runs.

## Why
The Nov 13 audit (`audits/2026-11-13-simulation-audit.md`, finding 3) and S60's validation found two gaps. First, S61's adults outside the labour force keep their status for the whole run (20-40 years with ageing): nobody leaves work for care, illness, school or early retirement after year 0, and nobody comes back. Second, the engine's response to the programme's unconditional dollars is all on hours: in S60's check against the US guaranteed-income experiment (Vivalt et al. 2026, $1,000 a month), earnings fell 15.6 cents per dollar per worker (the study: 16 cents) but nobody stopped working (0.0 points; the study: −4.2 points, standard error 1.7).

## What the engine does today (read before this file; not a result of any run)
- `lf` (S61, `LF_SCOPE`): at year 0 each adult 25-64 is drawn out of the labour force with the CPS ASEC 2026 share for their household type and age band, by reason (disability, early retirement, care, school), and given an own income by reason. Such an adult is treated as retired (`a._ret`): no wage, no job loss, no response. Fixed for the run.
- The labour response (`LABOR`, session 4): this year's earnings are `max(0, E0 × raise − I − D)`, where `I` is the income effect (0.16 cents per unconditional dollar, `rho`), `D` the displacement by conversion, and `raise` the programme's raises at one elasticity. Everyone with a wage keeps some earnings unless `I + D` exceeds them.

## Sources opened (Nov 14, 2026; `sources/s73_lf_flows.py`, output `sources/s73_lf_flows.json`)
- Census Bureau, CPS ASEC 2025 and 2026 public-use files (sha256 `318845a2…` and `fe819d0d…`, the second as S61). About half of one March's sample is interviewed again the next March; the person identifier links 39,927 records, of which 18,937 adults 25-63 pass the check (same sex, age up 0-2 years). Status as S61: out = did not work in the year for one of the four reasons.
  - Yearly exits from work: 4.7% of those in work (survey's own flows), by reason: care 37%, early retirement 31%, disability 24%, school 8% (women: care 45%; men: disability 32%, retirement 35%).
  - Yearly returns: disability 12%, retirement 11%, care 22%, school 44%.
  - Those who left earned $48,000 in the year before (those who stayed: $87,000).
  - At fixed ages the survey's own flows would raise the out share from 17% to 28%: they include the life cycle (people leave more than they return as they age). So two readings: exits that hold each cell's share where ages do not move (the engine without ageing; mean exit 3.6% a year), and the survey's own exits (for runs with ageing).
- Chetty (Econometrica 2012), the engine's existing source for the wage elasticity: compensated elasticities 0.33 on hours (intensive) and 0.25 on participation (extensive). Their ratio gives the extensive margin's share of a response: 0.25 / (0.25 + 0.33) = 0.43.
- Vivalt et al. (NBER w32719, revised Aug 2026; already opened by S60, `sources/s60_bargain.py`): participation −4.2 points (SE 1.7), so the 95% interval is −7.5 to −0.9; income excluding the transfer −16 cents per dollar. A check, never a target.

## What is built (options of `lf`; off by default)
1. `lf.fl` (yearly flows): `'stock'` (main) or `'panel'`. Each year, on its own random stream (seed + 730073, two draws per adult-year whatever the state), an adult 25-64 in work leaves for reason r with the cell's exit chance (age band × sex × household type), and an adult out for reason r returns with the reason's return chance (age band × sex). A leaver gets an own income drawn as S61's; a returner's wage is the wage at exit, moved with the price level (no wage growth while out: a stated simplification). With `fl` set the year-0 draw uses the same fitted stock (now by sex) so year 0 and the flows agree. Adults 67 and over are untouched (the engine's retirement).
2. `lf.pm` (the programme's participation margin): the share of the income effect taken by leaving work. One rule (guardrail 7): the income effect's dollars `L` from the programme (its unconditional dollars at the income effect's weights, without today's safety net, as S60's outside option) are unchanged in total; a worker leaves for the year when a fixed personal draw `u` (own stream, drawn once per adult) is below `q = pm × min(L, E) / E`, `E` this year's earnings after the safety net's response; a worker who stays loses `(1 − pm) × min(L, E) / (1 − q)`. So expected earnings are exactly those of today's rule; only how the loss falls changes (some leave, the rest cut less). Main value 0.43 (Chetty's ratio, above); swept 0, 0.25, 0.43, 0.7, 1. A leaver has no earnings that year and gets no unemployment insurance (a quit). With `pm` 0 the response is today's.
3. Reporting keys: the out share by year, exits and returns per 100 adult-years, the share ever out, programme leavers (adult-years), their earnings forgone, participation (adult-years 25-66 with earnings).
4. `r2MainRow` gains `lf: {fl: 'stock', pm: 0.43}` (Claude's recommendation, fixed now, subject to rule A's report) and `R2_ALT` a row for `pm 0` with `fl 'panel'`; the on-together tests (`dev/tools/s68_pairs.js`) are rerun.

## Unit tests (written with the build)
Off identical (guard test); `lf {}` with `fl` and `pm` unset identical to today; `pm 0` identical to `fl` alone; draws per adult-year on the main stream unchanged (eight); the flows' stream draws two per adult-year; with `pm` the mean earnings over a large population equal today's within sampling error (the rule's expected-value identity is also checked exactly on a single adult); stock-holding flows keep the out share within 1 point of year 0 at year 20 without ageing (reference environment, no programme, 20 seeds); a returner's wage equals the exit wage times the price ratio.

## Pilot (100 seeds; session machine, free)
Seeds 1-100, 500 adults, 20 years, Reference, Adverse and Stress, the candidate main row (`r2MainRow`, `r2MainStudy`) in both runs, both designs (release and C2.2):
- (A) today's main row (`lf {}`); `fl 'stock'`; `fl 'stock'` + `pm 0.43`.
- (B) `pm` 0, 0.25, 0.7, 1 with `fl 'stock'`; ageing (`ag`) with `fl 'panel'` and with `fl 'stock'`, `pm 0.43`.
- (C) the price rule and the contribution's base: C2.2 under the flat contribution on wages (S72's D21 row: share 1, base `w`, cap 0.9, `fx.fin 'money'`) without and with `pm 0.43`.
- (V) S60's validation: $12,000 a year to every adult, no programme otherwise, with `pm` 0, 0.43 and 1 (`fl 'stock'`).
Outcomes: participation (adult-years 25-66 with earnings), programme leavers, earnings and hours (`hrs`), earnings per transfer dollar (V), basket poverty (`fgt0PY`), wealth poverty (year 20 and yearly average), programme inflation (`endoAnn`), the contribution's rate (C), the out share by year, exits and returns. Paired differences against the no-programme run with 95% intervals (paired t over seeds).
Command: `node dev/tools/s73_pilot.js ENV 100`; tables `node dev/tools/s73_table.js`.

## Decision rules (fixed now)
- (A) Validation: with `pm 0.43` the $12,000 check's participation change lies in −7.5 to −0.9 points and earnings per transfer dollar stay within 2 cents of the run with `pm 0` (the rule keeps the total). If participation falls outside the interval the report says so and why; no value is retuned; the sweep is printed beside it.
- (B) Recommendation to S63 (fixed now): `lf {fl: 'stock', pm: 0.43}` in the main row; `pm` 0 and 1 beside every poverty and work result; `fl 'panel'` with ageing as the reading for ageing rows. If rule A fails because the participation change is smaller than the interval's upper end (−0.9), `pm 1` (the most participation the one-rule margin can give) is also printed beside the main row.
- (C) Headline: if `pm 0.43` moves basket poverty or wealth poverty (yearly average) by more than 1 point against `fl 'stock'` alone in any design and environment, the margin goes to S70's screen as headline-moving; otherwise the note says it moves little and why.
- (D) The flows: if `fl 'stock'` moves either poverty measure by more than 1 point against `lf {}`, the same.
- (E) Through the price rule and the contribution's base: the change in programme inflation and in the contribution's rate with `pm 0.43` is reported with its interval, whatever its size.
- Every outcome above is published (compassionism-sim-results and the report), whatever its direction.

## Unpaid work (Duke's note, ledger Nov 13)
People who leave paid work may do work of value the market does not pay for: care of children and family, community work, inventions and new businesses. The report carries "Claude's reading of the design" on this (research rule 6) and states what the model counts (paid earnings and their effects on income, prices and the contribution) and what it leaves out (the value of unpaid care and community work, and any business a leaver starts), with the hours released and the survey's reasons for leaving beside the participation result. No value of unpaid work enters poverty or any headline.

## Limits stated in advance
- The linked sample loses movers (the CPS samples addresses); its out share (17.0%) is close to the full sample's (17.2%).
- Returners keep their real wage at exit; the evidence of a wage penalty after time out is not modelled.
- `pm` splits the income effect only; the response to the programme's raises stays on hours.
- Reasons are fixed for a spell (a person out for care who later is out for disability is not followed).
- Programme leavers are not given a reason; the survey's reasons describe today's leavers, not the programme's.
- Hours depend on population size in the frozen engine (S68 part 2).

## Amendments
(none yet)
