# «¿CONOCÍAS ESTE LUGAR?» — la Plaça del Diamant, siete tarjetas, TODAS CON FOTO (7-sep).
#
# El porqué y los hechos verificados, en piezas/barcelona/GUION.md. En una frase: el reel
# se guardó CERO veces con 1 258 espectadores, y lo que se guarda no es un demo de
# producto sino algo que vale por sí solo. Aquí lo que vale por sí solo es la historia de
# una plaza de barrio con un refugio antiaéreo debajo.
#
# LAS FOTOS SON OBLIGATORIAS (dueño, 6-sep: «tienen que haber fotos 100 %, es la esencia de
# mi feed»). La versión anterior las sustituía por fechas sobre fondo oscuro; ésta las lleva
# todas. Vienen de Unsplash y de Pexels (regla ampliada ese día, AGENTS.md), sin atribución
# obligatoria y sin marca de agua, y el crédito de cada una está en banco/fotos/creditos.json.
#
# LA PORTADA NO ES LA PLAÇA DEL DIAMANT, y por eso no dice «¿Conocías este lugar?». De esa
# plaza no hay ni una foto libre en Unsplash, Pexels, Pixabay ni Flickr CC0 (buscado el
# 7-sep; las 14 de Commons son CC BY-SA). La portada es el campanar de la plaça de la Vila
# de Gràcia —el símbolo del barrio, entre plátanos— y el texto señala al barrio, no a la
# foto: «Aquí hay algo que casi nadie sabe». La plaza se nombra en la tarjeta 2. Si el
# dueño la fotografía él mismo (diez minutos, y de paso la Colometa y la boca del refugio),
# se cambia FOTOS[1] y vuelve la pregunta original.
#
# EL PLANO DEL REFUGIO (Commons, CC BY-SA 3.0) YA NO VA: exige atribución y ShareAlike, y
# la regla de la casa lo deja fuera. La tarjeta 3 lleva foto como las demás.
#
# EL GOLPE VA EN LA TARJETA 2, a propósito: en un carrusel la gente se va pronto, y el
# refugio en la quinta no lo vería casi nadie. La 1 pregunta y la 2 responde.
#
# NADA DE ESTO SE ESCRIBE DE MEMORIA. Cada dato está comprobado contra el Ajuntament de
# Barcelona, el Taller d'Història de Gràcia y Wikipedia; si se cambia una cifra, se vuelve
# a comprobar. Las fuentes están en el GUION.
#
# LO ÚNICO QUE FALTA es la CAPTURA del tour de la app con la parada de la plaza, y la trae
# el dueño. Sin ella, la tarjeta 6 pinta un aviso en naranja: una tarjeta sin la prueba no
# puede parecer terminada.
#
# Uso, desde salida/:  python3 ../piezas/barcelona/gen-diamant.py
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tarjetas import (SOMBRA, MENTA, NOCHE, VELO_FOTO, VELO_TELEFONO,
                      pagina as _pagina, raiz, foto, velo, kicker, titular, sub, marca,
                      telefono, pendiente, documento, numero)

HELMET = open('Main.dc.html').read().split('<helmet>')[1].split('</helmet>')[0]
pagina = lambda cuerpo: _pagina(cuerpo, HELMET)

# Los ficheros que espera. Cambiar aquí y en ningún otro sitio.
CAPTURA = 'tourdiamant-900.webp'     # el tour de la app con la parada de la plaza
FOTOS = {
    1: 'f-bcn-plaza.jpg',    # el campanar de la plaça de la Vila de Gràcia, entre plátanos
    2: 'f-bcn-noche.jpg',    # un callejón de noche, mojado, con luces: debajo de la ciudad
    3: 'f-bcn-patio.jpg',    # los tejados y el patio de una manzana: lo que no se ve desde la calle
    4: 'f-bcn-balcon.jpg',   # balcones con plantas al sol: el terrat de la Colometa
    5: 'f-bcn-calle.jpg',    # una calle estrecha con árboles y bolardos: las calles del joyero
    6: 'f-bcn-paseo.jpg',    # gente andando por una calle del casco antiguo: «mientras lo andas»
    7: 'f-bcn-cierre.jpg',   # Barcelona al anochecer desde el Park Güell, que es Gràcia
}

