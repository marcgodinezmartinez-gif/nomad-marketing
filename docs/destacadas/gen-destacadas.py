# Las DESTACADAS de Instagram (1-sep): dos historias permanentes que viven bajo la bio y
# le explican la app a quien acaba de llegar al perfil.
#
# El porqué, medido y no supuesto: el grid explica la app a quien ya está mirando el
# perfil, pero un post envejece y baja; una destacada no. Es la ÚNICA superficie de
# Instagram pensada para «acabo de llegar aquí, ¿qué es esto?», y la cuenta no tenía
# ninguna. Las 11 tarjetas se suben primero como historias del día — así que además son
# el contenido de hoy — y al terminar se guardan cada una en su destacada.
#
# Zona segura de historias: la interfaz tapa ~250px arriba y ~250px abajo. Todo el texto
# vive entre y=280 e y=1500, y de y=1520 abajo se deja LIBRE a propósito: ahí va el
# adhesivo de enlace, que es lo único que convierte dentro de una historia.
#
# Mismo HELMET, mismas fotos CC0 y mismas capturas reales que los reels y el grid: si
# alguien salta del anuncio al perfil, tiene que ser el mismo sitio.
HELMET = open('Main.dc.html').read().split('<helmet>')[1].split('</helmet>')[0]

W, H = 1080, 1920
SOMBRA = 'text-shadow: 0 4px 34px rgba(0, 0, 0, 0.55)'
MENTA = '#5CC0A6'

def pagina(cuerpo):
    return ('<!doctype html>\n<html>\n<head>\n  <meta charset="utf-8">\n'
            '  <script src="./support.js"></script>\n  <style>body { margin: 0 }</style>\n</head>\n<body>\n<x-dc>\n'
            '<helmet>' + HELMET + '</helmet>\n' + cuerpo + '\n</x-dc>\n</body>\n</html>\n')

RAIZ = (f'<div style="width: {W}px; height: {H}px; box-sizing: border-box; position: relative; '
        'overflow: hidden; background: #100E0B; color: #FFFDF9">')

def foto(src, escala=1.0):
    return (f'<img src="fotos/{src}" alt="" style="position: absolute; inset: 0; width: 100%; height: 100%; '
            f'object-fit: cover; transform: scale({escala}); display: block">')

def velo(g):
    return f'<div style="position: absolute; inset: 0; background: {g}"></div>'

def telefono(png, ancho=480, arriba=680):
    return (f'''<div style="position: absolute; left: 50%; top: {arriba}px; transform: translateX(-50%);
      width: {ancho}px; aspect-ratio: 9 / 19.5; background: #0b0b0d; border-radius: 66px; padding: 14px;
      box-shadow: 0 50px 120px rgba(0, 0, 0, 0.6)">
    <div style="position: absolute; inset: 0; border-radius: 66px; border: 5px solid #98979c"></div>
    <div style="position: absolute; top: 28px; left: 50%; transform: translateX(-50%); width: 144px; height: 40px;
      background: #0b0b0d; border-radius: 22px; z-index: 2"></div>
    <div style="width: 100%; height: 100%; border-radius: 52px; background: #F5F0E8; overflow: hidden">
      <img src="{png}" alt="" style="width: 100%; display: block">
    </div>
  </div>''')

def kicker(t, y=300, color=None):
    c = color or 'rgba(255, 253, 249, 0.82)'
    return (f'<p class="sans" style="position: absolute; left: 84px; top: {y}px; margin: 0; font-size: 32px; '
            f'letter-spacing: 0.18em; text-transform: uppercase; color: {c}; '
            f'font-weight: 600; {SOMBRA}">{t}</p>')

def titular(t, y, size=82, ancho=912):
    return (f'<h1 class="serif" style="position: absolute; left: 84px; top: {y}px; margin: 0; width: {ancho}px; '
            f'font-size: {size}px; line-height: 1.08; letter-spacing: -0.015em; {SOMBRA}">{t}</h1>')

def sub(t, y, size=40, color='rgba(255, 253, 249, 0.9)', ancho=912, peso=500):
    return (f'<p class="sans" style="position: absolute; left: 84px; top: {y}px; margin: 0; width: {ancho}px; '
            f'font-size: {size}px; line-height: 1.35; color: {color}; font-weight: {peso}; {SOMBRA}">{t}</p>')

def marca(y=1400):
    return (f'<div style="position: absolute; left: 84px; top: {y}px; display: flex; align-items: center; gap: 20px">'
            f'<img src="mark.png" style="width: 54px; height: 54px">'
            f'<span class="sans" style="font-size: 30px; color: rgba(255, 253, 249, 0.85); font-weight: 600; '
            f'letter-spacing: 0.02em; {SOMBRA}">travelsnomad.com</span></div>')

