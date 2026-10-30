# Saca SILUETA, el contorno del logo que recorre el hilo del arranque (index.html, S1), de los tres trazos
# del logo que ya van en index.html (los de mobile/assets/nomad_soft_swoosh_logo.svg de la app):
#   1. los pinta a 2048 px con el Chrome sin pantalla (el de portada.sh);
#   2. cierra los huecos blancos entre los trazos (miden 22 unidades del viewBox; se cierran con 30) y
#      rellena lo de dentro, así que queda la silueta de los tres juntos;
#   3. saca el contorno con contourpy (pip install contourpy), lo suaviza y lo remuestrea cada 6 unidades;
#   4. lo hace empezar en el lado izquierdo de la coma y correr en el sentido del reloj, que es por donde
#      el hilo sale hacia arriba, sin esquina, a dibujar la pantalla.
# Imprime si coincide con el SILUETA de index.html; con --escribir, lo sustituye.
# Uso: python3 silueta-del-logo.py [--escribir]
import glob, json, os, re, subprocess, sys, tempfile
import numpy as np
from PIL import Image
from scipy import ndimage as nd
import contourpy

AQUI = os.path.dirname(os.path.abspath(__file__))
INDEX = os.path.join(AQUI, 'index.html')
K = 2.0          # píxeles por unidad del viewBox (1024 → 2048)
CIERRE = 30      # unidades: los huecos blancos miden 22
h = open(INDEX, encoding='utf-8').read()
trazos = re.findall(r'<path id="l[123]" d="([^"]+)"', h)
assert len(trazos) == 3, 'no encuentro los tres trazos del logo en index.html'

# 1. Pintarlos.
chrome = os.environ.get('CHROME') or sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))[-1]
with tempfile.TemporaryDirectory() as t:
    with open(f'{t}/logo.html', 'w') as f:
        f.write('<html><body style="margin:0;background:#fff"><svg width="2048" height="2048" viewBox="0 0 1024 1024">'
                '<g transform="translate(0,1024) scale(0.1,-0.1)" fill="#000">'
                + ''.join(f'<path d="{d}"/>' for d in trazos) + '</g></svg></body></html>')
    subprocess.run([chrome, '--headless=new', '--no-sandbox', '--hide-scrollbars', '--force-device-scale-factor=1',
                    '--window-size=2048,2248', f'--screenshot={t}/logo.png', f'file://{t}/logo.html'],
                   check=True, capture_output=True)
    m = np.array(Image.open(f'{t}/logo.png').convert('L'))[:2048, :2048] < 128

# 2. Cerrar los huecos (dilatar y erosionar CIERRE unidades) y rellenar.
r = CIERRE * K
dil = nd.distance_transform_edt(~m) <= r
sil = nd.binary_fill_holes(nd.distance_transform_edt(dil) > r)

# 3. El contorno, en unidades del viewBox (x, y con la y hacia abajo).
f = nd.gaussian_filter(sil.astype(float), 2.0)
c = max(contourpy.contour_generator(z=f, line_type='Separate').lines(0.5), key=len) / K
def remuestrea(c, paso):
    c = np.vstack([c, c[:1]])
    s = np.concatenate([[0], np.cumsum(np.hypot(*np.diff(c, axis=0).T))])
    t = np.linspace(0, s[-1], int(round(s[-1] / paso)) + 1)
    return np.stack([np.interp(t, s, c[:, 0]), np.interp(t, s, c[:, 1])], 1)[:-1]
c = remuestrea(c, 2.0)
c = np.stack([nd.gaussian_filter1d(c[:, k], 4, mode='wrap') for k in (0, 1)], 1)

# 4. Empieza en el punto más a la izquierda de la coma (y entre 330 y 480) y sube.
izq = np.where((c[:, 1] > 330) & (c[:, 1] < 480))[0]
c = np.roll(c, -izq[np.argmin(c[izq, 0])], axis=0)
if c[5, 1] > c[0, 1]:
    c = np.vstack([c[:1], c[1:][::-1]])
c = remuestrea(c, 6.0)
nueva = ' '.join('%g,%g' % (round(x, 1), round(y, 1)) for x, y in c)

vieja = re.search(r'var SILUETA = "([^"]+)";', h).group(1)
pv = np.array([[float(v) for v in q.split(',')] for q in vieja.split()])
print(f'{len(c)} puntos (index.html tiene {len(pv)})', end='')
if len(pv) == len(c):
    print(f'; la mayor diferencia con el de index.html es {np.abs(pv - np.round(c, 1)).max():.1f} unidades')
else:
    print()
if '--escribir' in sys.argv:
    open(INDEX, 'w', encoding='utf-8').write(h.replace(vieja, nueva))
    print('escrito en index.html')
