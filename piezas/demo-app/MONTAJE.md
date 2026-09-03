# El montaje de la demo — la receta exacta (2-sep, revisada el 3-sep)

**Desde el 3-sep el reel es `piezas/historias-animadas/demo-reel/`**: la grabación de la
app dentro del móvil de la casa, sobre las fotos del grid con su velo y con los rótulos de
las destacadas. Lo decidió el dueño mirando el corte anterior al lado del grid: *«una cosa
tiene un estilo superelegante y esto parece un vídeo un poco cutre y mal hecho»*. Tenía
razón; «La capa de presentación», abajo, cuenta el porqué y la receta. **El corte del
metraje —qué segundo de qué grabación— es el mismo** y sigue en «Los cortes».

De 63 s de grabación en cuatro ficheros salen **23,2 s de app** y **28,0 s de reel** en
1080×1920, 30 fps y **sin pista de audio** (se elige dentro de Instagram, como los reels).
Tres ficheros de salida, los tres del mismo render:

| Fichero | Dur | Para qué |
|---|---|---|
| `demo-reel.mp4` | 28,0 s | el reel, entero |
| `demo-reel-historia-1.mp4` | 12,0 s | historia 1: el asistente y el plan (0 → 12,0 del reel) |
| `demo-reel-historia-2.mp4` | 15,0 s | historia 2: tour, museo y cierre (13,0 → 28,0) |

Las dos historias salen del reel cortado por sus capítulos: cada una cuenta algo entero
(pedir → plan; guiar → museo → precio) y ninguna pasa de 15 s. El adhesivo de enlace va
en las dos, de y=1520 abajo: ahí sólo hay la parte baja del móvil, que es teclado y
botonera.

## La capa de presentación (3-sep): la tarjeta de la casa, moviéndose

El reel es la tarjeta qe-2/qe-3/qe-4 de las destacadas (`piezas/destacadas/gen-destacadas.py`)
con la captura sustituida por la grabación: **los mismos números, no unos parecidos**.

- **Foto del grid con `VELO_TELEFONO`**, respirando de 1,04 a 1,09 en cada capítulo (las
  tarjetas la llevan a 1,04 quieta) y fundido de 0,5 s al cambiar. El Coliseo para el
  plan, el callejón del Albayzín (la de qe-3) para el tour, Santa Prassede (qe-4) para el
  museo, y San Pedro de noche con el velo de qe-7 para el cierre.
- **Kicker a y=300 y titular a y=380**, texto por texto los de las destacadas: «1 · El plan
  / Dices dónde y cuándo. / Te escribe los días.», «2 · El tour a pie / Una voz te lleva
  / de parada en parada.», «3 · El museo / Enfocas un cuadro / y te cuenta su historia.».
  El titular va a 72 px (64 en la tarjeta) porque aquí se lee en movimiento. La segunda
  línea del plan entra cuando la app se pone a escribir los días (5,25).
- **El móvil de `telefono()`, escalado de 480 a 808 px de ancho** para que la grabación
  (760 px de pantalla) se lea: mismo negro, aro, isla y radios en proporción. Arranca en
  y=600 y sangra 430 px por abajo, a propósito: lo que queda fuera es teclado y botonera,
  que la interfaz de Instagram tapa igualmente. Lo que demuestra el argumento —el campo de
  destino, el itinerario con horas y precios, la ficha de la obra— queda entre 624 y 1480.
- **El cierre es el de qe-7, sin móvil**: el teléfono se va por abajo en 0,7 s (22,5-23,2)
  **antes** de que acabe su vídeo (23,23), para que nunca se vea una pantalla vacía; y
  entran «Todavía no está publicada / Llega en octubre.», «2,99 € el viaje entero.», «En
  la lista, el primero por 1,99 €.» —en ese orden— y la marca con `travelsnomad.com` a
  y=1400. Reposo hasta 28,0.

Los cortes de capítulo son los del metraje: **5,10** (la app empieza a montar el viaje),
**12,24** (tour), **17,74** (museo), **23,23** (fin). El rótulo sale en el corte y el
siguiente entra 0,35 s después: el texto explica lo que ya se ve, no lo anuncia.

### La grabación dentro del móvil: `assets/pantalla.mp4`

