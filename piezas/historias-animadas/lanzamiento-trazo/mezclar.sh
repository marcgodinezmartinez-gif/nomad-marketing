#!/bin/bash
# El sonido de «Un trazo» (27-oct): la música de Lyria montada para que su golpe caiga en el
# cierre, once «tic» sintetizados aquí mismo y todo a -14 LUFS. Escribe assets/sonido.m4a, que
# es lo que se pone encima del render (README.md, «Para rehacerla»).
#
# LA MÚSICA (assets/musica-lyria.mp3, la toma 3 de las tres que se pidieron; README.md, «La
# música»): 30,77 s, unos 96 BPM (semicorcheas cada 0,156 s, medidas). Medido con librosa y con
# los arranques por bandas, no con `hyperframes beats`, que le dio 128 BPM con confianza baja:
#   - 24,04 s: entra el bajo y cambia la sección (la «B» de `hyperframes audio --only sections`
#     empieza en 24,065). Es el tiempo fuerte más claro de la pista.
#   - 26,57 s: el golpe, un compás después (2,53 s); de ahí se apaga sola hasta 30,6.
# Se empieza en 14,04, así que el bajo cae en el 10,00 del vídeo (el precio) y el golpe en el
# 12,53 (el cierre). Los tiempos del index.html salen de aquí: un compás son 2,5 s.
#
# LOS TIC: un seno corto que se apaga, sin IA. Los tiempos son los del index.html (BARRAS, DIAS,
# PERSONAS): si se mueve uno, se mueve en los dos sitios.
#   - las cuatro barras de cobertura que caen: 0,31 / 0,63 / 0,94 / 1,25, cada uno más grave;
#   - los tres días de la ruta: 5,63 / 6,25 / 6,88;
#   - las cuatro personas, más suaves, cuando cada línea llega a su círculo: 8,13 / 8,44 / 8,75 / 9,06.
set -e
cd "$(dirname "$0")/assets"
DUR=17.5
INICIO=14.04
tic() {  # tiempo, frecuencia, amplitud, caída (s)
  echo "if(between(t,$1,$1+0.3),$3*min(1,(t-$1)/0.002)*sin(2*PI*$2*(t-$1))*exp(-(t-$1)/$4),0)"
}
E="0"
for p in "0.31 2200" "0.63 1850" "0.94 1550" "1.25 1300"; do set -- $p; E="$E+$(tic $1 $2 0.30 0.020)"; done
for t in 5.63 6.25 6.88; do E="$E+$(tic $t 1660 0.26 0.028)+$(tic $t 3320 0.08 0.012)"; done
for t in 8.13 8.44 8.75 9.06; do E="$E+$(tic $t 990 0.16 0.035)"; done

# La música: del 14,04 al final de la pista (16,73 s) y silencio hasta 17,5. Se baja 4,4 dB desde
# el bajo (10,0), porque la sección B suena 9 dB por encima de la A: con 2 dB menos el precio y
# el cierre seguían 8 dB por encima del resto. Así quedan unos 5. 15 ms de entrada, sin chasquido.
ffmpeg -v error -y -i musica-lyria.mp3 -f lavfi -i "aevalsrc='$E':s=48000:d=$DUR" -filter_complex "
[0:a]atrim=start=$INICIO,asetpts=PTS-STARTPTS,aresample=48000,apad,atrim=0:$DUR,
volume='if(lt(t,9.98),1,if(lt(t,10.0),1-(t-9.98)/0.02*0.4,0.6))':eval=frame,
afade=t=in:d=0.015,afade=t=out:st=16.3:d=1.2[mus];
[1:a]pan=stereo|c0=c0|c1=c0[tics];
[mus][tics]amix=inputs=2:normalize=0:duration=first,alimiter=limit=0.72:level=false:attack=2:release=60:asc=1[mix]" \
  -map "[mix]" -ar 48000 -ac 2 -c:a pcm_s24le /tmp/trazo-mezcla.wav
# loudnorm en dos pasadas a -14 LUFS integrados y -1,5 dBTP, y LINEAL: una ganancia fija que deja
# la mezcla como se ha escrito arriba. LRA=20 y no 11: con 11, el rango de esta mezcla (11,1 LU,
# por la cola que se apaga) bastaba para que loudnorm se fuera al modo dinámico; en lineal el
# LRA no se usa para nada más. Si la ganancia dejara el pico verdadero por encima de -1,5,
# loudnorm se pasaría al modo DINÁMICO sin avisar (lanzamiento-ios/README.md): por eso el
# limitador de arriba deja sitio, y por eso se comprueba aquí.
M=$(ffmpeg -hide_banner -i /tmp/trazo-mezcla.wav -af loudnorm=I=-14:TP=-1.5:LRA=20:print_format=json -f null - 2>&1 | sed -n '/^{/,/^}/p')
g() { echo "$M" | python3 -c "import json,sys;print(json.load(sys.stdin)['$1'])"; }
LN="loudnorm=I=-14:TP=-1.5:LRA=20:measured_I=$(g input_i):measured_TP=$(g input_tp):measured_LRA=$(g input_lra):measured_thresh=$(g input_thresh):offset=$(g target_offset):linear=true"
TIPO=$(ffmpeg -hide_banner -i /tmp/trazo-mezcla.wav -af "$LN:print_format=json" -f null - 2>&1 | sed -n '/^{/,/^}/p' \
  | python3 -c "import json,sys;print(json.load(sys.stdin)['normalization_type'])")
if [ "$TIPO" != "linear" ]; then
  echo "loudnorm no queda lineal ($TIPO): baja el limit del alimiter o la música" >&2; exit 1
fi
echo "loudnorm: $TIPO (entrada $(g input_i) LUFS, $(g input_tp) dBTP)"
ffmpeg -v error -y -i /tmp/trazo-mezcla.wav -af "$LN,aresample=48000" \
  -ar 48000 -ac 2 -c:a aac -b:a 256k sonido.m4a
rm -f /tmp/trazo-mezcla.wav
ffmpeg -hide_banner -i sonido.m4a -af ebur128=peak=true -f null - 2>&1 | grep -E "^\s+(I|Peak|LRA):" | tr -s ' '
