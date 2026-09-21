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
# LAS DOS CORRECCIONES (y por qué existen): ver CORREGIDO más abajo. La app situó el
# correfoc y el piromusical en el sitio y la hora equivocados, y publicarlos tal cual habría
# mandado a la gente a Montjuïc un domingo a las siete a ver unos fuegos que son en la playa
# a las diez. Se publica el programa oficial y se deja escrito aquí qué dijo la app.
#
# Uso, desde salida/:  python3 ../piezas/merce/gen-plan-merce.py
#                      node ../piezas/roma/exportar-plan.mjs planmerce 8
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tarjetas import (SOMBRA, MENTA, PAPEL, NOCHE, VELO_FOTO, VELO_TELEFONO,
                      pagina as _pagina, raiz, foto, velo, kicker, titular, sub, marca, telefono)

HELMET = open('Main.dc.html').read().split('<helmet>')[1].split('</helmet>')[0]
pagina = lambda cuerpo: _pagina(cuerpo, HELMET)

CAPTURA = 'planmerce-24-900.webp'      # la pantalla del jueves, de la app real
PETICION = 'Barcelona, del 23 al 27 de septiembre. Quiero vivir la Merc&egrave;.'

# Cada parada: (hora, qué, categoría, precio, ¿gratis?). Copiado de las capturas.
DIAS = [
  dict(clave='23', dia='Mi&eacute;rcoles 23', total='55 &euro;', foto='f-bcn-paseo.jpg', planes=[
    ('10:30', 'Paseo por el Barri G&ograve;tic y El Born', 'Tour guiado', 'gratis', True),
    ('13:30', 'Almuerzo en El Xampanyet', 'Comida', '25 &euro;', False),
    ('16:00', 'Preg&oacute;n y pasacalles inaugural', 'Visita', 'gratis', True),
    ('20:30', 'Cena en Bar del Pla', 'Comida', '30 &euro;', False)]),

  dict(clave='24', dia='Jueves 24', total='55 &euro;', foto='f-merce-castell.jpg', planes=[
    ('10:00', 'Castellers en la Pla&ccedil;a de Sant Jaume', 'Visita', 'gratis', True),
    ('13:30', 'Almuerzo en Can Culleretes', 'Comida', '30 &euro;', False),
    ('16:00', 'Cabalgata por el Passeig de Gr&agrave;cia', 'Visita', 'gratis', True),
    ('21:00', 'Cena y BAM en la Pla&ccedil;a Reial', 'Comida', '25 &euro;', False)]),

  dict(clave='25', dia='Viernes 25', total='93 &euro;', foto='f-bcn-plaza.jpg', planes=[
    ('10:00', 'Bas&iacute;lica de la Sagrada Fam&iacute;lia', 'Museo', '26 &euro;', False),
    ('13:00', 'Paseo por el Parc de la Ciutadella', 'Visita', 'gratis', True),
    ('14:45', 'Almuerzo en Bodega La Puntual', 'Comida', '30 &euro;', False),
    ('17:00', 'Visita al Museo Picasso', 'Museo', '12 &euro;', False),
    ('21:00', 'Cena y conciertos en el Moll de la Fusta', 'Comida', '25 &euro;', False)]),

  dict(clave='26', dia='S&aacute;bado 26', total='75 &euro;', foto='f-merce-diable.jpg', planes=[
    ('10:30', 'Recorrido por el Park G&uuml;ell', 'Visita', '10 &euro;', False),
    ('13:30', 'Almuerzo en La Benaura', 'Comida', '25 &euro;', False),
    # CORREGIDO. La app: «18:00 · Correfoc de La Mercè en Via Laietana». El correfoc grande
    # es a las 20:30 y sale del Passeig de Gràcia (Provença → Consell de Cent) desde 2022;
    # a las 18:00 es el Correfoc dels Petits, en sentido inverso. Fuente: barcelona.cat
    # (Cultura Popular, «El Correfoc de la Mercè torna al passeig de Gràcia») y betevé.
    ('20:30', 'Correfoc en el Passeig de Gr&agrave;cia', 'Visita', 'gratis', True),
    ('21:00', 'Cena en Bar Ca&ntilde;ete', 'Comida', '40 &euro;', False)]),

  dict(clave='27', dia='Domingo 27', total='15 &euro;', foto='f-merce-espurnes.jpg', planes=[
    ('10:00', 'Puertas abiertas en el Palau de la Generalitat', 'Visita', 'gratis', True),
    ('12:00', 'La Rambla y el Mercado de la Boqueria', 'Visita', 'gratis', True),
    ('14:00', 'Almuerzo de despedida en Can Paixano', 'Comida', '15 &euro;', False),
    # CORREGIDO. La app: «19:00 · Piromusical de La Mercè en Montjuïc». Este año el
    # piromusical se va al litoral por las obras de la Fira: domingo 27 a las 22 h, se
    # dispara desde el espigón del Bogatell y se ve desde la Nova Icària. Fuente:
    # ajuntament.barcelona.cat (programación de la Mercè 2026), betevé y ElNacional.
    ('22:00', 'Piromusical en la playa de la Nova Ic&agrave;ria', 'Visita', 'gratis', True)]),
]

TOTAL = '293 &euro;'      # la suma de los cinco totales que da la app: 55+55+93+75+15
CUANTOS = 21              # las paradas de los cinco días
GRATIS = 9                # las que no cuestan nada

