# La Mercè — el carrusel (21-sep)

Seis tarjetas de 1080×1350 con el molde de `piezas/tarjetas.py`, para publicar el 21 o el
22, antes de que arranque la fiesta el miércoles 23.

## El cartel oficial no va dentro, y por qué

El dueño lo pidió: *«algo hablando de la Mercè que además incluya el cartel de fiestas»*.
**No se puede reproducir.** El cartel de 2026 es obra de la muralista **Cinta Vidal**
(«Barcelona desplegada»), con sus derechos de autor; la regla de la casa sólo admite
material que no deba atribución, y una obra con derechos reservados no entra ni con
crédito. Además, en una cuenta comercial el cartel oficial insinuaría un vínculo con el
Ajuntament que no existe.

**Lo que sí se puede**: citarlo en el pie —«el cartel de este año es de la muralista Cinta
Vidal»—, que es información, no reproducción. Y la portada la hacemos nosotros, que además
es lo que distingue el feed.

## Dos piezas, y cuál va primero

El 21-sep el dueño paró el enfoque: *«no me acaba de gustar como lo he enfocado, es como que
no hablo de la app»*. Tenía razón, y `campana/MERCADO` se la da: lo que nos diferencia no es
contar bien un sitio famoso —eso ya lo hace la competencia curada en seis ciudades— sino **la
generación**: cualquier sitio, cualquier tema, y el plan entero con precios. Así que hay dos
piezas y el orden importa:

| Pieza | Qué es | Estado |
|---|---|---|
| `gen-plan-merce.py` | **«Le pedimos a NOMAD un jueves de Mercè»**: el plan real del día 24, hora a hora y con precios, como el carrusel de Roma. El protagonista es el plan y la app es quien lo escribió | **La que va primero.** Falta el plan real de la app |
| `gen-merce.py` | El carrusel de la historia de la fiesta (1687, 1868, el programa). Bueno, pero la app aparece en la tarjeta 5 de 6 | Montado, en reserva |

**El plan tiene que ser el real.** El generador se niega a escribir nada si `JUEVES` está
vacío: un plan inventado sería justo la promesa que la app no cumple, que es lo único que la
casa no hace. Se lee de la captura, como se leyó el jueves de Roma.

### Qué hay que pedirle a la app

1. Nuevo viaje, **Barcelona**, el **jueves 24** (o los días de la Mercè, y se abre ese día).
2. Que el plan incluya lo de la fiesta: si no sale, al asistente — *«añade los castells de
   la plaça de Sant Jaume y la cercavila de gegants»*.
3. **Dos cosas para mí**: la captura de la pantalla del plan del jueves, vertical y con la
   barra de estado, guardada como `banco/capturas/planmerce-24-900.webp`; y que se lea bien
   cada parada con su hora, su categoría y su precio, para poder escribirlas en la tarjeta 2.

Con eso, el carrusel sale montado en diez minutos.

## Los hechos, verificados

| Dato | En la tarjeta | Fuentes |
|---|---|---|
| Plaga de langostas en 1687; el Consell de Cent hace el voto y la nombra patrona | 2 | Ajuntament de Barcelona, *Fiestas de la Mercè*: «en 1687 Barcelona sufrió una plaga de langostas y el Consell de Cent… votó pedir ayuda a la Virgen»; Wikipedia, *Fiestas de la Merced* |
| Pío IX lo hace oficial en 1868; desde entonces se celebra alrededor del 24 | 3 | ídem: «en 1868 el papa Pío IX autorizó instituir a la Virgen de la Mercè como patrona de Barcelona y su diócesis» |
| Del 23 al 27 de septiembre de 2026, diez distritos, más de 500 actividades | 1 y 4 | betevé, *Programa de la Mercè 2026*; idealista; ElNacional |
| El programa de la tarjeta 4 | 4 | betevé (medio público municipal), contrastado con la prensa |

**Donde las fuentes discrepaban, no se pone**: el recorrido del correfoc aparece como Via
Laietana en unas y passeig de Gràcia en otras, así que la tarjeta da día y hora y no el
sitio. El piromusical cambió de playa este año (Nova Icària, por las obras de la Fira) y eso
sí coincide en dos.

**Antes de publicar conviene un último vistazo al PDF oficial**: un horario mal puesto en
Instagram no se corrige, se queda.

## Las fotos no son de la Mercè

