# Cómo publicar el anuncio del lanzamiento

> **Rechazado por el dueño el 27-oct** (*«los recortes de la app se ven mal y reutilizamos vídeos de
> cosas ya anunciadas»*). No se publica: lo sustituye `../lanzamiento-trazo/`, que se queda con su
> cierre. Esto se guarda como registro y por lo que enseñó (la mezcla, la insignia, el cierre).

Dos ficheros, y nada más que hacer con ellos:

- `nomad-lanzamiento-1080x1920.mp4`: el vídeo. Dura 24,6 s y ya lleva la música y la voz. Es el
  mismo para el reel, la historia y TikTok.
- `nomad-lanzamiento-portada.jpg`: la portada del reel.

Pásalos al iPhone (AirDrop o Fotos de iCloud). **No los mandes por WhatsApp**: los comprime y
el texto de las pantallas se emborrona.

**Tres cosas que valen para todo:**

1. **No le pongas música** de Instagram ni de TikTok. El vídeo ya lleva la suya, y además la voz
   de la audioguía.
2. **Marca la etiqueta de IA en cada publicación.** La música, la voz y la narración están
   generadas con IA (Lyria y Gemini TTS). Meta exige marcar el audio realista creado
   digitalmente, y TikTok, el contenido generado con IA.
3. **Antes de pagar una promoción, mira la pantalla de pago.** Si aparece «Comisión de Apple»,
   cancela y promociona desde el navegador o desde la app Meta Ads Manager (AGENTS.md).

---

## 0. Antes de publicar: la bio (Instagram y TikTok)

