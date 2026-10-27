#!/bin/bash
# El sonido de «Un trazo» (27-oct): la música de Lyria montada para que su golpe caiga en el
# cierre, los «tic» y dos acentos sintetizados aquí mismo, y todo a -14 LUFS. Escribe
# assets/sonido.m4a, que es lo que se pone encima del render (README.md, «Para rehacerla»).
#
# LA MÚSICA (assets/musica-lyria.mp3, la toma 3 de las tres que se pidieron; README.md, «La
# música»): 30,77 s, en re mayor, unos 96 BPM. Medido con librosa y con los arranques por
# bandas, no con `hyperframes beats`, que le dio 128 BPM con confianza baja:
#   - 24,04 s: entra el bajo y cambia la sección (la «B» de `hyperframes audio --only sections`
#     empieza en 24,065). Es el tiempo fuerte más claro de la pista.
#   - 26,57 s: el golpe, un compás después (2,53 s); de ahí se apaga sola hasta 30,77.
# Se empieza en 14,04, así que el bajo cae en el 10,00 del vídeo (el precio) y el golpe en el
# 12,53 (el cierre). Un compás son 2,5 s, y la nota más fuerte de cada uno cae en 0,18 + 2,5k:
# ahí van los cortes del index.html (2,67 / 5,17 / 7,67). Las corcheas, en 0,025 + 0,3125k.
#
# EL BAJO Y EL GOLPE SON SUBGRAVE (revisión del 27-oct): el golpe tiene el pico en 37 Hz, un re,
# y el 90 % de su energía por debajo de 62 Hz. El altavoz de un iPhone no lo da, así que en el
# móvil el precio y el cierre sonaban como si la música se apagara. Por eso, desde el 10,0:
#   - un paso alto a 30 Hz (quita también la continua de la sección B) y un estante de -7 dB
#     por debajo de 120 Hz, y los medios a ganancia 1 (antes se bajaba todo 4,4 dB);
#   - un acento que se oye en el móvil: un acorde de re mayor sintetizado (re, fa#, la, con
#     armónicos hasta 3 kHz) en el 12,53, y uno corto y suave (re y la) en el 10,00.
# La sección A va 2,3 dB más fuerte por la izquierda (viene así de Lyria): se compensa sólo ahí.
#
# LOS TIC: un seno corto que se apaga, sin IA. Los tiempos son los del index.html (BARRAS, DIAS,
# LLEGAN): si se mueve uno, se mueve en los dos sitios.
#   - las cuatro barras de cobertura que caen: 0,3375 / 0,65 / 0,9625 / 1,275, cada uno más grave;
#   - los tres días de la ruta: 5,65 / 6,275 / 6,90;
#   - las cuatro personas, más suaves, cuando cada línea llega a su cabeza: 8,15 / 8,4625 / 8,775 / 9,0875.
set -e
cd "$(dirname "$0")/assets"
DUR=17.5
INICIO=14.04
tic() {  # tiempo, frecuencia, amplitud, caída (s)
  echo "if(between(t,$1,$1+0.3),$3*min(1,(t-$1)/0.002)*sin(2*PI*$2*(t-$1))*exp(-(t-$1)/$4),0)"
}
nota() {  # tiempo, frecuencia, amplitud, caída (s): cuatro armónicos, los altos se apagan antes
  local p="$3*min(1,(t-$1)/0.004)*(sin(2*PI*$2*(t-$1))*exp(-(t-$1)/$4)"
  p="$p+0.45*sin(2*PI*2*$2*(t-$1))*exp(-(t-$1)/($4*0.6))"
  p="$p+0.22*sin(2*PI*3*$2*(t-$1))*exp(-(t-$1)/($4*0.4))"
  p="$p+0.10*sin(2*PI*4*$2*(t-$1))*exp(-(t-$1)/($4*0.3)))"
  echo "if(between(t,$1,$1+4.6),$p,0)"
}
E="0"
for p in "0.3375 2200" "0.65 1850" "0.9625 1550" "1.275 1300"; do set -- $p; E="$E+$(tic $1 $2 0.30 0.020)"; done
for t in 5.65 6.275 6.9; do E="$E+$(tic $t 1660 0.26 0.028)+$(tic $t 3320 0.08 0.012)"; done
for t in 8.15 8.4625 8.775 9.0875; do E="$E+$(tic $t 990 0.16 0.035)"; done
# El acento del precio (10,00): re y la, cortos.
G=${GOLPE:-1}
E="$E+$(nota 10.0 587.33 $(echo "0.15*$G" | bc -l) 0.40)+$(nota 10.0 880 $(echo "0.09*$G" | bc -l) 0.32)"
# El del cierre (12,53): re mayor abierto, del re4 al re6, y un chasquido brillante encima.
for n in "293.66 0.16" "369.99 0.11" "440 0.12" "587.33 0.13" "880 0.07" "1174.66 0.05"; do
  set -- $n; E="$E+$(nota 12.53 $1 $(echo "$2*$G" | bc -l) 1.30)"
done
E="$E+$(tic 12.53 2349.3 $(echo "0.10*$G" | bc -l) 0.030)+$(tic 12.53 2960 $(echo "0.06*$G" | bc -l) 0.022)"

# La música: del 14,04 al final de la pista (16,73 s) y silencio hasta 17,5. Dos copias que se
# cruzan en 20 ms en el 10,0: hasta ahí, la sección A con el balance corregido; desde ahí, la B
# con el paso alto y el estante. El fundido acaba en 16,70, antes de que se acabe el fichero
# (antes acababa en 17,5 y la cola se cortaba en seco en 16,73). 15 ms de entrada, sin chasquido.
ffmpeg -v error -y -i musica-lyria.mp3 -f lavfi -i "aevalsrc='$E':s=48000:d=$DUR" -filter_complex "
[0:a]atrim=start=$INICIO,asetpts=PTS-STARTPTS,aresample=48000,apad,atrim=0:$DUR,highpass=f=30,asplit=2[ma][mb];
[ma]pan=stereo|c0=0.876*c0|c1=1.141*c1,volume='if(lt(t,9.98),1,if(lt(t,10.0),1-(t-9.98)/0.02,0))':eval=frame[a1];
[mb]lowshelf=f=120:g=-7,volume='if(lt(t,9.98),0,if(lt(t,10.0),(t-9.98)/0.02,1))':eval=frame[b1];
[a1][b1]amix=inputs=2:normalize=0,afade=t=in:d=0.015,afade=t=out:st=15.4:d=1.3[mus];
[1:a]pan=stereo|c0=c0|c1=c0[tics];
[mus][tics]amix=inputs=2:normalize=0:duration=first,afade=t=out:st=16.6:d=0.8,alimiter=limit=0.72:level=false:attack=2:release=60:asc=1[mix]" \
  -map "[mix]" -ar 48000 -ac 2 -c:a pcm_s24le /tmp/trazo-mezcla.wav
# loudnorm en dos pasadas a -14 LUFS integrados y -1,5 dBTP, y LINEAL: una ganancia fija que deja
# la mezcla como se ha escrito arriba. LRA=20 y no 11: con 11, el rango de esta mezcla bastaba para
# que loudnorm se fuera al modo dinámico; en lineal el LRA no se usa para nada más. Si la ganancia
# dejara el pico verdadero por encima de -1,5, loudnorm se pasaría al modo DINÁMICO sin avisar
# (lanzamiento-ios/README.md): por eso el limitador de arriba deja sitio, y por eso se comprueba.
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
