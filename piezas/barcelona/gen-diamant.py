# «¿CONOCÍAS ESTE LUGAR?» — la Plaça del Diamant, siete tarjetas (6-sep).
#
# El porqué y los hechos verificados, en piezas/barcelona/GUION.md. En una frase: el reel
# se guardó CERO veces con 1 258 espectadores, y lo que se guarda no es un demo de
# producto sino algo que vale por sí solo. Aquí lo que vale por sí solo es la historia de
# una plaza de barrio con un refugio antiaéreo debajo.
#
# EL GOLPE VA EN LA TARJETA 2, a propósito: en un carrusel la gente se va pronto, y el
# refugio en la quinta no lo vería casi nadie. La 1 pregunta y la 2 responde.
#
# NADA DE ESTO SE ESCRIBE DE MEMORIA. Cada dato está comprobado contra el Ajuntament de
# Barcelona, el Taller d'Història de Gràcia y Wikipedia; si se cambia una cifra, se vuelve
# a comprobar. Las fuentes están en el GUION.
#
# LO QUE FALTA PARA PUBLICARLO son dos cosas, y las dos las trae el dueño:
#   1. Las FOTOS. De la Plaça del Diamant hay 14 en Commons y las 14 son CC BY-SA, no CC0.
#      La regla de la casa (sólo CC0 o dominio público) las deja fuera, así que la salida
#      recomendada es que las haga él. Mientras no estén, el generador pinta el hueco.
#   2. La CAPTURA del tour de la app con la parada de la plaza. Sin ella, la tarjeta 6
#      pinta un aviso en naranja: una tarjeta sin la prueba no puede parecer terminada.
#
# Uso, desde salida/:  python3 ../piezas/barcelona/gen-diamant.py
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tarjetas import (SOMBRA, MENTA, NOCHE, VELO_FOTO, VELO_TELEFONO,
                      pagina as _pagina, raiz, foto, velo, kicker, titular, sub, marca,
                      telefono, pendiente, documento, numero)

HELMET = open('Main.dc.html').read().split('<helmet>')[1].split('</helmet>')[0]
pagina = lambda cuerpo: _pagina(cuerpo, HELMET)

# Los ficheros que espera. Cambiar aquí y en ningún otro sitio cuando lleguen los buenos.
PLANO   = 'f-diamant-plano.jpg'      # el plano original del refugio (Commons, CC BY-SA)
CAPTURA = 'tourdiamant-900.webp'     # el tour de la app con la parada de la plaza

def hay(f, carpeta='fotos'):
    return os.path.exists(f'{carpeta}/{f}' if carpeta else f)

def fondo(f, escala=1.06, v=VELO_FOTO):
    """La foto con su velo si existe; si no, el lienzo oscuro y un aviso, para que se vea
    de un vistazo qué tarjeta está a medias."""
    if hay(f): return foto(f, escala) + velo(v)
    return velo(NOCHE) + ('<p class="sans" style="position: absolute; left: 84px; top: 1050px; margin: 0; '
                          'font-size: 26px; font-weight: 700; color: #E4572E; letter-spacing: 0.06em">'
                          f'FALTA LA FOTO &middot; {f}</p>')

T = {}

# 1 · EL GANCHO. El fondo es el plano del refugio ampliado: a ese tamaño no se reconoce
#     —que es justo lo que se busca— y no es una foto de aficionado, es un documento.
T['diamant-1'] = (raiz(NOCHE)
  + (foto(PLANO, 2.6) + velo('linear-gradient(180deg, rgba(16, 14, 11, 0.88) 0%, '
                             'rgba(16, 14, 11, 0.66) 45%, rgba(16, 14, 11, 0.92) 100%)')
     if hay(PLANO) else velo(NOCHE))
  + kicker('Barcelona &middot; Gr&agrave;cia')
  + titular('&iquest;Conoc&iacute;as<br>este lugar?', 190, 108)
  + sub('Es una plaza de barrio. Y tiene tres historias debajo.', 480, 40, ancho=860)
  + marca()
  + '</div>')

