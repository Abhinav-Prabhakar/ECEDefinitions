#!/usr/bin/env node
/* Check derivation TeX in one artifact fragment.
   Run: node scripts/check-artifact-formulas.mjs data/artifacts/parts/<subject>.json */
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';

const root = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const require = createRequire(import.meta.url);
const katex = require(path.join(root, 'assets', 'katex', 'katex.min.js'));

const file = process.argv[2];
if (!file) {
  console.error('usage: node scripts/check-artifact-formulas.mjs <fragment.json>');
  process.exit(2);
}
const payload = JSON.parse(fs.readFileSync(file, 'utf8'));
let steps = 0;
let bad = 0;
for (const [id, a] of Object.entries(payload.artifacts || {})) {
  if (a.type !== 'derivation') continue;
  (a.steps || []).forEach((step, i) => {
    steps++;
    if (/\$|\\begin\{|\\end\{/.test(step)) {
      bad++;
      console.log(`- ${id} step ${i + 1}: delimiters/environments`);
      return;
    }
    try {
      katex.renderToString(step, {
        displayMode: false, throwOnError: true, strict: 'ignore', trust: false, output: 'html'
      });
    } catch (err) {
      bad++;
      console.log(`- ${id} step ${i + 1}: ${err.message.split('\n')[0]}`);
    }
  });
}
console.log(`derivation steps=${steps}`);
if (bad) {
  console.log(`ARTIFACT FORMULA CHECK FAILED: ${bad}`);
  process.exit(1);
}
console.log('ARTIFACT FORMULA CHECK OK');