# En las tarjetas 2-5 el texto ocupa dos tercios del alto (número, titular y párrafo), así
# que el velo de foto de la casa —claro en el centro— dejaría letras sobre fachada al sol.
# Éste es más parejo: la foto se ve, pero detrás del texto.
VELO_TEXTO = ('linear-gradient(180deg, rgba(16, 14, 11, 0.8) 0%, rgba(16, 14, 11, 0.64) 55%, '
              'rgba(16, 14, 11, 0.42) 100%)')
# En la portada el texto está arriba y el campanar abajo: el velo de la casa oscurece el
# pie al 86 % y se comía la base de la torre. Éste deja ver la torre entera.
VELO_PORTADA = ('linear-gradient(180deg, rgba(16, 14, 11, 0.76) 0%, rgba(16, 14, 11, 0.3) 45%, '
                'rgba(16, 14, 11, 0.58) 100%)')

def hay(f, carpeta='fotos'):
    return os.path.exists(f'{carpeta}/{f}' if carpeta else f)

def fondo(n, v=VELO_TEXTO, escala=1.04):
    """La foto de la tarjeta con su velo; si falta, el lienzo oscuro y un aviso, para que se
    vea de un vistazo qué tarjeta está a medias."""
    f = FOTOS[n]
    if hay(f): return foto(f, escala) + velo(v)
    return velo(NOCHE) + ('<p class="sans" style="position: absolute; left: 84px; top: 1050px; margin: 0; '
                          'font-size: 26px; font-weight: 700; color: #E4572E; letter-spacing: 0.06em">'
                          f'FALTA LA FOTO &middot; {f}</p>')

# VERSIÓN B, sólo para decidir (7-sep): el dueño pidió ver la plaza y el refugio. Lo único
# que existe libre de eso está en Commons y es CC BY-SA —la plaza, la cabina de entrada
# del refugio y la Colometa—, que exige atribución y ShareAlike, y la regla de la casa lo
# deja fuera. Del interior del refugio no hay NINGUNA foto libre. Con VARIANTE=commons se
# escriben las tarjetas diamantb-* con esas fotos (que viven sólo en salida/fotos, no en el
# banco) y el listado de refugios de 1937 como documento, que sí es CC0. Si el dueño dice
# que sí, la atribución va en el pie y las fotos entran al banco con esa regla nueva.
VARIANTE = os.environ.get('VARIANTE', '')
if VARIANTE == 'commons':
    FOTOS[1] = 'f-diamant-plaza.jpg'      # la plaza de día, con la terraza  (CC BY-SA 3.0)
    FOTOS[2] = 'f-diamant-boca.jpg'       # la cabina de entrada del refugio (CC BY-SA 4.0)
    FOTOS[4] = 'f-diamant-colometa.jpg'   # la escultura                      (CC BY-SA 3.0)
LLISTAT = 'f-diamant-llistat.jpg'         # listado de refugios de Barcelona, 9-dic-1937 (CC0)
PREFIJO = 'diamantb' if VARIANTE == 'commons' else 'diamant'

T = {}

# 1 · EL GANCHO. El campanar de Gràcia entre plátanos: quien conoce el barrio lo reconoce
#     al instante, y el texto habla del barrio («aquí»), no de la foto.
T['diamant-1'] = (raiz(NOCHE)
  + fondo(1, VELO_PORTADA)
  + kicker('Barcelona &middot; Gr&agrave;cia')
  + (titular('&iquest;Conoc&iacute;as<br>este lugar?', 190, 108) if VARIANTE == 'commons' else
     titular('Aqu&iacute; hay algo<br>que casi nadie sabe.', 190, 100))
  + sub('Es una plaza de barrio. Y tiene tres historias debajo.' if VARIANTE == 'commons' else
        'Una plaza de barrio con tres historias debajo.', 480, 40, ancho=860)
  + marca()
  + '</div>')

