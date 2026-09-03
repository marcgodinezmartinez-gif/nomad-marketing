# El montaje de la demo — la receta exacta (2-sep, revisada)

De 63 s de grabación en cuatro ficheros salen **27,2 s** en 1080×1920, 30 fps y **sin pista
de audio** (se elige dentro de Instagram, como los reels). Tres ficheros de salida:

| Fichero | Dur | Para qué |
|---|---|---|
| `nomad-demo.mp4` | 27,2 s | el reel, entero |
| `nomad-demo-historia-1.mp4` | 12,2 s | historia 1: el asistente y el plan |
| `nomad-demo-historia-2.mp4` | 14,8 s | historia 2: tour, museo y cierre |

Las dos historias **no son el reel partido por la mitad**: cada una cuenta algo entero
(pedir → plan; guiar → museo → precio), y las dos quedan por debajo de los 15 s donde
Instagram trocea. La segunda lleva el cierre a 3,8 s en vez de 4,0 para no rozar el
límite. El adhesivo de enlace va en la segunda, de y=1520 abajo.

## Las cuatro grabaciones

| | Fichero | Dur | Resolución |
|---|---|---|---|
| 1 | asistente completo → Generar → «Montando tus 3 días» | 26,7 s | 1206×2456 |
| A | el plan: home del viaje, mapa e itinerario | 8,8 s | 1206×2456 |
| B | el tour a pie | 15,8 s | 1206×2462 |
| C | el museo | 12,3 s | 1206×2454 |

**Las tres alturas son distintas** (2456 / 2462 / 2454): recorte propio para cada una.
Todas salen a 1080×1920 quitando 2144 px de alto y escalando; los ~312 px sobrantes se
quitan casi todos de **arriba** (se va la barra de estado) para no tocar la botonera de
abajo, donde viven «Siguiente» y «Generar viaje». Recortes: `0:240`, `0:243`, `0:239`.

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

## Dos decisiones

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

**Casi no lleva rótulos, porque la app se narra sola.** «Montando tus 3 días en Roma —
elegimos qué ver cada día y en qué orden, para no cruzar la ciudad dos veces». «Diseñando
tu tour — trazando una ruta sin rodeos y eligiendo dónde merece la pena parar».
«Preparando la visita — eligiendo las obras y ordenando las salas para no repetir
ninguna». Esas tres pantallas de carga son el guion, y por eso tienen que **durar lo que
tardan en leerse**: 1,8–2,2 s las de dos líneas. Sólo el cierre lleva texto añadido.

**Transiciones: cortes secos, a propósito.** Una grabación de pantalla corta seco de forma
nativa; un fundido la convierte en «vídeo producido», que es la estética del anuncio que
la regla de la casa manda evitar. **Portada: ninguna.** El primer fotograma es la app
preguntando «¿A dónde vamos?», que es el gancho, y al final del primer corte ya sube el
teclado: hay movimiento antes del segundo 1.

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
