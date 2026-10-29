"""S46 follow-up: the S46 items the first S46 pass (research-hub PR #9) left open.

    python3 -I apply_followup.py <research-hub checkout> [--check]

Each edit names the exact passage it replaces and must find it exactly once, or
nothing is written. Items: A01 (abstract), B013, B067/B014 (dual-currency-inflation),
B019/A07 (economic-modeling-simulation), B108 (integrated-digital-governance).
Notation follows PR #9's optimal-transfer-design sec 4.1: units spent plus units
converted come out of the allocation plus units received as payment, each counted once.
"""
import pathlib
import sys

OTD = "optimal-transfer-design.html"
DCI = "dual-currency-inflation.html"
EMS = "economic-modeling-simulation.html"
IDG = "integrated-digital-governance.html"
EDITS = []  # (file, id, start, end or None, new); end None: replace start; else replace start..end (end excluded)

EDITS.append((OTD, "A01",
    "mechanisms, demonstrating how this dual-tier system achieves Pareto efficiency improvements over existing welfare designs while fostering cultural enhancement and innovation.",
    None,
    "mechanisms, and state the conditions under which this dual-tier system, which also aims to foster cultural enhancement and innovation, would leave no one worse off than existing welfare designs (Proposition 1); no Pareto improvement is claimed."))

EDITS.append((DCI, "B013", "<p><strong>Household Budget Constraints:</strong></p>", "<p><strong>Basic Unit Dynamics:</strong></p>", """<p><strong>Household Budget Constraints:</strong></p>
        <ul>
            <li>Basic units: B<sup>spent</sup><sub>i,t</sub> + B<sup>conv</sup><sub>i,t</sub> ≤ B<sub>t</sub> + B<sup>rec</sup><sub>i,t</sub> (each unit is spent once or offered for conversion once; the rest lapse)</li>
            <li>Essential consumption: x<sub>E</sub> ≤ B<sup>spent</sup><sub>i,t</sub> + P<sub>E</sub></li>
            <li>Non-essential consumption: x<sub>N</sub> ≤ P<sub>N</sub></li>
            <li>Sources of primary currency: P<sub>t</sub> = w<sub>i</sub>h<sub>i,t</sub> + P<sub>convert,i</sub> + (1 + r)S<sub>t-1</sub> + Y<sub>i,t</sub></li>
            <li>Uses of primary currency: P<sub>t</sub> = P<sub>E</sub> + P<sub>N</sub> + S<sub>t</sub></li>
        </ul>

        <p>Where B<sub>t</sub> represents basic units received in period t, B<sup>rec</sup><sub>i,t</sub> basic units the household receives as payment, B<sup>spent</sup><sub>i,t</sub> and B<sup>conv</sup><sub>i,t</sub> the units it spends on essentials and offers for conversion (sec 3.3; units beyond its capacity lapse), P<sub>E</sub> and P<sub>N</sub> are primary currency allocated to essential and non-essential consumption respectively, w<sub>i</sub>h<sub>i,t</sub> is earnings, P<sub>convert,i</sub> represents converted currency from Creator Collective participation (a source of primary currency like any other, spent on either kind of good or saved), S<sub>t</sub> represents savings carried forward at interest rate r, and Y<sub>i,t</sub> other primary income. This is the budget of the mechanism-design paper (Optimal Transfer Design, sec 4.1).</p>

        """))

EDITS.append((DCI, "B067 B014", "<p><strong>Octave Capacity Function:</strong></p>", "<h3>3.3 Conversion Mechanism</h3>", """<p><strong>Octave Capacity Function:</strong></p>
        <p>C<sub>i,j,t</sub> = B<sub>0</sub> × 2<sup>min(O<sub>i,j</sub>, Ō<sub>j</sub>)</sup></p>

        <p>Where:</p>
        <ul>
            <li>C<sub>i,j,t</sub> = Conversion capacity for individual i in industry j at time t</li>
            <li>B<sub>0</sub> = Base conversion capacity ($1,200)</li>
            <li>O<sub>i,j</sub> = Individual i's octave level in industry j</li>
            <li>Ō<sub>j</sub> = Industry j's maximum octave level</li>
        </ul>

        <p>One rule caps conversion: the industry maximum Ō<sub>j</sub> limits the octave level, and the capacity that level gives limits the units converted (sec 3.3). A person active in several industries has one capacity per period, the highest of their industry capacities: C<sub>i,t</sub> = max<sub>j</sub> C<sub>i,j,t</sub>. (Modelling assumption: the papers do not say whether capacities in different industries add up; this is the more cautious reading.)</p>

        """))

EDITS.append((DCI, "B067", "<p>P<sub>convert,i</sub> = min(C<sub>i,j,t</sub>, B<sub>expired,i</sub>) × R<sub>i</sub> × Q<sub>i,t</sub></p>", None,
    "<p>P<sub>convert,i</sub> = min(C<sub>i,t</sub>, B<sub>expired,i</sub>) × R<sub>i</sub> × Q<sub>i,t</sub></p>"))
