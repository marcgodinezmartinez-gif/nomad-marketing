#!/bin/bash
# Renderiza «Tu primer viaje, gratis» y sus fotogramas de revisión. Es el variantes.sh de ../puente-viena/
# con otras versiones. Escribe en <salida> (por defecto salida/ del repo):
#   nomad-primer-viaje-gratis-reel-1080x1920.mp4             con «Enlace en el perfil», voz y música
#   nomad-primer-viaje-gratis-reel-sin-musica-1080x1920.mp4  el mismo, con la voz y los efectos solos
#   nomad-primer-viaje-gratis-anuncio-1080x1920.mp4          sin «Enlace en el perfil» (el anuncio lleva su botón)
#   nomad-primer-viaje-gratis-portada-1080x1920.png          la tarjeta de la oferta, quieta
# Y en revision/, un PNG por escena y el cierre con las zonas seguras dibujadas.
# Antes: python3 -I preparar-voz.py && python3 -I mezclar.py
# Uso: bash piezas/historias-animadas/primer-viaje-gratis/variantes.sh [salida]
set -e
D="$(cd "$(dirname "$0")" && pwd)"
R="$(cd "$D/../../.." && pwd)"
OUT="${1:-$R/salida}"
mkdir -p "$OUT" "$D/revision"
HF="npx -y hyperframes@0.8.203"
[ -f "$D/assets/sonido.m4a" ] || { echo "falta el sonido: python3 -I mezclar.py" >&2; exit 1; }
version() { printf '// Lo escribe variantes.sh antes de cada pasada. La versionada es la del reel.\nwindow.NOMAD_VERSION = "%s";\n' "$1" > "$D/assets/version.js"; }
trap 'version reel' EXIT
CHECK="$(mktemp)"
# Un instante por escena, sacado de los cortes de assets/tiempos.json.
ESCENAS=$(python3 - "$D/assets/tiempos.json" <<'PY'
import json, sys
T = json.load(open(sys.argv[1])); c = T['cortes']; f = T['frases']
print(' '.join(f'{t:.2f}:{n}' for t, n in [
    (0.03, '00-el-fotograma-0'), (c['pivote'] - 0.15, '01-la-lista'), (c['nomad'] - 0.25, '02-estas-aqui'),
    (f['g1']['empieza'] + 2.6, '03-la-parada'), (f['g1']['acaba'] - 0.4, '04-la-historia'),
    (c['resumen'] + 0.9, '05-eso-es-nomad'), (f['k3']['palabras'][10][1] - 0.2, '06-parada-a-parada'),
    (c['oferta'] - 0.15, '07-obra-a-obra'), (c['cierre'] - 0.3, '08-la-oferta'), (c['fin'] - 0.4, '09-el-cierre')]))
PY
)
for V in ${VERSIONES:-reel anuncio}; do
  version "$V"
  ( cd "$D" && $HF check 2>&1 | sed 's/\x1b\[[0-9;]*m//g' | grep -E "Check (passed|failed)|✗|WCAG|error\(s\)" ) | tee "$CHECK"
  grep -q "Check passed" "$CHECK" || { echo "check no pasa en $V" >&2; exit 1; }
  T=$(mktemp -d)
  ( cd "$D" && $HF snapshot --no-end --at "$(echo $ESCENAS | tr ' ' '\n' | cut -d: -f1 | paste -sd,)" -o "$T" >/dev/null 2>&1 )
  i=0
  for E in $ESCENAS; do
    F=$(ls "$T"/frame-$(printf %02d $i)-at-*.png)
    python3 -c "from PIL import Image;Image.open('$F').convert('RGB').save('$D/revision/$V-${E#*:}.png',optimize=True)"
    i=$((i+1))
  done
  # Las zonas seguras de un reel encima del cierre y de la oferta: texto entre y=230 e y=1480, y la
  # columna de botones a la derecha (x>900, de y=900 a y=1480).
  for N in 08-la-oferta 09-el-cierre; do
  python3 - "$D/revision/$V-$N.png" "$D/revision/$V-$N-zonas.png" <<'PY'
import sys
from PIL import Image, ImageDraw
im = Image.open(sys.argv[1]).convert('RGBA')
capa = Image.new('RGBA', im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(capa)
rojo = (200, 40, 40, 70)
d.rectangle([0, 0, 1080, 230], fill=rojo); d.rectangle([0, 1480, 1080, 1920], fill=rojo); d.rectangle([900, 900, 1080, 1480], fill=rojo)
Image.alpha_composite(im, capa).convert('RGB').save(sys.argv[2], optimize=True)
PY
  done
  [ "$V" = reel ] && python3 -c "from PIL import Image;Image.open('$D/revision/reel-08-la-oferta.png').save('$OUT/nomad-primer-viaje-gratis-portada-1080x1920.png',optimize=True)"
  rm -rf "$T"
  ( cd "$D" && $HF render --quiet --fps 30 --video-bitrate 12M --output "$OUT/.render-$V.mp4" >/dev/null 2>&1 )
  # El sonido se vuelve a poner desde el fichero de la mezcla, sin recodificar.
  ffmpeg -v error -y -i "$OUT/.render-$V.mp4" -i "$D/assets/sonido.m4a" -map 0:v:0 -map 1:a:0 \
    -c:v copy -c:a copy -movflags +faststart "$OUT/nomad-primer-viaje-gratis-$V-1080x1920.mp4"
  echo "$OUT/nomad-primer-viaje-gratis-$V-1080x1920.mp4"
  if [ "$V" = reel ]; then
    ffmpeg -v error -y -i "$OUT/.render-$V.mp4" -i "$D/assets/sonido-sin-musica.m4a" -map 0:v:0 -map 1:a:0 \
      -c:v copy -c:a copy -movflags +faststart "$OUT/nomad-primer-viaje-gratis-reel-sin-musica-1080x1920.mp4"
    echo "$OUT/nomad-primer-viaje-gratis-reel-sin-musica-1080x1920.mp4"
  fi
  rm -f "$OUT/.render-$V.mp4"
  ( cd "$D" && $HF clean >/dev/null 2>&1 || true )
done
rm -f "$CHECK"
