#!/bin/bash
# El sonido de «Un trazo», versión 2 (27-oct): la música de Lyria montada para que su golpe caiga en
# el cierre, los «tic» y el acorde del cierre sintetizados aquí mismo, y todo a -14 LUFS. Escribe
# assets/sonido.m4a, que es lo que se pone encima del render (README.md, «Para rehacerla»).
#
# LA MÚSICA (assets/musica-lyria.mp3, la toma 2 de las tres que se pidieron el 27-oct; README.md, «La
# música»): 29,28 s, en si bemol mayor, 96 BPM. Medido con librosa (arranques por bandas y la fase de
# la rejilla de corcheas), no con `hyperframes beats`:
#   - la rejilla de corcheas cae en 0,25 + 0,3125k;
#   - 12,75 s: entra la batería (el bombo); 15,76-15,88 s: entra el bajo, grave y lleno;
#   - 26,50 s: el golpe, con el acorde entero; de ahí se apaga sola en un segundo y medio.
# Se empieza en 5,25, así que la rejilla del vídeo es 0,3125k, la batería cae en el 7,50 (los paseos),
# el bajo en el 10,5 (la audioguía) y el golpe en el 21,25 (el cierre).
#
# EL BAJO Y EL BOMBO SON SUBGRAVE (como en la primera versión): el altavoz de un iPhone no los da, y
# lo que no se oye ahí no golpea. Por eso, desde el 7,5: un paso alto a 30 Hz y un estante de -6 dB por
# debajo de 120 Hz. Y el golpe del cierre lleva encima un acorde de si bemol mayor sintetizado, con
# armónicos hasta 3 kHz y un chasquido brillante, que se oye en el móvil y que, además, alarga la cola:
# la de la toma dura un segundo y medio y el cierre dura cuatro y medio.
#
# LOS TIC: un seno corto que se apaga, sin IA, en notas de si bemol mayor. Los tiempos son los del
# index.html (las corcheas E(k) = 0,3125k): si se mueve uno, se mueve en los dos sitios.
#   - nace la línea, del logo: E(1);
#   - las siete opciones que se eligen: E(9)…E(15), subiendo la escala;
#   - los cuatro planes del día: E(18)…E(21);
#   - las tres paradas del paseo: E(25)…E(27);
#   - las cuatro barras que caen: E(33), E(33,5), E(34), E(34,5), cada una más grave;
#   - las cuatro voces que suenan, E(45)…E(48), y la elegida, E(49);
#   - las cuatro personas del grupo: E(54)…E(57), más suaves;
#   - las tres chinchetas de Lugares: E(62)…E(64).
set -e
cd "$(dirname "$0")/assets"
DUR=25.8
INICIO=5.25
e() { echo "0.3125*$1" | bc -l; }
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
E="$E+$(tic $(e 1) 1174.66 0.16 0.030)"
k=9; for f in 932.33 1046.50 1174.66 1244.51 1396.91 1567.98 1760.00; do E="$E+$(tic $(e $k) $f 0.22 0.022)"; k=$((k+1)); done
for k in 18 19 20 21; do E="$E+$(tic $(e $k) 1396.91 0.20 0.026)+$(tic $(e $k) 2793.83 0.05 0.012)"; done
for k in 25 26 27; do E="$E+$(tic $(e $k) 1174.66 0.20 0.026)"; done
for p in "33 1864.66" "33.5 1567.98" "34 1396.91" "34.5 1174.66"; do set -- $p; E="$E+$(tic $(e $1) $2 0.28 0.020)"; done
for k in 45 46 47 48; do E="$E+$(tic $(e $k) 1396.91 0.12 0.020)"; done
E="$E+$(tic $(e 49) 1864.66 0.20 0.026)"
for k in 54 55 56 57; do E="$E+$(tic $(e $k) 932.33 0.15 0.035)"; done
k=62; for f in 1396.91 1567.98 1864.66; do E="$E+$(tic $(e $k) $f 0.22 0.024)"; k=$((k+1)); done
# El del cierre (21,25): si bemol mayor abierto, del si bemol 3 al si bemol 5, y un chasquido brillante.
G=${GOLPE:-1}
for n in "233.08 0.15" "293.66 0.12" "349.23 0.11" "466.16 0.13" "587.33 0.08" "698.46 0.06" "932.33 0.05"; do
  set -- $n; E="$E+$(nota 21.25 $1 $(echo "$2*$G" | bc -l) 1.70)"
done
E="$E+$(tic 21.25 2349.32 $(echo "0.10*$G" | bc -l) 0.030)+$(tic 21.25 2793.83 $(echo "0.06*$G" | bc -l) 0.022)"

# La música: del 5,25 al final de la pista (24,03 s del vídeo) y silencio hasta 25,8. Dos copias que se
# cruzan en 20 ms en el 7,5: hasta ahí, tal cual; desde ahí, con el estante. 15 ms de entrada, sin
# chasquido, y un fundido de 0,6 s que acaba antes de que se acabe el fichero.
ffmpeg -v error -y -i musica-lyria.mp3 -f lavfi -i "aevalsrc='$E':s=48000:d=$DUR" -filter_complex "
[0:a]atrim=start=$INICIO,asetpts=PTS-STARTPTS,aresample=48000,apad,atrim=0:$DUR,highpass=f=30,asplit=2[ma][mb];
[ma]volume='if(lt(t,7.48),1,if(lt(t,7.5),1-(t-7.48)/0.02,0))':eval=frame[a1];
[mb]lowshelf=f=120:g=-6,volume='if(lt(t,7.48),0,if(lt(t,7.5),(t-7.48)/0.02,1))':eval=frame[b1];
[a1][b1]amix=inputs=2:normalize=0,afade=t=in:d=0.015,afade=t=out:st=23.35:d=0.6[mus];
[1:a]pan=stereo|c0=c0|c1=c0[tics];
[mus][tics]amix=inputs=2:normalize=0:duration=first,afade=t=out:st=24.6:d=1.15,alimiter=limit=0.72:level=false:attack=2:release=60:asc=1[mix]" \
  -map "[mix]" -ar 48000 -ac 2 -c:a pcm_s24le /tmp/trazo-mezcla.wav
# loudnorm en dos pasadas a -14 LUFS integrados y -1,5 dBTP, y LINEAL: una ganancia fija que deja la
# mezcla como se ha escrito arriba. Si la ganancia dejara el pico verdadero por encima de -1,5,
# loudnorm se pasaría al modo DINÁMICO sin avisar (lanzamiento-ios/README.md): por eso el limitador de
# arriba deja sitio, y por eso se comprueba.
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
