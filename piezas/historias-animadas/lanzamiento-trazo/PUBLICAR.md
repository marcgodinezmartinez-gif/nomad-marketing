# Cómo publicar «Un trazo», el anuncio de que Nomad ya está en la App Store

Cuatro ficheros:

- `nomad-trazo-reel-1080x1920.mp4`: el **reel** de Instagram y el vídeo de **TikTok**. Acaba con
  «Enlace en el perfil».
- `nomad-trazo-historia-1080x1920.mp4`: la **historia** de Instagram. Acaba con dos flechas finas que
  señalan abajo, donde va el adhesivo de enlace.
- `nomad-trazo-portada.jpg`: la portada del reel (y la de TikTok, si te deja subirla).
- `nomad-trazo-limpia-1080x1920.mp4`: sólo si hace falta (TikTok sin el campo «Sitio web», o una
  historia promocionada). Acaba sin flecha y sin texto.

Los vídeos duran 17,5 s y ya llevan la música. Pásalos al iPhone por AirDrop o Fotos de iCloud.
**No los mandes por WhatsApp**: los comprime y la letra pequeña se emborrona.

**Tres cosas que valen para todo:**

1. **No le pongas música** de Instagram ni de TikTok. El vídeo ya lleva la suya, cuadrada con lo que
   se ve: las barras que caen, los días de la ruta y el golpe del cierre.
2. **Marca la etiqueta de IA en cada publicación.** La música está generada con IA (Lyria, de Google).
   Lo demás (el dibujo, los textos y los «tic») no lleva IA.
3. **Antes de pagar una promoción, mira la pantalla de pago.** Si aparece «Comisión de Apple», cancela
   y promociona desde el navegador o desde la app Meta Ads Manager (AGENTS.md).

---

## 0. Antes de nada: prueba el enlace en tu iPhone (5 minutos)

En julio y agosto hubo quejas de que el navegador de dentro de Instagram, en iPhone, no abría los
enlaces de la App Store. Apple sí manda abrir la tienda (probado el 27-oct), pero obedecer depende de
Instagram y de TikTok. Antes de publicar:

1. **Historia de prueba**: sube cualquier foto como historia **sólo para Mejores amigos** (y que en la
   lista no haya nadie, o sólo tú), ponle el adhesivo de enlace del paso 2 y tócalo desde tu iPhone.
   Tiene que abrirse la App Store en la ficha de «Nomad: guía de viajes». Bórrala después.
2. **La bio de Instagram**: toca el enlace de tu perfil desde el iPhone. Lo mismo.
3. **La bio de TikTok**, si ya tienes el campo «Sitio web» (paso 3).

Si en alguno se queda en blanco o no abre la tienda: en esa pantalla, **⋯ → Abrir en el navegador
externo** sí la abre. Apunta qué pasó en la issue #13; si falla en los tres, no digas «toca y se abre»
en ningún sitio.

Y comprueba la bio: dice que ya está en la App Store para iPhone y Android pronto, y **no** dice
«Apúntate» ni «lista de espera». En TikTok: **Editar perfil** → **Biografía**:
`Ya en la App Store, para iPhone. Android, pronto 👇`

## Para poder medirlo: el `pt` (opcional, pero sin él no se mide)

Con `https://apps.apple.com/app/id6797973945` la gente llega a la ficha, pero **App Store Connect no
sabrá de dónde vino**. Para saberlo hace falta tu **token de proveedor** (`pt`): App Store Connect → la
app → **Analítica** → **Adquisición** → **Campañas** → **+** (al generar un enlace sale dentro).
Con él, usa sólo **tres** campañas, para que lleguen antes a las 5 primeras descargas que Apple pide
para enseñar una:

| dónde | enlace |
|---|---|
| el adhesivo de la historia | `https://apps.apple.com/app/id6797973945?pt=TU_TOKEN&ct=ig-historia` |
| la bio de Instagram | `https://apps.apple.com/app/id6797973945?pt=TU_TOKEN&ct=ig-bio` |
| la bio de TikTok | `https://apps.apple.com/app/id6797973945?pt=TU_TOKEN&ct=tiktok-bio` |

