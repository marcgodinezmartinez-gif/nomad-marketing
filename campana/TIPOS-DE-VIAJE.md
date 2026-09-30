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
`supabase/functions/_shared/itineraryPrompt.ts` del repo de la app). Lo que dice cada regla
(está en inglés en el código; aquí va traducida), y los destinos que el buscador de la app
propone para cada tipo:

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
3. **«¿Qué planea NOMAD para el puente en…?»**, que ya existe. En diciembre, los
   mercadillos de Navidad: Viena, del 13 de noviembre al 26 de diciembre; Praga, del 28 de
   noviembre al 6 de enero; y Colmar, del 23 de noviembre al 29 de diciembre. Estrasburgo
   todavía no ha publicado fechas. Viena recibió 31.017 viajeros de España en diciembre de
   2025, casi los mismos que en agosto.

**La capa de Vicio**: rivalidad entre ciudades, con cariño: *«Madrid contado para los de
Barcelona»*. Nunca contra los guías: la app no los sustituye y no se dice que lo haga.

**La capa de Estrella Damm**: la firma de la casa, *«La ciudad, contada»*, en piezas al
amanecer con la ciudad vacía y la voz encima.

**Cuándo**: siempre; más en los puentes, en diciembre y por San Valentín (domingo 14 de
febrero), para parejas.

**Quién**: @imartatravels (Barcelona) y @derutapormadrid (Madrid) de `CREADORES.md`,
@hoyviajamos (escapadas por Europa) de `INFLUENCERS.md`, y estas nuevas (TikTok, leídas el
30-sep):

| | Cuenta | Seguidores · mediana de vistas | Por qué | Ojo con |
|---|---|---|---|---|
| A | @rutaideal (Kalina y David, Málaga) | 88.045 · **107.900** | Escapadas por Europa y planes; llegan a más gente que sus seguidores | Afiliación de seguros de viaje en la bio |
| A | @sarapostcard (Barcelona) | 189.824 · 23.050 | «Turista en tu ciudad»: planes gratis y la Mercè | 2.073 vídeos: puede estar saturada de publi |
| A | @pdeplanazos (María, Madrid) | 57.782 · 18.600 | Planes en Madrid y escapadas, **con lo que cuestan** | Enlace de descuentos en la bio |
| B | @gianpiaventuras (Madrid) | 31.880 · 21.805 | Planes en Madrid, Lisboa y Oporto | Mucho consumo y pop-ups |

**Coste**: casi cero si se graba en la ciudad de cada uno.

**Lo que hay que comprobar**: lo de siempre, cada dato contra dos fuentes. En un museo,
sólo donde se puede grabar.

---

## 2. Playa: «Planear para no hacer nada»

**Lo que enseña**: el día según el sol, y un plan que presume de tener poco. La regla de la
app dice que *«dos o tres actividades en un día completo es lo correcto aquí, no un fallo en
llenarlo»*, y trata el atardecer como un acontecimiento.

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
corta. En el último trimestre de 2025, diciembre fue el mes con más viajes de los
residentes en España: 13,2 millones (INE). En Navidad, la ocupación hotelera de la
provincia de Santa Cruz de Tenerife fue del 85,8 %.

**Después: «Planear para no hacer nada»**, de junio a septiembre de 2027, con la decisión
tomada en abril.

**Quién** (TikTok, leídas el 30-sep; de Baleares no salió ninguna, y con la masificación de
por medio no es mala noticia):

| | Cuenta | Seguidores · mediana de vistas | Por qué | Ojo con |
|---|---|---|---|---|
| A | @localguidegrancanaria | 75.204 · 17.950 | Gran Canaria contada por alguien de allí: planes de finde, tascas, charcos y piscinas naturales. Sol en invierno sin «calas secretas» | Enlace de descuentos en la bio (probable afiliación) |
| B | @lamochiladesara (Sara Caballero) | 37.376 · 25.900 | Escapadas de playa «más baratas de lo que crees» | Publica poco; hace publi con Skyscanner |

**Coste**: un viaje a Canarias si lo graba el dueño, o una pieza de un creador que ya vive
allí, que es lo barato.

**Lo que hay que comprobar**: **nada de «calas secretas»**. El Caló des Moro, en
Mallorca, recibía unas 4.000 visitas al día en 2024 para un sitio en el que caben unas
100, y el auge se atribuye a Instagram y TikTok. En julio de 2026 decenas de miles de
personas se manifestaron en Palma contra la turistificación. Una cala masificada por un
vídeo es la peor prensa posible para una app de viajes.

---

## 3. Naturaleza: «Tres semanas de cobre» y «Sin postureo»

**Lo que enseña**: la honestidad de la ruta —cuánto dura y lo dura que es—, los permisos
en las notas, empezar temprano, y comer donde está el día.

