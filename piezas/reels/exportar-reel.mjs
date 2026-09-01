import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--no-sandbox'] });
for (let i = 1; i <= 5; i++) {
  const n = `reel-0${i}`;
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  await p.goto('file://' + process.cwd() + `/${n}.dc.html`, { waitUntil: 'load' });
  await p.waitForTimeout(900);
  await p.screenshot({ path: `${n}.png` });
  await p.close();
  console.log('exportada', n);
}
await b.close();
