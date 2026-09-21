# LA MERCÈ — seis tarjetas (21-sep). La fiesta mayor de Barcelona, del 23 al 27 de septiembre.
#
# POR QUÉ ESTA PIEZA Y NO OTRA. El dueño quería subir algo de la Mercè con el cartel oficial
# dentro. **El cartel no se puede reproducir**: el de 2026 es obra de la muralista Cinta
# Vidal, con sus derechos, y la regla de la casa sólo admite lo que no debe atribución. Y en
# una cuenta comercial, el cartel oficial además insinuaría un vínculo con el Ajuntament que
# no existe. Así que la portada es nuestra, con el molde de la casa, y el cartel se cita en
# el pie (citar sí se puede; reproducir, no).
#
# EL GANCHO ES VERDAD Y CASI NADIE LO SABE: la Mercè es patrona de Barcelona por una plaga
# de langostas. Verificado en dos fuentes (el Ajuntament y Wikipedia), como manda la casa.
#
# LA TARJETA 4 ES LA QUE SE GUARDA. Los insights del reel decían que lo que falta son
# guardados, y lo que se guarda es un plan con horas. Por eso el programa va en tarjeta
# propia, con los actos grandes y su día.
#
# LAS FOTOS NO SON DE LA MERCÈ y eso importa: son castells de Tarragona y correfocs de Les
# Borges Blanques, de archivo. Ninguna tarjeta dice «esto es la plaça de Sant Jaume»: el
# texto habla de la tradición, la foto la ilustra. Enseñar un sitio diciendo «éste» es lo
# único que la casa no hace.
#
# Uso, desde salida/:  python3 ../piezas/merce/gen-merce.py
#                      node ../piezas/roma/exportar-plan.mjs merce 6
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tarjetas import (SOMBRA, MENTA, NOCHE, VELO_FOTO, VELO_TELEFONO,
                      pagina as _pagina, raiz, foto, velo, kicker, titular, sub, marca,
                      telefono, pendiente, numero)

HELMET = open('Main.dc.html').read().split('<helmet>')[1].split('</helmet>')[0]
pagina = lambda cuerpo: _pagina(cuerpo, HELMET)

CAPTURA = 'tourgotic-900.webp'   # el tour a pie de la app por Ciutat Vella

# El velo parejo de la serie: el texto ocupa dos tercios y la foto se ve detrás.
VELO_TEXTO = ('linear-gradient(180deg, rgba(16, 14, 11, 0.8) 0%, rgba(16, 14, 11, 0.64) 55%, '
              'rgba(16, 14, 11, 0.42) 100%)')
VELO_PORTADA = ('linear-gradient(180deg, rgba(16, 14, 11, 0.78) 0%, rgba(16, 14, 11, 0.34) 45%, '
                'rgba(16, 14, 11, 0.6) 100%)')
# Sobre el programa el texto son seis líneas: hace falta un velo más cerrado y parejo.
VELO_PROGRAMA = ('linear-gradient(180deg, rgba(16, 14, 11, 0.86) 0%, rgba(16, 14, 11, 0.78) 60%, '
                 'rgba(16, 14, 11, 0.6) 100%)')

# El programa, contrastado el 21-sep entre betevé (el medio público municipal) y la prensa.
# Sólo entra lo que coincide o lo que da betevé; donde las fuentes discrepaban —el recorrido
# del correfoc, Via Laietana o passeig de Gràcia— NO se pone el sitio.
PROGRAMA = [
    ('Mi&eacute; 23', 'El preg&oacute;n abre la fiesta',          'Sal&oacute; de Cent &middot; 18.30 h'),
    ('Jue 24',        'Els castells',                             'Pla&ccedil;a de Sant Jaume &middot; 13 h'),
    ('Jue 24',        'La cercavila de gegants',                  'Pl. Catalunya 18 h &middot; St. Jaume 19 h'),
    ('S&aacute;b 26', 'El correfoc',                              '20.30 h'),
    ('Dom 27',        'Diada castellera',                         'Pla&ccedil;a de Sant Jaume &middot; 12 h'),
    ('Dom 27',        'El piromusical',                           'Platja de la Nova Ic&agrave;ria &middot; 22 h'),
]

def hay(f, carpeta='fotos'):
    return os.path.exists(f'{carpeta}/{f}' if carpeta else f)

def fondo(f, v=VELO_TEXTO):
    if not hay(f):
        return velo(NOCHE) + ('<p class="sans" style="position: absolute; left: 84px; top: 1050px; margin: 0; '
                              'font-size: 26px; font-weight: 700; color: #E4572E; letter-spacing: 0.06em">'
                              f'FALTA LA FOTO &middot; {f}</p>')
    return foto(f, 1.04) + velo(v)