def paso(n, t, y):
    """Un paso numerado. El número en menta y grande: es lo que se lee de un vistazo."""
    return (f'<div style="position: absolute; left: 84px; top: {y}px; width: 912px; display: flex; '
            f'align-items: baseline; gap: 28px">'
            f'<span class="serif" style="font-size: 76px; line-height: 1; color: {MENTA}; {SOMBRA}">{n}</span>'
            f'<span class="sans" style="font-size: 42px; line-height: 1.3; font-weight: 600; {SOMBRA}">{t}</span>'
            f'</div>')

VELO_TEXTO = ('linear-gradient(180deg, rgba(16, 14, 11, 0.62) 0%, rgba(16, 14, 11, 0.3) 45%, '
              'rgba(16, 14, 11, 0.85) 100%)')
# Una banda oscura DETRÁS del bloque de texto, no un velo global: subir el velo entero
# para que se lea el titular apaga la foto y la deja marrón. Esto salió de dos tarjetas
# que se exportaron ilegibles — el neón de Montmartre y la piedra de la Alhambra — con
# el velo de arriba puesto y aun así el titular perdido dentro de la imagen.
def scrim(desde=240, hasta=1140):
    return (f'<div style="position: absolute; left: 0; right: 0; top: {desde}px; height: {hasta - desde}px; '
            'background: linear-gradient(180deg, rgba(16, 14, 11, 0) 0%, rgba(16, 14, 11, 0.72) 18%, '
            'rgba(16, 14, 11, 0.72) 78%, rgba(16, 14, 11, 0) 100%)"></div>')
VELO_TELEFONO = ('linear-gradient(180deg, rgba(16, 14, 11, 0.82) 0%, rgba(16, 14, 11, 0.46) 36%, '
                 'rgba(16, 14, 11, 0.55) 100%)')

TARJETAS = {}

# ─────────────────────────────────────────────────────────────────────────────
# DESTACADA 1 · «Qué es» — siete tarjetas. Una función por tarjeta, en el orden en
# que alguien las descubriría usando la app: primero el plan, luego la calle, luego
# el museo, luego el grupo. El precio va el penúltimo, a propósito: se dice DESPUÉS
# de que valga la pena, no antes.
# ─────────────────────────────────────────────────────────────────────────────

TARJETAS['qe-1'] = (RAIZ
  + foto('f-portada.jpg', 1.04)
  + velo(VELO_TEXTO)
  + scrim(240, 1000)
  + kicker('Llega en octubre')
  + titular('&iquest;Qu&eacute; es<br>NOMAD?', 420, 108)
  + sub('Una app que te escribe el viaje entero<br>y te lo cuenta al o&iacute;do mientras lo andas.', 800, 44)
  + marca()
  + '</div>')

TARJETAS['qe-2'] = (RAIZ
  + foto('f-plan.jpg', 1.04)
  + velo(VELO_TELEFONO)
  + kicker('1 &middot; El plan')
  + titular('Dices d&oacute;nde y cu&aacute;ndo.<br>Te escribe los d&iacute;as.', 380, 64, 900)
  + telefono('plan-900.webp')
  + '</div>')

TARJETAS['qe-3'] = (RAIZ
  + foto('f-tour.jpg', 1.04)
  + velo(VELO_TELEFONO)
  + kicker('2 &middot; El tour a pie')
  + titular('Una voz te lleva<br>de parada en parada.', 380, 64, 900)
  + telefono('tour-900.webp')
  + '</div>')

TARJETAS['qe-4'] = (RAIZ
  + foto('f-museo.jpg', 1.04)
  + velo(VELO_TELEFONO)
  + kicker('3 &middot; El museo')
  + titular('Enfocas un cuadro<br>y te cuenta su historia.', 380, 64, 900)
  + telefono('museo-900.webp')
  + '</div>')

TARJETAS['qe-5'] = (RAIZ
  + foto('f-grupo.jpg', 1.04)
  + velo(VELO_TELEFONO)
  + kicker('4 &middot; El grupo')
  + titular('Tus amigos entran con un QR.<br>Los gastos se reparten solos.', 380, 58, 960)
  + telefono('grupo-900.webp')
  + '</div>')

TARJETAS['qe-6'] = (RAIZ
  + foto('f-precio.jpg', 1.06)
  + velo('linear-gradient(180deg, rgba(16, 14, 11, 0.5) 0%, rgba(16, 14, 11, 0.32) 32%, rgba(16, 14, 11, 0.9) 100%)')
  + scrim(240, 1000)
  + kicker('Y cu&aacute;nto cuesta')
  + titular('El viaje entero,<br>2,99&nbsp;&euro;.', 420, 104)
  + sub('Sin suscripci&oacute;n. Se paga por viaje,<br>y s&oacute;lo si lo generas.', 830, 44)
  + marca()
  + '</div>')

