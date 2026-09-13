# LA IMAGEN DE FONDO DEL FORMULARIO INSTANTÁNEO DE META (13-sep), 1200×628.
#
# El anuncio es el reel; el formulario es lo que se abre al tocar «Registrarte», y Meta sólo
# deja UNA imagen de fondo en su pantalla de presentación (el dueño preguntó si dos: no).
# Es lo primero que ve quien acaba de tocar, así que repite la oferta y enseña la app: la
# terraza del café (el ancla de precio de la casa, la misma foto que los estáticos), el
# móvil con la app real y «Tu primer viaje, por 1,99 €», con el precio como es: dure lo
# que dure. Sin «2,99 €» a secas.
#
# LA CAPTURA TIENE QUE SER LA APP DE HOY. La primera versión llevaba plan-900.webp, del
# 29-ago, y el dueño la paró: la app ha cambiado de aspecto desde entonces. Va la parada
# del Templo de Debod del 11-sep, que sí es la app actual y enseña la audioguía. Si la
# app vuelve a cambiar, se vuelve a capturar: una captura vieja en un anuncio es una
# promesa que la app no cumple.
#
# Uso, desde salida/:  python3 ../piezas/anuncios/gen-formulario.py
#                      node ../piezas/roma/exportar-plan.mjs formulario 1 1200 628
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tarjetas import SOMBRA, MENTA, PAPEL, pagina as _pagina, telefono

HELMET = open('Main.dc.html').read().split('<helmet>')[1].split('</helmet>')[0]
W, H = 1200, 628

html = (f'<div style="width: {W}px; height: {H}px; position: relative; overflow: hidden; background: #100E0B; color: {PAPEL}">'
        f'<img src="fotos/f-precio.jpg" alt="" style="position: absolute; inset: 0; width: 100%; height: 100%; '
        f'object-fit: cover; object-position: 50% 40%; transform: scale(1.04); display: block">'
        f'<div style="position: absolute; inset: 0; background: linear-gradient(90deg, rgba(16, 14, 11, 0.9) 0%, '
        f'rgba(16, 14, 11, 0.72) 48%, rgba(16, 14, 11, 0.3) 100%)"></div>'
        # el texto, a la izquierda
        f'<p class="sans" style="position: absolute; left: 64px; top: 78px; margin: 0; font-size: 20px; letter-spacing: 0.16em; '
        f'text-transform: uppercase; color: {MENTA}; font-weight: 600; {SOMBRA}">NOMAD &middot; lista de espera</p>'
        f'<h1 class="serif" style="position: absolute; left: 64px; top: 118px; margin: 0; width: 620px; font-size: 72px; '
        f'line-height: 1.04; letter-spacing: -0.02em; font-weight: 400; {SOMBRA}">Tu primer viaje,<br>por 1,99&nbsp;&euro;.</h1>'
        f'<p class="sans" style="position: absolute; left: 64px; top: 300px; margin: 0; width: 560px; font-size: 28px; '
        f'line-height: 1.4; color: rgba(255, 253, 249, 0.9); font-weight: 500; {SOMBRA}">Dure lo que dure, hasta 30 d&iacute;as. '
        f'Te escribe el viaje entero y te lo cuenta al o&iacute;do. Sale en octubre.</p>'
        f'<div style="position: absolute; left: 64px; top: 528px; display: flex; align-items: center; gap: 14px">'
        f'<img src="mark.png" alt="" style="width: 40px; height: 40px">'
        f'<span class="sans" style="font-size: 24px; color: rgba(255, 253, 249, 0.85); font-weight: 600; {SOMBRA}">travelsnomad.com</span></div>'
        # el móvil con el plan real, a la derecha, asomando por abajo
        f'<div style="position: absolute; left: 640px; top: 0; width: 560px; height: {H}px">'
        + telefono('tourdebod-900.webp', 300, 70).replace('left: 50%; top: 70px; transform: translateX(-50%)', 'left: 130px; top: 70px')
        + '</div></div>')

open('formulario-1.dc.html', 'w').write(_pagina(html, HELMET))
print('formulario-1.dc.html, 1200×628')
