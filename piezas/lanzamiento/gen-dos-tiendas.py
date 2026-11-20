# «YA EN IPHONE Y ANDROID» (20-nov) — BORRADOR, dos variantes de historia 1080×1920.
#
# Android está en Google Play desde el 19-nov (#21). El dueño enseñó como referencia un anuncio de
# otra app: color plano, el icono en grande, «ya en iOS y Android», las dos insignias. Aquí va
# esa pieza con lo de Nomad, y otra con el producto delante, para elegir:
#   dos-1 · el anuncio a secas, en los colores del icono
#   dos-2 · lo mismo con el plan de un día en el móvil
#   dos-3 · el anuncio con misterio: sin decir qué hace ni cuánto cuesta
#
# Para quién sirve cada una, qué se midió antes de hacerlas y qué no está decidido: README.md.
#
# ZONAS SEGURAS: el texto vive entre y=280 e y=1500; de 1520 para abajo va el adhesivo de
# enlace (o el botón, si es un anuncio).
#
# LAS INSIGNIAS son las oficiales, sin tocar, y van como piden sus normas (leídas el 20-nov):
#   - la de Apple, en negro y la primera (izquierda o arriba), con un cuarto de su alto libre
#     alrededor (developer.apple.com/app-store/marketing/guidelines);
#   - la de Google, igual de grande o más que la otra. Su PNG trae margen dentro (29 px arriba
#     y abajo de 250): para que las dos midan lo mismo a la vista, su imagen va 1,3 veces más
#     alta que la de Apple, como en la web (40 y 52);
#   - «Android» lleva ™ la primera vez y su línea de marca (developer.android.com, guía de marca).
# La guía de la insignia de Google Play no se pudo leer ese día (su página daba 404): antes de
# PAGAR un anuncio con ella, se lee.
#
# Uso, desde salida/:  python3 ../piezas/lanzamiento/gen-dos-tiendas.py
#                      node ../piezas/roma/exportar-plan.mjs dos 3 1080 1920
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tarjetas import SOMBRA, MENTA, PAPEL, NOCHE, pagina as _pagina, kicker, titular, sub

HELMET = open('Main.dc.html').read().split('<helmet>')[1].split('</helmet>')[0]
pagina = lambda cuerpo: _pagina(cuerpo, HELMET)
H = 1920
CREMA, VERDE, TINTA = '#E8E1D5', '#107A6D', '#16130F'

for f in ('icono-app.png', 'insignia-app-store-es.svg', 'insignia-google-play-es.png', 'plan-20nov-900.webp'):
    if not os.path.exists(f):
        sys.exit(f'FALTA {f}. ¿Has pasado piezas/preparar.sh?')

def insignias(x, y, alto, centro=False, columna=False):
    """Las dos, a la misma altura visible. `alto` es el de la de Apple."""
    a = (f'<img src="insignia-app-store-es.svg" alt="Cons&iacute;guelo en el App Store" '
         f'style="height: {alto}px; width: auto; display: block">')
    g = (f'<img src="insignia-google-play-es.png" alt="Disponible en Google Play" '
         f'style="height: {round(alto * 1.3)}px; width: auto; display: block">')
    donde = (f'left: 0; width: 1080px; justify-content: center' if centro else f'left: {x}px')
    sentido = 'flex-direction: column; align-items: flex-start; gap: 14px' if columna else 'align-items: center; gap: 26px'
    return (f'<div style="position: absolute; top: {y}px; {donde}; display: flex; {sentido}">{a}{g}</div>')

LEGAL = ('iPhone es una marca comercial y App Store una marca de servicio de Apple Inc. Google Play, '
         'el logotipo de Google Play y Android son marcas comerciales de Google LLC.')

def legal(color, y=1456, x=84, ancho=912, centro=False):
    al = 'text-align: center; ' if centro else ''
    return (f'<p class="sans" style="position: absolute; left: {x}px; top: {y}px; margin: 0; width: {ancho}px; '
            f'{al}font-size: 19px; line-height: 1.35; font-weight: 500; color: {color}">{LEGAL}</p>')

T = {}

# ── dos-1 · el anuncio a secas ────────────────────────────────────────────────────────────────
T['dos-1'] = (
    f'<div style="width: 1080px; height: {H}px; box-sizing: border-box; position: relative; overflow: hidden; '
    f'background: {CREMA}; color: {TINTA}">'
    f'<p class="sans" style="position: absolute; left: 0; top: 300px; width: 1080px; margin: 0; text-align: center; '
    f'font-size: 30px; letter-spacing: 0.18em; text-transform: uppercase; font-weight: 700; color: {VERDE}">Ya es oficial</p>'
    f'<h1 class="serif" style="position: absolute; left: 84px; top: 368px; width: 912px; margin: 0; text-align: center; '
    f'font-size: 104px; line-height: 1.04; letter-spacing: -0.018em; font-weight: 400">Nomad ya est&aacute; en iPhone y&nbsp;Android&trade;.</h1>'
    f'<img src="icono-app.png" alt="" style="position: absolute; left: 350px; top: 726px; width: 380px; height: 380px; '
    f'border-radius: 85px; display: block; box-shadow: 0 30px 80px rgba(22, 19, 15, 0.22), 0 0 0 1px rgba(22, 19, 15, 0.06)">'
    f'<p class="serif" style="position: absolute; left: 0; top: 1136px; width: 1080px; margin: 0; text-align: center; '
    f'font-size: 56px; line-height: 1.1">Nomad: gu&iacute;a de viajes</p>'
    + insignias(0, 1236, 92, centro=True)
    + f'<p class="sans" style="position: absolute; left: 84px; top: 1378px; width: 912px; margin: 0; text-align: center; '
      f'font-size: 36px; line-height: 1.35; font-weight: 600; color: rgba(22, 19, 15, 0.82)">'
      f'Descargarla es gratis. Se paga por viaje, desde 2,99&nbsp;&euro;.</p>'
    + legal('rgba(22, 19, 15, 0.5)', y=1446, centro=True)
    + '</div>')

