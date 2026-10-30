#!/usr/bin/env node
/* S32 (Oct 30, 2026): design checks made before the study programme was preregistered. It prints only whether each setting runs and which settings give
 * bit-identical results (every measure, every seed); it prints no outcome value. 60 adults, seeds 1-2, so it takes seconds.
 * Run in a checkout of the engine (BetterToBest/compassionism-simulation at d33de07): node /path/to/s32_feasibility.js */
const path = require('path'), H = require(path.join(process.cwd(), 'harness.js'));
const SN = {abawd: true, slope: true}, SC = H.SPEND_SOURCED, svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G);
const so = Object.assign({fin: 'tax', aT: 0, a: 0, X: 0, sc: SC}, H.REL_V52_STUDY), ENVS = ['FULL_INTEGRATION', 'ADVERSE_REFERENCE', 'STRESS_TEST'];
const copy = x => JSON.parse(JSON.stringify(x));
function rows(env, o) { const P = Object.assign({}, H[env], {years: 20, nAgents: 60}, o || {}), PR = H.tbPresets(P); return {P, M: H.relMainCfgs(PR).map(c => Object.assign(c, {sc: SC, sn: SN}))}; }
function res(P, c) { try { return Object.entries(H.tbStudy([c], 2, P, so, 1)[0]._s).map(([k, v]) => [k, JSON.stringify(Array.from(v))]); } catch (e) { return 'ERR ' + e.message; } }
const differ = (a, b) => typeof a === 'string' || typeof b === 'string' ? ['(error)'] : a.filter((x, i) => x[1] !== b[i][1]).map(x => x[0]);
const cell = (M, b) => { const c = copy(M[1]); Object.assign(c.p, {ccoOn: b[0], ptf: b[1], pth: b[2], szh: b[3], cip: b[4]}); return c; };
const name = b => 'CFHZI'.split('').map((ch, i) => b[i] ? ch : ch.toLowerCase()).join('');
const bits = m => [16, 8, 4, 2, 1].map(x => !!(m & x));
try {
  ENVS.forEach(env => { const {P, M} = rows(env), R = {}; for (let m = 0; m < 32; m++) R[name(bits(m))] = res(P, cell(M, bits(m)));
    const none = res(P, M[0]), main = res(P, M[1]), errs = Object.keys(R).filter(k => typeof R[k] === 'string');
    const sigs = new Set(Object.values(R).map(r => JSON.stringify(r)));
    console.log(env + ': 32 architecture cells run, errors: ' + (errs.length ? errs.join(' ') : 'none') + '; distinct results: ' + sigs.size + '; all five on equals the release row: ' + (differ(R.CFHZI, main).length === 0));
    console.log('  all five off against no programme, measures that differ: ' + differ(R.cfhzi, none).join(' '));
    console.log('  SZH alone against all off, measures that differ: ' + differ(R.cfhZi, R.cfhzi).join(' '));
    const raiseOn = c => { delete c.pw; return c; }, noC = cell(M, [false, true, true, true, true]);
    console.log('  PTF, PTH, SZH, CIP without CCO: octave raise changes results: ' + (differ(res(P, noC), res(P, raiseOn(copy(noC)))).length > 0) +
      '; with the raise off, starting octaves (maxOct as preset vs 1) change results: ' + (differ(res(P, noC), res(P, Object.assign(copy(noC), {p: Object.assign(copy(noC.p), {maxOct: 1})}))).length > 0));
  });
  { const a = rows('FULL_INTEGRATION', {partRate: 0.1}), b = rows('FULL_INTEGRATION');
    console.log('Participation 10% runs: ' + (typeof res(a.P, a.M[1]) !== 'string') + '; no-programme measures that differ from 78%: ' + differ(res(a.P, a.M[0]), res(b.P, b.M[0])).join(' ')); }
  { const {P, M} = rows('FULL_INTEGRATION', {years: 40}), cps = {lt: {s: 'all', m: 'all'}, ag: {}};
    const r = [res(P, Object.assign(copy(M[0]), cps)), res(P, Object.assign(copy(M[1]), cps))];
    console.log('40 years with ageing and CPS earnings, both rows run: ' + r.every(x => typeof x !== 'string')); }
} finally { H.resetNR6(svN); H.tbSetG(svG); }
