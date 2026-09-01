# El SEGUNDO Reel de la cuenta (1-sep): el del grupo.
#
# Por qué éste y no otro: el primer Reel («le pedí a una IA que me organizara 3 días en
# Roma») cuenta el producto entero, y repetir eso con otras fotos no enseña nada nuevo a
# quien ya lo vio. El ángulo del grupo es el único de los cuatro de la campaña que
# ningún competidor puede copiar —ellos escriben itinerarios, no reparten cuentas— y en
# vídeo no estaba contado. El gancho no habla de la app: habla de una persona que el
# espectador reconoce en dos segundos, que es lo que para el dedo.
#
# Mismas reglas que `gen-reel.py`, y no se repiten aquí: zona segura entre y=230 e
# y=1480, sin pista de audio a propósito (se elige dentro de Instagram, de tendencias),
# y las dos trampas de ffmpeg viven en `montar-reel.sh`.
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

def scrim(desde=240, hasta=1100):
    return (f'<div style="position: absolute; left: 0; right: 0; top: {desde}px; height: {hasta - desde}px; '
            'background: linear-gradient(180deg, rgba(16, 14, 11, 0) 0%, rgba(16, 14, 11, 0.72) 18%, '
            'rgba(16, 14, 11, 0.72) 78%, rgba(16, 14, 11, 0) 100%)"></div>')

def telefono(png, ancho=560, arriba=560):
    return (f'''<div style="position: absolute; left: 50%; top: {arriba}px; transform: translateX(-50%);
      width: {ancho}px; aspect-ratio: 9 / 19.5; background: #0b0b0d; border-radius: 76px; padding: 16px;
      box-shadow: 0 50px 120px rgba(0, 0, 0, 0.6)">
    <div style="position: absolute; inset: 0; border-radius: 76px; border: 5px solid #98979c"></div>
    <div style="position: absolute; top: 32px; left: 50%; transform: translateX(-50%); width: 168px; height: 46px;
      background: #0b0b0d; border-radius: 26px; z-index: 2"></div>
    <div style="width: 100%; height: 100%; border-radius: 60px; background: #F5F0E8; overflow: hidden">
      <img src="{png}" alt="" style="width: 100%; display: block">
    </div>
  </div>''')

def kicker(t, y=250):
    return (f'<p class="sans" style="position: absolute; left: 84px; top: {y}px; margin: 0; font-size: 32px; '
            f'letter-spacing: 0.18em; text-transform: uppercase; color: rgba(255, 253, 249, 0.82); '
            f'font-weight: 600; {SOMBRA}">{t}</p>')

def titular(t, y, size=78, ancho=912):
    return (f'<h1 class="serif" style="position: absolute; left: 84px; top: {y}px; margin: 0; width: {ancho}px; '
            f'font-size: {size}px; line-height: 1.1; letter-spacing: -0.015em; {SOMBRA}">{t}</h1>')

def sub(t, y, size=38, color='rgba(255, 253, 249, 0.9)'):
    return (f'<p class="sans" style="position: absolute; left: 84px; top: {y}px; margin: 0; width: 912px; '
            f'font-size: {size}px; line-height: 1.35; color: {color}; font-weight: 500; {SOMBRA}">{t}</p>')

def marca(y=1440):
    return (f'<div style="position: absolute; left: 84px; top: {y}px; display: flex; align-items: center; gap: 20px">'
            f'<img src="mark.png" style="width: 58px; height: 58px">'
            f'<span class="sans" style="font-size: 32px; color: rgba(255, 253, 249, 0.85); font-weight: 600; '
            f'letter-spacing: 0.02em; {SOMBRA}">travelsnomad.com</span></div>')

ESCENAS = {}

# 1 · EL GANCHO. No dice qué es la app. Describe a una persona, y el que la reconoce
#     —o se reconoce— ya no se va.
ESCENAS['reelg-01'] = (RAIZ
  + foto('f-grupo.jpg', 1.06)
  + velo('linear-gradient(180deg, rgba(16, 14, 11, 0.5) 0%, rgba(16, 14, 11, 0.28) 40%, rgba(16, 14, 11, 0.82) 100%)')
  + scrim(300, 1120)
  + titular('En todo grupo hay<br>uno que acaba<br>organiz&aacute;ndolo todo.', 400, 88)
  + sub('Si eres t&uacute;, esto es para ti. 👇', 940, 44)
  + marca()
  + '</div>')

# 2 · EL VIAJE ESCRITO.
ESCENAS['reelg-02'] = (RAIZ
  + foto('f-plan.jpg', 1.04)
  + velo('linear-gradient(180deg, rgba(16, 14, 11, 0.8) 0%, rgba(16, 14, 11, 0.44) 34%, rgba(16, 14, 11, 0.5) 100%)')
  + kicker('Uno')
  + titular('Dices d&oacute;nde y cu&aacute;ndo.<br>Los d&iacute;as se escriben solos.', 320, 60, 940)
  + telefono('plan-900.webp', 600, 560)
  + '</div>')

# 3 · EL QR. La tarjeta flota sobre la foto: es un objeto, no una captura de pantalla.
ESCENAS['reelg-03'] = (RAIZ
  + foto('f-tour.jpg', 1.04)
  + velo('linear-gradient(180deg, rgba(16, 14, 11, 0.82) 0%, rgba(16, 14, 11, 0.5) 34%, rgba(16, 14, 11, 0.6) 100%)')
  + kicker('Dos')
  + titular('Tus amigos entran<br>escaneando un c&oacute;digo.', 320, 60, 940)
  + '<img src="tarjeta-qr-ejemplo.png" style="position: absolute; left: 50%; top: 620px; '
    'transform: translateX(-50%) rotate(-3deg); width: 620px; border-radius: 32px; '
    'box-shadow: 0 50px 110px rgba(0, 0, 0, 0.65)">'
  + '</div>')

# 4 · LOS GASTOS. El argumento entero está en la captura: el saldo, ya calculado.
ESCENAS['reelg-04'] = (RAIZ
  + foto('f-portada.jpg', 1.04)
  + velo('linear-gradient(180deg, rgba(16, 14, 11, 0.82) 0%, rgba(16, 14, 11, 0.46) 34%, rgba(16, 14, 11, 0.55) 100%)')
  + kicker('Tres')
  + titular('Y los gastos<br>se reparten solos.', 320, 62, 900)
  + telefono('grupo-900.webp', 600, 560)
  + '</div>')

# 5 · EL PRECIO Y LA LISTA. Una sola instrucción, como en el primer Reel.
ESCENAS['reelg-05'] = (RAIZ
  + foto('f-oferta.jpg', 1.06)
  + velo('linear-gradient(180deg, rgba(16, 14, 11, 0.5) 0%, rgba(16, 14, 11, 0.35) 30%, rgba(16, 14, 11, 0.9) 100%)')
  + kicker('Llega en octubre', 400)
  + titular('2,99&nbsp;&euro; el viaje.<br>Lo pagas t&uacute;, una vez.', 470, 74)
  + f'<p class="sans" style="position: absolute; left: 84px; top: 800px; margin: 0; font-size: 40px; '
    f'line-height: 1.4; color: {MENTA}; font-weight: 700; {SOMBRA}">En la lista de espera,<br>'
    f'tu primer viaje por 1,99&nbsp;&euro;.</p>'
  + sub('Ap&uacute;ntate en el enlace de la bio.', 990, 38)
  + marca()
  + '</div>')

for nombre, cuerpo in ESCENAS.items():
    open(f'{nombre}.dc.html', 'w').write(pagina(cuerpo))
print('escritas', len(ESCENAS), 'escenas')