**No uses `travelsnomad.com/app`** para medir: salta a la tienda y por el camino pierde el `pt`, el
`ct` y el UTM (issue #14). Y ojo: este enlace, abierto en un Android, lleva a la ficha web de la tienda
de EE. UU., donde no se puede instalar nada. Por eso el vídeo dice «Pronto en Android».

---

## 1. Instagram: el reel (@app.nomad)

1. **+** → **Reel** → elige `nomad-trazo-reel-1080x1920.mp4` del carrete → **Siguiente**.
2. En el editor **no toques la música** → **Siguiente**.
3. **Editar portada** → **Añadir del carrete** → `nomad-trazo-portada.jpg`. En la cuadrícula se ve
   recortada a 3:4, y todo cabe dentro.
4. Pega el pie (abajo).
5. **Configuración avanzada** → activa **Etiqueta de IA** («Añadir etiqueta "Información de IA"»).
   Si no la ves ahí, está en la última pantalla, en **Más opciones**.
6. **Mostrar en la cuadrícula: decide tú.** AGENTS.md dice que el feed es fotográfico y éste es un
   vídeo gráfico, sin fotos. Si lo quitas de la cuadrícula, sigue saliendo en la pestaña de reels.
7. **Compartir**.
8. Nada más publicarlo, escribe el comentario de abajo desde @app.nomad y **fíjalo**: mantén pulsado
   el comentario → **Fijar**.

**Pie del reel** (la primera línea es la que se ve antes del «más»):

```
¿Sin cobertura? La audioguía sigue sonando. «Nomad: guía de viajes» ya está disponible para iPhone.

Le dices a dónde vas y qué días, y te deja el viaje escrito: qué ver cada jornada y en qué orden. Después te lo cuenta parada a parada, con audioguías de paseos y museos que se descargan y suenan en modo avión. Y lleva las cuentas del grupo.

Descargarla es gratis. Se paga por viaje, sin suscripción: desde 2,99 €. Una compra abre el viaje a todo el grupo.

Para iPhone con iOS 15.1 o superior. Android, pronto.

El enlace, en la bio.

¿Cuál sería tu primera escapada con ella?

#appdeviajes #viajar #viajes #audioguia #escapada
```

**Comentario para fijar** (Instagram y TikTok):

```
Para encontrarla: App Store, «Nomad: guía de viajes». Hay más apps que se llaman Nomad: fíjate en el icono verde. Necesita un iPhone con iOS 15.1 o superior. Descargarla es gratis; el viaje se paga, sin suscripción. Android: pronto, sin fecha. Síguenos y te avisamos el día que salga.
```

## 2. Instagram: la historia (@app.nomad)

**Súbela desde el carrete, no compartas el reel.** Compartido, el reel se ve con un toque y no lleva
enlace. Subida aparte, lleva el adhesivo.

1. Desliza a **Historia** → elige `nomad-trazo-historia-1080x1920.mp4`. Dura 17,5 s: cabe en una sola.
2. **Adhesivos** → **Enlace** → pega `https://apps.apple.com/app/id6797973945` (o el de `ct=ig-historia`
   si tienes el `pt`) y en «Personalizar el texto del adhesivo» escribe **Descárgala**.
3. **Colócalo abajo, donde apuntan las flechas**: más o menos a un 80 % de la altura, justo encima de
   «Enviar mensaje». El vídeo deja esa franja libre todo el rato; en el cierre queda debajo de la
   letra pequeña de Apple y de las flechas. Déjalo pequeño y **que no tape la insignia**.
4. **Etiqueta de IA**: los tres puntos de arriba a la derecha → **Etiqueta de IA** → activar.
5. **Tu historia**.

Si la quieres **promocionar**: una historia promocionada no admite el adhesivo. Sube aparte
`nomad-trazo-limpia-1080x1920.mp4` y pon el enlace como botón al crear el anuncio, desde el navegador
o desde Meta Ads Manager.

## 3. TikTok

**Antes, una vez:** pasa la cuenta a **cuenta de empresa**: Perfil → ☰ → **Ajustes y privacidad** →
**Cuenta** → **Cambiar a cuenta de empresa** → categoría «Viajes» (o «Apps» si la hay). Después,
Perfil → **Editar perfil** → **Sitio web**: el enlace de la App Store (con `ct=tiktok-bio` si tienes el
`pt`).

**Si el campo «Sitio web» no aparece** (TikTok lo da con 1.000 seguidores o con una cuenta de empresa
registrada, y la app está a tu nombre): sube `nomad-trazo-limpia-1080x1920.mp4` en vez del reel, y
quita del pie la frase «Enlace en el perfil.». El pie ya dice el nombre exacto y el comentario fijado
explica cómo encontrarla.

1. **+** → **Subir** → elige `nomad-trazo-reel-1080x1920.mp4` → **Siguiente**.
2. **No añadas sonido.** Si te sugiere uno, quítalo: el vídeo ya trae el suyo.
3. **Siguiente**. Pega el pie (abajo).
4. **Portada**: si te deja subir una imagen, `nomad-trazo-portada.jpg`. Si no, deja el primer fotograma:
   ya lleva la marca, «¿Sin cobertura?», las barras y la onda.
5. **Más opciones**:
   - activa **Contenido generado por IA** (por la música);
   - activa **Divulgar contenido comercial** → marca **Tu marca**.
6. **Publicar**.
7. Escribe el comentario de arriba y **fíjalo** (mantén pulsado → Fijar).

**Pie de TikTok:**

```
¿Sin cobertura? La audioguía de Nomad sigue sonando: se descarga y suena en modo avión. Antes, te deja el viaje escrito día a día. Se llama «Nomad: guía de viajes» y ya está disponible para iPhone. Descargarla es gratis; el viaje, desde 2,99 € y sin suscripción, y una compra vale para todo el grupo. Android, pronto. Enlace en el perfil.

#viajes #viajar #appdeviajes #audioguia #escapada
```

## Cuándo

**Hoy, martes 27, o mañana, miércoles 28 de octubre de 2026, entre las 19:30 y las 21:00** (hora
peninsular): primero el reel y en el mismo minuto la historia; TikTok, a la misma hora. Es una regla
general, no un dato de la cuenta: si en Instagram, **Panel profesional → Estadísticas → Seguidores →
Momentos de más actividad**, sale otra franja, usa ésa.

**El anuncio de `lanzamiento-ios/` no se publica**: es el que se rechazó el 27-oct. Éste lo sustituye.

## Si algo falla

- **Instagram te pide añadir música**: no hace falta; sigue sin elegir.
- **El vídeo se ve borroso al subirlo**: Instagram → Configuración → Uso de datos y calidad multimedia
  → activa **Subir con la máxima calidad**.
- **No encuentras la etiqueta de IA**: actualiza la app; Meta y TikTok la mueven de sitio.
- **Te preguntan por Android**: «Todavía no. Pronto, pero sin fecha, y no vamos a inventarnos una.
  Síguenos y te avisamos el día que salga.»
- **Te preguntan por qué la insignia no se puede tocar**: es una imagen dentro del vídeo; en ninguna
  red se puede. El enlace está en el adhesivo de la historia y en la bio.
