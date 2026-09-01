# El TALLER DE REDES (1-sep, noche): un lienzo editable con todo lo que hace falta para
# fabricar una pieza de Instagram sin pedirla — el kit de marca, las plantillas y las
# piezas ya hechas, cada una como un artboard que se retoca en sitio y se exporta a PNG.
#
# Salió de una frase del dueño: «no quiero que me mandes las fotos, quiero poder
# editarlas yo antes por si algo no me gusta». Hasta ahora cada pieza salía de un
# generador (gen-destacadas.py, gen-reel*.py) y llegaba como PNG cerrado; lo que cambia
# es dónde vive: en el lienzo, con el texto editable y la foto elegible.
#
# Lo que NO cambia: los generadores siguen siendo la fuente. Este script COPIA sus
# artboards al taller (con las rutas de imagen aplanadas al nombre de fichero, que es lo
# que el lienzo entiende) y añade encima el kit y las plantillas. Si una pieza se
# rehace en su generador, se vuelve a construir el taller; si el dueño la edita en el
# lienzo, manda el lienzo y ya no se vuelve a sembrar encima sin leerlo antes.
#
# Uso: SC=<scratchpad> python3 construir-taller.py  → escribe <scratchpad>/taller/
import os, re, json, shutil, sys
from PIL import Image

SC = os.environ.get('SC') or '/tmp/claude-0/-home-user-NOMAD/540f89ad-ecf3-574a-baa5-50e2739fd1e9/scratchpad'
IG, OUT = f'{SC}/ig', f'{SC}/taller'
os.makedirs(OUT, exist_ok=True)

HELMET = open(f'{IG}/Main.dc.html').read().split('<helmet>')[1].split('</helmet>')[0]
CREDITOS = json.load(open(f'{IG}/fotos/creditos.json'))
FOTOS = list(CREDITOS.keys())                      # las once del banco, en su orden
LUCIDE = json.load(open('/tmp/claude-0/lucide-kit.json'))

# ── colores de la casa (mobile/src/theme/tokens.ts, copiados a mano y no redondeados) ──
INK, PAPEL, CREMA, MUTED = '#14120F', '#FFFDF9', '#F5F0E8', '#6E675C'
ACENTO, CLAY = '#0F766E', '#A65B3F'
NOCHE, MENTA = '#100E0B', '#5CC0A6'               # los de historias y reels: fondo fijo
LINEA = 'rgba(20, 18, 15, 0.10)'

# ═══════════════════════════════════════════════════════════════════════════════
# 1 · IMÁGENES. Las fotos van a 1080×1920 (recorte 9:16 centrado, que es exactamente
#     el encuadre que hacía `object-fit: cover` sobre las de 1080×1350: nada se mueve).
#     Las tres postales salían de recortes de 980×380 — cinco veces ampliadas en una
#     historia — y aquí vuelven a cortarse de sus originales de Commons.
# ═══════════════════════════════════════════════════════════════════════════════
ORIGEN = {'f-oia.jpg': 'g_oia.jpg', 'f-porto.jpg': 'g_porto.jpg', 'f-alhambra.jpg': 'c_tres2_0.jpg'}

def recorte_916(src, dst, ancho=1080, alto=1920):
    im = Image.open(src).convert('RGB')
    w, h = im.size
    if w / h > ancho / alto:            # demasiado ancha: recortar los lados
        nw = int(h * ancho / alto); x0 = (w - nw) // 2; im = im.crop((x0, 0, x0 + nw, h))
    else:                               # demasiado alta: recortar arriba y abajo
        nh = int(w * alto / ancho); y0 = (h - nh) // 2; im = im.crop((0, y0, w, y0 + nh))
    im = im.resize((ancho, alto), Image.LANCZOS)
    im.save(dst, 'JPEG', quality=82, optimize=True, progressive=True)
    return os.path.getsize(dst)

peso = 0
for f in FOTOS:
    peso += recorte_916(f'{IG}/fotos/{ORIGEN.get(f, f)}', f'{OUT}/{f}')
CAPTURAS = ['plan', 'tour', 'museo', 'grupo', 'crear', 'visita']
for c in CAPTURAS:
    for suf in ('', '-it'):
        shutil.copy(f'{IG}/{c}-900{suf}.webp', OUT); peso += os.path.getsize(f'{OUT}/{c}-900{suf}.webp')
for extra in ('mark.png', 'mark-claro.png', 'tarjeta-qr-ejemplo.png'):
    shutil.copy(f'{IG}/{extra}', OUT); peso += os.path.getsize(f'{OUT}/{extra}')
print(f'imágenes: {peso // 1024} KB')

# ═══════════════════════════════════════════════════════════════════════════════
# 2 · LAS PIEZAS HECHAS: se copian de los generadores con la ruta `fotos/` aplanada.
# ═══════════════════════════════════════════════════════════════════════════════
PIEZAS = {}   # stem del artboard -> (fichero origen, título visible)
for i in range(1, 8):
    PIEZAS[f'ES-QueEs-{i}'] = (f'qe-{i}', f'Qué es · {i}')
    PIEZAS[f'IT-QueEs-{i}'] = (f'qe-it-{i}', f'Cos\'è · {i}')