# 2 · EL GOLPE, con la medida de protagonista. Va en la 2 a propósito: en un carrusel la
#     gente se va pronto, y el refugio en la quinta no lo vería casi nadie.
T['diamant-2'] = (raiz(NOCHE)
  + kicker('Doce metros bajo tus pies', 110, MENTA)
  + numero('12<span style="font-size: 120px; letter-spacing: 0">&nbsp;m</span>', 190, 300)
  + titular('Hay un refugio antia&eacute;reo.', 570, 82)
  + sub('Lo cavaron los propios vecinos durante la Guerra Civil. Cab&iacute;an m&aacute;s de '
        'doscientas personas. Es el refugio 232.', 720, 40, ancho=880)
  + marca()
  + '</div>')

# 3 · EL AÑO EN QUE APARECIÓ, con el plano original presentado COMO DOCUMENTO: de fondo se
#     leería como textura y no se entendería qué es.
T['diamant-3'] = (raiz(NOCHE)
  + kicker('Y nadie lo sab&iacute;a', 110)
  + numero('1992', 180, 240, MENTA)
  + titular('Apareci&oacute; haciendo obras.', 460, 76)
  + (documento(PLANO, 880, 610, -1.5) if hay(PLANO) else
     pendiente('FALTA EL PLANO<br>del refugio', 500, 610))
  + sub('Barcelona lleg&oacute; a tener unos 1.300 refugios, m&aacute;s de 90 s&oacute;lo en Gr&agrave;cia. '
        'Se visita los domingos, con reserva.', 1080, 32, 'rgba(255, 253, 249, 0.86)')
  + '</div>')

# 4 · LA NOVELA.
T['diamant-4'] = (raiz(NOCHE)
  + kicker('Arriba, en la plaza', 110)
  + numero('1962', 180, 240)
  + titular('Empieza la novela<br>m&aacute;s le&iacute;da en catal&aacute;n.', 460, 76)
  + sub('<i>La pla&ccedil;a del Diamant</i>, de Merc&egrave; Rodoreda. Traducida a m&aacute;s de treinta '
        'idiomas.', 700, 40, ancho=880)
  + sub('La escultura de la plaza es la Colometa: la protagonista, atrapada contra un muro '
        'mientras las palomas levantan el vuelo.', 850, 36, 'rgba(255, 253, 249, 0.72)', ancho=880)
  + marca()
  + '</div>')

# 5 · EL NOMBRE.
T['diamant-5'] = (raiz(NOCHE)
  + kicker('Y el nombre', 110)
  + numero('1860', 180, 240)
  + titular('Se lo puso un joyero.', 460, 82)
  + sub('Josep Rosell compr&oacute; estos terrenos y bautiz&oacute; las calles de Gr&agrave;cia con '
        'nombres de piedras preciosas. De ah&iacute; el Diamant.', 620, 40, ancho=880)
  + marca()
  + '</div>')

# 6 · LA PRUEBA. Sin esta captura el carrusel no se publica: el cierre pasaría de ser una
#     prueba a ser una promesa, y una promesa que la app no cumple es lo que la regla de
#     la casa prohíbe.
T['diamant-6'] = (raiz(NOCHE)
  + kicker('C&oacute;mo se entera uno de esto')
  + titular('Te lo cuenta al o&iacute;do,<br>mientras lo andas.', 180, 82)
  + (telefono(CAPTURA, 430, 520) if hay(CAPTURA, '') else
     pendiente('FALTA LA CAPTURA<br>del tour de la app<br>con esta parada', 430, 520))
  + '</div>')

# 7 · EL CIERRE, el del reel y el de Roma, pero SIN FOTO. La primera versión traía
#     f-oferta.jpg, que es San Pedro y el puente de Sant'Angelo: cerrar un carrusel de
#     Barcelona con una foto de Roma. Y sin foto queda además coherente con las otras seis.
T['diamant-7'] = (raiz(NOCHE)
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

faltan = [f for f in (PLANO,) if not hay(f)] + \
         ([CAPTURA] if not hay(CAPTURA, '') else [])
print(f'{len(T)} tarjetas: ' + ', '.join(T))
if faltan: print('FALTAN, y las tarjetas lo dicen en naranja: ' + ', '.join(faltan))