**Dos ideas, una para cada estación:**

**«Tres semanas de cobre»** (octubre-noviembre, o sea **ahora**). El hayedo sólo está de
cobre unas semanas al año, y saber qué fin de semana ir lo es todo. La app enseña el tiempo
de esos días y escribe la ruta y dónde comer en el pueblo de al lado. Es un
ritual con fecha, lo de Estrella Damm, y encaja con la escapada del dueño: los hayedos
famosos están junto a pueblos muy pequeños. El color llega a su máximo en la segunda
quincena de octubre y la primera de noviembre.

**Y aquí la app tiene que demostrar lo que dice**, porque casi todos los hayedos tienen
normas de acceso:

- Irati cobra 7 € por coche y cierra el acceso cuando se llenan los aparcamientos.
- Tejera Negra pide reservar el aparcamiento los fines de semana de octubre y noviembre.
- Montejo sólo se visita con guía, gratis y con una reserva que se sortea.
- A la pradera de Ordesa sólo se sube en autobús desde Torla en las fechas marcadas; son
  6 € y no se vende por internet.

La regla de la app pide poner en las notas los permisos y las reservas. **Se comprueba en
cada plan antes de grabarlo**: si la app no avisa de la reserva de Tejera Negra, el vídeo
no sale, y es un fallo para el repo de la app.

**«Sin postureo»** (primavera y verano). La foto famosa contra lo que dice la app: *«4 h
30, sin sombra, reserva obligatoria»*. Y luego la ruta de verdad. La capa de Vicio sale
sola: *«La app que te dice que esa ruta no es para ti.»*

**La competencia, dicha para no pelear con quien no toca**: Wikiloc, que es española,
tiene más de 19 millones de usuarios y unos 74 millones de rutas, y AllTrails, 100
millones de miembros. Las dos planifican la ruta, no el viaje. NOMAD no es una app de
tracks: es el viaje alrededor de la ruta. Qué día ir con el tiempo que va a hacer, dónde
comer y cómo encaja la ruta en el resto del viaje.

**Quién**: @mochileandosobreruedas (naturaleza y pueblos) de `CREADORES.md`, @viajesyrutas
de `INFLUENCERS.md`, y estas nuevas (TikTok, leídas el 30-sep):

| | Cuenta | Seguidores · mediana de vistas | Por qué | Ojo con |
|---|---|---|---|---|
| A | @myro.ko (Catalunya) | 23.959 · 20.100 | Pirineo, Aigüestortes, Mont-rebei; **da distancia, tiempo y a veces dificultad**, que es «Sin postureo» tal cual | Su correo es de Ucrania: comprobar que su público es español |
| A | @davidrutas | 42.962 · 26.200 | Rutas por Catalunya, Teruel y Cuenca: pasarelas, ríos y cañones; constante | Parte de su público puede ser latinoamericano |
| A | @viajar__contigo (Manoli y Álex) | TT 29.416 · IG más de 284K | Su formato estrella es **el itinerario de X días**, lo que escribe NOMAD; su «escapada de 3 días por Huesca este otoño» llegó a 463.200 | Publi frecuente; hoteles de lujo |

**Coste**: el de la escapada, unos 75 €, con la del pueblo en el mismo viaje.

**Lo que hay que comprobar**: **se graba sin dron**. En un parque nacional está prohibido
volar por debajo de 3.000 m sin autorización (Ley 30/2014), y en otros espacios protegidos
hace falta el permiso del gestor. Tampoco se manda a nadie a una ruta peligrosa, y no se
empuja hacia un sitio que ya está masificado.

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

**La segunda idea: «Plan B»**. *«¿Y si no nieva?»*. La regla de la app le pide escribir
siempre qué hacer si no hay nieve o cierran los remontes: un paseo por el valle, el pueblo,
unas termas. Es útil, y en España pasa cada vez más. Como todo, se comprueba en el plan
antes de enseñarlo.

**La capa de Estrella Damm**: la primera bajada del año con los de siempre.

**Los números que la sostienen**: el forfait de un día en Baqueira pasó de 70 € en
2025-26 (71,50 €), y el forfait más el alojamiento salen por entre 118 y 172 € por persona
y día según la estación (Holidu), sin comida, material ni viaje. España hizo 4,6 millones
de días de esquí en 2024-25 (ATUDEM). En Sierra Nevada, el 94,8 % de los esquiadores de
2025-26 fueron españoles.

**La competencia**: las apps de esquí (Skitude, Slopes o las de cada estación) dan el parte
de nieve, el mapa de pistas y el forfait. **Ninguna organiza el viaje día a día.**

