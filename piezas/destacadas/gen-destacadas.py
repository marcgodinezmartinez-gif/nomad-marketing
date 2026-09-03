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
#
# Bilingüe desde la misma tarde (1-sep): `python3 gen-destacadas.py` escribe la versión
# en español y `python3 gen-destacadas.py it` la italiana, con las capturas `*-900-it`.
# El dueño calcula que la mitad de los seguidores son italianos, y la base de datos dice
# que NINGUNO se ha apuntado (las 8 altas llevan `lang = es`; la historia italiana del
# 31-ago no dejó ni una fila). Las destacadas en italiano son la forma más barata de
# saber si el idioma era la barrera o si son seguidores de cortesía: si aparecen altas
# con `lang = it`, era el idioma. Los textos van en una tabla por idioma y el resto del
# fichero no sabe en cuál está.
import sys
IDIOMA = sys.argv[1] if len(sys.argv) > 1 else 'es'
assert IDIOMA in ('es', 'it'), IDIOMA
SUFIJO = '' if IDIOMA == 'es' else f'-{IDIOMA}'          # qe-1 / qe-it-1
CAPTURA = '' if IDIOMA == 'es' else f'-{IDIOMA}'         # plan-900.webp / plan-900-it.webp
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

# Los textos. Cada entrada es (kicker, titular, sub) o lo que necesite la tarjeta; las
# etiquetas de tamaño viven abajo, con la tarjeta, porque dependen de cuántas letras
# tiene cada idioma y no del idioma en sí.
T = {
  'es': {
    'qe-1': ('Llega en octubre', '&iquest;Qu&eacute; es<br>NOMAD?',
             'Una app que te escribe el viaje entero<br>y te lo cuenta al o&iacute;do mientras lo andas.'),
    'qe-2': ('1 &middot; El plan', 'Dices d&oacute;nde y cu&aacute;ndo.<br>Te escribe los d&iacute;as.'),
    'qe-3': ('2 &middot; El tour a pie', 'Te lleva de parada en parada.'),
    'qe-4': ('3 &middot; El museo', 'Enfocas una obra<br>y te cuenta su historia.'),
    'qe-5': ('4 &middot; El grupo', 'Tus amigos entran con un QR.<br>Los gastos se reparten solos.'),
    'qe-6': ('Y cu&aacute;nto cuesta', 'El viaje entero,<br>2,99&nbsp;&euro;.',
             'Sin suscripci&oacute;n. Se paga por viaje,<br>y s&oacute;lo si lo generas.'),
    'qe-7': ('Todav&iacute;a no est&aacute; publicada', 'Llega en octubre.',
             'La lista de espera ya est&aacute; abierta,<br>y el primer viaje sale por 1,99&nbsp;&euro;.',
             'Toca el enlace 👇'),
    'li-1': ('Antes del lanzamiento', 'La lista<br>de espera.',
             'Qu&eacute; es, qu&eacute; te llevas<br>y c&oacute;mo se entra. 👉'),
    'li-2': ('Lo que te llevas', 'Tu primer viaje,<br>por 1,99&nbsp;&euro;.',
             'En vez de 2,99&nbsp;&euro;. S&oacute;lo para quien<br>est&eacute; en la lista el d&iacute;a que abramos.'),
    'li-3': ('C&oacute;mo se entra', 'Tres pasos<br>y treinta segundos.',
             'Toca el enlace de la bio<br>(o el de esta historia).', 'Escribe tu correo.',
             'Ya est&aacute;. Te avisamos el d&iacute;a<br>del lanzamiento.'),
    'li-4': ('Sin letra peque&ntilde;a', 'Un correo. Uno.',
             'El d&iacute;a que abramos. Ni promociones,<br>ni recordatorios, ni nada m&aacute;s.<br><br>Y te borras cuando quieras.'),
  },
  'it': {
    'qe-1': ('Arriva a ottobre', 'Cos&rsquo;&egrave;<br>NOMAD?',
             'Un&rsquo;app che ti scrive il viaggio intero<br>e te lo racconta all&rsquo;orecchio mentre cammini.'),
    'qe-2': ('1 &middot; Il piano', 'Dici dove e quando.<br>Ti scrive le giornate.'),
    'qe-3': ('2 &middot; Il tour a piedi', 'Ti porta di tappa in tappa.'),
    'qe-4': ('3 &middot; Il museo', 'Inquadri un&rsquo;opera<br>e ti racconta la sua storia.'),
    'qe-5': ('4 &middot; Il gruppo', 'I tuoi amici entrano con un QR.<br>Le spese si dividono da sole.'),
    'qe-6': ('E quanto costa', 'Il viaggio intero,<br>2,99&nbsp;&euro;.',
             'Senza abbonamento. Si paga a viaggio,<br>e solo se lo generi.'),
    'qe-7': ('Non &egrave; ancora online', 'Arriva a ottobre.',
             'La lista d&rsquo;attesa &egrave; gi&agrave; aperta,<br>e il primo viaggio costa 1,99&nbsp;&euro;.',
             'Tocca il link 👇'),
    'li-1': ('Prima del lancio', 'La lista<br>d&rsquo;attesa.',
             'Cos&rsquo;&egrave;, cosa ti porti a casa<br>e come si entra. 👉'),
    'li-2': ('Cosa ti porti a casa', 'Il primo viaggio,<br>a 1,99&nbsp;&euro;.',
             'Invece di 2,99&nbsp;&euro;. Solo per chi &egrave;<br>in lista il giorno in cui apriamo.'),
    'li-3': ('Come si entra', 'Tre passi<br>e trenta secondi.',
             'Tocca il link in bio<br>(o quello di questa storia).', 'Scrivi la tua email.',
             'Fatto. Ti avvisiamo il giorno<br>del lancio.'),
    'li-4': ('Niente asterischi', 'Una mail. Una sola.',
             'Il giorno in cui apriamo. Niente promozioni,<br>niente promemoria, niente altro.<br><br>E ti cancelli quando vuoi.'),
  },
}[IDIOMA]

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
  + kicker(T['qe-1'][0])
  + titular(T['qe-1'][1], 420, 108)
  + sub(T['qe-1'][2], 800, 44)
  + marca()
  + '</div>')