for i in range(1, 5):
    PIEZAS[f'ES-Lista-{i}'] = (f'li-{i}', f'La lista · {i}')
    PIEZAS[f'IT-Lista-{i}'] = (f'li-it-{i}', f'Lista d\'attesa · {i}')
PIEZAS['Caratula-QueEs'] = ('car-quees', 'Carátula · Qué es')
PIEZAS['Caratula-Lista'] = ('car-lista', 'Carátula · La lista')
for i in range(1, 6):
    PIEZAS[f'Reel-Roma-{i}'] = (f'reel-0{i}', f'Reel Roma · escena {i}')
    PIEZAS[f'Reel-Grupo-{i}'] = (f'reelg-0{i}', f'Reel Grupo · escena {i}')
    PIEZAS[f'Reel-RomaIT-{i}'] = (f'reelit-0{i}', f'Reel Roma IT · escena {i}')

for stem, (origen, _) in PIEZAS.items():
    s = open(f'{IG}/{origen}.dc.html').read().replace('src="fotos/', 'src="')
    assert 'fotos/' not in s, stem
    open(f'{OUT}/{stem}.dc.html', 'w').write(s)

# ═══════════════════════════════════════════════════════════════════════════════
# 3 · Los ladrillos de las plantillas y del kit.
# ═══════════════════════════════════════════════════════════════════════════════
SOMBRA = 'text-shadow: 0 4px 34px rgba(0, 0, 0, 0.55)'

def pagina(cuerpo, script=''):
    return ('<!doctype html>\n<html>\n<head>\n  <meta charset="utf-8">\n'
            '  <script src="./support.js"></script>\n  <style>body { margin: 0 }</style>\n</head>\n<body>\n<x-dc>\n'
            '<helmet>' + HELMET + '</helmet>\n' + cuerpo + '\n</x-dc>\n' + script + '</body>\n</html>\n')

def raiz(w, h, fondo=NOCHE, color=PAPEL):
    return (f'<div style="width: {w}px; height: {h}px; box-sizing: border-box; position: relative; '
            f'overflow: hidden; background: {fondo}; color: {color}">')

def clave(f):                      # f-portada.jpg -> es_portada
    return 'es_' + re.sub(r'[^a-z0-9]', '_', f[2:-4])

def capa_foto(escala=1.04):
    """Una rama por foto del banco: el chip «foto» decide cuál se pinta. Cada rama lleva su
    `src` literal, que es lo único que el lienzo sustituye por la imagen."""
    partes = []
    for f in FOTOS:
        ph = 'true' if f == FOTOS[0] else 'false'
        partes.append('<sc-if value="{{ ' + clave(f) + ' }}" hint-placeholder-val="{{ ' + ph + ' }}">'
                      f'<img src="{f}" alt="" style="position: absolute; inset: 0; width: 100%; height: 100%; '
                      f'object-fit: cover; transform: scale({escala}); display: block"></sc-if>')
    return ''.join(partes)

def capa_captura():
    """Doce ramas: seis pantallas por dos idiomas. Los chips «captura» e «idioma» eligen."""
    partes = []
    for c in CAPTURAS:
        for suf, idioma in (('', 'es'), ('-it', 'it')):
            ph = 'true' if (c == 'plan' and idioma == 'es') else 'false'
            partes.append('<sc-if value="{{ cap_' + c + '_' + idioma + ' }}" hint-placeholder-val="{{ ' + ph + ' }}">'
                          f'<img src="{c}-900{suf}.webp" alt="" style="width: 100%; display: block"></sc-if>')
    return ''.join(partes)

def props_foto(extra=None):
    d = {'foto': {'editor': 'enum', 'options': FOTOS, 'default': FOTOS[0], 'section': 'Fondo'}}
    if extra: d.update(extra)
    return json.dumps(d, ensure_ascii=False)

def vals_foto():
    return ', '.join(f"{clave(f)}: foto === '{f}'" for f in FOTOS)

def script_foto(extra_props=None, extra_vals=''):
    return ("<script data-dc-script data-props='" + props_foto(extra_props) + "'>\n"
            "class Component extends DCLogic {\n  renderVals() {\n"
            f"    const foto = this.props.foto ?? '{FOTOS[0]}';\n"
            "    const cap = this.props.captura ?? 'plan';\n    const idioma = this.props.idioma ?? 'es';\n"
            "    return { " + vals_foto() + (', ' + extra_vals if extra_vals else '') + " };\n  }\n}\n</script>\n")

def velo(g):
    return f'<div style="position: absolute; inset: 0; background: {g}"></div>'

def scrim(desde=240, hasta=1140):
    return (f'<div style="position: absolute; left: 0; right: 0; top: {desde}px; height: {hasta - desde}px; '
            'background: linear-gradient(180deg, rgba(16, 14, 11, 0) 0%, rgba(16, 14, 11, 0.72) 18%, '
            'rgba(16, 14, 11, 0.72) 78%, rgba(16, 14, 11, 0) 100%)"></div>')