Los 18 cortes de abajo, **sin recortar** (dentro de un móvil tiene que verse el móvil
entero) y escalados a **760×1548**, la pantalla del marco. Y encima, **102 px de barra de
estado** que la grabación no traía y la captura de la casa (`plan-900.webp`) sí: hora a
la izquierda, cobertura y batería a la derecha, la isla en medio. El fondo de esos 102 px
se cuece en el vídeo como **reflejo desenfocado de sus propias primeras filas** —crema
sobre crema, mapa sobre mapa, sin costura—; los glifos van en el HTML. Sin esa banda, la
isla del marco tapaba «Buenas tardes, Marc» y el título del tour: la primera prueba
salió así.

```bash
# cada corte, desde el original (los tiempos, en la tabla de «Los cortes»)
ffmpeg -i 1.mov -vf "trim=start=0.55:end=1.30,setpts=PTS-STARTPTS,\
  scale=760:1548:force_original_aspect_ratio=increase,crop=760:1548,fps=30,setsar=1" \
  -an -c:v libx264 -crf 18 01.mp4
# concatenar y añadir la barra de estado en la misma pasada (una sola generación)
ffmpeg -f concat -safe 0 -i l.txt -filter_complex \
  "[0:v]split[a][b];[b]crop=760:102:0:0,vflip,gblur=sigma=18[c];[c][a]vstack,setsar=1" \
  -an -c:v libx264 -crf 18 -pix_fmt yuv420p -r 30 assets/pantalla.mp4
```

`pantalla.mp4` **se versiona** (4,8 MB; excepción a `*.mp4` en `.gitignore`) porque es la
materia prima de la composición y las grabaciones originales viven en el móvil del dueño,
no en el repo. Sin él, la composición no se rehace.

### Cómo se fabrica

```bash
bash piezas/historias-animadas/construir.sh          # fuentes y marca desde el banco
cd piezas/historias-animadas/demo-reel
npx hyperframes check                                 # 0/0, 21/21 en contraste
npx hyperframes render --output demo-reel.mp4         # 28 s a 30 fps
ffmpeg -i demo-reel.mp4 -t 12.0 -an -c:v libx264 -crf 18 demo-reel-historia-1.mp4
ffmpeg -i demo-reel.mp4 -ss 13.0 -an -c:v libx264 -crf 18 demo-reel-historia-2.mp4
ffmpeg -i demo-reel.mp4 -ss 9.0 -frames:v 1 -q:v 2 demo-reel-portada.jpg   # la portada
```

Lo que sale de ahí no se versiona (regla de `salida/`): se rehace del repo en tres minutos.
El render tarda ~2 min y sale h264 High, yuv420p, 30 fps, 5,3 Mb/s: entra en Instagram
tal cual.

Trampa de HyperFrames pagada aquí: **un `fromTo` de salida pisa la entrada.** Los `fromTo`
pintan su estado inicial al construirse, así que un `fromTo({autoAlpha: 1} → 0)` para
sacar un rótulo lo deja visible desde el fotograma 0. Las salidas van con `.to`.

## Las cuatro grabaciones

| | Fichero | Dur | Resolución |
|---|---|---|---|
| 1 | asistente completo → Generar → «Montando tus 3 días» | 26,7 s | 1206×2456 |
| A | el plan: home del viaje, mapa e itinerario | 8,8 s | 1206×2456 |
| B | el tour a pie | 15,8 s | 1206×2462 |
| C | el museo | 12,3 s | 1206×2454 |

**Las tres alturas son distintas** (2456 / 2462 / 2454): recorte propio para cada una.
En el corte a pantalla completa del 2-sep salían a 1080×1920 quitando 2144 px de alto y
escalando; los ~312 px sobrantes se quitaban casi todos de **arriba** para no tocar la
botonera de abajo, donde viven «Siguiente» y «Generar viaje». Recortes: `0:240`, `0:243`,
`0:239`. **En el reel de la casa (3-sep) no se recorta nada**: ver «La capa de presentación».

## Los cortes

