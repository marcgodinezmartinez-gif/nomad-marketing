// Pinta el vídeo fotograma a fotograma: abre index.html en Chromium, llama a seek(t) para cada
// fotograma y le pasa la captura a ffmpeg por una tubería. Es determinista: el mismo t da siempre
// la misma imagen. Sin sonido; el sonido lo pone mezclar.sh.
//
//   node render.mjs <salida.mp4> [version]         version: reel (por defecto), historia o limpia
//   node render.mjs --fotogramas <carpeta> t1 t2…   sólo esos instantes, en PNG, para revisar
//   node render.mjs --portada <salida.jpg>           la portada del reel
//
// Playwright ya está en el contenedor (require('playwright') vale desde cualquier carpeta).
import { createRequire } from 'node:module';
import { spawn } from 'node:child_process';
import { mkdirSync } from 'node:fs';
import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';

const require = createRequire(import.meta.url);
const { chromium } = require('playwright');
const aqui = path.dirname(fileURLToPath(import.meta.url));
const FPS = 30;

const args = process.argv.slice(2);
const sueltos = args[0] === '--fotogramas';
const portada = args[0] === '--portada';
const version = (sueltos || portada ? 'reel' : args[1]) || 'reel';

const navegador = await chromium.launch();
const pagina = await navegador.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
const errores = [];
pagina.on('pageerror', (e) => errores.push(String(e)));
pagina.on('console', (m) => { if (m.type() === 'error') errores.push(m.text()); });
await pagina.goto(pathToFileURL(path.join(aqui, 'index.html')).href + '?version=' + version + (portada ? '&portada=1' : ''));
await pagina.evaluate(() => window.listo);
const duracion = await pagina.evaluate(() => window.DURACION);
if (errores.length) { console.error('errores en la página:', errores); process.exit(1); }

if (portada) {
  // La portada del reel: el fotograma del gancho con la raya ya trazada y un texto que no caduca.
  await pagina.evaluate(() => window.seek(1.6));
  await pagina.screenshot({ path: args[1], type: 'jpeg', quality: 93 });
  console.log(args[1]);
  await navegador.close();
  process.exit(0);
}

if (sueltos) {
  const carpeta = args[1];
  mkdirSync(carpeta, { recursive: true });
  for (const t of args.slice(2).map(Number)) {
    await pagina.evaluate((x) => window.seek(x), t);
    const f = path.join(carpeta, `t${t.toFixed(2).padStart(5, '0')}.png`);
    await pagina.screenshot({ path: f, type: 'png' });
    console.log(f);
  }
  await navegador.close();
  process.exit(0);
}

const salida = args[0];
const total = Math.round(duracion * FPS);
const ff = spawn('ffmpeg', ['-loglevel', 'error', '-y', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', 'pipe:0',
  '-c:v', 'libx264', '-preset', 'slow', '-crf', '14', '-pix_fmt', 'yuv420p', '-vf', 'scale=in_range=full:out_range=tv,format=yuv420p',
  '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709', '-color_range', 'tv',
  '-movflags', '+faststart', '-r', String(FPS), salida], { stdio: ['pipe', 'inherit', 'inherit'] });
const acabado = new Promise((ok, mal) => ff.on('close', (c) => (c === 0 ? ok() : mal(new Error('ffmpeg salió con ' + c)))));
for (let i = 0; i < total; i++) {
  await pagina.evaluate((x) => window.seek(x), i / FPS);
  const img = await pagina.screenshot({ type: 'jpeg', quality: 96 });
  if (!ff.stdin.write(img)) await new Promise((r) => ff.stdin.once('drain', r));
  if (i % 150 === 0) console.log(`fotograma ${i} de ${total}`);
}
ff.stdin.end();
await acabado;
await navegador.close();
if (errores.length) { console.error('errores en la página:', errores); process.exit(1); }
console.log(`${salida}: ${total} fotogramas, ${duracion} s, versión ${version}`);
