# Corta las tomas de «Pruébalo antes de pagar», cada una a su fichero, ya a su velocidad final (la de la
# escena × VELOCIDAD), a 404×806 (el tamaño de la pantalla en el vídeo), 30 fps, sin sonido. Es el
# cortar-tomas.py de asi-funciona/ con las grabaciones nuevas.
#
# Las grabaciones son las de capturas/muestras.sh del repo de la app (bloques muestras-hoja,
# muestras-itinerario, muestras-paseo, muestras-museo y muestras-ia): vídeos verticales de 1206×2622 a
# 60 fps, sin sonido. Como en asi-funciona, sin la barra de estado ni la barra de inicio: la grabación del
# simulador lleva pintada la isla negra del iPhone, y con ella el borde verde sería el dibujo de un iPhone,
# que Apple no deja (../incluye-pago/README.md). Se quitan 168 px de arriba y 48 de abajo, lo medido en las
# grabaciones de asi-funciona: con las nuevas hay que mirarlo otra vez (README.md, «Lo que falta»).
#
# Los cortes de tomas.json son una ESTIMACIÓN («revisar»: true) hecha antes de que llegaran las
# grabaciones. Al llegar se miran a 10 fps, se ajustan entrada y salida, y se quita la marca.
#
# Sin grabaciones, --provisional escribe en su lugar una toma de prueba por escena, del mismo tamaño y la
# misma duración: el fondo de la app, el nombre de la toma, lo que tendrá que enseñar y una barra que corre
# arriba (para que se vea que la toma avanza). Las de la hoja (s2b y s7) llevan además un botón con
# «$2.99» abajo, donde estará el precio, para comprobar que el velo lo tapa.
#
# Uso: METRAJE=/ruta/a/videos python3 -I cortar-tomas.py [tomas.json]
#      python3 -I cortar-tomas.py --provisional
import json, os, subprocess, sys, tempfile
VELOCIDAD = 1.15
D = os.path.dirname(os.path.abspath(__file__))
args = [x for x in sys.argv[1:] if not x.startswith('--')]
PROVISIONAL = '--provisional' in sys.argv
tomas = json.load(open(os.path.join(D, args[0] if args else 'tomas.json'), encoding='utf-8'))
os.makedirs(os.path.join(D, 'assets/tomas'), exist_ok=True)
FONDO = '#FCFAF6'          # el fondo de la app (el del velo de asi-funciona)
VERDE = '#0F766E'
CON_PRECIO = {'s2b', 's7'}  # las tomas de la hoja: el precio sale abajo, en el botón


def provisional(t, dura, sal):
    from PIL import Image, ImageDraw, ImageFont
    def letra(n, negrita=False):
        f = '/usr/share/fonts/truetype/dejavu/DejaVuSans' + ('-Bold' if negrita else '') + '.ttf'
        return ImageFont.truetype(f, n)
    im = Image.new('RGBA', (404, 806), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.text((202, 300), t['id'], font=letra(96, True), fill=VERDE, anchor='mm')
    d.text((202, 372), 'TOMA PROVISIONAL', font=letra(20, True), fill='#100E0B', anchor='mm')
    d.text((202, 404), t['fichero'] + f"  {t['entrada']:.2f}–{t['salida']:.2f}", font=letra(17), fill='#6B655C', anchor='mm')
    # Lo que tendrá que enseñar, en renglones de 30 letras.
    pal, ren, r = t.get('que', '').split(), [], ''
    for p in pal:
        if len(r) + len(p) + 1 > 30: ren.append(r); r = p
        else: r = (r + ' ' + p).strip()
    if r: ren.append(r)
    for k, r in enumerate(ren):
        d.text((202, 450 + 28 * k), r, font=letra(19), fill='#3B3731', anchor='mm')
    if t['id'] in CON_PRECIO:
        d.rounded_rectangle([24, 716, 380, 770], radius=27, fill=VERDE)
        d.text((202, 743), 'Generar mi itinerario · $2.99', font=letra(18, True), fill='#FFFDF9', anchor='mm')
    with tempfile.TemporaryDirectory() as tmp:
        png = os.path.join(tmp, 't.png'); im.save(png)
        subprocess.run(['ffmpeg', '-v', 'error', '-y',
                        '-f', 'lavfi', '-i', f'color=c={FONDO}:s=404x806:r=30:d={dura:.3f}',
                        '-loop', '1', '-r', '30', '-i', png,
                        '-f', 'lavfi', '-i', f'color=c={VERDE}:s=404x8:r=30:d={dura:.3f}',
                        '-filter_complex', f"[0][1]overlay=0:0:shortest=1[a];[a][2]overlay=x='-w+w*t/{dura:.3f}':y=0:eval=frame:shortest=1,format=yuv420p",
                        '-t', f'{dura:.3f}', '-an', '-c:v', 'libx264', '-crf', '18', '-g', '15', '-movflags', '+faststart', sal], check=True)


if not PROVISIONAL:
    M = os.environ.get('METRAJE') or sys.exit('falta METRAJE=<carpeta con muestras-*.mp4> (o --provisional)')
for t in tomas:
    largo = t['salida'] - t['entrada']                 # segundos de grabación
    dura = (t['fin'] - t['inicio']) / VELOCIDAD        # segundos que se ve en el vídeo final
    v = largo / dura
    sal = os.path.join(D, 'assets/tomas', t['id'] + '.mp4')
    if PROVISIONAL:
        provisional(t, dura, sal)
    else:
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f"{t['entrada']:.3f}", '-t', f'{largo:.3f}',
                        '-i', os.path.join(M, t['fichero']), '-vf', f'setpts=(PTS-STARTPTS)/{v:.6f},fps=30,crop=1206:2406:0:168,scale=404:806:flags=lanczos',
                        '-an', '-c:v', 'libx264', '-crf', '14', '-preset', 'slow', '-g', '15', '-pix_fmt', 'yuv420p',
                        '-movflags', '+faststart', sal], check=True)
    real = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', sal],
                                capture_output=True, text=True).stdout)
    marca = '  (PROVISIONAL)' if PROVISIONAL else ('  (corte por revisar)' if t.get('revisar') else '')
    print(f"{t['id']}: {t['fichero']} {t['entrada']}-{t['salida']} a {v:.3f}× → {real:.3f} s "
          f"(data-start {t['inicio'] / VELOCIDAD:.3f}, data-duration {dura:.3f}){marca}")
