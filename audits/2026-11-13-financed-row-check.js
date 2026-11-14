#!/usr/bin/env node
/* Nov 13, 2026 audit (audits/2026-11-13-simulation-audit.md, finding 1): what the C2.2 design paid for by a flat contribution on wages
 * (ledger D21) needs, and what happens to the part of its cost the contribution does not cover.
 * Analysis only: no engine change is committed. The frozen row (frozenRow, today's safety net, CPS earnings), round-2 switches off,
 * 500 adults, 20 years. Rows: no programme; C2.2 paid by the Source (the frozen batch's row); C2.2 with o.fin 'tax' (the flat contribution).
 * With --gap, a temporary copy of the engine counts the cost the capped contribution does not raise as new money, as the engine already does
 * for the progressive and land-value taxes (index.html, the line `else if (o.fin === 'tax') U = extra + (o.taxBase ? ... : 0)`).
 * Usage: node audits/2026-11-13-financed-row-check.js SIM_DIR [ENV] [SEEDS] [--gap]
 *        SIM_DIR a compassionism-simulation checkout (checked at 3f8ae15); ENV FULL_INTEGRATION | ADVERSE_REFERENCE | STRESS_TEST; SEEDS default 10 */
const fs = require('fs'), os = require('os'), path = require('path'), cp = require('child_process');
const A = process.argv.slice(2).filter(a => !/^--/.test(a)), GAP = process.argv.indexOf('--gap') >= 0;
let dir = path.resolve(A[0] || '.');
const env = A[1] || 'FULL_INTEGRATION', N = +(A[2] || 10);
if (GAP) {
  const t = fs.mkdtempSync(path.join(os.tmpdir(), 'finrow-'));
  cp.execSync('cp -r ' + JSON.stringify(dir + '/.') + ' ' + JSON.stringify(t));
  const f = path.join(t, 'index.html'), s = fs.readFileSync(f, 'utf8');
  const old = "else if (o.fin === 'tax') U = extra + (o.taxBase ? Math.max(0, need - C.tax) : 0);";
  if (s.split(old).length !== 2) throw new Error('engine line not found exactly once: the engine has changed since 3f8ae15');
  fs.writeFileSync(f, s.replace(old, "else if (o.fin === 'tax') U = extra + Math.max(0, need - C.tax);"));
  dir = t;
}
const H = require(path.join(dir, 'harness.js'));
const svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G);
try {
  const P = Object.assign({}, H[env], {years: 20, nAgents: 500});
  const so = Object.assign({fin: 'tax', aT: 0, a: 0, X: 0, sc: H.SPEND_SOURCED}, H.REL_V52_STUDY);
  const pair = () => H.relMainCfgs(H.tbPresets(P)).map(c => { c.sc = H.SPEND_SOURCED; c.sn = {abawd: true, slope: true}; c.lt = {s: 'all', m: 'all'}; return H.frozenRow(c); });
  const src = H.c22Design(pair()[1]), flat = H.c22Design(pair()[1]); flat.o = Object.assign({}, flat.o, {fin: 'tax'});
  const R = H.tbStudy([pair()[0], src, flat], N, P, so);
  const ks = ['need', 'tax', 'treas', 'tauMean', 'tauLast', 'endoAnn', 'fgt0PY', 'pov', 'hrs', 'cBU', 'cConv'];
  console.log('env ' + env + ', seeds 1-' + N + (GAP ? ', uncovered cost counted as new money' : ', engine as committed'));
  [['no programme', 0], ['C2.2, Source', 1], ['C2.2, flat contribution', 2]].forEach(([l, i]) =>
    console.log(l.padEnd(26) + ks.map(k => k + ' ' + (R[i][k] === undefined ? '-' : (+R[i][k]).toPrecision(4))).join('  ')));
  const r = R[2];
  console.log('flat contribution: uncovered share of cost ' + (-r.treas / r.need * 100).toFixed(1) + '%; year-20 rate at the 0.90 cap in ' +
    Array.from(r._s.tauLast).filter(v => v >= 0.8999).length + ' of ' + N + ' seeds');
} finally { H.resetNR6(svN); H.tbSetG(svG); }