def fila(dia, que, donde, y):
    """Un acto del programa. El día en serif a la izquierda, como las horas del plan de Roma;
    el sitio y la hora debajo, que es lo que hace que la tarjeta se guarde."""
    return (f'<div style="position: absolute; left: 84px; top: {y}px; width: 912px; display: flex; gap: 28px">'
            f'<span class="serif" style="font-size: 40px; line-height: 1.1; color: rgba(255, 253, 249, 0.55); '
            f'width: 128px; flex: none">{dia}</span>'
            f'<span style="display: block">'
            f'<span class="sans" style="display: block; font-size: 36px; line-height: 1.2; font-weight: 600">{que}</span>'
            f'<span class="sans" style="display: block; font-size: 27px; line-height: 1.45; margin-top: 4px; '
            f'color: {MENTA}; font-weight: 600">{donde}</span></span></div>')

T = {}

# 1 · EL GANCHO. Un castell altísimo y el dato que nadie espera.
T['merce-1'] = (raiz(NOCHE)
  + fondo('f-merce-castell.jpg', VELO_PORTADA)
  + kicker('Barcelona &middot; del 23 al 27 de septiembre')
  + titular('La Merc&egrave; empez&oacute;<br>por una plaga.', 190, 100)
  + sub('La fiesta m&aacute;s grande de la ciudad. Y casi todo es gratis.', 480, 40, ancho=860)
  + marca()
  + '</div>')

# 2 · EL GOLPE. La plaga y el voto del Consell de Cent.
T['merce-2'] = (raiz(NOCHE)
  + fondo('f-merce-diable.jpg')
  + kicker('Por qu&eacute; existe', 110, MENTA)
  + numero('1687', 180, 240)
  + titular('Una plaga de langostas.', 460, 76)
  + sub('Barcelona se encomend&oacute; a la Mare de D&eacute;u de la Merc&egrave; y el Consell de Cent hizo un '
        'voto: si la plaga se iba, la nombrar&iacute;a patrona de la ciudad.', 620, 40, ancho=880)
  + sub('Se fue. Y cumplieron.', 900, 36, 'rgba(255, 253, 249, 0.74)', ancho=880)
  + marca()
  + '</div>')

# 3 · POR QUÉ EL 24 DE SEPTIEMBRE.
T['merce-3'] = (raiz(NOCHE)
  + fondo('f-merce-castell2.jpg')
  + kicker('Y por qu&eacute; el 24 de septiembre')
  + numero('1868', 180, 240, MENTA)
  + titular('Casi dos siglos despu&eacute;s,<br>se hizo oficial.', 440, 76)
  + sub('El papa P&iacute;o IX confirm&oacute; a la Merc&egrave; como patrona de Barcelona. Desde entonces la '
        'ciudad celebra su fiesta mayor alrededor del 24, que es su d&iacute;a.', 660, 40, ancho=880)
  + marca()
  + '</div>')

# 4 · EL PROGRAMA. La que se guarda: seis actos con su día y su hora.
T['merce-4'] = (raiz(NOCHE)
  + fondo('f-bcn-noche.jpg', VELO_PROGRAMA)
  + kicker('Lo que no te puedes perder')
  + titular('Cinco d&iacute;as de fiesta.', 180, 82)
  + ''.join(fila(d, q, s, 330 + i * 140) for i, (d, q, s) in enumerate(PROGRAMA))
  + sub('M&aacute;s de quinientas actividades en los diez distritos. Programa entero en barcelona.cat/lamerce',
        1200, 28, 'rgba(255, 253, 249, 0.66)')
  + '</div>')

# 5 · LA PRUEBA. Sin la captura, el cierre sería una promesa.
T['merce-5'] = (raiz(NOCHE)
  + fondo('f-bcn-paseo.jpg', VELO_TELEFONO)
  + kicker('Y el resto del a&ntilde;o')
  + titular('Barcelona, contada<br>mientras la andas.', 180, 82)
  + (telefono(CAPTURA, 430, 520) if hay(CAPTURA, '') else
     pendiente('FALTA LA CAPTURA<br>del tour a pie<br>por Ciutat Vella', 430, 520))
  + '</div>')

# 6 · EL CIERRE, el de siempre, sobre las chispas de un correfoc.
T['merce-6'] = (raiz(NOCHE)
  + fondo('f-merce-espurnes.jpg', VELO_FOTO)
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

faltan = [f for f in ('f-merce-castell.jpg', 'f-merce-diable.jpg', 'f-merce-castell2.jpg',
                      'f-bcn-noche.jpg', 'f-bcn-paseo.jpg', 'f-merce-espurnes.jpg') if not hay(f)]
if not hay(CAPTURA, ''): faltan.append(CAPTURA)
print(f'{len(T)} tarjetas: ' + ', '.join(T))
if faltan: print('FALTA, y la tarjeta lo dice en naranja: ' + ', '.join(faltan))