def kicker(t, y=300, color='rgba(255, 253, 249, 0.82)'):
    return (f'<p class="sans" style="position: absolute; left: 84px; top: {y}px; margin: 0; font-size: 32px; '
            f'letter-spacing: 0.18em; text-transform: uppercase; color: {color}; font-weight: 600; {SOMBRA}">{t}</p>')

def titular(t, y, size=82, ancho=912):
    return (f'<h1 class="serif" style="position: absolute; left: 84px; top: {y}px; margin: 0; width: {ancho}px; '
            f'font-size: {size}px; line-height: 1.08; letter-spacing: -0.015em; font-weight: 400; {SOMBRA}">{t}</h1>')

def sub(t, y, size=40, color='rgba(255, 253, 249, 0.9)', peso=500):
    return (f'<p class="sans" style="position: absolute; left: 84px; top: {y}px; margin: 0; width: 912px; '
            f'font-size: {size}px; line-height: 1.35; color: {color}; font-weight: {peso}; {SOMBRA}">{t}</p>')

def marca(y=1400):
    return (f'<div style="position: absolute; left: 84px; top: {y}px; display: flex; align-items: center; gap: 20px">'
            f'<img src="mark.png" alt="" style="width: 54px; height: 54px">'
            f'<span class="sans" style="font-size: 30px; color: rgba(255, 253, 249, 0.85); font-weight: 600; '
            f'letter-spacing: 0.02em; {SOMBRA}">travelsnomad.com</span></div>')

def telefono(interior, ancho=480, arriba=680):
    r = int(ancho * 66 / 480)
    return (f'<div style="position: absolute; left: 50%; top: {arriba}px; transform: translateX(-50%); width: {ancho}px; '
            f'aspect-ratio: 9 / 19.5; background: #0b0b0d; border-radius: {r}px; padding: 14px; box-shadow: 0 50px 120px rgba(0, 0, 0, 0.6)">'
            f'<div style="position: absolute; inset: 0; border-radius: {r}px; border: 5px solid #98979c"></div>'
            f'<div style="position: absolute; top: 28px; left: 50%; transform: translateX(-50%); width: 144px; height: 40px; background: #0b0b0d; border-radius: 22px; z-index: 2"></div>'
            f'<div style="width: 100%; height: 100%; border-radius: {r - 14}px; background: {CREMA}; overflow: hidden">{interior}</div></div>')

def paso(n, t, y):
    return (f'<div style="position: absolute; left: 84px; top: {y}px; width: 912px; display: flex; align-items: baseline; gap: 28px">'
            f'<span class="serif" style="font-size: 76px; line-height: 1; color: {MENTA}; {SOMBRA}">{n}</span>'
            f'<span class="sans" style="font-size: 42px; line-height: 1.3; font-weight: 600; {SOMBRA}">{t}</span></div>')

VELO_TEXTO = 'linear-gradient(180deg, rgba(16, 14, 11, 0.62) 0%, rgba(16, 14, 11, 0.3) 45%, rgba(16, 14, 11, 0.85) 100%)'
VELO_TELEFONO = 'linear-gradient(180deg, rgba(16, 14, 11, 0.82) 0%, rgba(16, 14, 11, 0.46) 36%, rgba(16, 14, 11, 0.55) 100%)'

PLANTILLAS = {}

PLANTILLAS['Plantilla-HistoriaFoto'] = pagina(
    raiz(1080, 1920) + capa_foto() + velo(VELO_TEXTO) + scrim(240, 1000)
    + kicker('Llega en octubre') + titular('Un titular<br>de dos l&iacute;neas.', 420, 108)
    + sub('Una frase que lo explica,<br>y no m&aacute;s de dos l&iacute;neas.', 800, 44) + marca() + '</div>',
    script_foto())

PLANTILLAS['Plantilla-HistoriaTelefono'] = pagina(
    raiz(1080, 1920) + capa_foto() + velo(VELO_TELEFONO)
    + kicker('1 &middot; Lo que hace') + titular('Lo que se ve<br>en la pantalla.', 380, 64, 900)
    + telefono(capa_captura()) + '</div>',
    script_foto({'captura': {'editor': 'enum', 'options': CAPTURAS, 'default': 'plan', 'section': 'Teléfono'},
                 'idioma': {'editor': 'enum', 'options': ['es', 'it'], 'default': 'es', 'section': 'Teléfono'}},
                ', '.join(f"cap_{c}_{i}: cap === '{c}' && idioma === '{i}'" for c in CAPTURAS for i in ('es', 'it'))))

PLANTILLAS['Plantilla-HistoriaPasos'] = pagina(
    raiz(1080, 1920) + velo('linear-gradient(160deg, #16130F 0%, #100E0B 55%, #1B2620 100%)')
    + kicker('C&oacute;mo se hace') + titular('Tres pasos<br>y treinta segundos.', 380, 76)
    + paso('1', 'El primer paso,<br>en una l&iacute;nea o dos.', 700) + paso('2', 'El segundo.', 940)
    + paso('3', 'Y el tercero, que es<br>el que cierra.', 1090) + marca(1420) + '</div>')

