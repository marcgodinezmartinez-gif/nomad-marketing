# La historia para buscar testers de Android (26-oct)

Google Play denegó el acceso a producción porque los testers estaban poco implicados, y pide otros
14 días de prueba cerrada con testers **reales**. El dueño descarta pagar servicios de testers y
Reddit, así que hay que reunir entre 15 y 20 personas con Android de su círculo y de los seguidores
de @app.nomad. Esta pieza es la historia de Instagram para eso, en castellano y en italiano, porque la
mitad de los seguidores son italianos y la app está en italiano.

Cómo se publica: `PUBLICAR.md`. Los textos que se pegan, versionados aquí al lado para no perderlos con
el contenedor: `textos/grupo-bienvenida.txt` (los pasos, en castellano, italiano e inglés, para el
**Mensaje de bienvenida** del grupo de Google, que es lo que sale arriba de la página a la que lleva el
enlace), `textos/grupo-descripcion.txt` (una línea para la descripción, que sólo sale en la pestaña
*Información*) y `textos/mensajes-whatsapp.txt` (castellano, italiano, el de reenviar y el recordatorio
del día 7).

## Lo que se ve, segundo a segundo (10 s, 1080×1920, 30 fps)

| s | qué |
|---|---|
| 0 | El Coliseo al atardecer, a sangre y quieto, con una banda oscura arriba. Ya están el icono de la app con «Nomad · ANDROID» y, grande, **«¿Tienes Android?»** / «Hai Android?». Es el primer vistazo: en un segundo se sabe de quién es y a quién le habla |
| 0,35-1,1 | Entran «Prueba Nomad» y, en menta, «antes de que salga.» (en italiano, «Prova Nomad / prima che esca.») |
| 1,25-1,9 | La línea de qué es: «Te escribe el viaje día a día / y te lo cuenta con audioguías.» («Ti prepara il viaggio giorno per giorno / e te lo racconta con le audioguide.») |
| 1,9-2,8 | **Sólo la castellana**: sube desde fuera del cuadro, opaca, la pantalla real del itinerario: el sábado de un viaje a Roma, con «Coliseo y Foro Romano» y su «Iniciar tour» |
| 3,2-3,75 (it: 2,1-2,65) | Entra con un golpe pequeño la cápsula menta: **«Genera tus viajes gratis / durante la prueba.»** |
| 4,3-4,8 (it: 3,1-3,6) | Entra «Toca «Únete a la prueba»» («Tocca «Partecipa al test»»), con el texto exacto del adhesivo, y debajo dos chevrones menta que botan 20 px hacia él hasta el final |
| hasta 10 | Todo quieto salvo los chevrones: cinco segundos (seis en la italiana) para leerlo y tocar el adhesivo |

A los 3 segundos ya se sabe qué piden y a quién.

## Las decisiones, y por qué

- **Animada y no dos tarjetas.** El mensaje cabe en una sola pantalla. Si fuera fija, «¿Tienes Android?»
  y el gancho tendrían que competir desde el primer fotograma; animada, se leen en ese orden. Además, una
  historia de 10 s no tiene que esperar a que Instagram la pase (una foto también dura unos 5 s). Por si
  acaso, `render.sh` deja también el último fotograma en PNG.
- **Sin música (una pista AAC en silencio).** Hay tres motivos. (1) La música de Lyria del anuncio está
  generada con IA y obliga a etiquetar la publicación como «Información de IA». En una pieza que pide
  confianza a gente que no conoce la app, esa etiqueta resta, y más con el dueño desconfiando de las webs
  de testers por parecer «hechas con IA». (2) Una historia que pide un favor se lee, no se escucha, y casi
  todo el mundo las pasa sin sonido. (3) La regla de la casa es elegir el audio dentro de Instagram. La
  pista en silencio es para que el fichero sea H.264 + AAC, que es lo que mejor aceptan las subidas.
  Medido en el máster: −91 dB de pico, o sea silencio digital.
- **El Coliseo y el día de Roma van juntos.** La pantalla empieza en «Coliseo y Foro Romano», así que la
  foto y la app cuentan el mismo viaje. La foto es CC0 (no hay que acreditar a nadie).
