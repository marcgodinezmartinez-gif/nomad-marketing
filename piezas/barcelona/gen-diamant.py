# «¿CONOCÍAS ESTE LUGAR?» — la Plaça del Diamant, siete tarjetas, TODAS CON FOTO (7-sep).
#
# El porqué y los hechos verificados, en piezas/barcelona/GUION.md. En una frase: el reel
# se guardó CERO veces con 1 258 espectadores, y lo que se guarda no es un demo de
# producto sino algo que vale por sí solo. Aquí lo que vale por sí solo es la historia de
# una plaza de barrio con un refugio antiaéreo debajo.
#
# LAS FOTOS SON OBLIGATORIAS (dueño, 6-sep: «tienen que haber fotos 100 %, es la esencia de
# mi feed») Y SON DEL SITIO (dueño, 7-sep: «quiero fotos de la plaza, del refugio, del
# interior del refugio; es como mejor va a quedar el carrusel»). De la plaza y del refugio
# sólo hay fotos en Commons y son CC BY-SA, así que la regla de la casa cambió a conciencia
# ese día (AGENTS.md): ESAS FOTOS ENTRAN CON SU ATRIBUCIÓN EN LA PROPIA TARJETA —credito(),
# debajo de la marca— Y EN EL PIE, y la tarjeta que las lleva queda bajo CC BY-SA por el
# ShareAlike. Las tarjetas 5, 6 y 7 llevan Unsplash, sin atribución.
#
# DEL INTERIOR DEL 232 NO HAY NINGUNA FOTO LIBRE, con ninguna licencia. El interior que se
# ve es el del refugio 307 (Poble-sec), de la misma red y el mismo año, y LA TARJETA LO
# DICE, en el texto y en el crédito: enseñar otro refugio sin decirlo sería la promesa que
# la app no cumple, en versión foto. Cuando el dueño baje al 232 (domingos a las 11:00, con
# reserva) o el Taller d'Història de Gràcia ceda una foto, se cambian FOTOS[3] y CREDITO[3].
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
                      telefono, pendiente, numero, credito)

HELMET = open('Main.dc.html').read().split('<helmet>')[1].split('</helmet>')[0]
pagina = lambda cuerpo: _pagina(cuerpo, HELMET)

# Los ficheros que espera. Cambiar aquí y en ningún otro sitio.
CAPTURA = 'tourdiamant-900.webp'     # el tour de la app con la parada de la plaza
FOTOS = {
    1: 'f-diamant-plaza.jpg',       # la plaza de día, con la terraza: ES el sitio          CC BY-SA 3.0
    2: 'f-diamant-boca.jpg',        # la cabina de entrada del 232, la escalera tras el cristal  CC BY-SA 4.0
    3: 'f-refugi307-interior.jpg',  # la galería de ladrillo del refugio 307, Poble-sec    CC BY-SA 3.0
    4: 'f-diamant-colometa.jpg',    # la Colometa                                          CC BY-SA 3.0
    5: 'f-bcn-calle.jpg',           # una calle estrecha con árboles: las calles del joyero  Unsplash
    6: 'f-bcn-paseo.jpg',           # gente andando por el casco antiguo: «mientras lo andas»  Unsplash
    7: 'f-bcn-cierre.jpg',          # Barcelona al anochecer desde el Park Güell, que es Gràcia  Unsplash
}
# El crédito que va EN la tarjeta. El texto es el mismo que en banco/fotos/creditos.json:
# se cambian los dos a la vez o no se cambia ninguno.
CREDITO = {
    1: 'Foto: 1997 &middot; Wikimedia Commons &middot; CC BY-SA 3.0',
    2: 'Foto: Vanbasten 23 &middot; Wikimedia Commons &middot; CC BY-SA 4.0',
    3: 'Foto: refugio 307 (Poble-sec), Pere Herrero / MUHBA &middot; Wikimedia Commons &middot; CC BY-SA 3.0',
    4: 'Foto: 1997 &middot; Wikimedia Commons &middot; CC BY-SA 3.0',
}

