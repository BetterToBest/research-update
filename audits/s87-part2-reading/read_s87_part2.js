// Build the reading packet for the later sections of us-money-history.html (S87 items 4-8) and
// write the request for a model on NVIDIA's API catalogue.
// Usage: node read_s87_part2.js PATH/TO/research-hub OUTDIR MODEL
// Writes OUTDIR/packet.txt (exactly what the model was given) and OUTDIR/request.json; then
//   curl -s https://integrate.api.nvidia.com/v1/chat/completions -H 'Content-Type: application/json' -d @request.json > response.json
// (the session's proxy adds the key).
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
(async () => {
  const [hub, out, model] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({viewport: {width: 1100, height: 900}});
  await p.goto('file://' + path.join(hub, 'us-money-history.html'));
  await p.waitForTimeout(500);
  await p.evaluate(() => document.querySelectorAll('details').forEach(d => { d.open = true; }));
  const text = await p.evaluate(() => ['crypto', 'offshore', 'college', 'media', 'changes', 'limits']
    .map(id => document.getElementById(id).innerText).join('\n\n'));
  await b.close();
  const src = fs.readFileSync(path.join(hub, 'data/s87/SOURCES.md'), 'utf8');
  const part2 = src.slice(src.indexOf('## Part 2'));
  const prompt = [
    'You are an independent reviewer of sections of a public web page of descriptive US economic history. The sections were drafted by another AI model from sources it opened.',
    'Read them as a careful economic historian, lawyer and fact-checker. Report, as a numbered list:',
    '1. Any statement of fact (a date, amount, name, law, court decision, or what a law did) that you believe is wrong or imprecise, with what you believe is correct and how sure you are.',
    '2. Any arithmetic, unit or method error (volatility, largest fall, tax as a share of profits, ratios).',
    '3. Any wording that is not neutral, overstates what the sources show, implies a cause the page does not test, or treats any person or company unfairly. The page covers living people and a sitting President: say if anything there goes beyond what the cited sources state.',
    '4. Anything important a reader would need that is missing, or any count or measure presented without its definition.',
    'Say plainly when you have no objection. Do not invent sources; if you are unsure, say so. You cannot open links; judge from your own knowledge and the text below.',
    '', '=== SECTIONS (rendered text, tables opened) ===', text,
    '', '=== SOURCES FILE (part 2) ===', part2,
  ].join('\n');
  fs.mkdirSync(out, {recursive: true});
  fs.writeFileSync(path.join(out, 'packet.txt'), prompt);
  fs.writeFileSync(path.join(out, 'request.json'), JSON.stringify({model, messages: [{role: 'user', content: prompt}], temperature: 0.2, max_tokens: 20000}));
  console.log('packet chars', prompt.length);
})();
