# EL PLAN DE ROMA — carrusel de 5 tarjetas para el feed (6-sep).
#
# POR QUÉ EXISTE, y el número que lo obligó: el reel del 3-sep llegó a 1 258 espectadores
# y se guardó CERO veces. Los guardados son la moneda del alcance orgánico, y un demo de
# producto no se guarda. Un itinerario sí. Así que aquí el protagonista es EL PLAN y la
# app baja al pie: «esto lo escribió NOMAD en menos de un minuto».
#
# Y resuelve la contradicción que arrastraba todo lo anterior: el plan sirve HOY, aunque
# la app no se pueda usar hasta octubre.
#
# EL PLAN ES REAL, leído fotograma a fotograma de la grabación del 3-sep (jueves 03 sept,
# 5 planes · 52 €). Las cuentas cuadran solas: 25 + 5 + 22 = 52. No se inventa ni una
# línea; si algún día cambia el plan de la app, se vuelve a leer de una grabación nueva.
#
# Uso, desde salida/ (piezas/preparar.sh la monta):  python3 ../piezas/roma/gen-plan-roma.py
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tarjetas import (W, H, SOMBRA, MENTA, PAPEL, NOCHE, VELO_FOTO, VELO_TELEFONO,
                      pagina as _pagina, raiz, foto, velo, kicker, titular, sub, marca, telefono)

HELMET = open('Main.dc.html').read().split('<helmet>')[1].split('</helmet>')[0]
pagina = lambda cuerpo: _pagina(cuerpo, HELMET)

# El jueves, tal como lo escribió la app. (hora, qué, categoría, precio, ¿es gratis?)
JUEVES = [
    ('10:30', 'Llegada y traslado al centro',                 'Transporte', 'gratis', True),
    ('11:30', 'Tour por el Centro Hist&oacute;rico y las Plazas', 'Tour guiado', 'gratis', True),
    ('14:15', 'Comida en Armando al Pantheon',                 'Comida',     '25 &euro;', False),
    ('16:00', 'Visita al Pante&oacute;n de Agripa',                 'Museo',      '5 &euro;',  False),
    ('19:30', 'Cena en Rifugio Romano',                        'Comida',     '22 &euro;', False),
]

def fila(hora, que, cat, precio, gratis, y):
    """Una parada del plan. La hora en serif a la izquierda, como en la app; lo gratis en
    menta, porque es lo que sorprende y es lo que hace que la tarjeta se guarde."""
    c = MENTA if gratis else 'rgba(255, 253, 249, 0.62)'
    return (f'<div style="position: absolute; left: 84px; top: {y}px; width: 912px; display: flex; gap: 34px">'
            f'<span class="serif" style="font-size: 46px; line-height: 1.1; color: rgba(255, 253, 249, 0.55); '
            f'width: 130px; flex: none">{hora}</span>'
            f'<span style="display: block">'
            f'<span class="sans" style="display: block; font-size: 40px; line-height: 1.22; font-weight: 600">{que}</span>'
            f'<span class="sans" style="display: block; font-size: 30px; line-height: 1.5; margin-top: 6px; '
            f'color: {c}; font-weight: 600">{cat} &middot; {precio}</span></span></div>')

T = {}

# 1 · PORTADA. El gancho es el número: un día entero de Roma por lo que cuesta una cena.
T['roma-1'] = (raiz()
  + foto('f-portada.jpg', 1.06)
  + velo(VELO_FOTO)
  + kicker('Un d&iacute;a en Roma')
  + titular('Un jueves entero,<br>por 52&nbsp;&euro;.', 180, 104)
  + sub('Hora a hora y con precios. Dos de las cinco cosas del d&iacute;a no cuestan nada.', 430, 38, ancho=860)
  + marca()
  + '</div>')

# 2 · EL DÍA ENTERO. ESTA es la tarjeta que se guarda: sin foto, sin adornos, legible.
T['roma-2'] = (raiz(NOCHE)
  + kicker('Jueves &middot; 5 planes &middot; 52&nbsp;&euro;', 110, MENTA)
  + ''.join(fila(*p, 240 + i * 172) for i, p in enumerate(JUEVES))
  + '<div style="position: absolute; left: 84px; top: 1136px; width: 912px; height: 1px; '
    'background: rgba(255, 253, 249, 0.16)"></div>'
  + sub('El d&iacute;a entero, con las dos comidas y el museo: <b>52&nbsp;&euro;</b>.', 1180, 34,
        'rgba(255, 253, 249, 0.8)')
  + '</div>')

# 3 · LO QUE NO CUESTA NADA. El tour a pie es el foso del producto y sale gratis dentro
#     del viaje; la instrucción de la parada 1 es literal de la app.
T['roma-3'] = (raiz()
  + foto('f-grupo.jpg', 1.06)
  + velo(VELO_FOTO)
  + kicker('Lo que no cuesta nada')
  + titular('El tour a pie<br>va incluido.', 180, 96)
  + sub('Seis paradas por las plazas del centro, 130 minutos, y una voz que te va '
        'contando cada una.', 420, 38, ancho=860)
  + sub('Sin reservar, sin grupo y sin propina.', 570, 38, 'rgba(255, 253, 249, 0.72)', ancho=860)
  + marca()
  + '</div>')

# 4 · CÓMO SE HIZO. La captura es de la app real, del mismo jueves de la tarjeta 2.
T['roma-4'] = (raiz()
  + foto('f-museo.jpg', 1.06)
  + velo(VELO_TELEFONO)
  + kicker('C&oacute;mo se hizo')
  + titular('Dijimos &laquo;Roma,<br>3 d&iacute;as&raquo;.', 180, 96)
  + sub('Y esto sali&oacute; en menos de un minuto.', 400, 38)
  + telefono('planjueves-900.webp', 430, 520)
  + '</div>')

# 5 · CIERRE. El mismo de qe-7 y del reel: sin cuenta atrás y con el asterisco explicado.
T['roma-5'] = (raiz()
  + foto('f-oferta.jpg', 1.04)
  + velo('linear-gradient(180deg, rgba(16, 14, 11, 0.6) 0%, rgba(16, 14, 11, 0.34) 32%, '
         'rgba(16, 14, 11, 0.9) 100%)')
  + kicker('Todav&iacute;a no est&aacute; publicada')
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
