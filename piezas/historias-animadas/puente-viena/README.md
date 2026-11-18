# El puente en Viena (18-nov)

Un reel de **27,5 s**, 1080×1920, 30 fps, H.264 + AAC, con la voz de Kore y la música de «Un trazo». Cuenta el
puente de diciembre en Viena: los tres días del viaje listo de la app y los cinco mercadillos de Navidad que
quedan a la puerta de una parada. Acaba en una tarjeta para guardar, con los cinco y su horario.

Lo pidió el dueño el 18-nov: «hazlo todo tú, monta el vídeo, que únicamente tenga que subirlo a Instagram, toma
todas las decisiones, busca los mejores ganchos». Cómo se publica y el pie: `PUBLICAR.md`.

## Por qué es así

- **Es fotográfico, no la app en pantalla.** `VISION.md`: «un demo de producto no se guarda; un plan de viaje sí».
  El protagonista es el plan y la app llega en la tarjeta del final. Además no hay toma de «Viajes listos»: salió
  el 10-nov, después de la última pasada de capturas, y en el simulador cada tarjeta enseña «$2.99».
- **Fotos reales, a sangre y quietas.** Sin zoom (el dueño, 6-oct) y sin imágenes generadas. Son diez de Unsplash
  (`assets/fotos/CREDITOS.md`).
- **Lleva el audio dentro.** Es la excepción a la regla de los reels sin pista (`AGENTS.md`), tomada con el encargo
  del dueño de decidirlo todo y de que sólo tenga que subirlo. Queda dicho en la issue de la pieza.
