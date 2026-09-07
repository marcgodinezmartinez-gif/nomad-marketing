# «¿CONOCÍAS ESTE LUGAR?» — la serie (7-sep). Un sitio muy fotografiado, una historia que
# casi nadie sabe, y la app contándola en la parada del tour.
#
# NACIÓ DEL CARRUSEL DE LA PLAÇA DEL DIAMANT (piezas/barcelona), que se quedó sin fotos del
# sitio: de una plaza de barrio no hay ni una foto libre. De aquí la regla de la serie, que
# el dueño fijó el 7-sep: «coge lo mejor en cuanto a fotos y en cuanto a explicación». Los
# tres filtros, en orden: (1) una historia que sorprenda y se pueda comprobar; (2) UN SITIO
# MUY FOTOGRAFIADO, porque Unsplash y Pexels sólo tienen lo famoso, y la portada tiene que
# SER el sitio para poder preguntar «¿conocías este lugar?»; (3) que sea parada de un tour
# de la app, porque la tarjeta del móvil es la prueba y sin ella el cierre es una promesa.
#
# Seis tarjetas, el molde de piezas/tarjetas.py: portada con pregunta, el golpe con un
# número grande, dos de profundidad, el móvil con la captura, y el cierre del reel. Sin
# crédito en ninguna tarjeta ni en el pie: todas las fotos son Unsplash o Pexels.
#
# Cada dato de aquí está comprobado contra las fuentes que lista el .md de la pieza; si se
# cambia una cifra, se vuelve a comprobar. Lo que no se ha podido confirmar en dos fuentes
# NO está en la tarjeta (la altitud del Turó de la Rovira, por ejemplo: 262 m en una, 167 en
# otra).
#
# Uso, desde salida/:  python3 ../piezas/conocias/gen-conocias.py carmel
#                      node ../piezas/roma/exportar-plan.mjs carmel 6
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tarjetas import (SOMBRA, MENTA, NOCHE, VELO_FOTO, VELO_TELEFONO,
                      pagina as _pagina, raiz, foto, velo, kicker, titular, sub, marca,
                      telefono, pendiente, numero)

HELMET = open('Main.dc.html').read().split('<helmet>')[1].split('</helmet>')[0]
pagina = lambda cuerpo: _pagina(cuerpo, HELMET)

# Velos: en las tarjetas de dato el texto ocupa dos tercios del alto, así que el velo es
# parejo; en la portada y el cierre el texto está arriba y la foto se deja ver abajo.
VELO_TEXTO = ('linear-gradient(180deg, rgba(16, 14, 11, 0.8) 0%, rgba(16, 14, 11, 0.64) 55%, '
              'rgba(16, 14, 11, 0.42) 100%)')
VELO_PORTADA = ('linear-gradient(180deg, rgba(16, 14, 11, 0.76) 0%, rgba(16, 14, 11, 0.3) 45%, '
                'rgba(16, 14, 11, 0.58) 100%)')

def hay(f, carpeta='fotos'):
    return os.path.exists(f'{carpeta}/{f}' if carpeta else f)

def fondo(f, v):
    if not hay(f):
        return velo(NOCHE) + ('<p class="sans" style="position: absolute; left: 84px; top: 1050px; margin: 0; '
                              'font-size: 26px; font-weight: 700; color: #E4572E; letter-spacing: 0.06em">'
                              f'FALTA LA FOTO &middot; {f}</p>')
    return foto(f, 1.04) + velo(v)

# ── Los cuatro tipos de tarjeta ──────────────────────────────────────────────────────────
def portada(t):
    return (raiz(NOCHE) + fondo(t['foto'], VELO_PORTADA)
            + kicker(t['kicker'])
            + titular(t.get('titular', '&iquest;Conoc&iacute;as<br>este lugar?'), 190, 108)
            + sub(t['sub'], 480, 40, ancho=860)
            + marca() + '</div>')

