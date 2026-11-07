# Pruébalo antes de pagar (7-nov)

Un vídeo de **31,1 s** (todo a 1,15×), 1080×1920, 30 fps, H.264, **sin sonido**, para Instagram (reel e
historia) y TikTok. Cuenta lo que la app enseña de un viaje antes de pagarlo: la hoja con «Incluye», el
esqueleto del itinerario, las guías de muestra del paseo y del museo, NOMAD AI, y que si convence se paga
una vez y es para todo el grupo.

Lo que pidió el dueño (7-nov): «monta el vídeo ya, sin audio, y dame el guion». Así que:

- **sin audio**: ni voz ni música; el máster no lleva pista de sonido. Las frases del guion están para
  grabar la voz de Kore después, y los cortes ya salen de ellas;
- **la estética de «Así funciona»**, idéntica (`../asi-funciona/`, que es el molde): el logo que se hace
  hilo y dibuja el borde de la pantalla, las tomas de la app dentro, los dibujos editoriales a la derecha
  que se trazan solos y respiran sin una línea que los una a la pantalla, el texto de abajo en dos líneas
  y el cierre de A y B;
- **ningún precio** en pantalla ni en el texto: el simulador enseña dólares y la casa no ancla el precio
  en nada que no sea el café.

Lo común (el motor de la línea, por qué no se dibuja un iPhone, cómo se cortan las tomas) está en
`../incluye-pago/README.md`; lo propio de la estética, en `../asi-funciona/README.md`. Cómo se publica,
con los pies listos para copiar: `PUBLICAR.md`.

**Hoy lleva TOMAS PROVISIONALES** (el nombre de cada toma sobre el fondo de la app): la animación está
probada y renderizada, y falta meter las grabaciones de verdad (abajo, «Lo que falta»).

## Tres versiones y la portada

| fichero | para |
|---|---|
| `nomad-pruebalo-historia-1080x1920.mp4` | historia de Instagram: acaba en dos flechas hacia el adhesivo de enlace |
| `nomad-pruebalo-reel-1080x1920.mp4` | reel de Instagram y TikTok: acaba en «Enlace en el perfil» |
| `nomad-pruebalo-limpia-1080x1920.mp4` | TikTok sin «Sitio web», o una promoción pagada: sin flechas ni texto |
| `nomad-pruebalo-portada.jpg` | la portada del reel: el logo haciéndose hilo y «¿Pagar sin ver / qué te llevas?» |

El cierre es el de A y B: «Secuencias acortadas.» y el crédito de Apple, y «Pronto en Android™» con
«Android es una marca comercial de Google LLC.».

## El guion

Los segundos son los del vídeo final. Cada escena dura su frase leída a ritmo de Kore a 1,15× (unas
3 palabras por segundo) más 0,55 s de aire. Dos excepciones, a propósito: **S2 lleva 0,5 s más**,
porque en su primer segundo el hilo aún está cerrando el borde y la hoja necesita verse; y **el cierre
dura lo de «Así funciona» (4,7 s)** y no lo de su frase (2,9), porque el crédito tiene que poder
leerse. Las frases son las del encargo, sin cambiar ninguna.

| n | de-a (s) | abajo | a la derecha | toma | Kore diría |
|---|---|---|---|---|---|
| 1 | 0-3,57 | ¿Pagar sin ver / qué te llevas? | el logo que se hace hilo y dibuja el borde | — | ¿Pagar un viaje sin ver lo que te llevas? |
| 2 | 3,57-7,65 | Antes de pagar, / ya ves tu viaje. | nada: lo cuenta la pantalla | s2a, el asistente rápido; s2b, la hoja con «Incluye» y sus flechas verdes | Con Nomad, antes de pagar, ya ves tu viaje. |
| 3 | 7,65-11,87 | Tus días, / listos para escribirse. | el calendario, y sus días brotan uno a uno | s3, el esqueleto del itinerario | Tus días, con sus fechas y tus imprescindibles, listos para escribirse. |
| 4 | 11,87-15,09 | La guía de tu paseo, / ya preparándose. | los auriculares, y sus ondas | s4, la guía de muestra del paseo | La guía de tu paseo, preparándose mientras decides. |
| 5 | 15,09-18,30 | Y la de tu museo, / obra por obra. | un cuadro con su marco; el sol late con «obra por obra» | s5, la guía de muestra del museo | Y la de tu museo, obra por obra. |
| 6 | 18,30-21,52 | NOMAD AI ya / conoce tu ciudad. | el robot pequeño | s6, la conversación de NOMAD AI | Y NOMAD AI, que ya conoce tu ciudad. |
| 7 | 21,52-26,39 | Si te convence, / un solo pago. | tres personas sobre su línea: una se enciende con «lo pagas una vez» y las otras dos con «para todo el grupo» | s7, la hoja otra vez, con el precio tapado | Si te convence, lo pagas una vez y es para todo el grupo. |
| 8 | 26,39-31,10 | (el cierre) | | | Nomad. Descárgala gratis en la App Store. |