TARJETAS['qe-2'] = (RAIZ
  + foto('f-plan.jpg', 1.04)
  + velo(VELO_TELEFONO)
  + kicker(T['qe-2'][0])
  + titular(T['qe-2'][1], 380, 64, 900)
  + telefono(f'plan-900{CAPTURA}.webp')
  + '</div>')

TARJETAS['qe-3'] = (RAIZ
  + foto('f-tour.jpg', 1.04)
  + velo(VELO_TELEFONO)
  + kicker(T['qe-3'][0])
  + titular(T['qe-3'][1], 380, 64, 900)
  + telefono(f'tour-900{CAPTURA}.webp')
  + '</div>')

TARJETAS['qe-4'] = (RAIZ
  + foto('f-museo.jpg', 1.04)
  + velo(VELO_TELEFONO)
  + kicker(T['qe-4'][0])
  + titular(T['qe-4'][1], 380, 64, 900)
  + telefono(f'museo-900{CAPTURA}.webp')
  + '</div>')

TARJETAS['qe-5'] = (RAIZ
  + foto('f-grupo.jpg', 1.04)
  + velo(VELO_TELEFONO)
  + kicker(T['qe-5'][0])
  + titular(T['qe-5'][1], 380, 58, 960)
  + telefono(f'grupo-900{CAPTURA}.webp')
  + '</div>')

TARJETAS['qe-6'] = (RAIZ
  + foto('f-precio.jpg', 1.06)
  + velo('linear-gradient(180deg, rgba(16, 14, 11, 0.5) 0%, rgba(16, 14, 11, 0.32) 32%, rgba(16, 14, 11, 0.9) 100%)')
  + scrim(240, 1000)
  + kicker(T['qe-6'][0])
  + titular(T['qe-6'][1], 420, 100)
  + sub(T['qe-6'][2], 830, 44)
  + marca()
  + '</div>')

TARJETAS['qe-7'] = (RAIZ
  + foto('f-oferta.jpg', 1.04)
  + velo('linear-gradient(180deg, rgba(16, 14, 11, 0.55) 0%, rgba(16, 14, 11, 0.35) 30%, rgba(16, 14, 11, 0.9) 100%)')
  + kicker(T['qe-7'][0])
  + titular(T['qe-7'][1], 420, 96)
  + sub(T['qe-7'][2], 620, 44)
  + sub(T['qe-7'][3], 1420, 40, MENTA, peso=700)
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
  + kicker(T['li-1'][0])
  + titular(T['li-1'][1], 420, 108)
  + sub(T['li-1'][2], 800, 44)
  + marca()
  + '</div>')

TARJETAS['li-2'] = (RAIZ
  + foto('f-alhambra.jpg', 1.06)
  + velo('linear-gradient(180deg, rgba(16, 14, 11, 0.5) 0%, rgba(16, 14, 11, 0.3) 30%, rgba(16, 14, 11, 0.9) 100%)')
  + scrim(240, 1020)
  + kicker(T['li-2'][0])
  + titular(T['li-2'][1], 420, 100)
  + sub(T['li-2'][2], 800, 42)
  + marca()
  + '</div>')

TARJETAS['li-3'] = (RAIZ
  + velo('linear-gradient(160deg, #16130F 0%, #100E0B 55%, #1B2620 100%)')
  + kicker(T['li-3'][0])
  + titular(T['li-3'][1], 380, 76)
  + paso('1', T['li-3'][2], 700)
  + paso('2', T['li-3'][3], 940)
  + paso('3', T['li-3'][4], 1090)
  + marca(1420)
  + '</div>')

TARJETAS['li-4'] = (RAIZ
  + velo('linear-gradient(160deg, #1B2620 0%, #100E0B 55%, #16130F 100%)')
  + kicker(T['li-4'][0])
  + titular(T['li-4'][1], 420, 96)
  + sub(T['li-4'][2], 640, 44)
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

if IDIOMA == 'es':
    TARJETAS['car-quees'] = caratula('#100E0B')
    TARJETAS['car-lista'] = caratula('#0F766E')

for nombre, cuerpo in TARJETAS.items():
    # qe-1 → qe-1.dc.html en español, qe-it-1.dc.html en italiano; las carátulas no
    # tienen idioma y sólo se escriben con el español.
    fichero = nombre if nombre.startswith('car-') else nombre.replace('-', f'{SUFIJO}-', 1)
    open(f'{fichero}.dc.html', 'w').write(pagina(cuerpo))
print('escritas', len(TARJETAS), 'tarjetas', IDIOMA)