PLANTILLAS['Plantilla-HistoriaPlana'] = pagina(
    raiz(1080, 1920) + velo('linear-gradient(160deg, #1B2620 0%, #100E0B 55%, #16130F 100%)')
    + kicker('Sin foto') + titular('Una frase corta.', 420, 96)
    + sub('Lo que va debajo, en tres o cuatro<br>l&iacute;neas como mucho.<br><br>Y un cierre.', 640, 44)
    + marca(1400) + '</div>')

PLANTILLAS['Plantilla-ReelEscena'] = pagina(
    raiz(1080, 1920) + capa_foto(1.04)
    + velo('linear-gradient(180deg, rgba(16, 14, 11, 0.8) 0%, rgba(16, 14, 11, 0.44) 34%, rgba(16, 14, 11, 0.5) 100%)')
    + kicker('Uno', 250) + titular('La escena del reel:<br>zona segura de 230 a 1480.', 320, 60, 940)
    + telefono(capa_captura(), 600, 560) + '</div>',
    script_foto({'captura': {'editor': 'enum', 'options': CAPTURAS, 'default': 'plan', 'section': 'Teléfono'},
                 'idioma': {'editor': 'enum', 'options': ['es', 'it'], 'default': 'es', 'section': 'Teléfono'}},
                ', '.join(f"cap_{c}_{i}: cap === '{c}' && idioma === '{i}'" for c in CAPTURAS for i in ('es', 'it'))))

PLANTILLAS['Plantilla-Post'] = pagina(
    '<div style="width: 1080px; height: 1350px; box-sizing: border-box; display: flex; flex-direction: column; '
    f'background: {NOCHE}; color: {PAPEL}; position: relative; overflow: hidden; padding: 84px 96px 72px; justify-content: space-between">'
    + capa_foto(1.0)
    + velo('linear-gradient(180deg, rgba(16, 14, 11, 0.38) 0%, rgba(16, 14, 11, 0) 30%, rgba(16, 14, 11, 0) 46%, rgba(16, 14, 11, 0.82) 88%)')
    + '<img src="mark.png" alt="" style="width: 96px; height: 96px; position: relative">'
    + '<div style="display: flex; flex-direction: column; gap: 44px; position: relative">'
    + '<h1 class="serif" style="margin: 0; font-size: 116px; line-height: 1.06; letter-spacing: -0.02em; font-weight: 400; text-shadow: 0 3px 30px rgba(0, 0, 0, 0.45)">El titular<br>del post.</h1>'
    + '<p class="sans" style="margin: 0; font-size: 40px; color: rgba(255, 253, 249, 0.85)">La frase de debajo, una sola.</p>'
    + '<div style="display: flex; align-items: center; gap: 18px; position: relative"><img src="mark.png" alt="" style="width: 52px; height: 52px">'
    + '<span class="sans" style="font-size: 28px; color: rgba(255, 253, 249, 0.78); letter-spacing: 0.02em">travelsnomad.com</span></div>'
    + '</div></div>',
    script_foto())

PLANTILLAS['Plantilla-Caratula'] = pagina(
    '<div style="width: 1080px; height: 1920px; box-sizing: border-box; position: relative; overflow: hidden; background: {{ fondo }}">'
    '<sc-if value="{{ oscuro }}" hint-placeholder-val="{{ true }}"><img src="mark-claro.png" alt="" style="position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%); width: 380px; height: 380px"></sc-if>'
    '<sc-if value="{{ claro }}" hint-placeholder-val="{{ false }}"><img src="mark.png" alt="" style="position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%); width: 380px; height: 380px"></sc-if>'
    '</div>',
    "<script data-dc-script data-props='" + json.dumps({'fondo': {'editor': 'color', 'options': [NOCHE, ACENTO, CREMA, CLAY], 'default': NOCHE}}) + "'>\n"
    "class Component extends DCLogic {\n  renderVals() {\n    const fondo = this.props.fondo ?? '" + NOCHE + "';\n"
    "    const claro = fondo.toUpperCase() === '" + CREMA + "' || fondo.toUpperCase() === '" + PAPEL + "';\n"
    "    return { fondo, claro, oscuro: !claro };\n  }\n}\n</script>\n")

for stem, html in PLANTILLAS.items():
    open(f'{OUT}/{stem}.dc.html', 'w').write(html)

# ═══════════════════════════════════════════════════════════════════════════════
# 4 · EL KIT. Tableros en crema, con la letra de la casa, que documentan lo que hay.
# ═══════════════════════════════════════════════════════════════════════════════
def tablero(w, h, cuerpo):
    return pagina(f'<div style="width: {w}px; height: {h}px; box-sizing: border-box; position: relative; overflow: hidden; '
                  f'background: {CREMA}; color: {INK}; padding: 72px 80px; display: flex; flex-direction: column; gap: 40px">'
                  + cuerpo + '</div>')

def eyebrow(t):
    return (f'<p class="sans" style="margin: 0; font-size: 14px; letter-spacing: 0.14em; text-transform: uppercase; '
            f'font-weight: 600; color: {MUTED}">{t}</p>')

def h1(t, size=64):
    return f'<h1 class="serif" style="margin: 0; font-size: {size}px; line-height: 1.05; letter-spacing: -0.02em; font-weight: 400">{t}</h1>'

