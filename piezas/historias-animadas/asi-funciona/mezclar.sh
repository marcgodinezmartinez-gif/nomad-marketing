#!/bin/bash
# El sonido de «Así funciona» (30-oct), el vídeo único de #18: la voz de Kore encima de la MISMA música de
# «Un trazo», con la misma cadena de sonido que aquél (lanzamiento-trazo/mezclar.sh, que es donde se explica
# cada paso y por qué) y la de incluye-pago/. Escribe assets/sonido.m4a.
#
# LA VOZ (assets/voz/v01…v12.flac): Kore, gemini-3.1-flash-tts-preview, piezas/ia/voz.py, una toma por
# frase, recortada con recortar-voz.py de «Un trazo» y comprobada con faster-whisper (README.md, «La voz»).
#
# LA MÚSICA: la de «Un trazo», que dura 60,7 s, y el vídeo pide 65,4 a 1×: se alarga REPITIENDO dos compases
# justos (6,407 s). Hasta el 11,26 de la pista tal cual y, desde ahí, la misma pista 6,407 s ANTES, fundidas
# en dos segundos (9,26-11,26 a 1×, que es el corte de S2 a S3) donde los acordes de las dos se parecen
# más (croma 0,916 en 2 s, 0,894 en 4). Con tres compases no hay junta buena (croma 0,6 como mucho: la
# armonía va de dos en dos), y con uno, 0,73. Así su último acorde (el 51,25 de la pista, el arranque más
# fuerte del final) cae en 57,66 a 1×, debajo de «…como lo has disfrutado tú», y el cierre suena sobre su
# cola, que se apaga sola. La negra de la música (0,80083 s) no se mueve: la junta es de compases enteros.
set -e
cd "$(dirname "$0")/assets"
VEL=1.15
DUR=56.867
VOCES=(v01 v02 v03 v04 v05 v06 v07 v08 v09 v10 v11 v12)
# Dónde empieza cada frase, en segundos del vídeo a 1×: su corte (T, en index.html) más 0,25, y la del
# cierre, 0,2. Si se mueve un corte, se mueve aquí.
EMPIEZA=(0.25 4.59 10.05 15.95 22.02 28.95 33.57 39.54 44.09 49.78 53.98 60.2)
T=$(mktemp -d)
trap 'rm -rf "$T"' EXIT

# Cada toma a -18 LUFS, para que ninguna frase suene más fuerte que otra, con un paso alto a 80 Hz y
# una compresión suave. Y en su sitio.
# EL apad ANTES DEL adelay NO SE QUITA. Sin él, ffmpeg 6.1 corta en seco el final de cada frase que
# acaba antes que la siguiente: amix da por acabada la entrada y tira lo que adelay aún retenía. Así
# salió la primera versión con voz, con «Esto es Nomad» sin sus últimos 0,23 s («Nom…», lo oyó el
# dueño) y la frase de los paseos sin 0,34. Reproducido con dos tonos: sin apad, el de 1,76 s puesto en
# 0,3 acaba en 1,84; con apad, en 2,06. La comprobación va al final de este script.
# La aceleración va en su propia pasada, toma a toma: puesto dentro del grafo grande, rubberband dejaba
# ffmpeg girando sin acabar (más de cinco minutos al 100 %, 27-oct).
ENTRADAS=""; FILTRO=""; MEZCLA=""
N=${#VOCES[@]}
for i in $(seq 1 $N); do
  ffmpeg -v error -y -i voz/${VOCES[$((i-1))]}.flac -af "rubberband=tempo=$VEL" -c:a pcm_s24le "$T/f$i.wav"
  I=$(ffmpeg -hide_banner -i voz/${VOCES[$((i-1))]}.flac -af ebur128 -f null - 2>&1 | sed -n 's/^ *I: *\(-*[0-9.]*\) LUFS/\1/p' | tail -1)
  GAN=$(echo "-18 - ($I)" | bc -l)
  MS=$(echo "${EMPIEZA[$((i-1))]} * 1000 / $VEL / 1" | bc)
  ENTRADAS="$ENTRADAS -i $T/f$i.wav"
  FILTRO="$FILTRO[$((i-1)):a]highpass=f=80,volume=${GAN}dB,acompressor=threshold=-24dB:ratio=2.5:attack=8:release=160:makeup=1,apad=pad_dur=1,adelay=$MS[v$i];"
  MEZCLA="$MEZCLA[v$i]"
done
ffmpeg -v error -y $ENTRADAS -filter_complex "${FILTRO}${MEZCLA}amix=inputs=$N:normalize=0,apad,atrim=0:$DUR,aresample=48000[voz]" \
  -map "[voz]" -ac 1 -c:a pcm_s24le "$T/voz.wav"
# Que ninguna frase llegue cortada: los 50 ms de antes de su fundido final tienen que sonar en la pista
# de voz (un corte deja ahí ceros exactos). Si no, se para.
python3 - "$T/voz.wav" "$VEL" "${VOCES[*]}" "${EMPIEZA[@]}" <<'PY'
import subprocess, sys, numpy as np
sr = 48000
v = np.frombuffer(subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', sys.argv[1], '-f', 'f32le', '-ac', '1', '-ar', str(sr), '-'],
                                 capture_output=True).stdout, np.float32)
