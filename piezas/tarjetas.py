# LOS AYUDANTES DE UNA TARJETA DE POST (1080x1350), compartidos por los carruseles.
#
# Existe desde el 6-sep, cuando el segundo carrusel (Barcelona) iba a copiar entero el
# molde del primero (Roma). Los generadores de historias y reels sí repiten sus ayudantes
# —cada uno tiene su lienzo y sus posiciones—, pero estos dos son EL MISMO formato, y
# duplicarlo significaba que un retoque de estilo se aplicaría a un carrusel y al otro no.
#
# Los números salen de gen-destacadas.py y no se reinventan: kicker de 30 px con
# letter-spacing 0.18em en mayúsculas, titular en serif con line-height 1.06, la sombra de
# la casa, el menta, y el móvil de telefono() a escala de post.
#
# Se importa desde salida/, que es donde corren los generadores:
#     import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
#     from tarjetas import *
W, H = 1080, 1350
SOMBRA = 'text-shadow: 0 4px 34px rgba(0, 0, 0, 0.55)'
MENTA, PAPEL = '#5CC0A6', '#FFFDF9'
NOCHE = 'linear-gradient(160deg, #16130F 0%, #100E0B 55%, #1B2620 100%)'

# Los velos de la casa, adaptados al alto del post.
VELO_FOTO = ('linear-gradient(180deg, rgba(16, 14, 11, 0.72) 0%, rgba(16, 14, 11, 0.34) 42%, '
             'rgba(16, 14, 11, 0.86) 100%)')
VELO_TELEFONO = ('linear-gradient(180deg, rgba(16, 14, 11, 0.84) 0%, rgba(16, 14, 11, 0.5) 38%, '
                 'rgba(16, 14, 11, 0.6) 100%)')

def pagina(cuerpo, helmet):
    return ('<!doctype html>\n<html>\n<head>\n  <meta charset="utf-8">\n'
            '  <script src="./support.js"></script>\n  <style>body { margin: 0 }</style>\n</head>\n<body>\n<x-dc>\n'
            '<helmet>' + helmet + '</helmet>\n' + cuerpo + '\n</x-dc>\n</body>\n</html>\n')

def raiz(fondo=None):
    f = fondo or '#100E0B'
    return (f'<div style="width: {W}px; height: {H}px; box-sizing: border-box; position: relative; '
            f'overflow: hidden; background: {f}; color: {PAPEL}">')

def foto(src, escala=1.04, ajuste='cover', pos=None):
    # `object-position` sólo se escribe si se pide: `center` es el valor por defecto de CSS
    # y añadirlo cambiaría la salida de los generadores que ya existen sin cambiar el píxel.
    p = f'object-position: {pos}; ' if pos else ''
    return (f'<img src="fotos/{src}" alt="" style="position: absolute; inset: 0; width: 100%; height: 100%; '
            f'object-fit: {ajuste}; {p}transform: scale({escala}); display: block">')

def velo(g):
    return f'<div style="position: absolute; inset: 0; background: {g}"></div>'

def kicker(t, y=110, color=None):
    c = color or 'rgba(255, 253, 249, 0.82)'
    return (f'<p class="sans" style="position: absolute; left: 84px; top: {y}px; margin: 0; font-size: 30px; '
            f'letter-spacing: 0.18em; text-transform: uppercase; color: {c}; font-weight: 600; {SOMBRA}">{t}</p>')

def titular(t, y, size=92, ancho=912):
    return (f'<h1 class="serif" style="position: absolute; left: {84}px; top: {y}px; margin: 0; width: {ancho}px; '
            f'font-size: {size}px; line-height: 1.06; letter-spacing: -0.018em; font-weight: 400; {SOMBRA}">{t}</h1>')

def sub(t, y, size=38, color='rgba(255, 253, 249, 0.88)', ancho=912, peso=500):
    """Sin <br> en el cuerpo, a propósito: el corte forzado ignora el ancho real de la
    fuente al exportar (las del HELMET y las reales no miden igual) y deja renglones
    sueltos. Se controla con el ancho y se deja fluir; `text-wrap: pretty` evita viudas."""
    return (f'<p class="sans" style="position: absolute; left: 84px; top: {y}px; margin: 0; width: {ancho}px; '
            f'font-size: {size}px; line-height: 1.4; color: {color}; font-weight: {peso}; '
            f'text-wrap: pretty; {SOMBRA}">{t}</p>')

