"""S103: reporting-only instrumentation of an old engine's supply-path store.
S103_FIX=1 adds the v5.9.22 key (rowKeyS93's settings) to the store's keys; unset, the engine computes exactly as before.
S103_LOG=FILE logs, without S103_FIX, every lookup that takes a path stored under the same old key but different settings."""
import sys, re
p = sys.argv[1]; s = open(p).read()
def once(a, b):
    global s
    assert s.count(a) == 1, (a, s.count(a)); s = s.replace(a, b)
once("var S3_CACHE = {};\n", """var S3_CACHE = {};
var S103_FIX = process.env.S103_FIX === '1', S103_LOG = process.env.S103_LOG || null, S103_SEEN = {}, S103_ROW = -1, S103_CALL = 0;
function s103Suffix(){ var x = {};
  if (typeof EARN_HH !== 'undefined' && EARN_HH) x.eh = EARN_HH; if (typeof PRICE_RULE !== 'undefined' && (PRICE_RULE !== 'qt' || PR_OPTS)) x.pr = [PRICE_RULE, PR_OPTS];
  if (typeof BARGAIN !== 'undefined' && BARGAIN) x.bg = BARGAIN; if (typeof GOV !== 'undefined' && GOV) x.gv = GOV; if (typeof PTF_OPS !== 'undefined' && PTF_OPS) x.po = PTF_OPS;
  return Object.keys(x).length ? '|s93' + JSON.stringify(x) : ''; }
function s103Key(k, where, seed){ var x = s103Suffix();
  if (S103_LOG && !S103_FIX){ if (!(k in S103_SEEN)) S103_SEEN[k] = x;
    else if (S103_SEEN[k] !== x) require('fs').appendFileSync(S103_LOG, JSON.stringify({w:where, call:S103_CALL, row:S103_ROW, seed:seed, stored:S103_SEEN[k], own:x}) + '\\n'); }
  return S103_FIX ? k + x : k; }
""")
once("  if (!S3_CACHE[k]) S3_CACHE[k] = priceRun", "  k = s103Key(k, 's3', seed); if (!S3_CACHE[k]) S3_CACHE[k] = priceRun")
once("  if (S3_CACHE[k]) return S3_CACHE[k];", "  k = s103Key(k, 'tb', seed); if (S3_CACHE[k]) return S3_CACHE[k];")
once("function tbStudy(cfgs, N, envP, o0, lo){\n", "function tbStudy(cfgs, N, envP, o0, lo){ S103_CALL++;\n")
once("cfgs.forEach(function(c, i){ var lw0 = lwSet(c.lw);", "cfgs.forEach(function(c, i){ S103_ROW = i; var lw0 = lwSet(c.lw);")
open(p, 'w').write(s)
