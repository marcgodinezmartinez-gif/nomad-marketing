# LAS HISTORIAS DIARIAS DE LA MERCÈ (21-sep), 1080×1920, una por día del 23 al 27.
#
# Idea del dueño: «cuando empiecen los días de fiesta, poner historias con el planning que
# dé la app para cada día». Es la mejor forma de enseñar la app sin que parezca un anuncio:
# el plan de HOY, en un sitio donde hoy hay medio millón de personas.
#
# CÓMO SE USA, cada mañana de la fiesta:
#   1. En la app: nuevo viaje a Barcelona para ese día (o el plan ya generado, día a día).
#      Captura de la pantalla del plan, vertical, con la barra de estado.
#   2. Se guarda como banco/capturas/planmerce-<día>-900.webp (planmerce-24-900.webp…).
#   3. bash piezas/preparar.sh && cd salida
#      python3 ../piezas/merce/gen-historias.py
#      node ../piezas/roma/exportar-plan.mjs mercehist 5 1080 1920
#      (mercehist-1 … mercehist-5 son los días 23, 24, 25, 26 y 27, en ese orden: el
#       exportador numera 1..N y no sabe de fechas. Las CAPTURAS sí llevan el día en el
#       nombre, que es donde importa no equivocarse.)
#   4. Se sube con el ADHESIVO DE ENLACE, que es lo que hace que esto sirva de algo:
#      https://travelsnomad.com/?utm_source=instagram&utm_medium=organic&utm_campaign=merce-dia
#
# ZONAS SEGURAS de una historia (AGENTS.md): la interfaz tapa unos 250 px arriba y abajo. El
# texto vive entre y=280 e y=1500, y de y=1520 para abajo va el adhesivo. Por eso el móvil
# acaba en 1493 y debajo no hay nada: ese hueco es del adhesivo, no del diseño.
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tarjetas import MENTA, SOMBRA, NOCHE

W, H = 1080, 1920
HELMET = open('Main.dc.html').read().split('<helmet>')[1].split('</helmet>')[0]

# (día del mes, cómo se dice, la foto de fondo)
DIAS = [
    ('23', 'mi&eacute;rcoles 23', 'f-merce-castell.jpg'),
    ('24', 'jueves 24',           'f-merce-castell2.jpg'),
    ('25', 'viernes 25',          'f-bcn-noche.jpg'),
    ('26', 's&aacute;bado 26',           'f-merce-diable.jpg'),
    ('27', 'domingo 27',          'f-merce-espurnes.jpg'),
]

VELO = ('linear-gradient(180deg, rgba(16, 14, 11, 0.84) 0%, rgba(16, 14, 11, 0.6) 32%, '
        'rgba(16, 14, 11, 0.72) 100%)')

def hay(f, carpeta='fotos-historia'):
    return os.path.exists(f'{carpeta}/{f}' if carpeta else f)

def telefono(png, ancho=440, arriba=540):
    """El móvil de la casa a escala de historia. 9:19,5 como el iPhone; con ancho 440 el alto
    sale 953 y el conjunto acaba en 1493, justo dentro de la zona segura."""
    return (f'<div style="position: absolute; left: 50%; top: {arriba}px; transform: translateX(-50%); '
            f'width: {ancho}px; aspect-ratio: 9 / 19.5; background: #0b0b0d; border-radius: 60px; padding: 13px; '
            f'box-shadow: 0 50px 120px rgba(0, 0, 0, 0.65)">'
            f'<div style="position: absolute; inset: 0; border-radius: 60px; border: 4px solid #98979c"></div>'
            f'<div style="position: absolute; top: 26px; left: 50%; transform: translateX(-50%); width: 132px; '
            f'height: 37px; background: #0b0b0d; border-radius: 20px; z-index: 2"></div>'
            f'<div style="width: 100%; height: 100%; border-radius: 47px; background: #F5F0E8; overflow: hidden">'
            f'<img src="{png}" alt="" style="width: 100%; display: block"></div></div>')

def pendiente(ancho=440, arriba=540):
    return (f'<div style="position: absolute; left: 50%; top: {arriba}px; transform: translateX(-50%); '
            f'width: {ancho}px; aspect-ratio: 9 / 19.5; border: 4px dashed #E4572E; border-radius: 60px; '
            f'display: flex; align-items: center; justify-content: center; text-align: center">'
            f'<p class="sans" style="margin: 0; font-size: 28px; line-height: 1.5; font-weight: 700; '
            f'color: #E4572E; letter-spacing: 0.04em">FALTA LA CAPTURA<br>del plan de la app<br>para este d&iacute;a</p></div>')

faltan = []
for i, (dia, como, foto) in enumerate(DIAS, 1):
    captura = f'planmerce-{dia}-900.webp'
    fondo = (f'<img src="fotos-historia/{foto}" alt="" style="position: absolute; inset: 0; width: 100%; height: 100%; '
             f'object-fit: cover; display: block">' if hay(foto) else '')
    cuerpo = (f'<div style="width: {W}px; height: {H}px; box-sizing: border-box; position: relative; '
              f'overflow: hidden; background: {NOCHE}; color: #FFFDF9">'
              + fondo
              + f'<div style="position: absolute; inset: 0; background: {VELO}"></div>'
              + f'<p class="sans" style="position: absolute; left: 84px; top: 290px; margin: 0; font-size: 32px; '
                f'letter-spacing: 0.18em; text-transform: uppercase; color: {MENTA}; font-weight: 600; {SOMBRA}">'
                f'La Merc&egrave; &middot; {como}</p>'
              + f'<h1 class="serif" style="position: absolute; left: 84px; top: 340px; margin: 0; width: 912px; '
                f'font-size: 86px; line-height: 1.06; letter-spacing: -0.018em; font-weight: 400; {SOMBRA}">'
                f'El plan de hoy.</h1>'
              + f'<p class="sans" style="position: absolute; left: 84px; top: 456px; margin: 0; width: 860px; '
                f'font-size: 36px; line-height: 1.35; color: rgba(255, 253, 249, 0.86); font-weight: 500; {SOMBRA}">'
                f'Se lo pedimos a NOMAD y lo escribi&oacute; en menos de un minuto.</p>'
              + (telefono(captura) if hay(captura, '') else pendiente())
              + '</div>')
    open(f'mercehist-{i}.dc.html', 'w').write(
        '<!doctype html>\n<html>\n<head>\n  <meta charset="utf-8">\n'
        '  <script src="./support.js"></script>\n  <style>body { margin: 0 }</style>\n</head>\n<body>\n<x-dc>\n'
        '<helmet>' + HELMET + '</helmet>\n' + cuerpo + '\n</x-dc>\n</body>\n</html>\n')
    if not hay(captura, ''): faltan.append(captura)

print(f'{len(DIAS)} historias: ' + ', '.join(f'mercehist-{i} = día {d}' for i, (d, _, _) in enumerate(DIAS, 1)))
print('Se exportan con:  node ../piezas/roma/exportar-plan.mjs mercehist 5 1080 1920')
if faltan: print('FALTAN, y la historia lo dice en naranja: ' + ', '.join(faltan))
