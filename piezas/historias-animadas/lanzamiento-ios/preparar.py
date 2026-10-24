# Prepara assets/ del anuncio del lanzamiento (24-oct). Se corre una vez y cuando cambie
# una pantalla. Lo que escribe se versiona salvo escribir.mp4, que se rehace de la
# grabación de Córdoba (versionada en plan-cordoba/assets/) en un segundo.
#
# Uso, desde la raíz del repo de marketing:
#   python3 piezas/historias-animadas/lanzamiento-ios/preparar.py [ruta del repo de la app]
# El repo de la app (por defecto /home/user/NOMAD) sólo hace falta para volver a recortar
# eventos y gastos, que salen de las capturas en bruto de la ficha (docs/tienda/capturas/piezas).
import os, shutil, subprocess, sys
from PIL import Image

R = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
A = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets')
APP = sys.argv[1] if len(sys.argv) > 1 else '/home/user/NOMAD'
os.makedirs(A, exist_ok=True)

# Las fotos, tal cual del banco (créditos en banco/fotos/creditos.json).
for src, dst in [('f-debod-nubes.jpg', 'fondo-debod.jpg'), ('f-cordoba.jpg', 'fondo-cordoba.jpg'),
                 ('f-merce-diable.jpg', 'fondo-correfoc.jpg'), ('f-bcn-festa.jpg', 'fondo-gotic.jpg')]:
    shutil.copy(f'{R}/banco/fotos/historia/{src}', f'{A}/{dst}')
shutil.copy(f'{R}/piezas/historias-animadas/plan-cordoba/assets/gsap.min.js', f'{A}/gsap.min.js')
shutil.copy(f'{R}/banco/marca/icono-app.png', f'{A}/icono-app.png')
# La insignia oficial de Apple, sin tocar (la misma que web/insignias/app-store-es.svg de la app).
shutil.copy(f'{R}/banco/marca/insignia-app-store-es.svg', f'{A}/insignia-app-store-es.svg')

def recorte(src, caja, ancho, dst):
    im = Image.open(src).convert('RGB').crop(caja)
    im = im.resize((ancho, round(im.height * ancho / im.width)), Image.LANCZOS)
    im.save(f'{A}/{dst}', optimize=True)
    print(dst, im.size)

# La audioguía de Debod (banco/capturas/tourdebod-900.webp, 900 de ancho): del final del mapa,
# con la ruta y las paradas 4-6, a «Descargar el audio · Para oírlo sin cobertura». Sin barra
# de estado (empieza en y=510).
recorte(f'{R}/banco/capturas/tourdebod-900.webp', (0, 510, 900, 1435), 720, 'pantalla-debod.png')
# Qué hay esos días y los gastos: capturas en bruto del iPhone del dueño, 1206 de ancho.
P = f'{APP}/docs/tienda/capturas/piezas'
if os.path.exists(f'{P}/pantalla-eventos.png'):
    recorte(f'{P}/pantalla-eventos.png', (0, 200, 1206, 1400), 720, 'pantalla-eventos.png')
    # Los gastos, SOLO hasta encima de la tarjeta negra: ahí sale el nombre de una persona real.
    recorte(f'{P}/pantalla-gastos.png', (0, 400, 1206, 990), 720, 'pantalla-gastos.png')

# Escribir el viaje: tres trozos de la grabación de Córdoba (760x1652, 30 fps), cada uno con
# su ventana, a 720x700. Fotogramas: el tecleo 250-324, «Montando» 461-517 y el sábado
# 536-610. El 611 es el domingo con el Palacio de Viana mal puesto: NO entra. Antes del 461
# sale el resumen con el nombre del viaje: tampoco.
G = f'{R}/piezas/historias-animadas/plan-cordoba/assets/pantalla.mp4'
tramos = [(250, 325, 320), (461, 518, 520), (536, 611, 290)]
f = ';'.join(f'[0:v]trim=start_frame={a}:end_frame={b},setpts=PTS-STARTPTS,crop=760:739:0:{y},'
             f'scale=720:700:flags=lanczos,setsar=1[t{i}]' for i, (a, b, y) in enumerate(tramos))
f += ';' + ''.join(f'[t{i}]' for i in range(3)) + 'concat=n=3:v=1:a=0,fps=30,format=yuv420p[v]'
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', G, '-filter_complex', f, '-map', '[v]', '-an',
                '-c:v', 'libx264', '-crf', '14', '-preset', 'slow', '-movflags', '+faststart',
                f'{A}/escribir.mp4'], check=True)
print('escribir.mp4', subprocess.run(['ffprobe', '-v', 'error', '-count_frames', '-show_entries',
      'stream=nb_read_frames', '-of', 'csv=p=0', f'{A}/escribir.mp4'], capture_output=True, text=True).stdout.strip(), 'fotogramas')
