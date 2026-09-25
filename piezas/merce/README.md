# La Mercè (21-sep)

Dos carruseles de 1080×1350 con el molde de `piezas/tarjetas.py` y cinco historias de
1080×1920, para la fiesta del 23 al 27. **El que se publica es el del plan**; el otro queda
en reserva. El porqué, más abajo.

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
| `gen-plan-merce.py` | **«Le pedimos a NOMAD los cinco días de la Mercè»**: 8 tarjetas — la petición escrita, los cinco días hora a hora con precios, la pantalla de la app y el cierre. El protagonista es el plan y la app es quien lo escribió | **La que va**, montada — pero **en espera**: faltan dos días regenerados en la app (ver abajo) |
| `gen-merce.py` | El carrusel de la historia de la fiesta (1687, 1868, el programa). Bueno, pero la app aparece en la tarjeta 5 de 6 | Montado, en reserva |

**El plan es el real.** El generador se niega a escribir nada si `DIAS` se queda vacío: un
plan inventado sería justo la promesa que la app no cumple, que es lo único que la casa no
hace. Está leído de las cinco capturas que trajo el dueño el 21-sep, fila a fila, y **las
cinco sumas cuadran con el total que da la app**: 55, 55, 93, 75 y 15 € — 21 planes, 293 €
con todas las comidas dentro y 9 actos que no cuestan nada.

```bash
bash piezas/preparar.sh
cd salida && python3 ../piezas/merce/gen-plan-merce.py
node ../piezas/roma/exportar-plan.mjs planmerce 8
```

### Las cinco filas que NO salen como las escribió la app

El plan trae **cinco actos de la fiesta**, y la app puso mal la hora de los cinco y el sitio
de tres. No son erratas de redacción: Via Laietana dejó de ser el recorrido del correfoc en
2022 y Montjuïc dejó de ser el sitio del piromusical este año. Se publica el programa
oficial, y aquí queda escrito qué dijo la app. El generador lo imprime entero cada vez que
se ejecuta, para que no se olvide.

| Día | Lo que escribió la app | Lo que se publica | Fuente |
|---|---|---|---|
| Mié 23 | 16:00 · Pregón y *paseacalles* inaugural | **18:30** · Pregón en el **Saló de Cent** | betevé: «de 18.30 a 20 h», Saló de Cent |
| Jue 24 | 10:00 · Castellers en la plaça de Sant Jaume | **13:00** · Diada castellera | betevé: «13 h»; el Ajuntament corta los accesos de 11.30 a 14.30-15 h |
| Jue 24 | 16:00 · Cabalgata **por el passeig de Gràcia** | **18:00** · de **pl. Catalunya a Sant Jaume** | betevé: «18 h plaça Catalunya, 19 h pl. Sant Jaume». No pasa por el passeig de Gràcia |
| Sáb 26 | 18:00 · Correfoc **en Via Laietana** | **20:30** · Correfoc en el **passeig de Gràcia** | barcelona.cat/Cultura Popular: passeig de Gràcia desde 2022, Provença → Consell de Cent. Las 18 h son el *Correfoc dels Petits* |
| Dom 27 | 19:00 · Piromusical **en Montjuïc** | **22:00** · Piromusical en la **platja de la Nova Icària** | ajuntament.barcelona.cat y betevé: 22 h, desde el espigó del Bogatell; movido al litoral por las obras de la Fira |

Y la errata: la app escribe «pasea**c**alles» donde va «pasacalles». En la tarjeta va
corregido; **en la captura del día 23 se ve el error**, porque una captura no se retoca nunca.

### 25-sep: el corte del finde, porque el de cinco días llegó tarde

Nadie subió nada y la fiesta empezó. El 25 el dueño quiso volver a publicar, y un plan de
cinco días publicado el tercero es medio papel mojado: el 23 y el 24 ya han pasado. Así que
el mismo generador tiene dos cortes:

```bash
python3 ../piezas/merce/gen-plan-merce.py          # 8 tarjetas, los cinco días
python3 ../piezas/merce/gen-plan-merce.py finde    # 7 tarjetas, viernes a domingo
node ../piezas/roma/exportar-plan.mjs planmerce 7
```

El corte del finde cambia tres cosas: la portada es un reloj («Quedan tres días de Mercè»,
13 planes y 183 €), el viernes lleva «· hoy» en el kicker, y entra **la tarjeta 2, el aviso**
— los dos actos que han cambiado de sitio este año. Esa tarjeta es la que gana el deslizar y
la que se reenvía; y es, además, exactamente lo que la app puso mal.

