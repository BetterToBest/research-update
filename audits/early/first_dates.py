#!/usr/bin/env python3
"""When each early headline figure first appeared on the Hub (step S30).

Usage: python3 audits/early/first_dates.py <research-hub checkout (full history)> <compassionism-simulation checkout>

For each figure, `git log -G` finds the first research-hub commit whose diff adds a line matching the
figure's pattern (the frozen /v1/ archive is excluded) and the file it was added to. The first commit of
the simulation engine (index.html, or compassionism-simulation.html before the rename) is printed for
comparison: an engine cannot have produced a figure published before it existed.
"""
import subprocess, sys

FIGURES = [  # label, regex (git -G, extended)
    ("85% poverty reduction (CCO only)", r"85% poverty (reduction|elimination)"),
    ("98% poverty reduction / elimination (CCO-PTF)", r"98% poverty (reduction|elimination)"),
    ("$37,000 median wealth", r"\$37,000"),
    ("$82,000 median wealth", r"\$82,000|82000"),
    ("95% interval on median wealth ($64,000-$103,000)", r"\$64,000"),
    ("65% lower inflation", r"65% lower"),
    ("10,000 iterations / simulations", r"10,000\+? (Monte Carlo|simulation|iteration)"),
    ("Elasticity table (-0.71 for the Basic Unit amount)", r"-0\.71|−0\.71"),
    ("Gini 0.28", r"0\.45 (→|to) 0\.28|Gini.{0,40}0\.28"),
    ("30% participation threshold", r"30% (population )?participation"),
    ("55% minimum viable participation", r"(viable|minimum).{0,30}55%|55%.{0,30}(viable|minimum)"),
    ("75% minimum viable participation", r"minimum viable: 75%"),
    ("theta 0.15-0.25 'Monte Carlo' calibration", r"0\.15[-–]0\.25"),
    ("94% system stability", r"94% (system )?stability|stability.{0,20}94%"),
    ("88% work participation", r"88% work"),
]

def git(repo, *a):
    return subprocess.run(["git", "-C", repo, *a], capture_output=True, text=True).stdout

def main():
    hub, sim = sys.argv[1], sys.argv[2]
    first_engine = git(sim, "log", "--reverse", "--format=%h %ad", "--date=short", "--", "index.html", "compassionism-simulation.html").split("\n")[0]
    print(f"First simulation engine commit: {first_engine}\n")
    print("| Figure | First on the Hub | Commit | File |\n|---|---|---|---|")
    for label, rx in FIGURES:
        out = git(hub, "log", "--reverse", "-G", rx, "-E", "--format=%h %ad", "--date=short", "--name-only", "--", ".", ":(exclude)v1")
        lines = [l for l in out.split("\n") if l.strip()]
        commit = date = fname = "not found"
        if lines:
            commit, date = lines[0].split()
            fname = lines[1] if len(lines) > 1 else ""
        print(f"| {label} | {date} | `{commit}` | {fname} |")

if __name__ == "__main__":
    main()
