# Prepara la historia para buscar testers de Android (26-oct): copia la foto, el icono y gsap,
# recorta la pantalla del itinerario (sólo la castellana es real: ver PANTALLA) y escribe index.html en el idioma pedido
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

# La pantalla: el sábado del viaje a Roma (banco/capturas/plan-900.webp, 900 de ancho), del borde
# de la hoja (y=296, sin mapa ni barra de estado) a 25 px por debajo de la tarjeta del Coliseo con su
# «Iniciar tour» (y=890). La primera versión llegaba a la parada 2 y el gancho, que va encima del pie
# de la pantalla, tapaba la mitad de la tarjeta. Sin la barra de pestañas y sin datos de nadie: es un
# viaje de ejemplo. 620 de ancho.
#
# SÓLO EN CASTELLANO. La italiana del banco (plan-900-it.webp) NO es una captura: es la castellana con
# los textos sustituidos a mano y en otra fuente (una serif ancha en la fecha, una sans tipo Arial en la
# tarjeta y en «Inizia il tour», la píldora sin borde). La revisión del 26-oct lo vio junto al titular en
# Instrument Serif y se nota. Hasta que haya una captura hecha en un móvil con la app en italiano, la
# historia italiana va SIN pantalla (PANTALLA['it'] = None). Cuando la haya: ponerla aquí, ajustar CAJA si
# cambia la escala, y no retocarla.
CAJA = (0, 296, 900, 890)
ANCHO = 620
PANTALLA = {'es': 'plan-900.webp', 'it': None}
alto = None
for lang, src in PANTALLA.items():
    if not src:
        continue
    im = Image.open(f'{R}/banco/capturas/{src}').convert('RGB').crop(CAJA)
    im = im.resize((ANCHO, round(im.height * ANCHO / im.width)), Image.LANCZOS)
    im.save(f'{A}/pantalla-{lang}.png', optimize=True)
    alto = im.height
    print(f'pantalla-{lang}.png', im.size)
if os.path.exists(f'{A}/pantalla-it.png'):
    os.remove(f'{A}/pantalla-it.png')

# Los textos. Cada línea es su propio bloque (HyperFrames no admite <br>). Lo que va en menta es
# la tercera línea del título. El gancho legítimo es probarla antes de que salga en Android y generar
# los viajes gratis DURANTE la prueba (son testers con licencia); nada a cambio de reseñas, nada después.
# «antes de que salga» y no «antes que nadie»: está en la App Store desde el 19-oct y la cuenta lo
# anunció el 24. La marca dice sólo «ANDROID», para no repetir «prueba» tres veces en pantalla.
# «Toca» nombra el adhesivo con su texto exacto (PUBLICAR.md): si cambia uno, cambia el otro.
TEXTOS = {
    'es': dict(plataforma='Android', t1='¿Tienes Android?', t2='Prueba Nomad', t3='antes de que salga.',
               l1='Te escribe el viaje día a día', l2='y te lo cuenta con audioguías.',
               g1='Genera tus viajes gratis', g2='durante la prueba.', toca='Toca «Únete a la prueba»'),
    'it': dict(plataforma='Android', t1='Hai Android?', t2='Prova Nomad', t3='prima che esca.',
               l1='Ti prepara il viaggio giorno per giorno', l2='e te lo racconta con le audioguide.',
               g1='Genera i tuoi viaggi gratis', g2='durante il test.', toca='Tocca «Partecipa al test»'),
}
# Los tiempos: sin pantalla, el gancho y «Toca» no tienen que esperarla.
# rep_flecha: idas y vueltas de 0,5 s que caben hasta los 10 s.
TIEMPOS = {True: dict(t_gancho='3.2', t_toca='4.3', t_flecha='4.8', rep_flecha='9'),
           False: dict(t_gancho='2.1', t_toca='3.1', t_flecha='3.6', rep_flecha='11')}
plantilla = open(f'{P}/plantilla.html.in', encoding='utf-8').read()
LANG = sys.argv[1] if len(sys.argv) > 1 else 'es'
for lang, t in [(LANG, TEXTOS[LANG])]:
    html = plantilla.replace('<!-- PLANTILLA. No se renderiza: preparar.py escribe index.html con los textos del idioma que\n'
                             '     se le pida. Lo que se toca a mano es esto y la tabla TEXTOS de preparar.py. -->\n',
                             '<!-- GENERADO por preparar.py desde plantilla.html.in. No se edita a mano. -->\n')
    con_pantalla = bool(PANTALLA[lang])
    if not con_pantalla:
        a, b = html.index('<!-- PANTALLA -->'), html.index('<!-- /PANTALLA -->') + len('<!-- /PANTALLA -->')
        html = html[:a] + '<!-- Sin pantalla: no hay captura real en este idioma (preparar.py). -->' + html[b:]
    campos = dict(t, **TIEMPOS[con_pantalla], lang=lang, id=f'testers-android-{lang}',
                  pantalla=f'pantalla-{lang}.png', alto_pantalla=str(alto))
    for k, v in campos.items():
        html = html.replace('{{' + k + '}}', v)
    assert '{{' not in html, 'queda un hueco sin rellenar'
    open(f'{P}/index.html', 'w', encoding='utf-8').write(html)
    print('index.html', lang, 'con pantalla' if con_pantalla else 'SIN pantalla')