def dato(t):
    """Kicker, número grande, titular y uno o dos párrafos. El segundo, más ligero."""
    h = (raiz(NOCHE) + fondo(t['foto'], VELO_TEXTO)
         + kicker(t['kicker'], 110, MENTA if t.get('kicker_menta') else None)
         + numero(t['numero'], 180, t.get('numero_size', 240), MENTA if t.get('numero_menta') else None)
         + titular(t['titular'], t.get('titular_y', 460), t.get('titular_size', 76)))
    y = t.get('sub_y', 620)
    subs = t['subs'] if isinstance(t['subs'], (list, tuple)) else [t['subs']]
    for i, s in enumerate(subs):
        if i == 0: h += sub(s, y, 40, ancho=880)
        else:      h += sub(s, t.get('sub2_y', 900), 36, 'rgba(255, 253, 249, 0.74)', ancho=880)
    return h + marca() + '</div>'

def app(t, captura):
    return (raiz(NOCHE) + fondo(t['foto'], VELO_TELEFONO)
            + kicker('En el tour de NOMAD')
            + titular('Cada parada, con su historia.<br>Al o&iacute;do, mientras caminas.', 180, 76)
            + (telefono(captura, 430, 520) if hay(captura, '') else
               pendiente('FALTA LA CAPTURA<br>del tour de la app<br>con esta parada', 430, 520))
            + '</div>')

def cierre(t):
    return (raiz(NOCHE) + fondo(t['foto'], VELO_FOTO)
            + kicker('Lista de espera abierta')
            + titular('Llega en octubre.', 180, 96)
            + (f'<h2 class="serif" style="position: absolute; left: 84px; top: 320px; margin: 0; width: 912px; '
               f'font-size: 84px; line-height: 1.06; letter-spacing: -0.018em; font-weight: 400; {SOMBRA}">'
               f'Tu primer viaje por <span style="color: {MENTA}">1,99&nbsp;&euro;</span>*</h2>')
            + sub('*Si te apuntas a la lista de espera en travelsnomad.com', 450, 32, 'rgba(255, 253, 249, 0.8)')
            + marca() + '</div>')

TIPOS = dict(portada=portada, dato=dato, app=app, cierre=cierre)

# ── Las piezas ───────────────────────────────────────────────────────────────────────────
PIEZAS = {}

# BÚNKERS DEL CARMEL. Fuentes y copia: piezas/conocias/CARMEL.md.
# Textos reescritos el 7-sep con la voz de la app (dueño: «adaptar los textos a la
# profesionalidad de la app»): precisos, sin coloquialismos, el tono de una guía.
PIEZAS['carmel'] = dict(captura='tourcarmel-900.webp', tarjetas=[
  dict(tipo='portada', foto='f-carmel-portada.jpg', kicker='Barcelona &middot; Tur&oacute; de la Rovira',
       sub='Uno de los miradores m&aacute;s visitados de la ciudad. Su historia empieza en 1937.'),
  dict(tipo='dato', foto='f-carmel-plataformas.jpg', kicker='Bater&iacute;a antia&eacute;rea &middot; 1937-1938', kicker_menta=True,
       numero='1938', titular='Una bater&iacute;a antia&eacute;rea<br>sobre la ciudad.', titular_y=440, sub_y=660, sub2_y=920,
       subs=['Siete plataformas de tiro y cuatro ca&ntilde;ones Vickers de 105 mm, instalados a finales de 1937 '
             'para defender Barcelona de los bombardeos de la aviaci&oacute;n italiana con base en Mallorca.',
             'Barcelona fue una de las primeras ciudades del mundo sometidas a bombardeos a&eacute;reos sistem&aacute;ticos.']),
  dict(tipo='dato', foto='f-carmel-tarde.jpg', kicker='La posguerra',
       numero='1990', titular='De bater&iacute;a a barrio<br>de barracas.', titular_y=440, sub_y=660,
       subs='Terminada la guerra, sobre las plataformas creci&oacute; el asentamiento de Los Ca&ntilde;ones: '
            'un centenar de barracas habitadas hasta 1990.'),
  dict(tipo='dato', foto='f-carmel-noche.jpg', kicker='El presente', numero='2011', numero_menta=True,
       titular='Patrimonio de la ciudad.',
       subs='El Museu d&rsquo;Hist&ograve;ria de Barcelona excav&oacute; y restaur&oacute; la bater&iacute;a entre 2006 y 2008, '
            'y la abri&oacute; al p&uacute;blico en 2011. Los llamados &laquo;b&uacute;nkers&raquo; son, en realidad, '
            'las plataformas de tiro.'),
  dict(tipo='app', foto='f-carmel-gente.jpg'),
  dict(tipo='cierre', foto='f-carmel-luces.jpg'),
])