mal = []
vel = float(sys.argv[2])
voces = sys.argv[3].split()
for i, t0 in enumerate(map(float, sys.argv[4:]), 1):
    t0 /= vel
    d = 1 / vel * float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f'voz/{voces[i-1]}.flac'],
                             capture_output=True, text=True).stdout)
    x = v[int((t0 + d - 0.10) * sr):int((t0 + d - 0.05) * sr)]
    db = 20 * np.log10(np.sqrt(np.mean(x.astype(np.float64) ** 2)) + 1e-12)
    if db < -100: mal.append(f'{voces[i-1]} ({db:.0f} dB al final)')
if mal: sys.exit('frases cortadas en la pista de voz: ' + ', '.join(mal))
print(f'las {len(voces)} frases llegan enteras a la pista de voz')
PY

# La música: principio y final fundidos, a -33 LUFS (quince por debajo de la voz), y apartándose unos
# cinco decibelios más mientras la voz habla.
ffmpeg -v error -y -i musica-calma.mp3 -filter_complex "
[0:a]aresample=48000,asplit=2[a][b];
[a]atrim=0:11.26,asetpts=PTS-STARTPTS[a1];
[b]atrim=start=2.85336,asetpts=PTS-STARTPTS[b1];
[a1][b1]acrossfade=d=2:c1=qsin:c2=qsin[m]" \
  -map "[m]" -ac 2 -c:a pcm_s24le "$T/mus1.wav"
ffmpeg -v error -y -i "$T/mus1.wav" -af "rubberband=tempo=$VEL,afade=t=in:d=0.03,apad,atrim=0:$DUR,afade=t=out:st=$(echo "$DUR - 0.8" | bc -l):d=0.8" \
  -ac 2 -c:a pcm_s24le "$T/mus0.wav"
IM=$(ffmpeg -hide_banner -i "$T/mus0.wav" -af ebur128 -f null - 2>&1 | sed -n 's/^ *I: *\(-*[0-9.]*\) LUFS/\1/p' | tail -1)
ffmpeg -v error -y -i "$T/mus0.wav" -i "$T/voz.wav" -filter_complex "
[0:a]volume=$(echo "-33 - ($IM)" | bc -l)dB[mus];
[1:a]asplit=2[v1][sc];
[mus][sc]sidechaincompress=threshold=0.04:ratio=3:attack=60:release=550[dk];
[v1]pan=stereo|c0=c0|c1=c0[vs];
[dk][vs]amix=inputs=2:normalize=0,alimiter=limit=0.28:attack=3:release=60:level=false[mx]" \
  -map "[mx]" -c:a pcm_s24le "$T/mezcla.wav"

# loudnorm en dos pasadas a -16 LUFS integrados y -1,5 dBTP, y LINEAL: una ganancia fija. Si la
# ganancia dejara el pico verdadero por encima de -1,5, loudnorm se pasaría al modo DINÁMICO sin
# avisar (lanzamiento-ios/README.md): por eso el limitador de arriba deja sitio, y por eso se comprueba.
M=$(ffmpeg -hide_banner -i "$T/mezcla.wav" -af loudnorm=I=-16:TP=-1.5:LRA=20:print_format=json -f null - 2>&1 | sed -n '/^{/,/^}/p')
g() { echo "$M" | python3 -c "import json,sys;print(json.load(sys.stdin)['$1'])"; }
LN="loudnorm=I=-16:TP=-1.5:LRA=20:measured_I=$(g input_i):measured_TP=$(g input_tp):measured_LRA=$(g input_lra):measured_thresh=$(g input_thresh):offset=$(g target_offset):linear=true"
TIPO=$(ffmpeg -hide_banner -i "$T/mezcla.wav" -af "$LN:print_format=json" -f null - 2>&1 | sed -n '/^{/,/^}/p' \
  | python3 -c "import json,sys;print(json.load(sys.stdin)['normalization_type'])")
if [ -n "$PISTAS" ]; then mkdir -p "$PISTAS" && cp "$T/voz.wav" "$T/mus0.wav" "$T/mezcla.wav" "$PISTAS/"; fi
if [ "$TIPO" != "linear" ]; then
  echo "loudnorm no queda lineal ($TIPO): baja el limit del alimiter" >&2; exit 1
fi
echo "loudnorm: $TIPO (entrada $(g input_i) LUFS, $(g input_tp) dBTP)"
ffmpeg -v error -y -i "$T/mezcla.wav" -af "$LN,aresample=48000" -ar 48000 -ac 2 -c:a aac -b:a 256k sonido.m4a
ffmpeg -hide_banner -i sonido.m4a -af ebur128=peak=true -f null - 2>&1 | grep -E "^\s+(I|Peak|LRA):" | tr -s ' '
