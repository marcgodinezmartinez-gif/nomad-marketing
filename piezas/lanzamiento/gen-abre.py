# «¿QUÉ PASA EL DÍA QUE ABRA NOMAD?» — carrusel de 5 tarjetas (29-sep).
#
# EL POST DE LA SEMANA DEL CIERRE. `campana/LANZAMIENTO-PUBLICIDAD.md` lo dejó escrito en
# agosto: «el lanzamiento es en octubre y la lista se cierra el día que se abre la tienda», y
# «la cuenta atrás de la última semana es la que más altas trae: una lista que se cierra es
# una razón para apuntarse hoy en vez de "ya me apuntaré"». El copy D (urgencia) se guardó
# para esta semana exacta. Octubre empieza el jueves 1.
#
# SIN FECHA, A PROPÓSITO. No hay fecha de tienda, así que nada aquí dice «quedan X días» ni
# «el día N»: una cuenta atrás con un número inventado es la promesa que no se cumple. Lo que
# sí es verdad y se dice: octubre empieza el jueves, y la lista se cierra el día que abramos.
#
# EL FORMATO, del dueño: una pregunta con NOMAD de sujeto («¿Qué planea NOMAD para la
# Mercè?» le gustó; «Queda el finde» no). Y la app en la tarjeta 2, no en la 5: la queja del
# 21-sep era justo que los carruseles la escondían al final.
#
# EL PRECIO, en el orden de la casa (AGENTS.md): primero «desde 2,99 € el viaje entero» con la
# tabla por días, después el 1,99 € de la lista. Nunca «2,99 €» a secas, y sin el café en la
# tarjeta de la tabla: con un 6,99 € debajo, «lo que cuesta un café» no se sostiene.
#
# Uso, desde salida/:  python3 ../piezas/lanzamiento/gen-abre.py
#                      node ../piezas/roma/exportar-plan.mjs abre 5
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tarjetas import (SOMBRA, MENTA, PAPEL, NOCHE, VELO_FOTO, VELO_TELEFONO,
                      pagina as _pagina, raiz, foto, velo, kicker, titular, sub, marca, telefono)

HELMET = open('Main.dc.html').read().split('<helmet>')[1].split('</helmet>')[0]
pagina = lambda cuerpo: _pagina(cuerpo, HELMET)

CAPTURA = 'tourdebod-900.webp'   # el tour a pie con el mapa y la ruta: el foso, a la vista

# La tabla de la web, tal cual (AGENTS.md: «2,99 € hasta 3 días, 4,99 € de 4 a 7 y 6,99 € de
# 8 a 30, como dice la web»).
TARIFAS = [('Hasta 3 d&iacute;as', '2,99&nbsp;&euro;'),
           ('De 4 a 7 d&iacute;as', '4,99&nbsp;&euro;'),
           ('De 8 a 30 d&iacute;as', '6,99&nbsp;&euro;')]

# Un velo más cerrado para las tarjetas de texto largo: la foto se ve, pero no compite.
VELO_TEXTO = ('linear-gradient(180deg, rgba(16, 14, 11, 0.78) 0%, rgba(16, 14, 11, 0.56) 40%, '
              'rgba(16, 14, 11, 0.88) 100%)')

def tarifa(dias, precio, y):
    """Una fila de la tabla: los días a la izquierda, el precio en serif a la derecha."""
    return (f'<div style="position: absolute; left: 84px; top: {y}px; width: 912px; display: flex; '
            f'align-items: baseline; justify-content: space-between; padding-bottom: 22px; '
            f'border-bottom: 1px solid rgba(255, 253, 249, 0.2)">'
            f'<span class="sans" style="font-size: 38px; font-weight: 600; {SOMBRA}">{dias}</span>'
            f'<span class="serif" style="font-size: 64px; line-height: 1; color: {MENTA}; {SOMBRA}">{precio}</span>'
            f'</div>')

