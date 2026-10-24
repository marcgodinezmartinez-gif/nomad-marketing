# «NOMAD YA ESTÁ EN LA APP STORE» — carrusel de 6 tarjetas del lanzamiento en iPhone (24-oct).
#
# EL PRIMER POST DE LA APP YA PUBLICADA. Sustituye a «¿Qué pasa el día que abra NOMAD?»
# (gen-abre.py), que prometía una lista que ya no existe: la tienda abrió el 19-oct (la ficha
# lo dice: `releaseDate` 2026-10-19), la web oculta la lista de espera con una tienda
# encendida (`tienda.js`) y el dueño la cerró para todos el 17-oct (NOMAD#305).
#
# TODO LO QUE AFIRMA SALE DE LA FICHA PÚBLICA, no de la memoria: el nombre («Nomad: guía de
# viajes»), que descargarla es gratis, los tres precios por viaje, «sin suscripción», «una
# compra abre el viaje para todo el grupo», las audioguías que se descargan y suenan sin
# cobertura. Los titulares de las tarjetas 2-4 son los de las capturas de la propia ficha, para
# que quien llegue desde el post y vea la tienda reconozca lo mismo. Android: SIN fecha («muy
# pronto», que es lo que dice la web); lo decidido el 1-oct es «síguenos y te avisamos».
#
# EL PRECIO, en el orden de la casa (AGENTS.md): «desde 2,99 € el viaje entero» con la tabla
# por días. El 1,99 € de la lista NO aparece en ninguna tarjeta: ya no se ofrece a nadie nuevo,
# y cómo lo canjean quienes estaban dentro lo sabe el dueño, no el repo. Si hay que decirlo, va
# en las historias o en un comentario, nunca en las tarjetas.
#
# LAS CAPTURAS son las de la ficha (banco/capturas/movil-*.webp, recortadas de ahí con las
# esquinas transparentes): son la app de HOY, cosa que las del banco anteriores a octubre no
# eran (issue #5). El nombre exacto y el icono van en la portada y en el cierre: en la tienda
# hay media docena de apps que se llaman «Nomad».
#
# Uso, desde salida/:  python3 ../piezas/lanzamiento/gen-ios.py
#                      node ../piezas/roma/exportar-plan.mjs ios 6
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tarjetas import (SOMBRA, MENTA, PAPEL, NOCHE, VELO_FOTO,
                      pagina as _pagina, raiz, foto, velo, kicker, titular, sub, marca)

HELMET = open('Main.dc.html').read().split('<helmet>')[1].split('</helmet>')[0]
pagina = lambda cuerpo: _pagina(cuerpo, HELMET)

NOMBRE_TIENDA = 'Nomad: gu&iacute;a de viajes'      # tal cual en la tienda de España

for f in ('fotos/f-sagrada-pasion.jpg', 'fotos/f-bcn-cierre.jpg', 'fotos/f-bcn-noche.jpg',
          'fotos/f-grupo.jpg', 'fotos/f-precio.jpg', 'fotos/f-sagrada-estanque.jpg',
          'movil-crear.webp', 'movil-audioguia.webp', 'movil-gastos.webp',
          'icono-app.png', 'insignia-app-store-es.svg'):
    if not os.path.exists(f):
        sys.exit(f'FALTA {f}. ¿Has pasado piezas/preparar.sh?')

