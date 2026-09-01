# El primer VÍDEO de la cuenta (31-ago): un Reel vertical 1080x1920 con las escenas
# como PNG y el movimiento puesto por ffmpeg (zoompan + xfade).
#
# El tono NO es de anuncio, a propósito: primera persona, «le pedí a una IA», que es
# como se cuenta una herramienta en el feed de 2026. Un Reel que parece un anuncio se
# salta; uno que parece alguien enseñando lo que ha probado, no.
#
# Zona segura de Reels: la interfaz de Instagram tapa ~200px arriba y ~420px abajo
# (usuario, pie, botones laterales). Todo el texto vive entre y=230 e y=1480.
HELMET = open('Main.dc.html').read().split('<helmet>')[1].split('</helmet>')[0]

W, H = 1080, 1920
SOMBRA = 'text-shadow: 0 4px 34px rgba(0, 0, 0, 0.55)'

def pagina(cuerpo):
    return ('<!doctype html>\n<html>\n<head>\n  <meta charset="utf-8">\n'
            '  <script src="./support.js"></script>\n  <style>body { margin: 0 }</style>\n</head>\n<body>\n<x-dc>\n'
            '<helmet>' + HELMET + '</helmet>\n' + cuerpo + '\n</x-dc>\n</body>\n</html>\n')

RAIZ = (f'<div style="width: {W}px; height: {H}px; box-sizing: border-box; position: relative; '
        'overflow: hidden; background: #100E0B; color: #FFFDF9; display: flex; flex-direction: column">')

def foto(src, escala=1.0):
    # `scale` da margen para que el zoompan de ffmpeg no muerda los bordes.
    return (f'<img src="fotos/{src}" alt="" style="position: absolute; inset: 0; width: 100%; height: 100%; '
            f'object-fit: cover; transform: scale({escala}); display: block">')

def velo(g):
    return f'<div style="position: absolute; inset: 0; background: {g}"></div>'

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

# 1 · EL GANCHO. Primera persona y una pregunta concreta: es lo que para el dedo.
ESCENAS['reel-01'] = (RAIZ
  + foto('f-portada.jpg', 1.06)
  + velo('linear-gradient(180deg, rgba(16, 14, 11, 0.55) 0%, rgba(16, 14, 11, 0.25) 40%, rgba(16, 14, 11, 0.8) 100%)')
  + titular('Le ped&iacute; a una IA<br>que me organizara<br>3 d&iacute;as en Roma.', 470, 88)
  + sub('Esto es lo que me escribi&oacute;. 👇', 900, 44)
  + marca()
  + '</div>')

# 2 · EL PLAN. El teléfono ocupa la pantalla: es la prueba, no la ilustración.
ESCENAS['reel-02'] = (RAIZ
  + foto('f-plan.jpg', 1.04)
  + velo('linear-gradient(180deg, rgba(16, 14, 11, 0.78) 0%, rgba(16, 14, 11, 0.42) 34%, rgba(16, 14, 11, 0.5) 100%)')
  + kicker('El d&iacute;a, escrito')
  + titular('Qu&eacute; ver, en qu&eacute; orden<br>y cu&aacute;nto cuesta.', 320, 62, 900)
  + telefono('plan-900.webp', 600, 560)
  + '</div>')

# 3 · EL TOUR.
ESCENAS['reel-03'] = (RAIZ
  + foto('f-tour.jpg', 1.04)
  + velo('linear-gradient(180deg, rgba(16, 14, 11, 0.78) 0%, rgba(16, 14, 11, 0.4) 34%, rgba(16, 14, 11, 0.5) 100%)')
  + kicker('Y por la calle')
  + titular('Te lo cuenta al o&iacute;do<br>mientras lo andas.', 320, 62, 900)
  + telefono('tour-900.webp', 600, 560)
  + '</div>')

# 4 · EL MUSEO.
ESCENAS['reel-04'] = (RAIZ
  + foto('f-museo.jpg', 1.04)
  + velo('linear-gradient(180deg, rgba(16, 14, 11, 0.78) 0%, rgba(16, 14, 11, 0.4) 34%, rgba(16, 14, 11, 0.5) 100%)')
  + kicker('Dentro del museo')
  + titular('Enfocas un cuadro<br>y te cuenta su historia.', 320, 62, 900)
  + telefono('museo-900.webp', 600, 560)
  + '</div>')

# 5 · EL PRECIO Y LA LISTA. El número grande y una sola instrucción.
ESCENAS['reel-05'] = (RAIZ
  + foto('f-precio.jpg', 1.06)
  + velo('linear-gradient(180deg, rgba(16, 14, 11, 0.5) 0%, rgba(16, 14, 11, 0.35) 30%, rgba(16, 14, 11, 0.88) 100%)')
  + kicker('Llega en octubre', 400)
  + titular('El viaje entero,<br>por 2,99&nbsp;&euro;.', 470, 88)
  + f'<p class="sans" style="position: absolute; left: 84px; top: 800px; margin: 0; font-size: 40px; line-height: 1.4; color: #5CC0A6; font-weight: 700; {SOMBRA}">En la lista de espera,<br>tu primer viaje por 1,99&nbsp;&euro;.</p>'
  + sub('Ap&uacute;ntate en el enlace de la bio.', 990, 38)
  + marca()
  + '</div>')

for nombre, cuerpo in ESCENAS.items():
    open(f'{nombre}.dc.html', 'w').write(pagina(cuerpo))
print('escritas', len(ESCENAS), 'escenas')
