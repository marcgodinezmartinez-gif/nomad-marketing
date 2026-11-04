#!/bin/bash
# Renderiza la beta de Android (4-nov) y sus fotogramas de revisión. Es el variantes.sh de asi-funciona/
# con una sola versión: el vídeo de TikTok (sirve igual de reel de Instagram), que acaba en «Comenta
# ANDROID» y no necesita enlace.
# Escribe en <salida> (por defecto salida/ del repo):
#   nomad-beta-android-1080x1920.mp4   1080x1920, 30 fps, 21,7 s (todo a 1,15×), H.264 + AAC, voz y música dentro
# Y en revision/, un PNG por escena y el cierre con las zonas seguras de TikTok dibujadas encima.
# Uso, desde cualquier sitio: bash piezas/historias-animadas/beta-android/render.sh [salida]
# Antes, las tomas: METRAJE=<carpeta> python3 -I cortar-tomas.py tomas.json (README.md).
set -e
D="$(cd "$(dirname "$0")" && pwd)"
R="$(cd "$D/../../.." && pwd)"
OUT="${1:-$R/salida}"
mkdir -p "$OUT" "$D/revision"
HF="npx -y hyperframes@0.8.203"
bash "$R/piezas/historias-animadas/construir.sh" >/dev/null
[ -f "$D/assets/sonido.m4a" ] || bash "$D/mezclar.sh"
ls "$D"/assets/tomas/*.mp4 >/dev/null 2>&1 || { echo "faltan las tomas: METRAJE=<carpeta> python3 -I $D/cortar-tomas.py tomas.json" >&2; exit 1; }
# Un instante por escena (segundos del vídeo final), cuando ya está todo dentro.
ESCENAS="0.30:00-gancho 2.20:01-hilo 5.74:02-iphone 9.04:03-personas 12.60:04-oido 16.17:05-sello 20.43:06-cierre"
( cd "$D" && $HF check --at-transitions 2>&1 | sed 's/\x1b\[[0-9;]*m//g' | grep -E "Check (passed|failed)|✗|⚠|WCAG" ) | tee /tmp/beta-android-check.txt
grep -q "Check passed" /tmp/beta-android-check.txt || { echo "check no pasa" >&2; exit 1; }
T=$(mktemp -d)
( cd "$D" && $HF snapshot --no-end --at "$(echo $ESCENAS | tr ' ' '\n' | cut -d: -f1 | paste -sd,)" -o "$T" >/dev/null 2>&1 )
i=0
for E in $ESCENAS; do
  F=$(ls "$T"/frame-$(printf %02d $i)-at-*.png)
  python3 -c "from PIL import Image;Image.open('$F').convert('RGB').save('$D/revision/${E#*:}.png',optimize=True)"
  i=$((i+1))
done
# Las zonas que tapa TikTok, encima del cierre y de una escena: arriba las pestañas (0-230), abajo el
# texto del vídeo, el usuario y el sonido (de 1480 para abajo), y a la derecha la columna de botones.
for E in 06-cierre 03-personas; do
python3 - "$D/revision/$E.png" "$D/revision/$E-zonas.png" <<'PY'
import sys
from PIL import Image, ImageDraw
im = Image.open(sys.argv[1]).convert('RGBA')
capa = Image.new('RGBA', im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(capa)
rojo = (200, 40, 40, 70)
d.rectangle([0, 0, 1080, 230], fill=rojo); d.rectangle([0, 1480, 1080, 1920], fill=rojo)
d.rectangle([900, 900, 1080, 1480], fill=rojo)
Image.alpha_composite(im, capa).convert('RGB').save(sys.argv[2], optimize=True)
PY
done
rm -rf "$T"
( cd "$D" && $HF render --quiet --fps 30 --video-bitrate 12M --output "$OUT/.render-beta.mp4" >/dev/null 2>&1 )
# El render ya lleva el sonido (el <audio> de index.html); se vuelve a poner desde sonido.m4a sin
# recodificar, para que el máster lleve exactamente la mezcla medida.
ffmpeg -v error -y -i "$OUT/.render-beta.mp4" -i "$D/assets/sonido.m4a" -map 0:v:0 -map 1:a:0 \
  -c:v copy -c:a copy -movflags +faststart "$OUT/nomad-beta-android-1080x1920.mp4"
rm -f "$OUT/.render-beta.mp4"
( cd "$D" && $HF clean >/dev/null 2>&1 || true )
echo "$OUT/nomad-beta-android-1080x1920.mp4"
