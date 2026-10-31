#!/usr/bin/env node
/* S37 (Oct 31, 2026): checks of the community and zone layer made before its preregistration addendum. It prints only whether each setting runs, which
 * settings give bit-identical results (every measure, every seed), and the layer's own placement figures (communities, zones, where members live); it
 * prints no outcome value. Seeds 1-2; 60 to 400 adults, so it takes a few minutes.
 * Run in a checkout of the engine (BetterToBest/compassionism-simulation, branch claude/s37-community-layer): node /path/to/s37_layer_checks.js */
const path = require('path'), H = require(path.join(process.cwd(), 'harness.js'));
const SN = {abawd: true, slope: true}, SC = H.SPEND_SOURCED, svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G);
const so = Object.assign({fin: 'tax', aT: 0, a: 0, X: 0, sc: SC}, H.REL_V52_STUDY), ENVS = ['FULL_INTEGRATION', 'ADVERSE_REFERENCE', 'STRESS_TEST'];
const CPS = {lt: {s: 'all', m: 'all'}}, CL = new Set(H.CL_KEYS), copy = x => JSON.parse(JSON.stringify(x));
function rows(env, o) { const P = Object.assign({}, H[env], {years: 20, nAgents: 60}, o || {}), PR = H.tbPresets(P); return {P, M: H.relMainCfgs(PR).map(c => Object.assign(c, {sc: SC, sn: SN}, copy(CPS)))}; }
function study(P, c) { try { return H.tbStudy([c], 2, P, so, 1)[0]; } catch (e) { return 'ERR ' + e.message; } }
function res(P, c) { const r = study(P, c); return typeof r === 'string' ? r : Object.entries(r._s).filter(([k]) => !CL.has(k)).map(([k, v]) => [k, JSON.stringify(Array.from(v))]); }
const differ = (a, b) => typeof a === 'string' || typeof b === 'string' ? ['(error)'] : a.length !== b.length ? ['(keys)'] : a.filter((x, i) => x[1] !== b[i][1]).map(x => x[0]);
const same = (a, b) => differ(a, b).length === 0;
const cell = (M, b) => { const c = copy(M[1]); Object.assign(c.p, {ccoOn: b[0], ptf: b[1], pth: b[2], szh: b[3], cip: b[4]}); return c; };
const withCl = (c, cl) => Object.assign(copy(c), {cl: cl || {}});
const place = r => typeof r === 'string' ? r : 'communities ' + r.clN + ', zones at the start ' + r.clZ + ', members where the share is 40% or more ' + r.clHi.toFixed(0) + '%, where theta is above 0 ' + r.clTh.toFixed(0) + '%';
try {
  ENVS.forEach(env => {
    console.log(env + ':');
    { const {P, M} = rows(env);  /* 60 adults: k 100 makes one community */
      console.log('  one community (60 adults, k 100), release row, equals the layer off: ' + same(res(P, withCl(M[1])), res(P, M[1])) +
        '; no-programme row with the layer equals off: ' + same(res(P, withCl(M[0])), res(P, M[0])) +
        '; CCO alone (no PTF) with the layer, k 10, equals off: ' + same(res(P, withCl(cell(M, [true, false, true, true, true]), {k: 10})), res(P, cell(M, [true, false, true, true, true])))); }
    { const {P, M} = rows(env, {years: 40}), ag = c => Object.assign(c, {ag: {}});
      console.log('  one community, 40 years with ageing, equals off: ' + same(res(P, ag(withCl(M[1]))), res(P, ag(copy(M[1]))))); }
    { const {P, M} = rows(env, {nAgents: 400}), off = res(P, M[1]), on = study(P, withCl(M[1]));
      console.log('  400 adults, main settings (k 100, f 0.5): runs ' + (typeof on !== 'string') + ', differs from off: ' + !same(res(P, withCl(M[1])), off) + '; ' + place(on));
      console.log('    run twice, identical: ' + same(res(P, withCl(M[1])), res(P, withCl(M[1]))));
      [{k: 50}, {k: 250}, {f: 2/3}, {f: 1}, {bass: 'pop'}].forEach(o => { const r = study(P, withCl(M[1], o)); console.log('    ' + JSON.stringify(o) + ': runs ' + (typeof r !== 'string') + '; ' + place(r)); });
      const noZ = cell(M, [true, true, true, true, false]);
      console.log('    SZH and PTF on, CIP off: zones with zc false: ' + study(P, withCl(noZ)).clZ + ', with zc true: ' + study(P, withCl(noZ, {zc: true})).clZ +
        '; SZH off: ' + study(P, withCl(cell(M, [true, true, true, false, true]))).clZ); }
  });
} finally { H.resetNR6(svN); H.tbSetG(svG); }
