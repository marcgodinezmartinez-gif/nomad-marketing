# «AQUÍ HAY ALGO QUE CASI NADIE SABE» — la Plaça del Diamant, seis tarjetas, TODAS CON FOTO (7-sep).
#
# El porqué y los hechos verificados, en piezas/barcelona/GUION.md. En una frase: el reel
# se guardó CERO veces con 1 258 espectadores, y lo que se guarda no es un demo de
# producto sino algo que vale por sí solo. Aquí lo que vale por sí solo es la historia de
# una plaza de barrio con un refugio antiaéreo debajo.
#
# LAS FOTOS SON OBLIGATORIAS (dueño, 6-sep: «tienen que haber fotos 100 %, es la esencia de
# mi feed») Y SIN CRÉDITO ENCIMA NI EN EL PIE (dueño, 7-sep: «dar créditos en las fotos se ve
# feísimo», «no me acaba de gustar» en el pie). Y el dueño no está en Barcelona: todo tiene
# que salir de internet. Se hizo la pasada completa por los bancos con licencia sin
# atribución —Unsplash, Pexels, Pixabay, Flickr en CC0 y dominio público, Openverse, Commons
# en CC0 y dominio público, Europeana; PxHere, Picryl, StockSnap y Reshot no responden desde
# aquí— y el resultado está en el GUION: de la plaza, de la cabina del refugio y de la
# Colometa NO HAY NI UNA FOTO SIN ATRIBUCIÓN en ningún sitio, y las de Gràcia en dominio
# público son fotos de compacta de 2007-2010, pequeñas y a pleno sol. Así que el carrusel va
# con las mejores del banco, de Unsplash y Pexels, y no debe crédito a nadie.
#
# CON_ATRIBUCION = True cambia dos fotos por las de Commons —la cabina del 232 en su plaza y
# la Colometa, CC BY-SA— y pone su línea de crédito en la tarjeta de cierre; entonces el pie
# lleva además el bloque de créditos del GUION. Es la única manera de enseñar el búnker.
#
# EL GOLPE VA EN LA TARJETA 2, a propósito: en un carrusel la gente se va pronto, y el
# refugio en la quinta no lo vería casi nadie. La 1 pregunta y la 2 responde, Y LO CUENTA
# TODO (dueño, 7-sep: «unimos la 2 y la 3 y contamos todo en una»): los 12 m, quién lo
# cavó, el 232, el 1992 y las visitas. Antes el 1992 tenía tarjeta propia; sobraba.
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
                      telefono, pendiente, numero, credito)

HELMET = open('Main.dc.html').read().split('<helmet>')[1].split('</helmet>')[0]
pagina = lambda cuerpo: _pagina(cuerpo, HELMET)

# Los ficheros que espera. Cambiar aquí y en ningún otro sitio.
CAPTURA = 'tourdiamant-900.webp'     # el tour de la app con la parada de la plaza
CON_ATRIBUCION = False
FOTOS = {
    1: 'f-bcn-plaza.jpg',    # el campanar de la plaça de la Vila de Gràcia, entre plátanos      Pexels
    2: 'f-bcn-noche.jpg',    # un callejón de noche, mojado, con luces: debajo de la ciudad      Unsplash
    3: 'f-bcn-balcon.jpg',   # balcones con plantas al sol: el terrat de la Colometa             Unsplash
    4: 'f-bcn-calle.jpg',    # una calle estrecha con árboles y bolardos: las calles del joyero  Unsplash
    5: 'f-bcn-paseo.jpg',    # gente andando por el casco antiguo: «mientras lo andas»           Unsplash
    6: 'f-bcn-cierre.jpg',   # Barcelona al anochecer desde el Park Güell, que es Gràcia         Unsplash
}
CREDITO_CIERRE = ''
if CON_ATRIBUCION:
    FOTOS[2] = 'f-diamant-boca.jpg'       # la cabina de entrada del 232, en su plaza   CC BY-SA 4.0
    FOTOS[3] = 'f-diamant-colometa.jpg'   # la Colometa                                 CC BY-SA 3.0
    # El mismo texto que banco/fotos/creditos.json; se cambian los dos a la vez.
    CREDITO_CIERRE = ('Fotos de la plaza: Vanbasten 23 y 1997 &middot; Wikimedia Commons &middot; '
                      'CC BY-SA 4.0 / 3.0')