def parrafo(t, size=20, color=INK, ancho=None):
    w = f' max-width: {ancho}px;' if ancho else ''
    return f'<p class="sans" style="margin: 0; font-size: {size}px; line-height: 1.45; color: {color};{w}">{t}</p>'

def seccion(titulo):
    return (f'<div style="display: flex; align-items: center; gap: 16px"><span class="sans" style="font-size: 15px; font-weight: 700; '
            f'letter-spacing: 0.1em; text-transform: uppercase">{titulo}</span><div style="flex-grow: 1; height: 1px; background: {LINEA}"></div></div>')

# 4a · Portada del taller (Main)
def fila_pagina(nombre, contenido):
    return (f'<div style="display: flex; gap: 24px; align-items: baseline; padding: 14px 0; border-bottom: 1px solid {LINEA}">'
            f'<span class="serif" style="font-size: 30px; width: 260px; flex-shrink: 0">{nombre}</span>'
            f'<span class="sans" style="font-size: 19px; line-height: 1.4; color: {MUTED}">{contenido}</span></div>')

def regla(n, t):
    return (f'<div style="display: flex; gap: 20px; align-items: baseline"><span class="serif" style="font-size: 40px; color: {ACENTO}; line-height: 1">{n}</span>'
            f'<span class="sans" style="font-size: 19px; line-height: 1.45">{t}</span></div>')

KIT = {}
KIT['Main'] = tablero(1200, 1500,
    eyebrow('Taller de redes &middot; septiembre 2026') + h1('Taller de redes NOMAD', 84)
    + parrafo('Todo lo que hace falta para fabricar una pieza de Instagram sin pedirla: el kit de marca, siete plantillas y las piezas ya hechas. Cada una es un artboard que se retoca en sitio y se exporta a PNG.', 22, INK, 980)
    + '<div style="display: flex; flex-direction: column">'
    + fila_pagina('Kit', 'Colores, tipograf&iacute;a, la marca, 22 iconos de la app, las 11 fotos del banco (Commons, CC0 o dominio p&uacute;blico, con su cr&eacute;dito) y las 12 capturas reales.')
    + fila_pagina('Plantillas', 'Siete arranques: historia con foto, con tel&eacute;fono, de pasos, plana, escena de reel, post del feed y car&aacute;tula.')
    + fila_pagina('Historias &middot; ES', '&laquo;Qu&eacute; es&raquo; (7) y &laquo;La lista&raquo; (4), m&aacute;s las dos car&aacute;tulas.')
    + fila_pagina('Historias &middot; IT', '&laquo;Cos&rsquo;&egrave;&raquo; (7) y &laquo;Lista d&rsquo;attesa&raquo; (4).')
    + fila_pagina('Reels', 'Roma (5 escenas), Grupo (5) y Roma en italiano (5). Cada escena es un PNG; el movimiento lo pone ffmpeg.')
    + '</div>'
    + seccion('C&oacute;mo se usa')
    + '<div style="display: flex; flex-direction: column; gap: 22px">'
    + regla('1', 'Duplica la plantilla o la pieza m&aacute;s parecida. Tocas un texto y lo reescribes en sitio.')
    + regla('2', 'La foto se cambia con el chip &laquo;foto&raquo; de encima de la plantilla; la pantalla del tel&eacute;fono, con &laquo;captura&raquo; e &laquo;idioma&raquo;. El banco entero est&aacute; en Kit &rarr; Fotos.')
    + regla('3', 'Exporta PNG desde el artboard. Historias y escenas de reel a 1080&times;1920; posts a 1080&times;1350. Instagram tapa ~250 px arriba y abajo de una historia: el texto vive entre 280 y 1500, y de 1520 para abajo va el adhesivo de enlace.')
    + '</div>'
    + parrafo('Tipograf&iacute;as embebidas: Instrument Serif para lo que es del viaje, Instrument Sans para lo funcional. Las fotos son de Wikimedia Commons y no deben atribuci&oacute;n; el cr&eacute;dito est&aacute; igualmente en el banco.', 16, MUTED, 980))

# 4b · Colores
def muestra(nombre, hexa, borde=False):
    b = f' border: 1px solid {LINEA};' if borde else ''
    return (f'<div style="display: flex; flex-direction: column; gap: 8px"><div style="height: 96px; border-radius: 14px; background: {hexa};{b}"></div>'
            f'<span class="sans" style="font-size: 15px; font-weight: 600">{nombre}</span>'
            f'<span class="sans" style="font-size: 13px; color: {MUTED}">{hexa}</span></div>')

def rejilla(items, cols=6):
    return f'<div style="display: grid; grid-template-columns: repeat({cols}, minmax(0, 1fr)); gap: 20px">' + ''.join(items) + '</div>'

