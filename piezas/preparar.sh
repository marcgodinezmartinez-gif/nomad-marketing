#!/bin/bash
# Monta salida/ — el directorio de trabajo que los generadores esperan como cwd — con lo
# que hasta el 1-sep vivía en el scratchpad de una sesión y moría con ella: el HELMET de
# fuentes, las fotos del banco, las capturas, la marca y la tarjeta QR.
#
# Los generadores no saben de este repo a propósito: leen 'Main.dc.html', 'fotos/x.jpg',
# 'plan-900.webp' o 'mark.png' de donde estén, y así se ejecutan igual desde aquí que
# desde cualquier otro sitio. Uso, desde la raíz del repo:
#   bash piezas/preparar.sh && cd salida && python3 ../piezas/destacadas/gen-destacadas.py
set -e
R="$(cd "$(dirname "$0")/.." && pwd)"
mkdir -p "$R/salida/fotos"
cp "$R"/banco/fuentes/Main.dc.html "$R"/salida/
cp "$R"/banco/fotos/post/f-*.jpg "$R"/salida/fotos/
cp "$R"/banco/capturas/*.webp "$R"/banco/marca/*.png "$R"/banco/qr/tarjeta-qr-*.png "$R"/salida/
[ -x "$R/node_modules/ffmpeg-static/ffmpeg" ] || echo "aviso: falta ffmpeg — npm install en la raíz (11 s) antes de montar un reel"
echo "salida/ lista"