El dueño dijo el 24-oct que el perfil de Instagram ya está limpio (issue #12). Sólo una comprobación,
porque el pie manda a la bio:

1. Instagram → tu perfil: la bio dice que ya está en la App Store para iPhone y Android pronto, y
   **no** dice «Apúntate» ni «lista de espera».
2. Toca el enlace de la bio desde tu iPhone: tiene que abrir la ficha de «Nomad: guía de viajes».
3. TikTok → **Editar perfil** → **Biografía**: `Ya en la App Store, para iPhone. Android, pronto 👇`

---

## 1. Instagram: el reel (@app.nomad)

1. **+** → **Reel** → elige `nomad-lanzamiento-1080x1920.mp4` del carrete → **Siguiente**.
2. En el editor **no toques la música** → **Siguiente**.
3. **Editar portada** → **Añadir del carrete** → `nomad-lanzamiento-portada.jpg`. En la cuadrícula
   se ve recortada a 3:4, y el texto cabe dentro.
4. Pega el pie (abajo).
5. **Configuración avanzada** → activa **Etiqueta de IA** («Añadir etiqueta "Información de IA"»).
   Si no la ves ahí, está en la última pantalla, en **Más opciones**.
6. Deja activado **Mostrar en la cuadrícula**.
7. **Compartir**.
8. Nada más publicarlo, escribe el comentario de abajo desde @app.nomad y **fíjalo**: mantén
   pulsado el comentario → **Fijar**.

**Pie del reel** (la primera línea es la que se ve antes del «más»):

```
Nomad ya está en la App Store. Se llama «Nomad: guía de viajes».

Le dices a dónde vas y cómo te gusta viajar, y escribe el viaje día a día: qué ver cada jornada y en qué orden. Después te lo cuenta parada a parada, con audioguías de paseos y museos que se descargan y suenan sin cobertura. Y además, qué hay esos días en la ciudad y los gastos del grupo.

Lo que suena es un trozo de la parada del Templo de Debod, en Madrid: el texto que escribió la app, leído con Kore, una de las voces que puedes elegir en ella.

Descargarla es gratis. Se paga por viaje, sin suscripción: desde 2,99 €.

Para iPhone con iOS 15.1 o superior. Android, pronto.

El enlace, en la bio.

#appdeviajes #viajar #viajes #audioguia #escapada
```

**Comentario para fijar** (Instagram y TikTok):

```
Para encontrarla: App Store, «Nomad: guía de viajes». Hay más apps que se llaman Nomad: fíjate en el icono. Necesita un iPhone con iOS 15.1 o superior. Descargarla es gratis; el viaje se paga, sin suscripción. Android: pronto, sin fecha. Síguenos y te avisamos el día que salga.
```

## 2. Instagram: la historia (@app.nomad)

**Súbela desde el carrete, no compartas el reel.** Si compartes el reel, la gente lo ve con un
toque desde la historia y no tiene enlace. Subido aparte, lleva el adhesivo de enlace.

1. Desliza a **Historia** → elige el mismo `nomad-lanzamiento-1080x1920.mp4`. Dura 24,6 s:
   cabe en una sola historia.
2. **Adhesivos** → **Enlace** → pega el enlace directo a la ficha de la App Store:
   `https://apps.apple.com/app/id6797973945`
   y en «Personalizar el texto del adhesivo» escribe **Descárgala**.

   **Con ese enlace la historia NO se puede medir**: App Store Connect no sabrá que la descarga
   vino de aquí. Para medirla hace falta tu token de proveedor (`pt`), que está en App Store
   Connect → la app → **Analítica** → **Fuentes** → **Enlaces de campaña** (o al generar uno ahí
   mismo). Si lo tienes a mano, pega en su lugar
   `https://apps.apple.com/app/id6797973945?pt=TU_TOKEN&ct=ig-historia-anuncio`
   (issues #13 y #14). **No uses `travelsnomad.com/app?utm_…`**: esa página salta a la
   tienda y por el camino tira el UTM, así que tampoco mide, y en un Android lleva a la portada.
3. **Coloca el adhesivo abajo, por debajo de la franja del texto**: más o menos a un 80 % de la
   altura, justo encima de «Enviar mensaje». Ahí no tapa nada en ningún momento del vídeo (en el
   cierre queda debajo de «Pronto en Android»). Déjalo pequeño.
4. **Etiqueta de IA**: los tres puntos de arriba a la derecha → **Etiqueta de IA** → activar.
5. **Tu historia**.

Y en la cuenta personal, si quieres, lo mismo (subida desde el carrete, nunca compartiendo el
reel), con una mención a @app.nomad; con el token, `ct=ig-historia-anuncio-personal`.

## 3. TikTok

**Antes, una vez:** pasa la cuenta a **cuenta de empresa**: Perfil → ☰ → **Ajustes y
privacidad** → **Cuenta** → **Cambiar a cuenta de empresa** → categoría «Viajes» (o «Apps» si
la hay) → **Siguiente**. Pon en la bio el enlace `https://travelsnomad.com/app` (Perfil → Editar
perfil → Sitio web).

**Si el campo «Sitio web» no aparece** (TikTok lo da según el tipo de cuenta y, en algunos
sitios, según los seguidores, y la cuenta es nueva): quita del pie la frase «Enlace en el
perfil.». El pie ya dice el nombre exacto, «Nomad: guía de viajes», y el comentario fijado
explica cómo encontrarla.

1. **+** → **Subir** → elige `nomad-lanzamiento-1080x1920.mp4` → **Siguiente**.
2. **No añadas sonido.** Si te sugiere uno, quítalo: el vídeo ya trae el suyo.
3. **Siguiente**. Pega el pie (abajo).
4. **Portada**: si te deja subir una imagen, usa `nomad-lanzamiento-portada.jpg`. Si no, arrastra
   el selector hasta **el segundo 1**: el templo con «La ciudad, contada.» y la tarjeta de Nomad.
   (El primer fotograma ya lleva el texto y la marca, así que dejarlo como viene también vale.)
5. **Más opciones**:
   - activa **Contenido generado por IA** («Etiqueta de contenido generado por IA»);
   - activa **Divulgar contenido comercial** → marca **Tu marca**.
6. **Publicar**.
7. Escribe el comentario de arriba y **fíjalo** (mantén pulsado → Fijar).

**Pie de TikTok:**

```
Le dices a dónde vas y Nomad escribe el viaje día a día. Después te lo cuenta parada a parada, también sin cobertura. Se llama «Nomad: guía de viajes» y ya está en la App Store. Descargarla es gratis; el viaje, desde 2,99 € y sin suscripción. Android, pronto. Enlace en el perfil.

#viajes #viajar #appdeviajes #audioguia #escapada
```

## Cuándo

**Hoy, martes 27, o mañana, miércoles 28 de octubre de 2026, entre las 19:30 y las 21:00** (hora
peninsular): primero el reel y en el mismo minuto la historia; TikTok, a la misma hora. Iba a
salir el domingo 25 y no salió. Es una regla general, no un dato de la cuenta: si en Instagram,
**Panel profesional → Estadísticas → Seguidores → Momentos de más actividad**, sale otra franja,
usa ésa. Para la próxima pieza, el domingo por la tarde, que es cuando se piensa en la escapada.

## Si algo falla

- **Instagram te pide añadir música**: no hace falta; sigue sin elegir.
- **El vídeo se ve borroso al subirlo**: Instagram → Configuración → Uso de datos y calidad
  multimedia → activa **Subir con la máxima calidad**.
- **No encuentras la etiqueta de IA**: actualiza la app; Meta y TikTok la mueven de sitio.
- **Te preguntan por Android**: «Todavía no. Pronto, pero sin fecha, y no vamos a inventarnos una.
  Síguenos y te avisamos el día que salga.»
