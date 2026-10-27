# Un trazo: el anuncio de que Nomad ya está en la App Store (27-oct)

Un vídeo de **17,5 s**, 1080×1920, 30 fps, H.264 + AAC, con la música dentro, para Instagram (reel e
historia) y TikTok. Sustituye al de `lanzamiento-ios/`, que el dueño rechazó el 27-oct: *«los
recortes de la app se ven mal y reutilizamos vídeos de cosas ya anunciadas»*. De aquel se queda lo
que le gustó, **el cierre**, con la insignia de la App Store; lo que abre la tienda es el adhesivo de
la historia o el enlace del perfil (la insignia, dentro de un vídeo, no se puede tocar).

El concepto lo eligió el dueño entre tres (está en el scratchpad de la sesión del 27-oct,
`anuncio-conceptos.json`, «Un trazo»): **una sola línea verde que no se levanta del papel cuenta el
anuncio entero**. Empieza como la onda de una audioguía que sigue sonando mientras la cobertura cae a
cero, dibuja la ruta de un viaje de tres días, se parte en cuatro (el grupo), subraya el precio y se
recoge en el icono de la app. Todo es tipografía y dibujo de marca sobre el papel de la app: **ni
pantallas, ni fotos, ni voz**. Nada sale de una pieza ya publicada. Todo va centrado en x=540, como
la portada y el cierre.

Cómo se publica, con los pies listos para copiar: `PUBLICAR.md`.

## Tres versiones, que sólo cambian en el cierre

| fichero (en `salida/`) | para | en el cierre, debajo del crédito de Apple |
|---|---|---|
| `nomad-trazo-historia-1080x1920.mp4` | historia de Instagram | dos chevrones finos que botan en cada tiempo, hasta el final, hacia la franja de y=1520-1700, que queda libre para el **adhesivo de enlace** |
| `nomad-trazo-reel-1080x1920.mp4` | reel de Instagram y TikTok | «Enlace en el perfil», en y=1256, justo debajo de Android, y la letra legal de Apple debajo (1324-1414) |
| `nomad-trazo-limpia-1080x1920.mp4` | TikTok sin el campo «Sitio web», o una historia promocionada | nada: el botón lo pone la plataforma |

La insignia dentro de un vídeo es una imagen: tocarla no hace nada en ninguna red. Lo que abre la
tienda es el adhesivo de la historia, el enlace de la bio o el botón de un anuncio (`PUBLICAR.md`).

## El guion, plano a plano

