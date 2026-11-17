// Build the reading packet for us-money-history.html (S87) and send it to a model on NVIDIA's
// API catalogue. Usage: node read_s87.js PATH/TO/research-hub OUTDIR MODEL
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
  await p.waitForTimeout(400);
  await p.evaluate(() => document.querySelectorAll('details').forEach(d => { d.open = true; }));
  const text = await p.evaluate(() => document.querySelector('main').innerText);
  await b.close();
  const sources = fs.readFileSync(path.join(hub, 'data/s87/SOURCES.md'), 'utf8');
  const wage = fs.readFileSync(path.join(hub, 'data/s87/minimum-wage-silver.csv'), 'utf8');
  const prompt = [
    'You are an independent reviewer of a public web page of descriptive US economic history. The page was drafted by another AI model.',
    'Read it as a careful economic historian and fact-checker. Report, as a numbered list:',
    '1. Any statement of fact (a date, amount, law, or what a law or order did) that you believe is wrong or imprecise, with what you believe is correct and how sure you are.',
    '2. Any arithmetic or unit error in the figures (for example the silver content of coins, the conversions into ounces or hours).',
    '3. Any wording that is not neutral, overstates what the data show, or implies a cause the page does not test.',
    '4. Anything important a reader would need that is missing, especially on the advantages and disadvantages of backing money with gold or silver.',
    '5. Whether the treatment of Duke Johnson\'s figure (about 5 ounces of silver a week) is fair.',
    'Say plainly when you have no objection. Do not invent sources; if you are unsure, say so. You cannot open links; judge from your own knowledge and the text below.',
    '', '=== PAGE TEXT (rendered, tables opened) ===', text,
    '', '=== SOURCES FILE ===', sources,
    '', '=== DATA: minimum-wage-silver.csv ===', wage,
  ].join('\n');
  fs.mkdirSync(out, {recursive: true});
  fs.writeFileSync(path.join(out, 'packet.txt'), prompt);
  const body = {model, messages: [{role: 'user', content: prompt}], temperature: 0.2, max_tokens: 6000};
  fs.writeFileSync(path.join(out, 'request.json'), JSON.stringify(body));
  console.log('packet chars', prompt.length);
})();
