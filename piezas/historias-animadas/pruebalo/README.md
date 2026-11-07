# Pruébalo antes de pagar (7-nov)

Un vídeo de **30,83 s** (todo a 1,15×), 1080×1920, 30 fps, H.264 + AAC, **con la voz de Kore y la música
de «Un trazo»**, para Instagram (reel e historia) y TikTok. Cuenta lo que la app enseña de un viaje antes de pagarlo: la hoja con «Incluye», el
esqueleto del itinerario, las guías de muestra del paseo y del museo, NOMAD AI, y que si convence se paga
una vez y es para todo el grupo.

Lo que pidió el dueño (7-nov): primero «monta el vídeo ya, sin audio, y dame el guion», y esa noche, con
el vídeo visto, «métele la voz». Así que:

- **la voz y la música**: las ocho frases del guion, una toma de Kore por cada una, con la música de «Un
  trazo» debajo y la mezcla de «Así funciona» (abajo, «La voz» y «La música y la mezcla»). Los cortes
  salen de la voz. El vídeo sin sonido quedó en el commit `60bae2a`;
- **la estética de «Así funciona»**, idéntica (`../asi-funciona/`, que es el molde): el logo que se hace
  hilo y dibuja el borde de la pantalla, las tomas de la app dentro, los dibujos editoriales a la derecha
  que se trazan solos y respiran sin una línea que los una a la pantalla, el texto de abajo en dos líneas
  y el cierre de A y B;
- **ningún precio** en pantalla ni en el texto: el simulador enseña dólares y la casa no ancla el precio
  en nada que no sea el café.

Lo común (el motor de la línea, por qué no se dibuja un iPhone, cómo se cortan las tomas) está en
`../incluye-pago/README.md`; lo propio de la estética, en `../asi-funciona/README.md`. Cómo se publica,
con los pies listos para copiar: `PUBLICAR.md`.

Lleva las **tomas de verdad** (7-nov): la grabación del simulador con un fin de semana en Lisboa, del
sábado 7 al lunes 9 de noviembre de 2026 (abajo, «Las tomas»).

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

Los segundos son los del vídeo final. Los cortes salen de la voz, como en «Así funciona»: cada escena dura
su toma más 0,55 s (a 1×), y la frase empieza 0,25 s después del corte (la del cierre, 0,2). Dos
excepciones, a propósito: **S2 lleva 0,52 s más** (0,6 a 1×), porque en su primer segundo el hilo aún está
cerrando el borde y la hoja necesita verse; y **el cierre dura lo de «Así funciona» (4,7 s)** y no lo de
su frase (2,6), porque el crédito tiene que poder leerse. Las frases son las del encargo, sin cambiar
ninguna.

| n | de-a (s) | abajo | a la derecha | toma (de qué grabación y qué segundos) | Kore dice |
|---|---|---|---|---|---|
| 1 | 0-2,63 | ¿Pagar sin ver / qué te llevas? | el logo que se hace hilo y dibuja el borde | — | ¿Pagar un viaje sin ver lo que te llevas? |
| 2 | 2,63-6,56 | Antes de pagar, / ya ves tu viaje. | un ojo: se dibuja, mira a la pantalla cuando sube la hoja y parpadea | 3,46-4,90 `s2a`, hoja 31,30-40,50 (6,4×): el paso 1 del asistente, escribe «Lisboa», la elige y salen las fechas (07 nov – 09 nov · 2 noches); 4,90-6,56 `s2b`, hoja 56,48-58,14 (1×): la hoja con «Incluye» y sus flechas, el pie tapado; sube con «ya ves tu viaje» | Con Nomad, antes de pagar, ya ves tu viaje. |
| 3 | 6,56-12,15 | Tus días, / listos para escribirse. | el calendario de NOV 2026 con el sábado 7, el domingo 8 y el lunes 9, que brotan uno a uno | `s3`, itinerario 12,50-19,50 (1,25×): el mapa de Lisboa, «Sábado, 07 nov», los chips SÁB 7 · DOM 8 · LUN 9, las barras, «Se escribe en cuanto pagues» y la Torre de Belém; a las 11,06 pasa al domingo | Tus días, con sus fechas y tus imprescindibles, listos para escribirse. |
| 4 | 12,15-16,26 | La guía de tu paseo, / ya preparándose. | los auriculares, y sus ondas | `s4`, paseo 9,18-13,30 (1×): la muestra del paseo sube sobre la hoja (Torre de Belém, «Paseo por Belém…», «Escuchas 2 de sus 5 paradas», «Empezar la muestra») | La guía de tu paseo, preparándose mientras decides. |
| 5 | 16,26-19,26 | Y la de tu museo, / obra por obra. | un cuadro con su marco; el sol late con «obra por obra» | `s5`, museo 9,00-9,90 (**0,3×**): la muestra del museo con su esqueleto («Preparando las obras de la muestra») y las partes entrando hasta «Escuchas 2 de sus 5 obras» | Y la de tu museo, obra por obra. |
| 6 | 19,26-22,03 | NOMAD AI ya / conoce tu ciudad. | el robot pequeño; late la señal de su antena | `s6`, ia 7,78-10,54 (1×): NOMAD AI sube con «¿Qué no me puedo perder en Lisboa?» y los cuatro imprescindibles | Y NOMAD AI, que ya conoce tu ciudad. |
| 7 | 22,03-26,12 | Si te convence, / un solo pago. | tres personas sobre su línea: una se enciende con «una vez» y las otras dos con «todo el grupo» | `s7`, hoja 58,00-62,71 (1,15×): la hoja quieta, con los dos botones tapados y «Pago único para todo el grupo.» a la vista | Si te convence, lo pagas una vez y es para todo el grupo. |
| 8 | 26,12-30,83 | (el cierre) | | | Nomad. Descárgala gratis en la App Store. |

