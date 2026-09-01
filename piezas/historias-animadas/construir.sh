#!/bin/bash
# Prepara los proyectos de HISTORIAS ANIMADAS con lo que necesitan del banco.
#
# Una historia animada es una pieza que el taller NO puede producir: el movimiento ES
# la pieza, así que no hay nada que editar a mano en el lienzo. Por eso vive aparte y
# no toca a los generadores de tarjetas.
#
# LAS FUENTES NO SALEN DEL HELMET, Y ESO TIENE UNA RAZÓN MEDIDA (1-sep).
# El HELMET de banco/fuentes/Main.dc.html embebe dos woff2 en base64 llamados
# 'Instrument Serif' e 'Instrument Sans', pero son subconjuntos que contienen
# EXACTAMENTE DOS GLIFOS CADA UNO: «A» y «Á». Medido con CDP
# (CSS.getPlatformFontsForNode) carácter a carácter sobre 83: 2/83 en las dos. Todo lo
# demás cae a la fuente del sistema — en este contenedor, Liberation Serif. En el lienzo
# no se nota porque Claude Design sirve las fuentes de su lado; al renderizar fuera, sí.
#
# Así que las historias animadas usan las fuentes REALES, bajadas de Google Fonts (OFL)
# a banco/fuentes/webfonts/ con sus unicode-range, y se embeben en base64 para que el
# render no dependa de la red (regla de determinismo de HyperFrames).
#
# gsap.min.js va versionado en assets/ por lo mismo.
# Uso: bash piezas/historias-animadas/construir.sh
set -e
R="$(cd "$(dirname "$0")/../.." && pwd)"
D="$R/piezas/historias-animadas"

for P in "$D"/*/; do
  [ -f "$P/index.html" ] || continue
  mkdir -p "$P/assets"
  python3 - "$R/banco/fuentes/webfonts" "$P/assets/fuentes.css" <<'PY'
import base64, json, os, sys
fuente, destino = sys.argv[1], sys.argv[2]
manifiesto = json.load(open(f'{fuente}/manifiesto.json'))
piezas = ['/* Generado por piezas/historias-animadas/construir.sh desde\n'
          '   banco/fuentes/webfonts/. No se edita a mano.\n'
          '   Las fuentes van embebidas: el render no puede depender de la red. */']
caras = 0
for familia, ficheros in manifiesto.items():
    for f in ficheros:
        datos = open(f'{fuente}/{f["fichero"]}', 'rb').read()
        b64 = base64.b64encode(datos).decode()
        rango = f'\n  unicode-range: {f["unicode_range"]};' if f['unicode_range'] else ''
        piezas.append(
            f"@font-face {{\n  font-family: '{familia}';\n  font-style: normal;\n"
            f"  font-weight: 100 900;\n"
            f"  src: url(data:font/woff2;base64,{b64}) format('woff2');{rango}\n}}")
        caras += 1
open(destino, 'w').write('\n'.join(piezas) + '\n')
proyecto = os.path.basename(os.path.dirname(os.path.dirname(os.path.normpath(destino))))
print(f'  {proyecto}/assets/fuentes.css — {caras} caras, '
      f'{os.path.getsize(destino)} bytes')
PY
  cp "$R/banco/marca/mark.png" "$P/assets/"
  echo "  $(basename "$P") listo"
done
