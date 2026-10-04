import { execSync } from 'node:child_process';
import { mkdirSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { pathToFileURL } from 'node:url';

const list = (name, fallback) => (process.env[name] || fallback).split(',').filter(Boolean);
const base = (process.env.BASE || 'http://127.0.0.1:1313').replace(/\/$/, '');
const pages = list('PAGES', '/,/fr/,/ar/,/resume/,/ar/resume/,/projects/,/projects/memorytracer/,/projects/paridata/,/ar/projects/paridata/,/tech/,/tech/windows-memory-management-deep-dive/,/tech/montreal-forecast-reliability/,/adventures/,/adventures/indian-head-rainbow-falls/,/tags/,/tags/cpp/,/search/,/fr/tech/barcode-flight/,/ar/tech/barcode-flight/,/404.html');
const viewports = list('VIEWPORTS', '320,360,390,768,1024,1440').map(v => v.includes('x') ? v.split('x').map(Number) : [Number(v), 900]);
const themes = list('THEMES', 'light,dark');
const shoot = list('SHOOT', '').map(Number);
const out = process.env.OUT || join(tmpdir(), 'ibraverse-responsive');

const { chromium } = await import('playwright').catch(() =>
  import(pathToFileURL(join(execSync('npm root -g').toString().trim(), '@playwright/cli/node_modules/playwright/index.mjs'))));
const browser = await chromium.launch({ channel: 'chrome' }).catch(() => chromium.launch());
if (shoot.length) mkdirSync(out, { recursive: true });

const failures = [], warnings = [];
for (const theme of themes) for (const [w, h] of viewports) {
  const ctx = await browser.newContext({ viewport: { width: w, height: h }, colorScheme: theme });
  await ctx.addInitScript(t => { try { localStorage.setItem('pref-theme', t); } catch {} }, theme);
  const page = await ctx.newPage();
  for (const p of pages) {
    const where = `${theme} ${w}x${h} ${p}`;
    const res = await page.goto(base + p, { waitUntil: 'load' });
    if (!res || res.status() >= 400) { failures.push(`${where}: HTTP ${res?.status()}`); continue; }
    const { overflow, small } = await page.evaluate(() => {
      const vw = document.documentElement.clientWidth, name = el => `${el.tagName.toLowerCase()}${[...el.classList].map(c => '.' + c).join('')}`;
      const overflow = [], small = [];
      if (document.documentElement.scrollWidth > vw + 1) overflow.push(`page ${document.documentElement.scrollWidth}px wide in ${vw}px`);
      for (const el of document.querySelectorAll('body *')) {
        const cs = getComputedStyle(el), b = el.getBoundingClientRect();
        if (cs.display === 'none' || cs.visibility === 'hidden' || !b.width || !b.height) continue;
        let anc = el.parentElement, clipped = false;
        for (; anc && anc !== document.body; anc = anc.parentElement) if (/auto|scroll|hidden|clip/.test(getComputedStyle(anc).overflowX)) { clipped = true; break; }
        if (!clipped && (b.right > vw + 1 || b.left < -1)) overflow.push(`${name(el)} spans ${Math.round(b.left)}–${Math.round(b.right)}px`);
        const text = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
        if (text && parseFloat(cs.fontSize) < 12) small.push(`text ${cs.fontSize} ${name(el)} "${el.textContent.trim().slice(0, 30)}"`);
        if (/^(A|BUTTON)$/.test(el.tagName) && b.width < 24 && b.height < 24) small.push(`target ${Math.round(b.width)}x${Math.round(b.height)} ${name(el)} "${(el.textContent || el.getAttribute('aria-label') || '').trim().slice(0, 20)}"`);
      }
      return { overflow: [...new Set(overflow)].slice(0, 20), small: [...new Set(small)].slice(0, 20) };
    });
    if (overflow.length) failures.push(`${where}\n  ${overflow.join('\n  ')}`);
    if (small.length) warnings.push(`${where}\n  ${small.join('\n  ')}`);
    if (shoot.includes(w)) await page.screenshot({ path: join(out, `${theme}-${w}${p.replace(/[/+.]/g, '_')}.png`), fullPage: true });
  }
  await ctx.close();
}
await browser.close();

if (warnings.length) console.log(`small text or targets (check by eye):\n${warnings.join('\n')}\n`);
if (shoot.length) console.log(`screenshots: ${out}\n`);
console.log(failures.length ? `❌ ${failures.length} failure(s):\n${failures.join('\n')}` : `✅ ${pages.length} pages × ${viewports.length} viewports × ${themes.length} themes: no overflow`);
process.exit(failures.length ? 1 : 0);