KIT['Kit-Colores'] = tablero(1200, 1400,
    eyebrow('Kit &middot; colores') + h1('Los colores')
    + seccion('Historias y reels &middot; fondo fijo, no depende del tema')
    + rejilla([muestra('noche (fondo)', NOCHE), muestra('paperWhite (texto)', PAPEL, True), muestra('menta (subrayado)', MENTA),
               muestra('accent', ACENTO), muestra('velo', 'rgba(16, 14, 11, 0.72)'), muestra('crema (pantalla)', CREMA, True)])
    + seccion('La app &middot; tema claro')
    + rejilla([muestra('bg', CREMA, True), muestra('surface', PAPEL, True), muestra('ink', INK), muestra('muted', MUTED),
               muestra('accent', ACENTO), muestra('clay (= ahora)', CLAY), muestra('panel', INK), muestra('error', '#A6403A'),
               muestra('success', '#3F7D53'), muestra('warning', '#B5852C'), muestra('info', '#3B6EA5'), muestra('nightDeep', '#083634')])
    + seccion('La app &middot; tema oscuro')
    + rejilla([muestra('bg', '#14120F'), muestra('surface', '#1E1A16'), muestra('ink', '#FBF7F0', True), muestra('muted', '#9A9186'),
               muestra('accent', '#5EEAD4'), muestra('clay', '#E0A184'), muestra('panel', '#2A241E'), muestra('error', '#E0736C'),
               muestra('success', '#77C48D'), muestra('warning', '#E0B15C'), muestra('info', '#7FA8DC'), muestra('onAccent', '#0C0A08')])
    + parrafo('Dos reglas de la casa: <b>clay</b> no es un estado, significa &laquo;ahora&raquo; (el d&iacute;a activo, la hora actual) y no se usa para nada m&aacute;s; y el texto sobre una foto lleva siempre paperWhite, porque el blanco puro sobre papel c&aacute;lido se ve azul.', 16, MUTED, 1000))

# 4c · Tipografía
def espec(clase, size, peso, t, extra=''):
    return (f'<div style="display: flex; gap: 28px; align-items: baseline; padding: 12px 0; border-bottom: 1px solid {LINEA}">'
            f'<span class="sans" style="font-size: 13px; color: {MUTED}; width: 210px; flex-shrink: 0">{clase} &middot; {size}px &middot; {peso}</span>'
            f'<span class="{clase}" style="font-size: {size}px; line-height: 1.1; font-weight: {peso}; {extra}">{t}</span></div>')

KIT['Kit-Tipografia'] = tablero(1200, 1500,
    eyebrow('Kit &middot; tipograf&iacute;a') + h1('Dos familias, y cu&aacute;l lleva qu&eacute;')
    + parrafo('<b>Instrument Serif</b> para lo que es del viaje: el destino, el d&iacute;a, la hora, el importe, el titular. <b>Instrument Sans</b> para todo lo funcional: el kicker, la frase de apoyo, los pasos, el bot&oacute;n.', 18, INK, 1000)
    + seccion('En historias y reels')
    + '<div style="display: flex; flex-direction: column">'
    + espec('serif', 108, 400, '&iquest;Qu&eacute; es NOMAD?', 'letter-spacing: -0.015em')
    + espec('serif', 82, 400, 'Llega en octubre.', 'letter-spacing: -0.015em')
    + espec('serif', 64, 400, 'Dices d&oacute;nde y cu&aacute;ndo.', 'letter-spacing: -0.015em')
    + espec('sans', 32, 600, '1 &middot; EL PLAN', 'letter-spacing: 0.18em')
    + espec('sans', 44, 500, 'Una app que te escribe el viaje entero.')
    + espec('sans', 42, 600, 'Toca el enlace de la bio.')
    + '</div>'
    + seccion('En la app (typeScale.ts)')
    + '<div style="display: flex; flex-direction: column">'
    + espec('serif', 34, 400, 'display &middot; Roma en 5 d&iacute;as', 'letter-spacing: -0.6px')
    + espec('serif', 24, 400, 'heading &middot; S&aacute;bado, 29 de agosto', 'letter-spacing: -0.3px')
    + espec('sans', 19, 700, 'screenTitle &middot; Itinerario', 'letter-spacing: -0.3px')
    + espec('sans', 15, 400, 'body &middot; Te lleva de una parada a la siguiente y te dice d&oacute;nde ponerte.')
    + espec('serif', 28, 400, 'dataHero &middot; 225,00 &euro;', 'letter-spacing: -0.6px')
    + espec('sans', 10, 600, 'LABEL &middot; GASTO DEL GRUPO', 'letter-spacing: 1.4px')
    + '</div>')

# 4d · Marca
def tesela(fondo, marca_png, etiqueta, borde=False):
    b = f' border: 1px solid {LINEA};' if borde else ''
    return (f'<div style="display: flex; flex-direction: column; gap: 12px"><div style="height: 300px; border-radius: 20px; background: {fondo};{b} display: flex; align-items: center; justify-content: center">'
            f'<img src="{marca_png}" alt="" style="width: 150px; height: 150px"></div><span class="sans" style="font-size: 15px; color: {MUTED}">{etiqueta}</span></div>')