# En las tarjetas 2-4 el texto ocupa dos tercios del alto (número, titular y párrafo), así
# que el velo de foto de la casa —claro en el centro— dejaría letras sobre fachada al sol.
# Éste es más parejo: la foto se ve, pero detrás del texto.
VELO_TEXTO = ('linear-gradient(180deg, rgba(16, 14, 11, 0.8) 0%, rgba(16, 14, 11, 0.64) 55%, '
              'rgba(16, 14, 11, 0.42) 100%)')
# En la portada el texto está arriba y la plaza abajo: el velo de la casa oscurece el pie al
# 86 % y se comería la terraza. Éste deja ver la plaza entera.
VELO_PORTADA = ('linear-gradient(180deg, rgba(16, 14, 11, 0.76) 0%, rgba(16, 14, 11, 0.3) 45%, '
                'rgba(16, 14, 11, 0.58) 100%)')

def hay(f, carpeta='fotos'):
    return os.path.exists(f'{carpeta}/{f}' if carpeta else f)

def fondo(n, v=VELO_TEXTO, escala=1.04):
    """La foto de la tarjeta n con su velo y, si exige atribución, su crédito. Si la foto no
    está, el lienzo oscuro y un aviso: se ve de un vistazo qué tarjeta está a medias."""
    f = FOTOS[n]
    if not hay(f):
        return velo(NOCHE) + ('<p class="sans" style="position: absolute; left: 84px; top: 1050px; margin: 0; '
                              'font-size: 26px; font-weight: 700; color: #E4572E; letter-spacing: 0.06em">'
                              f'FALTA LA FOTO &middot; {f}</p>')
    return foto(f, escala) + velo(v)

T = {}

# 1 · EL GANCHO. El campanar de Gràcia entre plátanos: quien conoce el barrio lo reconoce
#     al instante, y el texto habla del barrio («aquí»), no de la foto. No dice «¿Conocías
#     este lugar?» porque la foto no es la plaza; la plaza aparece en la 2, con el búnker.
T['diamant-1'] = (raiz(NOCHE)
  + fondo(1, VELO_PORTADA)
  + kicker('Barcelona &middot; Gr&agrave;cia')
  + titular('Aqu&iacute; hay algo<br>que casi nadie sabe.', 190, 100)
  + sub('Una plaza de barrio con tres historias debajo.', 480, 40, ancho=860)
  + marca()
  + '</div>')

# 2 · EL GOLPE, entero: la medida de protagonista, y debajo quién lo cavó, cuándo apareció y
#     cómo se visita. Detrás, un callejón de noche: debajo de la ciudad. Con CON_ATRIBUCION,
#     la cabina de entrada del refugio con la escalera que baja tras el cristal.
T['diamant-2'] = (raiz(NOCHE)
  + fondo(2)
  + kicker('Pla&ccedil;a del Diamant &middot; bajo tus pies', 110, MENTA)
  + numero('12<span style="font-size: 120px; letter-spacing: 0">&nbsp;m</span>', 190, 300)
  + titular('Hay un refugio antia&eacute;reo.', 570, 82)
  + sub('Lo cavaron los propios vecinos durante la Guerra Civil. Cab&iacute;an m&aacute;s de '
        'doscientas personas. Es el refugio 232.', 720, 40, ancho=880)
  + sub('Nadie se acordaba de &eacute;l hasta que apareci&oacute; en 1992, haciendo obras. Barcelona '
        'lleg&oacute; a tener unos 1.300 refugios, m&aacute;s de 90 s&oacute;lo en Gr&agrave;cia. '
        'Se visita los domingos, con reserva.', 910, 36, 'rgba(255, 253, 249, 0.74)', ancho=880)
  + marca()
  + '</div>')

