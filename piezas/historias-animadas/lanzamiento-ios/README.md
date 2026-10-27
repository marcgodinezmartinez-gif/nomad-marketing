# El anuncio del lanzamiento (24-oct)

> **Rechazado por el dueño el 27-oct** (*«los recortes de la app se ven mal y reutilizamos vídeos de
> cosas ya anunciadas»*). No se publica: lo sustituye `../lanzamiento-trazo/`, que se queda con su
> cierre. Esto se guarda como registro y por lo que enseñó (la mezcla, la insignia, el cierre).

Un vídeo de **24,6 s**, 1080×1920, con la música y la voz dentro, que vale tal cual para el
reel, la historia y TikTok. Sale de lo que pidió el dueño al ver la idea de presentarse él
(«He hecho una app»): *«No me gusta la idea de promocionarla así. Quiero que lo montes tú de una
manera hiper profesional. Que le metas el audio y todo lo que sea necesario. Solo quiero
descargarlo y publicarlo.»*

Así que es un **anuncio de marca**: ni la cara, ni la voz, ni la primera persona del dueño.
**Y lleva audio**, por decisión suya, por encima de la regla de la casa de subir los reels sin
pista: al publicarlo **no se le añade música de Instagram ni de TikTok**. Si eso pasa a ser la
regla de los anuncios de marca, lo decide el dueño en #15.

Cómo se publica, con los pies listos para copiar: `PUBLICAR.md`.

## El guion, plano a plano

| Segundos | Imagen | Texto en pantalla | Audio |
|---|---|---|---|
| 0-7,5 | El Templo de Debod (foto quieta). En 2,4 sube desde fuera del cuadro la pantalla real de la audioguía de Debod (parada 5), opaca | Desde el fotograma 0: «TEMPLO DE DEBOD · MADRID» / «La ciudad, *contada.*» y la tarjeta con **el icono de la app y «Nomad»**, «Audioguía · un paseo de 6 paradas» y la frase de la voz, palabra a palabra | Kore, de 0,60 a 7,18: «Fue desmontado piedra a piedra, empaquetado en miles de cajas y transportado hasta este lugar.» La música entra suave por debajo |
| 7,5-14,4 | Corte seco a la torre de la Mezquita de Córdoba, desenfocada a propósito. La grabación real de la app: el tecleo (2,5 s), «Montando tus 3 días en Córdoba» (1,9 s) y el sábado escrito (2,5 s) | «CÓRDOBA · TRES DÍAS» / «Tú dices dónde.»; con «Montando» entra «*Nomad lo escribe.*» | La música sube a su nivel |
| 14,4-16,0 | Corte seco a un correfoc. La pantalla «Qué hay esos días» | «Qué hay *esos días.*» | |
| 16,0-17,6 | Corte seco a una calle del Gòtic. La pantalla de los gastos, cortada por encima de la leyenda «Tú 56 €» | «Los gastos, *en paz.*» | |
| 17,6-20,0 | Tinta | «Desde / 2,99 € / el viaje.» y, un compás después, «Sin suscripción.» | |
| 20,0-24,6 | El papel de la app | El icono, «Nomad: guía de viajes», la insignia oficial de la App Store y «Pronto en Android». Todo quieto desde 21,2 | El golpe de la música en 20,0, que se apaga hasta el final |

(En cursiva, lo que va en menta.)

## Las decisiones, y por qué

- **Abre con la audioguía y no con escribir el viaje**, al revés de la estructura de partida.
  `campana/MERCADO-2026-08-15.md`: *«el itinerario ya no es defendible: ChatGPT y Gemini lo
  regalan […] El gancho es el tour a pie»*. Una voz que cuenta un monumento en el primer segundo
  es lo que no da un chat, y es un gancho de sonido, que es lo que este vídeo tiene y los demás no.
  Escribir el viaje va segundo, como la prueba de que el viaje también lo hace.
- **Los titulares son los de las capturas de la ficha** («La ciudad, contada.», «Tú dices dónde.
  Nomad lo escribe.», «Qué hay esos días.», «Los gastos, en paz.»): los mismos que verá quien
  toque el enlace.
