# Tu primer viaje, gratis (24-nov) — el reel del Black Friday

Un reel de **31,7 s** para la semana del Black Friday: el primer viaje de cada cuenta es gratis (NOMAD#479).
Junta eso con lo que salió de la simulación de MiroFish: quien no ha probado la app no ve por qué usarla en
vez de pedirle el plan a cualquier IA. El guion y los textos de la campaña están en la issue #23.

**Lo pidió el dueño así** (24-nov): montado entero aquí, sin ningún vídeo suyo, antes de tocar la app, y que
enganche. Por eso la pantalla de pago con «Gratis» no sale: todavía no existe en ningún móvil, y una
captura inventada sería una maqueta. La oferta va en una tarjeta de texto.

## La idea

Una IA te hace la lista. Lo que no hace es ir contigo. El vídeo enseña las dos cosas seguidas:

| seg. | qué se ve | qué se oye |
|---|---|---|
| 0-3,2 | Un chat de IA genérico escribe la lista de 3 días en Lisboa | Kore: «Una IA te hace la lista en diez segundos.» |
| 3,2-6,2 | La lista se apaga y queda una línea, «Praça do Comércio», con una chincheta: «Estás aquí» | Kore: «Pero cuando estás allí, ¿quién te cuenta lo que tienes delante?» |
| 6,2-18,1 | El papel de la app se abre desde la chincheta: la parada 1 del paseo de verdad, y la tarjeta de la audioguía con cada palabra encendiéndose | Charon, la audioguía: «El 1 de noviembre de 1755, un devastador terremoto seguido de un maremoto y un incendio voraz destruyó el antiguo Palacio Real que se erigía exactamente en este espacio.» |
| 18,1-24,2 | El plan del sábado, la parada 2, la parada 3, la obra 1 y la obra 2 del museo | Kore: «Eso es Nomad. Te guía a pie, parada a parada, y en el museo, obra a obra.» |
| 24,2-28,6 | La oferta, sobre verde: «Tu primer viaje, gratis.» con sus dos condiciones | Kore: «Y esta semana, tu primer viaje es gratis.» |
| 28,6-31,7 | El cierre, quieto: el icono, el nombre, las dos tiendas y la oferta otra vez | Kore: «Descárgala en la App Store o en Google Play.» |

Los cortes salen de la voz (`preparar-voz.py`), no al revés.

## Qué es de verdad y qué no

- **Las pantallas son capturas de la app del 19-nov**, a su tamaño (1206 × 2622), sin tocar
  (`assets/pantallas/`). Salen del guion `web` de `capturas/` del repo de la app, en castellano, con la
  cuenta demo y su viaje a Lisboa. Se ven por una ventana y lo único que se mueve es por dónde se mira.
  No hay nada pintado encima. No sale ningún código de invitación, correo ni nombre.
- **La frase de la audioguía es la de la app, palabra por palabra**: «La historia» de la parada 1 del
  paseo por la Baixa y el Chiado, segunda frase. Se ve escrita en la captura cuando la ventana baja.
- **Las dos voces son voces de la app** (`mobile/src/lib/narrationVoices.ts`: Kore, Puck y Charon), con el
  modelo de la app (`gemini-3.1-flash-tts-preview`). La de la audioguía lleva la instrucción de tono que
  usa `narrate` («Narra como una guía turística cercana y entusiasta…»). La app lee trozos más largos:
  aquí se le pidió esa frase sola.
- **El chat no es de nadie.** Es una piel genérica («Asistente de IA»), hecha en HTML. Es una
  dramatización: no imita la pantalla de ninguna marca ni dice que ninguna IA recomiende Nomad. Lo que
  escribe es lo que escribe cualquiera: una lista de sitios por días.
- **La música es de Lyria** (`lyria-3-clip-preview`, `musica-prompt.txt`) y las voces son sintéticas. Al
  publicar se marca la etiqueta de contenido hecho con IA.

## Lo que el vídeo no puede dar a entender

- Que «gratis» es para siempre o para todos los viajes: las dos condiciones van escritas en la oferta y
  otra vez en el cierre (un viaje por cuenta, hasta el 3 de diciembre).
- Que una IA no sabe contarte nada de un sitio: el vídeo dice lo que hace Nomad, no lo que otros no pueden.
- Nada de «lista de espera» ni de 1,99 €. El precio, «desde 2,99 € el viaje».

## Lo que falta por confirmar (es del dueño)

- **La fecha, «hasta el 3 de diciembre»**, y que no haya tope a la vista. Están escritas en `index.html`
  (la oferta y el cierre). Si cambian, se cambia el texto y se vuelve a renderizar: unos diez minutos.
- **El vídeo no se publica hasta que la promoción esté encendida** (NOMAD#479). Antes, anuncia algo que
  la app no hace.
- **Las voces**: si prefiere a Kore también en la audioguía, o sin narradora, se regraba.

## Cómo se rehace

```bash
bash ../construir.sh                 # las fuentes embebidas
python3 -I preparar-voz.py           # las seis frases, sus tiempos y los cortes: assets/tiempos.js
python3 -I mezclar.py                # assets/sonido.m4a y assets/sonido-sin-musica.m4a
bash variantes.sh <salida>           # los vídeos, la portada y los fotogramas de revisión
```

Las tomas crudas de voz y la música no se versionan (`assets/voz/tomas/`, `assets/musica/`): se regraban
con `../../ia/voz.py` y `../../ia/musica.py`. Lo que sí está: las seis frases ya preparadas
(`assets/voz/*.flac`) y la mezcla.

## Lo que se aprendió montándolo

- **La grabación en vídeo de la guía que hay es del 29-oct y enseña una errata** («centro neurológico»)
  que la app corrigió el 13-nov. Las capturas del 19-nov ya dicen «neurálgico». Antes de usar una toma,
  se mira si lo que enseña sigue siendo lo que hace la app.
- **Las grabaciones grandes de la página privada del dueño no se pueden bajar desde una sesión**: la
  herramienta corta en 4 MB, y las del paseo y el museo pesan 6. Las capturas sí.
- **Una frase de la audioguía dura más de lo que parece**: 13,4 s a su ritmo, 11,5 s a 1,15×. Con ella el
  vídeo pasa de los 30 s. Se dejó entera porque es lo que cuenta la app, y cortarla la cambia.
- **Las páginas de la tarjeta cambian en una pausa de la voz.** La primera versión cambiaba justo detrás
  de «Palacio Real» y la palabra se veía encendida 0,1 s.