EDITS.append((DCI, "B013", "<li>B<sub>expired,i</sub> = Basic units available for conversion</li>", None,
    "<li>B<sub>expired,i</sub> = B<sup>conv</sup><sub>i,t</sub>, the basic units i offers for conversion: unspent units of their own, or units received as payment (sec 3.1). Units received as payment were spent by someone else, so across all N households Σ<sub>i</sub> B<sub>expired,i</sub> ≤ N × B<sub>t</sub>: no unit is converted twice</li>"))
EDITS.append((DCI, "B013",
    "<p>The critical insight is that conversion is capacity-constrained by industry octave limits, creating an endogenous ceiling on monetary expansion independent of basic unit distribution.</p>", None,
    "<p>Conversion is bounded twice: by capacity, and by the units issued, since no unit is converted twice. So ΣP<sub>convert,i,t</sub> ≤ (R × Q)<sub>max</sub> × min(Σ<sub>i</sub> C<sub>i,t</sub>, N × B<sub>t</sub>). Industry octave limits cap monetary expansion, but the ceiling also rises with the basic units distributed.</p>"))

EDITS.append((EMS, "B019 A07", "<li>Risk preference: γ<sub>i</sub> ~ Beta(α<sub>γ</sub>, β<sub>γ</sub>)</li>", None,
    "<li>Relative risk aversion: γ<sub>i</sub>, drawn from the distribution in section 4.1</li>"))
EDITS.append((EMS, "B019", "<p>U<sub>i</sub> = u(c<sub>i</sub>, l<sub>i</sub>, s<sub>i</sub>) + β<sub>social</sub> × SocialStatus<sub>i</sub></p>", None,
    """<p>U<sub>i</sub> = u(c<sub>i</sub>, l<sub>i</sub>) + β<sub>social</sub> × SocialStatus<sub>i</sub></p>

        <p>with u(c, l) = [(c<sup>1-α<sub>leisure</sub></sup> l<sup>α<sub>leisure</sub></sup>)<sup>1-γ<sub>i</sub></sup> - 1]/(1 - γ<sub>i</sub>), the log of the composite when γ<sub>i</sub> = 1. Skill s<sub>i</sub> enters through the wage, w<sub>i</sub> = w̄ × s<sub>i</sub>, and future periods are discounted by δ. This form uses only the behavioural parameters of section 4.1 (risk aversion γ, time preference δ, work-leisure preference α<sub>leisure</sub>). It is a modelling assumption: an earlier version left u unspecified.</p>"""))

EDITS.append((IDG, "B108", "<p><strong>dZ<sub>k</sub>/dt", "<h3>4.4 Network Value Quantification</h3>", """<p><strong>dZ<sub>k</sub>/dt = Σ<sub>i≠k</sub> F<sub>ik</sub> - Σ<sub>j≠k</sub> F<sub>kj</sub>, with F<sub>ij</sub> = M<sub>ij</sub> · Z<sub>i</sub> · f(P<sub>i</sub>, P<sub>j</sub>) · g(Z<sub>i</sub>/C<sub>i</sub>)</strong></p>

        <p>Where:</p>
        <ul>
            <li>Z<sub>k</sub> is the population of zone k, and F<sub>ij</sub> the flow of people from zone i to zone j</li>
            <li>M<sub>ij</sub> represents mobility rates between zones (per resident)</li>
            <li>f(P<sub>i</sub>, P<sub>j</sub>) captures preference alignment, between 0 and 1</li>
            <li>g(Z<sub>i</sub>/C<sub>i</sub>) represents capacity constraints: a nondecreasing function of zone i's population relative to its capacity C<sub>i</sub>, for example g(x) = x</li>
        </ul>

        <p>Each flow is proportional to the population of the zone people leave, so no one leaves an empty zone; and every departure from one zone is an arrival in another, so total population is conserved. An earlier version left the outflow term g(C<sub>k</sub>) undefined.</p>

        """))


def main():
    hub = pathlib.Path(sys.argv[1])
    texts, errors = {}, []
    for f, ids, start, end, new in EDITS:
        t = texts.setdefault(f, (hub / f).read_text(encoding="utf-8"))
        for m in [start] + ([end] if end else []):
            if t.count(m) != 1:
                errors.append(f"{f} ({ids}): found {t.count(m)} times: {m[:70]!r}")
        if errors:
            continue
        a = t.index(start)
        b = t.index(end) if end else a + len(start)
        texts[f] = t[:a] + new + t[b:]
    if errors:
        sys.exit("Not applied:\n  " + "\n  ".join(errors))
    print(f"{len(EDITS)} edits match in {len(texts)} pages.")
    if "--check" not in sys.argv:
        for f, t in texts.items():
            (hub / f).write_text(t, encoding="utf-8")
        print("Written.")


if __name__ == "__main__":
    main()
