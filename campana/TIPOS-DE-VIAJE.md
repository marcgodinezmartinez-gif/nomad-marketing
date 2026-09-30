# Una campaña por tipo de viaje

Escrito el 30 de septiembre de 2026, a petición del dueño: *«todas giran alrededor de los
pueblos, pero en la app se pueden hacer viajes a ciudades, esquí, playa, road trips y
naturaleza. Lo mismo que has hecho para los pueblos, hazlo para los diferentes tipos de
viajes, y así podremos pensar qué campañas seleccionamos».*

**Esto es un menú para elegir, no un plan.** Seis campañas —la del pueblo, que ya está en
`VISION.md`, y cinco nuevas—, cada una con lo que la app hace de verdad con ese viaje, la
idea, los formatos, cuándo, con quién y lo que cuesta. Al final, la tabla para compararlas
(§7) y una propuesta de cuáles y en qué orden (§8). Lo que se decida va a la issue #9.

**Lo que este documento NO hace**: no cambia `VISION.md` hasta que se elija, no fabrica
piezas, no escribe a nadie y no sube el techo de 4.400 €.

---

## 0. Lo que la app hace con cada tipo de viaje, leído en el código

Cada campaña enseña algo que la app hace de verdad, y eso cambia con el tipo de viaje: el
generador de itinerarios lleva una regla distinta para cada uno (`TRIP_TYPE_RULES`, en
`supabase/functions/_shared/itineraryPrompt.ts` del repo de la app). Lo que dice cada regla,
y los destinos que el buscador de la app propone para cada tipo:

| Tipo | Lo que cambia en el plan | Destinos del buscador |
|---|---|---|
| **Ciudad** | Barrios, museos, monumentos, comida y noche; un barrio a pie cada vez. Y la audioguía de calle y de museo, con **dónde ponerte y en qué fijarte** en cada parada | 14, de Lisboa a Kioto |
| **Playa** | *«El mar es el plan»*: bloques largos junto al agua, las horas de calor a la sombra y **el atardecer como un acontecimiento**. Dos o tres cosas al día *«no es un fallo»* | Menorca, Costa Brava, Cádiz, Algarve, Cerdeña, Sicilia, Malta, Dubrovnik, y **Tenerife y Fuerteventura todo el año** |
| **Naturaleza** | Rutas, miradores, agua y luz; una o dos salidas al día. **Cuánto se tarda y lo dura que es, dicho con honestidad**; permisos y reservas en las notas; se come donde está el día, sea el bar del pueblo o un bocadillo en la ruta | Picos de Europa, Ordesa, Dolomitas, Azores, Islandia, Selva Negra |
| **Esquí** | Mañana en pistas, comida en la montaña y tarde en pistas; horario de remontes en las notas; alquiler del material el primer día, après-ski y un día de descanso o spa. **Y un plan B si no hay nieve o cierran los remontes** | Baqueira, Sierra Nevada, Grandvalira (Soldeu), Chamonix |
| **Road trip** | Conducir es parte del viaje: la etapa es la columna del día, **se come en ruta y no al llegar**, con paradas a 40 minutos de la autopista. **Nunca más de unas cinco horas de coche al día**, con distancias que calcula la app y no inventa el modelo | Andalucía, La Rioja, costa vasca, Toscana, Provenza, Highlands, California |

Y en todos: el tiempo real de esas fechas, la cartelera, los gastos del grupo, y hueco
reservado para el deporte de cada uno. Son unos cincuenta, del pádel por horas al surf con
escuela.

---

## 1. Ciudad: «Fíjate en…»

**Lo que enseña**: la voz, parada a parada, con sus dos líneas propias: **«Colócate aquí»**
y **«Fíjate en»**. La voz las lee en voz alta, con esas palabras (`tourScript.ts` y
`SmartGuide.tsx` del repo de la app). En el castillo de Porrentruy, lo que sigue a «Fíjate
en» es *«La Tour Réfous, una imponente torre circular de homenaje medieval del siglo
XIII»*. **La campaña se llama como lo que dice la app.**

**La verdad en la que se apoya**: en una ciudad miras el móvil para decidir adónde ir y te
pierdes lo que tienes delante. Pasas cien veces por delante de algo sin saber qué es.

