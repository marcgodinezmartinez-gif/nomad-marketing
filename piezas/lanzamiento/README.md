# El lanzamiento

## «Ya en iPhone y Android» (20-nov) — `gen-dos-tiendas.py`, BORRADOR

Android está en Google Play desde el 19-nov (#21). El dueño enseñó como referencia un anuncio en
historias de otra app: color plano, el icono en grande, «ya en iOS y Android», las dos insignias y
«descárgala». Tres historias de 1080×1920 para elegir:

| # | Qué es | Para quién |
|---|---|---|
| `dos-1` | El anuncio a secas, en los colores del icono | Quien ya conoce Nomad: seguidores, quien preguntó por Android, quien vio los vídeos |
| `dos-2` | Lo mismo con el plan de un día en el móvil | Quien no la conoce: dice qué hace antes de decir dónde está |
| `dos-3` | El anuncio con misterio, «Tu próximo viaje ya está escrito.»: sin decir qué hace ni cuánto cuesta | La apuesta del dueño para quien no la conoce («el tema enigmático a la gente le suele gustar»). Se prueba contra `dos-2` |

```bash
bash piezas/preparar.sh
cd salida && python3 ../piezas/lanzamiento/gen-dos-tiendas.py
node ../piezas/roma/exportar-plan.mjs dos 3 1080 1920
```

**No está publicado ni decidido.** Falta que el dueño elija variante y diga si va sólo como historia
con adhesivo de enlace o también como anuncio.

### La prueba de pago: misterio contra la app delante (20-nov)

El dueño quiere saber si el anuncio con misterio trae gente que no conoce Nomad. Se prueba
`dos-3` contra `dos-2`, con el mismo público y el mismo dinero, y gana el que traiga más descargas,
no más toques.

| nivel | qué |
|---|---|
| campaña | «Las dos tiendas · misterio vs la app delante» (`120249214297860710`): tráfico, sin presupuesto de campaña, tope de gasto de 100 € (el mínimo que deja Meta) |
| conjuntos | uno por anuncio, iguales: España, 18+, Instagram (historias y reels), público automático, iPhone y Android, 7 € al día; activos del 20-nov 11:31 al 25-nov 00:00 (antes, del 21 al 25-nov). 70 € en total, lo que dijo el dueño (12-15 € al día, 5 días) |
| anuncios | **publicados el 20-nov hacia las 11:20 (hora de Madrid), con el sí del dueño, y activos desde las 11:31 de ese día**: «Misterio · historia» (`120249214804450710`, creativo `1457924286492362`, imagen `dos-3`) en el conjunto `120249214300100710`, y «La app delante · historia» (`120249214804900710`, creativo `1409108671245773`, imagen `dos-2`) en el `120249214300140710`. Uno por conjunto, sin errores de validación, las mejoras automáticas de Meta apagadas y la etiqueta de IA en «no» (decisión del dueño) |
| enlaces | `travelsnomad.com/app?utm_source=meta&utm_medium=paid&utm_campaign=meta-misterio` y `…=meta-app`, con el botón Descargar |

**Publicada el 20-nov y activa desde ese día a las 11:31 (hora de Madrid).** Se publicó para
empezar el 21 a las 00:00, y el dueño la quiso «activa ya». Se adelantó el inicio en los dos
conjuntos, y el final pasó del 26 al **25-nov a las 00:00**: así son cinco días de presupuesto (el 20
a medias, y del 21 al 24) y el total sigue sin pasar de 70 €. Los dos conjuntos siguen iguales. Leído
después en Meta: la campaña, los dos conjuntos y los dos anuncios en activo (la revisión ya pasó), con
7 € al día y sin errores que bloqueen la entrega.

**Lo que bloqueó el 20-nov, y cómo se resolvió:** subir las imágenes desde la sesión lo denegó el
sistema de permisos, dos veces y en dos sesiones. La segunda se reintentó una vez, con el sí del dueño,
y entró: `dos-3.png` es la imagen `8d13cf45da9e866378388cad9b976659` de la biblioteca y `dos-2.png`, la
`4eb335565b00ea964121d3795e5355c8`. Se generaron otra vez con las órdenes de arriba y salieron con las
huellas que aprobó el dueño (sha256 `6958f04193882096…` y `79b1c3cf1b20e2cb…`).

**Lo que cambió después de publicarla** (historial de la cuenta, hora de Madrid):

- 20-nov 14:14: los dos conjuntos pasan de 7 a **15 € al día**, desde la app Ads Manager del móvil.
  Son 30 € al día, no los 12-15 € del plan, y el total ya no son 70 €. El tope de 100 € de la
  campaña sigue puesto.
- 21-nov 10:27: se pausa la campaña. A las 12:52 se reactiva y **se pausa el conjunto de misterio**.
  Desde entonces sólo corre «La app delante», a 15 € al día, hasta el 25-nov a las 00:00.

**Lo medido el 21-nov a las 18 h, con día y medio de campaña** (Meta y producción, de sólo lectura):

| | misterio | la app delante |
|---|---|---|
| gasto | 12,33 € | 16,53 € |
| impresiones | 1.676 | 2.819 |
| toques en el enlace | 146 | 185 |
| toques por cada 100 impresiones | 8,7 | 6,6 |
| coste por toque | 0,08 € | 0,09 € |
| llegadas a la página | 104 | 129 |

- Misterio tuvo más toques por impresión, y el mismo coste por toque y las mismas llegadas por
  euro. No es una prueba controlada: cada anuncio va en su conjunto y misterio sirvió menos horas.
  **Qué anuncio trae más descargas no se sabe desde aquí**: lo dicen las campañas `meta-misterio`
  y `meta-app` en App Store Connect y en la consola de Google Play.
- **El 93 % del dinero se fue a móviles Android** (26,86 € de 28,86 €). A iPhone, 2 €.
- El 70 % del gasto fue a hombres, repartido por edades. Por comunidad, los toques siguen a la
  población: Cataluña 83, Andalucía 52, C. Valenciana 40, Madrid 38.
- Cuentas reales nuevas desde que empezó: 6 (2 de iPhone, 2 de Android y 2 sin saber), y 1 creada
  y borrada. Android había salido a la tienda 14 horas antes, así que no se puede separar lo que
  trajo el anuncio de lo que trajo la salida. Es pronto para un coste por cuenta.
- De las 233 llegadas a la página, como mucho 3 de cada 100 acabaron con cuenta. Dónde se pierde el
  resto (la ficha de la tienda, la instalación o el registro) sólo lo enseñan las tiendas. La ficha
  de Google Play seguía diciendo «10+ descargas» ese día.

**Cómo se lee al acabar:** toques por anuncio, en Meta. Descargas por anuncio, en App Store Connect
(campañas `meta-misterio` y `meta-app`) y en la consola de Google Play. Cuentas nuevas por día, en
producción. Con estas cifras puede salir un empate.

**Las insignias de la imagen no se tocan**: en una historia sólo se toca el adhesivo de enlace, y en
un anuncio, su botón. El enlace que vale para los dos móviles es `travelsnomad.com/app`.

**Lo que se midió ese día, antes de hacerla** (cuenta de Meta, producción y las dos fichas):

- En Meta, desde agosto: 184 € y 3.183 clics en el enlace, a 0,06 € el clic. El anuncio a la App
  Store («Así funciona») lleva 96,22 €: los 37 € del 31-oct al 2-nov que apunta
  `campana/CAMPANA-ASI-FUNCIONA.md` y otros 59 € del 8 al 11-nov, que no estaban apuntados.
- Desde que la app está en la tienda (19-oct): 78 cuentas nuevas y 2 ventas reales, las dos en
  iPhone, que dejan 7,01 € netos. En los cuatro días del 8 al 11-nov entraron 14 cuentas.
  **Corregido el 21-nov: esas cifras contaban a los probadores de Android.** De las 14 cuentas
  del 8 al 11-nov, 12 eran de prueba o internas y 2 reales (1 de iPhone). Reales desde el 19-oct:
  31 (23 de iPhone). Las cifras buenas están en `AGENTS.md`, «Medir antes de opinar».
- Las fichas: 1 valoración en la App Store y «10+ descargas» en Google Play.

O sea: el clic sale barato y el anuncio no es el problema. Lo que falla está después del clic.
Pagar por descargas hoy compra aprendizaje, no ventas. (El «9 céntimos por cuenta» que había aquí
salía de las 78 cuentas con probadores dentro, y no vale.)

**Lo que se contrastó con fuentes de fuera ese día** (cinco lectores y dos escépticos):

- Apple Ads (antes Apple Search Ads) tiene una modalidad que cobra por instalación, Basic, sin nada
  dentro de la app, y España está en su lista de países. El mínimo y el crédito de bienvenida no
  constan: se ven al crear la cuenta.
- Google Ads cuenta las instalaciones de Google Play sin SDK, pero recomienda un presupuesto diario
  de 50 veces lo que se quiere pagar por instalación. Con decenas de euros no aprende.
- En Meta, optimizar a instalaciones pide su SDK o un socio de medición dentro de la app. Sin él,
  una campaña sólo puede buscar clics.
- La consola de Google Play enseña visitas e instalaciones por `utm_source` y `utm_campaign` sin
  SDK, y agrupa en «Otros» lo que tiene poco volumen. El enlace de la web a Play aún no los lleva
  (NOMAD#473).
- Un enlace de campaña de Apple sólo aparece en App Store Connect con 5 personas distintas y pasadas
  24 horas. A este volumen, un enlace por canal, no uno por pieza.
- No hay ningún estudio serio que compare «enseñar el producto» con «anuncio de marca» para público
  frío, ni el efecto de tener pocas valoraciones. Las dos cosas son hipótesis razonables.

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
