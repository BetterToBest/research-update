#!/usr/bin/env node
/* S103: the recession's idle share (prSlk) on the full-coverage design under the capacity rule's main values, Adverse, seed 39, one row alone in a
 * fresh process (so its supply path is its own on any engine). Usage: node rs39.js ENGINE_DIR */
const path = require('path'), H = require(path.join(path.resolve(process.argv[2]), 'harness.js'));
const svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G), Y = {sn: {abawd: true, slope: true}, lt: {s: 'all', m: 'all'}};
try { const P = Object.assign({}, H.ADVERSE_REFERENCE, {years: 20}), PR = H.tbPresets(P), so = Object.assign({fin: 'tax', aT: 0, a: 0, X: 0, sc: H.SPEND_SOURCED, mf: true}, H.REL_V52_STUDY);
  const c = H.c22Design(H.frozenRow(Object.assign(H.relMainCfgs(PR)[1], JSON.parse(JSON.stringify(Y)), {pr: true}))); if (process.env.VAT) c.sp = Object.assign({}, c.sp === true ? {} : (c.sp || {}), {vAt: process.env.VAT});
  const r = H.tbStudy([c], 39, P, so, 39)[0]; console.log('prSlk', r.prSlk, 'pLev20', r.pLev20);
} finally { H.resetNR6(svN); H.tbSetG(svG); }
