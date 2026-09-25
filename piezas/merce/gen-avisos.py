# LOS DOS AVISOS DE LA MERCÈ (25-sep), 1080×1920: el correfoc y el piromusical.
#
# POR QUÉ EXISTEN, y por qué no son las historias diarias: las diarias enseñan la captura de
# la app tal cual, y la app puso mal la hora y el sitio de los cinco actos de la fiesta
# (issue #6). Las del sábado y el domingo no se pueden subir. Pero justo esos dos actos son
# lo más buscado del fin de semana Y los dos han cambiado de sitio este año, así que la
# información buena es lo más útil que podemos publicar: no es relleno, es lo único de esta
# semana que alguien reenvía por WhatsApp.
#
# Una historia no se comparte por bonita, se comparte porque resuelve algo. Aquí el dato
# grande va en serif y a tamaño de titular, y debajo va lo práctico.
#
# Uso, desde salida/:  python3 ../piezas/merce/gen-avisos.py
#                      node ../piezas/roma/exportar-plan.mjs merceaviso 2 1080 1920
#
# Se suben CON EL ADHESIVO DE ENLACE, de 1520 para abajo:
#   https://travelsnomad.com/?utm_source=instagram&utm_medium=organic&utm_campaign=merce-aviso
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tarjetas import MENTA, PAPEL, SOMBRA, NOCHE

W, H = 1080, 1920
HELMET = open('Main.dc.html').read().split('<helmet>')[1].split('</helmet>')[0]

# Cerrado de la mitad para abajo: el dato vive ahí y tiene que leerse a pulso, en la calle,
# con sol y a una mano.
VELO = ('linear-gradient(180deg, rgba(16, 14, 11, 0.7) 0%, rgba(16, 14, 11, 0.42) 22%, '
        'rgba(16, 14, 11, 0.88) 48%, rgba(16, 14, 11, 0.96) 100%)')

AVISOS = [
  dict(stem='merceaviso-1', foto='f-merce-diable.jpg',
       cuando='S&aacute;bado 26', que='El correfoc.',
       hora='20:30', donde='Passeig de Gr&agrave;cia',
       recorrido='De Proven&ccedil;a a Consell de Cent, con la Porta de l&rsquo;Infern en Proven&ccedil;a.',
       ojo='Ya no pasa por Via Laietana: cambi&oacute; en 2022.',
       practico='A las 18 h es el de los peque&ntilde;os, el mismo recorrido al rev&eacute;s. '
                'Si te metes: algod&oacute;n de manga larga, zapato cerrado, gorro y gafas.'),
  dict(stem='merceaviso-2', foto='f-merce-espurnes.jpg',
       cuando='Domingo 27', que='El piromusical.',
       hora='22:00', donde='Platja de la Nova Ic&agrave;ria',
       recorrido='Se dispara desde el espig&oacute;n del Bogatell y se ve desde toda esa playa.',
       ojo='Ya no es en Montju&iuml;c: se ha movido por las obras de la Fira.',
       practico='Media hora de espect&aacute;culo, y cierra la fiesta. La m&uacute;sica la ha elegido '
                'Josep Montero, de Oques Grasses.'),
]

def texto(t, y, size, color=PAPEL, peso=500, familia='sans', alto=1.36, ancho=912):
    return (f'<p class="{familia}" style="position: absolute; left: 84px; top: {y}px; margin: 0; '
            f'width: {ancho}px; font-size: {size}px; line-height: {alto}; color: {color}; '
            f'font-weight: {peso}; text-wrap: pretty; {SOMBRA}">{t}</p>')

for a in AVISOS:
    cuerpo = (f'<div style="width: {W}px; height: {H}px; box-sizing: border-box; position: relative; '
              f'overflow: hidden; background: {NOCHE}; color: {PAPEL}">'
      + f'<img src="fotos-historia/{a["foto"]}" alt="" style="position: absolute; inset: 0; width: 100%; '
        f'height: 100%; object-fit: cover; display: block">'
      + f'<div style="position: absolute; inset: 0; background: {VELO}"></div>'
      # arriba, dentro de la zona segura (la interfaz tapa unos 250 px)
      + (f'<p class="sans" style="position: absolute; left: 84px; top: 296px; margin: 0; font-size: 32px; '
         f'letter-spacing: 0.18em; text-transform: uppercase; color: {MENTA}; font-weight: 600; {SOMBRA}">'
         f'La Merc&egrave; &middot; {a["cuando"]}</p>')
      + texto(a['que'], 348, 92, familia='serif', peso=400, alto=1.06)
      # EL DATO. Lo único que alguien necesita recordar de esta historia.
      + texto(a['hora'], 520, 176, MENTA, 400, 'serif', 1.0)
      + texto(a['donde'], 730, 60, PAPEL, 600, 'serif', 1.14)
      + texto(a['recorrido'], 850, 36, 'rgba(255, 253, 249, 0.82)')
      # la línea que hace que se reenvíe
      + (f'<div style="position: absolute; left: 84px; top: 990px; width: 912px; box-sizing: border-box; '
         f'padding: 26px 30px; border-radius: 22px; background: rgba(92, 192, 166, 0.14); '
         f'border-left: 6px solid {MENTA}">'
         f'<span class="sans" style="font-size: 38px; line-height: 1.3; font-weight: 600; color: {PAPEL}">'
         f'{a["ojo"]}</span></div>')
      + texto(a['practico'], 1150, 34, 'rgba(255, 253, 249, 0.76)')
      # y sólo entonces, la marca
      + (f'<div style="position: absolute; left: 84px; top: 1370px; display: flex; align-items: center; gap: 20px">'
         f'<img src="mark.png" alt="" style="width: 56px; height: 56px">'
         f'<span class="sans" style="font-size: 30px; color: rgba(255, 253, 249, 0.85); font-weight: 600; '
         f'letter-spacing: 0.02em; {SOMBRA}">travelsnomad.com</span></div>')
      + '</div>')
    open(f'{a["stem"]}.dc.html', 'w').write(
        '<!doctype html>\n<html>\n<head>\n  <meta charset="utf-8">\n'
        '  <script src="./support.js"></script>\n  <style>body { margin: 0 }</style>\n</head>\n<body>\n<x-dc>\n'
        '<helmet>' + HELMET + '</helmet>\n' + cuerpo + '\n</x-dc>\n</body>\n</html>\n')

print(f'{len(AVISOS)} avisos: ' + ', '.join(a['stem'] for a in AVISOS))
print('Se exportan con:  node ../piezas/roma/exportar-plan.mjs merceaviso 2 1080 1920')
print('El texto acaba en 1426: de 1520 abajo queda libre para el adhesivo de enlace.')
