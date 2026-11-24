# Tu primer viaje, gratis (24-nov) — el reel del Black Friday

Un reel de **34 s** para la semana del Black Friday: el primer viaje de cada cuenta es gratis (NOMAD#479).
Junta eso con lo que salió de la simulación de MiroFish: quien no ha probado la app no ve por qué usarla en
vez de pedirle el plan a cualquier IA. El guion y los textos de la campaña están en la issue #23.

**Lo pidió el dueño así** (24-nov): montado entero aquí, sin ningún vídeo suyo, antes de tocar la app, y que
enganche. Por eso la pantalla de pago con «Gratis» no sale: todavía no existe en ningún móvil, y una
captura inventada sería una maqueta. La oferta va en una tarjeta de texto.

## La idea

Una IA te hace la lista. Lo que no hace es ir contigo. El vídeo enseña las dos cosas seguidas:

| seg. | qué se ve | qué se oye |
|---|---|---|
| 0-3,8 | **El gancho**, sobre el verde de la oferta: el icono, «¿Qué es Nomad?» y, con la voz, «Esta semana puedes probarlo gratis.» | Kore: «¿Qué es Nomad? Esta semana puedes probarlo gratis.» |
| 3,8-5,6 | Un chat de IA genérico escribe la lista de 3 días en Lisboa. Abajo, la firma: «Nomad · Primer viaje gratis esta semana» | Kore: «Una IA te hace la lista.» |
| 5,6-8,6 | La lista se apaga y queda una línea, «Praça do Comércio», con una chincheta: «Estás aquí» | Kore: «Pero cuando estás allí, ¿quién te cuenta lo que tienes delante?» |
| 8,6-20,4 | El papel de la app se abre desde la chincheta. En la pantalla del móvil, entera y con su borde verde, la presentación del paseo y su parada 1. A la derecha, los auriculares. Abajo, lo que dice la audioguía, con cada palabra encendiéndose | Charon, la audioguía: «El 1 de noviembre de 1755, un devastador terremoto seguido de un maremoto y un incendio voraz destruyó el antiguo Palacio Real que se erigía exactamente en este espacio.» |
| 20,4-26,5 | En la pantalla, el plan del sábado, la parada 2, la parada 3, la obra 1 y la obra 2 del museo. A la derecha, el logo, el pin y el cuadro | Kore: «Eso es Nomad. Te guía a pie, parada a parada, y en el museo, obra a obra.» |
| 26,5-30,5 | La oferta, sobre verde, con la marca: «Tu primer viaje, gratis.» y sus dos condiciones | Kore: «Y esta semana, tu primer viaje es gratis.» |
| 30,5-34 | El cierre, quieto: el icono, el nombre, las dos tiendas, la oferta con sus condiciones y el precio de después, y las líneas de marcas de Apple y Google | Kore: «Descárgala en la App Store o en Google Play.» |

Los cortes salen de la voz (`preparar-voz.py`), no al revés.

## Qué es de verdad y qué no

- **Las pantallas son capturas de la app del 19-nov**, sin tocar (`assets/pantallas/`). Salen del guion
  `web` de `capturas/` del repo de la app, en castellano, con la cuenta demo y su viaje a Lisboa. Se ven
  ENTERAS, sin la barra de estado, dentro del borde de la pantalla del molde de «Así funciona». No hay
  nada pintado encima. No sale ningún código de invitación, correo ni nombre.
- **Son capturas, no una grabación: dentro de la pantalla la app no se mueve, sólo cambia de pantalla.**
  En «Así funciona» corría la grabación del simulador. Aquí no hay una grabación de hoy (ver abajo).
- **Los dibujos de la derecha son los del molde** (`dibujos.py` los saca de
  `../puente-viena/iconos/editorial.json`): los auriculares, el pin y el cuadro. No se dibujó nada nuevo.
- **La frase de la audioguía es la de la app, palabra por palabra**: «La historia» de la parada 1 del
  paseo por la Baixa y el Chiado, segunda frase. Empieza escrita al pie de la captura de esa parada.
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

## El gancho es del dueño (24-nov)

Al ver la segunda versión: **«creo que el gancho sería: ¿qué es Nomad? No te preocupes, esta semana
tienes la oportunidad de conocerlo gratis, o algo así. Eso hará que la gente se quede de primeras»**.
Antes el vídeo abría con el chat («Una IA te hace la lista en diez segundos») y la oferta no salía entera
hasta el segundo 24. Ahora la pregunta y la oferta van en los cuatro primeros segundos, el chat se
acorta a una frase, y «Eso es Nomad» pasa a ser la respuesta a la pregunta del principio.

## Lo que dijo el dueño al verlo (24-nov)

La primera versión enseñaba la app recortada en un recuadro con sombra, con la vista bajando y
acercándose, y una tarjeta para la audioguía. El dueño: **«no se ve guay así como en cuadrados las
capturas de la app. Se notan demasiado con IA»**. Se rehízo la parte de la app en el molde de «Así
funciona», que ya había aprobado: la pantalla entera del móvil con su borde, el dibujo y la frase. El
chat del principio, la oferta y el cierre no cambiaron.

Lo que hay que llevarse: **una captura recortada y animada por encima (paneos, acercamientos, sombras)
se lee como plantilla hecha por una máquina**. La app se enseña entera, en su pantalla, y lo que se
mueve es la app, no la cámara.

## Cómo se revisó

Antes de darlo por bueno lo miraron cuatro revisores independientes, cada uno con una cosa: las reglas
de la casa y los tiempos, quien se lo encuentra sin sonido, el sonido medido, y los datos y las normas
de fuera. Cada hallazgo grave o medio de los tres últimos lo intentó tumbar un escéptico. Lo que se cambió:

- **Los textos del cierre se salían por la derecha.** Estaban centrados en el ancho entero (1080) y por
  debajo de y=900 la columna de botones tapa desde x=900. Ahora van en dos líneas, entre x=180 y x=900.
- **Las condiciones de «gratis» estaban 2,2 s en pantalla.** Entraban después de la palabra «gratis».
  Ahora entran con «viaje» (3,4 s) y el cierre dura medio segundo más.
- **El icono del chat era una estrella de cuatro puntas**, que recuerda a la de una marca de IA. Ahora es
  un bocadillo con tres puntos, que no es de nadie.
- **La cabecera del chat y la burbuja** bajaron y entraron en la zona segura.
- **El primer fotograma estaba medio vacío** (la lista tardaba 0,3 s en empezar). Ahora la respuesta ya
  va por la cuarta línea cuando se abre el vídeo, y la firma lleva la oferta.
- **Las páginas de la frase de la audioguía cambiaban 0,16 s antes de acabar la palabra.** Ahora cambian cuando empieza
  la primera palabra de la página siguiente.
- **El golpe de «gratis» era un seno de 46 a 78 Hz**, que el altavoz de un móvil no reproduce. Ahora va
  saturado, con armónicos. Los tics del chat subieron 5 dB y la música del principio, 6.
- **El pie decía «Lo otro no»**, que se lee como que una IA no puede. Ahora dice lo que cambia el viaje.
- **Las insignias** quedaron a 30 px una de otra (un cuarto de su altura, lo que piden las dos tiendas) y
  el cierre lleva las dos líneas de marcas.

Lo que los revisores dijeron y se dejó: que el chat con «Estás aquí» puede leerse como que la IA sabe
dónde estás (el escéptico no lo vio así: la pregunta de la voz deja la respuesta abierta), y que la
oferta no salía entera hasta el segundo 24 (el dueño lo resolvió después con el gancho).

**Lo que nadie ha comprobado**: cómo suena. Las voces, la música y los efectos están transcritos y
medidos, pero no los ha oído una persona.

## Cómo se rehace

```bash
bash ../construir.sh                 # las fuentes embebidas
python3 -I dibujos.py                # los dibujos del molde: assets/dibujos.js
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
- **Un texto centrado no está dentro de la zona segura por estar centrado.** La zona es asimétrica: por
  debajo de y=900 acaba en x=900. Lo que va ahí abajo se centra en la columna libre, no en el lienzo.
- **Un efecto grave se comprueba en la banda que reproduce un móvil** (de 150 Hz para arriba), no en la
  que suena bien en unos cascos.