| Segundos | Imagen | Texto en pantalla | Sonido |
|---|---|---|---|
| 0-2,67 | **La señal cae.** Papel con una rejilla de puntos. Desde el fotograma 0: lo que anuncia el vídeo, el titular, cuatro barras de cobertura dibujadas aquí (no son los símbolos de iOS) y, debajo, la onda: una línea verde de 10 px con forma de voz (una campana simétrica que respira) que no para. Las barras se vacían de la más alta a la más baja en 0,34 / 0,65 / 0,96 / 1,28 (las corcheas de la música) y quedan como contorno; la onda no se entera | marca + «Ya en la App Store, para iPhone» (verde, 42 px) / «¿Sin cobertura?» / ▶ «Audioguía» | La música, desde su primer tiempo. Un «tic» por barra, cada uno más grave |
| 2,67-5,17 | **Y sigue sonando.** La misma escena; la onda late en las notas fuertes (2,68 / 3,46 / 4,09 / 4,87). La de 4,09 es la vuelta de la música después del respiro de 3,80-4,05 | «Sigue sonando.» (verde) y, en 2,98, «Las audioguías descargadas / suenan en modo avión.» (44 px) | Sólo música |
| 5,17-7,67 | **El viaje, de un trazo.** Se va todo en el mismo fotograma menos la marca y la onda. La onda sigue viva y se recoge desde la izquierda mientras, desde su punta derecha, la línea dibuja la ruta en tres tramos; cada tramo acaba en un día (5,65 / 6,28 / 6,90) y ahí brota el punto, encima del trazo. Arriba, un rótulo de salidas cambia de ciudad cada medio tiempo | «Lisboa» → «Nápoles» → «Bilbao» → «Sevilla» / «Viernes», «Sábado», «Domingo» / «Y el viaje, / escrito día a día.» | Un «tic» en cada día |
| 7,67-10,00 | **Para todo el grupo.** La ruta se recoge hacia el domingo y de ahí salen cuatro líneas paralelas, al 100 / 75 / 55 / 40 %; cada una baja hasta lo alto de la cabeza de su persona (cabeza y hombros, sin cara), que brotan en 8,15 / 8,46 / 8,78 / 9,09 | «Se paga una vez / y lo abre todo el grupo.» | Un «tic» suave por persona |
| 10,00-12,53 | **El precio, sobre papel.** Entra el bajo. Las cuatro líneas se convierten en una, el subrayado entero de la cifra (0,6 s), y los textos entran cuando ya han bajado | en 10,25 «Descargarla es gratis.» / 10,40 «El viaje, desde» / 10,63 «2,99 €» (verde, 220 px) / 10,94 «Sin suscripción.» | El bajo y un acento corto (re y la) que se oye en el móvil |
| 12,53-17,50 | **El cierre aprobado**, sobre crema. El subrayado se encoge hasta un punto en el centro del icono y de ahí nace el icono (12,73). El nombre (12,88); la insignia oficial, **entera de un fotograma a otro** (el 394, 13,13 s), sin fundido, y quieta hasta el final; «Pronto en Android» (13,33); el crédito de Apple (13,53); y lo de cada versión. Desde 13,78, el icono late en cada tiempo hasta el final (y en la historia, los chevrones con él): ningún fotograma se repite | «Nomad: guía de viajes» / [«Consíguelo en el App Store»] / «Pronto en Android» / sólo en el reel: «Enlace en el perfil» / «Apple, el logotipo de Apple e iPhone son marcas comerciales de Apple Inc., registradas en EE. UU. y en otros países. App Store es una marca de servicio de Apple Inc.» | El golpe en 12,53, con un acorde de re mayor encima; la música se apaga hasta 16,7 y el acorde hasta 17,4 |

## Lo que cambió respecto al guion del concepto, y por qué

**Después de la revisión del 27-oct** (tres revisores: diseño, verdad y sonido):

- **Los puntos de los días y el grupo se escalaban desde otro sitio.** El `transformOrigin` iba sólo
  en el estado final del `fromTo`, GSAP lo compensaba con una traslación del tamaño del radio, y los
  puntos quedaban 15 px arriba a la izquierda del trazo; los cuatro círculos del grupo, 28 px, así
  que cada línea llegaba a su borde derecho y se leían como cuatro notas musicales. Ahora el origen
  se fija una vez, con `svgOrigin`, antes de ninguna escala, y las personas son cabeza y hombros.
- **«Descargarla es gratis.» salía tachada 4 fotogramas** (la barra de arriba del peine la cruzaba):
  ahora entra en 10,25, cuando las líneas ya han bajado. Y las cuatro líneas se convierten
  directamente en el subrayado entero; antes se quedaban en un guion suelto de 40 px.
- **«Sin suscripción.» se veía 1,2 s**: ahora entra en 10,94 (1,6 s). La aclaración del modo avión
  entra en 2,98 (2,2 s), a 44 px y más oscura.
- **Lo que anuncia el vídeo era el texto más pequeño** («Nomad · ya disponible para iPhone», 30 px
  al 82 %). Ahora es el de la portada, «Ya en la App Store, para iPhone», en verde y a 42 px.
- **Un solo eje.** Hasta el precio iba todo a la izquierda (x=84) y de ahí en adelante centrado: en
  10,0 todo saltaba de columna. Ahora va todo centrado, como la portada.
- **La onda parecía un electrocardiograma** (una V honda y picos sueltos) y se aplanaba en 5,0-5,3,
  justo después de «Sigue sonando»: una línea plana dice «se ha parado». Ahora es una campana
  simétrica por dos senos, y sigue viva mientras se recoge.
- **Los cortes caían 5 fotogramas antes de la música** (ver «La música»): ahora van en 2,67, 5,17 y
  7,67, y los «tic», en las corcheas.
