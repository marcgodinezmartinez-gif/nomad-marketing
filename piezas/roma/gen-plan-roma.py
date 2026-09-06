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
W, H = 1080, 1350
HELMET = open('Main.dc.html').read().split('<helmet>')[1].split('</helmet>')[0]
SOMBRA = 'text-shadow: 0 4px 34px rgba(0, 0, 0, 0.55)'
MENTA, PAPEL = '#5CC0A6', '#FFFDF9'
NOCHE = 'linear-gradient(160deg, #16130F 0%, #100E0B 55%, #1B2620 100%)'

# El jueves, tal como lo escribió la app. (hora, qué, categoría, precio, ¿es gratis?)
JUEVES = [
    ('10:30', 'Llegada y traslado al centro',                 'Transporte', 'gratis', True),
    ('11:30', 'Tour por el Centro Hist&oacute;rico y las Plazas', 'Tour guiado', 'gratis', True),
    ('14:15', 'Comida en Armando al Pantheon',                 'Comida',     '25 &euro;', False),
    ('16:00', 'Visita al Pante&oacute;n de Agripa',                 'Museo',      '5 &euro;',  False),
    ('19:30', 'Cena en Rifugio Romano',                        'Comida',     '22 &euro;', False),
]

def pagina(cuerpo):
    return ('<!doctype html>\n<html>\n<head>\n  <meta charset="utf-8">\n'
            '  <script src="./support.js"></script>\n  <style>body { margin: 0 }</style>\n</head>\n<body>\n<x-dc>\n'
            '<helmet>' + HELMET + '</helmet>\n' + cuerpo + '\n</x-dc>\n</body>\n</html>\n')

def raiz(fondo=None):
    f = fondo or '#100E0B'
    return (f'<div style="width: {W}px; height: {H}px; box-sizing: border-box; position: relative; '
            f'overflow: hidden; background: {f}; color: {PAPEL}">')

def foto(src, escala=1.04):
    return (f'<img src="fotos/{src}" alt="" style="position: absolute; inset: 0; width: 100%; height: 100%; '
            f'object-fit: cover; transform: scale({escala}); display: block">')

def velo(g):
    return f'<div style="position: absolute; inset: 0; background: {g}"></div>'

# Los velos de la casa, adaptados al alto del post.
VELO_FOTO = ('linear-gradient(180deg, rgba(16, 14, 11, 0.72) 0%, rgba(16, 14, 11, 0.34) 42%, '
             'rgba(16, 14, 11, 0.86) 100%)')
VELO_TELEFONO = ('linear-gradient(180deg, rgba(16, 14, 11, 0.84) 0%, rgba(16, 14, 11, 0.5) 38%, '
                 'rgba(16, 14, 11, 0.6) 100%)')

def kicker(t, y=110, color=None):
    c = color or 'rgba(255, 253, 249, 0.82)'
    return (f'<p class="sans" style="position: absolute; left: 84px; top: {y}px; margin: 0; font-size: 30px; '
            f'letter-spacing: 0.18em; text-transform: uppercase; color: {c}; font-weight: 600; {SOMBRA}">{t}</p>')

def titular(t, y, size=92, ancho=912):
    return (f'<h1 class="serif" style="position: absolute; left: 84px; top: {y}px; margin: 0; width: {ancho}px; '
            f'font-size: {size}px; line-height: 1.06; letter-spacing: -0.018em; font-weight: 400; {SOMBRA}">{t}</h1>')

def sub(t, y, size=38, color='rgba(255, 253, 249, 0.88)', ancho=912, peso=500):
    """Sin <br> en el cuerpo, a propósito: el corte forzado ignora el ancho real de la
    fuente al exportar (las del HELMET y las reales no miden igual) y deja renglones
    sueltos. Se controla con el ancho y se deja fluir; `text-wrap: pretty` evita viudas."""
    return (f'<p class="sans" style="position: absolute; left: 84px; top: {y}px; margin: 0; width: {ancho}px; '
            f'font-size: {size}px; line-height: 1.4; color: {color}; font-weight: {peso}; '
            f'text-wrap: pretty; {SOMBRA}">{t}</p>')

def marca(y=1200):
    return (f'<div style="position: absolute; left: 84px; top: {y}px; display: flex; align-items: center; gap: 18px">'
            f'<img src="mark.png" alt="" style="width: 50px; height: 50px">'
            f'<span class="sans" style="font-size: 28px; color: rgba(255, 253, 249, 0.85); font-weight: 600; '
            f'letter-spacing: 0.02em; {SOMBRA}">travelsnomad.com</span></div>')

def telefono(png, ancho=430, arriba=500):
    """El móvil de las destacadas (telefono() en gen-destacadas.py), a escala de post."""
    r, p, ar, isla_w, isla_h = 59, 13, 4, 129, 36
    return (f'<div style="position: absolute; left: 50%; top: {arriba}px; transform: translateX(-50%); '
            f'width: {ancho}px; aspect-ratio: 9 / 19.5; background: #0b0b0d; border-radius: {r}px; padding: {p}px; '
            f'box-shadow: 0 44px 110px rgba(0, 0, 0, 0.6)">'
            f'<div style="position: absolute; inset: 0; border-radius: {r}px; border: {ar}px solid #98979c"></div>'
            f'<div style="position: absolute; top: 25px; left: 50%; transform: translateX(-50%); width: {isla_w}px; '
            f'height: {isla_h}px; background: #0b0b0d; border-radius: 20px; z-index: 2"></div>'
            f'<div style="width: 100%; height: 100%; border-radius: {r - p}px; background: #F5F0E8; overflow: hidden">'
            f'<img src="{png}" alt="" style="width: 100%; display: block"></div></div>')

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
