# «LE PEDIMOS A NOMAD LOS CINCO DÍAS DE LA MERCÈ» — carrusel de 8 tarjetas (21-sep).
#
# EL GIRO QUE PIDIÓ EL DUEÑO ese día: «no me acaba de gustar como lo he enfocado, es como
# que no hablo de la app». Tenía razón, y el repo se la daba: los tres carruseles de
# «¿Conocías este lugar?» enseñan un dato bonito y esconden la app en la tarjeta 5 de 6, y
# eso es justo lo que NO nos diferencia — la competencia curada ya cuenta bien seis
# ciudades, y mil cuentas de curiosidades tienen más volumen que nosotros.
#
# Lo que sí nos diferencia, según campana/MERCADO: LA GENERACIÓN. Cualquier sitio, cualquier
# tema, y el plan entero con precios. Así que aquí el protagonista es EL PLAN, la app es
# quien lo escribió, y la portada enseña LA PETICIÓN: el formato que pidió el dueño es
# «Le pedí a NOMAD esto y mira lo que salió».
#
# POR QUÉ LA MERCÈ Y POR QUÉ HOY: la fiesta va del 23 al 27, la ciudad está llena, y un plan
# de fiesta local es la prueba de la cola larga — ninguna guía curada tiene el jueves de la
# Mercè. Los cinco días juntos son 21 planes, 293 € con todas las comidas dentro y 9 actos
# que no cuestan nada.
#
# EL PLAN ES EL REAL DE LA APP: leído de las cinco capturas que trajo el dueño el 21-sep
# (banco/capturas/planmerce-23..27-900.webp), fila a fila, con sus horas, sus categorías y
# sus precios. Las cinco sumas cuadran con el total que da la app. Si DIAS se vacía, el
# generador PARA: una tarjeta con un plan inventado es la promesa que la app no cumple.
#
# LAS CINCO CORRECCIONES, que es lo importante de este fichero: el plan trae CINCO actos de
# la fiesta, y la app puso mal la hora de los cinco (y el sitio de tres). No son erratas: Via
# Laietana dejó de ser el recorrido del correfoc en 2022 y Montjuïc dejó de ser el sitio del
# piromusical este año. Publicarlas tal cual habría mandado a la gente a Montjuïc un domingo
# a las siete a ver unos fuegos que son en la playa a las diez. Se publica el programa
# oficial, y CORREGIDAS deja por escrito qué dijo la app y de dónde sale lo que se publica.
#
# LO QUE ESTO DEJA ROTO, y hay que decirlo antes de publicar: con las horas buenas, el jueves
# tiene la diada castellera a las 13:00 y el almuerzo a las 13:30, y el sábado el correfoc a
# las 20:30 y la cena a las 21:00. El plan de la app estaba montado ALREDEDOR de las horas
# malas, así que corregir las filas no arregla el día: hay que volver a generar el jueves y
# el sábado en la app y traer dos capturas nuevas. Los otros tres días quedan coherentes.
#
# Uso, desde salida/:  python3 ../piezas/merce/gen-plan-merce.py
#                      node ../piezas/roma/exportar-plan.mjs planmerce 8
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tarjetas import (SOMBRA, MENTA, PAPEL, NOCHE, VELO_FOTO, VELO_TELEFONO,
                      pagina as _pagina, raiz, foto, velo, kicker, titular, sub, marca, telefono)
from plan import (PETICION, DIAS, TOTAL, CUANTOS, GRATIS, VELO_PROGRAMA, AVISOS,
                  programa, peticion, aviso, cuentas, avisa_correcciones)

HELMET = open('Main.dc.html').read().split('<helmet>')[1].split('</helmet>')[0]
pagina = lambda cuerpo: _pagina(cuerpo, HELMET)

# DOS CORTES DEL MISMO CARRUSEL. Sin argumento, los cinco días (el de antes de que
# empezara la fiesta). Con `finde`, sólo lo que queda —viernes, sábado y domingo— más la
# tarjeta del aviso: es lo que sirve a partir del día 25, porque un plan de cinco días
# publicado el tercero es medio papel mojado.
#     python3 ../piezas/merce/gen-plan-merce.py         → 8 tarjetas, los cinco días
#     python3 ../piezas/merce/gen-plan-merce.py finde   → 7 tarjetas, viernes a domingo
FINDE = 'finde' in sys.argv[1:]
CAPTURA = 'planmerce-25-900.webp' if FINDE else 'planmerce-24-900.webp'