**Y la decisión del 25, que corrige la del 21**: el sábado sigue con el correfoc a las 20:30
y la cena a las 21:00, y aun así se publica. Esperar a una captura regenerada costó cuatro
días de una fiesta que dura cinco. Lo que se publica es verdad y es útil; lo apretado del
sábado es del plan, no del dato.

### Los dos avisos del finde (`gen-avisos.py`)

Dos historias de 1080×1920, **el sábado por la mañana y el domingo**: el correfoc y el
piromusical, con la hora y el sitio grandes y lo práctico debajo. Existen porque las
historias diarias del sábado y el domingo **no se pueden subir** —enseñan la captura de la
app tal cual, con la hora y la calle malas— y porque esos dos actos son lo más buscado del
fin de semana. Una historia no se comparte por bonita: se comparte porque resuelve algo.

```bash
cd salida && python3 ../piezas/merce/gen-avisos.py
node ../piezas/roma/exportar-plan.mjs merceaviso 2 1080 1920
```

Con el adhesivo de enlace, de 1520 para abajo:
`https://travelsnomad.com/?utm_source=instagram&utm_medium=organic&utm_campaign=merce-aviso`

### 25-sep por la noche: el finde en historias (`gen-finde-historias.py`)

El dueño: *«el carrusel molaba para subirlo a historias, pero ajústalo a contar los planes de
sábado y domingo solo»*. Seis historias de 1080×1920, en este orden:

| # | Qué | Nota |
|---|---|---|
| 1 | «¿Qué planea NOMAD para la Mercè?» — 8 planes, 90 €, 4 gratis | El titular es del dueño: «Queda el finde de Mercè» no le gustó |
| 2 | El aviso: los dos cambios de sitio | Lo que se reenvía |
| 3 | Sábado 26 · 4 planes · 75 € | |
| 4 | Domingo 27 · 4 planes · 15 € | |
| 5 | Cómo se hizo, con el móvil | **Enseña el viernes a propósito**: las capturas del sábado y el domingo llevan la calle y la hora malas, y un móvil que dijera «Montjuïc» justo después del aviso sería un gol en propia |
| 6 | El cierre, señalando el adhesivo | |

Es el carrusel bajado 190 px a la zona segura, con los velos rehechos para 1920. El plan
sale de **`plan.py`**, que es de donde lo lee también el carrusel: las cinco filas
corregidas viven en un sitio y no en dos. (Movidas sin tocar un byte: los dos cortes del
carrusel dan exactamente el mismo HTML y la misma salida que antes.)

```bash
bash piezas/preparar.sh
cd salida && python3 ../piezas/merce/gen-finde-historias.py
node ../piezas/roma/exportar-plan.mjs mercefinde 6 1080 1920
```

Adhesivo de enlace en la primera y en la última (el hueco está reservado en las seis):
`https://travelsnomad.com/?utm_source=instagram&utm_medium=organic&utm_campaign=merce-finde`

**Y un arreglo que venía de antes**: `preparar.sh` sólo copiaba los recortes de post, así que
toda historia estiraba una foto de 1350 a 1920 — la trampa de las postales de AGENTS.md, en
pequeño. Ahora copia también `banco/fotos/historia/` a `salida/fotos-historia/`, y las tres
piezas de historias de la Mercè (esta, los avisos y las diarias) leen de ahí.

### Por qué el carrusel de cinco días no llegó a publicarse

Corregir las filas no arregla los días, porque **el plan estaba montado alrededor de las
horas malas**:

- **Jueves 24**: diada castellera a las 13:00 y almuerzo en Can Culleretes a las 13:30. La
  diada dura hasta las 14.30.
- **Sábado 26**: correfoc a las 20:30 y cena en Bar Cañete a las 21:00.

Los otros tres días (23, 25 y 27) quedan coherentes con la hora buena. Así que lo que falta
es pequeño y concreto: **volver a generar en la app el jueves y el sábado** con los datos
buenos y traer dos capturas nuevas (`planmerce-24-900.webp` y `planmerce-26-900.webp`). El
carrusel se vuelve a sacar en un minuto.

**Las historias diarias están bloqueadas por lo mismo, y es peor**: enseñan la captura de la
app tal cual, sin corregir nada, y se suben el día que toca a gente que está en la calle en
Barcelona. Una historia del sábado con el correfoc a las 18:00 en Via Laietana manda a
alguien a la calle equivocada dos horas antes.

