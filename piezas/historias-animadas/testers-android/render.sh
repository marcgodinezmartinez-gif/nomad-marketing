#!/bin/bash
# Renderiza la historia de los testers de Android en castellano y en italiano (26-oct).
# Escribe en <salida> (por defecto salida/ del repo):
#   nomadapp-testers-android-<es|it>.mp4   1080x1920, 30 fps, 10 s, H.264 + una pista AAC en SILENCIO
#   nomadapp-testers-android-<es|it>.png   el último fotograma, por si se prefiere una tarjeta fija
# Uso, desde cualquier sitio: bash piezas/historias-animadas/testers-android/render.sh [salida]
#
# La pista de audio va en silencio a propósito (README.md, «El sonido»): el fichero cumple H.264 +
# AAC, que es lo que mejor traga cualquier subida, y no lleva música generada con IA que obligue a
# la etiqueta de IA en una pieza que pide confianza. Si el dueño quiere música, la elige en Instagram.
set -e
D="$(cd "$(dirname "$0")" && pwd)"
R="$(cd "$D/../../.." && pwd)"
OUT="${1:-$R/salida}"
mkdir -p "$OUT"
HF="npx -y hyperframes@0.8.203"
bash "$R/piezas/historias-animadas/construir.sh" >/dev/null
for L in es it; do
  python3 "$D/preparar.py" "$L"
  ( cd "$D" && $HF check 2>&1 | grep -E "Check (passed|failed)|✗|⚠ text|WCAG" )
  ( cd "$D" && $HF render --quiet --video-bitrate 10M --output "$OUT/.render-$L.mp4" >/dev/null 2>&1 )
  ffmpeg -v error -y -i "$OUT/.render-$L.mp4" -f lavfi -i anullsrc=r=48000:cl=stereo \
    -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -b:a 128k -shortest -movflags +faststart \
    "$OUT/nomadapp-testers-android-$L.mp4"
  ffmpeg -v error -y -sseof -0.1 -i "$OUT/.render-$L.mp4" -frames:v 1 -update 1 "$OUT/nomadapp-testers-android-$L.png"
  rm -f "$OUT/.render-$L.mp4"
  echo "$OUT/nomadapp-testers-android-$L.mp4"
done
# El index.html versionado es el castellano.
python3 "$D/preparar.py" es >/dev/null