for f in ('fotos/f-porto.jpg', 'fotos/f-santiago.jpg', 'fotos/f-precio.jpg', 'fotos/f-oia.jpg',
          'fotos/f-segovia.jpg', CAPTURA):
    if not os.path.exists(f):
        sys.exit(f'FALTA {f}. ¿Has pasado piezas/preparar.sh?')

T = {}

# 1 · LA PREGUNTA. Y el único dato con fecha que es verdad.
T['abre-1'] = (raiz(NOCHE)
  + foto('f-porto.jpg', 1.06) + velo(VELO_FOTO)
  + kicker('Lista de espera')
  + titular('&iquest;Qu&eacute; pasa el d&iacute;a<br>que abra NOMAD?', 180, 96)
  + sub('Octubre empieza el jueves.', 430, 42)
  + marca()
  + '</div>')

# 2 · LO QUE VA DENTRO. La app, en la segunda: el tour a pie con su mapa, que es lo que
# ningún planificador hace (campana/MERCADO: «el foso es cruzar la puerta»).
T['abre-2'] = (raiz(NOCHE)
  + foto('f-santiago.jpg', 1.06) + velo(VELO_TELEFONO)
  + kicker('Lo que va dentro')
  + titular('Te escribe los d&iacute;as.<br>Te los cuenta al o&iacute;do.', 170, 80)
  + sub('El plan con horas y precios, los tours a pie narrados, las gu&iacute;as de museo y los '
        'gastos del grupo. Todo en el mismo viaje.', 370, 34, ancho=880)
  + telefono(CAPTURA, 430, 560)
  + '</div>')

# 3 · LO QUE CUESTA CUANDO ABRA. Primero el precio normal, siempre.
T['abre-3'] = (raiz(NOCHE)
  + foto('f-precio.jpg', 1.06) + velo(VELO_TEXTO)
  + kicker('Cuando abra')
  + titular('Cada viaje,<br>desde 2,99&nbsp;&euro;.', 180, 96)
  + ''.join(tarifa(d, p, 500 + i * 118) for i, (d, p) in enumerate(TARIFAS))
  + sub('El viaje entero, sin suscripci&oacute;n: se paga por viaje y dentro va todo.', 900, 36,
        'rgba(255, 253, 249, 0.84)', ancho=880)
  + marca()
  + '</div>')

# 4 · Y SI ESTÁS EN LA LISTA.
T['abre-4'] = (raiz(NOCHE)
  + foto('f-oia.jpg', 1.06) + velo(VELO_TEXTO)
  + kicker('Si est&aacute;s en la lista')
  + titular(f'Tu primer viaje,<br><span style="color: {MENTA}">1,99&nbsp;&euro;</span>.', 180, 104)
  + sub('Dure lo que dure: un finde o un mes, hasta 30 d&iacute;as. Es el precio de quien se '
        'apunta antes de que abramos.', 450, 40, ancho=880)
  + marca()
  + '</div>')

# 5 · LA RESPUESTA, y lo que hay que hacer con ella.
T['abre-5'] = (raiz(NOCHE)
  + foto('f-segovia.jpg', 1.04)
  + velo('linear-gradient(180deg, rgba(16, 14, 11, 0.74) 0%, rgba(16, 14, 11, 0.44) 40%, '
         'rgba(16, 14, 11, 0.9) 100%)')
  + kicker('El d&iacute;a que abramos')
  + titular('La lista<br>se cierra.', 180, 110)
  + sub('Quien est&eacute; dentro guarda su primer viaje a 1,99&nbsp;&euro;. Quien llegue despu&eacute;s, '
        'paga lo que cuesta.', 450, 40, ancho=880)
  + (f'<div style="position: absolute; left: 84px; top: 640px; padding: 22px 34px; border-radius: 999px; '
     f'background: {MENTA}; color: #10231D">'
     f'<span class="sans" style="font-size: 34px; font-weight: 700">Ap&uacute;ntate: el enlace, en la bio</span></div>')
  + marca()
  + '</div>')

for stem, html in T.items():
    open(f'{stem}.dc.html', 'w').write(pagina(html))
print(f'{len(T)} tarjetas: ' + ', '.join(T))
