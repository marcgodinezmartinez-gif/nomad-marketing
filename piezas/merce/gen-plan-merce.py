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
PETICION = 'Barcelona, del 23 al 27 de septiembre. Quiero vivir la Merc&egrave;.'

# Cada parada: (hora, qué, categoría, precio, ¿gratis?). Copiado de las capturas.
DIAS = [
  dict(clave='23', dia='Mi&eacute;rcoles 23', total='55 &euro;', foto='f-bcn-paseo.jpg', planes=[
    ('10:30', 'Paseo por el Barri G&ograve;tic y El Born', 'Tour guiado', 'gratis', True),
    ('13:30', 'Almuerzo en El Xampanyet', 'Comida', '25 &euro;', False),
    ('18:30', 'Preg&oacute;n de la Merc&egrave; en el Sal&oacute; de Cent', 'Visita', 'gratis', True),
    ('20:30', 'Cena en Bar del Pla', 'Comida', '30 &euro;', False)]),

  dict(clave='24', dia='Jueves 24', total='55 &euro;', foto='f-merce-castell.jpg', planes=[
    ('13:00', 'Diada castellera en la Pla&ccedil;a de Sant Jaume', 'Visita', 'gratis', True),
    ('13:30', 'Almuerzo en Can Culleretes', 'Comida', '30 &euro;', False),
    ('18:00', 'Cabalgata: de Pla&ccedil;a Catalunya a Sant Jaume', 'Visita', 'gratis', True),
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
    ('20:30', 'Correfoc en el Passeig de Gr&agrave;cia', 'Visita', 'gratis', True),
    ('21:00', 'Cena en Bar Ca&ntilde;ete', 'Comida', '40 &euro;', False)]),

  dict(clave='27', dia='Domingo 27', total='15 &euro;', foto='f-merce-espurnes.jpg', planes=[
    ('10:00', 'Puertas abiertas en el Palau de la Generalitat', 'Visita', 'gratis', True),
    ('12:00', 'La Rambla y el Mercado de la Boqueria', 'Visita', 'gratis', True),
    ('14:00', 'Almuerzo de despedida en Can Paixano', 'Comida', '15 &euro;', False),
    ('22:00', 'Piromusical en la playa de la Nova Ic&agrave;ria', 'Visita', 'gratis', True)]),
]

# (día, lo que escribió la app, lo que se publica, de dónde sale). Se imprime al generar:
# una corrección que no se ve cada vez que corres el generador es una corrección que se
# olvida, y ésta hay que llevarla a la issue de la app.
CORREGIDAS = [
  ('Mié 23', '16:00 · Pregón y paseacalles inaugural de La Mercè',
             '18:30 · Pregón de la Mercè en el Saló de Cent',
             'betevé, programa de la Mercè 2026: «de 18.30 a 20 h», Saló de Cent'),
  ('Jue 24', '10:00 · Diada de la Mercè: Castellers en Plaça de Sant Jaume',
             '13:00 · Diada castellera en la Plaça de Sant Jaume',
             'betevé: «13 h», pl. Sant Jaume; el Ajuntament corta los accesos de 11.30 a 14.30-15 h'),
  ('Jue 24', '16:00 · Cabalgata de la Mercè por el Passeig de Gràcia',
             '18:00 · Cabalgata: de Plaça Catalunya a Sant Jaume',
             'betevé: «18 h plaça Catalunya, 19 h pl. Sant Jaume». No pasa por el Passeig de Gràcia'),
  ('Sáb 26', '18:00 · Correfoc de La Mercè en Via Laietana',
             '20:30 · Correfoc en el Passeig de Gràcia',
             'barcelona.cat/Cultura Popular: passeig de Gràcia desde 2022, Provença → Consell '
             'de Cent; las 18 h son el Correfoc dels Petits'),
  ('Dom 27', '19:00 · Piromusical de La Mercè en Montjuïc',
             '22:00 · Piromusical en la playa de la Nova Icària',
             'ajuntament.barcelona.cat y betevé: 22 h, se dispara desde el espigó del Bogatell; '
             'se ha movido al litoral por las obras de la Fira'),
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

# LOS DOS CAMBIOS DE SITIO DE ESTE AÑO. No es relleno: es lo que la gente busca el fin de
# semana y lo único de esta pieza que alguien reenvía por WhatsApp. Y es exactamente lo que
# la app puso mal, así que aquí se dice bien y con el sitio delante.
AVISOS = [
  ('Correfoc', 'S&aacute;bado 26, 20:30',
   'Ya no pasa por Via Laietana: sale del <b>passeig de Gr&agrave;cia</b> y baja de Proven&ccedil;a a '
   'Consell de Cent. A las 18 h es el infantil, en sentido contrario.'),
  ('Piromusical', 'Domingo 27, 22:00',
   'Ya no es en Montju&iuml;c: se dispara desde el espig&oacute;n del Bogatell y se ve desde la '
   '<b>platja de la Nova Ic&agrave;ria</b>. Se ha movido por las obras de la Fira.'),
]

def aviso(titulo, cuando, texto, y):
    return (f'<div style="position: absolute; left: 84px; top: {y}px; width: 912px">'
            f'<span class="sans" style="display: block; font-size: 28px; letter-spacing: 0.16em; '
            f'text-transform: uppercase; color: {MENTA}; font-weight: 700">{titulo} &middot; {cuando}</span>'
            f'<span class="sans" style="display: block; margin-top: 14px; font-size: 36px; line-height: 1.36; '
            f'font-weight: 500; color: rgba(255, 253, 249, 0.92); text-wrap: pretty; {SOMBRA}">{texto}</span>'
            f'</div>')

def hay(f, carpeta='fotos'):
    return os.path.exists(f'{carpeta}/{f}' if carpeta else f)

if not DIAS or any(not d['planes'] for d in DIAS):
    sys.exit('FALTA EL PLAN. Se lee de las capturas de la app, fila a fila. No se inventa ni\n'
             'una línea: un plan inventado es la promesa que la app no cumple.')
if not hay(CAPTURA, ''):
    sys.exit(f'FALTA LA CAPTURA {CAPTURA} en banco/capturas/')

T = {}
DIAS_QUE_VAN = DIAS[2:] if FINDE else DIAS
_n = len(DIAS_QUE_VAN)
_planes = sum(len(d['planes']) for d in DIAS_QUE_VAN)
_euros = sum(int(p.split('&')[0]) for d in DIAS_QUE_VAN for _, _, _, p, _ in d['planes'] if p != 'gratis')
_gratis = sum(1 for d in DIAS_QUE_VAN for p in d['planes'] if p[4])

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
print(f'\nOJO: {len(CORREGIDAS)} filas NO salen como las escribió la app. Los cinco actos de '
      'la fiesta\nque trae el plan llevaban la hora mal, y tres el sitio:')
for dia, app, va, fuente in CORREGIDAS:
    print(f'  {dia}\n    la app: {app}\n    se publica: {va}\n    {fuente}')
print('\nY con las horas buenas el jueves y el sábado dejan de cuadrar (13:00 castells / 13:30\n'
      'almuerzo; 20:30 correfoc / 21:00 cena). Esos dos días hay que volver a generarlos en la\n'
      'app y traer capturas nuevas antes de publicar.')