# TEMPLO DE DEBOD. Fuentes y copia: piezas/conocias/DEBOD.md.
PIEZAS['debod'] = dict(captura='tourdebod-900.webp', tarjetas=[
  dict(tipo='portada', foto='f-debod-portada.jpg', kicker='Madrid &middot; Parque del Oeste',
       sub='Un templo egipcio aut&eacute;ntico, con m&aacute;s de dos mil a&ntilde;os, en el centro de Madrid.'),
  dict(tipo='dato', foto='f-debod-luna.jpg', kicker='Templo de Debod &middot; 1968', kicker_menta=True,
       numero='1968', titular='Un regalo de Egipto<br>a Espa&ntilde;a.', titular_y=440, sub_y=660, sub2_y=920,
       subs=['La presa de Asu&aacute;n amenazaba los templos de Nubia y la UNESCO pidi&oacute; ayuda. '
             'Espa&ntilde;a particip&oacute; en el rescate de Abu Simbel, y Egipto lo agradeci&oacute; con el templo de Debod.',
             'Fueron cuatro los templos donados. Los otros tres est&aacute;n en Nueva York, Tur&iacute;n y Leiden.']),
  dict(tipo='dato', foto='f-debod-puertas.jpg', kicker='Su origen',
       numero='2.200<span style="font-size: 100px; letter-spacing: 0">&nbsp;a&ntilde;os</span>',
       titular='Fundado por un rey nubio.',
       subs='Adijalamani de Meroe lo erigi&oacute; a comienzos del siglo II a. C. Los Ptolomeos y los '
            'emperadores romanos lo ampliaron despu&eacute;s.'),
  dict(tipo='dato', foto='f-debod-nubes.jpg', kicker='Piedra a piedra', numero='1972', numero_menta=True,
       titular='Reconstruido en Madrid.',
       subs='Se levant&oacute; en el solar del antiguo Cuartel de la Monta&ntilde;a y se inaugur&oacute; el 18 de julio '
            'de 1972, orientado de este a oeste, como en su emplazamiento original junto al Nilo.'),
  dict(tipo='app', foto='f-debod-reflejo.jpg'),
  dict(tipo='cierre', foto='f-madrid.jpg'),
])

if __name__ == '__main__':
    slug = sys.argv[1] if len(sys.argv) > 1 else ''
    if slug not in PIEZAS:
        sys.exit('Uso: gen-conocias.py <pieza>   piezas: ' + ', '.join(PIEZAS))
    p = PIEZAS[slug]
    faltan = []
    for i, t in enumerate(p['tarjetas'], 1):
        html = TIPOS[t['tipo']](t, p['captura']) if t['tipo'] == 'app' else TIPOS[t['tipo']](t)
        open(f'{slug}-{i}.dc.html', 'w').write(pagina(html))
        if not hay(t['foto']): faltan.append(t['foto'])
    if not hay(p['captura'], ''): faltan.append(p['captura'])
    print(f'{len(p["tarjetas"])} tarjetas: ' + ', '.join(f'{slug}-{i}' for i in range(1, len(p['tarjetas']) + 1)))
    if faltan: print('FALTA, y la tarjeta lo dice en naranja: ' + ', '.join(faltan))