# ---------------------------------------------------------------- el copy, en un solo sitio
COPY = {
    'portada': dict(kicker='Ya en iPhone &middot; Android, muy pronto',
                    titular='Nomad ya est&aacute;<br>en la App Store.',
                    sub='Los d&iacute;as escritos. La ciudad, contada.'),
    'crear':   dict(kicker='El viaje', l1='T&uacute; dices d&oacute;nde.', l2='Nomad lo escribe.',
                    sub='Destino, fechas y c&oacute;mo te gusta viajar. Sale el viaje d&iacute;a a d&iacute;a: '
                        'qu&eacute; ver, en qu&eacute; orden y cu&aacute;nto cuesta.'),
    'oido':    dict(kicker='Al o&iacute;do', l1='La ciudad,', l2='contada.',
                    sub='Audioguías con voz real, parada a parada. Las descargas y suenan sin cobertura.'),
    'grupo':   dict(kicker='El grupo', l1='Los gastos,', l2='en paz.',
                    sub='Qui&eacute;n pag&oacute; qu&eacute; y a qui&eacute;n se debe. Una compra abre el viaje '
                        'para todo el grupo.'),
    'precio':  dict(kicker='El precio', titular='Desde 2,99&nbsp;&euro;<br>el viaje entero.',
                    sub='Sin suscripci&oacute;n. Descargarla es gratis: se paga por viaje.'),
    'cierre':  dict(kicker='Ya en iPhone', l1='B&uacute;scala como', l2=NOMBRE_TIENDA,
                    sub='Hay m&aacute;s apps que se llaman Nomad: f&iacute;jate en el icono.',
                    android='Android: muy pronto. S&iacute;guenos y te avisamos.'),
}

TARIFAS = [('Hasta 3 d&iacute;as', '2,99&nbsp;&euro;'),
           ('De 4 a 7 d&iacute;as', '4,99&nbsp;&euro;'),
           ('De 8 a 30 d&iacute;as', '6,99&nbsp;&euro;')]

VELO_TEXTO = ('linear-gradient(180deg, rgba(16, 14, 11, 0.78) 0%, rgba(16, 14, 11, 0.56) 40%, '
              'rgba(16, 14, 11, 0.88) 100%)')
VELO_MOVIL = ('linear-gradient(180deg, rgba(16, 14, 11, 0.86) 0%, rgba(16, 14, 11, 0.52) 38%, '
              'rgba(16, 14, 11, 0.5) 100%)')

def dos(l1, l2):
    """El titular de la ficha: una línea blanca y la segunda en menta (las capturas de la
    tienda la llevan en cursiva verde; la fuente que se inyecta aquí sólo trae el romano,
    y una cursiva sintetizada se ve peor que el color solo)."""
    return f'{l1}<br><span style="color: {MENTA}">{l2}</span>'

def movil(png, ancho, arriba):
    """El móvil recortado de la ficha, asomando por abajo como en el resto de carruseles.
    `drop-shadow` y no `box-shadow`: la sombra sigue el contorno transparente."""
    return (f'<img src="{png}" alt="" style="position: absolute; left: 50%; top: {arriba}px; '
            f'transform: translateX(-50%); width: {ancho}px; display: block; '
            f'filter: drop-shadow(0 40px 60px rgba(0, 0, 0, 0.55))">')

def icono(x, y, lado):
    # El redondeo de iOS, aproximado: 22,37 % del lado.
    return (f'<img src="icono-app.png" alt="" style="position: absolute; left: {x}px; top: {y}px; '
            f'width: {lado}px; height: {lado}px; border-radius: {round(lado * 0.2237)}px; display: block; '
            f'box-shadow: 0 18px 50px rgba(0, 0, 0, 0.5)">')

def tarifa(dias, precio, y):
    return (f'<div style="position: absolute; left: 84px; top: {y}px; width: 912px; display: flex; '
            f'align-items: baseline; justify-content: space-between; padding-bottom: 22px; '
            f'border-bottom: 1px solid rgba(255, 253, 249, 0.2)">'
            f'<span class="sans" style="font-size: 38px; font-weight: 600; {SOMBRA}">{dias}</span>'
            f'<span class="serif" style="font-size: 64px; line-height: 1; color: {MENTA}; {SOMBRA}">{precio}</span>'
            f'</div>')

T = {}
c = COPY