**Cuándo**: desde el puente de diciembre, que este año es de cuatro días en nueve
comunidades y en Melilla. Las aperturas previstas, si hay nieve: Baqueira el 28 de
noviembre, Formigal el 27 (orientativa) y Grandvalira hacia el 4 de diciembre. Sigue
hasta Semana Santa, con Carnaval en medio.

**Quién**: **en TikTok España casi no hay creadores de nieve dedicados** entre 20.000 y
500.000 seguidores. Lo que hay son generalistas que ya hicieron su viaje de esquí, y cuentas
pequeñas de nieve para canje:

| | Cuenta | Seguidores · mediana de vistas | Por qué | Ojo con |
|---|---|---|---|---|
| B | @francuellar26_ | 339.033 · 8.109 | En febrero de 2025 publicó su viaje de esquí a Saint-Lary **con el presupuesto por persona (750 €)**: «Nieve a medias» antes de que existiera | Generalista, publi frecuente, agencia Keepers |
| B | @dani_abreu (Andorra) | 47.193 · 51.100 | Nevadas y curiosidades de Andorra; su «La gran nevada» llegó a 2,3 M | Publica a trompicones: nada en los últimos 30 días |
| C | @artaishreds · @110ski | 8.805 · 4.507 | Snowboard y esquí de travesía: credibilidad técnica, para canje | Muy pequeñas |

Y una agencia que no es creador pero habla a este público: @esquiades_com vende hotel y
forfait. Es competencia o socio, no una pieza.

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

**La segunda idea: «Tu copiloto»**. El asistente de la app se llama «copiloto» en la
propia app: *«El copiloto se despierta el día que empiece el viaje»*, dice antes de salir.
Sketches del amigo que se duerme de copiloto, el que no sabe leer un mapa y el que pone la
misma canción: *«Por fin un copiloto que sabe dónde parar.»* Encaja con los humoristas de
«Organizadores Anónimos».

**La capa de Estrella Damm**: las ventanillas bajadas y una carretera con nombre, como la
N-260, que cruza el Pirineo de Portbou a Sabiñánigo.

**El momento acompaña**: España es el primer destino de alquiler de coches (Skyscanner,
2026), y las autocaravanas y campers repuntan (+25 % de matriculaciones en junio de 2026).

**La competencia**: Park4night (unos 9 millones de usuarios) dice dónde parar y dormir con
la furgoneta. Roadtrippers planifica la ruta entera con IA, pero **sólo funciona en Estados
Unidos y Canadá**. Las apps de road trip que se usan aquí no escriben el día con la comida
en ruta.

**Cuándo**: los puentes, Semana Santa (del 25 al 29 de marzo de 2027) y el verano.

**Quién**: @mochileandosobreruedas y @conunpardemaletas (camper), @viajesyrutas y
@unaideaunviaje (rutas en coche), y estas nuevas (TikTok, leídas el 30-sep):

| | Cuenta | Seguidores · mediana de vistas | Por qué | Ojo con |
|---|---|---|---|---|
| A | @lakillawander (Ainara y su gata Levante) | 52.881 · 10.700 | Vive en una furgo; cuenta las cumbres sin adornos («5 cumbres, 13 km, +1.000 m») | Ritmo medio |
| A | @viajeros30 (Rebeca Serna, Burgos) | 44.319 · 9.877 | «Bloguera, furgonetera y montañera»: road trips y escapadas, con oficio con marcas | Publica poco; mucha publi |

**Coste**: gasolina y comida, como la escapada.

**Lo que hay que comprobar**: la Ley de Tráfico prohíbe al conductor usar el móvil (art.
13.3): 200 € y hasta 6 puntos, y grabar es usarlo. **Graba siempre el pasajero**, y nunca
se enseña al conductor con el móvil.

---

## 6. Y un nicho, por si sirve: «La rutina también viaja»

La app reserva hueco para el deporte de cada uno, de una pista de pádel por horas a una
ruta para correr, y lo pone donde se hace de verdad. *«Le pedí a una app una pista de pádel
en Roma. Me la ha encontrado.»* El 9,7 % de los mayores de 15 años jugó al pádel el último
año, uno de cada cuatro tiene palas en casa (Encuesta de Hábitos Deportivos 2024-25), y
España es el país con más pistas del mundo. Es un nicho, pero el pádel tiene público propio
y nadie le habla de viajes.

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
   junto a un hayedo. Coste añadido: cero. Si se quiere una cara, por canje, porque el
   segundo tramo llega tarde para el otoño: @myro.ko o @davidrutas, que ya publican rutas
   con tiempo y dificultad.
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

Consultadas el 30-sep-2026, salvo la fecha que diga cada una.

