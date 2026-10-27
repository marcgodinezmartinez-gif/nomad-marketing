#!/bin/bash
# Cambia la velocidad de todo el vídeo (voz, música y dibujo) en los tres sitios que la llevan:
# VELOCIDAD y las dos data-duration de index.html, VEL y DUR de mezclar.sh, y los instantes de
# revisión de variantes.sh. Después: bash mezclar.sh && bash variantes.sh.
# Uso: bash velocidad.sh 1.15
set -e
cd "$(dirname "$0")"
python3 - "$1" <<'PY'
import re, sys
v = float(sys.argv[1])
frames = round(1168 / v)          # 1168 fotogramas a 1× (MAPA en index.html)
dur = f"{frames / 30:.4f}".rstrip('0').rstrip('.')
def cambia(fich, pat, nuevo, n):
    s = open(fich, encoding='utf-8').read()
    s2, k = re.subn(pat, nuevo, s)
    if k != n: sys.exit(f'{fich}: {pat} aparece {k} veces, no {n}')
    open(fich, 'w', encoding='utf-8').write(s2)
cambia('index.html', r'var VELOCIDAD = [0-9.]+;', f'var VELOCIDAD = {v};', 1)
cambia('index.html', r'data-duration="[0-9.]+"', f'data-duration="{dur}"', 2)
cambia('mezclar.sh', r'(?m)^VEL=[0-9.]+$', f'VEL={v}', 1)
cambia('mezclar.sh', r'(?m)^DUR=[0-9.]+$', f'DUR={dur}', 1)
# Un instante por escena, a 1×: cuando ya está todo dentro.
A1 = [(0.00, '0-el-logo'), (2.30, '0-el-logo-y-la-linea'), (7.65, '1-tu-eliges'), (12.05, '2-el-plan'),
      (16.15, '3-paseos-y-museos'), (20.85, '4-sin-cobertura'), (25.25, '5-cuatro-voces'), (28.55, '6-los-gastos'),
      (33.40, '7-lugares'), (38.00, '8-el-cierre')]
esc = ' '.join(f'{t / v:.2f}:{n}' for t, n in A1)
cambia('variantes.sh', r'ESCENAS="[^"]*"', f'ESCENAS="{esc}"', 1)
cambia('variantes.sh', r'30 fps, [0-9,]+ s \(todo a [0-9,]+×\)', f'30 fps, {frames / 30:.1f} s (todo a {v:g}×)'.replace('.', ','), 1)
print(f'velocidad {v}: {frames} fotogramas, {dur} s')
PY