| # | Origen | Desde | Hasta | Dur | Qué |
|---|---|---|---|---|---|
| 01 | 1 | 0,55 | 1,30 | 0,75 | la home: «¿A dónde vamos?»; al final ya sube el teclado |
| 02 | 1 | 2,90 | 3,22 | 0,32 | teclear «Roma» (termina antes del «Sin resultados» de 3,25) |
| 03 | 1 | 4,70 | 5,60 | 0,90 | el desplegable real y «Continuar» activándose |
| 04 | 1 | 7,80 | 8,60 | 0,80 | paso 1: tipo de viaje y fechas |
| 05 | 1 | 11,20 | 11,90 | 0,70 | paso 2: estilo, ritmo, presupuesto |
| 06 | 1 | 15,60 | 16,30 | 0,70 | paso 3: con quién viajas |
| 07 | 1 | 19,40 | 20,30 | 0,90 | paso 4 y el RESUMEN; la home asoma en 20,35 y se corta antes |
| 08 | 1 | 25,05 | 26,70 | 1,65 **+0,50 congelado** | «Montando tus 3 días en Roma» — la pantalla limpia empieza en 25,05 |
| 09 | A | 2,10 | 3,15 | 1,05 | el mapa entero y limpio (sólo existe en 2,1) y el scroll que descubre el viaje |
| 10 | A | 5,55 | 7,85 | 2,30 **+0,70 congelado** | jueves: el itinerario con horas y precios. Es el plano que vende |
| 11 | A | 7,92 | 8,82 | 0,90 | viernes: «y hay un segundo día» |
| 12 | B | 3,20 | 5,00 | 1,80 | «Diseñando tu tour — trazando una ruta sin rodeos…» (12 palabras: 1,8 s) |
| 13 | B | 6,50 | 8,00 | 1,50 | 6 paradas · 130 min · punto de encuentro |
| 14 | B | 9,20 | 11,40 | 2,20 | el mapa de la ruta y la audioguía con «Colócate aquí» |
| 16 | C | 0,90 | 2,00 | 1,10 | «Preparando la visita» — la ficha asoma en 2,1 y se corta antes |
| 17 | C | 2,30 | 3,80 | 1,50 | 7 obras · 105 min · 2 plantas |
| 18 | C | 5,15 | 7,05 | 1,90 | el Coloso de Constantino grande, con su audioguía debajo |
| 19 | C | 11,25 | 12,25 | 1,00 | todas las obras con miniaturas (la lista se llena en 11,2) |
| 20 | — | — | — | 4,00 | el cierre (3,8 en la historia 2) |

**Ya no hay 15.** Era 1,5 s del texto de la audioguía: un muro que nadie lee en 1,5 s y
cuyo único mensaje —«hay texto»— ya lo da el corte 14. Fuera, y el tour baja de 7,0 a 5,5 s.

## El congelado, y por qué es honesto

La grabación sólo tiene 2,3 s del itinerario del jueves limpio, y ese plano es el que
vende. Se **congela el último fotograma** 0,7 s (y 0,5 en «Montando»). La pantalla era
estática: es idéntico a haber sujetado el móvil más rato, y no fabrica nada. Sigue siendo
la app real.

Cómo se hace, y la trampa que tiene: **`-t` después de `-i` capa la duración de salida y
se come lo que `tpad` añade**; y subir `-t` en el 10 habría metido fotogramas reales del
viernes. Lo correcto es cortar con `trim` (exacto por PTS) y congelar después:

```bash
ffmpeg -i A.mov -vf "trim=start=5.55:end=7.85,setpts=PTS-STARTPTS,\
  crop=1206:2144:0:240,scale=1080:1920,fps=30,setsar=1,\
  tpad=stop_mode=clone:stop_duration=0.70" -an -c:v libx264 -crf 20 10.mp4
```

## Dos decisiones (2-sep: valen para el corte a pantalla completa, que ya no es el reel)

**La pantalla del precio no se quita: se mueve al final.** Enumera lo que incluye, pone
2,99 € en un botón y remata con «pago único para todo el grupo». En el segundo 20 es un
peaje; de cierre es un resumen de valor. Va de fondo del corte 20.

