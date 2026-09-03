# Historias animadas — la prueba con HyperFrames (1-sep)

Una pieza de prueba, no una migración. Sale de una pregunta del dueño esa noche: *«¿no
lo ves una buena herramienta para hacer contenido para subir a historias y reels, rollo
tema animaciones?»*.

**Qué es HyperFrames**: un framework open source de HeyGen (Apache 2.0) que convierte
HTML + CSS + animaciones en MP4 determinista — Chrome headless pinta los fotogramas,
ffmpeg los encodea. El render local es gratis y offline: sin cuenta, sin API key, sin
coste por render. Anthropic lo distribuye como plugin oficial de Claude Code.

## La regla de por dónde entra

**No convierte lo que ya existe.** Su documentación es explícita: el paso de Claude
Design a HyperFrames es **de un solo sentido**, y el proyecto pasa a ser el artefacto
editable. Convertir las 22 tarjetas del taller costaría lo único que el dueño pidió por
escrito — *«quiero poder editarlas yo antes por si algo no me gusta»*.

Así que entra **sólo por lo aditivo**: piezas que el taller no puede producir de ninguna
manera, donde el movimiento ES la pieza y no hay nada que editar a mano. Las tarjetas
estáticas se quedan donde están, en el lienzo, intactas.

## La pieza

`lista-pasos/` — los tres pasos de la lista de espera, apareciendo en orden. Es la
versión animada de `li-3`, la tarjeta que convierte (§«Destacada 2» de
`piezas/destacadas/README.md`): mismo texto, mismo degradado, misma tipografía y mismas
posiciones que la estática. Lo único que cambia es que los pasos se leen **en orden
porque aparecen en orden**, no porque el ojo elija.

- 1080×1920, 30 fps, **9,0 s**, h264, **0 pistas de audio** — el audio se elige dentro
  de Instagram, de tendencias, como los reels.
- Los tres pasos entran en 5,5 s y quedan 3,5 s de reposo para leerlos y tocar el enlace.
- Zona segura respetada: nada por debajo de y=1520, que es donde va el adhesivo de
  enlace con `?utm_source=instagram&utm_medium=organic&utm_campaign=destacada-lista`.

```bash
bash piezas/historias-animadas/construir.sh          # fuentes y marca desde el banco
cd piezas/historias-animadas/lista-pasos
npx hyperframes check                                 # lint, layout, movimiento, contraste
npx hyperframes render --output lista-pasos.mp4
```

`check` pasa con 0 hallazgos y **44/44 en contraste WCAG AA**. El render tarda ~21 s.

**Hace falta `ffprobe` además de `ffmpeg`**, y `ffmpeg-static` no lo trae. Si esto se
adopta, `ffprobe-static` entra en el `package.json`; para la prueba se instaló fuera.

## Lo que encontró la prueba: las fuentes del banco están rotas

El hallazgo más caro de la tarde, y no tiene que ver con HyperFrames — lo destapó su lint
al obligar a quitar las reservas de tipografía.

**Los dos woff2 embebidos en el HELMET de `banco/fuentes/Main.dc.html` contienen
exactamente dos glifos cada uno: «A» y «Á».** Medido carácter a carácter sobre 83 con
CDP (`CSS.getPlatformFontsForNode`): 2/83 en las dos familias. Todo lo demás cae a la
fuente del sistema — en un contenedor, Liberation Serif. La primera versión de esta
pieza salió con el texto de los pasos en serif del sistema, no en Instrument Sans.

En el lienzo no se nota, porque Claude Design sirve las fuentes de su lado. **Se nota al
renderizar fuera**, que es lo que hacen `exportar-reel.mjs` y esto. Las tarjetas
exportadas a mano desde el taller están bien; lo exportado por un script, no.

El arreglo aquí: las fuentes **reales** de Google Fonts (OFL) en
`banco/fuentes/webfonts/` con sus `unicode-range`, embebidas en base64 por
`construir.sh` — el render no puede depender de la red (regla de determinismo). No se
tocó `Main.dc.html`: el taller es del dueño y eso se decide, no se cambia por la espalda.
Queda abierto en una issue.

## Trampas pagadas en esta pieza

- **Nada de `<br>` en el cuerpo.** HyperFrames lo prohíbe y tiene razón: fuerza un corte
  que ignora el ancho real de la fuente al renderizar y acaba solapando. Cada línea es su
  propio bloque.
- **El estado inicial va dentro del `fromTo`, nunca en un `transform` de CSS.** El valor
  de CSS y el arranque del tween se pelean, y el lint lo rechaza.
- **La línea de tiempo se registra al final**, dentro de `document.fonts.ready`. Si se
  registra antes de meter los tweens, HyperFrames la anida vacía y el render sale en
  blanco, sin error.
- **El elemento que se transforma tiene que ser bloque y tener caja.** El número del paso
  es un `<span>`: escalarlo sin `display: block` no hace nada.
- `StaticGuard` avisa de que no encuentra los `@font-face`. Es un **falso positivo**:
  mira el HTML y no sigue la hoja enlazada. Verificado por CDP que los glifos salen de
  Instrument Serif e Instrument Sans.

## La segunda pieza: el cierre animado de la demo (2-sep)

`demo-cierre/` — 4 s sobre un fotograma de la pantalla del precio de la app real: cae la
banda y entran «Sale en octubre», 2,99 € y 1,99 €, en ese orden. Era el único tramo del
corte a pantalla completa hecho con HyperFrames; el resto era ffmpeg. Ese corte dejó de
ser el reel el 3-sep (abajo), pero la pieza sigue valiendo como cierre suelto.

## La tercera pieza: el reel de la demo en el estilo de la casa (3-sep)

`demo-reel/` — 28 s. Es la primera pieza donde HyperFrames **es** el reel, no un tramo:
la grabación de la app (`assets/pantalla.mp4`, 23,2 s, ya cortada) dentro del móvil de
las tarjetas, sobre las fotos del grid con su velo, con los kicker y titulares de las
destacadas entrando capítulo a capítulo (plan, tour, museo) y el cierre de qe-7 sin
móvil. El dueño lo pidió al ver el corte a pantalla completa al lado del grid: no parecía
de la misma casa. La receta y las decisiones, en `piezas/demo-app/MONTAJE.md`, «La capa
de presentación».

- `check`: 0 errores, 0 avisos, **21/21 en contraste**. El móvil sangra por abajo a
  propósito y lo declara con `data-layout-allow-overflow`.
- El `<video>` lleva su tiempo (`data-start`/`data-duration`) y su envoltorio —el móvil—
  no lleva ninguno: HyperFrames rechaza las dos cosas a la vez, y el fallo es real (frames
  equivocados y el clip desaparece a mitad).
- El móvil se va de pantalla **antes** de que acabe su vídeo, para que nunca se vea la
  pantalla vacía cuando el clip termina.
- **Un `fromTo` de salida pisa la entrada**: pinta su estado inicial (visible) al
  construirse. Las salidas van con `.to`.