**La idea: «Fíjate en…»**. Cada vídeo, un detalle que la app te hace mirar: 15-20 s, la
voz de la app y el sitio. *«Llevas años pasando por aquí. Fíjate en…»*. Es la evolución de
«¿Conocías este lugar?», el mejor formato publicado, en un formato más corto que se hace
en una tarde.

**Formatos**:

1. **«Fíjate en…»**, una ciudad cada semana, tres o cuatro detalles.
2. **«Turista en tu ciudad»**: un creador local descubre su propia ciudad con la app.
   *«Llevo treinta años en Madrid y una app me ha contado cinco cosas que no sabía.»* Tiene
   que ser verdad, y el creador lo dice con su voz.
3. **«¿Qué planea NOMAD para el puente en…?»**, que ya existe, y en diciembre [[MERCADILLOS]].

**La capa de Vicio**: rivalidad entre ciudades, con cariño: *«Madrid contado para los de
Barcelona»*. Nunca contra los guías: la app no los sustituye y no se dice que lo haga.

**La capa de Estrella Damm**: la firma de la casa, *«La ciudad, contada»*, en piezas al
amanecer con la ciudad vacía y la voz encima.

**Cuándo**: siempre; más en los puentes, en diciembre y por San Valentín (domingo 14 de
febrero), para parejas.

**Quién**: @imartatravels (Barcelona) y @derutapormadrid (Madrid) de `CREADORES.md`,
@hoyviajamos (escapadas por Europa) de `INFLUENCERS.md`, y [[CREADORES-CIUDAD]].

**Coste**: casi cero si se graba en la ciudad de cada uno.

**Lo que hay que comprobar**: lo de siempre, cada dato contra dos fuentes. En un museo,
sólo donde se puede grabar.

---

## 2. Playa: «Planear para no hacer nada»

**Lo que enseña**: el día según el sol, y un plan que presume de tener poco. La regla de la
app dice literalmente que *«dos o tres actividades en un día completo es lo correcto aquí,
no un fallo en llenarlo»*, y trata el atardecer como un acontecimiento.

**La verdad en la que se apoya**: nadie quiere planificar la playa… y al tercer día estás
en la misma toalla, en el mismo chiringuito, preguntando «¿y hoy qué hacemos?».

**La idea: «Planear para no hacer nada»**. La única app de viajes que te apunta la siesta.
*«Le pedí a una app que me organizara la playa y me ha dejado la tarde sin nada.»* El chiste
es el propio plan, así que se enseña el plan de verdad: la cala de al lado, el barco, la
tarde libre y el atardecer.

**La capa de Vicio**: *«Siesta: de 15:00 a 17:00. No negociable.»* Sólo si el plan la pone;
si no, se usa lo que ponga.

**La capa de Estrella Damm**: el atardecer como ritual. **Pero el verano mediterráneo es
suyo**: competir en junio con *Mediterráneamente* es perder. Por eso la playa entra por
el invierno.

**Ahora: «Verano en enero»**. Tenerife y Fuerteventura salen en el buscador de la app como
destinos de todo el año. El puente de diciembre, las Navidades y la cuesta de enero en manga
corta. [[CANARIAS]]

**Después: «Planear para no hacer nada»**, de junio a septiembre de 2027, con la decisión
tomada en abril.

**Quién**: [[CREADORES-PLAYA]]

**Coste**: un viaje a Canarias si lo graba el dueño, o una pieza de un creador que ya vive
allí, que es lo barato.

**Lo que hay que comprobar**: **nada de «calas secretas»**. [[MASIFICACION]] Una cala
masificada por un vídeo es la peor prensa posible para una app de viajes.

---

## 3. Naturaleza: «Tres semanas de cobre» y «Sin postureo»

**Lo que enseña**: la honestidad de la ruta —cuánto dura y lo dura que es—, los permisos
en las notas, empezar temprano, y comer donde está el día.

**Dos ideas, una para cada estación:**

**«Tres semanas de cobre»** (octubre-noviembre, o sea **ahora**). El hayedo sólo está de
cobre unas semanas al año, y saber qué fin de semana ir lo es todo. La app mira el tiempo
de esos días y escribe la ruta, dónde dormir y dónde comer en el pueblo de al lado. Es un
ritual con fecha, lo de Estrella Damm, y encaja con la escapada del dueño: los hayedos
famosos están junto a pueblos muy pequeños. [[HAYEDOS]]

