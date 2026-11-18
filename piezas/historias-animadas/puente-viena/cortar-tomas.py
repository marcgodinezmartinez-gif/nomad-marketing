# Corta las tomas de «El puente, ya organizado», cada una a su fichero, ya a su velocidad final, a 404×806
# (el tamaño de la pantalla en el vídeo), 30 fps, sin sonido. Es el cortar-tomas.py de pruebalo/, que es
# donde se explica por qué se hace así:
#
# 1. LAS GRABACIONES SON DE FOTOGRAMAS VARIABLES, Y SU MP4 MIENTE EN LOS TIEMPOS: cada grabación se copia
#    primero a un .mkv (que guarda el pts), se pasa a 120 fps fijos y la ventana se corta después (trim).
# 2. LO QUE HAY QUE TAPAR SE TAPA AQUÍ, en píxeles de la grabación («velos» en tomas.json: y0, y1 y el color
#    de debajo), antes de recortar y escalar: el código de invitación del viaje demo, sobre todo.
#
# Las grabaciones son las de capturas/viena.sh del repo de la app (recorrido-viena-*.mp4, 18-nov):
# 1206×2622, sin sonido. Sin la barra de estado ni la barra de inicio, como en asi-funciona: se quitan 168 px
# de arriba y 48 de abajo.
#
# Uso: METRAJE=/ruta/a/las/grabaciones python3 -I cortar-tomas.py [tomas.json]   y después  python3 -I poner-tomas.py
import json, os, subprocess, sys, tempfile
VELOCIDAD = 1.15
D = os.path.dirname(os.path.abspath(__file__))
args = [x for x in sys.argv[1:] if not x.startswith('--')]
tomas = json.load(open(os.path.join(D, args[0] if args else 'tomas.json'), encoding='utf-8'))
os.makedirs(os.path.join(D, 'assets/tomas'), exist_ok=True)
M = os.environ.get('METRAJE') or sys.exit('falta METRAJE=<carpeta con recorrido-viena-*.mp4>')
TMP = tempfile.mkdtemp()
def mkv(fichero):
    sal = os.path.join(TMP, fichero + '.mkv')
    if not os.path.exists(sal):
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', os.path.join(M, fichero), '-map', '0:v:0', '-c', 'copy', sal], check=True)
    return sal
for t in tomas:
    largo = t['salida'] - t['entrada']                 # segundos de grabación
    dura = (t['fin'] - t['inicio']) / VELOCIDAD        # segundos que se ve en el vídeo final
    v = largo / dura
    # (el trim corta 0,1 s de vídeo final más allá de «salida»: la toma no se queda un fotograma corta por redondeo,
    # y el <video> sólo enseña data-duration)
    sal = os.path.join(D, 'assets/tomas', t['id'] + '.mp4')
    velos = ''.join(f",drawbox=x=0:y={a}:w=1206:h={b - a}:color=0x{c.lstrip('#')}@1:t=fill" for a, b, c in t.get('velos', []))
    vf = (f"fps=120,trim=start={t['entrada']:.3f}:end={t['salida'] + 0.1 * v:.3f},setpts=(PTS-STARTPTS)/{v:.6f},fps=30,"
          f"format=rgb24{velos},crop=1206:2406:0:168,scale=404:806:flags=lanczos:out_color_matrix=bt709:out_range=tv,format=yuv420p")
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', mkv(t['fichero']), '-vf', vf,
                    '-an', '-c:v', 'libx264', '-crf', '14', '-preset', 'slow', '-g', '15',
                    '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709',
                    '-movflags', '+faststart', sal], check=True)
    real = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', sal],
                                capture_output=True, text=True).stdout)
    print(f"{t['id']}: {t['fichero']} {t['entrada']}-{t['salida']} a {v:.3f}× → {real:.3f} s "
          f"(data-start {t['inicio'] / VELOCIDAD:.3f}, data-duration {dura:.3f})")
import shutil; shutil.rmtree(TMP, ignore_errors=True)
