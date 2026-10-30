# Corta las tomas de la app de «Lo que incluye tu viaje», cada una a su fichero, ya a su velocidad
# final (la de la escena × VELOCIDAD), a 404×806 (el tamaño de la pantalla en el vídeo), 30 fps.
# Sin la barra de estado ni la barra de inicio: la grabación del simulador lleva pintada la isla negra
# del iPhone, y con ella el borde verde sería el dibujo de un iPhone, que Apple no deja (README.md).
# Se quitan 168 px de arriba (la hora, la isla y los iconos acaban en 151) y 48 de abajo (la barra de
# inicio empieza en 2.580), medido sobre las once tomas.
# Así cada <video class="clip"> empieza en 0 y va a 1×: sin saltos al fotograma clave de antes.
#
# Las grabaciones NO están en el repo (llevan el código del viaje demo): banco/metraje/README.md dice
# dónde están. Se bajan a una carpeta y se pasa con METRAJE=<carpeta>.
# Uso: METRAJE=/ruta/a/videos python3 cortar-tomas.py tomas.json
import json, os, subprocess, sys
VELOCIDAD = 1.15
D = os.path.dirname(os.path.abspath(__file__))
M = os.environ.get('METRAJE') or sys.exit('falta METRAJE=<carpeta con recorrido-*.mp4>')
tomas = json.load(open(os.path.join(D, sys.argv[1] if len(sys.argv) > 1 else 'tomas.json')))
os.makedirs(os.path.join(D, 'assets/tomas'), exist_ok=True)
for t in tomas:
    largo = t['salida'] - t['entrada']                 # segundos de grabación
    dura = (t['fin'] - t['inicio']) / VELOCIDAD        # segundos que se ve en el vídeo final
    v = largo / dura
    sal = os.path.join(D, 'assets/tomas', t['id'] + '.mp4')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f"{t['entrada']:.3f}", '-t', f'{largo:.3f}',
                    '-i', os.path.join(M, t['fichero']), '-vf', f'setpts=(PTS-STARTPTS)/{v:.6f},fps=30,crop=1206:2406:0:168,scale=404:806:flags=lanczos',
                    '-an', '-c:v', 'libx264', '-crf', '14', '-preset', 'slow', '-g', '15', '-pix_fmt', 'yuv420p',
                    '-movflags', '+faststart', sal], check=True)
    real = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', sal],
                                capture_output=True, text=True).stdout)
    print(f"{t['id']}: {t['fichero']} {t['entrada']}-{t['salida']} a {v * 1:.3f}× → {real:.3f} s "
          f"(data-start {t['inicio'] / VELOCIDAD:.3f}, data-duration {dura:.3f})")
