#!/bin/bash
# Renderiza las versiones de «Un trazo», versión 2 (27-oct, con los arreglos de la revisión), y sus
# fotogramas de revisión.
# Escribe en <salida> (por defecto salida/ del repo):
#   nomad-trazo-historia-1080x1920.mp4  con la flecha hacia el adhesivo de enlace
#   nomad-trazo-reel-1080x1920.mp4      con «Enlace en el perfil» (reel de Instagram y TikTok)
# Los dos: 1080x1920, 30 fps, 25,8 s, H.264 + AAC, la música dentro.
# Y en revision/, los PNG de comprobación: uno por escena y versión, y el cierre con las zonas
# seguras dibujadas encima.
# Uso, desde cualquier sitio: bash piezas/historias-animadas/lanzamiento-trazo/variantes.sh [salida]
#
# La versión se elige con assets/version.js, que se reescribe antes de cada pasada (check,
# snapshot y render leen el mismo index.html), y al acabar vuelve a «historia», que es la
# versionada. Hay una tercera, sin flecha ni texto, para una historia promocionada o un anuncio
# (README.md): no se renderiza por defecto; `VERSIONES="limpia" bash variantes.sh`.
set -e
D="$(cd "$(dirname "$0")" && pwd)"
R="$(cd "$D/../../.." && pwd)"
OUT="${1:-$R/salida}"
mkdir -p "$OUT" "$D/revision"
HF="npx -y hyperframes@0.8.203"
bash "$R/piezas/historias-animadas/construir.sh" >/dev/null
[ -f "$D/assets/sonido.m4a" ] || bash "$D/mezclar.sh"
version() { printf '// Lo escribe variantes.sh antes de cada pasada. La versionada es la historia.\nwindow.NOMAD_VERSION = "%s";\n' "$1" > "$D/assets/version.js"; }
trap 'version historia' EXIT
# Un instante por escena: cuando ya está todo dentro y nada se mueve.
ESCENAS="0.00:0-el-logo 1.80:0-el-logo-y-la-linea 4.30:1-tu-eliges 7.40:2-el-plan 9.70:3-paseos-y-museos 13.00:4-sin-cobertura 15.55:5-cuatro-voces 18.05:6-los-gastos 21.15:7-lugares 24.50:8-el-cierre"
for V in ${VERSIONES:-historia reel}; do
  version "$V"
  ( cd "$D" && $HF check --at-transitions 2>&1 | sed 's/\x1b\[[0-9;]*m//g' | grep -E "Check (passed|failed)|✗|⚠|WCAG" ) | tee /tmp/trazo-check.txt
  grep -q "Check passed" /tmp/trazo-check.txt || { echo "check no pasa en $V" >&2; exit 1; }
  T=$(mktemp -d)
  ( cd "$D" && $HF snapshot --no-end --at "$(echo $ESCENAS | tr ' ' '\n' | cut -d: -f1 | paste -sd,)" -o "$T" >/dev/null 2>&1 )
  i=0
  for E in $ESCENAS; do
    F=$(ls "$T"/frame-$(printf %02d $i)-at-*.png)
    python3 -c "from PIL import Image;Image.open('$F').convert('RGB').save('$D/revision/$V-${E#*:}.png',optimize=True)"
    i=$((i+1))
  done
  # El cierre con las zonas seguras encima (AGENTS.md): historia, texto entre 280 y 1500 y el
  # adhesivo de 1520 para abajo; reel, entre 230 y 1480, y la columna de botones a la derecha.
  python3 - "$D/revision/$V-8-el-cierre.png" "$D/revision/$V-8-el-cierre-zonas.png" "$V" <<'PY'
import sys
from PIL import Image, ImageDraw
im = Image.open(sys.argv[1]).convert('RGBA'); v = sys.argv[3]
capa = Image.new('RGBA', im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(capa)
rojo, azul = (200, 40, 40, 70), (30, 90, 200, 60)
if v == 'historia':
    d.rectangle([0, 0, 1080, 280], fill=rojo); d.rectangle([0, 1500, 1080, 1920], fill=rojo)
    d.rectangle([140, 1530, 940, 1690], outline=(30, 90, 200, 255), width=4, fill=azul)
    d.text((160, 1540), 'adhesivo de enlace (y 1520-1700)', fill=(30, 90, 200, 255))
else:
    d.rectangle([0, 0, 1080, 230], fill=rojo); d.rectangle([0, 1480, 1080, 1920], fill=rojo)
d.rectangle([900, 900, 1080, 1480], fill=rojo)
Image.alpha_composite(im, capa).convert('RGB').save(sys.argv[2], optimize=True)
PY
  rm -rf "$T"
  ( cd "$D" && $HF render --quiet --fps 30 --video-bitrate 12M --output "$OUT/.render-$V.mp4" >/dev/null 2>&1 )
  # El render ya lleva el sonido (el <audio> de index.html); se vuelve a poner desde sonido.m4a
  # sin recodificar, para que el máster lleve exactamente la mezcla medida.
  ffmpeg -v error -y -i "$OUT/.render-$V.mp4" -i "$D/assets/sonido.m4a" -map 0:v:0 -map 1:a:0 \
    -c:v copy -c:a copy -movflags +faststart "$OUT/nomad-trazo-$V-1080x1920.mp4"
  rm -f "$OUT/.render-$V.mp4"
  ( cd "$D" && $HF clean >/dev/null 2>&1 || true )
  echo "$OUT/nomad-trazo-$V-1080x1920.mp4"
done