Los cortes (`T`, en `index.html`) están escritos a 1× y se estiran a 1/1,15 al final, como en «Así
funciona»: `T = [0, 0, 3.03, 7.54, 13.97, 18.70, 22.15, 25.33, 30.04]`, y el vídeo acaba en 925
fotogramas. **Si se mueve un corte, se mueve en `index.html`, en `EMPIEZA` de `mezclar.sh`, en
`tomas.json` y en los `<video>`** (los tiempos que imprime `cortar-tomas.py`). Los dos instantes atados a
palabras salen de la toma, con lo que whisper dice de cada palabra más 0,12 s, como `LLENA` en «Así
funciona»: el latido del sol en S5, con la primera «obra» (1,66 s dentro de v5), y las personas de S7
(`LLENA`), una con «una» (1,92 s dentro de v7) y las otras dos con «todo» (3,34), la tercera 0,15 s
detrás. Con «grupo» (3,84) no puede ser: la escena acaba 0,55 s después de la frase y las personas se
recogen en `T[8]` − 0,5, que es justo cuando se encendería.

**Dos dibujos son nuevos** y entran en el juego «editorial» (`iconos/editorial.json`): el **cuadro** de S5
(escena `cuadro`: 5 px el marco, que la línea dibuja empezando debajo del clavo y en sentido contrario al
reloj, como el calendario; 3 px el alambre, el paspartú, los montes y el sol; el clavo, relleno; de y 610 a
870) y el **ojo** de S2 (escena `ojo`, 7-nov: 5 px el contorno, que empieza en el lagrimal; 3 px el iris y
las tres pestañas; la pupila rellena con su brillo crema; de y 620 a 824). Los dos, centrados en y 740 como
los demás dibujos sueltos. **El ojo no estaba en el guion**: sin él la columna de la derecha se quedaba
vacía 4 s y, con la hoja quieta, la escena entera se paraba más de medio segundo. **El calendario** es el
de «Así funciona» con los días del viaje grabado, en una fila (sábado 7, lleno como el chip elegido del
itinerario; domingo 8 y lunes 9), y por eso su hoja es más baja. Los datos entran en `index.html` con
`iconos/datos.py`; a mano no se tocan.

## Las tomas

Salen de la grabación de `capturas/muestras.sh` del repo de la app del 7-nov: cinco bloques
(`recorrido-muestras-hoja`, `-itinerario`, `-paseo`, `-museo` e `-ia`), vídeos verticales de 1206×2622,
sin sonido, del simulador de iPhone. **No están en este repo** (es público; el metraje vive aparte,
`banco/metraje/README.md`), y las tomas cortadas tampoco (`*.mp4` está en `.gitignore`). `tomas.json` dice
qué trozo de qué grabación va en cada escena (`entrada`/`salida`, en segundos de la grabación), dónde
(`inicio`/`fin`, en segundos a 1×) y qué se tapa (`velos`); `cortar-tomas.py` corta cada trozo ya a su
velocidad, sin la isla ni la barra de inicio y a 404×806:

