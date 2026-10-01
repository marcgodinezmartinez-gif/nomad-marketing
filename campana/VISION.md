# La nueva visión: cómo se cuenta NOMAD en Instagram y TikTok

Escrito el 30 de septiembre de 2026, contestando al dueño: *«quiero una nueva visión de
cómo publicitarla, qué pasos seguir, a qué influencers contratar… Instagram y TikTok…
cuento con la ayuda de herramientas de IA; podría montar una campaña orgánica aparte de
los influencers. Algo innovador, del estilo de las campañas de Vicio, Estrella Damm y
marcas así».*

Aquí están: por qué hace falta (§1), qué se coge de esas dos marcas (§2), la idea (§3), la
segunda campaña (§4), lo que se publica cada semana (§5), a quién se contrata (§6), la
fábrica con IA (§7), el calendario hasta Semana Santa (§8), cómo se mide (§9), lo que
cuesta (§10) y lo que decide el dueño (§11). **Lo pendiente vive en la issue #9**, no aquí.

## En una pantalla

- **La idea: «Tu pueblo, contado».** La gente pide su pueblo en los comentarios y NOMAD
  contesta con su audioguía. En Navidad, «Tu abuela sabe más»: ponle la audioguía a tu
  abuela y graba lo que corrige. Y una pieza de 60-90 s, «La otra audioguía». Es lo que
  nadie más puede enseñar, y la gente lo reenvía (§3). Y una vez a la semana, **la
  escapada**: un pueblo muy pequeño con el día escrito por la app, hasta la mesa del
  restaurante y la cuenta (idea del dueño, §3.6).
- **De enero a Semana Santa, «Organizadores Anónimos»**, para el que siempre organiza el
  viaje, con «La Amnistía»: NOMAD salda deudas de viajes entre amigos (§4).
- **Siempre encendido**: «¿Qué planea NOMAD para…?» con el plan copiable en la app, y
  cinco vídeos a la semana, TikTok primero (§5).
- **Los creadores tienen un papel, no un precio por seguidor**: una abuela para la pieza
  de Navidad, creadores de pueblo para la serie, un humorista que ya hizo «el amigo que
  organiza» (§6 y `CREADORES.md`).
- **IA detrás de la cámara, gente y sitios de verdad delante, y etiquetado** (§7).
- **Lo grande va en diciembre**, cuando esté Android; octubre es para probar con iOS (§8).
- **Tres presupuestos hasta enero: unos 700, 4.400 o 18.000 €.** El dueño elige el de
  4.400 como techo, en tres tramos que sólo se abren si el anterior funcionó: hoy se
  arriesgan 325 € (§10). Lo demás que decides tú, en §11.

**Lo que este documento NO hace**, para que nadie lo busque dentro:

- No fabrica ninguna pieza, no escribe a ningún creador y no gasta un euro. Cada pieza se
  hace después con lo que ya hay en `piezas/`, y cada gasto lo decide el dueño.
- No toca la app ni la ficha de la tienda. Dos propuestas necesitarían el repo de la app
  (§3.5) y van marcadas como tales, sin darlas por hechas.
- No cambia los precios.
- No tira lo hecho: los guiones G1-G8, «¿Qué planea NOMAD para…?», «¿Conocías este
  lugar?» y la lista de `INFLUENCERS.md` se recolocan dentro de esto (§5 y §6).

**Y no es el único menú**: la misma idea para ciudad, playa, naturaleza, esquí y road trip,
con su comparativa y una propuesta de cuáles y en qué orden, está en
**`campana/TIPOS-DE-VIAJE.md`** (30-sep, a petición del dueño).

---

## 1. Por qué hace falta: lo que dicen los datos

| | |
|---|---|
| Altas en la lista, 31-ago → 30-sep (consulta de hoy a la base) | **14**: 10 de Instagram orgánico (8 en castellano, 2 en italiano), 2 invitaciones, 1 anuncio, 1 directa |
| Lo que se esperaba en septiembre (`LANZAMIENTO-PUBLICIDAD.md`) | 350 |
| La campaña de Meta | 20.000 de alcance → 457 visitas → **1 alta** (0,22 %). Cuatro argumentos distintos y los cuatro igual de muertos |
| El reel del demo | 1.258 espectadores, **4 s** vistos de 43, **0 guardados**; la distribución se paró a las 36 horas |
| La app hoy | 16 cuentas, todas de prueba |

Tres conclusiones, y la visión sale de ellas:

1. **Lo que falló fue lo que se pedía, no cómo se pedía.** Nadie da su correo por una app
   que no puede tocar; por eso cayeron los cuatro argumentos a la vez. Desde octubre se pide
   otra cosa, que es probarla, y eso cambia qué contenido sirve.
2. **Lo orgánico trajo diez veces más que lo pagado**, y es lo único que se paga solo:
   `INFLUENCERS.md` calculó que comprar alcance sale por unos 100 € el alta cuando un alta
   vale 0,24 €. **La campaña tiene que estar hecha para que la gente la reenvíe, no para
   comprarla.** Es lo que hacen Vicio y Estrella Damm, cada una a su manera (§2).
3. **Una demo no se guarda; una historia o un plan, sí.** «¿Conocías este lugar?» es el
   mejor formato publicado por esa razón: *vale por sí solo aunque nadie se descargue
   nada*. La idea de §3 es ese formato llevado a donde nadie más puede llegar.

Y dos hechos que ordenan el calendario:

