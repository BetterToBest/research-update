"""S103: backport of the per-run reset (added in the engine of Nov 14, between 3500d0b and df9cfbe; DECISIONS.md "The per-run reset") to an older
engine, behind S103_RESET=1: the mechanisms' per-run state (FWS, PJS, ESS, SPS, PDS, JNS, HCS) starts empty in every testbed run. Applied after patch.py."""
import sys
p = sys.argv[1]; s = open(p).read()
if 'S103_RESET' in s: sys.exit(0)
a = "  THETA_DENS = null;\n  var epD0 = housingDistressYear0(agents)"
assert s.count(a) == 1
s = s.replace(a, "  THETA_DENS = null;\n  if (S103_RESET){ FWS = null; PJS = null; ESS = null; SPS = null; PDS = null; JNS = null; HCS = null; }\n  var epD0 = housingDistressYear0(agents)")
b = "var S103_FIX = "; assert s.count(b) == 1
s = s.replace(b, "var S103_RESET = process.env.S103_RESET === '1';\nvar S103_FIX = ")
open(p, 'w').write(s)