```bash
METRAJE=<carpeta con recorrido-muestras-*.mp4> python3 -I cortar-tomas.py     # escribe assets/tomas/*.mp4
```

| toma | grabación | entrada-salida (s) | velocidad | qué enseña |
|---|---|---|---|---|
| s2a | hoja | 31,30-40,50 | 6,4× | el paso 1 del asistente: escribe «Lisboa», la elige y salen las fechas |
| s2b | hoja | 56,48-58,14 | 1× | la hoja con «Incluye» y sus flechas, ya arriba |
| s3 | itinerario | 12,50-19,50 | 1,25× | el esqueleto del sábado 7, y el paso al domingo 8 |
| s4 | paseo | 9,18-13,30 | 1× | la muestra del paseo, subiendo |
| s5 | museo | 9,00-9,90 | 0,3× | la muestra del museo: esqueleto y partes entrando |
| s6 | ia | 7,78-10,54 | 1× | la conversación de NOMAD AI, subiendo |
| s7 | hoja | 58,00-62,71 | 1,15× | la hoja quieta con «Pago único para todo el grupo.» |

**Con la voz cambiaron los largos de las escenas, y las tomas con ellas (7-nov), sin enseñar nada nuevo.**
Las que acaban quietas se alargan o se acortan por su tramo quieto, que en la grabación no tiene ni un
fotograma: la hoja (de 56,7 a 67,2), el paseo (de 9,71 a más de 16) y NOMAD AI (de 8,25 a 15,69). El
itinerario lleva el mismo tramo, más despacio (1,25× y no 1,66×), y el museo la misma 0,3×, acabando en
9,90 y no en 9,97. `s2a` no cambia.

Lo que se miró al elegirlas, fotograma a fotograma (todas las grabaciones tienen fotogramas variables:
sólo hay fotograma cuando la pantalla cambia):

- **El código de invitación del viaje demo** sale en «Mis viajes», en la tarjeta de Lisboa (hoja, de
  55,65 a 56,45, mientras sube la hoja; y antes, en la portada). `s2b` empieza a las 56,48, con la hoja
  ya tapando la tarjeta entera; ninguna otra toma pasa por «Mis viajes» con la tarjeta a la vista.
- **El precio** sale en el botón de la hoja («Generar mi itinerario · $2.99») y en el pie del esqueleto.
  Las tomas del paseo y de NOMAD AI suben sobre la hoja: empiezan en el primer fotograma en que la hoja
  nueva ya tapa el botón (9,180 y 7,778; el anterior, 9,163 y 7,762, aún lo enseña). La del museo empieza
  con su hoja ya arriba (9,00).
- **El presupuesto del asistente** («€ Económico» en el paso 2 y «Moderado (€€)» en el resumen del paso 4)
  es un símbolo de moneda: por eso `s2a` es sólo el paso 1.
- **El paseo no se ve prepararse**: la muestra estaba hecha y sube entera (9,18-9,50). **El museo sí**,
  pero dura un suspiro: el esqueleto de 9,00 a 9,17 y las partes entrando de 9,17 a 9,33. Por eso `s5` va a
  0,3×: medio segundo de esqueleto y medio de partes entrando. Lo que la grabación tiene es eso; si el
  dueño quiere ver más tiempo el esqueleto que respira, hay que grabar el museo sin la muestra hecha.
- **Las grabaciones no dan la hora en su mp4**: llevan fotogramas B y un dts que no sigue al pts, y
  ffmpeg, al decodificar, se come los tramos quietos (en `muestras-paseo`, el cierre de la hoja de las
  25,2 s le salía a las 9,9). `cortar-tomas.py` las copia antes a `.mkv`, que guarda el pts; está
  explicado en su cabecera. **Para mirar una grabación, haz lo mismo** o los tiempos no casan con
  ffprobe.
- **El recorte**: la hora y la isla acaban en y 150 y la barra de inicio va de 2583 a 2597, así que se
  quitan 168 px de arriba y 48 de abajo, como en «Así funciona».

**El precio, tapado al cortar.** `velos` pinta, en píxeles de la grabación y con el color medido debajo,
lo que no puede verse: en la hoja, los dos botones del pie (y 2062-2450, `#FCFAF6`; en `s2b`, también la
nota, hasta 2574); en el esqueleto, todo el pie (y 2272-2574, `#F2EDE6`, el fondo del itinerario, desde
debajo de la última línea entera). Sin capa encima en la página: el velo cae exacto en cada fotograma.