- **iOS sale en días; Android, no antes de la segunda quincena de octubre.** La prueba
  cerrada de Google se aprobó el 30-sep y pide 12 testers durante 14 días (NOMAD#303), y
  después Google revisa. Lo prudente es contar con noviembre. Y en España **casi siete de
  cada diez móviles son Android**: el 69,5 % del tráfico web móvil de 2026 (StatCounter,
  enero-septiembre). **Gastar el alcance grande antes de que salga Android es regalar la
  mayor parte**, así que el golpe grande va en diciembre (§8).
- **La app ya sabe contar un sitio pequeño.** `tours_cache` tiene 55 tours de 15 sitios, y
  no sólo capitales: Porrentruy (Suiza, unos 7.000 habitantes), Premià de Mar, Arrecife. La
  primera parada de Porrentruy empieza así: *«Durante más de doscientos años, este castillo
  no fue solo una fortaleza, sino la sede de la corte de los príncipes-obispos de
  Basilea»*, y te dice dónde ponerte: *«en el patio principal del castillo, junto a la
  balaustrada de piedra que domina el casco antiguo»*. Ése es el material de la campaña.

---

## 2. Lo que se coge de Vicio y de Estrella Damm

Parecen opuestas —una hamburguesería gamberra y una cerveza con cine de verano— y hacen lo
mismo: **la gente reenvía su publicidad porque no parece publicidad.** Vicio pasó de 0,2 M€
de facturación en 2020 a 55 M€ en 2024 diciendo que *«no ha habido nunca paid»*. Estrella
Damm estrena cada verano desde 2009 un corto que la prensa trata como el aviso de que
empieza el verano.

| | Vicio | Estrella Damm |
|---|---|---|
| **El método** | «Provocación educada»; una sola voz *«desde el producto, al packaging, al DM»*; equipo propio; *«falla rápido, falla barato»*. **Y el fundador no sale:** *«nunca participo directamente con mi imagen»* | Un lugar real, un grupo de amigos o un amor, nostalgia de lo que se repite, una canción que no suena a anuncio y **un estreno con fecha fija** |
| **La acción que lo resume** | Abril de 2024: flyers en el pomo de cada habitación del hotel de la convención mundial de McDonald's en Barcelona, reservando una sola noche. 300.000 reproducciones en menos de 24 h | *Verano del 78* (2024): una nieta recibe las fotos de su abuela, que ya ha muerto, y recorre los sitios de aquel verano. Es casi literalmente lo que hace NOMAD |
| **La que más se parece a esto** | Febrero de 2026: una clienta de A Coruña les mandó más de 800 mensajes pidiendo un local, y en la apertura la hicieron protagonista | *Lo mismo de siempre* (2025): cinco amigos, la misma casa, la misma playa, las mismas excursiones |
| **Lo que no se copia** | La Velada del Año, donde se jugaron la mitad de su presupuesto anual; Ferran Torres; cien creadores | Veinte caras conocidas y producción de cine |

**Lo que sí se coge, en cinco reglas:**

1. **Una sola voz, del pie de foto al mensaje directo** (Vicio).
2. **El producto por delante del famoso.** En «Perdona Ferran» (22-sep-2026) una
   hamburguesa tapa la cara del campeón del mundo. Aquí no hay famoso que tapar: la
   protagonista es la voz de NOMAD contando un sitio real.
3. **Lo que pide un fan se convierte en el acto.** Los 800 mensajes de A Coruña son, en
   pequeño, «pide tu pueblo en los comentarios» (Vicio).
4. **Un sitio concreto, gente de verdad y un ritual con fecha** (Estrella Damm).
5. **Los mayores, con dignidad y nunca como chiste.** Marina Prieto, la abuela gallega de
   100 años que JCDecaux y DAVID pusieron en el Metro de Madrid en 2023, pasó de 28 a más de
   39.000 seguidores y ganó seis Leones en Cannes. Nocilla, La Cocinera y Fabada Litoral se
   llevaron críticas por pintar a los mayores como torpes.

**Y una sexta que enseñan los que lo hicieron mal: la IA como estética fracasa.** Coca-Cola
se llevó críticas por sus anuncios de Navidad hechos con IA en 2024 y otra vez en 2025, y
McDonald's Países Bajos retiró el suyo en diciembre de 2025. Kantar (noviembre de 2025) lo
resume en que el público rechaza lo que «distrae o es poco natural». La IA funciona cuando
es el chiste —«el anuncio de CampofrIA», 2023— o **cuando hace algo que nadie más podría
hacer**, que es el caso de §3.4.

(De paso, una advertencia gratis de la otra cara del descaro: en julio de 2026 FACUA
denunció a Milfshakes, el socio de Vicio en su falso juicio, por prometer un 99 % de
descuento si España ganaba el Mundial. **El descaro se para donde empieza la promesa que
no se cumple.**)

---

## 3. La idea: «Tu pueblo, contado»

La firma de NOMAD ya existe y la eligió el dueño: **«Los días escritos. La ciudad,
contada.»** La campaña es su segunda mitad llevada a donde ninguna guía ha llegado nunca:

> **Tu pueblo, contado.**

### 3.1 Por qué el pueblo

- **España es un país de pueblos, y a casi ninguno lo ha contado nunca una guía.** De
  8.132 municipios, 4.980 tienen menos de 1.000 habitantes (el 61 %) y 1.406 no llegan a
  cien (INE, a 1-ene-2025). Cuánta gente «tiene pueblo» no lo mide ninguna encuesta
  fiable: es la intuición de la campaña, y la mide la propia serie. Si nadie pide el suyo
  en los comentarios, la intuición era falsa.
- **Enseña el foso sin enseñar la app.** `MERCADO-2026-08-15.md` lo dejó escrito: el
  itinerario lo regala ChatGPT; lo que nadie más hace es guiarte a pie *por cualquier
  sitio*. Un pueblo de 300 habitantes contado con voz es esa frase demostrada, y con
  emoción en vez de con una lista de funciones.
- **Se reenvía solo.** Tu pueblo narrado se manda al grupo de la familia, y el orgullo de
  pueblo —y la rivalidad con el de al lado— llena los comentarios. En Instagram, Mosseri
  cuenta tres señales —tiempo de visionado, «me gusta» por alcance y **envíos por alcance**—
  y los envíos son los que más pesan para llegar a quien no te sigue.
- **No se acaba.** Cada pueblo es un vídeo nuevo, una búsqueda nueva («qué ver en…») y, a
  veces, una noticia en la prensa local.
- **Es barato de verdad.** Narrar un tour nuevo de siete paradas le cuesta a NOMAD unos
  0,10 € (0,20 € desde enero, cuando Gemini dobla la tarifa: `docs/ECONOMIA.md`), y **cero**
  si ese pueblo ya se narró antes.
- **Nadie lo tiene.** De lo revisado, ninguno promete «cualquier pueblo, a demanda»:
  VoiceMap cubre las grandes ciudades con guías humanos, izi.TRAVEL depende de que alguien
  suba la guía, SmartGuide es una herramienta para oficinas de turismo, y Audiala, la más
  parecida, hace audioguías con IA de unas 1.100 ciudades. Faltan por mirar las apps de
  diputaciones y ayuntamientos.

### 3.2 Tres niveles, como una campaña y no como un post

1. **La serie: «¿Tu pueblo tiene audioguía?»** (siempre encendida desde noviembre). La
   gente pide su pueblo en los comentarios y NOMAD **contesta con un vídeo**: la voz real
   de la app, tres paradas, dónde ponerse y la curiosidad que nadie sabía. En TikTok es
   «responder con vídeo»; en Instagram, «responder con un reel». Cada respuesta es un vídeo
   nuevo que sale en el perfil de NOMAD y le llega a quien lo pidió.
2. **El ritual: «Tu abuela sabe más»** (Navidad). *Ponle la audioguía de su pueblo a tu
   abuela y graba lo que dice.* La app cuenta la historia que está escrita; la abuela, la
   que no: dónde estaba el cine, quién vivía en esa casa, que eso no fue así. **La IA sabe
   mucho. Tu abuela, más.** Vale igual el abuelo, la tía o el del bar: quien sepa.
3. **La pieza: «La otra audioguía»** (estreno la semana del 14 de diciembre). Un documental
   de 60-90 s: alguien que vuelve al pueblo por Navidad, lo recorre con su abuela y la
   audioguía, y ella la va interrumpiendo con su vida. Personas de verdad, pueblo de
   verdad, app de verdad. Cierra con: *«La historia de tu pueblo te la cuenta NOMAD. La de
   verdad, tu abuela.»* Y la música, si puede ser, **una canción del pueblo cantada por
   ella**: una canción popular tradicional es de dominio público y el momento no lo compra
   ningún presupuesto. Es, en pequeño, *Verano del 78*.

**Un permiso que no se salta**: para volver a publicar en la cuenta de NOMAD el vídeo de
alguien con su abuela hace falta su permiso por escrito (un mensaje basta) y el de la abuela.
La voz y la imagen de una persona no se usan en publicidad sin consentimiento expreso (Ley
Orgánica 1/1982, art. 7.6).

**Por qué «Tu abuela sabe más» es la parte lista y no sólo la tierna**: el mayor riesgo de
la idea es que la IA diga algo inexacto de un pueblo de 300 habitantes delante de los 300.
Esta campaña **invita a corregirla**. Convierte el riesgo en el motor: cada corrección es un
comentario, un vídeo de respuesta y una prueba de que la marca no se cree más lista que
nadie. En un feed lleno de IA que presume, **una IA que escucha a la abuela** es lo
innovador. (Eso no quita la regla de §7: lo que publica NOMAD se comprueba antes.)

### 3.3 La capa de Vicio: el descaro

El territorio es tierno; el tono de la serie, no siempre. Ganchos de ejemplo:

- *«Le hemos hecho audioguía al pueblo más pequeño de España. Tiene seis habitantes.»* Y
  son dos, empatados a seis según el INE: Torremochuela (Guadalajara) y Villanueva de Gormaz
  (Soria). La rivalidad viene hecha: *«¿cuál de los dos?»*.
- *«Los de [pueblo A] dicen que lo suyo es más bonito que [pueblo B]. Que decida la
  audioguía.»*
- *«Audioguía de tu pueblo para los del pueblo de al lado.»*
- *«Hemos contado cien pueblos. El que más pide su gente es…»* (el ranking semanal)
- *«Tu pueblo tiene más historia que tu ciudad. Treinta segundos.»*

**La regla: humor CON el pueblo, nunca contra él.** Nada que se ría de la gente mayor, del
acento o de la despoblación. Y el fin de semana de Todos los Santos (31-oct a 2-nov), que es
cuando más gente vuelve al pueblo a los cementerios, la serie calla.

### 3.4 Lo innovador, dicho en una frase

**Una marca que contesta cada comentario con una audioguía hecha para ese pueblo.** No es IA
de adorno ni un anuncio hecho con IA: es el producto trabajando delante del público, en
personalizado y a escala. Eso sólo lo puede hacer quien genera las guías, y es lo que lo
separa del «anuncio hecho con IA» que la gente ya se salta: en junio de 2026, el 73 % decía
confiar menos en un anuncio que sospecha hecho con IA (Harris Poll y 4As).

### 3.5 La palanca que lo multiplica todo (repo de la app, decisión del dueño)

**Que la audioguía de tu pueblo sea gratis durante la campaña**, una por cuenta. Hoy un tour
suelto cuesta 0,99 €, y generarlo le cuesta a NOMAD 0,10-0,20 €. Regalar el primero
convierte cada vídeo en una descarga con premio inmediato, por unos céntimos por cuenta que
la usa. Comprar una instalación en Apple Ads cuesta en España una mediana de **1,43 $**
(AppTweak, datos de 2025). Necesita un cambio en el servidor (un derecho de «un tour gratis
por cuenta», o un código de oferta) y es trabajo del repo de la app, no de éste.

Y un paso más allá, para después: **una página `travelsnomad.com/pueblo/<nombre>`** donde
se escucha la primera parada sin instalar nada, con su tarjeta de previsualización para
WhatsApp. Es lo que convertiría cada grupo de familia en un canal. Es trabajo grande (coste
por escucha, abuso, caché) y va después de probar la serie a mano.

### 3.6 La escapada al pueblo (idea del dueño, 30-sep)

*«Mostrar pueblos pequeños, hacer el tour por el pueblo y lo que tenga cerca, como una
escapada. Y el gancho de que te recomienda el restaurante del pueblo: grabar en el
restaurante, que se come súper bien y súper barato.»*

Es la mitad que le faltaba a la idea. La serie de respuestas enseña la audioguía de **tu**
pueblo; la escapada enseña un pueblo al que **no** has ido, con el día entero escrito. Lo
que añade:

- **El producto entero en una historia**: el plan, la voz, lo de alrededor, la comida y lo
  que cuesta. La respuesta de pueblo sólo enseña la audioguía.
- **Convierte**: lo que se compra es un viaje, y una escapada es un viaje de uno a tres
  días, desde 2,99 €, que se puede copiar con el código R-.
- **La comida es el final que se guarda y se reenvía**, y el restaurante y el ayuntamiento
  lo comparten.
- **Ayuda al pueblo sin sermón**: llevar gente al único bar de un pueblo pequeño es el
  propósito que Estrella Damm contaba con el plástico, aquí sin predicar.

**Lo que hay que comprobar antes de grabar, porque la app no siempre nombra el
restaurante.** En una ciudad casi siempre lo hace; en un pueblo, sólo si Mapbox encuentra
cerca un sitio de comer con ese nombre (#256 del repo de la app, 28-sep). Si no, la comida
se queda en «Comida en <pueblo>». Visto hoy en los viajes creados desde ese día: Vigo sale
con «Comida en O Portón» y «Comida en A Chabola», y Cangas, al otro lado de la ría, con
«Comida en Cangas». En un pueblo de cien habitantes lo normal será lo segundo, o que no haya
dónde comer. **Cuanto más pequeño el pueblo, mejor el gancho y menos probable el
restaurante.** Por eso el orden es: generar el plan, mirar si nombra un restaurante real,
llamarlo para saber si abre ese día, y sólo entonces ir. La app también pone precio a cada
comida (25 € era lo típico en esos viajes): lo que se enseña al final es **la cuenta de
verdad**, y si sale más barata que lo que dijo la app, mejor.

**El formato: 60-75 s en TikTok y un carrusel en Instagram.**

| Tramo | Qué se ve |
|---|---|
| 0-2 s | El cartel del pueblo y el número: *«38 habitantes. Le pedí a una app que me organizara el día aquí.»* |
| 2-8 s | El plan en la pantalla, con horas y precios |
| 8-35 s | El tour con la voz de la app, y lo de alrededor: *«y a diez minutos…»* |
| 35-55 s | La comida: lo que dijo la app, la mesa, el menú y **la cuenta** |
| 55-65 s | *«Todo el día: X €. Cópialo con el código R-…»*, y *«¿qué pueblo hacemos la semana que viene?»* |

El carrusel lleva el plan entero por horas, el restaurante con su precio y el total: es lo
que se guarda.

**Ganchos para elegir** con las tres primeras (los números, los reales de cada pueblo):

- *«Le dejé a una app elegir dónde comer en un pueblo de 40 habitantes.»*
- *«Un pueblo de 38 habitantes, su audioguía y un menú de 14 €.»*
- *«El único bar de un pueblo de 50 habitantes. Lo encontró una app.»*
- Y la serie, con cuenta atrás: *«Hay 4.980 pueblos en España con menos de mil habitantes.
  Empezamos por el que más votéis.»* Con «menos de cien» son 1.406 y el gancho pega más,
  pero casi ninguno tiene dónde comer.

**La placa, que es el gesto de Vicio**: al irse, una pegatina en la puerta del restaurante,
con su permiso: *«Este pueblo tiene audioguía»*, con un QR a la App Store con su propio
`ct=placa-<pueblo>`. Cuesta unos euros, se graba como cierre del episodio y deja en el pueblo
un punto de descarga que se puede medir.

**Lo que no se hace**: decir que la app recomendó un sitio que no recomendó; dejar que
invite el restaurante sin decirlo (se paga la cuenta, y si invitan, se dice); grabar dentro
sin permiso o a otros clientes reconocibles sin el suyo; construir el episodio sobre una
fiesta con fecha y hora; y escribir «barato» donde puede ir la cuenta.

**Quién lo graba y cuánto cuesta**: el dueño, sin salir en cámara si no quiere —funciona en
primera persona, con las manos, la mesa y la voz de la app—, por la gasolina y la comida,
unos 50-100 € y un día por episodio. O @ahora.vas.y.lo.vi, que ya hacen itinerarios día a
día por España (unos 500 € por pieza, `CREADORES.md`), y los creadores de pueblo de §6, cada
uno en su zona. **Uno a la semana como mucho**; las respuestas con la audioguía llenan el
resto de días. El primer episodio puede ser uno de los diez pueblos de prueba de §8: la
misma comprobación, más la del restaurante.

---

## 4. La segunda campaña (enero-marzo): «Organizadores Anónimos»

El pueblo abre la conversación; **lo que se vende en Semana Santa es el viaje en grupo**, y
el que paga es siempre el mismo: el que organiza. `INFLUENCERS.md` ya lo apuntó como
formato («Quién debe qué») y el copy E de agosto también. Aquí sube a campaña.

- **La idea**: un grupo de apoyo para los que siempre organizan el viaje. *«Hola, soy Marta
  y llevo once años organizando el viaje de las amigas.»* Aplausos. Una serie de
  confesiones de 20-30 s, con creadores de humor y abierta a que la gente mande la suya.
  Cierre: *«Paso uno: admitir que necesitas ayuda. Paso dos: dejar que organice otro.»* Y
  la firma, que ya está en la bio de TikTok: **«Nosotros organizamos. Tú viajas.»**
- **La acción, a lo Vicio: «La Amnistía»**, la semana de la cuesta de enero (arranca el
  Blue Monday, 18-ene-2027). Cuéntanos la deuda de viaje más antigua de tu grupo y NOMAD
  la salda: un jurado elige las diez mejores historias y se le paga al que puso el dinero,
  hasta 50 € cada una. Tope: 500 €. Lo que la hace legal y barata, a confirmar con un
  asesor antes de lanzarla:
  - **Es un concurso, no un sorteo.** Gratis y decidido por un jurado, queda fuera de la ley
    del juego y de su impuesto del 10 %; con premios de menos de 300 € no hay retención de
    IRPF. Lleva sus bases legales publicadas; el notario no es obligatorio.
  - **Etiquetar al deudor, opcional.** Meta prohíbe exigir o premiar etiquetas en una
    promoción. La gente etiquetará igual: es lo gracioso.
  - **Sólo se publica una historia con permiso de las dos personas.** Señalar a alguien
    como deudor en público toca su derecho al honor.
  - Se paga por transferencia, con justificante.
- **El argumento de producto, en una línea**: una compra abre el viaje a todo el grupo y
  entra sola en los gastos. *«Sale a menos de un euro por cabeza, y la app ya lo ha
  apuntado.»*
- **Por qué en enero**: la Semana Santa de 2027 va del Jueves Santo 25 al Lunes de Pascua
  29 de marzo, y enero es cuando empieza a hablarse de ella en los grupos. No hay un dato
  público fiable de con cuánta antelación se planifica, así que la fecha de arranque es una
  apuesta, dicha como tal. Y la semana del Blue Monday es también la de FITUR (20-24 de
  enero), con la prensa de viajes mirando.

---

## 5. Lo que se publica cada semana

Tres pilares, una sola cuenta y una sola voz:

| Pilar | Qué | Para qué | Peso |
|---|---|---|---|
| **Tu pueblo, contado** | Respuestas con vídeo, «¿Conocías este lugar?» llevado a pueblos, el ranking | Alcance y envíos | 40 % |
| **Lo que planea NOMAD** | «¿Qué planea NOMAD para el puente de…?», con el plan escrito en el pie y **el código R- para copiarlo en la app**; y «Este finde hago lo que diga NOMAD» (48 h siguiendo el plan) | Guardados, búsquedas y descargas | 35 % |
| **Con gracia** | Tours absurdos (G6: heladerías, vermuts), temas del día, respuestas a comentarios, y el fundador si quiere salir | Personalidad y seguidores | 25 % |

**El ritmo que aguanta una persona con la fábrica de §7**: cinco vídeos a la semana en
TikTok, los mismos en Reels y en Shorts, dos carruseles, y una historia al día. Cinco y no
uno porque el volumen se nota: pasar de un vídeo a la semana a entre dos y cinco da un 17 %
más de visualizaciones **por vídeo**, y entre seis y diez, un 29 % (Buffer, sobre 11,4 M de
publicaciones, también en cuentas pequeñas). Duolingo empezó igual: tres a cinco a la
semana, entre 15 minutos y dos horas cada uno.

**TikTok primero, Instagram después.** Los reels de prueba de Instagram —los que se
enseñan sólo a quien no te sigue— piden 1.000 seguidores, y TikTok es donde una cuenta
pequeña todavía llega a desconocidos. La serie se estrena allí y se sube a Reels la que
funcione. En TikTok, lo que más interacción saca son los vídeos de 15-30 s (6 %,
Socialinsider, sobre 6 M de vídeos de 2026); en Instagram, el carrusel logra nueve veces
más guardados que la foto suelta (Metricool, 2026), que es por lo que «¿Qué planea NOMAD
para…?» es un carrusel.

**Una cosa que comprobar antes de la primera pieza**: la casa sube los reels sin audio para
elegir el de tendencia dentro de la app, y hay fuentes que dicen que **una cuenta de empresa
sólo ve la biblioteca comercial** en Instagram y en TikTok. Se mira en @app.nomad; si es así,
la música sale de esa biblioteca. Y aunque no lo fuera, una pieza con música de tendencia no
se puede anunciar después (§6): lo que tenga papeletas de acabar en anuncio va con la voz de
la app o con música comercial desde el primer día.

**La voz**: la de la app es seria y concreta; la de la campaña es la misma persona con un
punto de guasa. Humor seco, frases cortas, cero exclamaciones y cero superlativos, que es lo
que ya pide `.agents/product-marketing.md`. La gracia sale de lo concreto: *«El grupo "Roma
2027 🍝" tiene 347 mensajes y ningún plan»* hace reír porque es verdad, no porque grite.

**Lo que se hereda de la casa y no se discute**: primera persona y nunca cara de anuncio;
subtítulos siempre; el plan escrito en el pie, porque es lo que se guarda; capturas de la app
real; «desde 2,99 €» y nunca «2,99 €» a secas; el café como ancla; **nada construido sobre un
acto con fecha y hora** (la app se equivocó en los cinco de la Mercè, issue #6). Y en un
museo, sólo donde se puede grabar: el Thyssen sí (sin flash, sin palo ni trípode), el Prado
no, y el Reina Sofía pide autorización para grabar con fines comerciales. Un cuadro de
Picasso no sale en un anuncio sin licencia: su obra está protegida hasta finales de 2053.

---

## 6. A quién se contrata, y para qué

**Nadie se contrata por alcance**: `INFLUENCERS.md` ya hizo la cuenta, y sale por unos 100 €
el alta. **Cada creador tiene un papel en la idea**, se le paga **la pieza** —con permiso
para anunciarla— y el resto va a canje. La lista entera, con sus números y lo que cuesta
cada tramo, está en **`campana/CREADORES.md`**; aquí va la elección.

**Y el precio se negocia por la mediana de vistas, no por los seguidores.** Medido hoy:
@ahora.vas.y.lo.vi tiene 24.000 seguidores y una mediana de 66.000 vistas por vídeo;
@romansocias, 600.000 seguidores y 17.000 vistas.

| Papel | Cuándo | La elección | Si no | Trato |
|---|---|---|---|---|
| **La pieza de Navidad**, «La otra audioguía» | Rodaje hasta el 11-dic | **@layayamaricarmen**: una abuela leonesa que vive en Barcelona y a la que graba su nieto (367K en TikTok, mediana 154K). Su cuenta ya tiene a los personajes de la pieza; la propuesta sería llevarla a su tierra con la audioguía puesta | Un creador de `CREADORES.md` A o B que grabe a su propia abuela, o alguien de la familia del dueño (§11, punto 7). Con dinero de sobra, @teresalapelaya: 95 años, de Ágreda (Soria), mediana de 642K | Pagada, con 60 días de derechos de anuncio y el material en bruto |
| **La serie del pueblo** | Noviembre-diciembre | **@carloartspain** («te muestro la otra España»; mediana 81K) y **@laguiadeltorrao** (la historia de los nombres de los pueblos de Murcia; 8.758 seguidores y mediana de 33K) | @andybu_rural, que vive en un pueblo de 32 habitantes. Y como socios, sin dinero: Los Pueblos Más Bonitos de España y @nosvamospalpueblo.es | Carlo, pagado; el resto, canje más una tarifa pequeña |
| **«Lo que planea NOMAD»** y **«Este finde hago lo que diga NOMAD»** | Octubre-marzo | **@ahora.vas.y.lo.vi**: itinerarios día a día por España, que es lo que escribe la app | @anastasia.viajera (pueblos y fiestas) o @imartatravels (Barcelona) | Una pieza pagada; el resto, canje |
| **«Organizadores Anónimos»** | Enero-marzo | **@ramonteli**: publicó «El amigo que organiza todo en los viajes» en abril de 2025, antes de que existiera esta campaña (mediana 45K) | @petercomey («Diferentes tipos de…») o @rikomedy, que junta pueblo, grupo y fiesta en la misma cuenta | Pagado, con derechos de anuncio |
| **El museo** | Siempre | Pedro Torrijos (castillos y pueblos contados, sobre todo en Instagram) o @la.inercia (un monumento en 60 s) | @lidiamerenciano, arqueóloga | Canje; si hay pieza, pagada |
| **La cantera** | Octubre-noviembre | Las 16 cuentas A y B de Instagram de `INFLUENCERS.md` | — | Canje: un bono de regalo con código, que la app ya tiene (`regalar-viaje`) |

**Lo que no se negocia con ninguno:**

- **La etiqueta, dentro del vídeo y desde el primer segundo**: «publi» o «publicidad»,
  además de la herramienta de cada red. Es el criterio que la CNMC aplica a los grandes
  (lo recordó en sus requerimientos de junio de 2026), y se le pide a todos. **El canje también obliga**: el código de conducta de 2025
  cuenta el producto gratis como pago.
- **Audio original o de la biblioteca comercial** en todo lo que se pueda querer anunciar.
  Un reel con música de tendencia de Instagram no se puede convertir en anuncio después; la
  voz de la app es audio original y sí vale.
- **Su enlace de campaña de la App Store (`ct=<creador>`), su código de oferta** y las
  capturas de sus estadísticas. Sin ellas no se paga.
- **Nadie que venda tours o guías**: @teexplicouncuadro vende una guía del Prado y
  @albasaenc, viajes en grupo. Fuera.
- **Se mira la polémica antes de firmar.** @ramonteli opina de política territorial y
  @helioroque_ tuvo una polémica en un acto político; está anotado en `CREADORES.md`.

**Lo que cabe esperar**: de cien microcuentas de TikTok escritas en frío contestan 5-10 y
publican 1-4 (Janney y Elev8or, 2026). Con mensaje personalizado y desde un correo propio,
la respuesta sube al 25-40 %. Por eso el canje solo no basta —un viaje de 2,99 € vale poco
para un creador— y funciona mejor **canje más una tarifa pequeña, o pagarle la escapada**.

---

## 7. La fábrica con IA: cómo publica una persona cinco vídeos a la semana

La regla que lo gobierna todo: **IA detrás de la cámara; personas y sitios de verdad
delante.** La única IA que sale en pantalla es la voz de la app, y se dice que lo es.

**Una respuesta de pueblo, de la petición al vídeo (objetivo: 20 minutos):**

1. **Recoger.** Cada mañana, los pueblos pedidos en los comentarios a una lista; se cuentan
   las peticiones de cada uno (el ranking sale de ahí).
2. **Generar en la app**, como lo haría cualquiera, y grabar la pantalla con la voz sonando.
   El material es la app de verdad, no una maqueta.
3. **Comprobar.** Una sesión de Claude contrasta cada dato de la narración con dos fuentes
   (la Wikipedia del pueblo y la web del ayuntamiento, como mínimo). Lo que no se puede
   comprobar se corta en el montaje. Es la regla de «¿Conocías este lugar?».
4. **Montar** con lo que ya existe: el molde de `piezas/historias-animadas/` (el móvil de la
   casa, el velo y el cierre) y ffmpeg, con los subtítulos sacados **del texto exacto de la
   narración**, que la app ya tiene escrito.
5. **Publicar** como respuesta al comentario, con el nombre del pueblo en el pie y en el
   texto de pantalla («audioguía de…», «qué ver en…»), y etiquetando al ayuntamiento.
6. **Prensa local**, para los mejores: un correo corto que Claude redacta y el dueño manda.

Las fotos del pueblo: las que mande quien lo pidió (con su permiso, por mensaje), las del
banco con su licencia, o las que ya enseña la app en la parada. Nunca Street View.

**Las herramientas, por menos de 20 € al mes** (precios de septiembre de 2026):

| Para qué | Qué | Cuánto |
|---|---|---|
| Guiones, pies, comprobar datos, montar, pedir prensa | Claude, en la sesión sobre este repo, y `piezas/` | Lo que ya se paga |
| La voz y la historia | **La propia app** | 0,10-0,20 € por pueblo nuevo; 0 si ya está narrado |
| Recortar, subtitular, montar rápido en el móvil | **Edits**, de Meta: gratis, y su asistente de IA lee la retención. **CapCut no**: desde junio de 2025 sus términos se quedan una licencia perpetua sobre lo que subes, cara y voz incluidas | 0 € |
| Mapas animados, transiciones, planos que no sean un sitio real | Google AI Plus (Veo en Flow) | 4,99 €/mes |
| Música para una pieza que se vaya a anunciar | La biblioteca comercial de cada red, primero. Suno Pro (uso comercial, anuncios incluidos) sólo si hace falta algo propio, sabiendo que un tribunal de Múnich falló contra Suno en julio de 2026 y la sentencia está recurrida | 0 € / 10 $/mes |
| El italiano, si se abre la prueba | La app ya narra en italiano | 0 € |

**Sora ya no existe** (OpenAI cerró la app el 26-abr-2026), y no hace falta: nada de esta
visión necesita vídeo generado.

**Lo que no se hace con IA, nunca**: personas inventadas, testimonios inventados, un sitio
real pintado por una máquina como si fuera una foto, ni la voz o la cara de alguien que no
lo ha autorizado.

**Y lo que sí se hace, se dice.** Desde el 2 de agosto de 2026 el artículo 50 del
Reglamento de IA obliga a avisar de un vídeo realista generado con IA, también si lo que
enseña es un lugar real. Meta pide etiquetar el **audio realista creado digitalmente**, y la
voz de la app lo es; TikTok, el contenido realista hecho con IA. Así que cada pieza con la
voz lleva la etiqueta de la red y una línea en el pie («la voz es de NOMAD, generada con
IA»). No cuesta nada: el 87 % de los internautas españoles considera imprescindible
etiquetar lo que hace la IA (IAB Spain, 2026). Y en España hay un proyecto de ley, aprobado
por el Gobierno en mayo de 2026 y aún en el Congreso, que pondría una marca «IA» visible y
multas desde 6.000 €: mejor llegar etiquetando.

---

## 8. El calendario, de octubre a Semana Santa

Los festivos, del BOE; los días de la semana, calculados.

| Cuándo | Qué | Por qué entonces |
|---|---|---|
| **1-11 oct** · iOS en la tienda, si Apple la aprueba estos días | Lo que ya está hecho: el reel de Córdoba para el puente del Pilar (sábado 10 a lunes 12) y «¿Qué pasa el día que abra NOMAD?», si se decide el punto 8 de §11. **Diez pueblos de prueba**: generados, comprobados y montados, sin publicar todavía | La tienda abre y el Pilar es el primer puente. Los diez pueblos dicen si la idea aguanta **antes** de anunciarla |
| **13-30 oct** | Las pruebas en TikTok: seis piezas de cada pilar (§5), y las primeras respuestas de pueblo con los comentarios que haya. La cantera de `INFLUENCERS.md`, con canje | Se aprende con iOS y una cuenta pequeña, antes de que llegue el público grande |
| **31 oct-2 nov** | La serie del pueblo calla | Todos los Santos: el lunes 2 es festivo en nueve comunidades, y es cuando más gente vuelve al pueblo, al cementerio |
| **Noviembre** · Android en la tienda (previsto) | Segundo lanzamiento. La serie del pueblo, a diario, y los creadores de pueblo. El plan del puente de diciembre | Con las dos tiendas abiertas, el alcance ya no se regala |
| **5-8 dic** | «¿Qué planea NOMAD para el puente?» | El lunes 7 es festivo en nueve comunidades y en Melilla, y allí el puente es de cuatro días |
| **Hasta el 11 dic** | Rodar «La otra audioguía» | |
| **Semana del 14 dic** | Estreno de la pieza. Si pasa la tabla de §9, un empujón pagado pequeño | La gente vuelve al pueblo por Navidad, que cae en viernes |
| **20 dic-6 ene** | «Tu abuela sabe más»: el reto, abierto por los creadores de abuelos | Las familias están juntas hasta Reyes (miércoles 6) |
| **Lunes 18 ene** (Blue Monday) | «Organizadores Anónimos» y «La Amnistía» | La cuesta de enero; los grupos empiezan a hablar de Semana Santa; FITUR es esa semana |
| **Febrero-marzo** | Planes de Semana Santa (Jueves Santo 25 a Lunes de Pascua 29 de marzo), y San Valentín (domingo 14) para parejas | |

Una fecha para apuntar: **el 1 de octubre es el Día de los Pueblos Más Bonitos de
España**, la asociación de 126 pueblos que tiene su propia red de creadores y acepta
«menciones, takeovers, contenido conjunto». Este año llega un día tarde; en 2027 puede ser
el cumpleaños de la serie, que es el ritual con fecha fija que hace Estrella Damm. Y
escribirles antes es barato: ofrecerles sus 126 pueblos contados.

### Fase 0: calentar las cuentas, del 1 al 14 de octubre

Pregunta del dueño, 1-oct: *«la app va a salir en 1-2 semanas. La cuenta de Instagram
tiene 122 seguidores y la de TikTok, como 12. Habría que primero potenciar ambas cuentas
y luego empezar las campañas».*

**Sí a empezar ya; no a «primero seguidores y luego la campaña».** Hoy el alcance no lo
deciden los seguidores, lo decide el vídeo. Alrededor del 70 % de las vistas de TikTok
salen del «Para ti», que enseña cada vídeo a desconocidos (Metricool, 2026). En Instagram,
lo que saca un reel fuera de tus seguidores son los envíos. Una cuenta de 12 seguidores con
un buen vídeo llega a miles, y una de 10.000 con un mal vídeo, a nadie. **La campaña es lo
que trae los seguidores**, no lo que viene después de tenerlos.

Lo que sí hace falta tener antes del día de la tienda son cuatro cosas, y para eso son
estas dos semanas:

1. **Los perfiles listos, hoy, en una hora.**
   - **Instagram**: en el nombre, que el buscador de Instagram lee, «NOMAD · app de viajes
     y audioguías». Las destacadas, subidas, y tres publicaciones fijadas: qué es, el plan
     de Córdoba y el primer pueblo cuando exista.
   - **TikTok: pásala a cuenta de empresa.** Así el enlace de la bio se puede tocar desde
     el primer seguidor (una cuenta personal necesita 1.000). A cambio sólo se usa la música
     comercial, que es además la única con la que se puede anunciar una pieza (§5); el
     sonido de la casa es la voz de la app.
   - **El día que Apple apruebe**: la última línea de la bio deja la lista de espera y pasa
     a decir que ya está en iPhone, con el enlace a `travelsnomad.com/app`.
2. **El ritmo, desde ya**: un TikTok al día, tres o cuatro reels a la semana (los que mejor
   hayan ido en TikTok) y una historia diaria con la app de verdad. Sin cuenta atrás: no hay
   fecha de tienda, y una urgencia falsa es lo que la casa no hace.
3. **Los primeros cien o trescientos, de verdad.** Son los que dan a cada vídeo su primera
   hora, que es cuando la red decide si lo enseña a más gente:
   - una historia en el Instagram personal del dueño, con su UTM (`story-personal`), y un
     mensaje a sus grupos de WhatsApp. De las 14 altas de septiembre, 10 vinieron de
     Instagram orgánico;
   - las 14 personas de la lista y los testers de Android (NOMAD#303): un mensaje personal,
     no un correo masivo;
   - **veinte minutos al día comentando de verdad** en cuentas de viajes, de pueblos y de
     oficinas de turismo, y contestando cada comentario propio en su primera hora (en
     TikTok, con vídeo).
4. **Llegar al lanzamiento sabiendo qué formato funciona.** Con unas catorce piezas en dos
   semanas, la tabla de parada del orgánico (§9) ya dice algo el día de la tienda.

**Lo que se publica** (primero lo que ya está hecho):

| Días | Qué | Estado |
|---|---|---|
| 1-3 oct | El Panteón de «¿Conocías este lugar?»: carrusel en Instagram y en modo foto en TikTok | Listo desde el 16-sep, si no ha salido ya |
| 2-5 oct | Los primeros «Fíjate en…» de la ciudad del dueño (`TIPOS-DE-VIAJE.md` §1) | Se graban en una tarde |
| 6-8 oct | «¿Qué planea NOMAD para el puente del Pilar?», el reel de Córdoba | Montado el 29-sep; sale antes del puente (10-12) |
| 6-14 oct | Los pueblos de prueba que pasen la comprobación (abajo) | Dependen de los diez pueblos |
| El día de la tienda | El anuncio, la bio nueva y, si se decide el punto 8 de §11, «¿Qué pasa el día que abra NOMAD?» | Hecho el 29-sep |
| 10-12 oct | La primera escapada, a un pueblo junto a un hayedo, para publicarla la semana siguiente | Depende de los tres pueblos candidatos |

**Lo que no se hace para crecer**: comprar seguidores, nunca; seguir y dejar de seguir;
grupos de «me gusta»; y sorteos de «sigue y etiqueta a tres amigos», porque Meta prohíbe
exigir etiquetas y un sorteo paga el 10 % del impuesto del juego.

**Un hito que sirve de algo**: los 1.000 seguidores de Instagram desbloquean los reels de
prueba. No se le pone fecha: depende de qué formato funcione.

### Las dos primeras semanas, paso a paso

| # | Quién | Qué |
|---|---|---|
| 1 | Dueño | Contestar §11; como mínimo, los puntos 1, 4 y 5 |
| 2 | Sesión | Elegir los diez pueblos de prueba: uno de los dos más pequeños de España, tres de menos de 500 habitantes, tres de Los Pueblos Más Bonitos y tres que pida gente conocida |
| 3 | Dueño | Generarlos en la app y grabar la pantalla con la voz. Diez tours nuevos cuestan alrededor de un euro |
| 4 | Sesión | Comprobar cada narración, frase a frase, contra dos fuentes, y contar cuántas se sostienen. **Si se sostienen menos del 90 %, la idea se replantea antes de publicar nada.** El umbral es una suposición, y está en una línea para poder cambiarlo |
| 5 | Sesión | Montar los que pasen, con el molde de `piezas/historias-animadas/` |
| 6 | Dueño | Publicar lo del lanzamiento y el reel de Córdoba antes del sábado 10 |
| 7 | Dueño | Escribir a las 16 A y B de `INFLUENCERS.md` con el mensaje de su §7, ahora con la app en la tienda y un bono de regalo (§6) |
| 8 | Sesión | En cuanto la app tenga datos, los enlaces de campaña de la App Store, y un código de oferta por creador |

---

## 9. Cómo se mide, y cuándo se para

**La base de datos sigue siendo la tabla de resultados.** Lo que cambia es la fila: desde
que abra la tienda ya no se cuentan altas en la lista, sino descargas, compras y viajes.

**En el orgánico, por pieza**: visualizaciones, tiempo medio, **(guardados + envíos) por
cada mil cuentas alcanzadas**, seguidores ganados y, en la serie del pueblo, **peticiones
nuevas en los comentarios**, que es la señal de que el formato se está contagiando.

**En el negocio**:

- **Descargas por pieza y por creador**, con un enlace de campaña de la App Store por pilar
  y por creador (`ct=pueblo`, `ct=planes`, `ct=<creador>`).
- **Compras por código de oferta** de Apple, uno por creador (hasta diez a la vez).
- **Viajes con dos o más miembros**, que mide si el bucle del grupo funciona: una compra
  que trae a tres amigos son cuatro personas que ya han usado NOMAD, y tres de ellas no
  han costado nada.
- **Tours de pueblo generados**, y cuántas de esas cuentas compran después un viaje.

Parte de esto aún no se registra en la app (NOMAD#308 lo está montando); hasta que lo haga,
lo que no se pueda contar se dice, no se estima.

**La tabla de parada del orgánico** (los umbrales son una suposición, dicha aquí y en una
línea para poder cambiarla): **un formato se juzga a las seis piezas, no antes.** Sigue si
alguna de las seis supera **tres veces la mediana de visualizaciones de la cuenta**, o si sus
(guardados + envíos) pasan del **2 % del alcance**. Si no, se cambia el formato, no el texto.

**El dinero, sólo detrás de lo que ya ganó gratis**: se amplifica (Spark Ads en TikTok,
anuncio de colaboración en Instagram) una pieza que ya pasó la tabla de arriba, con tope y
bajo la tabla de parada de `AGENTS.md`. El umbral de coste por descarga se recalcula en
cuanto se sepa qué parte de las descargas compra, que hoy no se sabe.

---

## 10. Lo que cuesta

Tres niveles, de octubre a enero. **Lo que se paga a un creador compra una pieza que se
queda, no alcance.** Las cifras de creadores son estimaciones sobre su mediana de vistas y
las tablas de `CREADORES.md` (12-35 € por cada mil vistas, más un 15-30 % por los
derechos); **ninguna es un precio pedido**.

| | Mínimo | Recomendado | Ambicioso |
|---|---:|---:|---:|
| Herramientas (§7), cuatro meses | 80 € | 80 € | 80 € |
| IA de los pueblos, y del tour gratis si se decide (§3.5) | 50 € | 300 € | 300 € |
| La cantera, con canje (la IA de sus viajes) | 50 € | 50 € | 50 € |
| «La otra audioguía» | 300 €: el viaje, con alguien de la familia | 1.000 €: un micro que graba a su abuela, más un día de videógrafo | 5.000 €: @layayamaricarmen con derechos |
| La serie del pueblo, con creadores | 0 €: socios y canje | 300 €: dos nanos con tarifa pequeña | 2.300 €: además, @carloartspain |
| «Lo que planea NOMAD» | 0 € | 500 €: @ahora.vas.y.lo.vi | 3.000 €: además, @imartatravels |
| «Organizadores Anónimos» | 0 €: lo graba el dueño o un micro con canje | 1.200 €: @ramonteli, con 30 días de derechos | 5.200 €: además, @rikomedy |
| «La Amnistía» | 250 €: cinco premios | 500 €: diez | 500 € |
| Amplificar lo que ya ganó gratis (§9) | 0 € | 500 € | 2.000 € |
| **Total, hasta enero** | **unos 700 €** | **unos 4.400 €** | **unos 18.000 €** |

Con @teresalapelaya en lugar de @layayamaricarmen, el ambicioso sube entre 3.000 y
15.000 € más.

**Qué compra cada uno:**

- **Mínimo**: la idea entera probada, con el dinero de una cena. La pieza de Navidad
  depende de la familia.
- **Recomendado**: cuatro piezas con cara que se pueden anunciar, y la acción de enero
  completa.
- **Ambicioso**: caras conocidas en los dos momentos grandes. Sólo tiene sentido si antes
  se ha visto qué parte de las descargas compra.

**Se sube de nivel con datos, no con ganas.** El recomendado se desbloquea si la serie del
pueblo pasa la tabla de §9 en octubre-noviembre; el ambicioso, si el primer mes de tienda
dice cuánto vale una descarga. Hasta entonces, cada euro de más es una apuesta.

**Y lo que no está en la tabla, a propósito**: campañas de instalación en TikTok, que en
iOS exigen un medidor externo de instalaciones compatible con SKAdNetwork, un gasto y una
complejidad que no tocan todavía; y Apple Ads, que en España cuesta una mediana de 1,43 $
por instalación (AppTweak, 2025). Apple Ads es el primer canal de pago con sentido —quien
busca «audioguía» ya quiere una—, en cuanto se sepa qué parte de las descargas compra.

### El recomendado, por tramos (elegido el 30-sep)

El dueño se queda con el recomendado, *«aunque a lo mejor es mucho»*. Lo es si se gasta de
golpe, y por eso no se gasta de golpe: **4.400 € es el techo, no el objetivo.** Se abre en
tres tramos, y cada uno sólo si el anterior ha funcionado. Las escapadas de §3.6 van dentro:
salen de lo que la tabla de arriba reservaba para amplificar y para regalar audioguías, que
ahora va aparte.

| Tramo | Cuándo | Qué | Cuánto | Se abre si… |
|---|---|---|---|---|
| 1 | Octubre | Herramientas, la IA de las pruebas, la cantera por canje y tres escapadas grabadas por el dueño (unos 75 € cada una, entre gasolina y comida) | **325 €** | Ya |
| 2 | Noviembre-diciembre | Cuatro escapadas más, dos nanos de pueblo, @ahora.vas.y.lo.vi, «La otra audioguía», la IA de la serie y un empujón pequeño a la pieza de Navidad | **2.340 €** | Algún formato pasa la tabla de §9 **y** los diez pueblos se sostienen (§8) |
| 3 | Enero | @ramonteli para «Organizadores Anónimos», y «La Amnistía» | **1.720 €** | La Navidad trajo descargas y ya se sabe qué parte compra (NOMAD#308) |
| | | **Total** | **4.385 €** | |

**Lo que se arriesga de verdad hoy son 325 €.** Si el primer tramo no pasa, se para ahí y se
replantea. Si pasa el segundo y no el tercero, el gasto se queda en unos 2.665 €.

**Dos palancas para bajarlo sin tocar la idea:**

- «La otra audioguía» con alguien de la familia del dueño en vez de con un creador: 700 €
  menos.
- «La Amnistía» con cinco premios en vez de diez: 250 € menos.

Con las dos, unos 3.450 €.

**Y una que lo subiría**: si se regala la audioguía del pueblo (§3.5), hasta 200 € más de IA
en el segundo tramo. Sería buena noticia: querría decir que la está usando mucha gente.

---

## 11. Lo que decide el dueño

Diez preguntas en cuatro bloques. Están también en la issue, con sus casillas.

**La idea**

1. **«Tu pueblo, contado» como campaña principal hasta Reyes, y «Organizadores Anónimos»
   de enero a Semana Santa.** ¿Así, al revés o sólo una? Recomiendo ese orden: el pueblo
   abre la conversación con lo que nadie más puede enseñar, y el grupo es lo que se vende
   en primavera.
2. **El tono**: la voz de la app con un punto de guasa (§5). ¿Te encaja, o la quieres más
   seria o más gamberra?
3. **La bio de TikTok ya dice «Nosotros organizamos. Tú viajas.»** Es el cierre natural
   de «Organizadores Anónimos». ¿Se queda?

**El dinero**

4. **El nivel de gasto hasta enero** (§10): mínimo, recomendado o ambicioso. *Decidido el
   30-sep: el recomendado, con 4.400 € de techo y por tramos.*
5. **La audioguía del pueblo gratis durante la campaña** (§3.5). Si es que sí, hace falta
   una issue en el repo de la app antes de noviembre.

**Tú**

6. **¿Sales en cámara?** No hace falta: el fundador de Vicio no sale nunca. Pero «una app
   de viajes hecha por una sola persona» es una historia que compra la prensa, y basta con
   la voz, sin la cara.
7. **La pieza de Navidad, ¿con un creador y su abuela, o con alguien de tu familia que
   tenga pueblo?** Lo segundo es más barato y más verdad; lo primero trae público.

**Lo demás**

8. **La lista de espera, ¿se cierra de verdad el día que abra iOS?** Para Android sigue
   abierta hasta que salga (NOMAD#305). De esto depende que se publique «¿Qué pasa el día
   que abra NOMAD?» (`piezas/lanzamiento/`), que lo promete.
9. **Italia**: ¿«Il tuo paese, raccontato» con las tres A italianas de `INFLUENCERS.md` en
   diciembre, o se aparca? La nonna funciona igual que la abuela.
10. **La escapada al pueblo (§3.6)**: ¿la grabas tú o un creador, desde qué ciudad se sale
    —para buscar pueblos a menos de dos horas— y con qué gancho?

---

## Fuentes

Consultadas entre el 30-sep-2026 y las fechas que dice cada una. Lo que venía de una sola
fuente débil no ha entrado en el documento.

**Datos propios**: `public.waitlist` y `tours_cache`, consultadas el 30-sep-2026;
`campana/BRIEF-REFORMULACION.md`; `piezas/demo-app/GUION.md`; `docs/ECONOMIA.md` y las
issues #303, #305 y #308 del repo de la app.

**Vicio**: [CESTE](https://www.ceste.es/areas-de-negocio/empresas/caso-exito-vicio/) ·
[Dircomfidencial, mar-2025](https://dircomfidencial.com/marketing/vicio-nos-convertiremos-en-un-icono-o-venderemos-en-el-intento-20250325-0404/) ·
[Marketing News, 2022](https://www.marketingnews.es/marcas/noticia/1168004054305/aleix-puig-marca-vicio-mas-grande-mi-pasado-ganador-de-masterchef.1.html) ·
[c de c](https://www.marketingdirecto.com/especiales/c-de-c-club-creatividad/vicio-claves-exito-creativo-c-de-c) ·
[la convención de McDonald's](https://www.marketingnews.es/marcas/noticia/1183245054305/asi-sido-la-repercusion-de-la-accion-gamberra-de-vicio-en-la-convencion-de-mcdonalds.1.html) ·
[La Velada IV](https://www.kolsquare.com/es/blog/analisis-de-la-velada-del-ano-4-influencers-estrategias-de-marketing-y-el-secreto-del-exito) ·
[A Coruña](https://www.merca20.com/vicio-campana-publicidad-apertura-a-coruna/) ·
[«Perdona Ferran»](https://ipmark.com/vicio-ficha-ferran-torres-demostrar-burgers-mandan/) ·
[FACUA y Milfshakes](https://www.ondavasca.com/el-youtuber-nil-ojeda-denunciado-por-facua-tras-ofrecer-un-99-de-descuento-si-espana-ganaba-el-mundial/)

**Estrella Damm y otras marcas**: [todos los «Mediterráneamente»](https://www.reasonwhy.es/actualidad/campanas/todos-los-spots-de-estrella-damm-mediterraneamente) ·
[c de c, 2026](https://www.reasonwhy.es/actualidad/club-de-creatividad-recupera-mediterraneamente-estrella-damm-2026) ·
[*La leyenda de Canyut*](https://www.eldebate.com/economia/20260611/estrella-damm-decreta-comienzo-verano-campana-leyenda-canyut_427825.html) ·
[Marina Prieto](https://www.storyboard18.com/advertising/global-ads-spotlight-when-marina-prieto-revived-the-future-of-spains-subway-advertising-68272.htm) ·
[anuncios edadistas](https://www.65ymas.com/economia/empresas/10-anuncios-mas-edadistas-ultimos-anos-abuelo-satisfyer-fabada-litoral_80478_102.html) ·
[CampofrIA](https://www.reasonwhy.es/actualidad/anuncio-navidad-campofrio-2023-inteligencia-artificial) ·
[Coca-Cola](https://www.genbeta.com/actualidad/coca-cola-ha-lanzado-tres-anuncios-ia-para-anunciar-navidad-que-no-queda-claro-queria-arruinar) ·
[McDonald's Países Bajos](https://www.reasonwhy.es/actualidad/mcdonalds-paises-bajos-retira-anuncio-navidad-inteligencia-artificial) ·
[Kantar sobre la IA en publicidad](https://www.elespanol.com/omicrono/tecnologia/20260201/publicidad-abraza-ia-hacer-campanas-imparable-gente-no-quiere-anuncios-cutres/1003744105164_0.html) ·
[Duolingo en TikTok](https://digiday.com/marketing/how-duolingo-is-using-its-unhinged-content-with-duo-the-owl-to-make-people-laugh-on-tiktok/)

**Plataformas y medición**: [el algoritmo de Instagram](https://blog.hootsuite.com/instagram-algorithm/) ·
[reels de prueba](https://www.socialsamosa.com/news-2/instagram-introduces-wider-access-trial-reels-9493132) ·
[Metricool, Instagram 2026](https://metricool.com/es/estudio-instagram/) ·
[Buffer, frecuencia en TikTok](https://buffer.com/resources/how-often-should-you-post-on-tiktok/) ·
[Socialinsider, duración](https://www.socialinsider.io/blog/how-long-are-tiktok-videos/) ·
[StatCounter, España](https://gs.statcounter.com/os-market-share/mobile/spain) ·
[IAB Spain 2026](https://ppc.land/spains-social-media-users-jump-to-7-2-platforms-but-42-quit-at-least-one/) ·
[Harris Poll y 4As](https://www.marketingbrew.com/stories/harris-poll-ai-fatigue-less-trust-ai-generated-ads-cannes-lions) ·
[Apple Ads, AppTweak](https://www.apptweak.com/en/aso-blog/apple-ads-benchmarks) ·
[enlaces de campaña](https://developer.apple.com/help/app-store-connect-analytics/acquisition/campaign-links) ·
[códigos de oferta](https://developer.apple.com/documentation/storekit/supporting-offer-codes-in-your-app)

**Herramientas**: [Google AI Plus en España](https://www.profesionalreview.com/2026/06/09/google-rebaja-ai-plus-a-499-euros-al-mes-en-espana-con-400-gb/) ·
[Edits](https://techcrunch.com/2026/06/11/metas-edits-app-is-getting-an-ai-assistant-and-a-desktop-version/) ·
[los términos de CapCut](https://www.techloy.com/capcuts-latest-terms-of-service-raises-big-questions-about-content-ownership/) ·
[Suno](https://suno.com/blog/suno-updates-tos) ·
[GEMA contra Suno](https://www.justiz.bayern.de/gerichte-und-behoerden/landgericht/muenchen-1/presse/2026/16.php) ·
[el cierre de Sora](https://the-decoder.com/openai-sets-two-stage-sora-shutdown-with-app-closing-april-2026-and-api-following-in-september/)

**Normativa**: [art. 50 del Reglamento de IA](https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act) ·
[lo que entró el 2-ago-2026](https://www.morganlewis.com/blogs/sourcingatmorganlewis/2026/08/eu-ai-acts-transparency-rules-what-went-into-effect-on-2-august) ·
[etiquetas de Meta](https://transparency.meta.com/governance/tracking-impact/labeling-ai-content) ·
[etiquetas de TikTok](https://newsroom.tiktok.com/more-ways-to-spot-shape-and-understand-ai-content?lang=en) ·
[el proyecto de ley español](https://www.xataka.com/legislacion-y-derechos/espana-aprueba-su-ley-ia-deepfakes-sexuales-fuera-etiqueta-ia-obligatoria-multas-millonarias-al-sector-privado) ·
[código de influencers, 2.ª versión](https://www.autocontrol.es/app/uploads/codigo-de-conducta-de-publicidad-a-traves-de-influencers-2025.pdf) ·
[CNMC, jun-2026](https://www.cnmc.es/prensa/requerimientos-influencer-20260603) ·
[RD 444/2024](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2024-8716) ·
[Ley 13/2011 del juego](https://www.boe.es/buscar/act.php?id=BOE-A-2011-9280) ·
[Reglamento del IRPF](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820) ·
[promociones en Meta](https://www.facebook.com/policies_center/pages_groups_events/) ·
[LO 1/1982](https://www.boe.es/buscar/act.php?id=BOE-A-1982-11196) ·
[Thyssen](https://www.museothyssen.org/sites/default/files/document/2025-04/FolletoThyssen_ES-19.pdf) ·
[Reina Sofía](https://www.museoreinasofia.es/visita/visita-individual/) ·
[festivos de 2026](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2025-21667)

**Pueblos**: [INE, cifras a 1-ene-2025](https://www.ine.es/jaxiT3/Tabla.htm?t=2872) ·
[Los Pueblos Más Bonitos, para creadores](https://lospueblosmasbonitosdeespana.org/para-creadores) ·
[su día, el 1 de octubre](https://lospueblosmasbonitosdeespana.org/eventos/el-1-de-octubre-ven-a-un-pueblo) ·
[izi.TRAVEL](https://izi.travel/es) · [VoiceMap](https://voicemap.me/) · [Audiala](https://audiala.com/)
