#!/bin/bash
# El sonido del anuncio (24-oct): la música de Lyria montada para que su golpe caiga en el
# cierre, Kore encima con la música bajada, y todo a -14 LUFS. Escribe assets/sonido.m4a,
# que es lo que se pone encima del render (ver README.md).
#
# La música (assets/musica-lyria.mp3, 95,7 BPM, un compás = 2,508 s) tiene su golpe a los
# 15,33 s. El cierre del vídeo empieza a los 20,0, así que se empieza en el primer tiempo
# fuerte (0,28) y se repiten los dos primeros compases (0,28-5,30): la entrada suena dos
# veces, debajo de la voz, y el golpe cae en 20,0 (medido en la mezcla: el pico de energía
# está entre 20,0 y 20,1).
# Kore (assets/voz-kore.wav) empieza a hablar a los 0,31 s de su fichero; se pone a 0,29
# para que la primera palabra caiga a los 0,60, que es lo que dicen los data-t del HTML.
set -e
cd "$(dirname "$0")/assets"
DUR=24.6
ffmpeg -v error -y -i musica-lyria.mp3 -i voz-kore.wav -filter_complex "
[0:a]atrim=0.28:5.326,asetpts=PTS-STARTPTS[m1];[0:a]atrim=0.28,asetpts=PTS-STARTPTS[m2];
[m1][m2]acrossfade=d=0.03:c1=tri:c2=tri,aresample=48000,atrim=0:$DUR,
volume='if(lt(t,7.2),0.18,if(lt(t,7.6),0.18+(t-7.2)/0.4*0.44,if(lt(t,19.9),0.62,if(lt(t,20.0),0.62+(t-19.9)/0.1*0.23,0.85))))':eval=frame,
afade=t=in:d=0.15,afade=t=out:st=23.2:d=1.4[mus];
[1:a]aresample=48000,highpass=f=70,adelay=290|290,apad,atrim=0:$DUR,pan=stereo|c0=c0|c1=c0[voz];
[mus][voz]amix=inputs=2:normalize=0:duration=first,alimiter=limit=0.72:level=false:attack=2:release=60:asc=1[mix]" -map "[mix]" -ar 48000 -ac 2 -c:a pcm_s24le /tmp/lanz-mezcla.wav
# loudnorm en dos pasadas a -14 LUFS integrados y -1,5 dBTP, y LINEAL: una ganancia fija, que
# deja la mezcla (el ducking, la subida, el golpe) como se ha escrito arriba.
# Ojo: si la ganancia lineal dejara el pico verdadero por encima de -1,5, loudnorm se pasa al modo
# DINÁMICO sin avisar (revisión del 24-oct: pasaba, con el pico de la mezcla en -0,49 dBTP, y la
# ganancia iba de -1,17 dB debajo de la voz a +0,46 en la música). Por eso el limitador de arriba
# (alimiter a 0,72, unos -2,9 dBFS de pico de muestra) deja sitio, y por eso se comprueba abajo.
M=$(ffmpeg -hide_banner -i /tmp/lanz-mezcla.wav -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json -f null - 2>&1 | sed -n '/^{/,/^}/p')
g() { echo "$M" | python3 -c "import json,sys;print(json.load(sys.stdin)['$1'])"; }
LN="loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=$(g input_i):measured_TP=$(g input_tp):measured_LRA=$(g input_lra):measured_thresh=$(g input_thresh):offset=$(g target_offset):linear=true"
TIPO=$(ffmpeg -hide_banner -i /tmp/lanz-mezcla.wav -af "$LN:print_format=json" -f null - 2>&1 | sed -n '/^{/,/^}/p' \
  | python3 -c "import json,sys;print(json.load(sys.stdin)['normalization_type'])")
if [ "$TIPO" != "linear" ]; then
  echo "loudnorm no queda lineal ($TIPO): baja el limit del alimiter o la música" >&2; exit 1
fi
echo "loudnorm: $TIPO (entrada $(g input_i) LUFS, $(g input_tp) dBTP)"
ffmpeg -v error -y -i /tmp/lanz-mezcla.wav -af "$LN,aresample=48000" \
  -ar 48000 -ac 2 -c:a aac -b:a 256k sonido.m4a
rm -f /tmp/lanz-mezcla.wav
ffmpeg -hide_banner -i sonido.m4a -af ebur128=peak=true -f null - 2>&1 | grep -E "^\s+(I|Peak|LRA):" | tr -s ' '
