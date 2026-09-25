# EL FINDE DE LA MERCÈ EN HISTORIAS (25-sep), 1080×1920: el carrusel del finde, pero sólo
# sábado y domingo, para subirlo a historias.
#
# Lo pidió el dueño el viernes por la noche: «el carrusel molaba para subirlo a historias,
# pero ajústalo a contar los planes de sábado y domingo solo». El viernes ya se había ido.
#
# ES EL MISMO CARRUSEL, BAJADO A LA ZONA SEGURA. Las posiciones son las del post
# (gen-plan-merce.py) desplazadas 190 px: el kicker del post en y=100-110 cae aquí en 290-300,
# justo debajo de lo que tapa la interfaz, y la marca del post en 1200 cae en 1390. De 1520
# para abajo no hay nada: es el sitio del adhesivo de enlace. Los velos, en cambio, NO se
# heredan: un degradado pensado para 1350 estirado a 1920 deja la lista del día a medio
# cerrar, así que aquí cada velo tiene las paradas donde está el texto de la historia.
#
# EL PLAN SALE DE plan.py, el mismo que el del carrusel: las cinco filas corregidas viven en
# un sitio. Las fotos, del recorte de historia (fotos-historia/), nunca del de post estirado.
#
# EL MÓVIL ENSEÑA EL VIERNES, a propósito: las capturas del sábado y el domingo llevan el
# correfoc en Via Laietana a las 18:00 y el piromusical en Montjuïc a las 19:00. Justo
# después de la historia del aviso, un móvil que dijera «Montjuïc» sería un gol en propia.
# La del viernes es la única del finde sin una hora mala, y es el mismo viaje: se ven las
# pestañas del sábado y el domingo.
#
# Uso, desde salida/:  python3 ../piezas/merce/gen-finde-historias.py
#                      node ../piezas/roma/exportar-plan.mjs mercefinde 6 1080 1920
# Adhesivo de enlace, de 1520 para abajo:
#   https://travelsnomad.com/?utm_source=instagram&utm_medium=organic&utm_campaign=merce-finde
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tarjetas import SOMBRA, MENTA, PAPEL, NOCHE, pagina as _pagina, velo, kicker, titular, sub, marca, telefono
from plan import DIAS, AVISOS, programa, aviso, cuentas, avisa_correcciones

W, H = 1080, 1920
HELMET = open('Main.dc.html').read().split('<helmet>')[1].split('</helmet>')[0]
pagina = lambda cuerpo: _pagina(cuerpo, HELMET)

CAPTURA = 'planmerce-25-900.webp'
FINDE = [d for d in DIAS if d['clave'] in ('26', '27')]
MARCA_Y = 1390      # la del post (1200) + 190; acaba en 1440, antes de la zona del adhesivo

# Los velos, con las paradas donde vive el texto de una historia (el de arriba cubre también
# los ~280 px que tapa la interfaz, que no hace falta que se vean).
VELO_FOTO = ('linear-gradient(180deg, rgba(16, 14, 11, 0.7) 0%, rgba(16, 14, 11, 0.5) 16%, '
             'rgba(16, 14, 11, 0.36) 44%, rgba(16, 14, 11, 0.62) 74%, rgba(16, 14, 11, 0.88) 100%)')
VELO_PROGRAMA = ('linear-gradient(180deg, rgba(16, 14, 11, 0.7) 0%, rgba(16, 14, 11, 0.6) 10%, '
                 'rgba(16, 14, 11, 0.34) 24%, rgba(16, 14, 11, 0.9) 46%, rgba(16, 14, 11, 0.97) 100%)')
VELO_TELEFONO = ('linear-gradient(180deg, rgba(16, 14, 11, 0.84) 0%, rgba(16, 14, 11, 0.62) 30%, '
                 'rgba(16, 14, 11, 0.55) 60%, rgba(16, 14, 11, 0.75) 100%)')
VELO_CIERRE = ('linear-gradient(180deg, rgba(16, 14, 11, 0.66) 0%, rgba(16, 14, 11, 0.5) 16%, '
               'rgba(16, 14, 11, 0.32) 40%, rgba(16, 14, 11, 0.72) 72%, rgba(16, 14, 11, 0.9) 100%)')

def raiz():
    return (f'<div style="width: {W}px; height: {H}px; box-sizing: border-box; position: relative; '
            f'overflow: hidden; background: {NOCHE}; color: {PAPEL}">')

def foto(src, escala=1.04):
    return (f'<img src="fotos-historia/{src}" alt="" style="position: absolute; inset: 0; width: 100%; '
            f'height: 100%; object-fit: cover; transform: scale({escala}); display: block">')

