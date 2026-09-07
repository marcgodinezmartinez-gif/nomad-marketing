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
            + kicker('C&oacute;mo se entera uno de esto')
            + titular('Te lo cuenta al o&iacute;do,<br>mientras lo andas.', 180, 82)
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
PIEZAS['carmel'] = dict(captura='tourcarmel-900.webp', tarjetas=[
  dict(tipo='portada', foto='f-carmel-portada.jpg', kicker='Barcelona &middot; El Carmel',
       sub='El mejor mirador de la ciudad. Y no lo hicieron para mirar.'),
  dict(tipo='dato', foto='f-carmel-plataformas.jpg', kicker='Tur&oacute; de la Rovira &middot; bajo tus pies', kicker_menta=True,
       numero='1938', titular='Aqu&iacute; disparaban a los aviones.',
       subs=['Siete plataformas de tiro y cuatro ca&ntilde;ones Vickers de 105 mm, montados a finales de 1937 '
             'para defender Barcelona de los bombardeos de la aviaci&oacute;n italiana, que despegaba de Mallorca.',
             'Barcelona fue de las primeras ciudades del mundo bombardeadas sistem&aacute;ticamente desde el aire.']),
  dict(tipo='dato', foto='f-carmel-tarde.jpg', kicker='Y al acabar la guerra',
       numero='1990', titular='Fue un barrio de barracas.',
       subs='Sobre las plataformas se levant&oacute; &laquo;Los Ca&ntilde;ones&raquo;: un centenar de chabolas, '
            'con familias viviendo dentro de la bater&iacute;a. Dur&oacute; hasta 1990.'),
  dict(tipo='dato', foto='f-carmel-noche.jpg', kicker='Hoy', numero='2011', numero_menta=True,
       titular='El atardecer m&aacute;s famoso<br>de Barcelona.', titular_y=440, sub_y=660,
       subs='El MUHBA excav&oacute; la bater&iacute;a en tres veranos, de 2006 a 2008, y la abri&oacute; en 2011. '
            'Y los &laquo;b&uacute;nkers&raquo; no son b&uacute;nkers: son las plataformas de los ca&ntilde;ones.'),
  dict(tipo='app', foto='f-carmel-gente.jpg'),
  dict(tipo='cierre', foto='f-carmel-luces.jpg'),
])

# TEMPLO DE DEBOD. Fuentes y copia: piezas/conocias/DEBOD.md.
PIEZAS['debod'] = dict(captura='tourdebod-900.webp', tarjetas=[
  dict(tipo='portada', foto='f-debod-portada.jpg', kicker='Madrid &middot; Parque del Oeste',
       sub='Es egipcio de verdad. Y tiene m&aacute;s de dos mil a&ntilde;os.'),
  dict(tipo='dato', foto='f-debod-luna.jpg', kicker='Templo de Debod &middot; un regalo', kicker_menta=True,
       numero='1968', titular='Egipto lo regal&oacute;.',
       subs=['La presa de Asu&aacute;n iba a inundar los templos de Nubia y la UNESCO pidi&oacute; ayuda. '
             'Espa&ntilde;a ayud&oacute; a salvar Abu Simbel, y Egipto lo agradeci&oacute; con un templo entero.',
             'Regal&oacute; cuatro. Los otros tres est&aacute;n en Nueva York, Tur&iacute;n y Leiden.']),
  dict(tipo='dato', foto='f-debod-puertas.jpg', kicker='Dos mil a&ntilde;os antes',
       numero='2.200<span style="font-size: 100px; letter-spacing: 0">&nbsp;a&ntilde;os</span>',
       titular='Lo empez&oacute; un rey nubio.',
       subs='Adijalamani de Meroe, hacia el a&ntilde;o 200 antes de Cristo. Despu&eacute;s lo ampliaron los '
            'Ptolomeos y los emperadores de Roma.'),
  dict(tipo='dato', foto='f-debod-nubes.jpg', kicker='Piedra a piedra', numero='1972', numero_menta=True,
       titular='Y se mont&oacute; en Madrid.',
       subs='Donde estaba el Cuartel de la Monta&ntilde;a. Se abri&oacute; el 18 de julio de 1972, orientado de '
            'este a oeste, como a orillas del Nilo.'),
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