- **Sólo dice lo que se contrastó el 18-nov** con las webs oficiales: los sitios de cada día, los cinco mercadillos
  con su horario y que abren en el puente. No enseña horas del plan, restaurantes ni precios de entradas: el plan
  de la app tiene varios mal (NOMAD#468).

## El gancho

Un panel de cuatro guionistas con cuatro enfoques, un juez de retención y un revisor de hechos. Ganó el del
organizador («nadie ha mirado nada»), con el contador «Mercadillo n de 5» y los textos de cada día del segundo.
Después, dos rondas de revisión del corte montado cambiaron tres cosas:

- **«Dos semanas para el puente» pasó a «está al caer»**: la cifra caducaba según el día de publicación.
- **La voz dice lo mismo que el texto.** La primera decía «Spoiler: lo vas a organizar tú» sobre otro texto, y tres
  revisores de cuatro lo leyeron como una contradicción.
- **Se abre con las lámparas del Graben, no con el arco del Ayuntamiento.** El mercadillo de la Rathausplatz no es
  uno de los cinco, y abrir con él confundía la cuenta. No sale en ninguna foto.

## Lo que el vídeo NO puede dar a entender

**Los mercadillos no vienen en el plan de la app.** Están a la puerta de cinco paradas, y eso lo ha mirado el
vídeo. Se dice en pantalla en el segundo 4 («Te los apuntamos aparte: no vienen en el plan.»), en la tarjeta del
final y en la segunda línea del pie. La primera versión sólo lo decía al final y en pequeño, y dos revisores la
pararon por eso.

## El guion

Los cortes salen de la voz (`tiempos.py` desde `voz.json`): cada frase empieza un hueco después de la anterior y
cada foto entra con la palabra que la nombra.

| de-a (s) | Kore dice | en pantalla | foto |
|---|---|---|---|
| 0-3,6 | El puente de diciembre está al caer y nadie ha mirado nada. | El puente de / diciembre está al caer / y nadie ha mirado nada. | el Graben; desde el 1,8, la torre de la Catedral |
| 3,6-6,5 | Viena, tres días, ya organizada. | Viena, 3 días, / ya organizada. · «+ 5 mercadillos a la puerta de sus paradas» · «Te los apuntamos aparte: no vienen en el plan.» | la estrella del mercadillo de Schönbrunn |
| 6,5-10,8 | Día uno: el centro y la Catedral, con su mercadillo. | DÍA 1 · El centro, la Catedral / y el Graben · Mercadillo 1 de 5 · En la plaza de la Catedral · de 11 a 21 h | el Kohlmarkt; después, la Catedral con los puestos |
| 10,8-14,9 | Día dos: el Hofburg y el museo, con otro delante. | DÍA 2 · Hofburg, museo / y Naschmarkt · Mercadillo 2 de 5 · Entre dos museos · hasta las 21 h | el Hofburg; después, un puesto ante uno de los museos |
| 14,9-18,0 | Día tres: Schönbrunn y su mercadillo. | DÍA 3 · Schönbrunn · Mercadillo 3 de 5 · En el patio del palacio · de 10 a 21 h | Schönbrunn con su árbol |
| 18,0-20,1 | El Belvedere y el suyo. | Belvedere · Mercadillo 4 de 5 · En el parque del palacio · hasta las 21 h | el Belvedere de noche |
| 20,1-22,0 | Y Karlsplatz, el último. | Karlsplatz · Mercadillo 5 de 5 · Art Advent · de 12 a 20 h | la Karlskirche con nieve |
| 22,0-27,5 | El viaje ya está hecho en Nomad. Mándaselo al grupo, anda. | la tarjeta: los cinco con su horario, que no vienen en el plan, la app, el precio | papel crema |

La portada: «Puente de / diciembre en Viena / 3 días y 5 mercadillos a la puerta.», sobre Schönbrunn.

## La voz

Kore, `gemini-3.1-flash-tts-preview` (`piezas/ia/voz.py`), a 1,15× con `atempo`. Cada toma se transcribió con
Gemini y con faster-whisper (modelo `small`, que además da el tiempo de cada palabra). Lo que pasó:

- **«Respira.» salió como un suspiro**, no como la palabra. Se cambió el texto.
- **Una toma del día 3 se inventó el final** («con camino propio» por «con el suyo»). Se descartó.
- **«Mándaselo al grupo.» sonó a pregunta en dos tomas de dos.** Con «, anda» suena a lo que es.
- **El día 3 son tres tomas** (una por palacio) y no una: en una sola frase, «Belvedere» duraba un segundo en
  pantalla y no daba tiempo a leer su horario.

Treinta y cinco llamadas al sintetizador en total, doce de ellas perdidas por un fallo del guion que las lanzaba:
el recortador llamaba a ffmpeg sin `-nostdin` dentro de un `while read`, y ffmpeg se comía la lista de frases.

## Cómo se rehace

```bash
bash ../construir.sh                                  # las fuentes embebidas (assets/fuentes.css)
python3 tiempos.py                                    # assets/tiempos.js, desde voz.json
bash mezclar.sh                                       # assets/sonido.m4a: voz y música
node render.mjs <salida>/mudo-reel.mp4 reel           # el vídeo, sin sonido; también «limpia»
ffmpeg -i <salida>/mudo-reel.mp4 -i assets/sonido.m4a -c copy -shortest <salida>/nomad-puente-viena-reel-1080x1920.mp4
node render.mjs --portada <salida>/nomad-puente-viena-portada.jpg
node render.mjs --fotogramas <carpeta> 0 5.6 9.9 24.2  # fotogramas sueltos, para revisar
```

`render.mjs` pinta con Playwright, fotograma a fotograma, llamando a `seek(t)`: no usa HyperFrames. `voz.py` busca
`ffmpeg` en `node_modules/ffmpeg-static/` (`npm install`, o un enlace al del sistema).

## Lo que se comprobó en el render final

- 27,5 s, 825 fotogramas, 1080×1920, H.264 + AAC a 48 kHz.
- El sonido: −16,0 LUFS, pico −3,8 dBFS, LRA 1,4 LU, loudnorm lineal, y las ocho frases enteras, sin pisarse.
- Whisper, sobre el audio final: las ocho frases, en su sitio.
- Dos rondas de revisores independientes sobre fotogramas a tamaño real: hechos, ortografía y lectura, gancho y
  ritmo, reglas de la casa y licencias.

## Trampas de esta pieza

- **Un `set` en el segundo 0 de la línea de tiempo no pinta el fotograma 0.** Salía en negro. Lo que tiene que
  estar desde el principio va puesto en el HTML.
- **Una caja `absolute` se pinta encima de los bloques sin posicionar.** La sombra de detrás del texto tapaba el
  título del gancho, que era el único sin `transform`. Va con `z-index: -1` dentro de un bloque con `isolation`.
- **Un degradado radial más grande que su caja enseña el borde de la caja.** `closest-side`.

## Lo que falta

- **Oírlo** (`PUBLICAR.md`).
- **Meter las diez fotos en el banco**, en los dos tamaños y con su entrada en `creditos.json`.
- **Una versión de historia** con las flechas hacia el adhesivo: no se hizo.