# 3 · LA NOVELA, sobre balcones al sol: el terrat de la Colometa y sus palomas. Con
#     CON_ATRIBUCION, la propia Colometa.
T['diamant-3'] = (raiz(NOCHE)
  + fondo(3)
  + kicker('Arriba, en la plaza')
  + numero('1962', 180, 240)
  + titular('Empieza la novela<br>m&aacute;s le&iacute;da en catal&aacute;n.', 460, 76)
  + sub('<i>La pla&ccedil;a del Diamant</i>, de Merc&egrave; Rodoreda. Traducida a m&aacute;s de treinta '
        'idiomas.', 700, 40, ancho=880)
  + sub('La escultura de la plaza es la Colometa: la protagonista, atrapada contra un muro '
        'mientras las palomas levantan el vuelo.', 850, 36, 'rgba(255, 253, 249, 0.72)', ancho=880)
  + marca()
  + '</div>')

# 4 · EL NOMBRE, sobre una calle estrecha del barrio: las que bautizó el joyero.
T['diamant-4'] = (raiz(NOCHE)
  + fondo(4)
  + kicker('Y el nombre')
  + numero('1860', 180, 240)
  + titular('Se lo puso un joyero.', 460, 82)
  + sub('Josep Rosell compr&oacute; estos terrenos y bautiz&oacute; las calles de Gr&agrave;cia con '
        'nombres de piedras preciosas. De ah&iacute; el Diamant.', 620, 40, ancho=880)
  + marca()
  + '</div>')

# 5 · LA PRUEBA. Sin esta captura el carrusel no se publica: el cierre pasaría de ser una
#     prueba a ser una promesa, y una promesa que la app no cumple es lo que la regla de
#     la casa prohíbe.
T['diamant-5'] = (raiz(NOCHE)
  + fondo(5, VELO_TELEFONO)
  + kicker('C&oacute;mo se entera uno de esto')
  + titular('Te lo cuenta al o&iacute;do,<br>mientras lo andas.', 180, 82)
  + (telefono(CAPTURA, 430, 520) if hay(CAPTURA, '') else
     pendiente('FALTA LA CAPTURA<br>del tour de la app<br>con esta parada', 430, 520))
  + '</div>')

# 6 · EL CIERRE, el del reel, sobre Barcelona al anochecer desde el Park Güell: la última
#     que se ve y la única con la ciudad entera. Sin «todavía no está publicada»: el dueño
#     lo quitó del reel el 5-sep y aquí tampoco hace falta, la lista de espera ya lo dice.
T['diamant-6'] = (raiz(NOCHE)
  + fondo(6, VELO_FOTO)
  + kicker('Lista de espera abierta')
  + titular('Llega en octubre.', 180, 96)
  + (f'<h2 class="serif" style="position: absolute; left: 84px; top: 320px; margin: 0; width: 912px; '
     f'font-size: 84px; line-height: 1.06; letter-spacing: -0.018em; font-weight: 400; {SOMBRA}">'
     f'Tu primer viaje por <span style="color: {MENTA}">1,99&nbsp;&euro;</span>*</h2>')
  + sub('*Si te apuntas a la lista de espera en travelsnomad.com', 450, 32,
        'rgba(255, 253, 249, 0.8)')
  + marca()
  + (credito(CREDITO_CIERRE, 1292, 'rgba(255, 253, 249, 0.5)') if CREDITO_CIERRE else '')
  + '</div>')

for stem, html in T.items():
    open(f'{stem}.dc.html', 'w').write(pagina(html))

faltan = [f for f in FOTOS.values() if not hay(f)] + \
         ([CAPTURA] if not hay(CAPTURA, '') else [])
print(f'{len(T)} tarjetas: ' + ', '.join(T))
if faltan: print('FALTA, y la tarjeta lo dice en naranja: ' + ', '.join(faltan))