# 1 · EL ANUNCIO. La foto del dueño (la fachada de la Pasión, la misma del reel de la
# audioguía), el nombre exacto de la tienda y el icono. Android, en el kicker: la noticia es
# «iPhone ya, Android pronto», y quien tiene Android lo lee en el primer vistazo.
T['ios-1'] = (raiz(NOCHE)
  + foto('f-sagrada-pasion.jpg', 1.04) + velo(VELO_FOTO)
  + kicker(c['portada']['kicker'])
  + titular(c['portada']['titular'], 180, 108)
  + sub(c['portada']['sub'], 470, 44)
  + icono(84, 1060, 150)
  + (f'<div style="position: absolute; left: 262px; top: 1076px">'
     f'<p class="serif" style="margin: 0; font-size: 58px; line-height: 1.05; {SOMBRA}">{NOMBRE_TIENDA}</p>'
     f'<p class="sans" style="margin: 8px 0 0; font-size: 30px; font-weight: 600; letter-spacing: 0.02em; '
     f'color: rgba(255, 253, 249, 0.82); {SOMBRA}">En la App Store</p></div>')
  + '</div>')

# 2-4 · LA APP, con los titulares de la ficha y su captura.
def tarjeta_app(stem, foto_, copy, png, ancho, arriba_movil):
    return (raiz(NOCHE)
      + foto(foto_, 1.06) + velo(VELO_MOVIL)
      + kicker(copy['kicker'])
      + titular(dos(copy['l1'], copy['l2']), 170, 92)
      + sub(copy['sub'], 395, 34, ancho=880)
      + movil(png, ancho, arriba_movil)
      + '</div>')

T['ios-2'] = tarjeta_app('ios-2', 'f-bcn-cierre.jpg', c['crear'],   'movil-crear.webp',     560, 560)
T['ios-3'] = tarjeta_app('ios-3', 'f-bcn-noche.jpg',  c['oido'],    'movil-audioguia.webp', 560, 560)
T['ios-4'] = tarjeta_app('ios-4', 'f-grupo.jpg',      c['grupo'],   'movil-gastos.webp',    560, 560)

# 5 · EL PRECIO, primero el «desde», siempre.
T['ios-5'] = (raiz(NOCHE)
  + foto('f-precio.jpg', 1.06) + velo(VELO_TEXTO)
  + kicker(c['precio']['kicker'])
  + titular(c['precio']['titular'], 180, 96)
  + ''.join(tarifa(d, p, 500 + i * 118) for i, (d, p) in enumerate(TARIFAS))
  + sub(c['precio']['sub'], 900, 36, 'rgba(255, 253, 249, 0.84)', ancho=880)
  + marca()
  + '</div>')

# 6 · EL CIERRE: cómo encontrarla (el nombre exacto, el icono y la insignia oficial de Apple,
# sin tocar) y la respuesta a «¿y en Android?».
T['ios-6'] = (raiz(NOCHE)
  + foto('f-sagrada-estanque.jpg', 1.04)
  + velo('linear-gradient(180deg, rgba(16, 14, 11, 0.8) 0%, rgba(16, 14, 11, 0.5) 40%, rgba(16, 14, 11, 0.9) 100%)')
  + kicker(c['cierre']['kicker'])
  + titular(dos(c['cierre']['l1'], c['cierre']['l2']), 180, 92)
  + sub(c['cierre']['sub'], 440, 36, ancho=880)
  + icono(84, 600, 190)
  + f'<img src="insignia-app-store-es.svg" alt="Descargar en la App Store" style="position: absolute; left: 330px; top: 650px; height: 90px; display: block">'
  + (f'<div style="position: absolute; left: 84px; top: 880px; padding: 22px 34px; border-radius: 999px; '
     f'background: {MENTA}; color: #10231D">'
     f'<span class="sans" style="font-size: 34px; font-weight: 700">{c["cierre"]["android"]}</span></div>')
  + marca()
  + '</div>')

for stem, html in T.items():
    open(f'{stem}.dc.html', 'w').write(pagina(html))
print(f'{len(T)} tarjetas: ' + ', '.join(T))