**La app**: `supabase/functions/_shared/itineraryPrompt.ts` (las reglas por tipo de viaje y
los deportes), `mobile/src/lib/destinationFinder.ts` (los destinos del buscador) y
`mobile/src/lib/tourScript.ts` (el «Fíjate en»), todos del repo de la app; y `tours_cache`
en producción.

**Creadores**: los perfiles y el embed oficial de TikTok (`tiktok.com/embed/@usuario`),
leídos el 30-sep; las cifras de Instagram, de [Metricool, feb-2026](https://metricool.com/es/influencers-de-viajes/).

**Esquí**: [apertura y pase de Baqueira, jul-2026](https://www.nevasport.com/noticias/art/71087/el-forfait-de-temporada-de-esqui-de-baqueira-ya-esta-a-la-venta/) ·
[el forfait de Baqueira pasa de 70 €, oct-2025](https://www.nevasport.com/noticias/art/69396/baqueira-supera-la-barrera-de-los-70-euros-por-su-forfait-de-esqui/) ·
[fechas de apertura previstas](https://www.infonieve.es/estaciones-esqui/fecha-inicio-fin-temporada/) ·
[índice de precios del esquí de Holidu](https://www.holidu.es/magazine/indice-de-precios-esqui) ·
[ATUDEM, temporada 2024-25](https://www.nevasport.com/noticias/art/69506/atudem-y-rfedi-presentan-la-temporada-de-esqui-2025-2026/) ·
[balance de Sierra Nevada 2025-26](https://umb.sierranevada.es/media/jwojyzvk/nota-informativa-balance-de-temporada-25-26.docx) ·
[Skitude](https://apps.apple.com/app/skitude/id493933087) · [Slopes](https://getslopes.com/)

**Naturaleza**: [el color de otoño llega más tarde](https://es.ara.cat/medio-y-crisi-climatica/colores-otono-aparecen-vez-tarde_1_5561186.amp.html) ·
[Irati](https://navarra.okdiario.com/articulo/sociedad/otono-selva-irati-pagar-acceso-navarra/20251016113629619442.html) ·
[Tejera Negra](https://medionatural.castillalamancha.es/content/reserva-aparcamiento-hayedo-tejera-negra) ·
[Montejo](https://www.comunidad.madrid/node/6065) ·
[autobús de Ordesa](https://ordesabus.com/fechas-horarios/) ·
[Ley 30/2014 de Parques Nacionales](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12588) ·
[RD 1180/2018, drones](https://www.boe.es/eli/es/rd/2018/09/21/1180/con) ·
[Wikiloc](https://www.publico.es/en-ruta/wikiloc-app-espanola-imprescindible-salir-monte.amp.html) ·
[AllTrails](https://outdoorindustry.org/press-release/alltrails-community-reaches-100-million-members/)

**Playa**: [el Caló des Moro](https://amp.majorcadailybulletin.com/holiday/beaches/2025/07/27/134979/mallorca-hidden-gem-that-became-instagram-sensation.html) ·
[Palma, jul-2026](https://es.euronews.com/my-europe/2026/07/26/decenas-de-miles-de-personas-protestan-en-palma-contra-la-turistificacion-de-mallorca) ·
[ocupación en Navidad en Tenerife](https://ashotel.es/wp-content/uploads/2026/01/09012026-ocupacion-hotelera-Navidad-2025.pdf) ·
[viajes de residentes, INE](https://www.ine.es/dyngs/Prensa/ETR4T25.htm)

**Road trip**: [Ley de Tráfico](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11722) ·
[el auge del road trip](https://www.hosteltur.com/177667_el-auge-del-road-trip-los-viajes-por-carretera-se-consolidan-como-gran-alternativa-turistica.html) ·
[autocaravanas y campers, jun-2026](https://www.pressdigital.es/articulo/economia/2026-07-06/5944128-matriculaciones-autocaravanas-campers-crecen-254-junio-hasta-893-unidades) ·
[Park4night](https://moderncampground.com/?p=72599) ·
[Roadtrippers](https://apps.apple.com/us/app/-/id944060491)

**Ciudad y pádel**: [mercadillo de Viena](https://www.christkindlmarkt.at/) ·
[de Praga](http://trhypraha.cz/) · [de Colmar](https://www.noel-colmar.com/) ·
[llegadas a Viena](https://b2b.wien.info/de/statistik/daten/statistik-aktuell/ankuenfte-naechtigungen-2025-853782) ·
[Encuesta de Hábitos Deportivos 2024-25](https://www.educacionfpydeportes.gob.es/dam/jcr:16f3890c-024a-477a-8267-637d68ab1add/ehd-2024-25-nota-resumen.pdf) ·
[Global Padel Report 2026](https://www.padeladdict.com/global-padel-report-2026-crecimiento-madurez-padel/)