TARJETAS['qe-7'] = (RAIZ
  + foto('f-oferta.jpg', 1.04)
  + velo('linear-gradient(180deg, rgba(16, 14, 11, 0.55) 0%, rgba(16, 14, 11, 0.35) 30%, rgba(16, 14, 11, 0.9) 100%)')
  + kicker('Todav&iacute;a no est&aacute; publicada')
  + titular('Llega en octubre.', 420, 96)
  + sub('La lista de espera ya est&aacute; abierta,<br>y el primer viaje sale por 1,99&nbsp;&euro;.', 620, 44)
  + sub('Toca el enlace 👇', 1420, 40, MENTA, peso=700)
  + '</div>')

# ─────────────────────────────────────────────────────────────────────────────
# DESTACADA 2 · «La lista» — cuatro tarjetas. Existe porque la pregunta «¿y cómo me
# apunto?» no puede tener como respuesta «busca el enlace»: los tres pasos escritos
# son la diferencia entre entenderlo y hacerlo. La última tarjeta es manejo de
# objeciones puro — «¿me vais a llenar el correo?» — que es lo que frena a quien ya
# estaba convencido.
# ─────────────────────────────────────────────────────────────────────────────

TARJETAS['li-1'] = (RAIZ
  + foto('f-oia.jpg', 1.04)
  + velo(VELO_TEXTO)
  + kicker('Antes del lanzamiento')
  + titular('La lista<br>de espera.', 420, 108)
  + sub('Qu&eacute; es, qu&eacute; te llevas<br>y c&oacute;mo se entra. 👉', 800, 44)
  + marca()
  + '</div>')

TARJETAS['li-2'] = (RAIZ
  + foto('f-alhambra.jpg', 1.06)
  + velo('linear-gradient(180deg, rgba(16, 14, 11, 0.5) 0%, rgba(16, 14, 11, 0.3) 30%, rgba(16, 14, 11, 0.9) 100%)')
  + scrim(240, 1020)
  + kicker('Lo que te llevas')
  + titular('Tu primer viaje,<br>por 1,99&nbsp;&euro;.', 420, 100)
  + sub('En vez de 2,99&nbsp;&euro;. S&oacute;lo para quien<br>est&eacute; en la lista el d&iacute;a que abramos.', 800, 42)
  + marca()
  + '</div>')

TARJETAS['li-3'] = (RAIZ
  + velo('linear-gradient(160deg, #16130F 0%, #100E0B 55%, #1B2620 100%)')
  + kicker('C&oacute;mo se entra')
  + titular('Tres pasos<br>y treinta segundos.', 380, 76)
  + paso('1', 'Toca el enlace de la bio<br>(o el de esta historia).', 700)
  + paso('2', 'Escribe tu correo.', 940)
  + paso('3', 'Ya est&aacute;. Te avisamos el d&iacute;a<br>del lanzamiento.', 1090)
  + marca(1420)
  + '</div>')

TARJETAS['li-4'] = (RAIZ
  + velo('linear-gradient(160deg, #1B2620 0%, #100E0B 55%, #16130F 100%)')
  + kicker('Sin letra peque&ntilde;a')
  + titular('Un correo. Uno.', 420, 96)
  + sub('El d&iacute;a que abramos. Ni promociones,<br>ni recordatorios, ni nada m&aacute;s.<br><br>Y te borras cuando quieras.', 640, 44)
  + marca(1400)
  + '</div>')

# ─────────────────────────────────────────────────────────────────────────────
# Las dos CARÁTULAS. Instagram recorta un círculo del CENTRO de la imagen, así que
# el icono va en el centro exacto y no hay texto: a 60px de diámetro no se lee nada.
# ─────────────────────────────────────────────────────────────────────────────

def caratula(fondo):
    return (RAIZ
      + f'<div style="position: absolute; inset: 0; background: {fondo}"></div>'
      + '<img src="mark-claro.png" style="position: absolute; left: 50%; top: 50%; '
        'transform: translate(-50%, -50%); width: 380px; height: 380px">'
      + '</div>')

TARJETAS['car-quees'] = caratula('#100E0B')
TARJETAS['car-lista'] = caratula('#0F766E')

for nombre, cuerpo in TARJETAS.items():
    open(f'{nombre}.dc.html', 'w').write(pagina(cuerpo))
print('escritas', len(TARJETAS), 'tarjetas')
