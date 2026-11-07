# Corta las tomas de «Pruébalo antes de pagar», cada una a su fichero, ya a su velocidad final, a 404×806
# (el tamaño de la pantalla en el vídeo), 30 fps, sin sonido. Es el cortar-tomas.py de asi-funciona/ con
# las grabaciones nuevas, y con dos cosas que aquéllas no necesitaban:
#
# 1. LAS GRABACIONES SON DE FOTOGRAMAS VARIABLES, Y SU MP4 MIENTE EN LOS TIEMPOS. El simulador sólo escribe
#    un fotograma cuando la pantalla cambia (la hoja quieta no tiene ni uno entre 56,7 y 67,2 s), y el mp4
#    lleva fotogramas B con un dts que no sigue al pts. ffprobe da el pts bueno, pero ffmpeg, al decodificar,
#    se queda con un tiempo deducido del dts y se COME los tramos quietos: en muestras-paseo, el cierre de la
#    hoja (25,2 s) le salía a 9,9 s. Medido el 7-nov: un corte hecho así enseñaba la hoja con el precio
#    donde tenía que estar el paseo. Por eso cada grabación se copia primero, sin recodificar, a un .mkv
#    (que guarda el pts y no el dts), se lee desde el principio y se pasa a 120 fps fijos (fps=120 repite
#    el último fotograma, y 120 deja que una toma a cámara lenta no pierda fotogramas), y la ventana se corta
#    después (trim). Con «-ss» delante de «-i», una ventana que cae en un tramo quieto sale vacía.
# 2. EL PRECIO SE TAPA AQUÍ, en píxeles de la grabación («velos» en tomas.json: y0, y1 y el color de
#    debajo), antes de recortar y escalar. Así el velo cae exacto en cada fotograma de la toma y no depende
#    de que el vídeo y una capa de la página vayan a la par. Se pinta en RGB, con el color medido en la
#    grabación, para que no quede un rectángulo de otro tono.
#
# Las grabaciones son las de capturas/muestras.sh del repo de la app (recorrido-muestras-hoja, -itinerario,
# -paseo, -museo e -ia, 7-nov): 1206×2622, sin sonido. Sin la barra de estado ni la barra de inicio, como
# en asi-funciona: la grabación lleva pintada la isla negra del iPhone, y con ella el borde verde sería el
# dibujo de un iPhone, que Apple no deja (../incluye-pago/README.md). Medido en estas grabaciones (7-nov):
# la hora y la isla acaban en y 150 y la barra de inicio va de 2583 a 2597, así que se quitan 168 px de
# arriba y 48 de abajo, lo mismo que en asi-funciona.
#
# Uso: METRAJE=/ruta/a/las/grabaciones python3 -I cortar-tomas.py [tomas.json]
import json, os, subprocess, sys, tempfile
VELOCIDAD = 1.15
D = os.path.dirname(os.path.abspath(__file__))
args = [x for x in sys.argv[1:] if not x.startswith('--')]
tomas = json.load(open(os.path.join(D, args[0] if args else 'tomas.json'), encoding='utf-8'))
os.makedirs(os.path.join(D, 'assets/tomas'), exist_ok=True)
M = os.environ.get('METRAJE') or sys.exit('falta METRAJE=<carpeta con recorrido-muestras-*.mp4>')
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
