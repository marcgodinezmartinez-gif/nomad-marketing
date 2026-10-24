# El anuncio del lanzamiento (24-oct)

Un vídeo de **24,6 s**, 1080×1920, con la música y la voz dentro, que vale tal cual para el
reel, la historia y TikTok. Sale de lo que pidió el dueño al ver la idea de presentarse él
(«He hecho una app»): *«No me gusta la idea de promocionarla así. Quiero que lo montes tú de una
manera hiper profesional. Que le metas el audio y todo lo que sea necesario. Solo quiero
descargarlo y publicarlo.»*

Así que es un **anuncio de marca**: ni la cara, ni la voz, ni la primera persona del dueño.
**Y lleva audio**, por decisión suya, por encima de la regla de la casa de subir los reels sin
pista: al publicarlo **no se le añade música de Instagram ni de TikTok**.

Cómo se publica, con los pies listos para copiar: `PUBLICAR.md`.

## El guion, plano a plano

| Segundos | Imagen | Texto en pantalla | Audio |
|---|---|---|---|
| 0-7,5 | El Templo de Debod (foto quieta). En 2,4 sube la pantalla real de la audioguía de Debod (parada 5) | «TEMPLO DE DEBOD · MADRID» / «La ciudad, *contada.*». Tarjeta «Audioguía · Parada 5 · El Templo de Debod» con la frase de la voz, palabra a palabra | Kore, de 0,60 a 7,18: «Fue desmontado piedra a piedra, empaquetado en miles de cajas y transportado hasta este lugar.» La música entra suave por debajo |
| 7,5-14,4 | La torre de la Mezquita de Córdoba. La grabación real de la app: el tecleo (2,5 s), «Montando tus 3 días en Córdoba» (1,9 s) y el sábado escrito (2,5 s) | «CÓRDOBA · TRES DÍAS» / «Tú dices dónde.»; con «Montando» entra «*Nomad lo escribe.*» | La música sube a su nivel |
| 14,4-16,0 | Un correfoc. La pantalla «Qué hay esos días» | «Qué hay *esos días.*» | |
| 16,0-17,6 | Una calle del Gòtic. La pantalla de los gastos, cortada por encima de la tarjeta con el nombre | «Los gastos, *en paz.*» | |
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
- **La audioguía es la de Madrid, no la de Córdoba.** En `tours_cache` no hay ningún paseo de
  Córdoba (consultado el 24-oct: 0 filas con «rdoba»; el «Paseo por el Centro Histórico y la
  Judería» del plan nunca se generó). Debod sí, y es la única ciudad española con la pantalla
  real del tour en el banco (`banco/capturas/tourdebod-900.webp`) y el texto real detrás.
- **Las fotos, a sangre y quietas**, con una banda oscura detrás del texto: el dueño tiró el zoom
  a la foto el 6-oct (*«el zoom innecesario a la foto hace que se vea mal»*).
- **La tarjeta de la voz es la del reel de la Sagrada Família**, la que el dueño pidió y aprobó:
  blanco roto de la app, el verde de la app sólo en el icono que suena y en «Audioguía», y la
  frase en negro encendiéndose palabra a palabra con los tiempos de la propia voz. Es el subtítulo:
  dice exactamente lo que suena (transcrito, abajo).
- **Las pantallas, sin marco**: un rectángulo con esquinas de 44 y sombra. Nada de iPhone
  dibujado. Ninguna lleva barra de estado ni datos personales.
- **Los gastos, cortados por encima de la tarjeta negra**: ahí sale «Maria Paola te paga», el
  nombre de una persona real. Se ve el gasto del grupo y el balance, que es lo que se lee en 1,5 s.
- **Los cortes van en los tiempos de la música** (95,7 BPM, un tiempo = 0,627 s): 7,52 (compás
  3), 14,42, 15,99, 17,56 y el golpe en 20,0, que es donde entra el cierre.
- **Los destellos duran 1,57 s**, no 1,25: `hyperframes check` pide 1,27 s mínimos para leer un
  titular de cuatro palabras, y el tiempo salió del precio, que tenía de sobra.
