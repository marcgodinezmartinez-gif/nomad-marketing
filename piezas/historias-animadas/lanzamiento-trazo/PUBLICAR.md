# Cómo publicar «Un trazo», el anuncio de que Nomad ya está en la App Store

Versión 2 (27-oct), la que pediste al ver la primera: abre con el logo, del logo nace la línea, y la
línea va contando cada apartado (lo que eliges al crear el viaje, el plan entero de los tres días, los
paseos y museos que salen de ese plan con su audioguía, la audioguía sin cobertura y sus cuatro voces,
los gastos divididos y Lugares) hasta el cierre que ya aprobaste. Lleva los arreglos de la revisión del
27-oct: cada dibujo se queda entero alrededor de un segundo antes de cambiar, y la frase de cada
apartado va siempre abajo (`README.md`, «Lo que dijo la revisión»). El precio no sale en el vídeo: va
en los pies.

**Y ahora con voz** (27-oct, la opción A que elegiste): Kore, la misma voz de la app, cuenta cada
apartado mientras se dibuja, y debajo va una música nueva, tranquila, de piano y cuerdas, muy por
debajo de la voz. Sin «tic». Cada escena dura lo que su frase, y todo va a 1,15× (voz, música y dibujo, sin cambiar el tono de la
voz), la velocidad que elegiste: el vídeo dura 33,9 s.
Lo que dice Kore:

> Esto es Nomad. · Le dices a dónde vas, cuántos días y cómo te gusta viajar. · Y te escribe el viaje
> entero, día a día. · Paseos y museos, con su audioguía. · Descárgala, y sigue sonando aunque no haya
> cobertura. · Elige la voz que te lo cuenta. Esta, por ejemplo. · Los gastos del grupo, repartidos. ·
> Y tus restaurantes y sitios favoritos, guardados en el mapa. · Nomad. Ya en la App Store, para iPhone.

Es el guion que aprobaste con un cambio: «Cada paseo y cada museo» pasa a **«Paseos y museos»**, como
el texto del vídeo, porque la app no pone audioguía a todos los paseos (en barco, en bici o en kayak no
la lleva) y «cada» prometería de más.

Cuatro ficheros:

- `nomad-trazo-reel-1080x1920.mp4`: el **reel** de Instagram y el vídeo de **TikTok**. Acaba con
  «Enlace en el perfil».
- `nomad-trazo-historia-1080x1920.mp4`: la **historia** de Instagram. Acaba con dos flechas finas que
  señalan abajo, donde va el adhesivo de enlace.
- `nomad-trazo-portada.jpg`: la portada del reel (y la de TikTok, si te deja subirla).
- `nomad-trazo-limpia-1080x1920.mp4`: acaba sin flechas y sin «Enlace en el perfil». Es para **TikTok si
  tu perfil no tiene el campo «Sitio web»** (TikTok no lo da hasta los 1.000 seguidores o una cuenta de
  empresa registrada), porque entonces «Enlace en el perfil» mandaría a un enlace que no existe, y para
  una **promoción pagada**, donde el botón lo pone Meta. Si no es ninguno de los dos casos, no la uses.

Los vídeos duran 33,9 s y ya llevan la voz y la música. Pásalos al iPhone por AirDrop o Fotos de iCloud.
**No los mandes por WhatsApp**: los comprime y la letra pequeña se emborrona.

**Tres cosas que valen para todo:**

1. **No le pongas música** de Instagram ni de TikTok. El vídeo ya lleva su sonido: la voz de Kore y,
   muy por debajo, la música, que se aparta un poco más cada vez que habla. Cada opción se elige cuando
   la voz la nombra, y Kore se queda elegida justo cuando dice «Esta, por ejemplo». **Escúchalo antes
   en el altavoz del iPhone y con auriculares**: está medido, no oído (`README.md`, «La voz» y «La
   música»). Si algo no te gusta, se cambia la frase o la música sin tocar el dibujo. **Una cosa antes**: la regla de la casa es que los reels salen sin pista de audio, y
   la excepción que escribiste en AGENTS.md (24-oct) nombra el anuncio de `lanzamiento-ios/`, el que se
   rechazó, no éste. Confírmalo en la issue #15 (que la excepción pasa a «Un trazo») y se cambia la ruta
   en AGENTS.md en el mismo commit.