# 2 · EL GOLPE, con la medida de protagonista y el nombre de la plaza en el kicker: es la
#     primera vez que se dice dónde.
T['diamant-2'] = (raiz(NOCHE)
  + fondo(2)
  + kicker('Pla&ccedil;a del Diamant &middot; bajo tus pies', 110, MENTA)
  + numero('12<span style="font-size: 120px; letter-spacing: 0">&nbsp;m</span>', 190, 300)
  + titular('Hay un refugio antia&eacute;reo.', 570, 82)
  + sub('Lo cavaron los propios vecinos durante la Guerra Civil. Cab&iacute;an m&aacute;s de '
        'doscientas personas. Es el refugio 232.', 720, 40, ancho=880)
  + marca()
  + '</div>')

# 3 · EL AÑO EN QUE APARECIÓ. Detrás, los tejados y el patio de una manzana: lo que la
#     ciudad esconde a la vista.
T['diamant-3'] = (raiz(NOCHE)
  + fondo(3)
  + kicker('Y nadie lo sab&iacute;a')
  + numero('1992', 180, 240, MENTA)
  + titular('Apareci&oacute; haciendo obras.', 460, 76)
  + ((documento(LLISTAT, 760, 560, -1.5)     # 1435×1078: a 760 de ancho mide 571 de alto
      + sub('El listado municipal de refugios del 9 de diciembre de 1937. Barcelona lleg&oacute; a tener '
            'unos 1.300, m&aacute;s de 90 s&oacute;lo en Gr&agrave;cia. Se visita los domingos, con reserva.',
            1160, 30, 'rgba(255, 253, 249, 0.86)'))
     if VARIANTE == 'commons' and hay(LLISTAT) else
     (sub('Barcelona lleg&oacute; a tener unos 1.300 refugios, m&aacute;s de 90 s&oacute;lo en Gr&agrave;cia. '
          'Se visita los domingos, con reserva.', 620, 40, ancho=880)
      + marca()))
  + '</div>')

# 4 · LA NOVELA, sobre balcones al sol: el terrat de la Colometa y sus palomas.
T['diamant-4'] = (raiz(NOCHE)
  + fondo(4)
  + kicker('Arriba, en la plaza')
  + numero('1962', 180, 240)
  + titular('Empieza la novela<br>m&aacute;s le&iacute;da en catal&aacute;n.', 460, 76)
  + sub('<i>La pla&ccedil;a del Diamant</i>, de Merc&egrave; Rodoreda. Traducida a m&aacute;s de treinta '
        'idiomas.', 700, 40, ancho=880)
  + sub('La escultura de la plaza es la Colometa: la protagonista, atrapada contra un muro '
        'mientras las palomas levantan el vuelo.', 850, 36, 'rgba(255, 253, 249, 0.72)', ancho=880)
  + marca()
  + '</div>')

# 5 · EL NOMBRE, sobre una calle estrecha del barrio: las que bautizó el joyero.
T['diamant-5'] = (raiz(NOCHE)
  + fondo(5)
  + kicker('Y el nombre')
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
  + fondo(6, VELO_TELEFONO)
  + kicker('C&oacute;mo se entera uno de esto')
  + titular('Te lo cuenta al o&iacute;do,<br>mientras lo andas.', 180, 82)
  + (telefono(CAPTURA, 430, 520) if hay(CAPTURA, '') else
     pendiente('FALTA LA CAPTURA<br>del tour de la app<br>con esta parada', 430, 520))
  + '</div>')

# 7 · EL CIERRE, el del reel, sobre Barcelona al anochecer desde el Park Güell: la última
#     que se ve y la única con la ciudad entera. Sin «todavía no está publicada»: el dueño
#     lo quitó del reel el 5-sep y aquí tampoco hace falta, la lista de espera ya lo dice.
T['diamant-7'] = (raiz(NOCHE)
  + fondo(7, VELO_FOTO)
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
    open(f'{stem.replace("diamant", PREFIJO, 1)}.dc.html', 'w').write(pagina(html))

faltan = [f for f in FOTOS.values() if not hay(f)] + \
         ([CAPTURA] if not hay(CAPTURA, '') else [])
print(f'{len(T)} tarjetas ({PREFIJO}-*): ' + ', '.join(T))
if faltan: print('FALTA, y la tarjeta lo dice en naranja: ' + ', '.join(faltan))