- **Sin Veo.** La toma de apertura se iba a pedir a Veo desde la foto de Debod, y la API contestó
  el 24-oct que `veo-3.1-fast-generate-preview` ya no existe y que se use otro modelo con otra
  API. No se probó un modelo nuevo de coste desconocido para una sola toma: la foto quieta es lo
  que el dueño prefiere de todos modos. Coste de vídeo: 0.
- **Una sola versión para las tres superficies**: todo el texto entre y=300 e y=1400 y entre
  x=84 y x=900; las pantallas acaban en x=900 (la columna de botones de TikTok e Instagram) y en
  y≤1446; por debajo de 1460 no hay nada (adhesivo de enlace de la historia, pie de TikTok).
  Comprobado en `revision/zonas-seguras.jpg` de la entrega.

## La voz

- **El texto es el de la app**: `tours_cache` id `688ed389-e44e-40c7-b21f-76f077b987cb` (Madrid,
  «tour por el templo de debod y plaza de españa», 6 paradas), parada 5 «El Templo de Debod»,
  campo `main_explanation`, segundo párrafo, **palabra por palabra hasta «lugar»**. La frase
  entera sigue «…para volver a erigirse respetando su orientación original hacia el oeste» y
  duraba 12 s; se corta donde cierra el sentido para quedar en 6,6 s. La pantalla que sale es la
  de esa misma parada (la captura enseña el comienzo del primer párrafo).
- **La voz y el modelo son los de la app**: Kore con `gemini-3.1-flash-tts-preview` y el mismo
  prefijo de estilo que pone `narrate` en castellano (`supabase/functions/narrate/index.ts` del
  repo de la app, `STYLE.es`):
  `python3 piezas/ia/voz.py voz.wav Kore gemini-3.1-flash-tts-preview "Narra como una guía turística cercana y entusiasta, con naturalidad de conversación real, en español de España:` + dos saltos de línea + la frase`"`.
  Cuatro tomas; se queda la tercera (`assets/voz-kore.wav`), la más ceñida: habla de 0,31 a 6,89.
- **Comprobada transcribiéndola** con `faster-whisper` (modelo medium), sola, en la mezcla y en
  el máster: las tres veces sale «Fue desmontado piedra a piedra, empaquetado en miles de cajas
  y transportado hasta este lugar.», sin una palabra de más ni de menos.

## La música

`assets/musica-lyria.mp3`: **Lyria** (`lyria-3-clip-preview`) por la API de Gemini, con
`piezas/ia/musica.py` y el prompt de `musica-prompt.txt`. Instrumental, 26,96 s, 95,7 BPM, con
la marca de agua SynthID. Se pidieron tres; las tres ignoraron el «empieza vacío» del prompt,
y ésta es la que tiene el golpe más claro (un platillo con acorde a los 15,33 s) y una cola
larga para el cierre. Según los términos de la API de Gemini, Google no reclama la propiedad de
lo generado; no lleva derechos de terceros que Instagram o TikTok puedan reclamar, pero **es
música generada con IA y se etiqueta al publicar**.

`mezclar.sh` la monta así: empieza en el primer tiempo fuerte (0,28) y repite sus dos primeros
compases, para que el golpe caiga en el 20,0 del vídeo; debajo de Kore va a 0,18 (unos 15 dB
por debajo), sube a 0,62 al acabar la voz y a 0,85 en el golpe, y se apaga de 23,2 a 24,6.
Después, loudnorm en dos pasadas: **−14,0 LUFS integrados, −1,4 dBTP, LRA 2,7**.

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
| `fondo-cordoba.jpg` | `f-cordoba.jpg`, «Cordoba - Mezquita-Catedral 22» (Commons) | CC0 |
| `fondo-correfoc.jpg` | `f-merce-diable.jpg`, Ramon Perucho. Es un correfoc de Les Borges Blanques, no de la Mercè: fondo de ambiente, y el vídeo no dice dónde es | Pexels License |
| `fondo-gotic.jpg` | `f-bcn-festa.jpg`, Henrique Ferreira | Unsplash License |
| `pantalla-debod.png` | `banco/capturas/tourdebod-900.webp`, y 510-1435 | captura de la app |
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