# El velo de una tarjeta de programa: abierto arriba para que la foto se vea, cerrado de la
# mitad para abajo, que es donde vive la lista. Una lista sobre foto sin cerrar no se lee, y
# ESTA es la tarjeta que se guarda.
VELO_PROGRAMA = ('linear-gradient(180deg, rgba(16, 14, 11, 0.6) 0%, rgba(16, 14, 11, 0.34) 20%, '
                 'rgba(16, 14, 11, 0.9) 52%, rgba(16, 14, 11, 0.97) 100%)')

def fila(hora, que, cat, precio, gratis):
    """Una parada. La hora en serif a la izquierda, como en la app; lo gratis en menta,
    porque en la Mercè es casi todo y es lo que hace que la tarjeta se guarde."""
    c = MENTA if gratis else 'rgba(255, 253, 249, 0.6)'
    return ('<div style="display: flex; gap: 30px; align-items: baseline">'
            f'<span class="serif" style="font-size: 44px; line-height: 1.1; color: rgba(255, 253, 249, 0.5); '
            f'width: 118px; flex: none">{hora}</span>'
            '<span style="display: block">'
            f'<span class="sans" style="display: block; font-size: 38px; line-height: 1.2; font-weight: 600">{que}</span>'
            f'<span class="sans" style="display: block; font-size: 28px; line-height: 1.5; margin-top: 4px; '
            f'color: {c}; font-weight: 600">{cat} &middot; {precio}</span></span></div>')

def programa(planes, abajo=210):
    """Las paradas del día, ancladas ABAJO y en columna flex: así el bloque acaba a la misma
    altura tanto si el día trae cuatro paradas como cinco, y una que se parta en dos
    renglones no empuja a la siguiente encima de la marca."""
    return (f'<div style="position: absolute; left: 84px; bottom: {abajo}px; width: 912px; '
            f'display: flex; flex-direction: column; gap: 28px">'
            + ''.join(fila(*p) for p in planes) + '</div>')

def peticion(t, y=196):
    """LA PETICIÓN, escrita como se escribe en la app. Es el gancho del formato: se ve lo
    que se pide antes de ver lo que sale, y por eso va en la portada y no en el pie."""
    return (f'<div style="position: absolute; left: 84px; top: {y}px; width: 912px; box-sizing: border-box; '
            f'padding: 34px 38px; border-radius: 28px; background: rgba(255, 253, 249, 0.1); '
            f'border: 2px solid rgba(255, 253, 249, 0.28); backdrop-filter: blur(6px)">'
            f'<span class="sans" style="display: block; font-size: 26px; letter-spacing: 0.16em; '
            f'text-transform: uppercase; color: {MENTA}; font-weight: 700">T&uacute; escribes</span>'
            f'<span class="sans" style="display: block; margin-top: 16px; font-size: 40px; line-height: 1.28; '
            f'font-weight: 500; color: {PAPEL}">&laquo;{t}&raquo;</span></div>')

def hay(f, carpeta='fotos'):
    return os.path.exists(f'{carpeta}/{f}' if carpeta else f)

if not DIAS or any(not d['planes'] for d in DIAS):
    sys.exit('FALTA EL PLAN. Se lee de las capturas de la app, fila a fila. No se inventa ni\n'
             'una línea: un plan inventado es la promesa que la app no cumple.')
if not hay(CAPTURA, ''):
    sys.exit(f'FALTA LA CAPTURA {CAPTURA} en banco/capturas/')

T = {}

# 1 · LA PORTADA: la petición, y la promesa de lo que sale.
T['planmerce-1'] = (raiz(NOCHE)
  + foto('f-bcn-festa.jpg', 1.06) + velo(VELO_FOTO)
  + kicker('Le pedimos esto a NOMAD')
  + peticion(PETICION)
  + titular('Y esto es lo<br>que sali&oacute;.', 470, 92)
  + sub(f'Los cinco d&iacute;as, hora a hora: {CUANTOS} planes y {TOTAL} con todas las comidas dentro. '
        f'{GRATIS} de ellos no cuestan nada.', 700, 38, ancho=880)
  + marca()
  + '</div>')

# 2-6 · UN DÍA POR TARJETA. ESTAS son las que se guardan: la lista, legible, con precios.
for i, d in enumerate(DIAS, start=2):
    T[f'planmerce-{i}'] = (raiz(NOCHE)
      + foto(d['foto'], 1.06) + velo(VELO_PROGRAMA)
      + kicker(d['dia'], 100, MENTA)
      + titular(f'{len(d["planes"])} planes &middot; {d["total"]}', 152, 76)
      + programa(d['planes'])
      + marca()
      + '</div>')

# 7 · CÓMO SE HIZO. La captura es de la app real, del jueves de la tarjeta 3.
T['planmerce-7'] = (raiz(NOCHE)
  + foto('f-bcn-calle.jpg', 1.06) + velo(VELO_TELEFONO)
  + kicker('C&oacute;mo se hizo')
  + titular('Un minuto.<br>Ni una reserva.', 170, 88)
  + sub('Escribes el sitio y los d&iacute;as. La app monta el plan entero, con horas y precios.',
        400, 36, ancho=880)
  + telefono(CAPTURA, 430, 540)
  + '</div>')

# 8 · EL CIERRE, el de siempre.
T['planmerce-8'] = (raiz(NOCHE)
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