2. **Marca la etiqueta de IA en cada publicación.** La voz (Kore, con el modelo de voz de Gemini) y la
   música (Lyria) están generadas con IA, de Google. Meta pide marcar el audio realista creado
   digitalmente, y TikTok, el contenido generado con IA. El dibujo, en cambio, está hecho en código: no
   sale de un generador de imagen ni de vídeo.
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
2. **La bio de Instagram**: primero, pon el enlace. El reel dice «Enlace en el perfil», así que el
   enlace de la bio tiene que llevar a la tienda: **Editar perfil** → **Enlaces** → el de la ficha,
   `https://apps.apple.com/app/id6797973945` (o el de `ct=ig-bio`, si ya tienes el `pt`). Hoy la bio
   lleva `travelsnomad.com` a secas, que fue decisión tuya antes de la tienda
   (`campana/INSTAGRAM-ARRANQUE.md`, #12): desde ahí son dos toques hasta la ficha. Si prefieres
   `travelsnomad.com/app`, también abre la tienda en un iPhone, pero **no mide** (pierde el `pt` y el
   `ct`, #14). Después, toca el enlace de tu perfil desde el iPhone: tiene que abrirse la ficha.
3. **La bio de TikTok**, si ya tienes el campo «Sitio web» (paso 3).

Si en alguno se queda en blanco o no abre la tienda: en esa pantalla, **⋯ → Abrir en el navegador
externo** sí la abre. Apunta qué pasó en la issue #13; si falla en los tres, no digas «toca y se abre»
en ningún sitio.

Y dos preguntas antes de subirlo. **«Pronto en Android» va dentro del vídeo**, y una vez publicado no se
cambia. En #13 sigue abierta la casilla «¿Android sale pronto de verdad?». Si puede tardar meses,
dilo antes: se cambia a «En camino para Android» y se vuelve a renderizar en unos minutos. Y el vídeo
dice **«la App Store»** (como la casa) durante 21 s y acaba en la insignia de Apple, que dice **«el App
Store»**. No incumple nada, pero no casa: si prefieres el masculino de Apple, se cambia en la cabecera,
la apertura, la portada y los pies, y se vuelve a renderizar.

Y comprueba la bio: dice que ya está en la App Store para iPhone y Android pronto, y **no** dice
«Apúntate» ni «lista de espera». En TikTok: **Editar perfil** → **Biografía**:
`Ya en la App Store, para iPhone. Android, pronto 👇`

## Para poder medirlo: el `pt` (opcional, pero sin él no se mide)

Con `https://apps.apple.com/app/id6797973945` la gente llega a la ficha, pero **App Store Connect no
sabrá de dónde vino**. Para saberlo hace falta un **enlace de campaña**: App Store Connect → la app →
**Analítica** → **Adquisición** → **Campañas** → **+**. **Copia tal cual el enlace que te da** (lleva
tu token de proveedor, `pt`, y la forma de Apple: `…/app/apple-store/id6797973945?pt=…&ct=…&mt=8`) y
cambia sólo el `ct`. No lo escribas a mano. Usa sólo **tres** campañas, para que lleguen antes a las
5 primeras descargas que Apple pide para enseñar una, con los nombres de #13 y #14:

| dónde | `ct` |
|---|---|
| el adhesivo de la historia | `ig-historia-anuncio` |
| la bio de Instagram | `ig-bio` |
| la bio de TikTok | `tt-bio` |

**No uses `travelsnomad.com/app`** para medir: salta a la tienda y por el camino pierde el `pt`, el
`ct` y el UTM (issue #14). Y ojo: este enlace, abierto en un Android, lleva a la ficha web de la App
Store, donde desde un Android no se puede instalar nada. Por eso el vídeo dice «Pronto en Android».

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
«Nomad: guía de viajes» ya está en la App Store, para iPhone. Así funciona, de un trazo.

Le dices a dónde vas, qué días, tu estilo, tu ritmo y tu presupuesto, y te sale el plan entero, día a día: visitas, comidas y horas.

Los paseos a pie y los museos del plan llevan su audioguía. Las que descargas funcionan en modo avión, y eliges entre cuatro voces.

Apuntáis los gastos del grupo y la app los divide y os dice quién debe a quién. Y en Lugares guardas tus restaurantes y sitios de interés, en el mapa del viaje.

La voz que lo cuenta es Kore, una de las que puedes elegir en la app. La voz y la música están hechas con IA.

Descargarla es gratis. Se paga por viaje, sin suscripción: desde 2,99 €. Una compra abre el viaje a todo el grupo.

Para iPhone con iOS 15.1 o superior. Android, pronto.

El enlace, en la bio.

¿A dónde sería tu primer viaje con ella?

#appdeviajes #viajar #viajes #audioguia #escapada
```

**Comentario para fijar** (Instagram y TikTok):

```
Para encontrarla: App Store, «Nomad: guía de viajes». Hay más apps que se llaman Nomad: fíjate en el icono crema con la marca verde. Necesita un iPhone con iOS 15.1 o superior. Descargarla es gratis; el viaje se paga, sin suscripción. Android: pronto, sin fecha. Síguenos y te avisamos el día que salga.
```

## 2. Instagram: la historia (@app.nomad)

**Súbela desde el carrete, no compartas el reel.** Compartido, el reel se ve con un toque y no lleva
enlace. Subida aparte, lleva el adhesivo.

1. Desliza a **Historia** → elige `nomad-trazo-historia-1080x1920.mp4`. Dura 33,9 s: cabe en una sola (el límite es 60).
2. **Adhesivos** → **Enlace** → pega `https://apps.apple.com/app/id6797973945` (o el de
   `ct=ig-historia-anuncio` si tienes el `pt`) y en «Personalizar el texto del adhesivo» escribe **Descárgala**.
3. **Colócalo abajo, donde apuntan las flechas**: más o menos a un 80 % de la altura, justo encima de
   «Enviar mensaje». El vídeo deja esa franja libre todo el rato; en el cierre queda debajo de la
   letra pequeña de Apple y de las flechas. Déjalo pequeño y **que no tape la insignia**.
4. **Etiqueta de IA**: los tres puntos de arriba a la derecha → **Etiqueta de IA** → activar.
5. **Tu historia**.

Si la quieres **promocionar**: una historia promocionada no admite el adhesivo. Sube aparte
`nomad-trazo-limpia-1080x1920.mp4` y pon el enlace como botón al crear el anuncio, desde el navegador
o desde Meta Ads Manager. **No es un paso de un minuto**: el botón que lleva a la App Store
(«Instalar», «Descargar») sólo existe con el objetivo **«Promoción de la app»**, y ese objetivo pide
dar de alta la app en **Meta for Developers**. La app no lleva el SDK de Meta, así que el anuncio sólo
se podrá optimizar para clics. Sin eso hecho, no se promociona la historia.

## 3. TikTok

**Antes, una vez:** pasa la cuenta a **cuenta de empresa**: Perfil → ☰ → **Ajustes y privacidad** →
**Cuenta** → **Cambiar a cuenta de empresa** → categoría «Viajes» (o «Apps» si la hay). Después,
Perfil → **Editar perfil** → **Sitio web**: el enlace de la App Store (con `ct=tt-bio` si tienes el
`pt`).

**Si el campo «Sitio web» no aparece** (TikTok lo da con 1.000 seguidores o con una cuenta de empresa
registrada, y la app está a tu nombre): sube `nomad-trazo-limpia-1080x1920.mp4` en vez del reel, y
quita del pie la frase «Enlace en el perfil.». El pie ya dice el nombre exacto y el comentario fijado
explica cómo encontrarla.

1. **+** → **Subir** → elige `nomad-trazo-reel-1080x1920.mp4` → **Siguiente**.
2. **No añadas sonido.** Si te sugiere uno, quítalo: el vídeo ya trae el suyo.
3. **Siguiente**. Pega el pie (abajo).
4. **Portada**: si te deja subir una imagen, `nomad-trazo-portada.jpg`. Si no, deja el primer fotograma:
   ya lleva el logo, «Nomad: guía de viajes» y «Ya en la App Store, para iPhone».
5. **Más opciones**:
   - activa **Contenido generado por IA** (por la voz y la música);
   - activa **Divulgar contenido comercial** → marca **Tu marca**.
6. **Publicar**.
7. Escribe el comentario de arriba y **fíjalo** (mantén pulsado → Fijar).

**Pie de TikTok:**

```
«Nomad: guía de viajes» ya está en la App Store, para iPhone. Eliges destino, días, estilo, ritmo y presupuesto, y te sale el plan entero, día a día. Paseos y museos, con su audioguía: las descargadas funcionan en modo avión, y hay cuatro voces. Los gastos del grupo, divididos, y tus restaurantes y sitios de interés, guardados en Lugares. Descargarla es gratis; el viaje, desde 2,99 € y sin suscripción. Android, pronto. Enlace en el perfil.

#viajes #viajar #appdeviajes #audioguia #escapada
```

## Cuándo

**Hoy, martes 27, o mañana, miércoles 28 de octubre de 2026, entre las 19:30 y las 21:00** (hora
peninsular): primero el reel y en el mismo minuto la historia; TikTok, a la misma hora. Es una regla
general, no un dato de la cuenta: si en Instagram, **Panel profesional → Estadísticas → Seguidores →
Momentos de más actividad**, sale otra franja, usa ésa.

**El anuncio de `lanzamiento-ios/` no se publica**: es el que se rechazó el 27-oct. **Ni la primera
versión de «Un trazo»** (17,5 s, la que acababa en el precio): ésta la sustituye.

## Si algo falla

- **Instagram te pide añadir música**: no hace falta; sigue sin elegir.
- **El vídeo se ve borroso al subirlo**: Instagram → Configuración → Uso de datos y calidad multimedia
  → activa **Subir con la máxima calidad**.
- **No encuentras la etiqueta de IA**: actualiza la app; Meta y TikTok la mueven de sitio.
- **Te preguntan por Android**: «Todavía no. Pronto, pero sin fecha, y no vamos a inventarnos una.
  Síguenos y te avisamos el día que salga.»
- **Te preguntan por las voces**: «Son cuatro: la del teléfono, que no necesita internet, y Kore, Puck y
  Charon, que se escuchan antes de elegir. Para oír una de esas tres sin cobertura, descarga el audio
  del tour antes de salir.»
- **Te preguntan cuánto cuesta**: «Descargarla es gratis. El viaje se paga una vez, sin suscripción:
  2,99 € hasta 3 días, 4,99 € de 4 a 7 y 6,99 € de 8 a 30. Una compra vale para todo el grupo.»
- **Te preguntan por qué la insignia no se puede tocar**: es una imagen dentro del vídeo; en ninguna
  red se puede. El enlace está en el adhesivo de la historia y en la bio.
