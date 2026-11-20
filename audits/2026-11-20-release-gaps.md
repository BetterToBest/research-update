# Gaps and limitations open before the next release (inventory, Nov 20, 2026)

Written in S94 at Duke's request: "address all gaps and limitations that we can prior to S93" (the release with the private price at the sale as the default). This inventory is what the outside readers were given (`audits/2026-11-20-pre-release/`). Their readings, and Claude's triage of them into plan steps, are in `audits/2026-11-20-pre-release-triage.md`.

Each item: what the gap is, where it shows, whether it can change a headline, and its status. "Ledger" means the item comes from the ledger's issues list and was not re-checked this session unless it says so.

## A. What the headline rests on
1. **Full backing is assumed in the main row.** Every programme dollar is matched by new output (a design parameter, the design's statement). The engine's own mechanism for new output reaches about 1% of the payout. The automation study's produced backing is 6-17% at 20 years (3-7% opt-in), with programme inflation of 48-69 points a year in full coverage. The findings page carries the footnote and a section. Open decision on the headline cards' headings and the full-backing condition (default: no change). *Can change how a headline reads: yes.*
2. **No limit on total supply below full backing.** A dated note covers the sentences below full backing. The supply-limit study exists but is not in the main row. *Below full backing only.*
3. **The opt-in design does far less than full coverage,** and with lost jobs it makes the rise in poverty larger in 9 of 12 cells. It is published, but the release text should keep it beside any full-coverage headline.

## B. Engine and model gaps
4. **The Creative Collectives' lending to start-ups** (Duke, Nov 17 and 19): preregistered Nov 20 (`prereg/2026-11-s94-collectives-lending.md`); build and run to follow.
5. **The late private price** (the BU's two-year swing): fixed behind an option, and the main rows were rerun. The release makes it the default. Item 5 of the release step, deciding which reached studies are rerun on the release engine (readings, financed rows, central bank, history, supply, the suite folders), is not yet preregistered.
6. **The simulation page still uses the Hub's early figures as targets**: `CFG.TARGET_WEALTH` 82000, `TARGET_GINI`, `TARGET_POVERTY`, `TARGET_STABILITY` and a "Target $82K" label on the interactive page (re-checked Nov 20: four occurrences in `index.html`). Research rule 3. *Visible to readers.*
7. **The written description does not describe the validation presets** it is checked by (MODEL_SPEC and ODD; ledger). The validation presets' "Gini" is of wealth less one year of the cost of living times the annual wage, not a wealth Gini.
8. **MODEL_SPEC gaps and contradictions** listed by the second implementation (four contradictions, about 30 gaps; ledger, status to confirm).
9. **Tax credits**: no child and dependent care credit; EITC reach is low (11.9% against 15.3%) because the model has no part-time work (ledger).
10. **Who is simulated**: working-age adults and their families; the Hub should say so (ledger). The labour-force scope option exists.
11. **Capacity of the community businesses is for the whole population**, not by zone or by sector. One utility share stands for electricity, gas and water.
12. **No private firms, banks or bond market.** The central-bank rule is a reduced form and has no channel to the price of essentials. There is no expectations channel.
13. **Capital income is not in the price rule's income**, and the automation dividend raises no investment.
14. **Displaced adults' outcomes by fifth of starting wealth** are not stored.
15. **Health, security and output per hour**: no opened source sizes health and security raising output per hour (left out of the automation study).

## C. The Hub and its figures
16. **Audit-flagged figures still live on the Hub**, many only in the PDFs: $847B net savings, "65% lower inflation", "15 percentage point" (it is 13), 85%/98% poverty reduction and $82,000 median wealth with a 95% interval, "10,000 iterations", elasticity −0.71 (it is −1.6), a steady state of 11.8% under a "below 5%" theorem, "14% of GDP" (about 11%), the Bristol Pound "£5 billion" and the 2.86 multiplier (it is 1.95). The main corrections package's first 22 items are not landed (ledger).
17. **168 cited external figures not yet opened** (`data/claims.csv`, "cited, not opened"; ledger).
18. **The θ "Monte Carlo calibration"**: no record it was ever run (ledger).
19. **The BLEI page may state the simulation's poverty line inverted** (ledger; status to confirm).
20. **The release data lacks series the BLEI visuals and the Five Measures chart need** (ledger; status to confirm).
21. **The Hub's 32-item site audit**: Gini comparability after the cost-of-living adjustment, terminology, sourcing gaps, AI-authorship disclosure, methodological transparency (ledger; status unknown).

## D. Process before a release
22. Outside readings of the results before they are published: done for the automation study (two readers), not yet for the release's own regenerated figures.