Los cortes (`T`, en `index.html`) están escritos a 1× y se estiran a 1/1,15 al final, como en «Así
funciona». **Si se mueve un corte, se mueve en `index.html`, en `tomas.json` y en los `<video>`** (los
tiempos que imprime `cortar-tomas.py`). Cuando se grabe la voz, cada frase empieza 0,25 s después de su
corte (la del cierre, 0,2), y los dos instantes atados a palabras se ajustan con la toma: el latido del
sol en S5 y las personas que se encienden en S7 (`LLENA`).

**El cuadro de S5 es nuevo** y entra en el juego «editorial» (`iconos/editorial.json`, escena
`cuadro`): 5 px el marco, que la línea dibuja empezando debajo del clavo y en sentido contrario al
reloj, como el calendario; 3 px el alambre, el paspartú, los montes y el sol; el clavo, relleno. Va de
y 610 a 870, centrado en 740 como los demás dibujos sueltos. Los datos entran en `index.html` con
`iconos/datos.py`, que es el de «Así funciona» con los dibujos de este vídeo; a mano no se tocan.

**La pantalla de S2 va sola**, como dice el guion: la columna de la derecha se queda vacía 4 s. Si en el
móvil se ve coja, lo fácil es centrar la pantalla en S2 y llevarla a la izquierda al empezar S3 (el
calendario tendría que empezar 0,3 s más tarde).

## Las tomas

Salen de la grabación de `capturas/muestras.sh` del repo de la app: cinco bloques, vídeos verticales de
1206×2622 a 60 fps, sin sonido. **No se commitean** (`*.mp4` está en `.gitignore`). `tomas.json` dice qué
trozo de qué grabación va en cada escena (`entrada`/`salida`, en segundos de la grabación) y dónde
(`inicio`/`fin`, en segundos a 1×); `cortar-tomas.py` corta cada trozo ya a su velocidad, sin la isla ni
la barra de inicio (168 px arriba y 48 abajo) y a 404×806:

```bash
METRAJE=<carpeta con muestras-*.mp4> python3 -I cortar-tomas.py     # escribe assets/tomas/*.mp4
python3 -I cortar-tomas.py --provisional                             # sin grabaciones: las de prueba
```

| toma | grabación | qué tiene que enseñar | a 1× | dura (s) |
|---|---|---|---|---|
| s2a | `muestras-hoja` | el asistente rápido: la ciudad, las fechas y «Crear» | 5,05-6,70 | 1,43 |
| s2b | `muestras-hoja` | la hoja sube con «Incluye» y sus flechas verdes | 6,70-8,80 | 1,83 |
| s3 | `muestras-itinerario` | el esqueleto: chips con fechas, mapa, barras y «Se escribe en cuanto pagues» | 8,80-13,65 | 4,22 |
| s4 | `muestras-paseo` | la guía de muestra del paseo: su esqueleto y las paradas entrando | 13,65-17,35 | 3,22 |
| s5 | `muestras-museo` | la guía de muestra del museo, obra por obra | 17,35-21,05 | 3,22 |
| s6 | `muestras-ia` | la conversación de NOMAD AI sobre su ciudad | 21,05-24,75 | 3,22 |
| s7 | `muestras-hoja` | la hoja otra vez, con el precio tapado | 24,75-30,35 | 4,87 |

