#!/bin/bash
# El sonido de «El puente en Viena» (18-nov): la voz de Kore encima de la música de «Un trazo», con la cadena
# de «Así funciona» (asi-funciona/mezclar.sh, donde se explica cada paso y por qué). Escribe assets/sonido.m4a.
#
# Lo que cambia aquí: los tiempos ya son los del vídeo final (los escribe tiempos.py desde voz.json), así que
# la voz se acelera a 1,15× con atempo y se coloca tal cual. La música va también a 1,15× (rubberband), y
# empieza 26 negras dentro de la pista (20,82 s) para que su último acorde (el 51,25 de la pista) caiga en el
# 26,46 del vídeo, cuando entra «Que nadie diga que no sabía».
set -e
cd "$(dirname "$0")/assets"
VEL=1.15
INICIO=20.8208
read -r _ DUR _ _ < <(python3 ../tiempos.py | grep '^DURACION')
EMPIEZA=($(python3 ../tiempos.py | sed -n 's/^EMPIEZA //p'))
VOCES=(v1 v2 v3 v4 v5 v6 v7)
T=$(mktemp -d)
trap 'rm -rf "$T"' EXIT

# Cada toma a -18 LUFS, con un paso alto a 80 Hz y una compresión suave, y en su sitio.
# EL apad ANTES DEL adelay NO SE QUITA (asi-funciona/mezclar.sh: sin él, ffmpeg 6.1 corta el final de la frase).
ENTRADAS=""; FILTRO=""; MEZCLA=""
N=${#VOCES[@]}
for i in $(seq 1 $N); do
  ffmpeg -v error -y -i voz/${VOCES[$((i-1))]}.flac -af "atempo=$VEL" -c:a pcm_s24le "$T/f$i.wav"
  I=$(ffmpeg -hide_banner -i voz/${VOCES[$((i-1))]}.flac -af ebur128 -f null - 2>&1 | sed -n 's/^ *I: *\(-*[0-9.]*\) LUFS/\1/p' | tail -1)
  GAN=$(echo "-18 - ($I)" | bc -l)
  MS=$(echo "${EMPIEZA[$((i-1))]} * 1000 / 1" | bc)
  ENTRADAS="$ENTRADAS -i $T/f$i.wav"
  FILTRO="$FILTRO[$((i-1)):a]highpass=f=80,volume=${GAN}dB,acompressor=threshold=-24dB:ratio=2.5:attack=8:release=160:makeup=1,apad=pad_dur=1,adelay=$MS[v$i];"
  MEZCLA="$MEZCLA[v$i]"
done
ffmpeg -v error -y $ENTRADAS -filter_complex "${FILTRO}${MEZCLA}amix=inputs=$N:normalize=0,apad,atrim=0:$DUR,aresample=48000[voz]" \
  -map "[voz]" -ac 1 -c:a pcm_s24le "$T/voz.wav"
# Que ninguna frase llegue cortada: los 50 ms de antes de su fundido final tienen que sonar en la pista de voz.
python3 - "$T/voz.wav" "$VEL" "${VOCES[*]}" "${EMPIEZA[@]}" <<'PY'
import subprocess, sys, numpy as np
sr = 48000
v = np.frombuffer(subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', sys.argv[1], '-f', 'f32le', '-ac', '1', '-ar', str(sr), '-'],
                                 capture_output=True).stdout, np.float32)
mal = []; vel = float(sys.argv[2]); voces = sys.argv[3].split()
for i, t0 in enumerate(map(float, sys.argv[4:]), 1):
    d = 1 / vel * float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f'voz/{voces[i-1]}.flac'],
                             capture_output=True, text=True).stdout)
    x = v[int((t0 + d - 0.10) * sr):int((t0 + d - 0.05) * sr)]
    db = 20 * np.log10(np.sqrt(np.mean(x.astype(np.float64) ** 2)) + 1e-12)
    if db < -100: mal.append(f'{voces[i-1]} ({db:.0f} dB al final)')
    if i < len(voces) and t0 + d > float(sys.argv[4 + i]) - 0.05: mal.append(f'{voces[i-1]} pisa a la siguiente')
