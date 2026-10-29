#!/bin/bash
# Fotografía portada.html de este vídeo a 1080x1920 en JPEG. Chrome sin pantalla pinta menos alto que la
# ventana que se le pide (docs/tienda/capturas del repo de la app): se pide 200 px más y se recorta.
# Uso: bash portada.sh <salida.jpg>   (CHROME=… si no está en /opt/pw-browsers)
set -e
# La salida, absoluta ANTES de cambiar de carpeta (con una ruta relativa, ffmpeg escribía en la
# carpeta de la pieza y fallaba).
SALIDA="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
cd "$(dirname "$0")"
CHROME=${CHROME:-$(ls -d /opt/pw-browsers/chromium-*/chrome-linux/chrome | head -1)}
T=$(mktemp -d)
"$CHROME" --headless=new --no-sandbox --hide-scrollbars --force-device-scale-factor=1 \
  --window-size=1080,2120 --virtual-time-budget=3000 --screenshot="$T/p.png" "file://$PWD/portada.html" 2>/dev/null
ffmpeg -v error -y -i "$T/p.png" -vf crop=1080:1920:0:0 -q:v 2 "$SALIDA"
rm -rf "$T"
echo "$SALIDA"
