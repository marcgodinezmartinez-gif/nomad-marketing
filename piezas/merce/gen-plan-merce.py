# «LE PEDIMOS A NOMAD UN JUEVES DE MERCÈ» — carrusel de 5 tarjetas (21-sep).
#
# EL GIRO QUE PIDIÓ EL DUEÑO ese día: «no me acaba de gustar como lo he enfocado, es como
# que no hablo de la app». Tenía razón, y el repo se la daba: los tres carruseles de
# «¿Conocías este lugar?» enseñan un dato bonito y esconden la app en la tarjeta 5 de 6, y
# eso es justo lo que NO nos diferencia — la competencia curada ya cuenta bien seis
# ciudades, y mil cuentas de curiosidades tienen más volumen que nosotros.
#
# Lo que sí nos diferencia, según campana/MERCADO: LA GENERACIÓN. Cualquier sitio, cualquier
# tema, y el plan entero con precios. Así que aquí el protagonista vuelve a ser EL PLAN, como
# en el carrusel de Roma, y la app es quien lo escribió.
#
# POR QUÉ LA MERCÈ Y POR QUÉ HOY: la fiesta va del 23 al 27, la ciudad está llena, y el
# gancho se escribe solo porque casi todos los actos son gratis. Un plan de fiesta local es
# además la prueba de la cola larga: ninguna guía curada tiene el jueves de la Mercè.
#
# EL PLAN TIENE QUE SER EL REAL DE LA APP. Aquí no se inventa ni una línea: se lee de la
# captura que trae el dueño, como se hizo con el jueves de Roma (fotograma a fotograma). Si
# JUEVES sigue vacío, el generador PARA y dice qué falta — una tarjeta con un plan inventado
# sería exactamente la promesa que la app no cumple.
#
# Uso, desde salida/:  python3 ../piezas/merce/gen-plan-merce.py
#                      node ../piezas/roma/exportar-plan.mjs planmerce 5
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tarjetas import (SOMBRA, MENTA, NOCHE, VELO_FOTO, VELO_TELEFONO,
                      pagina as _pagina, raiz, foto, velo, kicker, titular, sub, marca, telefono)

HELMET = open('Main.dc.html').read().split('<helmet>')[1].split('</helmet>')[0]
pagina = lambda cuerpo: _pagina(cuerpo, HELMET)

CAPTURA = 'planmerce-24-900.webp'     # la pantalla del plan del jueves, de la app real

# EL PLAN DEL JUEVES 24, tal como lo escriba la app. Se rellena LEYENDO la captura:
# (hora, qué, categoría, precio, ¿es gratis?). Ejemplo del formato, del jueves de Roma:
#   ('11:30', 'Tour por el Centro Hist&oacute;rico', 'Tour guiado', 'gratis', True),
JUEVES = [
]
TOTAL = None        # el total del día, tal como lo diga la app: 'gratis', '18 €'…
CUANTOS = None      # cuántos planes trae el día, tal como lo diga la app

def fila(hora, que, cat, precio, gratis, y):
    """Una parada del plan. La hora en serif a la izquierda, como en la app; lo gratis en
    menta, porque en la Mercè es casi todo y es lo que hace que la tarjeta se guarde."""
    c = MENTA if gratis else 'rgba(255, 253, 249, 0.62)'
    return (f'<div style="position: absolute; left: 84px; top: {y}px; width: 912px; display: flex; gap: 34px">'
            f'<span class="serif" style="font-size: 46px; line-height: 1.1; color: rgba(255, 253, 249, 0.55); '
            f'width: 130px; flex: none">{hora}</span>'
            f'<span style="display: block">'
            f'<span class="sans" style="display: block; font-size: 40px; line-height: 1.22; font-weight: 600">{que}</span>'
            f'<span class="sans" style="display: block; font-size: 30px; line-height: 1.5; margin-top: 6px; '
            f'color: {c}; font-weight: 600">{cat} &middot; {precio}</span></span></div>')

def hay(f, carpeta='fotos'):
    return os.path.exists(f'{carpeta}/{f}' if carpeta else f)

