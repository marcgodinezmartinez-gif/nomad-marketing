#!/bin/bash
# Renderiza las versiones de «Pruébalo antes de pagar» y sus fotogramas de revisión. Es el variantes.sh de
# asi-funciona/ con otros nombres, otros instantes y SIN SONIDO: no hay mezcla, y el máster sale sin pista
# de audio (el dueño, 7-nov: «monta el vídeo ya, sin audio»).
# Escribe en <salida> (por defecto salida/ del repo):
#   nomad-pruebalo-historia-1080x1920.mp4  con la flecha hacia el adhesivo de enlace
#   nomad-pruebalo-reel-1080x1920.mp4      con «Enlace en el perfil» (reel de Instagram y TikTok)
#   nomad-pruebalo-limpia-1080x1920.mp4    sin flecha ni texto (VERSIONES="limpia")
# Los tres: 1080x1920, 30 fps, 31,1 s (todo a 1,15×), H.264, sin audio.
# Y en revision/, los PNG de comprobación: uno por escena y versión, y el cierre con las zonas seguras
# dibujadas encima.
# Uso, desde cualquier sitio: bash piezas/historias-animadas/pruebalo/variantes.sh [salida]
# Antes, las tomas: METRAJE=<carpeta> python3 -I cortar-tomas.py (o --provisional, sin grabaciones).
#
# La versión se elige con assets/version.js, que se reescribe antes de cada pasada (check, snapshot y
# render leen el mismo index.html), y al acabar vuelve a «historia», que es la versionada.
set -e
D="$(cd "$(dirname "$0")" && pwd)"
R="$(cd "$D/../../.." && pwd)"
OUT="${1:-$R/salida}"
mkdir -p "$OUT" "$D/revision"
HF="npx -y hyperframes@0.8.203"
bash "$R/piezas/historias-animadas/construir.sh" >/dev/null
ls "$D"/assets/tomas/*.mp4 >/dev/null 2>&1 || { echo "faltan las tomas: METRAJE=<carpeta> python3 -I $D/cortar-tomas.py" >&2; exit 1; }
version() { printf '// Lo escribe variantes.sh antes de cada pasada. La versionada es la historia.\nwindow.NOMAD_VERSION = "%s";\n' "$1" > "$D/assets/version.js"; }
trap 'version historia' EXIT
CHECK="$(mktemp)"
# Un instante por escena (en segundos del vídeo final), cuando ya está todo dentro; y dos del arranque:
# el logo entero y el hilo dibujando el borde.
ESCENAS="0.30:00-el-logo 2.40:00b-el-hilo 5.20:01a-el-asistente 6.60:01b-la-hoja 10.60:02-tus-dias 13.90:03-el-paseo 17.30:04-el-museo 20.50:05-nomad-ai 25.20:06-un-solo-pago 30.80:07-el-cierre"
for V in ${VERSIONES:-historia reel}; do
  version "$V"
  ( cd "$D" && $HF check --at-transitions 2>&1 | sed 's/\x1b\[[0-9;]*m//g' | grep -E "Check (passed|failed)|✗|⚠|WCAG" ) | tee "$CHECK"
  grep -q "Check passed" "$CHECK" || { echo "check no pasa en $V" >&2; exit 1; }
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
  python3 - "$D/revision/$V-07-el-cierre.png" "$D/revision/$V-07-el-cierre-zonas.png" "$V" <<'PY'
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
  # Sin pista de audio: si el render pusiera una (muda), se quita sin recodificar el vídeo.
  ffmpeg -v error -y -i "$OUT/.render-$V.mp4" -map 0:v:0 -an -c:v copy -movflags +faststart "$OUT/nomad-pruebalo-$V-1080x1920.mp4"
  rm -f "$OUT/.render-$V.mp4"
  ( cd "$D" && $HF clean >/dev/null 2>&1 || true )
  echo "$OUT/nomad-pruebalo-$V-1080x1920.mp4"
done
rm -f "$CHECK"
