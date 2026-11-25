# LAS TOMAS DE LA APP (25-nov): de las grabaciones del simulador a los trozos que van dentro del móvil.
#
# Las grabaciones salen del guion `reel` de capturas/ del repo de la app (NOMAD, capturas/reel.sh): un
# vídeo por frase del guion, 1206 x 2622, sin sonido. NO están en este repo: cada una empieza en «Hoy»,
# donde se ve el código de invitación del viaje demo. Aquí sólo se usa lo de dentro del viaje.
#
# tomas.json dice, de cada momento, qué trozos de qué grabación se usan (en segundos de la grabación) y
# desde qué altura se enseña la pantalla (y0, en píxeles de la grabación). Este guion:
#   1. junta los trozos y los ajusta a lo que dura su momento (assets/tiempos.json): la velocidad sale
#      sola, y si pasa de 2x o baja de 0,6x avisa, porque se nota;
#   2. recorta desde y0, reduce a 680 de ancho (el móvil de index.html) y escribe assets/tomas/<id>.mp4;
#   3. pone los <video> en index.html, entre las marcas TOMAS, con su hora de entrada y su duración.
#
# Uso: METRAJE=<carpeta con recorrido-reel-*.mp4> python3 -I cortar-tomas.py
import json, os, re, subprocess, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
os.chdir(AQUI)
M = os.environ.get('METRAJE') or sys.exit('falta METRAJE=<carpeta con recorrido-reel-*.mp4>')
T = json.load(open('assets/tiempos.json'))
C = T['cortes']
ANCHO, ALTO_MOVIL = 680, 1300
# Qué momento del vídeo ocupa cada toma: de qué corte a qué corte.
MOMENTOS = {'plan': ('plan', 'plaza'), 'paseo': ('plaza', 'comer'), 'lugares': ('comer', 'cuentas'),
            'gastos': ('cuentas', 'asistente'), 'asistente': ('asistente', 'oferta')}
os.makedirs('assets/tomas', exist_ok=True)
tags = []
for t in json.load(open('tomas.json')):
    de, a = MOMENTOS[t['id']]
    dur = round(C[a] - C[de], 3)
    fuente = sum(s[1] - s[0] for s in t['trozos'])
    vel = fuente / dur
    if not 0.6 <= vel <= 2.0:
        print(f"OJO {t['id']}: {fuente:.2f} s de grabación en {dur:.2f} s de vídeo es {vel:.2f}x")
    f = os.path.join(M, t['fichero'])
    alto_fuente = min(2622 - t['y0'], int(ALTO_MOVIL * 1206 / ANCHO))
    alto_fuente -= alto_fuente % 2
    # Lo que se ve del móvil va de y=730 al borde del vídeo: 1190 px. Si la grabación se acaba antes
    # queda un hueco. Se rellena sólo si las 20 últimas filas de la pantalla son de un color liso (el
    # fondo de debajo de la barra de inicio): entonces el relleno no se distingue. Si llevan texto, se
    # para. Repetir la última fila no vale: con texto salen rayas.
    alto = int(alto_fuente * ANCHO / 1206); alto -= alto % 2
    falta = max(0, 1190 - alto)
    alarga = ''
    if falta:
        crudo = subprocess.run(['ffmpeg', '-v', 'error', '-i', f, '-vf', f"fps=30,trim=start={t['trozos'][-1][1] - 0.1},crop=1206:20:0:2602,format=rgb24",
                                '-frames:v', '1', '-f', 'rawvideo', '-'], capture_output=True, check=True).stdout
        pie = [crudo[i:i + 3] for i in range(0, len(crudo), 3)]
        if len(set(pie)) != 1 or falta > 120:
            sys.exit(f"{t['id']}: desde y={t['y0']} la grabación no llena el móvil (faltan {falta} px) y su pie no es liso")
        alarga = f",pad={ANCHO}:1190:0:0:color=0x{pie[0].hex()}"
    n = len(t['trozos'])
    # Las grabaciones del simulador sólo guardan un fotograma cuando la pantalla cambia. Sin pasarlas
    # antes a 30 por segundo, un trozo que empieza con la pantalla quieta pierde esa espera: trim salta
    # al primer fotograma que haya, que es ya el del cambio.
    fijo = f"[0:v]fps=30,split={n}" + ''.join(f'[s{i}]' for i in range(n)) + ';'
    partes = fijo + ''.join(f"[s{i}]trim=start={s[0]}:end={s[1]},setpts=PTS-STARTPTS[p{i}];" for i, s in enumerate(t['trozos']))
    junta = ''.join(f'[p{i}]' for i in range(n)) + f'concat=n={n}:v=1:a=0[j];'
    grafo = (partes + junta + f"[j]crop=1206:{alto_fuente}:0:{t['y0']},scale={ANCHO}:{alto}:flags=lanczos{alarga},"
             f"setpts=PTS/{vel:.6f},fps=30[v]")
    sal = f"assets/tomas/{t['id']}.mp4"
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', f, '-filter_complex', grafo, '-map', '[v]', '-an', '-t', f'{dur:.3f}',
                    '-c:v', 'libx264', '-crf', '15', '-preset', 'slow', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', sal], check=True)
    real = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', sal],
                                capture_output=True, text=True).stdout)
    print(f"{t['id']}: {n} trozo(s), {fuente:.2f} s a {vel:.2f}x → {real:.2f} s (su momento dura {dur:.2f}), desde y={t['y0']}")
    tags.append(f'          <video id="toma-{t["id"]}" class="toma clip" src="{sal}" data-start="{C[de]}" '
                f'data-duration="{dur}" muted playsinline></video>')
h = open('index.html', encoding='utf-8').read()
h2 = re.sub(r'(<!-- TOMAS:[^\n]*-->\n).*?([ \t]*<!-- /TOMAS -->)', lambda m: m.group(1) + ''.join(t + '\n' for t in tags) + '          <!-- /TOMAS -->', h, flags=re.S)
if h2 == h and tags: print('index.html: las tomas ya estaban puestas así')
open('index.html', 'w', encoding='utf-8').write(h2)
print(f'index.html: {len(tags)} tomas puestas')