# ── dos-2 · con el producto delante ───────────────────────────────────────────────────────────
def telefono_a(png, x, arriba, ancho):
    r, p, ar = 59, 13, 4
    return (f'<div style="position: absolute; left: {x}px; top: {arriba}px; width: {ancho}px; aspect-ratio: 9 / 19.5; '
            f'background: #0b0b0d; border-radius: {r}px; padding: {p}px; box-sizing: border-box; '
            f'box-shadow: 0 44px 110px rgba(0, 0, 0, 0.6)">'
            f'<div style="position: absolute; inset: 0; border-radius: {r}px; border: {ar}px solid #98979c"></div>'
            f'<div style="width: 100%; height: 100%; border-radius: {r - p}px; background: #F5F0E8; overflow: hidden">'
            f'<img src="{png}" alt="" style="width: 100%; display: block"></div></div>')

T['dos-2'] = (
    f'<div style="width: 1080px; height: {H}px; box-sizing: border-box; position: relative; overflow: hidden; '
    f'background: {NOCHE}; color: {PAPEL}">'
    + kicker('Ya en iPhone y Android&trade;', 300, MENTA)
    + titular('Dices a d&oacute;nde vas.<br>Nomad escribe el viaje.', 366, 96)
    + telefono_a('plan-20nov-900.webp', 84, 660, 392)
    + f'<img src="icono-app.png" alt="" style="position: absolute; left: 540px; top: 700px; width: 132px; height: 132px; '
      f'border-radius: 30px; display: block; box-shadow: 0 18px 50px rgba(0, 0, 0, 0.5)">'
    + f'<p class="serif" style="position: absolute; left: 540px; top: 862px; width: 470px; margin: 0; font-size: 58px; '
      f'line-height: 1.06">Nomad: gu&iacute;a de viajes</p>'
    + f'<p class="sans" style="position: absolute; left: 540px; top: 1010px; width: 456px; margin: 0; font-size: 34px; '
      f'line-height: 1.4; font-weight: 500; color: rgba(255, 253, 249, 0.86); text-wrap: pretty">'
      f'Qu&eacute; ver cada d&iacute;a, en qu&eacute; orden y cu&aacute;nto cuesta. Y te lo cuenta al o&iacute;do mientras lo andas.</p>'
    + insignias(540, 1228, 84, columna=True)
    + f'<p class="sans" style="position: absolute; left: 540px; top: 1452px; width: 456px; margin: 0; font-size: 28px; '
      f'line-height: 1.35; font-weight: 600; color: rgba(255, 253, 249, 0.9)">Descargarla es gratis. Se paga por viaje, desde 2,99&nbsp;&euro;.</p>'
    + legal('rgba(255, 253, 249, 0.46)', y=1560)
    + '</div>')

# ── dos-3 · el anuncio con misterio: como la referencia, sin decir qué hace ni cuánto cuesta ────
# Pedida por el dueño el 20-nov («el tema enigmático a la gente le suele gustar»): es la que se
# prueba contra dos-2 con público que no conoce Nomad. Sólo el titular, el icono y las tiendas.
T['dos-3'] = (
    f'<div style="width: 1080px; height: {H}px; box-sizing: border-box; position: relative; overflow: hidden; '
    f'background: {CREMA}; color: {TINTA}">'
    f'<p class="sans" style="position: absolute; left: 0; top: 310px; width: 1080px; margin: 0; text-align: center; '
    f'font-size: 30px; letter-spacing: 0.18em; text-transform: uppercase; font-weight: 700; color: {VERDE}">Ya es oficial</p>'
    f'<h1 class="serif" style="position: absolute; left: 84px; top: 378px; width: 912px; margin: 0; text-align: center; '
    f'font-size: 104px; line-height: 1.04; letter-spacing: -0.018em; font-weight: 400">Nomad ya est&aacute; en iPhone y&nbsp;Android&trade;.</h1>'
    f'<img src="icono-app.png" alt="" style="position: absolute; left: 320px; top: 740px; width: 440px; height: 440px; '
    f'border-radius: 98px; display: block; box-shadow: 0 34px 90px rgba(22, 19, 15, 0.24), 0 0 0 1px rgba(22, 19, 15, 0.06)">'
    + insignias(0, 1262, 96, centro=True)
    + f'<p class="sans" style="position: absolute; left: 0; top: 1404px; width: 1080px; margin: 0; text-align: center; '
      f'font-size: 30px; letter-spacing: 0.18em; text-transform: uppercase; font-weight: 700; color: rgba(22, 19, 15, 0.78)">'
      f'Desc&aacute;rgala ya</p>'
    + legal('rgba(22, 19, 15, 0.46)', y=1466, centro=True)
    + '</div>')

for stem, html in T.items():
    open(f'{stem}.dc.html', 'w').write(pagina(html))
print(f'{len(T)} borradores: ' + ', '.join(T))
