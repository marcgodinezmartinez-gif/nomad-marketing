#!/bin/bash
# Monta el Reel: 5 escenas PNG -> mp4 1080x1920, 30 fps, con movimiento (zoompan) y
# fundidos (xfade).
#
# DOS trampas de ffmpeg pagadas aquí, por si alguien lo toca:
#  1. `zoompan` genera `d` frames POR CADA FRAME DE ENTRADA. Con `-loop 1 -t 3` la
#     entrada ya son 90 frames y el resultado fue un vídeo de 5 minutos y 35 segundos.
#     La entrada es UNA imagen suelta (sin -loop): 1 frame x d=90 = 3 s exactos.
#  2. El pre-escalado x2 antes del zoompan es lo que quita el temblor de ese filtro.
set -e
FF=/tmp/claude-0/-home-user-NOMAD/540f89ad-ecf3-574a-baa5-50e2739fd1e9/scratchpad/node_modules/ffmpeg-static/ffmpeg

push() { echo "scale=2160:3840,zoompan=z='1+0.09*on/$1':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=$1:s=1080x1920:fps=30,setsar=1"; }
bajada() { echo "scale=2160:3840,zoompan=z='1.10':x='iw/2-(iw/zoom/2)':y='(ih-ih/zoom)*(0.30+0.40*on/$1)':d=$1:s=1080x1920:fps=30,setsar=1"; }

"$FF" -y -loglevel error \
  -i reel-01.png -i reel-02.png -i reel-03.png -i reel-04.png -i reel-05.png \
  -filter_complex "
    [0:v]$(push 90)[v0];
    [1:v]$(bajada 108)[v1];
    [2:v]$(bajada 90)[v2];
    [3:v]$(bajada 90)[v3];
    [4:v]$(push 108)[v4];
    [v0][v1]xfade=transition=fade:duration=0.4:offset=2.6[x1];
    [x1][v2]xfade=transition=fade:duration=0.4:offset=5.8[x2];
    [x2][v3]xfade=transition=fade:duration=0.4:offset=8.4[x3];
    [x3][v4]xfade=transition=fade:duration=0.4:offset=11.0[vout]
  " -map "[vout]" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p -r 30 -crf 20 -movflags +faststart \
  reel-nomad-es.mp4
echo "OK"