**«Sin postureo»** (primavera y verano). La foto famosa contra lo que dice la app: *«4 h
30, sin sombra, reserva obligatoria»*. Y luego la ruta de verdad. La capa de Vicio sale
sola: *«La app que te dice que esa ruta no es para ti.»*

**La competencia, dicha para no pelear con quien no toca**: [[WIKILOC]] NOMAD no es una app
de tracks: es el viaje alrededor de la ruta. Dónde dormir, dónde comer, qué día ir y qué
llevar.

**Quién**: @mochileandosobreruedas (naturaleza y pueblos) de `CREADORES.md`, @viajesyrutas
de `INFLUENCERS.md`, y [[CREADORES-NATURALEZA]].

**Coste**: el de la escapada, unos 75 €, con la del pueblo en el mismo viaje.

**Lo que hay que comprobar**: [[DRONES]] Tampoco se manda a nadie a una ruta peligrosa, y
no se empuja a un sitio que ya está masificado.

---

## 4. Esquí: «Nieve a medias» y «Plan B»

**Lo que enseña**: el día de esquí bien montado, el plan B si no hay nieve, y **los gastos
del grupo**, que en esquí es donde más duelen: apartamento, forfaits, alquiler, gasolina,
súper y cenas.

**La verdad en la que se apoya**: el viaje de esquí es el más caro y el más compartido del
año. Ocho personas, un apartamento y cuarenta y siete bizums.

**La idea: «Nieve a medias»**. El viaje de esquí con las cuentas claras. Y como la
temporada de esquí coincide con «Organizadores Anónimos» (enero-marzo), la mejor forma es
**meter el esquí dentro**: *«Organizadores Anónimos, edición nieve»*. Quien organiza el
apartamento para ocho es el organizador anónimo por excelencia. Y en «La Amnistía», la
deuda del forfait del jueves.

**La segunda idea: «Plan B»**. *«¿Y si no nieva?»*. La app escribe siempre qué hacer si
cierran los remontes: un paseo por el valle, el pueblo, unas termas. Es útil, es verdad y
en España cada vez pasa más.

**La capa de Estrella Damm**: la primera bajada del año con los de siempre. [[ESQUI]]

**Cuándo**: desde el puente de diciembre, si hay nieve, hasta Semana Santa, con Carnaval en
medio.

**Quién**: [[CREADORES-ESQUI]]

**Coste**: alto si lo graba el dueño (un fin de semana de esquí no baja de varios cientos
de euros), así que aquí manda un creador que ya va a esquiar.

**Lo que hay que comprobar**: la nieve y las fechas de apertura no se prometen nunca, y los
precios de forfait se miran el día que se publican.

---

## 5. Road trip: «Prohibido comer en la gasolinera»

**Lo que enseña**: las paradas en ruta, la comida en un sitio de verdad a mitad de etapa,
el límite de cinco horas de coche al día y los gastos del grupo, gasolina y peajes
incluidos.

**La verdad en la que se apoya**: lo mejor de un road trip está entre medias, y casi
siempre te lo saltas por no saber que estaba ahí. Y el bocadillo de gasolinera es el
símbolo del road trip mal hecho.

**La idea: «Prohibido comer en la gasolinera»**. Cada episodio, una etapa: el mirador o el
pueblo a cuarenta minutos de la autopista, y la comida en un restaurante de verdad a mitad
de camino. Es **la escapada del dueño con ruedas**, con la misma comprobación: la app tiene
que nombrar un restaurante que exista y que abra.

**La segunda idea: «Tu copiloto»**. El asistente de la app se llama literalmente
«copiloto». Sketches del amigo que se duerme de copiloto, el que no sabe leer un mapa y el
que pone la misma canción: *«Por fin un copiloto que sabe dónde parar.»* Encaja con los
humoristas de «Organizadores Anónimos».

**La capa de Estrella Damm**: las ventanillas bajadas y una carretera con nombre. [[RUTAS]]

**Cuándo**: los puentes, Semana Santa (del 25 al 29 de marzo de 2027) y el verano.

**Quién**: @mochileandosobreruedas y @conunpardemaletas (camper), @viajesyrutas y
@unaideaunviaje (rutas en coche), y [[CREADORES-ROADTRIP]].

**Coste**: gasolina y comida, como la escapada.

