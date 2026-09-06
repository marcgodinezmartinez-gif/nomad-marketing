# El plan de Roma — el carrusel que se guarda (6-sep)

## El número que lo obligó

El reel del 3-sep llegó a **1 258 espectadores y se guardó cero veces**. Los guardados son
la moneda del alcance orgánico —lo que Instagram premia para seguir repartiendo— y **un
demo de producto no se guarda**: se ve y se olvida. Un itinerario sí.

Así que aquí se invierte el papel: **el protagonista es EL PLAN** y la app baja al pie
(«esto lo escribió NOMAD en menos de un minuto»). De paso resuelve la contradicción que
arrastraba todo lo anterior — el plan **sirve hoy**, aunque la app no se pueda usar hasta
octubre.

## Las cinco tarjetas

```bash
bash piezas/preparar.sh
cd salida && python3 ../piezas/roma/gen-plan-roma.py    # los .dc.html
node ../piezas/roma/exportar-plan.mjs                   # los PNG 1080x1350
```

| # | Qué | Foto |
|---|---|---|
| 1 | Portada: «Un jueves entero, por 52 €» | Coliseo |
| 2 | **El día entero, hora a hora.** La que se guarda | ninguna, fondo oscuro |
| 3 | «El tour a pie va incluido» — sin reservar, sin grupo, sin propina | Fontana di Trevi |
| 4 | «Cómo se hizo»: el móvil con el plan real | Santa Prassede |
| 5 | Cierre: octubre y 1,99 € | San Pedro de noche |

**La tarjeta 2 es la pieza.** Sin foto y sin adornos, porque lo que se guarda se lee: las
cinco paradas con su hora, su categoría y su precio, y **lo gratis en menta**, que es lo
que sorprende. Las otras cuatro existen para que llegue hasta ella.

## El plan es real, y las cuentas cuadran

Leído fotograma a fotograma de la grabación del 3-sep (**jueves 03 sept, 5 planes ·
52 €**), no de memoria: 25 + 5 + 22 = 52. Si algún día la app escribe otro plan, se vuelve
a leer de una grabación nueva; **no se edita el texto a mano**.

La captura del móvil de la tarjeta 4 es de ese mismo jueves —`banco/capturas/planjueves-900.webp`,
sacada del original a 900 de ancho— y no la del banco (`plan-900.webp`), que es de otro
día (sábado 29 ago, 72 €). Una captura de un día distinto al del carrusel sería una
promesa que el carrusel no cumple.

## Dos trampas, una vieja y una nueva

- **El fondo CC0 de Openverse volvió a fallar exactamente igual.** Se pidieron una foto de
  la Piazza del Popolo y otra del Panteón: la primera vino siendo un **grabado del XVIII**
  (una *veduta*, digitalización de museo) y la segunda, la fachada de un edificio
  cualquiera con una hornacina — ni siquiera el Panteón. Las dos borradas antes de entrar.
  **La regla de mirarlas una a una no es opcional**, y el título engaña: uno decía
  «Piazza del Popolo» y el otro «Rome, Italy».
- **Nada de `<br>` en los cuerpos.** La primera exportación los llevaba y salieron
  renglones sueltos: el corte forzado ignora el ancho real de la fuente, y las del HELMET
  no miden como las reales que inyecta el exportador. Se controla con el ancho y se deja
  fluir, con `text-wrap: pretty`. Es la misma trampa que HyperFrames prohíbe de entrada.
- Y la de siempre: **el exportador inyecta las fuentes reales** de `banco/fuentes/webfonts`,
  porque las del HELMET son subconjuntos de dos glifos y lo exportado por un script sale
  en la fuente del sistema sin avisar.

## El pie (lleva el plan entero, que es lo que se lee)

> Un jueves entero en Roma, por 52 €. Hora a hora:
>
> 10:30 · Llegada y traslado al centro — gratis
> 11:30 · Tour a pie por el Centro Histórico y las Plazas — gratis
> 14:15 · Comida en Armando al Pantheon — 25 €
> 16:00 · Panteón de Agripa — 5 €
> 19:30 · Cena en Rifugio Romano — 22 €
>
> Dos de las cinco cosas del día no cuestan nada, y el tour a pie es una de ellas: seis
> paradas por las plazas del centro, sin reservar, sin grupo y sin propina.
>
> Esto lo escribió NOMAD. Le dijimos «Roma, 3 días» y salió en menos de un minuto, con el
> orden, las horas y lo que cuesta cada parada.
>
> Sale en octubre, y el primer viaje sale por 1,99 € para quien esté en la lista de espera.
> El enlace, en la bio.
>
> #roma #viajararoma #italia #viajar #viajes #escapada #europa

**Se sube como carrusel del feed, las cinco en orden 1 → 5** (al revés que el grid, que va
del 9 al 1: un carrusel se lee hacia adelante). Sin música: los posts del feed no la
llevan.

## Lo que queda pendiente

- **El viernes y el sábado.** El viernes tiene la última parada tapada por la botonera en
  las dos grabaciones, y del sábado no hay ninguna. Con una captura más salen otros dos
  carruseles iguales, y de ahí el pie de «3 días en Roma» entero.
- **El taller** sigue sin estas tarjetas (ver issue #3, que ya pide una siembra completa).