def marca(y=1200):
    return (f'<div style="position: absolute; left: 84px; top: {y}px; display: flex; align-items: center; gap: 18px">'
            f'<img src="mark.png" alt="" style="width: 50px; height: 50px">'
            f'<span class="sans" style="font-size: 28px; color: rgba(255, 253, 249, 0.85); font-weight: 600; '
            f'letter-spacing: 0.02em; {SOMBRA}">travelsnomad.com</span></div>')

def telefono(png, ancho=430, arriba=500):
    """El móvil de las destacadas (telefono() en gen-destacadas.py), a escala de post."""
    r, p, ar, isla_w, isla_h = 59, 13, 4, 129, 36
    return (f'<div style="position: absolute; left: 50%; top: {arriba}px; transform: translateX(-50%); '
            f'width: {ancho}px; aspect-ratio: 9 / 19.5; background: #0b0b0d; border-radius: {r}px; padding: {p}px; '
            f'box-shadow: 0 44px 110px rgba(0, 0, 0, 0.6)">'
            f'<div style="position: absolute; inset: 0; border-radius: {r}px; border: {ar}px solid #98979c"></div>'
            f'<div style="position: absolute; top: 25px; left: 50%; transform: translateX(-50%); width: {isla_w}px; '
            f'height: {isla_h}px; background: #0b0b0d; border-radius: 20px; z-index: 2"></div>'
            f'<div style="width: 100%; height: 100%; border-radius: {r - p}px; background: #F5F0E8; overflow: hidden">'
            f'<img src="{png}" alt="" style="width: 100%; display: block"></div></div>')

def pendiente(texto, ancho=430, arriba=500):
    """El hueco de una captura que todavía no existe. Se pinta A PROPÓSITO como un aviso
    chillón: una tarjeta a la que le falta la prueba no puede parecer terminada."""
    return (f'<div style="position: absolute; left: 50%; top: {arriba}px; transform: translateX(-50%); '
            f'width: {ancho}px; aspect-ratio: 9 / 19.5; border: 6px dashed #E4572E; border-radius: 59px; '
            f'background: rgba(228, 87, 46, 0.16); display: flex; align-items: center; justify-content: center; '
            f'padding: 40px; box-sizing: border-box">'
            f'<span class="sans" style="font-size: 30px; line-height: 1.4; font-weight: 700; text-align: center; '
            f'color: #FFFDF9">{texto}</span></div>')

def documento(src, ancho=820, arriba=560, giro=-1.5):
    """Una imagen presentada COMO DOCUMENTO —con su marco claro y una sombra— en vez de
    a sangre. Para planos, mapas y papeles: puestos de fondo se leen como textura y no se
    entiende qué son; enmarcados se leen como lo que son, un documento."""
    return (f'<div style="position: absolute; left: 50%; top: {arriba}px; transform: translateX(-50%) '
            f'rotate({giro}deg); width: {ancho}px; padding: 18px; background: #F5F0E8; '
            f'box-shadow: 0 40px 90px rgba(0, 0, 0, 0.55)">'
            f'<img src="fotos/{src}" alt="" style="width: 100%; display: block"></div>')

def numero(n, y=190, size=300, color=None):
    """UN NÚMERO COMO PROTAGONISTA. Sale de una pega del dueño (6-sep): las fotos que hay
    en Commons de un sitio concreto son documentales y «se ven cutres» al lado del grid.
    Un número grande en serif no necesita foto, es de la casa y aguanta a tamaño de rejilla
    — y una fecha es exactamente lo que engancha en una historia de sitios."""
    c = color or PAPEL
    return (f'<p class="serif" style="position: absolute; left: 78px; top: {y}px; margin: 0; '
            f'font-size: {size}px; line-height: 0.92; letter-spacing: -0.04em; color: {c}; '
            f'font-weight: 400; {SOMBRA}">{n}</p>')