KIT['Kit-Marca'] = tablero(1200, 700,
    eyebrow('Kit &middot; marca') + h1('La hoja', 56)
    + rejilla([tesela(CREMA, 'mark.png', 'mark.png sobre crema (el icono de la app)', True),
               tesela(NOCHE, 'mark-claro.png', 'mark-claro.png sobre noche (historias)'),
               tesela(ACENTO, 'mark-claro.png', 'mark-claro.png sobre accent (car&aacute;tulas)')], 3)
    + '<div style="display: flex; align-items: center; gap: 18px"><img src="mark.png" alt="" style="width: 40px; height: 40px">'
    + '<span class="sans" style="font-size: 22px; font-weight: 600; letter-spacing: 0.02em">travelsnomad.com</span>'
    + f'<span class="sans" style="font-size: 15px; color: {MUTED}; margin-left: 12px">&larr; el cierre de toda pieza: la hoja y el dominio, nunca el nombre en letras</span></div>')

# 4e · Iconos (Lucide, los mismos que carga la app; ISC)
def icono(nombre, svg):
    return (f'<div style="display: flex; flex-direction: column; align-items: center; gap: 10px">'
            f'<svg viewBox="0 0 24 24" width="44" height="44" fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{svg}</svg>'
            f'<span class="sans" style="font-size: 13px; color: {MUTED}">{nombre}</span></div>')

KIT['Kit-Iconos'] = tablero(1200, 700,
    eyebrow('Kit &middot; iconos') + h1('Los iconos de la app', 56)
    + parrafo('Lucide, la misma librer&iacute;a que carga la app (licencia ISC). Trazo de 2 px sobre 24, sin relleno; se recolorean con <i>stroke</i>. Nunca un emoji.', 16, MUTED, 1000)
    + rejilla([icono(n, s) for n, s in LUCIDE.items()], 8))

# 4f · Fotos: reutilizan los mismos ficheros que las historias, así que no pesan nada más.
def ficha_foto(f):
    c = CREDITOS[f]; titulo = c['titulo'].replace('File:', '')
    return (f'<div style="display: flex; flex-direction: column; gap: 10px"><img src="{f}" alt="" style="width: 100%; aspect-ratio: 9 / 16; object-fit: cover; border-radius: 14px; display: block">'
            f'<span class="sans" style="font-size: 16px; font-weight: 700">{f}</span>'
            f'<span class="sans" style="font-size: 13px; line-height: 1.35; color: {MUTED}">{titulo}<br>{c["lic"]} &middot; Wikimedia Commons</span></div>')

KIT['Kit-Fotos'] = tablero(1760, 1500,
    eyebrow('Kit &middot; banco de fotos') + h1('Las once fotos', 56)
    + parrafo('Todas de Wikimedia Commons, CC0 o dominio p&uacute;blico, verificadas una a una: no se debe atribuci&oacute;n. Aqu&iacute; van a 1080&times;1920 (9:16), recortadas del original. El nombre es lo que elige el chip &laquo;foto&raquo; de cada plantilla.', 16, MUTED, 1300)
    + rejilla([ficha_foto(f) for f in FOTOS], 6))

# 4g · Capturas
def ficha_captura(c, suf, idioma):
    return (f'<div style="display: flex; flex-direction: column; gap: 10px"><div style="aspect-ratio: 9 / 19.5; border-radius: 14px; overflow: hidden; background: {PAPEL}; border: 1px solid {LINEA}">'
            f'<img src="{c}-900{suf}.webp" alt="" style="width: 100%; display: block"></div>'
            f'<span class="sans" style="font-size: 15px; font-weight: 700">{c}-900{suf}.webp</span>'
            f'<span class="sans" style="font-size: 13px; color: {MUTED}">{idioma}</span></div>')

KIT['Kit-Capturas'] = tablero(1760, 1600,
    eyebrow('Kit &middot; capturas') + h1('Las pantallas reales', 56)
    + parrafo('Capturas de la app, no maquetas: el plan, el tour, el museo, los gastos del grupo, crear viaje y la visita. En espa&ntilde;ol y en italiano; los chips &laquo;captura&raquo; e &laquo;idioma&raquo; de las plantillas con tel&eacute;fono eligen entre estas doce.', 16, MUTED, 1300)
    + rejilla([ficha_captura(c, '', 'espa&ntilde;ol') for c in CAPTURAS] + [ficha_captura(c, '-it', 'italiano') for c in CAPTURAS], 6))

for stem, html in KIT.items():
    open(f'{OUT}/{stem}.dc.html', 'w').write(html)

# ═══════════════════════════════════════════════════════════════════════════════
# 5 · canvas.json: cinco páginas, y en Plantillas las notas que explican los chips.
# ═══════════════════════════════════════════════════════════════════════════════
A, N = [], []
def art(stem, x, y, w, h, page, title): A.append({'file': f'{stem}.dc.html', 'x': x, 'y': y, 'w': w, 'h': h, 'page': page, 'title': title})
def nota(i, x, y, w, texto, page): N.append({'id': i, 'x': x, 'y': y, 'w': w, 'text': texto, 'page': page})