- **El final eran 3,4 s del mismo fotograma** con la música casi apagada: en Reels y TikTok parece un
  vídeo atascado. Ahora el icono late en cada tiempo hasta el final.
- **En el reel, «Enlace en el perfil» iba debajo de la letra legal**, a 300 px de la insignia: ahora
  va justo debajo de Android, y la letra legal al final, como pide Apple. Así además queda lejos de
  la franja de abajo que tapa el pie en TikTok.

**De la primera versión:**

- **El cierre empieza en 12,53 y no en 12,50**: es donde está el golpe de la música, medido.
- **Las personas llegan en 8,15 / 8,46 / 8,78 / 9,09**, no en 7,50 / 8,13 / 8,75 / 9,38: una línea
  no puede llegar a su persona en el mismo instante en que sale, y cada corchea hace cascada.
- **La línea es una sola de verdad**: la cola de la onda se recoge mientras se dibuja la ruta, y la
  ruta se recoge hacia el domingo mientras salen las cuatro. Sin eso se quedaban dibujos encima de
  dibujos, y la idea es una línea que avanza.
- **La ruta va en tres tramos** que acaban cada uno en su día: el punto brota cuando llega la punta,
  en el tiempo de la música, con su «tic». Con una sola curva y una curva de velocidad, los puntos
  caían donde quisiera la curva.
- **Más grande que en el guion**: titular de 120, barras de 80 a 230, onda en y=1030. En la primera
  prueba todo cabía en la mitad de arriba y se veía pequeño.
- **El crédito de Apple, en 24 px y 720 de ancho** (no 22): a 23 se salía por la derecha, debajo de
  los botones de TikTok e Instagram (`revision/*-zonas.png`). Es letra legal, no de lectura, y por
  eso lleva `data-layout-ignore` (la puerta pide 28 px a lo que se lee).
- **Sin voz**, por encargo. El juez proponía meter la voz de la app debajo de la onda: no entra.

## Las frases, y dónde se comprobó que son ciertas (27-oct, en el código de la app)

Ninguna hubo que cambiarla.

- **«Las audioguías descargadas suenan en modo avión»** y **«Sigue sonando»**:
  `mobile/src/lib/offlineNarration.ts` guarda en el teléfono el audio de la voz de la nube, con el
  botón «Descargar el audio» (`SmartGuide.tsx`, `DescargaAudioRow`), que al acabar dice «Audio
  descargado: suena sin cobertura»; el reproductor lo lee del disco antes de ir a la red
  (`hooks/useTourNarration.ts`, `audioLocal`). El texto y las fotos del tour se guardan solos
  (`lib/offlineTours.ts`), y la voz del sistema no necesita red. La ficha dice lo mismo, palabra por
  palabra. El «descargadas» importa: el audio de la nube sólo suena sin cobertura si se ha bajado.
- **«Y el viaje, escrito día a día»**: `supabase/functions/gemini-search-travel/index.ts` escribe
  el itinerario por días (`itinerary.days`, `day_index`), con horas; la ficha: «Itinerario día a día».
- **«Se paga una vez y lo abre todo el grupo»**: `supabase/functions/unlock-trip/index.ts` escribe
  `trips.is_premium` una vez por viaje (`idx_purchases_trip` es único por viaje), y
  `_shared/premium.ts` (`getTripMembership`) da el viaje como pagado a todo miembro aceptado; en el
  móvil, cada miembro lee el mismo `trip.is_premium` (`SmartGuide.tsx`, `CopilotTab.tsx`). El muro
  de pago lo dice así: «Pago único para todo el grupo.» (`TripPaywall.tsx`).
- **«Descargarla es gratis»**: la ficha pública da `price 0.0`, «Gratis» (lookup del 27-oct).
- **«El viaje, desde 2,99 €»** y **«Sin suscripción»**: `mobile/src/utils/pricingTiers.ts` y
  `PRECIO_POR_TIER` de `unlock-trip`: 2,99 € de 1 a 3 días, 4,99 € de 4 a 7, 6,99 € de 8 a 30, por
  viaje; no hay ningún producto de suscripción. «Desde», porque un viaje largo cuesta más.