**El cierre es una composición HyperFrames** (`piezas/historias-animadas/demo-cierre/`),
la única parte del reel donde HyperFrames aporta algo visible: el fondo es un fotograma
de la pantalla del precio (`assets/fondo-cierre.png`) y encima, en 4 s: la pantalla se ve
limpia un instante, cae la banda oscura (0,15-0,65), entra «Sale en octubre» (0,45),
luego «2,99 € el viaje entero» (1,05) y luego «En la lista, el primero por 1,99 €»
(1,45) — **el orden de la casa, reforzado por el movimiento** — y reposo hasta el final.
`check` 0/0/0/0, contraste 14/14. Se renderiza con `npx hyperframes render`, se recodifica
a los parámetros del concat y entra como 20 (4,0 s) y 20h (los primeros 3,8 s, historia 2).
El texto empieza en y=300, dentro de la zona segura de historia; la versión quieta
anterior lo tenía en 210, dentro de la franja que la interfaz puede tapar.

El resto del reel sigue siendo ffmpeg a pelo, a propósito: es una edición de metraje, y
HyperFrames sólo entra donde hay algo que animar. **ffmpeg corta el metraje; HyperFrames
anima lo que va encima.**

El rótulo del cierre dice, en este orden: **«Sale en octubre.» / «2,99 € el viaje entero.»
/ «En la lista, el primero por 1,99 €.»** La versión anterior sólo decía 1,99 arriba y
dejaba el 2,99 al botón de abajo — el ojo leía 1,99 antes que 2,99, y la regla de la casa
es «siempre en ese orden». Corregido: el propio rótulo lleva los dos, ordenados.

**Casi no lleva rótulos, porque la app se narra sola** (en el reel de la casa sí los lleva,
pero son los de las destacadas, no unos nuevos; lo de abajo sigue mandando en la duración
de los cortes). «Montando tus 3 días en Roma —
elegimos qué ver cada día y en qué orden, para no cruzar la ciudad dos veces». «Diseñando
tu tour — trazando una ruta sin rodeos y eligiendo dónde merece la pena parar».
«Preparando la visita — eligiendo las obras y ordenando las salas para no repetir
ninguna». Esas tres pantallas de carga son el guion, y por eso tienen que **durar lo que
tardan en leerse**: 1,8–2,2 s las de dos líneas. Sólo el cierre lleva texto añadido.

**Transiciones: cortes secos, a propósito.** Una grabación de pantalla corta seco de forma
nativa; un fundido la convierte en «vídeo producido». En el reel de la casa la grabación
sigue cortando seco **dentro** del móvil; lo que se funde es la foto de fondo, como pasar
de una tarjeta a la siguiente. **Portada**: la del 2-sep era «ninguna»; la del 3-sep es un
fotograma del propio reel con el itinerario en pantalla (`demo-reel-portada.jpg`), porque
ahora el primer fotograma sí parece una tarjeta de la casa.

## LAS TRAMPAS, con precisión

1. **Las hojas de contacto hechas con `-vf "fps=N,…,tile"` derivan en el tiempo.** Son
   grabaciones de **fotograma variable** (iOS sólo emite fotograma cuando la pantalla
   cambia) y el filtro `fps` reconstruye una línea de tiempo que en el clip de mayor tasa
   (A, 60 fps de media) llegó a 1,3 s de desfase — y no en los otros, así que no se
   compensa. Cortando por esos tiempos entraron un barrido con el mapa sin tiles, el
   esqueleto de carga del itinerario y la mejor imagen del museo tapada por su panel.
   **El fotograma suelto lee el PTS y es la autoridad.** Búsqueda en dos etapas, exacta y
   rápida: `-ss (T-2) -i clip -ss 2 -frames:v 1`. Comprobado que coincide con la de una
   etapa (`-i clip -ss T`).
2. **`-ss` antes de `-i` salta al fotograma clave**, no al exacto. Por eso se perdió el
   desplegable en la primera versión.
3. **Leer el fotograma a tamaño de sello no es verificar.** Una discrepancia «real» entre
   dos fotogramas sueltos resultó ser una miniatura de 136 px mal leída: a 300 px el
   teclado era inconfundible. Los límites de corte se verifican a ≥300 px de ancho.
4. **`-t` después de `-i` capa lo que `tpad` añade.** Ver «El congelado».

La regla corta sigue valiendo: **la hoja de contacto sirve para ver QUÉ hay; el fotograma
suelto, a tamaño legible, decide CUÁNDO cortar.**
