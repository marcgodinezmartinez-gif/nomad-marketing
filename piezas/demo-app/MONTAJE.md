# El montaje de la demo — la receta exacta (2-sep)

De 63 s de grabación en cuatro ficheros salen **29,0 s** en 1080×1920, 30 fps y **sin pista
de audio** (se elige dentro de Instagram, como los reels). Sirve para reel y para historia.

## Las cuatro grabaciones

| | Fichero | Dur | Resolución |
|---|---|---|---|
| 1 | asistente completo → Generar → «Montando tus 3 días» | 26,7 s | 1206×2456 |
| A | el plan: home del viaje, mapa e itinerario | 8,8 s | 1206×2456 |
| B | el tour a pie | 15,8 s | 1206×2462 |
| C | el museo | 12,3 s | 1206×2454 |

**Las tres alturas son distintas** (2456 / 2462 / 2454), así que cada una lleva su recorte
propio. Todas salen a 1080×1920 quitando 2144 px de alto y escalando: se va la barra de
estado y **no se toca la botonera de abajo**, que es donde viven «Siguiente» y «Generar
viaje».

## Los cortes

| # | Origen | Desde | Dur | Qué |
|---|---|---|---|---|
| 01 | 1 | 0,30 | 1,10 | la home: «¿A dónde vamos?» |
| 02 | 1 | 2,90 | 0,40 | teclear «Roma» |
| 03 | 1 | 4,70 | 0,90 | el desplegable real y «Continuar» activándose |
| 04 | 1 | 7,80 | 0,80 | paso 1: tipo de viaje y fechas |
| 05 | 1 | 11,20 | 0,70 | paso 2: estilo, ritmo, presupuesto |
| 06 | 1 | 15,60 | 0,70 | paso 3: con quién viajas |
| 07 | 1 | 19,40 | 1,00 | paso 4 y el RESUMEN entero |
| 08 | 1 | 24,60 | 2,00 | «Montando tus 3 días en Roma» |
| 09 | A | 2,45 | 1,00 | el mapa con la ruta |
| 10 | A | 5,50 | 2,60 | jueves: el itinerario con horas y precios |
| 11 | A | 8,05 | 0,78 | viernes |
| 12 | B | 3,20 | 1,50 | «Diseñando tu tour» |
| 13 | B | 6,80 | 1,80 | 6 paradas · 130 min · punto de encuentro |
| 14 | B | 9,20 | 2,20 | el mapa de la ruta y la audioguía |
| 15 | B | 13,50 | 1,50 | «Colócate aquí» y la historia |
| 16 | C | 1,00 | 1,30 | «Preparando la visita» |
| 17 | C | 2,60 | 1,60 | 7 obras · 105 min · 2 plantas |
| 18 | C | 5,15 | 1,90 | el Coloso de Constantino con su audioguía |
| 19 | C | 11,00 | 1,25 | todas las obras, con miniaturas |
| 20 | — | — | 4,00 | el cierre |

## Dos decisiones

**La pantalla del precio no se quita: se mueve al final.** Enumera lo que incluye, pone
2,99 € en un botón y remata con «pago único para todo el grupo» — la mejor expresión de la
oferta que existe, y la escribió el producto. En el segundo 20 es un peaje; de cierre es un
resumen de valor. Va de fondo del corte 20, con «Sale en octubre» y el 1,99 € de la lista
encima, en banda oscura sólida (la interfaz es clara y el texto blanco se pierde).

**Casi no lleva rótulos, porque la app se narra sola.** «Montando tus 3 días en Roma —
elegimos qué ver cada día y en qué orden, para no cruzar la ciudad dos veces». «Diseñando
tu tour — trazando una ruta sin rodeos y eligiendo dónde merece la pena parar».
«Preparando la visita — eligiendo las obras y ordenando las salas para no repetir
ninguna». Esas tres pantallas de carga son el guion. Sólo el cierre lleva texto añadido.

## LA TRAMPA CARA: las hojas de contacto con el filtro `fps` MIENTEN sobre el tiempo

Para localizar los momentos se hicieron montajes con `-vf "fps=N,scale,tile"`. **Los
tiempos que sugieren están desplazados** — en el clip A, hasta 1,3 s. Cortando por esos
tiempos entraron en el montaje un barrido con **el mapa sin tiles cargados** y **el
esqueleto de carga del itinerario**, y el mejor plano del museo (la cabeza de Constantino)
se cortó donde el panel la tapaba. Curiosamente el desfase afectó a un clip y no a los
otros, así que ni siquiera es un desplazamiento constante que se pueda compensar.

**Los tiempos se sacan con fotogramas sueltos**, uno por extracción:

```bash
ffmpeg -i clip.mov -ss 5.15 -frames:v 1 -vf "scale=150:-1" f.jpg
```

Y **`-ss` va SIEMPRE después de `-i`**: antes de `-i` salta al fotograma clave más cercano,
no al exacto. Ese fue el primer fallo, y por él se perdió el desplegable del autocompletado
en la primera versión.

Regla corta: **la hoja de contacto sirve para ver QUÉ hay; nunca para decidir CUÁNDO
cortar.**