Los cinco errores están en la **issue #6**, que es del producto y se lleva al repo de la app:
lo que falla no es el generador de planes, es de dónde salen la hora y el sitio de un acto
que cambia cada año.

### Qué foto lleva cada tarjeta

| Tarjeta | Foto | Por qué |
|---|---|---|
| 1 · la petición | `f-bcn-festa.jpg` | Un callejón del Gòtic con las guirnaldas de fiesta colgadas: es la única del banco que *es* una fiesta de calle |
| 2 · mié 23 | `f-bcn-paseo.jpg` | El arco y la gente andando, que es el Born del primer plan del día |
| 3 · jue 24 | `f-merce-castell.jpg` | Un castell entre balcones, el día de los castellers |
| 4 · vie 25 | `f-bcn-plaza.jpg` | El campanario de la Vila de Gràcia, de día y claro: el viernes trae cinco filas y necesita la foto más legible |
| 5 · sáb 26 | `f-merce-diable.jpg` | El diable en silueta, que es la noche del correfoc |
| 6 · dom 27 | `f-merce-espurnes.jpg` | Las fuentes de chispas, lo más cerca que hay de un piromusical |
| 7 · cómo se hizo | `f-bcn-calle.jpg` | Fondo tranquilo detrás del móvil |
| 8 · el cierre | `f-bcn-cierre.jpg` | El Park Güell de noche sobre la ciudad, el cierre de la casa |

El velo de las tarjetas de día (`VELO_PROGRAMA`) va abierto arriba y cerrado de la mitad
para abajo: la foto se ve donde no hay lista y la lista se lee donde la hay. Y las paradas
van en **columna flex anclada abajo**, no a posiciones fijas: así un día de cinco y uno de
cuatro acaban a la misma altura, y una parada que se parta en dos renglones no empuja a la
siguiente encima de la marca.

## Los hechos, verificados

| Dato | En la tarjeta | Fuentes |
|---|---|---|
| Plaga de langostas en 1687; el Consell de Cent hace el voto y la nombra patrona | 2 | Ajuntament de Barcelona, *Fiestas de la Mercè*: «en 1687 Barcelona sufrió una plaga de langostas y el Consell de Cent… votó pedir ayuda a la Virgen»; Wikipedia, *Fiestas de la Merced* |
| Pío IX lo hace oficial en 1868; desde entonces se celebra alrededor del 24 | 3 | ídem: «en 1868 el papa Pío IX autorizó instituir a la Virgen de la Mercè como patrona de Barcelona y su diócesis» |
| Del 23 al 27 de septiembre de 2026, diez distritos, más de 500 actividades | 1 y 4 | betevé, *Programa de la Mercè 2026*; idealista; ElNacional |
| El programa de la tarjeta 4 | 4 | betevé (medio público municipal), contrastado con la prensa |

**El recorrido del correfoc quedó resuelto el 21-sep** y ya no hace falta esquivarlo: las
guías de turistas lo siguen poniendo en Via Laietana, pero el Ajuntament (Cultura Popular) y
betevé dicen passeig de Gràcia desde 2022 — Provença → Consell de Cent, con la Porta de
l'Infern en Provença. Manda el Ajuntament. El piromusical, igual de claro: 22 h en el
litoral, este año por las obras de la Fira.

**Antes de publicar, un último vistazo al programa oficial**: un horario mal puesto en
Instagram no se corrige, se queda. Es la comprobación que pilló los dos errores de la app.

## Las fotos no son de la Mercè (las dos piezas)

Son de archivo: castells de Tarragona (Lluis AB) y correfocs de Les Borges Blanques (Ramon
Perucho), las dos de Pexels y sin atribución obligatoria. **Ninguna tarjeta dice «esto es la
plaça de Sant Jaume»**: el texto habla de la tradición y la foto la ilustra. Queda anotado
en `banco/fotos/creditos.json`, en el campo `sitio` de cada una.

Cuál va en cada tarjeta del carrusel del plan está más arriba; esta tabla es la del
carrusel de la historia (`gen-merce.py`):

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

`piezas/merce/gen-historias.py` escribe cinco, una por día. **Las cinco capturas ya están en
el banco** (`planmerce-23` a `planmerce-27`) y las cinco historias están montadas; el hueco
naranja de «falta la captura» sólo saldría si se borrara alguna. **Pero no se suben todavía**:
una historia enseña la captura tal cual y cuatro de los cinco días llevan una hora mala de la
fiesta. Se sustituye la captura del día que se regenere y se vuelven a sacar:

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

