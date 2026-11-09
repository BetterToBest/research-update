# Handoff (Nov 9, 2026): S56 done, the outside reviews triaged

## Step status
S56 is **done**. Duke pasted two reviews (Grok, ChatGPT) of S39, S55 and the inequality measures. Every point was checked against the reports and code, every cited source that can be opened was opened, and each point is accepted, adapted or declined with a reason in `audits/2026-11-s39-s55-review-triage.md`.

## What shipped
- research-update [PR 74](https://github.com/BetterToBest/research-update/pull/74) (merged, 0d6c11e): the triage; PLAN.md (S7 and S57-S63 amended, new S66, S60 after S61, D18 as answered); study programme Amendment 12; correction notes in the audit prompt and the round-2 note; this file.
- compassionism-simulation [PR 87](https://github.com/BetterToBest/compassionism-simulation/pull/87): dated correction note in the S39 report (section 6); MODEL_SPEC section 9 (interval method, `giniW` vs `giniWN`); DECISIONS.md. Squash-merged (7895f27) after its checks (checks, guard) passed.
- Ledger synced (hub version 101): S56 done, S66 added, D19, D20, links for D18, next, log.

## Findings (plain words)
- The reviews confirm the project's reading: the placeholder price rule decides the inflation and wealth results; BeforeIT could not test it; no study covers new money of 30-50% of household income a year; the S55 wealth gain rests on PTF growth toward 49% at at-cost prices.
- Three wording errors, no figure changed: S39's "0 to 1" is the range between two assumptions, not a bound; the published wealth Gini counts debts as zero (the prereg said "debts kept"); study intervals are paired-bootstrap (MODEL_SPEC gave only the release row's formula).
- Two review claims were wrong: the headline already uses CPS earnings; the 21.9% vs 33.4% "debt gap" is the frozen headline (spending share 0.877, CPS wages) against S34's released v5.6.
- Five cited sources were not found or differ (triage, "Sources opened"); they are not used.

## In flight
- Nothing.

## Decisions waiting
- D19: who pays when PTF prices do not cover running costs. Default: S62 builds three readings; S63 chooses the main one.
- D20: density tests as hard steps or a smooth curve. Default: keep the steps in the main row, add a smooth-curve reading.
- D18 was answered Nov 9 (not the default): Hub text citing simulation figures (S24's simulation figures, S25, S40) waits for S65, as do S44, S45, S8. PLAN.md now says so.

## Next step
**S7** (sonnet, medium): the release of today's engine and its findings page; its section now carries S56's wording rules. S66 and S61 can also start now (both wait only on S56).

## Pitfalls
- No model names in commits: the S56 branch commit in compassionism-simulation named one; PR 87 is squash-merged with a clean message instead (no history rewrite).
- `eGiniW` is the debts-as-zero Gini; `eGiniWN` keeps debts and is already in every frozen output (S57 needs no rerun for it).
- The audit prompt is kept as sent; read its correction notes (top of the file) before reusing it.