art('Main', 0, 0, 1200, 1500, 'kit', 'Portada del taller')
art('Kit-Colores', 1280, 0, 1200, 1400, 'kit', 'Colores')
art('Kit-Tipografia', 2560, 0, 1200, 1500, 'kit', 'Tipografía')
art('Kit-Marca', 0, 1640, 1200, 700, 'kit', 'Marca')
art('Kit-Iconos', 1280, 1640, 1200, 700, 'kit', 'Iconos')
art('Kit-Fotos', 0, 2480, 1760, 1500, 'kit', 'Banco de fotos')
art('Kit-Capturas', 1840, 2480, 1760, 1600, 'kit', 'Capturas de la app')

P = [('Plantilla-HistoriaFoto', 1920, 'Historia · foto y texto'), ('Plantilla-HistoriaTelefono', 1920, 'Historia · teléfono'),
     ('Plantilla-HistoriaPasos', 1920, 'Historia · pasos'), ('Plantilla-HistoriaPlana', 1920, 'Historia · plana'),
     ('Plantilla-ReelEscena', 1920, 'Escena de reel'), ('Plantilla-Post', 1350, 'Post del feed'), ('Plantilla-Caratula', 1920, 'Carátula')]
for i, (stem, h, t) in enumerate(P):
    art(stem, i * 1160, 0, 1080, h, 'plantillas', t)
nota('nota-foto', 0, -330, 520, 'La foto se elige con el chip «foto» de encima de cada plantilla: son las once del banco (Kit → Fotos). En las de teléfono, «captura» e «idioma» eligen la pantalla.', 'plantillas')
nota('nota-zona', 1160, -330, 520, 'Zona segura de historias: Instagram tapa ~250 px arriba y ~250 abajo. El texto vive entre y=280 e y=1500; de 1520 para abajo va el adhesivo de enlace, así que ahí no se pone nada.', 'plantillas')
nota('nota-pieza', 2320, -330, 520, 'Para una pieza nueva: duplica la plantilla, retoca el texto en sitio y exporta PNG desde el artboard. Las historias a 1080×1920; el post a 1080×1350.', 'plantillas')
nota('nota-reel', 4640, -330, 520, 'Una escena de reel es un PNG más. El reel entero son cinco: se exportan y se montan con docs/reels/montar-reel.sh, que pone el movimiento y los fundidos.', 'plantillas')

for i in range(1, 8):
    art(f'ES-QueEs-{i}', (i - 1) * 1160, 0, 1080, 1920, 'es', PIEZAS[f'ES-QueEs-{i}'][1])
    art(f'IT-QueEs-{i}', (i - 1) * 1160, 0, 1080, 1920, 'it', PIEZAS[f'IT-QueEs-{i}'][1])
for i in range(1, 5):
    art(f'ES-Lista-{i}', (i - 1) * 1160, 2040, 1080, 1920, 'es', PIEZAS[f'ES-Lista-{i}'][1])
    art(f'IT-Lista-{i}', (i - 1) * 1160, 2040, 1080, 1920, 'it', PIEZAS[f'IT-Lista-{i}'][1])
art('Caratula-QueEs', 4 * 1160, 2040, 1080, 1920, 'es', 'Carátula · Qué es')
art('Caratula-Lista', 5 * 1160, 2040, 1080, 1920, 'es', 'Carátula · La lista')
for i in range(1, 6):
    art(f'Reel-Roma-{i}', (i - 1) * 1160, 0, 1080, 1920, 'reels', PIEZAS[f'Reel-Roma-{i}'][1])
    art(f'Reel-Grupo-{i}', (i - 1) * 1160, 2040, 1080, 1920, 'reels', PIEZAS[f'Reel-Grupo-{i}'][1])
    art(f'Reel-RomaIT-{i}', (i - 1) * 1160, 4080, 1080, 1920, 'reels', PIEZAS[f'Reel-RomaIT-{i}'][1])
nota('nota-orden', 0, -330, 520, 'Las destacadas se suben en orden normal, 1 → 7, al revés que el grid. El adhesivo de enlace va en la última de «Qué es» y en la 1 y la 3 de «La lista».', 'es')
nota('nota-it', 0, -330, 520, 'Los adhesivos de las italianas apuntan a travelsnomad.com/it/ directamente, no a la raíz: así un italiano con el móvil en inglés cae igual en la página italiana.', 'it')
nota('nota-montaje', 0, -330, 520, 'Cada fila es un reel: cinco escenas que se exportan a PNG y se montan con docs/reels/montar-reel.sh. Sin audio a propósito: se elige dentro de Instagram al subir.', 'reels')

canvas = {'pages': [{'id': 'kit', 'name': 'Kit'}, {'id': 'plantillas', 'name': 'Plantillas'}, {'id': 'es', 'name': 'Historias · ES'},
                    {'id': 'it', 'name': 'Historias · IT'}, {'id': 'reels', 'name': 'Reels'}],
          'artboards': A, 'annotations': N, 'launch': {'view': 'canvas', 'page': 'kit'}}
json.dump(canvas, open(f'{OUT}/canvas.json', 'w'), ensure_ascii=False, indent=1)
stems = [a['file'][:-8] for a in A]
assert len(stems) == len(set(s.lower() for s in stems)), 'stems repetidos'
print(f'artboards: {len(A)} · notas: {len(N)} · páginas: 5')