def hay(f, carpeta='fotos'):
    return os.path.exists(f'{carpeta}/{f}' if carpeta else f)

if not DIAS or any(not d['planes'] for d in DIAS):
    sys.exit('FALTA EL PLAN. Se lee de las capturas de la app, fila a fila. No se inventa ni\n'
             'una línea: un plan inventado es la promesa que la app no cumple.')
if not hay(CAPTURA, ''):
    sys.exit(f'FALTA LA CAPTURA {CAPTURA} en banco/capturas/')

T = {}
DIAS_QUE_VAN = DIAS[2:] if FINDE else DIAS
_planes, _euros, _gratis = cuentas(DIAS_QUE_VAN)

# 1 · LA PORTADA. En el corte del finde el gancho es el reloj: quedan tres días.
T['planmerce-1'] = (raiz(NOCHE)
  + foto('f-bcn-festa.jpg', 1.06) + velo(VELO_FOTO)
  + (kicker('La Merc&egrave; &middot; lo que queda') if FINDE else kicker('Le pedimos esto a NOMAD'))
  + (titular('Quedan tres d&iacute;as<br>de Merc&egrave;.', 210, 92) if FINDE else peticion(PETICION))
  + (sub('Se lo pedimos a NOMAD: viernes, s&aacute;bado y domingo, hora a hora y con precios. '
         f'{_planes} planes y {_euros}&nbsp;&euro; con todas las comidas dentro; {_gratis} no cuestan nada.',
         430, 38, ancho=880)
     if FINDE else
     titular('Y esto es lo<br>que sali&oacute;.', 470, 92))
  + ('' if FINDE else
     sub(f'Los cinco d&iacute;as, hora a hora: {CUANTOS} planes y {TOTAL} con todas las comidas dentro. '
         f'{GRATIS} de ellos no cuestan nada.', 700, 38, ancho=880))
  + marca()
  + '</div>')

_i = 2

# 2 · EL AVISO (sólo en el corte del finde), antes de los días: es lo que gana el deslizar.
if FINDE:
    T['planmerce-2'] = (raiz(NOCHE)
      + foto('f-merce-diable.jpg', 1.06) + velo(VELO_PROGRAMA)
      + kicker('Ojo, este a&ntilde;o')
      + titular('Dos cosas han<br>cambiado de sitio.', 170, 84)
      + ''.join(aviso(*a, 470 + i * 300) for i, a in enumerate(AVISOS))
      + marca()
      + '</div>')
    _i = 3

# UN DÍA POR TARJETA. ESTAS son las que se guardan: la lista, legible, con precios.
for d in DIAS_QUE_VAN:
    T[f'planmerce-{_i}'] = (raiz(NOCHE)
      + foto(d['foto'], 1.06) + velo(VELO_PROGRAMA)
      + kicker(d['dia'] + (' &middot; hoy' if FINDE and d['clave'] == '25' else ''), 100, MENTA)
      + titular(f'{len(d["planes"])} planes &middot; {d["total"]}', 152, 76)
      + programa(d['planes'])
      + marca()
      + '</div>')
    _i += 1

# CÓMO SE HIZO. La captura es de la app real, del mismo día que una de las tarjetas.
T[f'planmerce-{_i}'] = (raiz(NOCHE)
  + foto('f-bcn-calle.jpg', 1.06) + velo(VELO_TELEFONO)
  + kicker('C&oacute;mo se hizo')
  + titular('Un minuto.<br>Ni una reserva.', 170, 88)
  + sub('Escribes el sitio y los d&iacute;as. La app monta el plan entero, con horas y precios.',
        400, 36, ancho=880)
  + telefono(CAPTURA, 430, 540)
  + '</div>')

# EL CIERRE, el de siempre.
T[f'planmerce-{_i + 1}'] = (raiz(NOCHE)
  + foto('f-bcn-cierre.jpg', 1.04)
  + velo('linear-gradient(180deg, rgba(16, 14, 11, 0.6) 0%, rgba(16, 14, 11, 0.34) 32%, '
         'rgba(16, 14, 11, 0.9) 100%)')
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
print(f'{len(T)} tarjetas: ' + ', '.join(T))
avisa_correcciones()