- **«Viernes, sábado, domingo»** con 2,99 €: la escapada de 1 a 3 días es la del precio de 2,99 €.
- **«Nomad: guía de viajes»**, **«Ya en la App Store, para iPhone»**: la ficha (`trackName`, iOS 15.1
  o superior). **«Pronto en Android»**: la regla de la casa, sin fecha; la pregunta de si es «pronto»
  o «en camino» sigue abierta en #13, y va dentro del vídeo.
- Las cuatro ciudades del rótulo son un rótulo: no dicen que haya algo especial de ellas en la app,
  y no salen en ninguna pieza anterior.

## Las normas de Apple para la insignia (developer.apple.com/app-store/marketing/guidelines)

- **La oficial para España**, `banco/marca/insignia-app-store-es.svg`, idéntica byte a byte a la de
  la web de la app (md5 `ebdcadff…`). En pantalla dice «Consíguelo en el App Store».
- **Una sola** en todo el vídeo (la portada no la lleva).
- **Quieta y sin animar**: no está en el 393, aparece entera en el 394 y no cambia hasta el final
  (comparada contra el 500, la diferencia máxima es de 3 niveles, que es el códec). Ni fundido, ni
  escala, ni nada que la pise: el icono que late está 240 px por encima.
- **120 px de alto** (el mínimo es 40) y **aire de más de un cuarto de su alto** (30 px): 88 hasta
  el nombre y 70 hasta «Pronto en Android».
- **El crédito de marcas al final del vídeo**, con Apple, el logotipo de Apple (la insignia lo
  lleva) e iPhone (sale en la línea de marca). Es la plantilla de Apple traducida por nosotros.
- **«iPhone» y «App Store» se escriben tal cual**: nada en mayúsculas.

## Las zonas seguras (AGENTS.md)

Todo centrado en x=540 y nada a la derecha de x=900 (la columna de los botones de TikTok e
Instagram). Medido en los 525 fotogramas de cada versión, con lo que se aparta del papel: la tinta va
de y=288 a y=1472 en la historia (lo más bajo son los chevrones; de 1500 para abajo no hay nada y la
franja 1520-1700 es la del adhesivo), a 1414 en el reel (dentro de 230-1480) y a 1405 en la limpia.
Comprobado también sobre los fotogramas con las zonas pintadas encima:
`revision/historia-6-el-cierre-zonas.png`, `revision/reel-6-el-cierre-zonas.png` y
`revision/limpia-6-el-cierre-zonas.png`.

## La música

`assets/musica-lyria.mp3`: **Lyria**, su modelo de clips (`lyria-3-clip-preview`), por la API de
Gemini, con `piezas/ia/musica.py` y `musica-prompt.txt`. Instrumental, con la marca de agua SynthID.
Se pidieron **tres tomas** (0,04 $ cada una, 0,12 $ en total, en la cuenta de Google del dueño) y se
eligió por lo que se mide, no de oído:

- **toma 1**: 28 s, el ritmo plano todo el rato, sin golpe, y se para en seco a los 17 s;
- **toma 2**: el golpe más claro (20,4 s, con una cola de 3 s), pero la banda se calla 1,1 s cada dos
  compases (−39 dB): en «Sigue sonando» la música se habría callado, que es justo lo contrario;
- **toma 3, la elegida**: continua, en **re mayor**, unos 96 BPM, con sólo un respiro de 0,25 s cada
  dos compases (en el vídeo, 3,80-4,05 y 8,80-9,05). A los **24,04 s** entra el bajo y cambia la
  sección; a los **26,57**, un compás después, el golpe (un re1, 37 Hz), y de ahí se apaga sola.

`mezclar.sh` empieza en el 14,04: el bajo cae en el **10,00** del vídeo (el precio) y el golpe en el
**12,53** (el cierre).

**Dónde cae la música, medido con librosa** (arranques por posición dentro del compás, y por bandas):
las notas van en una rejilla de semicorcheas que empieza en 0,025 s, y **la nota más fuerte de cada
compás cae en 0,18 + 2,5k** (2,68 / 5,18 / 7,68), en todas las bandas. La primera versión cortaba en
2,50 / 5,00 / 7,50, justo en el hueco de antes, 5 fotogramas pronto. Ahora los cortes van en el
fotograma 80, 155 y 230 (2,67 / 5,17 / 7,67), y los «tic» en las corcheas (0,025 + 0,3125k). El
10,00 y el 12,53 no se mueven: ahí el sonido es el bajo y el golpe mismos.

