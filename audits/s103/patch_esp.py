"""S103: reporting-only detector of the ESP pool with no wage weight (fixed in v5.9.23), applied after patch.py.
S103_ESP=FILE logs each year in which the ESP's payroll pool is positive and no ESP worker had a wage last year.
S103_ESPFIX=1 backports the v5.9.23 rule (the whole pool returned to the ESP, converted with the rest of the returned BU)."""
import sys
p = sys.argv[1]; s = open(p).read()
if 'S103_ESPLOG' in s: sys.exit(0)
def once(a, b):
    global s
    assert s.count(a) == 1, (a, s.count(a)); s = s.replace(a, b)
once("ESS.wW=esW;esA.poolPaid+=esPool/esIdx;", "ESS.wW=esW;esA.poolPaid+=esPool/esIdx;if(esPool>0&&!(esW>0)&&S103_ESPLOG)require('fs').appendFileSync(S103_ESPLOG,JSON.stringify({call:S103_CALL,row:S103_ROW,seed:S103_SEED,yr:yr,pool:esPool})+'\\n');")
once("    if(ESP.cap==='save')agentSet.forEach(function(a){esSv+=a._esSv||0;});", "    if(S103_ESPFIX&&esPool>0&&!(esW>0)){esRet+=esPool;esA.retWage+=esPool/esIdx;}\n    if(ESP.cap==='save')agentSet.forEach(function(a){esSv+=a._esSv||0;});")
once("var S103_FIX = ", "var S103_ESPLOG = process.env.S103_ESP || null, S103_ESPFIX = process.env.S103_ESPFIX === '1', S103_SEED = 0;\nvar S103_FIX = ")
once("    var S = s3BaseS(envP, sd); HL_GOVREF = {};", "    S103_SEED = sd; var S = s3BaseS(envP, sd); HL_GOVREF = {};")
open(p, 'w').write(s)
