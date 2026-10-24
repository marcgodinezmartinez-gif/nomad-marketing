# LAS CAPTURAS DE LA FICHA DE LA APP STORE, a banco/capturas/ (24-oct).
#
# Por qué: la ficha pública de «Nomad: guía de viajes» lleva seis capturas hechas con el
# aspecto de HOY (las de plan/crear/grupo/museo del banco son de antes del rediseño: issue #5)
# y en la tipografía de la casa. Se leen de la API pública de iTunes, que devuelve sus URL; no
# hace falta nada del repo de la app.
#
# Qué hace:
#   1. `ficha-<nombre>-900.webp`: cada captura entera (titular y móvil), a 900 de ancho.
#   2. `movil-<nombre>.webp`: el móvil recortado de las tres que lo llevan recto (audioguía,
#      crear, gastos), con las esquinas transparentes. Las otras tres (itinerario, eventos,
#      lugares) llevan el móvil girado sobre fondo oscuro y no se recortan limpias.
#   3. `icono-app.png`: el icono, a 512.
#
# El recorte rellena el fondo desde los bordes (flood fill) y encoge la máscara 3 px: sin eso
# queda un halo claro de 2-3 px donde el borde negro del móvil se mezcla con el crema del fondo
# (se vio el 24-oct sobre una foto oscura). Los elementos que la ficha saca del marco (el
# reproductor, los chips) se conservan: forman parte de su estilo.
#
# Uso, desde la raíz del repo (necesita red):  python3 piezas/lanzamiento/recortar-moviles.py
# Después:  bash piezas/preparar.sh
import io, json, os, sys, urllib.request
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

ID = '6797973945'
BANCO = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'banco')
NOMBRES = ['itinerario', 'audioguia', 'crear', 'eventos', 'gastos', 'lugares']   # el orden de la ficha
CON_MOVIL_RECTO = {'audioguia', 'crear', 'gastos'}

def bajar(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60) as r:
        return r.read()

def recortar_movil(im):
    """El móvil entero, por debajo del titular, con alfa. `im` es la captura de 1284 px."""
    W, H = im.size
    reg = im.crop((int(W * 0.093), int(H * 0.298), int(W * 0.907), H))       # por debajo del titular
    w, h = reg.size
    trabajo = reg.copy()
    for semilla in ((3, 3), (w - 4, 3), (3, h - 4), (w - 4, h - 4), (3, h // 2), (w - 4, h // 2), (w // 2, 3)):
        ImageDraw.floodfill(trabajo, semilla, (255, 0, 255), thresh=45)
    a = np.array(trabajo).astype(int)
    fuera = (a[:, :, 0] == 255) & (a[:, :, 1] == 0) & (a[:, :, 2] == 255)
    # encoger la máscara: dilatar «fuera» 3 px (un filtro de máximo de 7 px)
    fuera_img = Image.fromarray((fuera * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(7))
    # quedarse sólo con lo que está unido al móvil: salpicaduras sueltas de la sombra de la
    # ficha, a unos píxeles del borde, sobrevivían a la máscara y se veían como motas claras.
    # (floodfill en RGB: en modo L con thresh=0 de Pillow no rellena nada)
    dentro_bin = Image.fromarray(255 - np.array(fuera_img)).convert('RGB')
    ImageDraw.floodfill(dentro_bin, (w // 2, h - 250), (0, 255, 0), thresh=0)
    b = np.array(dentro_bin)
    solo = (b[:, :, 0] == 0) & (b[:, :, 1] == 255) & (b[:, :, 2] == 0)
    dentro = Image.fromarray((solo * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.0))
    ys, xs = np.where(solo)
    caja = (xs.min(), ys.min(), xs.max() + 1, ys.max() + 1)
    sal = reg.convert('RGB'); sal.putalpha(dentro)
    return sal.crop(caja)

def main():
    info = json.loads(bajar(f'https://itunes.apple.com/lookup?id={ID}&country=es'))['results'][0]
    urls = info['screenshotUrls']
    if len(urls) != len(NOMBRES):
        sys.exit(f'La ficha trae {len(urls)} capturas y el script espera {len(NOMBRES)}: revisa NOMBRES.')
    for nombre, u in zip(NOMBRES, urls):
        base = u.rsplit('/', 1)[0]
        im = Image.open(io.BytesIO(bajar(base + '/1290x2796bb.png'))).convert('RGB')
        w = 900
        im.resize((w, round(im.size[1] * w / im.size[0])), Image.LANCZOS).save(
            f'{BANCO}/capturas/ficha-{nombre}-900.webp', quality=88, method=6)
        if nombre in CON_MOVIL_RECTO:
            m = recortar_movil(im)
            m.resize((800, round(m.size[1] * 800 / m.size[0])), Image.LANCZOS).save(
                f'{BANCO}/capturas/movil-{nombre}.webp', quality=90, method=6)
        print('ok', nombre)
    icono = bajar(info['artworkUrl512'].rsplit('/', 1)[0] + '/1024x1024bb.png')
    Image.open(io.BytesIO(icono)).convert('RGB').resize((512, 512), Image.LANCZOS).save(f'{BANCO}/marca/icono-app.png')
    print('ok icono')

if __name__ == '__main__':
    main()