**El bajo y el golpe son subgrave, y el altavoz de un iPhone no los da.** En la primera mezcla, el
golpe tenía el 90 % de su energía por debajo de 62 Hz y, además, todo se bajaba 4,4 dB desde el 10,0
(decidido con LUFS, que cuentan el subgrave): con un paso alto a 200 Hz, que es más o menos lo que
suena en el móvil, el precio quedaba a −17,8 LUFS y los 2 s del cierre a −31,0, contra −14,5 de la
sección A. La música no golpeaba: se iba. Ahora, desde el 10,0:

- un paso alto a 30 Hz (quita también la continua de la sección B) y un estante de −7 dB por debajo
  de 120 Hz, con los medios a ganancia 1;
- un **acorde de re mayor** sintetizado en el 12,53 (re, fa#, la, del re4 al re6, con armónicos hasta
  unos 3 kHz y un chasquido brillante encima) y uno corto y suave (re y la) en el 10,00. Sin IA, como
  los «tic». Están en la tonalidad de la toma, medida con un cromagrama (re mayor, 0,79).

Medido en el máster, con el paso alto a 200 Hz: **sección A −14,9, precio −15,3, los 2 s del cierre
−16,6 LUFS** (todo a menos de 2 LU). Por encima de 300 Hz, el golpe pasa de bajar 7,3 dB a **subir
6,0**, y la entrada del bajo, de −5,3 a −0,7.

Y tres cosas menores que también se arreglaron: la sección A sonaba 2,3 dB más por la izquierda (venía
así de Lyria; se compensa sólo ahí, y ahora da +0,1); la cola se cortaba en seco en 16,73, donde se
acaba el fichero (el fundido acaba ahora en 16,70, y el del acorde en 17,40); y el respiro de 3,80-4,05,
que cae debajo de «Sigue sonando», no se puede quitar sin mover el golpe: la onda late en 4,09, que
es la vuelta de la música, para que la imagen la acompañe. **Que suene bien lo tiene que decir el
dueño con el altavoz del iPhone**: aquí sólo se ha medido.

Los «tic» se sintetizan con `aevalsrc` (un seno de 2 ms de ataque que se apaga). Después, un
limitador y loudnorm en dos pasadas, **lineal** (el script se para si no lo es). Medido en el
máster: **−14,0 LUFS, pico −2,5 dBFS, LRA 8,4**.

**Los tiempos no salen de `hyperframes beats`**: le dio 128 BPM con confianza baja, y no es. Salen de
librosa (95,7 BPM), de los arranques por bandas y de `hyperframes audio --only sections`, que sí
pone el cambio de sección en 24,065. Las tomas 1 y 2 quedaron en el scratchpad de la sesión y se van
con el contenedor: si el dueño prefiere otra música, se pide otra toma con el mismo prompt y se
vuelven a medir los tiempos (cambian `INICIO` de `mezclar.sh`, las constantes del principio del
`<script>` de `index.html` y los tiempos de los «tic»).

Según los términos de la API de Gemini, Google no reclama la propiedad de lo generado. **Es música
generada con IA y se etiqueta al publicar.**

## Para rehacerla

```bash
bash piezas/historias-animadas/construir.sh                       # las fuentes y mark.png
bash piezas/historias-animadas/lanzamiento-trazo/mezclar.sh       # assets/sonido.m4a
bash piezas/historias-animadas/lanzamiento-trazo/variantes.sh     # historia y reel, y revision/ (~2 min)
VERSIONES=limpia bash piezas/historias-animadas/lanzamiento-trazo/variantes.sh
bash piezas/historias-animadas/lanzamiento-trazo/portada.sh salida/nomad-trazo-portada.jpg
```