**Lo que hay que comprobar**: [[DGT]] Nunca se graba al conductor con el móvil, ni desde el
asiento del conductor.

---

## 6. Y un nicho, por si sirve: «La rutina también viaja»

La app reserva hueco para el deporte de cada uno, de una pista de pádel por horas a una
ruta para correr, y lo pone donde se hace de verdad. *«Le pedí a una app una pista de pádel
en Roma. Me la ha encontrado.»* [[PADEL]] Es pequeño, pero el pádel en España tiene
público propio y nadie le habla de viajes.

---

## 7. Para comparar

| Campaña | Qué enseña de la app | Cuándo | Cómo se comparte | Coste | El riesgo |
|---|---|---|---|---|---|
| **Pueblo**: «Tu pueblo, contado» (`VISION.md`) | La voz en cualquier sitio | Octubre-enero | Al grupo de la familia; orgullo y rivalidad de pueblo | Bajo | Que la app se equivoque con un pueblo pequeño |
| **Ciudad**: «Fíjate en…» | La voz y su «Fíjate en» | Todo el año | Se guarda y se manda a quien va a ir | Casi cero | Es lo más visto: se gana con el detalle, no con el sitio |
| **Playa**: «Verano en enero», y luego «Planear para no hacer nada» | El día según el sol, y un plan que presume de tener poco | Canarias, diciembre-febrero; el resto, verano | Humor: «esto es lo que necesito» | Bajo, con un creador que ya vive allí | La masificación, y que el verano es de Estrella Damm |
| **Naturaleza**: «Tres semanas de cobre», y luego «Sin postureo» | La honestidad de la ruta, y qué día ir | Otoño (ahora) y primavera | Se guarda para el fin de semana | Bajo, en el mismo viaje que la escapada | La seguridad, la masificación y los drones |
| **Esquí**: «Nieve a medias» y «Plan B» | Los gastos del grupo, y el plan B | Diciembre-marzo | Al grupo del viaje | Medio o alto: el esquí es caro | La nieve, que no se promete |
| **Road trip**: «Prohibido comer en la gasolinera» | Las paradas y la comida en ruta; cinco horas de coche como mucho | Puentes, Semana Santa y verano | Se guarda la ruta | Gasolina y comida | Grabar al volante: nunca |

**Lo que se junta solo**: el pueblo, la escapada del dueño, el road trip y la naturaleza
son la misma historia —un sitio pequeño, un restaurante de verdad y la voz de la app— vista
desde cuatro sitios. El esquí es la misma que «Organizadores Anónimos» y «La Amnistía»: un
grupo, un viaje caro y las cuentas.

---

## 8. Una propuesta de cuáles, y en qué orden

**El calendario elige casi todo**: cada tipo tiene su momento, y el que es ahora gana
ahora. Para la ventana de octubre a marzo, la de los tres tramos:

1. **La principal sigue siendo «Tu pueblo, contado»**, como decide `VISION.md`.
2. **Octubre y noviembre: «Tres semanas de cobre».** Pasa ahora y sólo ahora, y cabe en el
   mismo viaje que la escapada: las tres escapadas del primer tramo pueden ser a pueblos
   junto a un hayedo. Coste añadido: cero.
3. **Siempre: «Fíjate en…».** Es el formato más barato que hay, se graba en cualquier
   ciudad en la que esté el dueño, y es la evolución del mejor formato publicado.
4. **De diciembre a marzo, el esquí dentro de «Organizadores Anónimos»**, sin campaña
   aparte: la edición nieve. La pieza de @ramonteli del tercer tramo puede ser la de nieve,
   y en «La Amnistía» cabe la deuda del forfait.
5. **Road trip, para Semana Santa**: «Prohibido comer en la gasolinera», preparado en
   febrero y publicado en marzo. Queda fuera de la ventana de los 4.400 €, así que se decide
   en febrero, con datos.
6. **Playa**: «Verano en enero» sólo si hay un creador canario que lo haga por canje o por
   poco dinero. «Planear para no hacer nada» se decide en abril.
7. **El pádel**, aparcado.

**Nada de esto sube el techo de 4.400 €.** Cambia a qué se dedican las tres escapadas del
primer tramo (a pueblos con hayedo) y cuál es la pieza de «Organizadores Anónimos» del
tercero (la de nieve).

---

## Fuentes

[[FUENTES]]
