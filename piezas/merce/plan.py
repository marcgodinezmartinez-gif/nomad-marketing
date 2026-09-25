# EL PLAN DE LA MERCÈ Y CÓMO SE DIBUJA UNA PARADA — compartido por el carrusel
# (gen-plan-merce.py) y las historias del finde (gen-finde-historias.py).
#
# Existe desde el 25-sep por la misma razón que tarjetas.py: cuando el carrusel del finde
# se pidió también en historias, copiar DIAS a otro generador era copiar también las cinco
# filas corregidas — y una corrección que vive en dos sitios acaba arreglada en uno solo.
# Aquí hay UN plan: lo que leyó la captura, lo que se corrigió y por qué.
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tarjetas import SOMBRA, MENTA, PAPEL

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


def cuentas(dias):
    """(paradas, euros, gratis) de unos días: lo que dice la portada de cada corte."""
    planes = sum(len(d['planes']) for d in dias)
    euros = sum(int(p.split('&')[0]) for d in dias for _, _, _, p, _ in d['planes'] if p != 'gratis')
    gratis = sum(1 for d in dias for p in d['planes'] if p[4])
    return planes, euros, gratis

def avisa_correcciones():
    """Se llama al final de cada generador: una corrección que no se ve cada vez que corres
    el generador es una corrección que se olvida."""
    print(f'\nOJO: {len(CORREGIDAS)} filas NO salen como las escribió la app. Los cinco actos de '
          'la fiesta\nque trae el plan llevaban la hora mal, y tres el sitio:')
    for dia, app, va, fuente in CORREGIDAS:
        print(f'  {dia}\n    la app: {app}\n    se publica: {va}\n    {fuente}')
    print('\nY con las horas buenas el jueves y el sábado dejan de cuadrar (13:00 castells / 13:30\n'
          'almuerzo; 20:30 correfoc / 21:00 cena). Esos dos días hay que volver a generarlos en la\n'
          'app y traer capturas nuevas antes de publicar.')