## La voz

Kore, `gemini-3.1-flash-tts-preview` (`piezas/ia/voz.py`), con el estilo de A, B y «Así funciona»:
«Locuta un vídeo corto para redes, cercana y con energía tranquila, con naturalidad de conversación real, en
español de España; Nomad se pronuncia «nómad»:» (lo de antes de los dos puntos no se lee). En la de NOMAD
AI, la pista va también dentro del estilo, como en A: «…; Nomad se pronuncia «nómad», y NOMAD AI se
pronuncia «nómad ei ai»:». Una toma por frase, recortada con `../lanzamiento-trazo/recortar-voz.py` y
transcrita con faster-whisper (medium). **La primera toma de cada frase dice todas sus palabras** y
ninguna leyó el estilo. Sólo se repitió la de los días: en el audio final, a 1,15×, whisper oía «listos
para **in**scribirse» (en la toma a 1× oía bien «escribirse»), y además paraba 0,31 s entre «listos» y
«para». La segunda se oye «escribirse» a 1× y a 1,15× y no para ahí. Nueve llamadas al TTS.

| frase | toma | dura (1×) | lo que oye whisper |
|---|---|---|---|
| v1 | p1-1 | 2,48 s | «¿Pagar un viaje sin ver lo que te llevas?»; sube +10 semitonos al final: suena a pregunta |
| v2 | p2-1 | 3,36 s | «Con Nomad, antes de pagar, ya ves tu viaje.» |
| v3 | p3-2 | 5,88 s | «Tus días con sus fechas y tus imprescindibles, listos para escribirse.»; para en las dos comas (0,38 y 0,62 s) |
| v4 | p4-1 | 4,18 s | «La guía de tu paseo, preparándose mientras decides.» |
| v5 | p5-1 | 2,90 s | «Y la de tu museo, obra por obra.» |
| v6 | p6-1 | 2,63 s | «y no Madellay, que ya conoce tu ciudad.»: es «nómad ei ai», ligado (ver abajo) |
| v7 | p7-1 | 4,16 s | «Si te convence, lo pagas una vez y es para todo el grupo.» |
| v8 | p8-1 | 2,95 s | «Nomad. Descárgala gratis en la App Store.» |

**NOMAD AI**: whisper en castellano no conoce la marca y escribe «y no Madellay»; el trozo (de 0,3 a
1,45 s), transcrito en inglés, da «Nomade Yay», y con «NOMAD AI» como pista, «NOMAD AI». O sea, «nómad ei
ai» con la «d» ligada a la «ei». Es lo primero que hay que oír.

La voz se acelera a 1,15× con `atempo` y no con `rubberband`, por lo que cuenta «Así funciona» (decisión
del dueño, 30-oct). **Nadie la ha oído todavía**: lo decide el oído del dueño, en el altavoz del móvil y
con auriculares.

## La música y la mezcla

La de «Un trazo», con la cadena de «Así funciona» (`mezclar.sh`): la voz a −18 LUFS, la música a −33 y
apartándose cuando habla Kore, y todo a −16 LUFS lineal. Aquí la pista sobra (60,7 s para 35,5 a 1×), así
que **no hay junta**, como en la beta de Android: empieza **6 compases dentro** (24 negras justas,
19,220 s), con un fundido de entrada de 0,3 s. Así su último acorde (el 51,25 de la pista) cae en 32,03 a
1× (27,85 en el vídeo, medido en la pista de música), 1,7 s después del corte del cierre, con «gratis», y
la rejilla de negras de «Así funciona» vale tal cual para los latidos. En el 19,22 la pista no está en
ningún bajón. Con 7 compases el acorde caería en S7; con 5, en el último medio segundo del vídeo.

Medido: **−16,0 LUFS, pico −3,3 dBFS, LRA 2,0 LU** (en «Así funciona», −16,0, −3,5 y 1,7; en la beta,
−15,8, −3,7 y 1,8), loudnorm lineal, y las ocho frases enteras en la pista de voz. La pista tiene sus
bajones cortos de siempre; el más claro, medio segundo antes del último acorde. **Está medido, no oído.**

## Cómo se rehace

