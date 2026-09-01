#!/bin/bash
# Monta el Reel del grupo: 5 escenas PNG -> mp4 1080x1920, 30 fps.
#
# Mismo motor que `montar-reel.sh` y con las mismas dos trampas de ffmpeg ya pagadas
# allí (zoompan multiplica `d` por cada frame de entrada — nada de `-loop`; y el
# pre-escalado x2 es lo que quita el temblor). Lo único propio de este Reel son los
# tiempos: el gancho aguanta 3,4 s porque tiene tres líneas que hay que leer enteras
# antes de que cambie, y el QR aguanta 3,6 s porque la gente intenta mirarlo.
set -e
FF=/tmp/claude-0/-home-user-NOMAD/540f89ad-ecf3-574a-baa5-50e2739fd1e9/scratchpad/node_modules/ffmpeg-static/ffmpeg

push() { echo "scale=2160:3840,zoompan=z='1+0.09*on/$1':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=$1:s=1080x1920:fps=30,setsar=1"; }
bajada() { echo "scale=2160:3840,zoompan=z='1.10':x='iw/2-(iw/zoom/2)':y='(ih-ih/zoom)*(0.30+0.40*on/$1)':d=$1:s=1080x1920:fps=30,setsar=1"; }

"$FF" -y -loglevel error \
  -i reelg-01.png -i reelg-02.png -i reelg-03.png -i reelg-04.png -i reelg-05.png \
  -filter_complex "
    [0:v]$(push 102)[v0];
    [1:v]$(bajada 96)[v1];
    [2:v]$(push 108)[v2];
    [3:v]$(bajada 96)[v3];
    [4:v]$(push 108)[v4];
    [v0][v1]xfade=transition=fade:duration=0.4:offset=3.0[x1];
    [x1][v2]xfade=transition=fade:duration=0.4:offset=5.8[x2];
    [x2][v3]xfade=transition=fade:duration=0.4:offset=9.0[x3];
    [x3][v4]xfade=transition=fade:duration=0.4:offset=11.8[vout]
  " -map "[vout]" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p -r 30 -crf 20 -movflags +faststart \
  reel-nomad-grupo.mp4
echo "OK"
