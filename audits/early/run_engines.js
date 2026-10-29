#!/usr/bin/env node
/* Run the Compassionism Simulation engines that predate v4.20, headless (step S30, item 3).

Usage: node audits/early/run_engines.js <compassionism-simulation checkout> <engines.txt> <seeds> <out.jsonl>

engines.txt lists one engine per line: "<commit> <label>". For each engine the page at that commit
(index.html, or compassionism-simulation.html before the rename) is loaded in headless Chromium with
outside scripts blocked and Chart.js replaced by a stub (the charts are not needed). The Full
Integration preset is applied ('optimal' before v3.5, 'reference' after), the run is started from the
page's own Run button, and when the run finishes every KPI tile (ids "kpi-*" before v3.3, "k-*" after)
is read as displayed, with any script errors the page raised. Nothing in the engine is changed.

Seeds: from v3.3 the page has its own seeded generator (Mulberry32) and a seed box (#s-seed); the seed
is typed there. Before v3.3 the engine calls Math.random directly and cannot be seeded, so this script
replaces Math.random with Mulberry32(seed) before the page loads: the same draws the page would make,
only reproducible. One JSON line per run is appended to out.jsonl as it finishes, so an interrupted
run resumes where it stopped. Seeds are given as "1-100" or "1,2,5".
*/
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path'), { execSync } = require('child_process');

const [repo, enginesFile, seedsArg, outFile] = process.argv.slice(2);
const TIMEOUT = +(process.env.RUN_TIMEOUT_MS || 180000);
const seeds = seedsArg.includes('-') ? (([a, b]) => Array.from({ length: b - a + 1 }, (_, i) => a + i))(seedsArg.split('-').map(Number)) : seedsArg.split(',').map(Number);
const engines = fs.readFileSync(enginesFile, 'utf8').trim().split('\n').filter(l => l && !l.startsWith('#')).map(l => { const [c, ...r] = l.trim().split(/\s+/); return { commit: c, label: r.join(' ') }; });

const done = new Set();
if (fs.existsSync(outFile)) for (const l of fs.readFileSync(outFile, 'utf8').split('\n')) { if (!l.trim()) continue; const r = JSON.parse(l); done.add(r.commit + ',' + r.seed); }

const CHART_STUB = `window.tailwind = { config: {} };
  window.Chart = class { constructor(ctx, cfg){ this.config = cfg || {}; this.data = (cfg && cfg.data) || { labels: [], datasets: [] }; this.options = (cfg && cfg.options) || {}; } destroy(){} update(){} resize(){} reset(){} static register(){} };
  window.Chart.defaults = { font:{}, plugins:{ legend:{ labels:{} }, tooltip:{} }, scale:{ grid:{} }, color:'' };`;
const MULBERRY = s => `(function(){ var a = ${s} >>> 0; Math.random = function(){ a |= 0; a = a + 0x6D2B79F5 | 0; var t = Math.imul(a ^ a >>> 15, 1 | a); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; })();`;

function pageAt(commit) {
  const dir = path.join(require('os').tmpdir(), 's30-engines'); fs.mkdirSync(dir, { recursive: true });
  const f = path.join(dir, commit + '.html');
  if (!fs.existsSync(f)) {
    let html;
    try { html = execSync(`git -C ${repo} show ${commit}:index.html`, { maxBuffer: 1 << 28 }); }
    catch (e) { html = execSync(`git -C ${repo} show ${commit}:compassionism-simulation.html`, { maxBuffer: 1 << 28 }); }
    fs.writeFileSync(f, html);
  }
  return 'file://' + f;
}

async function runOne(browser, eng, seed) {
  const ctx = await browser.newContext();
  await ctx.route(/^https?:/, r => r.abort());
  const page = await ctx.newPage();
  await page.addInitScript(CHART_STUB + MULBERRY(seed));
  page.on('dialog', d => d.dismiss().catch(() => {}));
  const errors = [];
  page.on('pageerror', e => errors.push(String(e.message).split('\n')[0]));
  const t0 = Date.now();
  try {
    await page.goto(pageAt(eng.commit), { waitUntil: 'load', timeout: 60000 });
    // some versions run seed 42 by themselves on load: let that finish first
    await page.waitForTimeout(600);
    await page.waitForFunction(() => !((typeof running !== 'undefined' && running) || (typeof simRunning !== 'undefined' && simRunning)), null, { timeout: TIMEOUT, polling: 250 });
    const info = await page.evaluate((seed) => {
      const out = {};
      for (const e of document.querySelectorAll('[id^="kpi-"],[id^="k-"]')) if (!/-label$/.test(e.id)) e.textContent = '—';
      const btns = [...document.querySelectorAll('button,[onclick]')];
      const preset = btns.find(b => /applyPreset\('(optimal|reference)'\)/.test(b.getAttribute('onclick') || ''));
      if (preset) { preset.click(); out.preset = (preset.getAttribute('onclick').match(/'(\w+)'/) || [])[1]; }
      const sb = document.getElementById('s-seed');
      if (sb) { sb.value = String(seed); sb.dispatchEvent(new Event('input')); out.seedBox = true; }
      const run = document.getElementById('run-btn') || btns.find(b => /^run[A-Za-z]*\(/.test(b.getAttribute('onclick') || '') && !/Multi|OAT|LHS|Validation|Shock|Explorer/.test(b.getAttribute('onclick')));
      out.run = run ? (run.getAttribute('onclick') || run.id) : null;
      if (run) run.click();
      return out;
    }, seed);
    if (!info.run) throw new Error('no run button');
    // finished when the page's own running flag (if any) is false and a KPI tile shows a value
    await page.waitForFunction(() => {
      const busy = (typeof running !== 'undefined' && running) || (typeof simRunning !== 'undefined' && simRunning);
      const rb = document.getElementById('run-btn');
      const k = [...document.querySelectorAll('[id^="kpi-"],[id^="k-"]')].filter(e => !/-d$|-label$/.test(e.id) && /\d/.test(e.textContent));
      return !busy && (!rb || !rb.disabled) && k.length > 0;
    }, null, { timeout: TIMEOUT, polling: 250 });
    await page.waitForTimeout(300);
    const kpis = await page.evaluate(() => {
      const o = {};
      for (const e of document.querySelectorAll('[id^="kpi-"],[id^="k-"]')) if (!/-label$/.test(e.id)) o[e.id] = e.textContent.replace(/\s+/g, ' ').trim();
      return o;
    });
    kpis._preset = info.preset || 'default'; kpis._seeded = info.seedBox ? 'page seed' : 'Math.random seeded';
    return { status: 'ok', secs: (Date.now() - t0) / 1000, kpis, errors };
  } catch (e) {
    return { status: 'error: ' + String(e.message).split('\n')[0], secs: (Date.now() - t0) / 1000, kpis: {}, errors };
  } finally { await ctx.close(); }
}

(async () => {
  const browser = await chromium.launch();
  for (const eng of engines) for (const seed of seeds) {
    if (done.has(eng.commit + ',' + seed)) continue;
    const r = await runOne(browser, eng, seed);
    fs.appendFileSync(outFile, JSON.stringify({ commit: eng.commit, label: eng.label, seed, status: r.status, secs: +r.secs.toFixed(1), kpis: r.kpis, errors: [...new Set(r.errors)].slice(0, 5) }) + '\n');
    process.stdout.write(`${eng.commit} ${eng.label} seed ${seed}: ${r.status} ${r.secs.toFixed(1)}s\n`);
  }
  await browser.close();
})();