**Los cortes de la grabación (`entrada`/`salida`) son una estimación** hecha antes de que existieran:
todas llevan `"revisar": true`. Al llegar se mira cada grabación a 10 fps, se eligen las ventanas (sin
código de invitación, sin un mapa cargando, quieta donde la escena necesita leerse), se mira el primer y
el último fotograma de cada toma, y se quita la marca.

**El precio, tapado.** La hoja lleva el precio en el botón fijo de abajo («Generar mi itinerario ·
$2.99»), así que en s2b y s7 el pie de la toma se funde con el fondo de la hoja (`.velo-precio`, como el
velo de la errata de «Así funciona»), y sólo mientras corre esa toma. La posición (y 690 de la toma) y el
color (`#FCFAF6`) son una estimación: las tomas provisionales de la hoja llevan un botón con «$2.99»
donde se espera, y en los fotogramas de revisión no se ve. Con la grabación de verdad se mide otra vez.

## Cómo se rehace

```bash
METRAJE=<carpeta> python3 -I cortar-tomas.py          # las tomas (o --provisional)
python3 -I iconos/datos.py                            # los dibujos, de iconos/editorial.json
VERSIONES="historia reel limpia" bash variantes.sh <salida>   # los tres vídeos y revision/*.png
bash portada.sh <salida>/nomad-pruebalo-portada.jpg
```

`variantes.sh` es el de «Así funciona» sin la mezcla: pasa `hyperframes check` en cada versión (avisa de
`film_silent`, que es lo pedido, y de la letra de 20 px del calendario, como allí), saca a `revision/` un
fotograma por escena más dos del arranque, y el cierre con las zonas seguras dibujadas encima, y
renderiza. El máster sale sin pista de audio (`ffmpeg -an`). `assets/motor.js` es una copia del de «Así
funciona», sin cambios; `silueta-del-logo.py`, también (comprueba `SILUETA` contra el logo; necesita
`scipy` y `contourpy`).

Los fotogramas de `revision/` de hoy son **con las tomas provisionales**: miran la animación, el texto,
las zonas seguras y el velo, no las pantallas.

**Lo que se comprobó en el render provisional (7-nov)**, en las tres versiones: 31,1 s, 933 fotogramas,
sólo pista de vídeo. Ningún dibujo toca la pantalla en ningún fotograma mirado, y la frase de abajo cabe
en las zonas seguras de la historia (280-1500) y del reel (230-1480). El botón con «$2.99» de las tomas
provisionales no asoma en ningún fotograma (contado píxel a píxel en la franja del botón). Con el detector
de «Un trazo» (270×480 en grises, se mueve si algún píxel cambia más de 2 niveles), mirando sólo fuera de
la toma: el arranque se quedaba quieto 0,43 s entre que entra la pregunta y la punta coge velocidad, y
ahora late «qué te llevas?» ahí; queda un tramo de 0,30 s en el cierre. En S2 lo único que se mueve es la
toma, que es lo que pide el guion.

## Lo que falta

- **Las grabaciones**: cortar las cinco con `cortar-tomas.py`, revisar las ventanas de `tomas.json` y
  quitar `revisar`. Comprobar en ellas que la isla y la barra de inicio caen donde en «Así funciona»
  (168 y 48 px); si no, se cambia el `crop`.
- **El velo del precio**, medido sobre s2b y s7: dónde cae el precio, el color de debajo, y que no se
  vea en ningún fotograma de las dos tomas. Si la hoja enseña el precio en otro sitio (arriba, o en
  «Antes $X»), un velo más.
- **El calendario de S3** es el de «Así funciona» (NOV 2026, del sábado 21 al sábado 28). Si el viaje
  grabado tiene otras fechas, se cambia en `iconos/editorial.json` (la cabecera y los ocho días, con su
  letra de la semana) y se vuelve a correr `datos.py`.
- **Volver a renderizar** las tres versiones y mirar los fotogramas con las tomas de verdad.
- **La voz**, cuando se pida: Kore, con el estilo y la cadena de «Así funciona» (`atempo`, no
  `rubberband`), una toma por frase del guion. Entonces vuelve el `<audio>` de `index.html`, `mezclar.sh`
  y el paso de `variantes.sh` que pone el sonido, y se ajustan `LLENA` (S7) y el latido del sol (S5) a
  sus palabras.