## El pie del corte del finde (el que se publica el 25)

> Quedan tres días de Mercè. Le pedimos a NOMAD el finde entero y esto es lo que salió.
>
> Viernes, sábado y domingo hora a hora, con precios: 13 planes y 183 € con todas las
> comidas y las cenas dentro. Cinco de ellos no cuestan nada.
>
> Y dos avisos, porque este año han cambiado de sitio los dos actos más grandes:
>
> · **Correfoc** — sábado 26, 20.30 h. Ya no pasa por Via Laietana: sale del passeig de
> Gràcia y baja de Provença a Consell de Cent. A las 18 h, el de los pequeños.
> · **Piromusical** — domingo 27, 22 h. Ya no es en Montjuïc: se dispara desde el espigón
> del Bogatell y se ve desde la platja de la Nova Icària.
>
> Vie 25 · 5 planes · 93 € — la Sagrada Família, la Ciutadella, La Puntual, el Picasso, los conciertos del Moll de la Fusta
> Sáb 26 · 4 planes · 75 € — el Park Güell, La Benaura, el correfoc, Bar Cañete
> Dom 27 · 4 planes · 15 € — puertas abiertas en el Palau de la Generalitat, la Boqueria, Can Paixano y el piromusical
>
> Los precios son estimados: la entrada de cada sitio y lo que se suele dejar en la mesa. El
> programa oficial entero, en barcelona.cat/lamerce.
>
> NOMAD sale en octubre. Le dices dónde vas y cuántos días y te monta el viaje así, con
> horas y precios, para cualquier sitio: no para seis ciudades. Desde 2,99 € el viaje
> entero, sin suscripción, según lo que dure; y el primero, para quien esté en la lista de
> espera, 1,99 € dure lo que dure. Enlace en la bio.
>
> #lamerce #lamerce2026 #barcelona #correfoc #piromusical #festamajor #bcn #viajar

## El pie del carrusel de cinco días (el que ya no llegó a tiempo)

> Le pedimos a NOMAD los cinco días de la Mercè. Esto es lo que salió.
>
> Una frase — «Barcelona, del 23 al 27 de septiembre» — y la app devolvió el viaje entero:
> 21 planes con su hora, su categoría y su precio. 293 € los cinco días, con todas las
> comidas y las cenas dentro. Nueve de los 21 no cuestan nada.
>
> Mié 23 · 4 planes · 55 € — el Gòtic y el Born, El Xampanyet, el pregón, Bar del Pla
> Jue 24 · 4 planes · 55 € — els castells en Sant Jaume, Can Culleretes, la cabalgata, el BAM en la plaça Reial
> Vie 25 · 5 planes · 93 € — la Sagrada Família, la Ciutadella, La Puntual, el Picasso, los conciertos del Moll de la Fusta
> Sáb 26 · 4 planes · 75 € — el Park Güell, La Benaura, el correfoc del passeig de Gràcia (20.30 h), Bar Cañete
> Dom 27 · 4 planes · 15 € — puertas abiertas en el Palau de la Generalitat, la Boqueria, Can Paixano y el piromusical en la platja de la Nova Icària (22 h)
>
> Los precios son estimados: la entrada de cada sitio y lo que se suele dejar en la mesa. El
> programa oficial entero, en barcelona.cat/lamerce — el cartel de este año es de la
> muralista Cinta Vidal.
>
> NOMAD sale en octubre. Le dices dónde vas y cuántos días y te monta el viaje así, con
> horas y precios, para cualquier sitio: no para seis ciudades. Desde 2,99 € el viaje
> entero, sin suscripción, según lo que dure; y el primero, para quien esté en la lista de
> espera, 1,99 € dure lo que dure. Enlace en la bio.
>
> #lamerce #lamerce2026 #barcelona #festamajor #correfoc #piromusical #castellers #viajar #bcn

**Por qué el pie repite el plan** aunque esté en las tarjetas: Instagram no indexa lo que hay
dentro de una imagen, y los nombres de los sitios son lo único de esta pieza que alguien
puede estar buscando esta semana.

## El pie del carrusel de la historia (en reserva)

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
> Sáb 26 · El correfoc — passeig de Gràcia, 20.30 h
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