- **La italiana, sin pantalla (revisión del 26-oct).** La primera versión usaba `plan-900-it.webp` del
  banco, y no es una captura: es la castellana con los textos cambiados a mano en otra fuente (la fecha
  en una serif ancha, la tarjeta y «Inizia il tour» en una sans tipo Arial, la píldora sin borde, y un
  resto de la sustitución que hubo que borrar). Pegada al titular en Instrument Serif, se notaba: es el
  «se ve hecho con IA» que no puede tener una pieza que pide confianza, y la regla de la casa es
  «capturas de la app real, nunca maquetas». Sin captura, la italiana enseña el Coliseo entero y el
  gancho llega antes. Cuando haya una captura hecha en un móvil con la app en italiano, se pone en
  `PANTALLA` de `preparar.py` y vuelve a salir, sin retoques. Las otras `*-it`, `*-en` y `*-fr` del banco
  tienen el mismo problema (#17).
- **El gancho es el de Google, y nada más.** «Prueba Nomad antes de que salga» y «Genera tus viajes
  gratis durante la prueba» son ciertos si los miembros del grupo son testers con licencia (PUBLICAR,
  paso 0.1): Google Play les enseña una compra de prueba. No hay nada a cambio de reseñas (los testers no
  pueden reseñar) ni nada prometido para después.
- **«antes de que salga» y no «antes que nadie».** Nomad está en la App Store desde el 19-oct y la cuenta
  lo anunció el 24-oct: «antes que nadie» sólo era cierto leído como «en Android», y un seguidor que vio
  el anuncio lo leería como exageración. «antes de que salga», debajo de «¿Tienes Android?», es exacto y
  casa con el «pronto» del lanzamiento.
- **«Te escribe el viaje día a día y te lo cuenta con audioguías»** sale de la ficha y del anuncio del
  lanzamiento. No se dice «voz real» ni «tiempo real», y no hay precio: durante la prueba no se paga.
- **La marca dice sólo «ANDROID»**: con «ANDROID · PRUEBA», «prueba» salía tres veces en pantalla. Y nunca
  «prueba cerrada», que es jerga de Play Console.
- **La pantalla, sin marco y sin barra de estado**: es el recorte desde el borde de la hoja hasta 25 px
  por debajo de la tarjeta del Coliseo. La primera versión llegaba a la parada 2, y la cápsula del gancho
  (que va encima del pie de la pantalla) tapaba la mitad de la tarjeta. El viaje es de ejemplo y no lleva
  datos de nadie.
- **«Toca «Únete a la prueba»» nombra el adhesivo con su texto exacto**, en una cápsula oscura que se lee
  sobre cualquier parte del Coliseo iluminado. La primera versión decía «Toca el enlace» con un chevrón
  DENTRO de la cápsula, y parecía un desplegable. Ahora son dos chevrones de CSS fuera, debajo, con
  sombra y botando 20 px (las fuentes no tienen «↓» y el emoji no sale en color). Si cambia el texto del
  adhesivo en PUBLICAR, cambia aquí (`TEXTOS`).
- **Zonas seguras de historia**: la marca empieza en y=290, la cápsula acaba en y=1440 y la punta más baja
  de los chevrones, en lo más hondo del rebote, en y=1507 (medido sobre los fotogramas de los dos vídeos).
  De 1520 para abajo solo hay foto: ahí va el adhesivo. Se ve en `revision/zonas-seguras-*.jpg` de la
  entrega.
- **Una composición raíz por proyecto.** HyperFrames la exige (`check` falla con
  `multiple_root_compositions` si hay dos HTML con `data-composition-id`). Por eso la plantilla es
  `plantilla.html.in`, y `preparar.py <idioma>` escribe `index.html` en ese idioma. El versionado es el
  castellano.
- `check` pasa en los dos idiomas con 0 errores y 0 avisos, y en contraste WCAG AA **41/41** la
  castellana y **43/43** la italiana (26-oct, después de la revisión). Una de las pasadas de la castellana dio `check_runtime_failure: Browser process did
  not exit after forced shutdown`, un fallo del Chrome del contenedor al cerrarse. Repetida, pasó limpia.

## Para rehacerla

```bash
python3 piezas/historias-animadas/testers-android/preparar.py      # assets e index.html (es)
bash piezas/historias-animadas/testers-android/render.sh [carpeta]  # las dos, ~1 min 30 s
```

`render.sh` corre `construir.sh` (las fuentes embebidas), y para cada idioma prepara, pasa `check`,
renderiza a 10 Mb/s, añade la pista AAC en silencio con `+faststart` y saca el último fotograma en PNG.
Al acabar deja `index.html` en castellano. Por defecto escribe en `salida/` (no se versiona). Usa
`npx -y hyperframes@0.8.203`, la misma versión que las otras piezas.

Para cambiar un texto, se cambia la tabla `TEXTOS` de `preparar.py`. Para cambiar la maquetación, se
cambia `plantilla.html.in`. Nunca `index.html` a mano.

## De dónde sale cada cosa

| Recurso | Origen | Licencia |
|---|---|---|
| `fondo-coliseo.jpg` | `banco/fotos/historia/f-portada.jpg`, «Colosseum of Rome, Italy» (Wikimedia Commons) | CC0, sin atribución obligatoria |
| `pantalla-es.png` | `banco/capturas/plan-900.webp`, y 296-890, a 620 de ancho. La italiana no lleva pantalla: no hay captura real en italiano | captura de la app |
| `icono-app.png` | `banco/marca/` | propio |
| Fuentes | Instrument Serif e Instrument Sans, `banco/fuentes/webfonts/`, embebidas por `construir.sh` | OFL |
| `gsap.min.js` | copia de `plan-cordoba/assets/` | licencia de GSAP |

## Lo que no está, a propósito

Precio, 1,99 €, lista de espera, «voz real», «tiempo real», cualquier fecha de Android, un iPhone
dibujado, la App Store, nada a cambio de una reseña y nada prometido después de la prueba. Tampoco el
francés ni el inglés: no tienen ni una señal en la cuenta (AGENTS.md). El inglés sí está en la
descripción del grupo, porque esa página la puede ver cualquiera que reciba el enlace.
