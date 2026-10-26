# Prepara la historia para buscar testers de Android (26-oct): copia la foto, el icono y gsap,
# recorta la pantalla del itinerario de cada idioma y escribe index.html en el idioma pedido
# desde plantilla.html.in. HyperFrames admite UNA composición raíz por proyecto (con dos, `check`
# falla con multiple_root_compositions), así que el idioma se elige al preparar y render.sh los
# hace uno detrás de otro. El index.html versionado es el castellano.
#
# Uso, desde la raíz del repo de marketing:
#   python3 piezas/historias-animadas/testers-android/preparar.py [es|it]   (por defecto, es)
import os, shutil, sys
from PIL import Image

R = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
P = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(P, 'assets')
os.makedirs(A, exist_ok=True)

# La foto: el Coliseo al atardecer (banco/fotos/historia/f-portada.jpg, Commons, CC0), porque la
# pantalla es el día de Roma que empieza en el Coliseo. Quieta y a sangre.
shutil.copy(f'{R}/banco/fotos/historia/f-portada.jpg', f'{A}/fondo-coliseo.jpg')
shutil.copy(f'{R}/banco/marca/icono-app.png', f'{A}/icono-app.png')
shutil.copy(f'{R}/piezas/historias-animadas/plan-cordoba/assets/gsap.min.js', f'{A}/gsap.min.js')

# La pantalla: el sábado del viaje a Roma (banco/capturas/plan-900*.webp, 900 de ancho), del borde
# de la hoja (y=296, sin mapa ni barra de estado) a 25 px por debajo de la tarjeta del Coliseo con su
# «Iniciar tour» (y=890). La primera versión llegaba a la parada 2 y el gancho, que va encima del pie
# de la pantalla, tapaba la mitad de la tarjeta. Sin la barra de pestañas y sin datos de nadie: es un
# viaje de ejemplo. 620 de ancho.
CAJA = (0, 296, 900, 890)
ANCHO = 620
alto = None
for src, dst in [('plan-900.webp', 'pantalla-es.png'), ('plan-900-it.webp', 'pantalla-it.png')]:
    im = Image.open(f'{R}/banco/capturas/{src}').convert('RGB')
    if src.endswith('-it.webp'):
        # La italiana tiene, entre la estrella y «Colosseo», un resto de 4 px de la sustitución
        # del texto con la que se hizo la captura traducida (la española no lo tiene). Se pinta
        # con el blanco de la tarjeta de al lado. No toca ningún texto: la «C» empieza en x=344.
        fondo = im.getpixel((330, 648))
        for x in range(334, 342):
            for y in range(628, 668):
                im.putpixel((x, y), fondo)
    im = im.crop(CAJA)
    im = im.resize((ANCHO, round(im.height * ANCHO / im.width)), Image.LANCZOS)
    im.save(f'{A}/{dst}', optimize=True)
    alto = im.height
    print(dst, im.size)

# Los textos. Cada línea es su propio bloque (HyperFrames no admite <br>). Lo que va en menta es
# la tercera línea del título. El gancho legítimo es probarla antes que nadie y generar los viajes
# gratis DURANTE la prueba (son testers con licencia); nada a cambio de reseñas, nada después.
TEXTOS = {
    'es': dict(plataforma='Android · prueba', t1='¿Tienes Android?', t2='Prueba Nomad', t3='antes que nadie.',
               l1='Te escribe el viaje día a día', l2='y te lo cuenta con audioguías.',
               g1='Genera tus viajes gratis', g2='durante la prueba.', toca='Toca el enlace'),
    'it': dict(plataforma='Android · test', t1='Hai Android?', t2='Prova Nomad', t3='prima di tutti.',
               l1='Ti scrive il viaggio giorno per giorno', l2='e te lo racconta con le audioguide.',
               g1='Genera i tuoi viaggi gratis', g2='durante il test.', toca='Tocca il link'),
}
plantilla = open(f'{P}/plantilla.html.in', encoding='utf-8').read()
LANG = sys.argv[1] if len(sys.argv) > 1 else 'es'
for lang, t in [(LANG, TEXTOS[LANG])]:
    html = plantilla.replace('<!-- PLANTILLA. No se renderiza: preparar.py escribe index.html con los textos del idioma que\n'
                             '     se le pida. Lo que se toca a mano es esto y la tabla TEXTOS de preparar.py. -->\n',
                             '<!-- GENERADO por preparar.py desde plantilla.html.in. No se edita a mano. -->\n')
    campos = dict(t, lang=lang, id=f'testers-android-{lang}', pantalla=f'pantalla-{lang}.png', alto_pantalla=str(alto))
    for k, v in campos.items():
        html = html.replace('{{' + k + '}}', v)
    assert '{{' not in html, 'queda un hueco sin rellenar'
    open(f'{P}/index.html', 'w', encoding='utf-8').write(html)
    print('index.html', lang)