- **La audioguía es la de Madrid, no la de Córdoba** (#16). En `tours_cache` no hay ningún paseo de
  Córdoba (consultado el 24-oct: 0 filas con «rdoba»; el «Paseo por el Centro Histórico y la
  Judería» del plan nunca se generó). Debod sí, y es la única ciudad española con la pantalla
  real del tour en el banco (`banco/capturas/tourdebod-900.webp`) y el texto real detrás.
- **Las fotos, a sangre y quietas**, con una banda oscura detrás del texto: el dueño tiró el zoom
  a la foto el 6-oct (*«el zoom innecesario a la foto hace que se vea mal»*).
- **La tarjeta de la voz es la del reel de la Sagrada Família**, la que el dueño pidió y aprobó:
  blanco roto de la app, el verde de la app sólo en las barras que suenan y en el nombre, y la
  frase en negro encendiéndose palabra a palabra con los tiempos de la propia voz. Es el subtítulo:
  dice exactamente lo que suena (transcrito, abajo).
- **La marca, desde el fotograma 0** (revisión del 24-oct). La primera versión no decía «Nomad»
  hasta los 10 s, y quien pasa un reel a los 3 s veía un anuncio bonito sin saber de quién. Ahora
  la tarjeta lleva el icono de la app y «Nomad», y su segunda línea («Audioguía · un paseo de 6
  paradas») ya no repite el título y la parada que enseña la pantalla de debajo. El kicker, el
  título y la tarjeta están quietos desde el primer fotograma: es la portada por defecto de TikTok.
- **Los cortes, en seco, en el tiempo fuerte** (revisión del 24-oct). La primera versión fundía la
  foto nueva sobre la vieja y las pantallas entraban fundiéndose: durante unos fotogramas se veían
  dos fotos y dos tarjetas medio transparentes, y en los destellos la tarjeta era translúcida un
  37 % de su tiempo. Ahora todo lo de una escena desaparece en el mismo fotograma en que entra la
  foto de la siguiente, y las pantallas son opacas desde su primer fotograma: entran moviéndose
  (desde abajo, con `expo.out`), nunca fundiéndose.
- **Córdoba, desenfocada a propósito.** `f-cordoba.jpg` es la única foto de Córdoba del banco y es
  blanda (medido: un tercio del detalle fino de las otras tres, con bloques de JPEG y el cielo
  quemado). Nítida, al lado de Debod, el correfoc y el Gòtic, delataba el montaje. `preparar.py` la
  desenfoca (gaussiano de 16) y la baja un 14 %, y se lee como fondo de ambiente detrás de la
  pantalla. No se pudo traer una nítida: desde el contenedor Commons da 429 y Unsplash pide un reto
  de bots. Si el dueño baja una (CC0, Unsplash o Pexels, con su crédito en `creditos.json`), se
  cambia en `preparar.py` y se quita el desenfoque. Queda en #16.
- **«Tour guiado · gratis» en la tarjeta del sábado, aceptado a conciencia.** Es el texto de la app:
  lo que cuesta ESA actividad (el paseo no tiene entrada), dentro de un viaje que ya se ha pagado.
  No se tapa ni se retoca una pantalla real, y el «gratis» que la casa reserva para «descargarla»
  es el de los textos que escribimos nosotros, no el de la interfaz.
- **Las pantallas, sin marco**: un rectángulo con esquinas de 44 y sombra. Nada de iPhone
  dibujado. Ninguna lleva barra de estado ni datos personales.
- **Los gastos, cortados por encima de la tarjeta negra**: ahí sale «Maria Paola te paga», el
  nombre de una persona real. Se ve el gasto del grupo y el balance, que es lo que se lee en 1,5 s.
- **Los cortes van en los tiempos de la música** (95,7 BPM, un tiempo = 0,627 s): 7,52 (compás
  3), 14,42, 15,99, 17,56 y el golpe en 20,0, que es donde entra el cierre.
- **Los destellos duran 1,57 s**, no 1,25: `hyperframes check` pide 1,27 s mínimos para leer un
  titular de cuatro palabras, y el tiempo salió del precio, que tenía de sobra.
- **Sin Veo.** La toma de apertura se iba a pedir a Veo desde la foto de Debod (el modelo rápido
  que usó `VEO.md`), y la API contestó el 24-oct que ese modelo ya no existe y que se use otro con
  otra API. No se probó un modelo nuevo de coste desconocido para una sola toma: la foto quieta es lo
  que el dueño prefiere de todos modos. Coste de vídeo: 0.
- **Una sola versión para las tres superficies**: todo el texto entre y=300 e y=1400 y entre
  x=84 y x=900; las pantallas acaban en x=900 (la columna de botones de TikTok e Instagram) y en
  y≤1396 (la de Debod; «Descargar el audio · Para oírlo sin cobertura» entra entera, con su
  recuadro, por encima de 1400); por debajo de 1460 no hay nada (adhesivo de enlace de la
  historia, pie de TikTok).
- **Los recortes de la grabación** (`preparar.py`, revisión del 24-oct): el tecleo empieza en y=295
  de la fuente y acaba en 1034; el sábado empieza en 252, con la cabecera «Sábado, 10 oct» con
  aire y el «+» entero.
- **Las burbujas de tecla del teclado de iOS**: recortar no bastaba. El cuerpo blanco asoma en
  y≥1050, pero su parte tenue empieza en y≈1000 y su sombra en y≈970 (medido contra el fotograma
  250 con umbral 3, en los nueve fotogramas con burbuja: 251, 255, 266, 270, 276, 282, 299, 301 y
  304). Como la franja 965-1034 no cambia en ningún otro fotograma, `preparar.py` la tapa entera con
  la del 250, que está limpia. Comprobado en los fotogramas de 8,20 y 9,23 s del máster.
- **Los gastos, hasta la barra**: debajo va «• Tú 56 €», el redondeo de la leyenda de la app, que
  al lado de «Gasto del grupo 55,99 €» parecía una cuenta mal hecha.
  Comprobado en `revision/zonas-seguras.jpg` de la entrega.

## La voz

- **El texto es el de la app**: `tours_cache` id `688ed389-e44e-40c7-b21f-76f077b987cb` (Madrid,
  «tour por el templo de debod y plaza de españa», 6 paradas), parada 5 «El Templo de Debod»,
  campo `main_explanation`, segundo párrafo, **palabra por palabra hasta «lugar»**. La frase
  entera sigue «…para volver a erigirse respetando su orientación original hacia el oeste» y
  duraba 12 s; se corta donde cierra el sentido para quedar en 6,6 s. La pantalla que sale es la
  de esa misma parada (la captura enseña el comienzo del primer párrafo).
- **La voz y el modelo son los de la app**: Kore, una de las voces que se eligen en la app (la de
  por defecto es la del sistema del teléfono), con el modelo de `TTS_MODEL` y el mismo prefijo de
  estilo que pone `narrate` en castellano (`supabase/functions/narrate/index.ts` del repo de la
  app, `STYLE.es`):
  `python3 piezas/ia/voz.py voz.wav Kore "$(grep -oP 'TTS_MODEL = "\K[^"]+' /home/user/NOMAD/supabase/functions/narrate/index.ts)" "Narra como una guía turística cercana y entusiasta, con naturalidad de conversación real, en español de España:` + dos saltos de línea + la frase`"`.
  Cuatro tomas; se queda la tercera (`assets/voz-kore.wav`), la más ceñida: habla de 0,31 a 6,89.
- **Comprobada transcribiéndola** con `faster-whisper` (modelo medium), sola, en la mezcla y en
  el máster: las tres veces sale «Fue desmontado piedra a piedra, empaquetado en miles de cajas
  y transportado hasta este lugar.», sin una palabra de más ni de menos.
- **Los subtítulos, con el arranque de cada palabra** (revisión del 24-oct). El `data-t` de cada
  palabra es cuándo EMPIEZA en la mezcla, y el encendido (0,14 s) arranca 0,07 s antes, para que
  su punto medio caiga ahí. La primera versión tenía «cajas» en 4,91, que es la /x/ de «-jas»: se
  encendía del todo 0,27 s después de empezar a sonar. Ahora «miles» 4,18, «cajas» 4,76 (el cierre
  de la /k/) y «transportado» 5,70; comprobado en los fotogramas del máster: «cajas» apagada a
  4,70, a medias a 4,77 y encendida a 4,83.

## La música

`assets/musica-lyria.mp3`: **Lyria**, su modelo de clips, por la API de Gemini, con
`piezas/ia/musica.py` y el prompt de `musica-prompt.txt`. Instrumental, 26,96 s, 95,7 BPM, con
la marca de agua SynthID. Se pidieron tres; las tres ignoraron el «empieza vacío» del prompt,
y ésta es la que tiene el golpe más claro (un platillo con acorde a los 15,33 s) y una cola
larga para el cierre. Según los términos de la API de Gemini, Google no reclama la propiedad de
lo generado; no lleva derechos de terceros que Instagram o TikTok puedan reclamar, pero **es
música generada con IA y se etiqueta al publicar**.

`mezclar.sh` la monta así: empieza en el primer tiempo fuerte (0,28) y repite sus dos primeros
compases, para que el golpe caiga en el 20,0 del vídeo; debajo de Kore va a 0,18 (unos 15 dB
por debajo), sube a 0,62 al acabar la voz y a 0,85 en el golpe, y se apaga de 23,2 a 24,6.
Después, un limitador (`alimiter` a 0,72, unos −2,9 dBFS de pico de muestra) y loudnorm en dos
pasadas, **lineal**: una sola ganancia fija (+0,3 dB), que deja la mezcla como está escrita.
Resultado medido en el máster: **−13,8 LUFS integrados, pico verdadero −2,5 dBTP, LRA 2,8**.

**Y el loudnorm de la primera versión no era lineal, aunque lo pedía** (revisión del 24-oct). Con
`linear=true`, si la ganancia deja el pico verdadero por encima del objetivo (−1,5), loudnorm se
pasa al modo dinámico sin avisar: la mezcla tenía el pico en −0,49 dBTP, y la ganancia iba de
−1,17 dB debajo de la voz a +0,46 en la música, o sea que el ducking quedaba 1,6 dB más corto de lo
escrito. Ahora `mezclar.sh` lee `normalization_type` de la segunda pasada y **se para si no dice
`linear`**.

## Para rehacerla

```bash
python3 piezas/historias-animadas/lanzamiento-ios/preparar.py   # fotos, pantallas y escribir.mp4
bash piezas/historias-animadas/construir.sh                      # las fuentes embebidas
bash piezas/historias-animadas/lanzamiento-ios/mezclar.sh        # assets/sonido.m4a
cd piezas/historias-animadas/lanzamiento-ios
npx hyperframes check                                            # 0 errores, 0 avisos, 27/27 contraste
npx hyperframes render --video-bitrate 12M --video-frame-format png \
  --output ../../../salida/lanzamiento-render.mp4                 # ~1 min 10 s
cd ../../.. && ffmpeg -i salida/lanzamiento-render.mp4 \
  -i piezas/historias-animadas/lanzamiento-ios/assets/sonido.m4a \
  -map 0:v:0 -map 1:a:0 -c:v copy -c:a copy -movflags +faststart \
  salida/nomad-lanzamiento-1080x1920.mp4                          # el máster
bash piezas/historias-animadas/lanzamiento-ios/portada.sh salida/nomad-lanzamiento-portada.jpg
```

El render ya lleva el sonido (el `<audio>` de `index.html`, para que la vista previa suene); el
último paso lo vuelve a poner desde `sonido.m4a` sin recodificar, para que el máster lleve
exactamente la mezcla medida. `escribir.mp4` no se versiona (`*.mp4`): `preparar.py` lo rehace en
un segundo de `plan-cordoba/assets/pantalla.mp4`. `preparar.py` necesita el repo de la app sólo
para volver a recortar eventos y gastos; los recortes están versionados.

## De dónde sale cada cosa

| Recurso | Origen | Licencia |
|---|---|---|
| `fondo-debod.jpg` | `banco/fotos/historia/f-debod-nubes.jpg`, Arthur Hinton | Unsplash License |
| `fondo-cordoba.jpg` | `f-cordoba.jpg`, «Cordoba - Mezquita-Catedral 22» (Commons), desenfocada en `preparar.py` | CC0 |
| `fondo-correfoc.jpg` | `f-merce-diable.jpg`, Ramon Perucho. Es un correfoc de Les Borges Blanques, no de la Mercè: fondo de ambiente, y el vídeo no dice dónde es | Pexels License |
| `fondo-gotic.jpg` | `f-bcn-festa.jpg`, Henrique Ferreira | Unsplash License |
| `pantalla-debod.png` | `banco/capturas/tourdebod-900.webp`, y 600-1470 | captura de la app |
| `pantalla-eventos.png`, `pantalla-gastos.png` | capturas en bruto del iPhone del dueño, `docs/tienda/capturas/piezas/` del repo de la app | captura de la app |
| `escribir.mp4` | `plan-cordoba/assets/pantalla.mp4`, fotogramas 250-324, 461-517 y 536-610 (el 611 es el domingo con el Palacio de Viana mal puesto; antes del 461, el resumen con el nombre del viaje) | grabación de la app |
| `icono-app.png` | `banco/marca/` | propio |
| `insignia-app-store-es.svg` | `banco/marca/` = `web/insignias/app-store-es.svg` de la app | insignia oficial de Apple, sin tocar, ≥ 40 px (aquí 120), sólo en el cierre |
| `voz-kore.wav` | Gemini TTS, voz Kore | generada con IA |
| `musica-lyria.mp3` | Lyria | generada con IA |
| Fuentes | Instrument Serif e Instrument Sans, `banco/fuentes/webfonts/` | OFL |
| `gsap.min.js` | copia de `plan-cordoba/assets/` | licencia de GSAP |

## Lo que no está, a propósito

«Voz real», «de verdad», «tiempo real», la audioguía de 6 €, «Llega en octubre», la lista de
espera, el 1,99 € y cualquier fecha de Android. Tampoco los idiomas ni el asistente: en 24 s
caben cinco ideas y ésas son las de la ficha.