def hay(f):
    return os.path.exists(f)

faltan = [f'fotos-historia/{d["foto"]}' for d in FINDE if not hay(f'fotos-historia/{d["foto"]}')]
faltan += [f for f in ('fotos-historia/f-bcn-festa.jpg', 'fotos-historia/f-merce-diable.jpg',
                       'fotos-historia/f-bcn-calle.jpg', 'fotos-historia/f-bcn-cierre.jpg', CAPTURA)
           if not hay(f)]
if len(FINDE) != 2 or faltan:
    sys.exit('FALTA: ' + (', '.join(faltan) or 'el sábado o el domingo en plan.py') +
             '\n¿Has pasado piezas/preparar.sh? Copia los recortes de historia a salida/fotos-historia/.')

_planes, _euros, _gratis = cuentas(FINDE)
S = {}

# 1 · LA PORTADA. El reloj, como en el carrusel que gustó: queda el finde.
S['mercefinde-1'] = (raiz()
  + foto('f-bcn-festa.jpg', 1.04) + velo(VELO_FOTO)
  + kicker('La Merc&egrave; &middot; el finde', 300)
  + titular('Queda el finde<br>de Merc&egrave;.', 400, 92)
  + sub('Se lo pedimos a NOMAD: s&aacute;bado y domingo, hora a hora y con precios. '
        f'{_planes} planes y {_euros}&nbsp;&euro; con todas las comidas dentro; {_gratis} no cuestan nada.',
        620, 38, ancho=880)
  + marca(MARCA_Y)
  + '</div>')

# 2 · EL AVISO. Lo que se reenvía, y lo que la app puso mal.
S['mercefinde-2'] = (raiz()
  + foto('f-merce-diable.jpg', 1.04) + velo(VELO_PROGRAMA)
  + kicker('Ojo, este a&ntilde;o', 300)
  + titular('Dos cosas han<br>cambiado de sitio.', 360, 84)
  + ''.join(aviso(*a, 660 + i * 300) for i, a in enumerate(AVISOS))
  + marca(MARCA_Y)
  + '</div>')

# 3-4 · SÁBADO Y DOMINGO. La lista anclada abajo, como en el post: acaba en 1330.
for i, d in enumerate(FINDE, start=3):
    S[f'mercefinde-{i}'] = (raiz()
      + foto(d['foto'], 1.04) + velo(VELO_PROGRAMA)
      + kicker(d['dia'], 290, MENTA)
      + titular(f'{len(d["planes"])} planes &middot; {d["total"]}', 342, 76)
      + programa(d['planes'], abajo=H - 1330)
      + marca(MARCA_Y)
      + '</div>')

# 5 · CÓMO SE HIZO. Titular en un renglón para que el móvil quepa entero: acaba en 1492.
S['mercefinde-5'] = (raiz()
  + foto('f-bcn-calle.jpg', 1.04) + velo(VELO_TELEFONO)
  + kicker('C&oacute;mo se hizo', 290)
  + titular('Un minuto. Ni una reserva.', 340, 72)
  + sub('Escribes el sitio y los d&iacute;as, y la app monta cada d&iacute;a con horas y precios.',
        440, 34, ancho=880)
  + telefono(CAPTURA, 430, 560)
  + '</div>')

# 6 · EL CIERRE, el de siempre, señalando el adhesivo.
S['mercefinde-6'] = (raiz()
  + foto('f-bcn-cierre.jpg', 1.04) + velo(VELO_CIERRE)
  + kicker('Lista de espera abierta', 300)
  + titular('Llega en octubre.', 370, 96)
  + (f'<h2 class="serif" style="position: absolute; left: 84px; top: 510px; margin: 0; width: 912px; '
     f'font-size: 84px; line-height: 1.06; letter-spacing: -0.018em; font-weight: 400; {SOMBRA}">'
     f'Tu primer viaje por <span style="color: {MENTA}">1,99&nbsp;&euro;</span>*</h2>')
  + sub('*Si te apuntas a la lista de espera: en el enlace de aqu&iacute; abajo.', 640, 32,
        'rgba(255, 253, 249, 0.8)')
  + marca(MARCA_Y)
  + '</div>')

for stem, html in S.items():
    open(f'{stem}.dc.html', 'w').write(pagina(html))
print(f'{len(S)} historias: ' + ', '.join(S))
print('Se exportan con:  node ../piezas/roma/exportar-plan.mjs mercefinde 6 1080 1920')
avisa_correcciones()