if not JUEVES:
    sys.exit('FALTA EL PLAN. Abre la app, pide Barcelona para el jueves 24 y rellena JUEVES,\n'
             'TOTAL y CUANTOS leyendo la pantalla. No se inventa ni una línea: un plan\n'
             'inventado es la promesa que la app no cumple.\n'
             f'Y guarda la captura como banco/capturas/{CAPTURA}.')

T = {}

# 1 · PORTADA. El gancho es el precio del día entero, que en la Mercè es casi nada.
T['planmerce-1'] = (raiz(NOCHE)
  + foto('f-merce-castell.jpg', 1.06) + velo(VELO_FOTO)
  + kicker('La Merc&egrave; &middot; jueves 24')
  + titular(f'Un jueves entero<br>de Merc&egrave;, por {TOTAL}.', 180, 96)
  + sub('Hora a hora y con precios. Se lo pedimos a NOMAD.', 430, 38, ancho=860)
  + marca()
  + '</div>')

# 2 · EL DÍA ENTERO. ESTA es la que se guarda: sin foto, sin adornos, legible.
T['planmerce-2'] = (raiz(NOCHE)
  + kicker(f'Jueves 24 &middot; {CUANTOS} planes &middot; {TOTAL}', 110, MENTA)
  + ''.join(fila(*p, 240 + i * 172) for i, p in enumerate(JUEVES))
  + '<div style="position: absolute; left: 84px; top: 1136px; width: 912px; height: 1px; '
    'background: rgba(255, 253, 249, 0.16)"></div>'
  + sub(f'El d&iacute;a entero: <b>{TOTAL}</b>.', 1180, 34, 'rgba(255, 253, 249, 0.8)')
  + '</div>')

# 3 · LO QUE NO CUESTA NADA. En la Mercè es casi todo, y es el argumento del producto.
T['planmerce-3'] = (raiz(NOCHE)
  + foto('f-merce-espurnes.jpg', 1.06) + velo(VELO_FOTO)
  + kicker('Lo que no cuesta nada')
  + titular('Casi toda la fiesta.', 180, 96)
  + sub('Los castells, la cercavila de gegants, el correfoc y el piromusical son gratis. '
        'Y el tour a pie va incluido en el viaje.', 400, 38, ancho=860)
  + sub('Sin reservar, sin grupo y sin propina.', 580, 38, 'rgba(255, 253, 249, 0.72)', ancho=860)
  + marca()
  + '</div>')

# 4 · CÓMO SE HIZO. La captura es de la app real, del mismo jueves de la tarjeta 2.
T['planmerce-4'] = (raiz(NOCHE)
  + foto('f-bcn-paseo.jpg', 1.06) + velo(VELO_TELEFONO)
  + kicker('C&oacute;mo se hizo')
  + titular('Dijimos &laquo;Barcelona,<br>el jueves de la Merc&egrave;&raquo;.', 180, 88)
  + sub('Y esto sali&oacute; en menos de un minuto.', 410, 38)
  + (telefono(CAPTURA, 430, 530) if hay(CAPTURA, '') else
     sys.exit(f'FALTA LA CAPTURA {CAPTURA} en banco/capturas/'))
  + '</div>')

# 5 · EL CIERRE, el de siempre.
T['planmerce-5'] = (raiz(NOCHE)
  + foto('f-merce-diable.jpg', 1.04)
  + velo('linear-gradient(180deg, rgba(16, 14, 11, 0.6) 0%, rgba(16, 14, 11, 0.34) 32%, '
         'rgba(16, 14, 11, 0.9) 100%)')
  + kicker('Lista de espera abierta')
  + titular('Llega en octubre.', 180, 96)
  + (f'<h2 class="serif" style="position: absolute; left: 84px; top: 320px; margin: 0; width: 912px; '
     f'font-size: 84px; line-height: 1.06; letter-spacing: -0.018em; font-weight: 400; {SOMBRA}">'
     f'Tu primer viaje por <span style="color: {MENTA}">1,99&nbsp;&euro;</span>*</h2>')
  + sub('*Si te apuntas a la lista de espera en travelsnomad.com', 450, 32,
        'rgba(255, 253, 249, 0.8)')
  + marca()
  + '</div>')

for stem, html in T.items():
    open(f'{stem}.dc.html', 'w').write(pagina(html))
print(f'{len(T)} tarjetas: ' + ', '.join(T))
