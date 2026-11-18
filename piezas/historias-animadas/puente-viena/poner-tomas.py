# Escribe en index.html los <video> de las tomas, entre las marcas «TOMAS», desde tomas.json: así los
# tiempos de la página y los del corte no se pueden desacompasar. data-start es el inicio de la toma en
# segundos del vídeo final (inicio a 1× entre 1,15), y data-duration lo que se ve.
# Uso: python3 -I poner-tomas.py
import json, os, re
D = os.path.dirname(os.path.abspath(__file__))
VELOCIDAD = 1.15
tomas = json.load(open(os.path.join(D, 'tomas.json'), encoding='utf-8'))
lineas = ''.join(
    f'        <video id="v-{t["id"]}" class="clip" src="assets/tomas/{t["id"]}.mp4" data-start="{t["inicio"] / VELOCIDAD:.3f}" '
    f'data-duration="{(t["fin"] - t["inicio"]) / VELOCIDAD:.3f}" muted playsinline></video>\n' for t in tomas)
p = os.path.join(D, 'index.html')
h = open(p, encoding='utf-8').read()
h2, n = re.subn(r'(        <!-- TOMAS:[^\n]*-->\n).*?(        <!-- /TOMAS -->\n)', lambda m: m.group(1) + lineas + m.group(2), h, count=1, flags=re.S)
assert n == 1, 'no encuentro las marcas de TOMAS en index.html'
open(p, 'w', encoding='utf-8').write(h2)
print(len(tomas), 'tomas escritas en index.html')
