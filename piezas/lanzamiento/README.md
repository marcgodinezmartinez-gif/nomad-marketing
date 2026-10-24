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