```bash
METRAJE=<carpeta> python3 -I cortar-tomas.py          # las tomas
python3 -I iconos/datos.py                            # los dibujos, de iconos/editorial.json
bash mezclar.sh                                       # assets/sonido.m4a, si cambian voz o tiempos
VERSIONES="historia reel limpia" bash variantes.sh <salida>   # los tres vídeos y revision/*.png
bash portada.sh <salida>/nomad-pruebalo-portada.jpg
```

`variantes.sh` es el de «Así funciona»: hace la mezcla si falta, pasa `hyperframes check` en cada versión
(avisa de la letra de 21 px del calendario, como allí), saca a `revision/` un fotograma por escena, dos del
arranque y uno del museo aún con su esqueleto, y el cierre con las zonas seguras dibujadas encima, y
renderiza. El máster lleva `assets/sonido.m4a` tal cual, sin recodificar. `piezas/ia/voz.py` busca
`ffmpeg` en `node_modules/ffmpeg-static/` (`npm install`, o un enlace al del sistema). `assets/motor.js`
es una copia del de «Así funciona», sin cambios; `silueta-del-logo.py`, también (comprueba `SILUETA` contra
el logo; necesita `scipy` y `contourpy`).

**Lo que se comprobó en el render final con la voz (7-nov)**, en las tres versiones: 30,83 s, 925
fotogramas, H.264 + AAC a 48 kHz, y la pista de sonido idéntica en las tres e idéntica a
`assets/sonido.m4a` (el mismo md5); `hyperframes check` pasa con el aviso de siempre (la letra del
calendario).

- **Cada frase en su escena.** Un fotograma en el arranque de cada frase, en una hoja de contactos: las
  siete primeras arrancan con su toma y su texto ya en pantalla (el corte va 0,25 s antes), y la del
  cierre con el cierre entrando.
- **Todas las palabras.** Whisper sobre el audio final de la historia: las ocho frases enteras, con
  «NOMAD AI» escrito «Nomad de Yay» (ver «La voz»).
- **El nivel**: −16,0 LUFS, pico verdadero −3,3 dBFS, LRA 2,0 LU, sin una muestra recortada (en «Así
  funciona», −16,0 y −3,5; en la beta, −15,8 y −3,7).
- **Ningún precio.** El detector de «$2.99» de la tanda sin voz (correlación con dos plantillas sacadas de
  la grabación; un fotograma sin tapar da 0,997), sobre la pantalla de cada fotograma: el máximo es 0,519
  (en el itinerario, a los 11,53 s), y ninguno pasa de 0,6 en ninguna versión. Sobre cada toma suelta,
  como mucho 0,506.
- **Ningún código de invitación ni QR**: ninguna toma enseña la tarjeta del viaje de «Mis viajes» (detrás
  de las hojas se ve la cabecera de «Mis viajes», como antes).
- **Nada quieto.** Con el detector de «Un trazo» (270×480 en grises, se mueve si algún píxel cambia más
  de 2 niveles): ningún tramo de 0,4 s o más en ninguna versión, ni mirando el fotograma entero ni sólo
  fuera de la pantalla. Con los cortes de la voz salían dos de 0,57 s, en S3 (la toma del itinerario,
  más lenta) y en S4 (el paseo, quieto): el calendario empieza a respirar antes y las ondas de los
  auriculares laten una vez más. El latido de más del sol (en `T[6]` − 1,08) se quitó: con la voz, el de
  «obra por obra» ya llena ese hueco y aquél lo pisaba (`gsap_tween_tail`).
- **Las zonas seguras**: la frase de abajo va de y 1291 a 1457 en todas las escenas (historia, 280-1500;
  reel, 230-1480). En la franja de los botones del reel (y 900-1480) los dibujos no pasan de x 811; más
  arriba, las ondas de los auriculares llegan a x 918 en el pico de su latido (y 793), fuera de esa franja.

## Lo que falta

- **Oírlo**: la voz y la mezcla están medidas, no oídas. Sobre todo «NOMAD AI» (v6), las dos pausas de la
  frase de los días (v3) y el final, con el último acorde. Si una frase suena mal, se regraba sólo ésa y se
  rehacen los cortes desde su duración.
- **Verlo en un móvil** antes de publicarlo: las tomas son pequeñas (404 px de ancho) y la hoja de `s2b` y
  `s7` lleva el pie en blanco donde estaban los botones.
