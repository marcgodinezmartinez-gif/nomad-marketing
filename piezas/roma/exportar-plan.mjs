// Exporta las cinco tarjetas del carrusel a PNG 1080x1350.
//
// LAS FUENTES SE INYECTAN, y esa es la única diferencia con abrir el .dc.html a mano.
// Los dos woff2 del HELMET de banco/fuentes/Main.dc.html tienen DOS GLIFOS cada uno
// («A» y «Á»), medido con CDP el 1-sep: lo exportado por un script sale en la fuente del
// sistema sin avisar. En el lienzo no se nota porque Claude Design sirve las suyas.
// Aquí se inyectan las reales de banco/fuentes/webfonts (Google Fonts, OFL), en base64,
// para que el render no dependa de la red.
//
// Uso, desde salida/:  node ../piezas/roma/exportar-plan.mjs
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import { readFileSync } from 'node:fs';

const BANCO = process.cwd() + '/../banco/fuentes/webfonts';
const man = JSON.parse(readFileSync(`${BANCO}/manifiesto.json`, 'utf8'));
const css = Object.entries(man).flatMap(([familia, ficheros]) => ficheros.map((f) => {
  const b64 = readFileSync(`${BANCO}/${f.fichero}`).toString('base64');
  const rango = f.unicode_range ? `\n  unicode-range: ${f.unicode_range};` : '';
  return `@font-face { font-family: '${familia}'; font-style: normal; font-weight: 100 900;
  src: url(data:font/woff2;base64,${b64}) format('woff2');${rango} }`;
})).join('\n') + `
.serif, .serif * { font-family: 'Instrument Serif' !important; }
.sans,  .sans  * { font-family: 'Instrument Sans'  !important; }`;

const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--no-sandbox'] });
for (let i = 1; i <= 5; i++) {
  const n = `roma-${i}`;
  const p = await b.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
  await p.goto('file://' + process.cwd() + `/${n}.dc.html`, { waitUntil: 'load' });
  await p.addStyleTag({ content: css });
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(600);
  await p.screenshot({ path: `${n}.png` });
  await p.close();
  console.log('exportada', n);
}
await b.close();
