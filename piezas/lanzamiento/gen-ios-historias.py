# LAS HISTORIAS DEL DÍA DEL LANZAMIENTO EN IPHONE (24-oct) — 1080×1920.
#
# Acompañan al carrusel de gen-ios.py: el post se queda en el perfil; la historia lleva el
# adhesivo de enlace, que en una publicación no existe. Dos tarjetas:
#   iosh-1 · el anuncio, con el hueco del adhesivo de enlace libre (y ≥ 1520)
#   iosh-2 · «¿Y en Android?» — la respuesta decidida el 1-oct: sin fecha, «síguenos y te avisamos»
#
# Una tercera, para quienes estaban en la lista de espera («gracias por llegar antes, ya puedes
# descargarla, te hemos escrito aparte»), NO se hace hasta que el dueño confirme cómo canjean su
# 1,99 € y les haya escrito: es el panel de copy del 24-oct el que la dejó condicionada.
#
# ZONAS SEGURAS (AGENTS.md): en una historia la interfaz tapa ~250 px arriba y abajo; el texto
# vive entre y=280 e y=1500 y de 1520 para abajo va el adhesivo.
#
# El enlace del adhesivo: la ficha directa (https://apps.apple.com/app/id6797973945) o, mejor
# para medir, un enlace de campaña de App Store Connect (pt + ct); travelsnomad.com/app pierde
# el UTM al saltar a la tienda (tienda.js hace location.replace).
#
# Uso, desde salida/:  python3 ../piezas/lanzamiento/gen-ios-historias.py
#                      node ../piezas/roma/exportar-plan.mjs iosh 2 1080 1920
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tarjetas import (SOMBRA, MENTA, PAPEL, NOCHE, pagina as _pagina, kicker, titular, sub, marca)

HELMET = open('Main.dc.html').read().split('<helmet>')[1].split('</helmet>')[0]
pagina = lambda cuerpo: _pagina(cuerpo, HELMET)
H = 1920
VELO = ('linear-gradient(180deg, rgba(16, 14, 11, 0.74) 0%, rgba(16, 14, 11, 0.36) 42%, '
        'rgba(16, 14, 11, 0.7) 100%)')

for f in ('fotos-historia/f-sagrada-pasion.jpg', 'fotos-historia/f-bcn-calle.jpg', 'icono-app.png'):
    if not os.path.exists(f):
        sys.exit(f'FALTA {f}. ¿Has pasado piezas/preparar.sh?')

def raiz():
    return (f'<div style="width: 1080px; height: {H}px; box-sizing: border-box; position: relative; '
            f'overflow: hidden; background: #100E0B; color: {PAPEL}">')

def foto(src, escala=1.04):
    return (f'<img src="fotos-historia/{src}" alt="" style="position: absolute; inset: 0; width: 100%; '
            f'height: 100%; object-fit: cover; transform: scale({escala}); display: block">')

def velo(g):
    return f'<div style="position: absolute; inset: 0; background: {g}"></div>'

def icono(x, y, lado):
    return (f'<img src="icono-app.png" alt="" style="position: absolute; left: {x}px; top: {y}px; '
            f'width: {lado}px; height: {lado}px; border-radius: {round(lado * 0.2237)}px; display: block; '
            f'box-shadow: 0 18px 50px rgba(0, 0, 0, 0.5)">')

T = {}

T['iosh-1'] = (raiz() + foto('f-sagrada-pasion.jpg') + velo(VELO)
  + kicker('Ya en iPhone', 300)
  + titular('Nomad ya est&aacute;<br>en la App Store.', 380, 116)
  + sub('Descargarla es gratis. Se paga por viaje.', 760, 46, ancho=900)
  + icono(84, 1000, 170)
  + (f'<div style="position: absolute; left: 290px; top: 1022px">'
     f'<p class="serif" style="margin: 0; font-size: 62px; line-height: 1.05; {SOMBRA}">Nomad: gu&iacute;a de viajes</p>'
     f'<p class="sans" style="margin: 10px 0 0; font-size: 32px; font-weight: 600; letter-spacing: 0.02em; '
     f'color: rgba(255, 253, 249, 0.82); {SOMBRA}">Para iPhone</p></div>')
  + sub('El enlace, aqu&iacute; abajo.', 1390, 38, 'rgba(255, 253, 249, 0.8)', ancho=900, peso=600)
  + '</div>')

T['iosh-2'] = (raiz() + foto('f-bcn-calle.jpg') + velo(VELO)
  + kicker('Android', 300)
  + titular('&iquest;Y en<br>Android?', 380, 130)
  + sub('Pronto, sin fecha, y no vamos a inventarnos una.', 800, 46, ancho=900)
  + (f'<div style="position: absolute; left: 84px; top: 1080px; padding: 26px 40px; border-radius: 999px; '
     f'background: {MENTA}; color: #10231D">'
     f'<span class="sans" style="font-size: 40px; font-weight: 700">S&iacute;guenos y te avisamos el d&iacute;a que salga</span></div>')
  + marca(1300)
  + '</div>')

for stem, html in T.items():
    open(f'{stem}.dc.html', 'w').write(pagina(html))
print(f'{len(T)} historias: ' + ', '.join(T))