if mal: sys.exit('frases cortadas o pisadas en la pista de voz: ' + ', '.join(mal))
print(f'las {len(voces)} frases llegan enteras a la pista de voz, y ninguna pisa a la siguiente')
PY

# La música, a -33 LUFS (quince por debajo de la voz), y apartándose mientras la voz habla.
ffmpeg -v error -y -i musica-calma.mp3 -af "aresample=48000,atrim=start=$INICIO,asetpts=PTS-STARTPTS" -ac 2 -c:a pcm_s24le "$T/mus1.wav"
ffmpeg -v error -y -i "$T/mus1.wav" -af "rubberband=tempo=$VEL,afade=t=in:d=0.3,apad,atrim=0:$DUR,afade=t=out:st=$(echo "$DUR - 0.9" | bc -l):d=0.9" \
  -ac 2 -c:a pcm_f32le "$T/mus0.wav"
IM=$(ffmpeg -hide_banner -i "$T/mus0.wav" -af ebur128 -f null - 2>&1 | sed -n 's/^ *I: *\(-*[0-9.]*\) LUFS/\1/p' | tail -1)
ffmpeg -v error -y -i "$T/mus0.wav" -i "$T/voz.wav" -filter_complex "
[0:a]volume=$(echo "-33 - ($IM)" | bc -l)dB[mus];
[1:a]asplit=2[v1][sc];
[mus][sc]sidechaincompress=threshold=0.04:ratio=3:attack=60:release=550[dk];
[v1]pan=stereo|c0=c0|c1=c0[vs];
[dk][vs]amix=inputs=2:normalize=0,alimiter=limit=0.28:attack=3:release=60:level=false[mx]" \
  -map "[mx]" -c:a pcm_s24le "$T/mezcla.wav"

# loudnorm en dos pasadas a -16 LUFS integrados y -1,5 dBTP, y LINEAL (una ganancia fija); si no queda lineal, se para.
M=$(ffmpeg -hide_banner -i "$T/mezcla.wav" -af loudnorm=I=-16:TP=-1.5:LRA=20:print_format=json -f null - 2>&1 | sed -n '/^{/,/^}/p')
g() { echo "$M" | python3 -c "import json,sys;print(json.load(sys.stdin)['$1'])"; }
LN="loudnorm=I=-16:TP=-1.5:LRA=20:measured_I=$(g input_i):measured_TP=$(g input_tp):measured_LRA=$(g input_lra):measured_thresh=$(g input_thresh):offset=$(g target_offset):linear=true"
TIPO=$(ffmpeg -hide_banner -i "$T/mezcla.wav" -af "$LN:print_format=json" -f null - 2>&1 | sed -n '/^{/,/^}/p' \
  | python3 -c "import json,sys;print(json.load(sys.stdin)['normalization_type'])")
if [ -n "$PISTAS" ]; then mkdir -p "$PISTAS" && cp "$T/voz.wav" "$T/mus0.wav" "$T/mezcla.wav" "$PISTAS/"; fi
if [ "$TIPO" != "linear" ]; then echo "loudnorm no queda lineal ($TIPO): baja el limit del alimiter" >&2; exit 1; fi
echo "loudnorm: $TIPO (entrada $(g input_i) LUFS, $(g input_tp) dBTP)"
ffmpeg -v error -y -i "$T/mezcla.wav" -af "$LN,aresample=48000" -ar 48000 -ac 2 -c:a aac -b:a 256k sonido.m4a
ffmpeg -hide_banner -i sonido.m4a -af ebur128=peak=true -f null - 2>&1 | grep -E "^\s+(I|Peak|LRA):" | tr -s ' '