# En las tarjetas 2-5 el texto ocupa dos tercios del alto (número, titular y párrafo), así
# que el velo de foto de la casa —claro en el centro— dejaría letras sobre fachada al sol.
# Éste es más parejo: la foto se ve, pero detrás del texto.
VELO_TEXTO = ('linear-gradient(180deg, rgba(16, 14, 11, 0.8) 0%, rgba(16, 14, 11, 0.64) 55%, '
              'rgba(16, 14, 11, 0.42) 100%)')
# En la portada el texto está arriba y la plaza abajo: el velo de la casa oscurece el pie al
# 86 % y se comería la terraza. Éste deja ver la plaza entera.
VELO_PORTADA = ('linear-gradient(180deg, rgba(16, 14, 11, 0.76) 0%, rgba(16, 14, 11, 0.3) 45%, '
                'rgba(16, 14, 11, 0.58) 100%)')
# La galería del refugio ya es oscura: con el velo de texto se perdía el ladrillo. Éste
# aclara el pie para que se vea la bóveda y la lámpara.
VELO_GALERIA = ('linear-gradient(180deg, rgba(16, 14, 11, 0.74) 0%, rgba(16, 14, 11, 0.5) 55%, '
                'rgba(16, 14, 11, 0.26) 100%)')

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
    return foto(f, escala) + velo(v) + (credito(CREDITO[n]) if n in CREDITO else '')

T = {}

# 1 · EL GANCHO, sobre la plaza de verdad: por eso puede preguntar por «este lugar».
T['diamant-1'] = (raiz(NOCHE)
  + fondo(1, VELO_PORTADA)
  + kicker('Barcelona &middot; Gr&agrave;cia')
  + titular('&iquest;Conoc&iacute;as<br>este lugar?', 190, 108)
  + sub('Es una plaza de barrio. Y tiene tres historias debajo.', 480, 40, ancho=860)
  + marca()
  + '</div>')

# 2 · EL GOLPE, con la medida de protagonista y, detrás, la cabina de entrada del refugio
#     con la escalera que baja tras el cristal: la prueba de que está ahí.
T['diamant-2'] = (raiz(NOCHE)
  + fondo(2)
  + kicker('Pla&ccedil;a del Diamant &middot; bajo tus pies', 110, MENTA)
  + numero('12<span style="font-size: 120px; letter-spacing: 0">&nbsp;m</span>', 190, 300)
  + titular('Hay un refugio antia&eacute;reo.', 570, 82)
  + sub('Lo cavaron los propios vecinos durante la Guerra Civil. Cab&iacute;an m&aacute;s de '
        'doscientas personas. Es el refugio 232.', 720, 40, ancho=880)
  + marca()
  + '</div>')

# 3 · EL AÑO EN QUE APARECIÓ, sobre la galería de un refugio de la misma red. Es el 307 del
#     Poble-sec, no el 232, y se dice en el texto («como éste, el 307») y en el crédito.
T['diamant-3'] = (raiz(NOCHE)
  + fondo(3, VELO_GALERIA)
  + kicker('Y nadie lo sab&iacute;a')
  + numero('1992', 180, 240, MENTA)
  + titular('Apareci&oacute; haciendo obras.', 460, 76)
  + sub('Como &eacute;ste, el 307 del Poble-sec, Barcelona lleg&oacute; a tener unos 1.300; m&aacute;s de 90 '
        's&oacute;lo en Gr&agrave;cia. El de la plaza se visita los domingos, con reserva.', 620, 40, ancho=880)
  + marca()
  + '</div>')

# 4 · LA NOVELA, sobre la Colometa: la escultura de la que habla el párrafo.
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
    open(f'{stem}.dc.html', 'w').write(pagina(html))

faltan = [f for f in FOTOS.values() if not hay(f)] + \
         ([CAPTURA] if not hay(CAPTURA, '') else [])
print(f'{len(T)} tarjetas: ' + ', '.join(T))
if faltan: print('FALTA, y la tarjeta lo dice en naranja: ' + ', '.join(faltan))