`variantes.sh` escribe la versión en `assets/version.js` antes de cada pasada (check, snapshot y
render leen el mismo `index.html`), para si `hyperframes check --at-transitions` no pasa, vuelve a
poner el sonido medido encima del render sin recodificar y pasa `hyperframes clean` (el disco va
justo). Al acabar deja `version.js` en «historia», que es la versionada. Los MP4 no se versionan.

Lo que hay que saber al tocar `index.html`:

- **La onda es una función del tiempo** calculada fotograma a fotograma antes de reproducir, y cada
  trozo es su propio `fromTo` del atributo `d`. HyperFrames salta a cada instante con los eventos
  apagados (`totalTime(t, true)`), así que un `onUpdate` no se llamaría y la vista previa y el render
  saldrían distintos.
- **GSAP interpola un trazado si los dos tienen los mismos números en el mismo orden**: así se
  convierten las cuatro líneas en el subrayado (`SUBRAYA`) y así se encoge el subrayado hasta el icono.
- **Un elemento SVG que se escala necesita su origen fijado antes** (`gsap.set(…, { svgOrigin })`).
  Si el `transformOrigin` va sólo en el estado final de un `fromTo`, GSAP compensa el cambio con una
  traslación y el elemento sale desplazado: así salieron los puntos de los días en la primera versión.
- Las ciudades del rótulo llevan `data-layout-ignore`: cambian cada medio tiempo a propósito, y la
  puerta pide 0,4 s para leer una palabra.

## De dónde sale cada cosa

| Recurso | Origen | Licencia |
|---|---|---|
| `icono-app.png`, `mark.png` | `banco/marca/` | propio |
| `insignia-app-store-es.svg` | `banco/marca/` = `web/insignias/app-store-es.svg` de la app = la de Apple para es-es | insignia oficial de Apple, sin tocar |
| `musica-lyria.mp3` | Lyria (toma 3 de 3) | generada con IA |
| `sonido.m4a` | `mezclar.sh`: la música y los tic sintetizados | — |
| Fuentes | Instrument Serif e Instrument Sans, `banco/fuentes/webfonts/` | OFL |
| `gsap.min.js` | copia de `lanzamiento-ios/assets/` (GSAP 3.14.2) | licencia de GSAP |
| Barras, onda, ruta, líneas, personas, chevrones | dibujados en el SVG de `index.html` | propio |
| «Tic» y los dos acentos (re mayor) | `mezclar.sh`, sintetizados con `aevalsrc` | propio |

## Lo que no está, a propósito

Capturas de la app, fotos, voz, la lista de espera, el 1,99 €, «voz real», «tiempo real», la
audioguía de 6 €, una fecha de Android, «gratis» fuera de «Descargarla es gratis», y «iPhone» o
«App Store» en mayúsculas. Tampoco el asistente, la cartelera ni los gastos: en 17 s caben cuatro
ideas, y son la audioguía sin cobertura, el viaje escrito, el grupo y el precio.

## Lo que queda por decidir o probar

- **Que el adhesivo y la bio abran la tienda en el iPhone del dueño** (en julio y agosto hubo quejas
  de que el navegador de Instagram no abría la App Store). `PUBLICAR.md`, «Antes de nada», que también
  dice qué enlace va en la bio de Instagram.
- **Si Android es «pronto» o «en camino»** (#13): va dentro del vídeo. Si cambia, se cambia el texto
  de `#c-android` y se vuelve a renderizar.
- **Que la música le guste**, escuchada en el altavoz del iPhone: está medida, no oída.
- **El `pt` para medir** (#14), con tres campañas: `ig-historia-anuncio`, `ig-bio` y `tt-bio` (los
  nombres de #13 y #14). Apple no enseña una campaña hasta que suma 5 primeras descargas.
- **Si va a la cuadrícula**: AGENTS.md dice que el feed es fotográfico, y éste es gráfico.
- **La regla del audio dentro** de los anuncios de marca (#15): éste lo lleva, como el anterior.
- **Que «Enlace en el perfil» no lo tape la interfaz de TikTok**: va en y=1256-1300, muy por encima de
  la franja que tapa el pie, pero ninguna sesión lo ha visto en un móvil.
- La ficha de la App Store dice «Audioguías con voz real», que es lo que la casa no dice: está en
  **NOMAD#426**, en el repo de la app.
