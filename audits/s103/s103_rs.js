#!/usr/bin/env node
/* S103: what the capacity price rule's recession-slack reading (pr.rs) does on each row's own supply path. Rows as the price-rule study's
 * (frozen yardstick, CPS earnings, today's safety net, the full-coverage design): today's rule; the nesting point (k 1, r a h 0) with rs false and
 * with rs counted; the main values with rs counted (the default) and with rs false. Run on an engine with the store keyed on the price rule
 * (v5.9.22 or later, or an older engine with S103_FIX=1), each row's path is its own. Usage: node s103_rs.js ENGINE_DIR ENV SEEDS OUT */
const fs = require('fs'), path = require('path');
const [ED, env, NS, OUT] = process.argv.slice(2), N = +NS;
const H = require(path.join(path.resolve(ED), 'harness.js'));
const NAME = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', st: 'STRESS_TEST'}[env];
const svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G), Y = {sn: {abawd: true, slope: true}, lt: {s: 'all', m: 'all'}};
const NEST = {k: 1, r: 0, a: 0, h: 0};
const ROWS = [['np', 0], ['c22', 2], ['nest-rs0', 2, Object.assign({rs: false}, NEST)], ['nest-rs1', 2, Object.assign({}, NEST)], ['cap-rs1', 2, true], ['cap-rs0', 2, {rs: false}]];
const K = ['endoAnn', 'pLev20', 'pov', 'fgt0PY', 'medWealthReal', 'hhCostPY', 'prSlk', 'prH', 'prX'];
const out = {_meta: {what: 'S103: pr.rs on its own path', env, seeds: N, engine: ED, fix: process.env.S103_FIX || 'native', rows: ROWS.map(r => r[0])}, rows: {}};
try {
  const P = Object.assign({}, H[NAME], {years: 20}), PR = H.tbPresets(P), so = Object.assign({fin: 'tax', aT: 0, a: 0, X: 0, sc: H.SPEND_SOURCED, mf: true}, H.REL_V52_STUDY);
  const mk = r => { const c = H.frozenRow(Object.assign(H.relMainCfgs(PR)[r[1] ? 1 : 0], JSON.parse(JSON.stringify(Y)), r[2] ? {pr: JSON.parse(JSON.stringify(r[2]))} : {})); return r[1] === 2 ? H.c22Design(c) : c; };
  const R = H.tbStudy(ROWS.map(mk), N, P, so);
  ROWS.forEach((r, i) => { out.rows[r[0]] = {}; K.forEach(k => { if (R[i]._s[k]) out.rows[r[0]][k] = Array.from(R[i]._s[k]); }); });
} finally { H.resetNR6(svN); H.tbSetG(svG); }
fs.writeFileSync(OUT, JSON.stringify(out));