Son de archivo: castells de Tarragona (Lluis AB) y correfocs de Les Borges Blanques (Ramon
Perucho), las dos de Pexels y sin atribución obligatoria. **Ninguna tarjeta dice «esto es la
plaça de Sant Jaume»**: el texto habla de la tradición y la foto la ilustra. Queda anotado
en `banco/fotos/creditos.json`, en el campo `sitio` de cada una.

| Fichero | Tarjeta | Qué es |
|---|---|---|
| `f-merce-castell.jpg` | 1 | Un castell altísimo entre balcones llenos |
| `f-merce-diable.jpg` | 2 | Un diable de correfoc en silueta, entre chispas |
| `f-merce-castell2.jpg` | 3 | Un castell con la multitud abajo |
| `f-bcn-noche.jpg` | 4 | Un callejón de noche: fondo tranquilo para las seis filas |
| `f-bcn-paseo.jpg` | 5 | Gente andando, detrás del móvil |
| `f-merce-espurnes.jpg` | 6 | Las fuentes de chispas de un correfoc |

## Qué falta

`banco/capturas/tourgotic-900.webp`: el tour a pie de la app por Ciutat Vella o el Gòtic,
con el título de la parada y la audioguía a la vista, como las tres de la serie «¿Conocías
este lugar?».

## Las historias diarias, del 23 al 27

Idea del dueño: *«cuando empiecen los días de fiesta, poner historias con el planning que dé
la app para cada día»*. Es la mejor forma de enseñar la app sin que parezca un anuncio: el
plan de HOY, en la ciudad donde hoy hay medio millón de personas. Y las historias son el
único sitio donde el enlace se toca, que es de donde salieron el 88 % de las vistas del reel.

El molde ya está: `piezas/merce/gen-historias.py` escribe cinco, una por día, cada una con
el hueco del móvil. **Cada mañana de fiesta**:

1. En la app, el plan de ese día en Barcelona. Captura vertical, con la barra de estado.
2. Guardarla como `banco/capturas/planmerce-<día>-900.webp` — `planmerce-24-900.webp`, etc.
3. ```bash
   bash piezas/preparar.sh
   cd salida && python3 ../piezas/merce/gen-historias.py
   node ../piezas/roma/exportar-plan.mjs mercehist 5 1080 1920
   ```
   `mercehist-1` … `mercehist-5` son los días 23, 24, 25, 26 y 27, en ese orden.
4. Subirla **con el adhesivo de enlace**, que es lo que hace que esto sirva de algo:
   `https://travelsnomad.com/?utm_source=instagram&utm_medium=organic&utm_campaign=merce-dia`

Las zonas seguras están respetadas: el texto vive entre y=290 e y=1493 y de y=1520 abajo
queda libre para el adhesivo. Ese hueco no es un descuido de diseño, es su sitio.

## El pie

> La Mercè es la fiesta mayor de Barcelona. Y su patrona lo es por una plaga de langostas.
>
> En 1687 la ciudad se encomendó a la Mare de Déu de la Mercè y el Consell de Cent hizo un
> voto: si la plaga se iba, la nombraría patrona. Se fue, y cumplieron. La Iglesia tardó casi
> dos siglos en hacerlo oficial: el papa Pío IX lo confirmó en 1868, y desde entonces
> Barcelona celebra su fiesta mayor alrededor del 24 de septiembre.
>
> Este año va del 23 al 27, con más de quinientas actividades repartidas por los diez
> distritos y casi todas gratuitas. Lo grande:
>
> Mié 23 · El pregón — Saló de Cent, 18.30 h
> Jue 24 · Els castells — plaça de Sant Jaume, 13 h
> Jue 24 · La cercavila de gegants — pl. Catalunya 18 h, St. Jaume 19 h
> Sáb 26 · El correfoc — 20.30 h
> Dom 27 · Diada castellera — plaça de Sant Jaume, 12 h
> Dom 27 · El piromusical — platja de la Nova Icària, 22 h
>
> El programa entero, en barcelona.cat/lamerce. El cartel de este año es de la muralista
> Cinta Vidal.
>
> Y el resto del año, NOMAD te cuenta Barcelona mientras la andas: cada parada del tour, con
> su historia, al oído. Sale en octubre; el primer viaje, por 1,99 € para quien esté en la
> lista de espera. Enlace en la bio.
>
> #lamerce #lamerce2026 #barcelona #festamajor #castellers #correfoc #viajar #bcn

## El enlace de la historia que lo señala

```
https://travelsnomad.com/?utm_source=instagram&utm_medium=organic&utm_campaign=merce
```
