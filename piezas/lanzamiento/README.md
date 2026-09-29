# El lanzamiento

## «¿Qué pasa el día que abra NOMAD?» (29-sep) — `gen-abre.py`

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
