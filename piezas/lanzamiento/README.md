# El lanzamiento

## «Nomad ya está en la App Store» (24-oct) — `gen-ios.py`

Carrusel de 6 tarjetas de 1080×1350 con el anuncio de que la app está en iPhone y de que
Android llega pronto (sin fecha). **Sustituye al «¿Qué pasa el día que abra NOMAD?»** de más
abajo, que prometía una lista de espera que ya no existe: la tienda abrió el 19-oct, la web
oculta la lista con una tienda encendida (`tienda.js` de la web) y el dueño la cerró para todos
el 17-oct (NOMAD#305).

| # | Tarjeta | Foto |
|---|---|---|
| 1 | El anuncio: «Nomad ya está en la App Store» + icono y nombre exacto | `f-sagrada-pasion.jpg` (del dueño) |
| 2 | «Tú dices dónde. Nomad lo escribe.» — móvil de crear viaje | `f-bcn-cierre.jpg` |
| 3 | «La ciudad, contada.» — móvil de la audioguía | `f-bcn-noche.jpg` |
| 4 | «Los gastos, en paz.» — móvil de gastos | `f-grupo.jpg` |
| 5 | «Desde 2,99 € el viaje entero» — la tabla por días | `f-precio.jpg` |
| 6 | Cómo encontrarla: el nombre exacto, el icono, la insignia de Apple y Android | `f-sagrada-estanque.jpg` |

```bash
python3 piezas/lanzamiento/recortar-moviles.py     # una vez (y si la ficha cambia sus capturas)
bash piezas/preparar.sh
cd salida && python3 ../piezas/lanzamiento/gen-ios.py
node ../piezas/roma/exportar-plan.mjs ios 6
```

**De dónde sale cada dato** (todo de la ficha pública, consultada el 24-oct con
`itunes.apple.com/lookup?id=6797973945&country=es`): el nombre «Nomad: guía de viajes», que la
descarga es gratis, los tres precios por viaje, «sin suscripción», «una compra abre el viaje
para todo el grupo», las audioguías que se descargan y suenan sin cobertura. Los titulares de
las tarjetas 2-4 son los de las capturas de la propia ficha.

**Las capturas son las de la ficha**, no las del banco anterior (issue #5): son la app de hoy.
`recortar-moviles.py` las baja de la API pública y recorta el móvil de las tres que lo llevan
recto. La insignia «Consíguelo en el App Store» es la oficial de Apple, **sin tocar**
([normas](https://developer.apple.com/app-store/marketing/guidelines/)).

**Lo que NO está en las tarjetas, a propósito:** el 1,99 € de la lista (ya no se ofrece a nadie
nuevo, y cómo lo canjean quienes estaban dentro no lo sabe este repo), idiomas (la ficha lista
EN FR DE IT ES; la casa dice cuatro) y cualquier fecha de Android.

**Dos cosas de la ficha que hay que saber al promocionar:** está **solo en español en todos los
países** (nombre, descripción y capturas), y el nombre se repite con media docena de apps
«Nomad» (de ahí el cierre: nombre exacto, icono, insignia).

### El pie, la bio y lo demás del día (verificado el 24-oct contra la ficha y AGENTS.md)

El panel de copy escribió tres versiones independientes (producto, voz, novedad) y un verificador
adversarial las rompió contra los hechos de la ficha y las reglas de precio (17 correcciones:
«gratis» sólo acompaña a «descargarla», sin «voz real» ni «tiempo real», sin los 0,99 € de la visita
suelta —contradicen el «desde»—, sin nombre del dueño en el comentario, sin el 1,99 € en nada
público). Lo que quedó:

> Nomad ya está en la App Store, para iPhone. Descargarla es gratis. Android, pronto.
>
> Se llama «Nomad: guía de viajes». Hay más apps que se llaman Nomad: fíjate en el icono. El
> enlace, en la bio.
>
> Dices a dónde vas y qué días. Nomad escribe el viaje entero: qué ver cada jornada, en qué orden y
> cuánto cuesta. Y luego te lo cuenta al oído mientras lo andas.
>
> Lo que hay dentro:
> · El itinerario, día a día.
> · Audioguías para pasear una ciudad o recorrer un museo. Se descargan y suenan sin cobertura.
> · Un asistente al que preguntar sobre la marcha, que ve por la cámara lo que tienes delante.
> · Los gastos del grupo, con quién debe qué a quién.
> · El viaje de otra persona, que puedes copiar y amoldar a tus días.
>
> Descargarla es gratis. Se paga por viaje, sin suscripción ni renovaciones: desde 2,99 € el viaje
> entero. Son 2,99 € hasta 3 días, 4,99 € de 4 a 7 y 6,99 € de 8 a 30. Una compra abre el viaje para
> todo el grupo. Y la escapada de hasta 3 días sale por poco más que un café.
>
> Android: pronto, sin fecha. Síguenos y te avisamos el día que salga.
>
> Los días escritos. La ciudad, contada.
>
> #appdeviajes #audioguia #viajar #viajes #itinerario #iphone

La primera línea mide 83 caracteres: el golpe entero antes del «ver más». Sin `#nomad` ni
`#nomads` a propósito (son de nómadas digitales). «Poco más que un café» sólo vale para la escapada
de hasta 3 días y sólo en el pie; si suena forzado, se corta esa frase sin tocar nada más.

- **Bio** (última línea): «Ya en la App Store, para iPhone. Android, pronto 👇». El enlace:
  `travelsnomad.com/app` (en un iPhone salta a la ficha; en un Android cae en «Muy pronto en
  Android») o la portada a secas; lo decide el dueño.
- **Comentario para fijar:** «Para encontrarla: App Store, "Nomad: guía de viajes". Hay más apps
  que se llaman Nomad: fíjate en el icono. Necesita un iPhone con iOS 15.1 o superior. Descargarla
  es gratis; el viaje se paga, sin suscripción. Android: pronto, sin fecha. Síguenos y te avisamos
  el día que salga.»
- **A «¿y en Android?»:** «Todavía no. Pronto, pero sin fecha, y no vamos a inventarnos una.
  Síguenos y te avisamos el día que salga.»
- **Historias** (`gen-ios-historias.py`): `iosh-1` el anuncio, con el adhesivo de enlace por debajo
  de y=1520 (enlace de campaña directo a la ficha, no `/app`); `iosh-2` «¿Y en Android?».
  **Una tercera, para quienes estaban en la lista** («gracias por llegar antes, ya puedes
  descargarla, te hemos escrito aparte»), no se publica hasta que el dueño confirme cómo canjean
  su 1,99 € y les haya escrito antes de que lo vean en el feed.

**Lo que hay que confirmar antes de publicar** (lo dejó el verificador): qué se ve antes de pagar un
viaje y si hay prueba gratuita (será la primera pregunta en los comentarios); cómo canjean el 1,99 €
las 14 personas de la lista; que Android va a salir «pronto» de verdad; que el asistente con cámara y
«copiar el viaje de otra persona» funcionan como los anuncia la ficha; qué idiomas tiene la app (la
ficha lista EN FR DE IT ES; la casa dice cuatro y el alemán no consta).

## «¿Qué pasa el día que abra NOMAD?» (29-sep) — `gen-abre.py` — OBSOLETO desde el 19-oct


Cinco tarjetas de 1080×1350 para la semana del cierre de la lista, que es la que el plan de
agosto marcaba como la que más altas trae (`campana/LANZAMIENTO-PUBLICIDAD.md`: *«una lista
que se cierra es una razón para apuntarse hoy en vez de "ya me apuntaré"»*).

| # | Tarjeta | Foto |
|---|---|---|
| 1 | ¿Qué pasa el día que abra NOMAD? — «Octubre empieza el jueves» | `f-porto.jpg` |
| 2 | Lo que va dentro — el móvil con el tour a pie de Debod: mapa, ruta y audioguía | `f-santiago.jpg` |
| 3 | Cada viaje, desde 2,99 € — la tabla de la web por días | `f-precio.jpg` |
| 4 | Si estás en la lista: tu primer viaje, 1,99 €, dure lo que dure | `f-oia.jpg` |
| 5 | El día que abramos, la lista se cierra — y el botón de apuntarse | `f-segovia.jpg` |

```bash
bash piezas/preparar.sh
cd salida && python3 ../piezas/lanzamiento/gen-abre.py
node ../piezas/roma/exportar-plan.mjs abre 5
```

**Antes de publicarlo, una condición que no es de diseño**: el post promete en público que
la lista se cierra el día que abra la tienda y que el 1,99 € se queda para quien esté dentro.
Es lo que dice el plan desde agosto, pero es una promesa: **si después de abrir se va a
seguir dando el 1,99 €, este post no sale**. Urgencia falsa es exactamente lo que la casa no
hace.

**No lleva fecha, a propósito.** No hay fecha de tienda, así que nada dice «quedan X días».
Lo único con fecha es verdad pase lo que pase: octubre empieza el jueves 1.

### El pie

> ¿Qué pasa el día que abra NOMAD? Octubre empieza el jueves, así que te lo contamos ya.
>
> Que la lista de espera se cierra.
>
> NOMAD te escribe los días del viaje, con horas y precios, y te los cuenta al oído mientras
> andas: tours a pie narrados, guías de museo y los gastos del grupo, todo en el mismo viaje.
>
> Cuando abramos, cada viaje costará desde 2,99 €, sin suscripción: 2,99 € hasta 3 días,
> 4,99 € de 4 a 7 y 6,99 € de 8 a 30.
>
> Si estás en la lista, tu primer viaje es 1,99 €, dure lo que dure. Y ese precio se queda
> para quien esté dentro el día que abramos.
>
> Apúntate antes: el enlace, en la bio.
>
> #viajar #viajes #escapada #viajeros #audioguia #appdeviajes

La primera línea hace la pregunta y la respuesta queda debajo del «más»: el feed corta a
~125 caracteres, y la pregunta cabe entera.
