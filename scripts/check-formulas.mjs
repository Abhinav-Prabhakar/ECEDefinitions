#!/usr/bin/env node
/* Validate every stored formula against the vendored KaTeX build.
   Run: node scripts/check-formulas.mjs
   The data files carry bare inline TeX; this catches a bad backslash,
   an unsupported command or a stray dollar sign before it reaches a lesson. */
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';

const root = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const require = createRequire(import.meta.url);
const katex = require(path.join(root, 'assets', 'katex', 'katex.min.js'));

const files = [];
function walk(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.name.startsWith('.')) continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) walk(full);
    else if (entry.name.endsWith('.json')) files.push(full);
  }
}
walk(path.join(root, 'data', 'subjects'));

let formulas = 0;
let bad = 0;
const problems = [];
for (const file of files) {
  const payload = JSON.parse(fs.readFileSync(file, 'utf8'));
  for (const def of payload.definitions || []) {
    if (!def.formula) continue;
    formulas++;
    if (/\$|\\begin\{|\\end\{/.test(def.formula)) {
      bad++;
      problems.push(`${path.relative(root, file)} · ${def.term}: delimiters/environments in formula`);
      continue;
    }
    try {
      katex.renderToString(def.formula, {
        displayMode: false,
        throwOnError: true,
        strict: 'ignore',
        trust: false,
        output: 'html'
      });
    } catch (err) {
      bad++;
      problems.push(`${path.relative(root, file)} · ${def.term}: ${err.message.split('\n')[0]}`);
    }
  }
}

console.log(`formulas=${formulas} subjects=${files.length}`);
if (bad) {
  console.log(`FORMULA CHECK FAILED: ${bad} problem(s)`);
  for (const p of problems) console.log(' -', p);
  process.exit(1);
}
console.log('FORMULA CHECK OK');
