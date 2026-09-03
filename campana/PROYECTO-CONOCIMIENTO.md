# Conocimiento del Proyecto «NOMAD · marketing»

Generado desde el repo `nomad-marketing` por `campana/generar-conocimiento.sh` (`campana/PROYECTO-CLAUDE.md` dice qué es y cuándo se sube). Seis documentos, uno detrás de otro. **El repo manda; esto es una copia: se regenera, no se edita.**


---

<!-- AGENTS.md -->

# nomad-marketing

Todo lo de NOMAD que **se publica en redes, se gasta en Meta o se mide en la lista de
espera**. Lo que se despliega o se somete a una tienda es código y vive en
`marcgodinezmartinez-gif/NOMAD` (la app, las funciones, la web con su formulario de
lista, los legales, la ficha de la tienda). Esa frase es la frontera; se separó el 1 de
septiembre de 2026 porque los tres trabajos —código, fabricar piezas, llevar la campaña—
vivían en la misma sesión y cada uno pagaba las reglas del otro.

```
campana/         los planes y sus decisiones: PLAN-INSTAGRAM, INSTAGRAM-ARRANQUE,
                 LANZAMIENTO-PUBLICIDAD, MERCADO. Son el porqué; se leen antes de opinar
piezas/          los generadores (reels, destacadas, el taller), preparar.sh, construir-todo.sh
banco/           el kit: fotos con sus créditos, capturas reales, marca, fuentes, iconos, QR
.claude/skills/  siete skills de marketing (Corey Haines, MIT); su README dice por qué siete
salida/          lo generado. No se versiona: se rehace en un minuto
```

**Lo pendiente vive en las GitHub issues de ESTE repo** (regla del dueño, 1-sep: «GitHub
Issues debe ser la biblia de lo que queda pendiente»). Las tres últimas de marketing
quedaron en el repo de la app —#68 subir destacadas y reels, #69 la tabla de parada,
#70 esta separación— y se cierran allí; las nuevas se abren aquí.

## Los números que gobiernan las decisiones

Calculados de costes reales en `campana/LANZAMIENTO-PUBLICIDAD.md`; no se discuten en
cada sesión, se aplican:

- **Un alta vale 0,24 €** (margen esperado de un miembro de la lista).
- **Coste objetivo por alta (TCPL): 0,25 €.** Un alta pagada en Meta en España cuesta
  0,30-1,50 €, así que **lo pagado compra aprendizaje** (qué argumento mueve), no altas.
- **Precio**: 2,99 € el viaje entero, sin suscripción; en la lista, el primero por 1,99 €.
  Siempre en ese orden. El ancla del precio es **el café**, nunca «la audioguía de 6 €»:
  el dueño la ha tirado dos veces y no vuelve por ninguna puerta.

**La tabla de parada** (aritmética, no corazonadas):

| Situación | Qué hacer |
|---|---|
| Un anuncio ha gastado < 0,75 € (3× TCPL) | Esperar. No hay señal todavía |
| Cero altas con ≥ 0,75 € gastados | Matar el CONCEPTO, no iterarlo con otro texto |
| **Hay clics y no hay altas** (< ~3 % de los clics se apuntan) | **No matar todavía**: el fallo está DESPUÉS del clic. Comparar «visitas a la página de destino» con «clics en el enlace» antes de tocar el anuncio |
| Coste por alta ≤ 0,25 € | Candidato a ganador |
| Entre 0,25 y 0,38 € | Vigilar: varianza normal |
| > 0,38 € (1,5× TCPL) | Cambiarlo: fallo estructural |
| Meta apenas le da gasto | Matar ya: el no-reparto ES el veredicto |

Y dos reglas que se salta todo el mundo: al iterar un anuncio muerto por falta de reparto
se cambia el gancho o el visual, **nunca el texto** (nadie llegó a leerlo); y **nunca se
pausa sin reemplazo listo**.

La fila de «hay clics y no hay altas» la pagó la campaña el 2-sep: 20 000 de alcance, 677
clics (3,4 % de CTR, bueno para tráfico frío) y **1 alta** — 0,15 %. La fila de «cero
altas» habría matado el creativo, que era la única parte que funcionaba. El porqué y el
diagnóstico de la portada, en `campana/LANZAMIENTO-PUBLICIDAD.md`.

## Medir antes de opinar

La única tabla de resultados es la base de datos, no lo que Meta se atribuya. Sin píxel,
a propósito. Dos consultas, cada día:

```sql
SELECT coalesce(source, '(directo)') AS origen, count(*) AS altas,
       min(created_at)::date AS primera, max(created_at)::date AS ultima
FROM public.waitlist GROUP BY 1 ORDER BY 2 DESC;

SELECT coalesce(lang, '(sin lang)') AS idioma, coalesce(source, '(directo)') AS origen, count(*)
FROM public.waitlist GROUP BY 1, 2 ORDER BY 3 DESC;
```

Se ejecutan contra el endpoint de consulta de la API de gestión de Supabase con el token
de gestión en la variable `SUPABASE_TOKEN_GESTION` (**nunca se imprime, nunca va a un
fichero del repo**). No existe todavía un rol de sólo lectura de Postgres; el día que
exista, la consulta diaria puede ser una Rutina programada. **El gasto de Meta no se
lee desde una sesión**: no hay conector, se mira en Business Suite y se anota en la
issue de la campaña.

Los orígenes que aparecen: `instagram/referral` (la bio), `meta/paid/lista-a|b|c|e` (los
cuatro anuncios), `invitacion` (/join), `recomendacion` (/r), y lo que lleve UTM propio.
**Lo que decía el 1-sep**: 8 altas, todas del 31-ago, todas `lang = es` — 4 `ig/social`,
3 `invitacion`, 1 `meta/paid/lista-a`; `lista-b`, `-c` y `-e` a cero.

## Instagram: cómo se publica aquí

- La cuenta es **@app.nomad**, empresa. Bio y enlace en `campana/INSTAGRAM-ARRANQUE.md`;
  el enlace es `travelsnomad.com` a secas (decisión del dueño): la portada atribuye por
  referrer y **redirige por idioma conservando el UTM**, así que un italiano cae en `/it/`.
- **El grid se sube al revés (9 → 1)**; **las destacadas, en orden (1 → 7)**. Las once
  tarjetas de una destacada se suben primero como historias, así que son el contenido del
  día.
- **Los reels salen sin pista de audio**, a propósito: se elige dentro de Instagram, de
  tendencias, que es lo que el algoritmo premia. Un reel que parece un anuncio se salta:
  primera persona, alguien enseñando lo que ha probado.
- **Zonas seguras**: en una historia la interfaz tapa ~250 px arriba y abajo — el texto
  vive entre y=280 e y=1500 y de 1520 para abajo va el adhesivo de enlace. En un reel,
  entre 230 y 1480.
- **UTM de cada adhesivo**: `utm_source=instagram&utm_medium=organic&utm_campaign=<pieza>`,
  con `-it` al final si es italiano, y entonces el enlace apunta a `travelsnomad.com/it/`
  directamente, no a la raíz.
- **Idiomas**: español es el mercado; el italiano es una prueba con UTM propio (la mitad de
  los seguidores lo son, y ninguno se ha apuntado); francés e inglés no tienen ni una señal
  y no se doblan. La regla superficie por superficie está en `piezas/destacadas/README.md`.
- **No se compran seguidores. Nunca.**

## Las piezas y cómo se fabrican

```bash
npm install                        # ffmpeg-static, una vez
bash piezas/construir-todo.sh      # prepara salida/, escribe todas las piezas y el taller
cd salida && node ../piezas/reels/exportar-reel.mjs && bash ../piezas/reels/montar-reel.sh
```

Los generadores leen de su directorio de trabajo (`Main.dc.html` con las fuentes,
`fotos/`, `plan-900.webp`, `mark.png`…) y no saben de este repo a propósito;
`piezas/preparar.sh` monta `salida/` con eso desde `banco/`. Hasta el 1-sep todo eso vivía
en el scratchpad de una sesión y moría con ella: **el banco existe para que no vuelva a
pasar**.

**El taller** (<https://claude.ai/code/artifact/0fea041b-1676-4675-94ab-fc326d44bdb3>) es
el lienzo editable con el kit, siete plantillas y todas las piezas. **Quién manda**:
mientras el dueño no toque el lienzo, manda el generador —se rehace la pieza, se
reconstruye y se vuelve a guardar—; en cuanto edite algo en el lienzo, manda el lienzo:
antes de sembrar hay que leerlo y construir sobre lo que haya, o su edición se pierde sin
aviso. `piezas/taller/README.md` tiene el detalle.

**Fotos: sólo CC0 o dominio público**, de Wikimedia Commons, verificadas foto a foto. No
se debe atribución y no hay marca de agua, pero el crédito queda en
`banco/fotos/creditos.json` para poder demostrar la procedencia. Una foto nueva entra con
su título de Commons y su licencia en ese fichero, y en los dos tamaños: `post/`
(1080×1350) e `historia/` (1080×1920), recortada del original, no de la otra.

**Capturas: de la app real**, nunca maquetas. Están en `banco/capturas/` por pantalla e
idioma (`plan-900.webp`, `plan-900-it.webp`…). Si la app cambia una pantalla, se vuelven
a capturar; una captura vieja en un anuncio es una promesa que la app no cumple.

## Trampas ya pagadas

- **`zoompan` genera `d` frames POR CADA FRAME DE ENTRADA.** Con `-loop 1 -t 3` el primer
  reel salió de 5 minutos y 35 segundos. La entrada es UNA imagen suelta. Y el
  pre-escalado ×2 antes del `zoompan` es lo que quita el temblor.
- **El HELMET no trae emoji en color**: una carátula con 🎟 salió en blanco y negro. A 60
  px de diámetro sólo se lee una forma; las carátulas llevan la marca y se distinguen por
  el fondo. En el texto, un emoji como mucho y sólo para señalar (👇 👉), como en la bio.
- **Un velo global no basta sobre neón ni piedra labrada**, y subirlo entero deja la foto
  marrón. Va una banda oscura detrás del bloque de texto (`scrim`).
- **En el lienzo, la foto elegible por chip es una rama `<sc-if>` por foto, cada una con
  su `src` literal**: el lienzo sustituye texto literal por la imagen, no valores. Un
  `src="{{foto}}"` sale roto y sin aviso.
- **Tres postales salieron de recortes de 980×380** ampliados cinco veces en una historia.
  Las fotos de historia se recortan del original, y por eso el banco tiene los dos tamaños.
- **De Commons, lo que devuelve 429 es SÓLO la API vieja** (`w/api.php`) — corregido el
  2-sep, porque antes ponía que fallaban las descargas y no es verdad. El servidor de
  ficheros (`upload.wikimedia.org`) baja originales de 26 MB sin rechistar y la API REST
  (`w/rest.php`) responde. **Sí se pueden traer fotos nuevas desde aquí**:
  `python3 piezas/fotos/ampliar-banco.py`.
- **El fondo CC0 de Openverse está lleno de digitalizaciones de museo**, y casan con
  cualquier búsqueda de texto. De 13 que bajó la primera pasada, 5 eran basura: «toledo»
  trajo un manuscrito medieval, «nápoles» una estatua, «venecia» el Venice Canal District
  **de California**. **Las fotos nuevas se miran una a una antes de darlas por buenas** —
  el título no basta, y el guion no puede decidirlo por ti.
- **Un `grep` encuentra la cadena también en los comentarios.** Se sonda el endpoint, no
  el fichero que lo llama. Y **una aserción se rompe a propósito antes de fiarse de ella**.

## Al trabajar

- **Commit por pieza y push según se va.** El contenedor se recicla y lo no empujado muere.
- **Nunca `git checkout -- .`, `git restore <fichero>` ni `reset --hard`** como limpieza.
- **Ningún identificador de modelo** en commits ni en ficheros.
- Los tokens (Supabase, Expo) **no se imprimen** y no entran en el repo.
- Al terminar un trabajo la issue se cierra o se comenta con su estado real; al encontrar
  algo pendiente se abre una **antes** de que se pierda en un fichero.


---

<!-- campana/LANZAMIENTO-PUBLICIDAD.md -->

# Publicidad de lanzamiento — plan de trabajo

Escrito el 23 de agosto de 2026, sobre el análisis de mercado del 15-ago (los precios de
competidores citados ahí están verificados contra fuentes públicas; aquí no se inventa
ninguno). La maquinaria de medición ya existe: cada enlace lleva `utm_*`, la web lo
captura y cae en `waitlist.source` — **cada euro se puede atribuir desde el día uno.**

> **Revisado el 24 de agosto.** Se le han añadido las tres cosas que le faltaban para ser
> un plan y no una lista de ideas: **una fecha**, **un número al que apuntar** y **un
> criterio para parar**. Los tres salen de números medidos —el panel ya existe— y no de
> estimaciones.
>
> Y ha cambiado algo de fondo desde el 23-ago: **la oferta de 1,99 € es sólo para quien
> esté en la lista.** Eso no es un matiz de copy, es el gancho entero. Antes te apuntabas
> para *enterarte*; ahora te apuntas para que te *dejen* comprarlo a ese precio. Todos los
> copys de abajo lo dicen ya así.

---

## Lo primero: cuánto vale un alta, porque decide todo lo demás

Antes de elegir canal o presupuesto hay que saber qué se puede pagar por un alta. Sale de
los costes reales de `admin_function_economics` y de los precios decididos:

| | |
|---|---:|
| Neto de un primer viaje a 1,99 € (IVA + 15 % de tienda) | 1,40 € |
| Coste de IA de ese viaje (4-7 días, destino nuevo, tarifa de **enero**) | −1,19 € |
| **Margen del primer viaje** | **0,21 €** |
| Margen de un segundo viaje a 4,99 € | 2,32 € |

**Dos supuestos, dichos aquí y no enterrados** — cámbialos cuando haya datos y todo lo de
abajo se recalcula: **30 %** de la lista compra el primer viaje, y **1 de cada 4** de esos
compra un segundo.

> ### Un alta vale **0,24 €**
> Y un alta pagada en Meta cuesta en España entre **0,30 € y 1,50 €**.

**Conclusión, y es la que reordena el plan: a los precios de hoy, comprar altas no se paga
solo.** Ni en el mejor caso del rango.

| % que compra el 1º ↓ · viajes adicionales por comprador → | 0,25 | 0,5 | 1,0 | 1,5 | 2,0 |
|---|---:|---:|---:|---:|---:|
| 15 % | 0,12 € | 0,20 € | 0,38 € | 0,55 € | 0,73 € |
| **30 %** | **0,24 €** | 0,41 € | 0,76 € | 1,10 € | 1,45 € |
| 50 % | 0,39 € | 0,68 € | 1,26 € | 1,84 € | 2,42 € |
| 70 % | 0,55 € | 0,96 € | 1,77 € | 2,58 € | 3,39 € |

Sale a cuenta sólo abajo a la derecha: **mucha conversión Y mucha repetición**. Y ahí está
la palanca de verdad — **no es el CPL, es que la gente repita**. Duplicar la repetición
mueve más que cualquier optimización de anuncio.

**Lo que eso cambia en este plan:**

1. **El orgánico no es la fase barata previa al dinero de verdad: es el canal.** Un vídeo
   que funciona trae altas a coste cero y no tiene techo.
2. **El presupuesto pagado de septiembre es de APRENDIZAJE, con techo fijo.** No se compra
   volumen: se compra saber qué creatividad funciona antes de pagar por instalaciones en
   octubre, que es donde el dinero sí puede tener sentido.
3. **La métrica de septiembre no es sólo el número de altas: es el coste por alta por
   canal**, para llegar a octubre sabiendo cuál escalar.

### Cuántas altas hacen falta

| Ventas el primer mes | Altas necesarias |
|---:|---:|
| 50 | 167 |
| **100** | **333** |
| 200 | 667 |

**El objetivo de septiembre: 350 altas.** Es el número que hace que octubre signifique
algo, y es alcanzable con orgánico si un vídeo de cada cinco funciona.

---

## El enfoque, en dos fases

**Fase 1 — AHORA (la app no está en la tienda): todo apunta a la lista de espera.**
El gancho es la oferta ya prometida en la portada: *apúntate y estrena por 1,99 €* (el
sellado de elegibilidad está vivo desde el 23-ago). Objetivo: llenar `waitlist` (hoy: 0)
y descubrir qué creatividad funciona ANTES de pagar por instalaciones.

**Fase 2 — LANZAMIENTO: las creatividades ganadoras pasan a campaña de instalación** +
Apple Search Ads (intención altísima y barata en español: «audioguía», «free tour»,
«guía de viaje» — las categorías donde el precio de NOMAD sorprende, según MERCADO §3).

## Canales — y por qué estos

| Canal | Papel | Por qué |
|---|---|---|
| **TikTok + Instagram Reels** | Principal (orgánico primero, pagado después) | El mismo vídeo vertical sirve a ambos; el público de citybreaks y museos vive ahí; el producto tiene un momento MUY grabable (abajo) |
| YouTube Shorts | Gratis de regalo | El mismo fichero, tercera plataforma, cero esfuerzo extra |
| **Facebook** | Solo como ubicación dentro de Meta Ads | No montar presencia propia: llega sola con Advantage+ y el público viajero mayor de 40 está ahí. Cero esfuerzo dedicado |
| **Apple Search Ads** | Fase 2, desde el día en tienda | Búsqueda con intención: quien teclea «audioguía Prado» ya quiere pagar por una |

**Medición sin píxel, a propósito.** La web es estática, sin banner de cookies, y así se
queda: nada de píxel de Meta por ahora — mediríamos mejor las campañas pero heredaríamos
consentimiento GDPR en una web que hoy no lo necesita. La atribución sale de
`waitlist.source` (consulta al pie). Si algún día el volumen justifica optimización por
conversión, se revisita CON banner.

## El mensaje (de MERCADO, no de la inspiración)

1. **El ancla de precio**: «La audioguía que otras apps venden a 5-15 € LA UNIDAD, aquí
   va incluida en un viaje entero de 2,99 €.» Verificado: VoiceMap 5-15 $/tour, WeGoTrip
   5-15 €/atracción.
2. **La cola larga**: «Funciona en cualquier pueblo y cualquier museo del mundo — no solo
   en las seis ciudades de siempre.» (El clúster GuideMapp cubre ~6 ciudades curadas;
   NOMAD genera Santa Marinella y un tour de heladerías.)
3. **El combo**: planificar + guiar + museo obra a obra + gastos de grupo. Nadie junta
   las cuatro piezas (MERCADO §«nadie más»).

## Los guiones (15-30 s, gancho en el primer segundo, subtítulos SIEMPRE)

Grabación: un iPhone basta. ⚠️ **En museos, consulta la norma antes de grabar** — el
Prado prohíbe fotografiar; Thyssen y muchos otros permiten sin flash. Elige un museo que
lo permita o graba la pantalla del teléfono fuera de sala.

**G1 · El museo (el killer — hazlo primero)**
POV: mano con el teléfono delante de un cuadro. Suena la narración real 3-4 s.
Texto en pantalla: «La audioguía oficial: 5-8 €. Esta: funciona en CUALQUIER museo.»
Cierre: la app mostrando la obra con su foto y la silueta a escala. CTA: «Lista de
espera en travelsnomad.com — estrenas por 1,99 €».

**G2 · Planificar en 30 segundos**
Screen recording: el asistente generando 4 días de Roma — presupuesto, a pie, con niños.
Texto: «Esto antes eran 3 horas de pestañas abiertas.» Se enseña el resultado real:
itinerario día a día con mapa. CTA igual.

**G3 · El paseo**
Andando por una calle bonita con auriculares. Se oye: «Dónde ponerte: …» / «Un dato
curioso: …» (la narración real del tour). Texto: «Un free tour que empieza cuando tú
quieras, en tu idioma.»

**G4 · La comparación desnuda**
Pantalla partida o tarjetas: «Un (1) tour de VoiceMap: 5-15 $ · Un VIAJE ENTERO de
NOMAD con tours y museos ilimitados: 2,99 €». Sin más. Este es para pagado: simple,
legible sin sonido.

**G5 · El pueblo que no sale en las guías**
«¿Tu app de viajes conoce Santa Marinella? La mía sí.» Enseñar el tour generado de un
pueblo pequeño real. Ataca directo el foso contra lo curado.

**G6 · El tour absurdo-encantador**
«Le pedí un tour de heladerías por Roma. Me lo hizo.» Humor + demostración de que el
tema lo eliges tú. Es el formato con más papeletas de compartirse.

**G7 · El modo avión**
Teléfono en modo avión, la audioguía descargada sonando. «Sin cobertura, sin roaming,
sin excusas.» (Grabar con la PRÓXIMA build, no con la 27 — el botón de descarga ya
existe pero el arreglo de honestidad viaja en la siguiente.)

**G8 · Los gastos del grupo**
«El viaje acabó. Nadie sabe quién debe qué. Esta app sí.» Secundario, para variar el
feed; no lleva presupuesto de pago.

## Copys para Meta Ads (fase 1, objetivo = tráfico a la lista)

*Reescritos el 24-ago con el gancho nuevo, y pulidos el 30-ago al montar la campaña real
(pedido del dueño: «hay que pulirlos»). Lo que cambió en la pulida: el golpe completo va
en la PRIMERA línea, porque el feed corta a ~125 caracteres con un «ver más»; los precios
siempre en el mismo orden (2,99 normal → 1,99 de lista); y el cierre reutiliza «Apúntate y
no te pierdas el lanzamiento», que ya es la voz de la bio y de la web. **La oferta de
1,99 € es sólo para quien esté en la lista**, y eso cambia el verbo: no te apuntas para
enterarte, te apuntas para que te dejen comprarlo a ese precio. Los saltos de línea van
A PROPÓSITO: se pegan tal cual, en tres párrafos.*

- **A (precio)** · Título: `Tu primer viaje, por 1,99 €`
  > El viaje entero, por lo que cuesta un café: desde 2,99 €.
  >
  > Los días escritos, los tours a pie contados al oído y las guías de museo — todo
  > incluido, sin suscripción. Y en la lista de espera, tu primer viaje por 1,99 €.
  >
  > Apúntate antes del lanzamiento y no te pierdas nada.

  (La comparación con la audioguía suelta de 6 € murió el 30-ago, y es la SEGUNDA vez
  que el dueño la tira — la primera fue el titular de la banda del precio de la web.
  Que no vuelva por ninguna puerta: el ancla del precio es el café, que además es
  literalmente lo que dice la imagen del anuncio. Sin ponerle precio al café, a
  propósito: un número concreto invita al comentario de «un café no cuesta eso».)
- **B (cola larga)** · Título: `Te guía por cualquier sitio`
  > Tu próximo viaje no tiene por qué ser a las seis ciudades de siempre.
  >
  > NOMAD te escribe el itinerario y te guía con voz por CUALQUIER sitio — hasta por el
  > pueblo de tu abuela. Llega en octubre, y los de la lista estrenan su primer viaje por
  > 1,99 €.
  >
  > Apúntate y no te pierdas el lanzamiento.
- **C (combo)** · Título: `Los días escritos. La ciudad, contada`
  > Te escribe los días. Te los cuenta al oído mientras andas la ciudad. Te dice qué
  > estás mirando en el museo. Y reparte los gastos del grupo.
  >
  > Todo por 2,99 € el viaje entero, sin suscripción — y en la lista, el primero por
  > 1,99 €.
  >
  > Apúntate antes del lanzamiento de octubre.
- **D (urgencia, para la semana 4):** «La lista se cierra cuando abramos. Después, el
  primer viaje cuesta lo que cuesta. Antes, 1,99 €.» (Sin pulir: se pule cuando le toque
  correr, con lo aprendido de los otros cuatro.)
- **E (grupo, añadido el 29-ago)** · Título: `Los gastos se reparten solos`
  > En todos los grupos hay uno que acaba organizándolo todo. Si eres tú, esto es para ti.
  >
  > NOMAD escribe el viaje, tus amigos se unen con un QR y los gastos se reparten solos.
  > 2,99 € por viaje, sin suscripción — en la lista, el primero por 1,99 €.
  >
  > Apúntate y no te pierdas el lanzamiento.

  Su enlace: `utm_campaign=lista-e`. En el arranque corren A/B/C/E y la D queda en
  reserva para la semana del cierre — quemar la urgencia el día 1 es gastar el cartucho
  cuando menos verdad tiene.
- **F (la IA, en reserva para el viernes 4-sep)** · Título: `La IA que te escribe el viaje`
  > Le dices a dónde vas y qué te gusta. La IA te escribe el viaje entero: qué ver, en
  > qué orden y cuánto cuesta.
  >
  > ¿Cambio de planes? Se lo pides y lo reescribe. Y por la calle te lo cuenta al oído.
  > Desde 2,99 € el viaje — en la lista, el primero por 1,99 €.
  >
  > Apúntate antes del lanzamiento y no te pierdas nada.

  Su enlace: `utm_campaign=lista-f`. Nace de la observación del dueño (31-ago): «no
  hemos hecho énfasis en el asistente IA en la publi» — y es verdad medible: la palabra
  IA no está en ninguno de los cuatro vivos. El porqué de meterla AHORA como quinto
  ángulo y no antes: «IA» en el feed de 2026 es papel pintado si es el argumento entero,
  pero como PALABRA-GANCHO abre el bolsillo de audiencia de los curiosos de herramientas
  IA, que los otros cuatro ángulos no tocan — el «one-keyword hack» de la doctrina
  Andromeda: la creatividad ES la segmentación. Entra el viernes con el veredicto (se
  mata el copy más flojo y entra éste), con LA MISMA imagen del Tertre que los demás,
  para que la variable siga siendo el argumento. Si la F gana, la segunda iteración es
  su creatividad propia: el teléfono con el paso del asistente («Indicaciones para la
  IA» + «Generar viaje») a la vista.

**Los cuatro son para PROBAR, no para elegir el que más te guste.** A ataca por precio, B
por cobertura, C por producto y D por urgencia — y son ángulos distintos a propósito,
porque lo que se está midiendo es cuál de las cuatro razones mueve a la gente. Con la
misma imagen en los cuatro, para que la diferencia sea el argumento y no la foto.

## TikTok: por qué NO se paga todavía (decidido el 31-ago)

Pregunta del dueño esa noche: «¿montamos una campaña igual en TikTok y vemos si funciona
por ahí también?». La tabla de arriba ya decía «orgánico primero, pagado después», y con
la campaña de Meta corriendo hay cuatro razones que lo hacen MÁS cierto, no menos:

1. **Partir 7 €/día en dos no son dos pruebas: son cero.** La regla de esta casa es no
   juzgar nada antes de 0,75 € gastados por anuncio, y con cuatro anuncios vivos el
   presupuesto ya va justo. Dividirlo deja las dos plataformas por debajo del umbral
   donde un número significa algo.
2. **La creatividad que corre en Meta moriría en TikTok.** Ahí la foto fija con texto
   encima se lee como publicidad a un kilómetro, y el algoritmo penaliza lo que no es
   nativo. Lo que funciona es cara, voz y movimiento — o una grabación de pantalla con
   un desenlace.
3. **Aún no sabemos qué mensaje funciona.** El veredicto de Meta es el viernes. Llevar un
   mensaje sin validar a una segunda plataforma multiplica las incógnitas en vez de
   reducirlas: si sale mal, no se sabrá si fue el canal o el argumento.
4. **La prueba mínima honesta en TikTok es más cara**, no más barata: el sistema necesita
   más volumen para salir de aprendizaje. Del orden de 20 €/día durante una semana
   (~140 €) para concluir algo. La mitad de 7 € no es una prueba, es ruido.

**Lo que sí se hace ya, y es gratis:** TikTok es la última plataforma donde una cuenta de
cero seguidores todavía alcanza público sin pagar. Los dos Reels del 31-ago
(`piezas/reels/`) sirven TAL CUAL — son 9:16, sin marca de agua de Instagram. Ahí está la
prueba real y sin coste de si el mensaje viaja en TikTok.

**La condición para abrir el grifo**, escrita para no discutirla en caliente: se paga en
TikTok cuando (a) el veredicto de Meta haya señalado un ángulo ganador, (b) ese ángulo
tenga una pieza NATIVA grabada — la grabación de pantalla generando un viaje es la
candidata—, y (c) uno de los vídeos orgánicos haya dado señales de vida. Con esas tres,
la campaña se monta con presupuesto propio (20 €/día, 7 días), no con el de Meta partido.

## Los enlaces (cópialos tal cual — la atribución depende de ellos)

```
Orgánico:
https://travelsnomad.com/?utm_source=tiktok&utm_medium=organic&utm_campaign=g1-museo
https://travelsnomad.com/?utm_source=instagram&utm_medium=organic&utm_campaign=g1-museo
  (cambia g1-museo por el guion que toque: g2-planificar, g4-precio, g5-pueblo…)

Pagado:
https://travelsnomad.com/?utm_source=meta&utm_medium=paid&utm_campaign=lista-a
https://travelsnomad.com/?utm_source=tiktok&utm_medium=paid&utm_campaign=lista-a
  (lista-a / lista-b / lista-c según el copy)
```

En TikTok/IG el enlace va en la bio (los orgánicos no permiten link en el vídeo): pon el
de `utm_campaign=bio` y cámbialo si un vídeo explota, o usa el enlace del guion en las
stories con sticker.

## El calendario de septiembre, con fechas

Cuatro semanas, y cada una tiene UNA cosa que decidir al final. La cuenta atrás es real:
el lanzamiento es en octubre y la lista se cierra el día que se abre la tienda.

| Semana | Qué se publica | Qué se decide el viernes |
|---|---|---|
| **1 · 1-7 sep** | G1 (museo), G2 (planificar). Dos vídeos, los dos en TikTok + Reels + Shorts. | ¿Cuál de los dos retiene más? Ése marca el tono del resto. |
| **2 · 8-14 sep** | G4 (comparación de precio), G5 (el pueblo). Más una **story diaria** con el contador de la lista. | ¿Hay ya un ganador claro? Si sí, empieza el pagado de aprendizaje. |
| **3 · 15-21 sep** | G6 (tour de heladerías) y una iteración del ganador de la semana 1 — **mismo concepto, ejecución nueva**, que es lo que se hace con lo que funciona. | ¿El coste por alta pagada baja de 0,60 €? Si no, se corta y todo va a orgánico. |
| **4 · 22-30 sep** | G7 (modo avión — necesita la build nueva) y G3 (el paseo). Empieza la cuenta atrás: «quedan X días para cerrar la lista». | ¿Se llega a 350? Y sobre todo: **qué canal las trajo**, que es lo que se escala en octubre. |

**La cuenta atrás de la última semana es la que más altas trae.** Una lista que se cierra
es una razón para apuntarse hoy en vez de «ya me apuntaré».

## Presupuesto: un techo, no un grifo

- **Semanas 1-2: cero euros.** Sólo orgánico. Nada de pagar por una creatividad que no ha
  demostrado retener a nadie gratis.
- **Semanas 3-4: 5 €/día, tope 150 € en total.** Es un presupuesto de **aprendizaje**, y
  el número de arriba explica por qué no puede ser más: a 0,24 € de valor por alta, cada
  euro gastado por encima del CPL real se pierde. Lo que se compra con esos 150 € no son
  altas — es saber a qué creatividad ponerle dinero en octubre.
- **Octubre (en tienda)**: ahí sí, campaña de instalación con las ganadoras + Apple Search
  Ads. El presupuesto se decide entonces, con el coste por alta de septiembre delante y
  con un dato que hoy no existe: cuánta gente compra el segundo viaje.

## Cuándo parar un anuncio, en aritmética y no en corazonadas

Del sistema de decisión de Meta de la skill `ads`, adaptado a nuestro número. El ancla es
**el coste objetivo por alta (TCPL) = 0,25 €**, y todo lo demás son múltiplos de él.

| Situación | Qué hacer | Por qué |
|---|---|---|
| Ha gastado **menos de 0,75 €** (3× TCPL) | **Esperar.** No mirar aún. | Con menos gasto no hay señal: juzgar a 2× tiene un 13 % de falsos negativos. A 3×, si el anuncio fuera bueno ya habrían entrado ~3 altas, así que cero altas ahí es un ~5 % de probabilidad. |
| **Cero altas** con ≥0,75 € gastados | **Matar el CONCEPTO,** no iterarlo. | Un concepto muerto no mejora cambiándole el texto. |
| **Hay clics y no hay altas** (menos del ~3 % de los clics se apuntan) | **No matar el concepto todavía.** Mirar el embudo primero: «visitas a la página de destino» contra «clics en el enlace». | La fila de arriba da por supuesto que después del clic el embudo convierte. Cuando no, mata el creativo — que es la parte que sí funciona. Ver abajo. |
| Coste por alta **≤ 0,25 €** | Candidato a ganador. | |
| Entre **0,25 y 0,38 €** | Vigilar. Es varianza normal. | |
| **> 0,38 €** (1,5× TCPL) | Cambiarlo. Es fallo estructural, no ruido. | |
| Meta apenas le da gasto | **Matar ya.** | Que el algoritmo no lo reparta ES el veredicto: te ha pre-cribado el anuncio gratis. |

**Y una regla que se salta todo el mundo: al iterar sobre un anuncio que murió por falta
de reparto, cambia el gancho o el visual — nunca el texto.** Si nadie llegó a leerlo, el
texto no era el problema.

**Nunca pausar sin un reemplazo listo.** Si no hay otro vídeo preparado, el dinero vuelve
al que ya funciona; dejar corriendo un anuncio muerto es peor que no tener ninguno.

### La fila que faltaba: hay clics y no hay altas (2-sep)

La tabla se escribió suponiendo que el embudo convierte y que el único fallo posible está
en el anuncio. La campaña demostró que no, y la fila nueva la pagó ese día.

**Los números que la motivan**, del panel de Meta:

| | |
|---|---|
| 20 000 de alcance → 677 clics | **3,4 % de CTR** — bueno para tráfico frío |
| 677 clics → 1 alta | **0,15 %** |
| Lo que da una página de lista que funciona | 10-30 % → **entre 68 y 200 altas** |
| Lo que daría una mala | 3 % → 20 altas |

Un factor de 60 a 200 no es varianza. Y aplicando la tabla vieja tal cual —cero altas con
gasto de sobra— tocaba **matar el concepto**, es decir, matar lo único que estaba
funcionando: un 3,4 % de CTR no es un anuncio que la gente ignore.

**La portada no es la culpable.** Comprobado en producción antes de opinar, no leyendo el
fichero: responde 200 en 0,25 s (36 KB) y las doce imágenes de `/shots/` responden 200; el
formulario viene en el HTML servido, no depende de JS para existir; en un iPhone 13
(390×664) el campo de correo está en **y=259, visible sin bajar**, con el precio debajo; el
guion de idioma conserva `location.search` entera, así que la atribución utm sobrevive al
salto; y el POST a `/rest/v1/waitlist` trata el 409 como éxito, así que un correo repetido
tampoco se pierde.

**El número que separa las dos historias** es «visitas a la página de destino» contra
«clics en el enlace»:

- **Visitas ≪ clics** (pongamos 150 de 677): los clics nunca llegaron. Con objetivo de
  *tráfico*, Meta compra los clics más baratos que encuentra, y eso suele ser Audience
  Network y toques accidentales. Se arregla **excluyendo esas ubicaciones**, no
  reescribiendo el texto.
- **Visitas ≈ clics** (600 de 677): llegaron, vieron el formulario a la vista y se fueron.
  Entonces sí es la oferta o el mensaje, y toca reescribir.

Hasta tener ese número, **no se mata ningún anuncio por esta vía**: matarlo sin saber cuál
de las dos historias es tira el aprendizaje, que es lo único que los 50 € compraban.

Y el contraste que la fila deja por escrito para la próxima vez: **lo pagado fueron 677
clics y 1 alta; lo orgánico, 4 altas sin gastar un euro.**

## La consulta de atribución (para cualquiera con acceso al SQL editor)

```sql
SELECT coalesce(source, '(directo)') AS origen, count(*) AS altas
FROM public.waitlist GROUP BY 1 ORDER BY 2 DESC;
```

## Checklist del dueño (nada de esto puede hacerlo una sesión)

- ☐ Cuenta TikTok Business y conversión de la de Instagram a empresa (o crearla).
- ☐ Grabar G1, G2, G4, G5 (un iPhone; museo que permita grabar; screen recordings de la
  build 27).
- ☐ Meta Business Suite si se llega a pagar (sin píxel — medimos por waitlist.source).
- ☐ Decidir el arranque del calendario: sin fecha de tienda, la lista puede abrirse ya.

## La web — revisada el 24-ago: funciona, y tiene tres frenos

*Este apartado decía «LISTA, no la toques». Sigue siendo verdad que nada de aquí bloquea la
campaña — pero se auditó la portada COMO EMBUDO el 24-ago (no como página) y aparecieron
tres cosas que cuestan altas. Están en `docs/EMBUDO-ALTA.md` con su porqué.*

### Lo que ya está bien

Formulario funcionando (sondeado 23-ago: 201), captura de UTM con memoria de primer
toque, oferta de 1,99 € ya prometida en portada, móvil arreglado (#28), OG/SEO/404 (#27).
La única mejora con valor real es **un vídeo demo en la portada cuando exista metraje**
(el G1 o G2 recortado) — se añade el día que exista, no bloquea nada de lo anterior.


---

<!-- campana/PLAN-INSTAGRAM.md -->

# Plan de subida a Instagram y primeros 50 € — documento de entrega

Escrito el 28 de agosto de 2026 como **documento autocontenido**: está pensado para
adjuntarse a otro proyecto (el de marketing del dueño) y ejecutarse sin acceso a este
repo. Por eso repite cosas que en el repo viven en `campana/INSTAGRAM-ARRANQUE.md` y
`campana/LANZAMIENTO-PUBLICIDAD.md` — **si algún día divergen, mandan esos dos**.

**Lo que este plan NO incluye**, para que nadie lo busque dentro: los vídeos orgánicos
(guiones G1-G7), que esperan a grabarse con un iPhone en la calle y un museo; TikTok, que
arranca con esos vídeos; y cualquier gasto por encima de los 50 € — eso es el plan de
septiembre y tiene su propio documento.

---

## La situación de partida

- Cuenta de Instagram **vacía**: 0 seguidores, 0 seguidos, sin posts.
- Los 9 posts del grid están **diseñados y listos para exportar** (1080×1350, PNG) en el
  lienzo «Posts de Instagram NOMAD» de Claude Code (claude.ai/code/artifacts, botón de
  exportar en cada tarjeta).
- La web (travelsnomad.com) tiene formulario de lista de espera con **atribución por UTM**:
  cada alta guarda de dónde vino (`waitlist.source`). Todo el plan se mide con eso — **sin
  píxel de Meta, a propósito**: medimos por nuestra base de datos, no por lo que Meta se
  atribuya.
- Números que gobiernan las decisiones (calculados de costes reales):
  - **Un alta vale 0,24 €** (margen esperado de un miembro de la lista).
  - **Coste objetivo por alta (TCPL): 0,25 €.**
  - Un alta pagada en Meta en España cuesta **0,30-1,50 €** — comprar altas NO se paga
    solo; los 50 € compran APRENDIZAJE (saber qué argumento mueve a la gente), no volumen.

---

## Fase 0 — Hoy: vestir la cuenta (1-2 h, manual)

1. **Cuenta profesional** → Ajustes → Cuenta → Cambiar a cuenta profesional → **Empresa**.
   Sin esto no hay anuncios ni métricas.
2. **Nombre**: `NOMAD` · **Usuario**: `@app.nomad` (el elegido el 29-ago; @travelsnomad no quedó libre).
3. **Foto de perfil**: el icono de la app (la hoja verde sobre crema).
4. **Bio** (tal cual, tres líneas — elegida por el dueño el 29-ago; cabe en los 150):
   > Los días escritos. La ciudad, contada.
   > Itinerarios, tours al oído y gastos del grupo.
   > 🎟 Apúntate y no te pierdas el lanzamiento ↓
5. **Enlace de la bio**: `travelsnomad.com` a secas (decisión del dueño, 29-ago — sin
   UTM a la vista). La atribución no se pierde: la portada reconoce el referrer del
   navegador de Instagram y esas altas quedan como `instagram/referral`.
6. **Sigue 20-30 cuentas del nicho**: oficinas de turismo, museos (@museodelprado,
   @lelouvre), cuentas de viajes en español. Señal de vida + cura tu feed para ver qué
   formato funciona nativo.
7. **No compres seguidores. Nunca.** Meta lo huele, la gente lo huele.

---

## Fase 1 — El grid: los 9 posts, el mismo día

Se suben los nueve de una vez (decisión del 29-ago: con 0 seguidores el alcance orgánico
es cero igual — el grid es el escaparate para quien llega del anuncio, y completo hoy vale
más que a medias tres días).

**⚠️ El orden de subida va AL REVÉS: del 9 al 1.** El grid de Instagram pone el post más
reciente arriba a la izquierda, así que para que el mosaico quede como está diseñado
(Coliseo arriba a la izquierda, Trevi abajo) la portada se sube LA ÚLTIMA. Sube 9, 8, 7…
hasta el 1, con unos minutos entre cada uno. Cada post con su caption de la tabla.

Al terminar, **comparte a stories los tres de arriba** (1, 2 y 4 — portada, plan y
precio); nueve stories seguidas sí es ruido.

| # | Post | Caption (copiar tal cual) |
|---|---|---|
| 1 | Portada — Coliseo al atardecer | Los días escritos. La ciudad, contada. Te escribe el viaje y te lo cuenta al oído. Llega en octubre. |
| 2 | El plan — tejados + teléfono con el itinerario | Dices destino y fechas. Tu viaje, planeado día a día: qué ver, en qué orden y cuánto cuesta. |
| 3 | El tour — callejón del Albaicín con la ruta 1-2-3 | Te lleva de una parada a la siguiente y te dice dónde ponerte. Una voz de verdad te lo cuenta al oído, incluso sin cobertura. |
| 4 | El precio — Place du Tertre de noche | El viaje entero, por lo que cuesta un café: desde 2,99 €. Sin suscripción. Se paga por viaje. |
| 5 | El museo — mosaico dorado de Santa Prassede | Apunta la cámara a un cuadro y te cuenta su historia. |
| 6 | La visita — biblioteca de Melk + teléfono | Se acuerda de por dónde has pasado, sin preguntar. |
| 7 | La lista — San Pedro de noche | Tu primer viaje, 1,99 €. Inscríbete y no te pierdas el lanzamiento — el enlace, en la bio. |
| 8 | El grupo — Fontana di Trevi + tarjeta QR | Tus amigos se unen con un QR y los gastos se reparten solos. |
| 9 | El buscador — tres postales: Santorini, Granada, Oporto | ¿Sin destino? Dile qué te apetece y elige entre tres viajes pensados para ti. |

Notas:

- **El QR del post 8 funciona de verdad**: lleva a la portada con
  `utm_campaign=post-grupo`, así que quien lo escanee cae en la lista y se le ve llegar en
  la medición. Si quieres, añade al caption: «(Sí, el QR funciona: pruébalo.)»
- **Hashtags** (sugerencia mía, 5-8 por post, ajustables): #viajar #viajes #escapada
  #europa #audioguia + el del destino de la foto (#roma, #lisboa, #granada, #paris).
- Todas las fotos de los posts son **CC0/dominio público verificado** — no se debe
  atribución a nadie y no hay marca de agua. No hay nada que declarar.

---

## Fase 2 — Los 50 € (arranca al día siguiente del grid)

El dinero NO arranca con la cuenta vacía: quien toque el perfil desde un anuncio no puede
encontrar un solar. Grid primero, dinero después — pero con los 9 subidos el mismo día,
«después» es mañana.

**Configuración en Meta Business Suite** (Crear anuncio):

- **Objetivo: Tráfico.** Sin píxel, a propósito — se mide por `waitlist.source`.
- **1 campaña · 1 conjunto · 4 anuncios**: los copys **A, B, C y E** de abajo. La D
  (urgencia) se guarda a propósito para la semana del cierre de la lista, cuando sea
  verdad; su hueco lo ocupa E (grupo), un ángulo que ningún competidor puede copiar.
- **La misma imagen en los cuatro**: la del post del plan o la del precio (Place du
  Tertre). Lo que se mide es el argumento, no la foto.
- **Público: amplio.** España, 20-55, **sin intereses apilados** — la creatividad es la
  segmentación (era Andromeda). Ubicaciones automáticas.
- **Presupuesto: 5 €/día. Tope total: 50 €** (≈10 días).
- **Un enlace por anuncio, exactos**:
  - A → `https://travelsnomad.com/?utm_source=meta&utm_medium=paid&utm_campaign=lista-a`
  - B → `...utm_campaign=lista-b` · C → `...lista-c` · E → `...lista-e`

**Los copys** (cuatro ángulos a propósito: precio, cobertura, producto, grupo — se
prueba cuál mueve, no se elige el que más guste). *Pulidos el 30-ago al montar la campaña:
el golpe entero en la primera línea (el feed corta a ~125 caracteres), precios siempre en
el orden 2,99 → 1,99, cierre con la voz de la bio. Se pegan con sus TRES párrafos:*

- **A (precio)** · Título: `Tu primer viaje, por 1,99 €`
  > El viaje entero, por lo que cuesta un café: desde 2,99 €.
  >
  > Los días escritos, los tours a pie contados al oído y las guías de museo — todo
  > incluido, sin suscripción. Y en la lista de espera, tu primer viaje por 1,99 €.
  >
  > Apúntate antes del lanzamiento y no te pierdas nada.

  (La comparación con la audioguía suelta de 6 € murió el 30-ago, y es la SEGUNDA vez
  que el dueño la tira — la primera fue el titular de la banda del precio de la web.
  Que no vuelva por ninguna puerta: el ancla del precio es el café, que además es
  literalmente lo que dice la imagen del anuncio. Sin ponerle precio al café, a
  propósito: un número concreto invita al comentario de «un café no cuesta eso».)
- **B (cobertura)** · Título: `Te guía por cualquier sitio`
  > Tu próximo viaje no tiene por qué ser a las seis ciudades de siempre.
  >
  > NOMAD te escribe el itinerario y te guía con voz por CUALQUIER sitio — hasta por el
  > pueblo de tu abuela. Llega en octubre, y los de la lista estrenan su primer viaje por
  > 1,99 €.
  >
  > Apúntate y no te pierdas el lanzamiento.
- **C (producto)** · Título: `Los días escritos. La ciudad, contada`
  > Te escribe los días. Te los cuenta al oído mientras andas la ciudad. Te dice qué
  > estás mirando en el museo. Y reparte los gastos del grupo.
  >
  > Todo por 2,99 € el viaje entero, sin suscripción — y en la lista, el primero por
  > 1,99 €.
  >
  > Apúntate antes del lanzamiento de octubre.
- **E (grupo)** · Título: `Los gastos se reparten solos`
  > En todos los grupos hay uno que acaba organizándolo todo. Si eres tú, esto es para ti.
  >
  > NOMAD escribe el viaje, tus amigos se unen con un QR y los gastos se reparten solos.
  > 2,99 € por viaje, sin suscripción — en la lista, el primero por 1,99 €.
  >
  > Apúntate y no te pierdas el lanzamiento.
- **D (urgencia — EN RESERVA, no arranca):** «La lista se cierra cuando abramos. Después,
  el primer viaje cuesta lo que cuesta. Antes, 1,99 €.» Se enciende la semana del cierre,
  con el enlace `...lista-d`, sustituyendo al peor de los cuatro. (Sin pulir a propósito:
  se pule cuando le toque, con lo aprendido de estos.)

**Cuándo parar, en aritmética y no en corazonadas** (ancla: TCPL 0,25 €):

| Situación | Qué hacer |
|---|---|
| Un anuncio ha gastado **< 0,75 €** (3× TCPL) | Esperar. No hay señal todavía. |
| **Cero altas** con ≥ 0,75 € gastados | Matar el CONCEPTO (no iterarlo con otro texto). |
| **Hay clics y no hay altas** (< ~3 % de los clics se apuntan) | **No matar todavía**: el fallo está después del clic. Comparar «visitas a la página de destino» con «clics en el enlace». |
| Coste por alta **≤ 0,25 €** | Candidato a ganador. |
| Entre **0,25 y 0,38 €** | Vigilar: es varianza normal. |
| **> 0,38 €** (1,5× TCPL) | Cambiarlo: fallo estructural, no ruido. |
| Meta apenas le da gasto | Matar ya: el no-reparto ES el veredicto. |

Dos reglas que se salta todo el mundo: al iterar un anuncio muerto por falta de reparto,
**cambia el gancho o el visual, nunca el texto** (nadie llegó a leerlo); y **nunca pauses
sin reemplazo listo** — si no hay otro, el dinero vuelve al que funciona.

---

## Fase 3 — El minuto diario de medición

En el SQL editor de Supabase (o el panel de admin):

```sql
SELECT coalesce(source, '(directo)') AS origen, count(*) AS altas
FROM public.waitlist GROUP BY 1 ORDER BY 2 DESC;
```

Los orígenes que verás: `instagram/referral` (la bio y todo lo orgánico de Instagram),
`instagram/organic/post-grupo` (el QR del post 8, que sí lleva UTM porque nadie ve esa
URL), `instagram/organic/story-personal` (la historia del Instagram personal del dueño,
30-ago — amigos y boca a boca, con su enlace UTM propio para no mezclarse con la bio),
`instagram/organic/story-italia` (31-ago: las amigas italianas de la novia del dueño
compartiendo a sus historias — es el TEST de si Italia convierte con la web aún en
español; si el viernes hay filas aquí, la expansión de idiomas se decide con ese dato), y
`meta/paid/lista-a`, `-b`, `-c`, `-e` (los anuncios). **La única
tabla de resultados que importa** es la comparación entre esos cuatro últimos.

**El viernes de la primera semana**: coste por alta por copy → se decide qué argumento se
escala en octubre y cuáles se matan. Ese aprendizaje es lo que compran los 50 €.

---

## Resumen del calendario

| Día | Qué |
|---|---|
| Hoy | Fase 0: vestir la cuenta (1-2 h) + Fase 1: los 9 posts, del 9 al 1 |
| Mañana | Fase 2: campaña de 5 €/día, 4 anuncios A/B/C/E |
| Cada día | Fase 3: la consulta SQL (1 minuto) + reglas de parada |
| Viernes sem. 1 | Decisión: qué argumento gana; informe de costes por alta |
| Día ~10 | Tope de 50 € alcanzado → parar y decidir octubre con datos |
| Semana del cierre | La D (urgencia) entra con `lista-d`, sustituyendo al peor |


---

<!-- campana/INSTAGRAM-ARRANQUE.md -->

# El arranque de Instagram y los primeros 50 €

Escrito el 28 de agosto de 2026, el día que el dueño dijo *«empezar hoy con 50 € de publi,
pero tengo la cuenta vacía: 0 seguidores y 0 seguidos»*. Este doc es la respuesta operativa;
la estrategia y la economía viven en `campana/LANZAMIENTO-PUBLICIDAD.md` y no se repiten aquí.

## La corrección de modelo mental, primero

**Los seguidores no importan para los anuncios.** Meta enseña el anuncio a quien quiere,
tengas 0 o 100.000. Lo que SÍ importa es que **quien toque el perfil desde el anuncio no
encuentre un solar**: un grid vacío huele a estafa y tira los clics pagados. Así que el
orden es: hoy se viste la cuenta, y el dinero arranca con el grid puesto — mañana o pasado,
no dentro de un mes.

**Y los 50 € no se gastan en un día.** El plan ya calculó por qué (un alta vale 0,24 € y
el CPL de Meta en España es 0,30-1,50 €): el pagado de septiembre es presupuesto de
APRENDIZAJE. 50 € son **5 €/día durante 10 días** — exactamente la forma del presupuesto
de aprendizaje del plan, empezado antes. Lo que compran no son altas: es saber cuál de los
cuatro argumentos (precio, cobertura, producto, grupo) mueve a la gente, ANTES de
ponerle dinero de verdad en octubre.

**No compres seguidores, nunca.** Meta lo huele, la gente lo huele, y no hay nada que un
perfil con 40 posts honestos no arregle solo.

## Hoy: vestir la cuenta (1-2 horas, todo tuyo)

1. **Pásala a cuenta de empresa** (Ajustes → Cuenta → Cambiar a cuenta profesional →
   Empresa). Sin esto no hay anuncios ni métricas.
2. **Nombre**: `NOMAD` · **Usuario**: `@app.nomad` (elegido el 29-ago; @travelsnomad no
   quedó libre).
3. **Bio** (cópiala tal cual — la eligió el dueño el 29-ago):
   > Los días escritos. La ciudad, contada.
   > Itinerarios, tours al oído y gastos del grupo.
   > 🎟 Apúntate y no te pierdas el lanzamiento ↓
4. **Enlace de la bio**: `travelsnomad.com` a secas (29-ago: el dueño no quiso UTM a la
   vista). La portada atribuye por referrer y esas altas salen como `instagram/referral`.
5. **Sigue 20-30 cuentas del nicho** — oficinas de turismo, museos (@museodelprado,
   @lelouvre), cuentas de viajes en español. Es señal de vida y te cura el feed para ver
   qué formato funciona nativo, que es de donde salen los anuncios que no parecen anuncios.

## Los 9 posts del grid (diseñados; se exportan del lienzo)

Los nueve están diseñados a 1080×1350 en el lienzo de Claude
(«Posts de Instagram NOMAD» — el enlace que te pasé por chat; también aparece en
claude.ai/code/artifacts). Cada tarjeta tiene su botón de **exportar PNG**.

**Se suben los nueve el mismo día y EN ORDEN INVERSO, del 9 al 1** (decidido el 29-ago):
el grid de Instagram pone lo más reciente arriba a la izquierda, así que para que el
mosaico quede como está diseñado la portada del Coliseo se sube LA ÚLTIMA.

Son fotográficos: fotografía real de viaje, scrim oscuro y titular en serif
encima. **Todas las fotos son CC0 o dominio público** (verificado foto a foto en
Wikimedia Commons el 28-ago): no se debe atribución a nadie, ni en la imagen ni
en el pie — por eso no hay marca de agua. El registro de qué fichero de Commons
es cada una queda guardado con los fuentes del lienzo, por si algún día hay que
demostrar la procedencia.

| # | Post (imagen del lienzo) | Pie (caption) |
|---|---|---|
| 1 | Portada — Coliseo al atardecer | «Los días escritos. La ciudad, contada. Te escribe el viaje y te lo cuenta al oído. Llega en octubre.» |
| 2 | El plan — tejados de Praga + teléfono | «Dices destino y fechas. Tu viaje, planeado día a día: qué ver, en qué orden y cuánto cuesta.» |
| 3 | El tour — callejón del Albaicín con la ruta 1-2-3 | «Te lleva de una parada a la siguiente y te dice dónde ponerte. Una voz de verdad te lo cuenta al oído, incluso sin cobertura.» |
| 4 | El precio — Place du Tertre (Montmartre) de noche, terrazas encendidas | «El viaje entero, por lo que cuesta un café: desde 2,99 €. Sin suscripción. Se paga por viaje.» |
| 5 | El museo — mosaico dorado de Santa Prassede (Roma) | «Apunta la cámara a un cuadro y te cuenta su historia.» |
| 6 | La visita — biblioteca de la abadía de Melk + teléfono | «Se acuerda de por dónde has pasado, sin preguntar.» |
| 7 | La lista — San Pedro y el puente de noche | «Tu primer viaje, 1,99 €. Inscríbete y no te pierdas el lanzamiento — el enlace, en la bio.» |
| 8 | El grupo — Fontana di Trevi de noche + tarjeta QR | «Tus amigos se unen con un QR y los gastos se reparten solos.» |
| 9 | El buscador — tres postales: Santorini, Granada, Oporto | «¿Sin destino? Dile qué te apetece y elige entre tres viajes pensados para ti.» |

Al terminar, a stories solo los tres fuertes (portada, plan y precio) — nueve seguidas
es ruido. Con el grid entero puesto, la campaña puede arrancar al día siguiente.

## Los 50 €, cuando el grid esté (día 2-3)

Meta Business Suite → Crear anuncio → **objetivo Tráfico** (sin píxel a propósito: medimos
por `waitlist.source`, no por lo que Meta se atribuya).

- **1 campaña, 1 conjunto, 4 anuncios** — los copys **A, B, C y E** de
  `LANZAMIENTO-PUBLICIDAD.md` §Copys (la D, urgencia, queda en reserva para la semana del
  cierre), con **la misma imagen los cuatro** (la del plan o la del precio — Place du
  Tertre): lo que se mide es el argumento, no la foto.
- **Público: amplio.** España, 20-55, sin intereses apilados — la creatividad es la
  segmentación (skill `ads`, era Andromeda). Ubicaciones automáticas.
- **Presupuesto: 5 €/día.** Tope total 50 €.
- **Enlaces, tal cual** (uno por anuncio):
  `https://travelsnomad.com/?utm_source=meta&utm_medium=paid&utm_campaign=lista-a` (…b/c/e)
- **Reglas de parada**: la tabla de `LANZAMIENTO-PUBLICIDAD.md` §Cuándo parar, anclada en
  TCPL 0,25 €. En corto: nada se juzga antes de 0,75 € gastados; cero altas con 0,75 € =
  concepto muerto; si Meta no le da gasto a uno, ése ya está juzgado. **Y la excepción que
  se lleva por delante a la segunda regla** (2-sep): si hay clics y no hay altas, el fallo
  está después del clic — se miran «visitas a la página de destino» contra «clics en el
  enlace» antes de matar nada.

## El minuto diario de medición

```sql
SELECT coalesce(source, '(directo)') AS origen, count(*) AS altas
FROM public.waitlist GROUP BY 1 ORDER BY 2 DESC;
```

En el SQL editor de Supabase (o el panel). `meta/paid/lista-a` contra `lista-b/c/e` es la
única tabla de resultados que importa. El viernes de la primera semana: coste por alta por
copy, y con eso se decide qué se escala y qué se mata.

(Un origen más desde el 30-ago: `instagram/organic/story-personal` — la historia del
Instagram personal del dueño hacia amigos, con su UTM propio
`utm_source=instagram&utm_medium=organic&utm_campaign=story-personal` para que el boca a
boca no se mezcle ni con la bio ni con los anuncios. No compite con los cuatro de arriba:
es gratis.)

## Lo que este doc NO cambia

El plan de septiembre sigue siendo el de `LANZAMIENTO-PUBLICIDAD.md`: **el canal que se
paga solo es el orgánico en vídeo** (un alta orgánica cuesta cero), y los guiones G1-G7
siguen esperando un iPhone y un museo. Estos 50 € adelantan el aprendizaje pagado con el
grid como requisito — no lo sustituyen.

## Los Reels: por qué, y cómo se fabrican sin cámara (31-ago)

Pregunta del dueño esa tarde: «¿consideras añadir más contenido a Instagram?». La
respuesta medida, y la razón de esta sección: **más posts del grid ya no compran nada**.
Con 0 seguidores un post estático no lo ve nadie — el grid es el escaparate de quien
llega del anuncio o de la bio, y con 12 piezas (9 del grid + 3 carruseles de idiomas) ese
trabajo ya está hecho. **Reels es la única superficie de Instagram que enseña algo a
quien NO te sigue**, y la cuenta tenía cero vídeo. Ese era el hueco, no el número de
posts.

Y hay una segunda razón para el formato: es el sitio natural del **asistente de IA**, que
en la publi estaba callado (de ahí también el copy F de `LANZAMIENTO-PUBLICIDAD.md`). El
gancho del Reel es «le pedí a una IA que me organizara 3 días en Roma» — primera persona,
alguien enseñando lo que ha probado, que es cómo se cuenta una herramienta en el feed. Un
Reel que parece un anuncio se salta.

**Se fabrican desde una sesión, sin grabar nada.** El pipeline vive en `piezas/reels/`:

1. `gen-reel.py` (y `gen-reel-it.py`) escriben 5 escenas HTML de 1080×1920 con el sistema
   visual de la casa — mismo HELMET de fuentes que los carruseles — y el teléfono
   compuesto con las capturas REALES ya parcheadas por idioma (`capplanit.png`…).
2. `exportar-reel.mjs` las convierte en PNG con el chromium de `/opt/pw-browsers`.
3. `montar-reel.sh` las monta en mp4 con **ffmpeg**, que NO viene en el contenedor pero se
   instala en 11 segundos: `npm i ffmpeg-static`.

Las dependencias que no están en el repo (fotos CC0 del banco, `Main.dc.html` con el
HELMET, las capturas parcheadas) se rehacen con los generadores del scratchpad; su
procedencia está en `fotos/bajadas.json`.

**Las dos trampas de ffmpeg, pagadas ya, para que nadie las vuelva a pagar:**

- **`zoompan` genera `d` frames POR CADA FRAME DE ENTRADA.** Con `-loop 1 -t 3` la entrada
  ya son 90 frames y `d=90` los multiplica: el primer montaje salió de **5 minutos y 35
  segundos** en vez de 14,6. La entrada tiene que ser UNA imagen suelta, sin `-loop`.
- **El pre-escalado ×2 antes del `zoompan`** es lo que quita el temblor que ese filtro
  tiene sobre imágenes grandes. Sin él, el movimiento «salta» de píxel en píxel.

**Zona segura**: la interfaz de Instagram tapa ~200 px arriba y ~420 px abajo. Todo el
texto vive entre `y=230` e `y=1480`; lo de abajo es decoración sacrificable.

**Los Reels salen SIN pista de audio, a propósito.** Un audio horneado es un riesgo de
copyright y, sobre todo, renuncia al empujón algorítmico: el audio se elige DENTRO de
Instagram al subir, de la lista de tendencias del día, que es lo que el sistema premia.
Instagram lo ajusta solo a la duración del vídeo.

## Las destacadas, y por qué NO son más posts (1-sep)

Pregunta del dueño esa tarde: *«¿debería seguir subiendo contenido, algo que ayude a los
nuevos followers a entender qué hace la app y cómo se apuntan a la waitlist?»*.

La respuesta larga —qué se sube, en qué orden, con qué texto y dónde va el adhesivo de
enlace— vive en **`piezas/destacadas/README.md`**. Lo que hay que saber sin abrirlo:

- **Más posts del grid ya no compran nada**, por lo mismo que decía la sección de los
  Reels: con doce piezas, el escaparate está hecho. Lo que faltaba eran las dos
  superficies que el grid no cubre.
- **Las destacadas** son el único sitio de Instagram pensado para «acabo de llegar aquí,
  ¿qué es esto?»: viven bajo la bio, no envejecen y no bajan por el feed. Son once
  tarjetas en dos destacadas —`Qué es` (7) y `La lista` (4)— y **se suben primero como
  historias, así que además son el contenido del día**.
- **La tarjeta de los tres pasos es la que convierte.** «¿Y cómo me apunto?» no puede
  tener como respuesta «busca el enlace»: escribir los tres pasos con el adhesivo de
  enlace delante es la diferencia entre entenderlo y hacerlo. Y la cuarta —«Un correo.
  Uno.»— contesta la objeción que frena a quien YA estaba convencido.
- **Un segundo Reel**, `reel-nomad-grupo.mp4`, con el ángulo del grupo: el único de los
  cuatro de la campaña que ningún competidor puede copiar, y el único que no estaba
  contado en vídeo.

**Y el dato que gobierna todo esto** (consulta del minuto diario, 1-sep): ocho altas,
**todas del 31 de agosto y ninguna del 1 de septiembre** — 4 de `ig/social`, 3 de
`invitacion`, 1 de `meta/paid/lista-a`. Lo orgánico trajo cuatro veces más que lo
pagado, y el día que no se publicó nada no entró nadie. Además `lista-b`, `-c` y `-e`
están a cero: **falta mirar el gasto por anuncio en Meta y aplicarles la tabla de
parada**, que con 5 €/día entre cuatro anuncios cruza el umbral de 0,75 € en menos de un
día. Ese dato no se lee desde una sesión.


---

<!-- piezas/destacadas/README.md -->

# Las destacadas y el segundo Reel — qué se sube, en qué orden y por qué

Escrito el 1 de septiembre de 2026, contestando a la pregunta del dueño esa tarde:
*«¿debería seguir subiendo contenido a redes, algo que ayude a los nuevos followers a
entender qué hace la app y cómo se pueden inscribir en la waitlist?»*

**Sí, pero no más posts del grid**, y la razón no es una opinión: con doce piezas ya
subidas (los 9 del grid + 3 carruseles), el escaparate del perfil está hecho. Lo que
falta en esa cuenta son las dos superficies que el grid no cubre:

- **Las destacadas** son el único sitio de Instagram pensado literalmente para «acabo de
  llegar aquí, ¿qué es esto?». Viven bajo la bio, no envejecen y no bajan por el feed.
  La cuenta no tiene ninguna.
- **Los Reels** son la única superficie que enseña algo a quien NO te sigue. Hay uno.

## Lo que este documento NO incluye

Los vídeos con cámara (guiones G1-G7 de `LANZAMIENTO-PUBLICIDAD.md`), TikTok, cualquier
cambio en la campaña pagada o en su presupuesto, y más posts del grid. Nada de eso está
aquí y no es que se haya olvidado.

## Antes de subir nada: el minuto de medición dice algo (1-sep)

```
origen              altas   primera      última
ig/social             4     31-ago       31-ago
invitacion            3     31-ago       31-ago
meta/paid/lista-a     1     31-ago       31-ago
```

Ocho altas, **todas del 31 de agosto y ninguna del 1 de septiembre**. Dos lecturas, y
las dos importan:

1. **Lo orgánico trajo 4 y lo pagado 1.** Y el día que no se publicó nada, no entró
   nadie. Ése es el argumento entero a favor de seguir subiendo contenido.
2. **`lista-b`, `lista-c` y `lista-e` están a cero altas.** La tabla de parada de
   `PLAN-INSTAGRAM.md` §Fase 2 dice: *cero altas con ≥ 0,75 € gastados = matar el
   CONCEPTO, no iterarlo*. Con 5 €/día repartidos entre cuatro anuncios, ese umbral se
   cruza en menos de un día. **Falta el dato del gasto**, que sólo se lee en Meta
   Business Suite y no desde aquí: mira lo gastado por anuncio y aplica la tabla. Si
   `lista-a` se ha llevado más de 0,25 € por esa única alta —y con casi total seguridad
   sí—, tampoco es un ganador todavía; es el único que no está muerto.

## Destacada 1 · «Qué es» — 7 tarjetas

Orden de subida: **1 → 7, en orden normal**. Las destacadas se leen hacia adelante, al
revés que el grid. Se suben como historias del día (así son también el contenido de hoy),
y al terminar se guardan las siete en una destacada nueva.

| # | Fichero | Qué dice |
|---|---|---|
| 1 | `qe-1.png` | ¿Qué es NOMAD? — la app en una frase |
| 2 | `qe-2.png` | 1 · El plan — dices dónde y cuándo, te escribe los días |
| 3 | `qe-3.png` | 2 · El tour a pie — te lleva de parada en parada |
| 4 | `qe-4.png` | 3 · El museo — enfocas una obra y te cuenta su historia |
| 5 | `qe-5.png` | 4 · El grupo — entran con un QR, los gastos se reparten solos |
| 6 | `qe-6.png` | Y cuánto cuesta — 2,99 €, sin suscripción |
| 7 | `qe-7.png` | Llega en octubre — la lista ya está abierta |

- **Nombre de la destacada: `Qué es`** · **carátula: `car-quees.png`**.
- **El adhesivo de enlace va en la tarjeta 7**, apuntando a
  `https://travelsnomad.com/?utm_source=instagram&utm_medium=organic&utm_campaign=destacada-quees`.
  La tarjeta tiene la mitad de abajo vacía a propósito, ahí es donde cabe.
- El precio va el penúltimo a propósito: se dice DESPUÉS de que valga la pena, no antes.

## Destacada 2 · «La lista» — 4 tarjetas

| # | Fichero | Qué dice |
|---|---|---|
| 1 | `li-1.png` | La lista de espera — qué es, qué te llevas, cómo se entra |
| 2 | `li-2.png` | Tu primer viaje por 1,99 € en vez de 2,99 € |
| 3 | `li-3.png` | Cómo se entra — los tres pasos, escritos |
| 4 | `li-4.png` | Un correo. Uno. — y te borras cuando quieras |

- **Nombre de la destacada: `La lista`** · **carátula: `car-lista.png`**.
- **El adhesivo de enlace va en la 1 y en la 3**, con
  `...utm_campaign=destacada-lista`. La 3 es la que convierte: es donde alguien que ya
  ha decidido apuntarse tiene el enlace delante mientras lee los pasos.
- La tarjeta 4 existe porque la pregunta que frena a quien ya estaba convencido no es
  «¿qué es esto?» sino «¿me vais a llenar el correo?». Contestarla antes de que la
  piense es manejo de objeciones, y es la tarjeta más barata de escribir de las once.

## El segundo Reel · «El del grupo»

`reel-nomad-grupo.mp4` — 1080×1920, 15,4 s, **sin pista de audio a propósito** (se elige
dentro de Instagram, de la lista de tendencias del día, que es lo que el algoritmo
premia; un audio horneado renuncia a ese empujón y es riesgo de copyright).

Por qué este ángulo y no otro: el primer Reel ya cuenta el producto entero, y repetirlo
con otras fotos no le enseña nada nuevo a quien lo vio. **El grupo es el único de los
cuatro argumentos de la campaña que ningún competidor puede copiar** —los demás escriben
itinerarios, no reparten cuentas— y en vídeo no estaba contado. El gancho no habla de la
app: describe a una persona que el espectador reconoce en dos segundos.

**Pie del Reel** (copiar tal cual):

> En todo grupo hay uno que acaba organizándolo todo. Si eres tú: NOMAD te escribe el
> viaje, tus amigos entran con un QR y los gastos se reparten solos. 2,99 € el viaje
> entero, sin suscripción — y en la lista de espera, el primero por 1,99 €.
>
> Llega en octubre. El enlace, en la bio.

Etiquetas: `#viajar #viajes #viajeenpareja #viajeconamigos #escapada #europa #roma`

**Al subirlo**: portada del carrete = el fotograma del QR (el segundo 7), que es el que
para el pulgar en la cuadrícula.

## ¿En todos los idiomas? No: en dos, y con una regla por superficie (1-sep, noche)

Pregunta del dueño: *«¿hay que subir en todos los idiomas? creo que el 50% de los
seguidores es gente de Italia»*.

**Lo que dice la base de datos antes de opinar.** Las 8 altas llevan `lang = es`. Cero
por `/it/`. Y la historia italiana del 31-ago (`story-italia`, las amigas de la novia del
dueño compartiéndola) **no dejó ni una fila**: no es un fallo de medición, porque la
portada conserva el UTM al redirigir a `/it/` y esa página graba `lang = it`. Los
italianos que la vieron no se apuntaron. Eso tiene dos lecturas y desde aquí no se
distingue cuál es la buena:

1. Siguieron la cuenta por cortesía (son amigas de una amiga) y no van a convertir en
   ningún idioma.
2. Tocaron un perfil en español —bio, historias, grid— y se fueron: **el idioma era la
   barrera**.

**Las destacadas en italiano son la prueba más barata que separa las dos.** Cuestan
minutos (el generador es bilingüe y las capturas `*-900-it` ya existían), y sus
adhesivos llevan un UTM propio: si en una semana aparecen altas con `lang = it`, era el
idioma y el italiano pasa a tratarse como el español. Si no, son seguidores de cortesía
y no se dobla nada más.

**No en cuatro idiomas.** Francés e inglés no tienen ni una señal —ni seguidores
contados, ni altas, ni prueba—, y cuadruplicar cada pieza para una audiencia que no
está medida es el trabajo que mata una cuenta pequeña. El carrusel en cada idioma que
ya hay en el grid dice «hablamos tu idioma», y con eso basta hasta que el dato diga otra
cosa.

**La regla, superficie por superficie**, que es la respuesta práctica a «hay que subir
en todos»:

| Superficie | Qué se hace | Por qué |
|---|---|---|
| **Bio** | Se queda en español | El enlace ya detecta el idioma del teléfono y manda a `/it/` **conservando el UTM** (`web/index.html`, el `location.replace` con `location.search`). No hay que tocarla. |
| **Destacadas** | Una por idioma: `Qué es` + `Cos'è`, `La lista` + `Lista d'attesa` | No ensucian el feed y son lo que ve quien acaba de llegar. **Los adhesivos italianos apuntan a `/it/` directamente**, no a la raíz: así un italiano con el móvil en inglés cae igual en la página italiana. |
| **Posts del feed** | Pie bilingüe: español, salto de línea, italiano. La imagen no se rehace | El grid está hecho y el texto en imagen es la marca. Instagram traduce pies con un toque, imágenes no. |
| **Historias del día** | En español | Es el mercado principal y donde está el dinero pagado. Si las destacadas italianas traen altas, se alterna. |
| **Reels** | Uno por idioma **cuando lo valga**. `reel-nomad-it.mp4` ya existe y no está subido: se sube | El texto en pantalla no se traduce. Un Reel en italiano llega a italianos que no te siguen, que es lo único que hace un Reel. El del grupo en italiano, sólo si el español funciona. |
| **Pagado en Italia** | Nada, todavía | El plan del 31-ago lo dejó escrito: la expansión se decide con las filas de `story-italia`. No hay filas. |

**El número real de seguidores italianos** no es «creo»: Instagram → panel profesional →
Estadísticas → Seguidores totales → Principales ubicaciones. Es un dato de un minuto y
cambia lo que vale esta apuesta.

**La medición**, cada día, junto a la de siempre:

```sql
SELECT coalesce(lang, '(sin lang)') AS idioma, coalesce(source, '(directo)') AS origen, count(*)
FROM public.waitlist GROUP BY 1, 2 ORDER BY 3 DESC;
```

### Destacadas en italiano · `Cos'è` (7) y `Lista d'attesa` (4)

Mismas fotos, mismas posiciones y mismas carátulas que las españolas. Ficheros
`quees-it-1..7.png` y `lista-it-1..4.png`. Los adhesivos:

- `Cos'è`, tarjeta 7 → `https://travelsnomad.com/it/?utm_source=instagram&utm_medium=organic&utm_campaign=destacada-quees-it`
- `Lista d'attesa`, tarjetas 1 y 3 → `...it/?...&utm_campaign=destacada-lista-it`

Se rehacen con `python3 gen-destacadas.py it && node exportar-destacadas.mjs it`.

## Dónde se editan ahora (1-sep, noche)

Las once tarjetas de cada idioma, las carátulas y las escenas de los tres reels viven en
el **taller de redes**, un lienzo editable con el kit de marca y siete plantillas:
<https://claude.ai/code/artifact/0fea041b-1676-4675-94ab-fc326d44bdb3>. Lo pidió el dueño
esa noche («quiero poder editarlas yo antes por si algo no me gusta»); cómo se construye y
quién manda cuando él edita algo, en `piezas/taller/README.md`. Los generadores de abajo
siguen siendo la fuente mientras no toque el lienzo.

## Cómo se rehacen

```bash
cd <scratchpad>/ig
python3 gen-destacadas.py && node exportar-destacadas.mjs        # 13 PNG de 1080x1920, español
python3 gen-destacadas.py it && node exportar-destacadas.mjs it  # 11 más, en italiano
python3 gen-reel-grupo.py  && node exportar-reelg.mjs && bash montar-reel-grupo.sh
```

Las dependencias que no están en el repo —`Main.dc.html` con el HELMET de fuentes, las
fotos CC0 de `fotos/`, las capturas reales `*-900.webp` y `tarjeta-qr-ejemplo.png`— son
las mismas del grid y de los Reels, y su procedencia está en `fotos/bajadas.json`.
`ffmpeg` no viene en el contenedor: `npm i ffmpeg-static`, 11 segundos.

**Zona segura de historias**: la interfaz tapa ~250 px arriba y ~250 px abajo. Todo el
texto vive entre `y=280` e `y=1500`, y de `y=1520` para abajo se deja libre a propósito —
ahí va el adhesivo de enlace, que es lo único que convierte dentro de una historia.

**Las carátulas se recortan en círculo desde el CENTRO**, y a 60 px de diámetro sólo se
lee UNA forma. Por eso las dos llevan la marca de la casa y se distinguen sólo por el
fondo. El primer intento usó emoji (🌎 y 🎟) y el del billete salió en blanco y negro:
la fuente del HELMET no trae emoji en color y el sistema cayó a una silueta.


---

<!-- campana/MERCADO-2026-08-15.md -->

# Mercado y competencia — 15 de agosto de 2026

Escrito la noche antes de fijar precios e ir a por influencers. Tarifas de competidores
verificadas hoy contra fuentes públicas (citadas al pie); lo que viene de memoria y no de
búsqueda está marcado.

## El mapa: tres categorías compiten por el mismo viaje

**1. Planificadores con IA** — te construyen el itinerario y ahí te dejan.
| Quién | Precio | Nota |
|---|---|---|
| Layla | ~49$/año (free limitado) | La más completa en descubrir+precios vivos |
| Wanderlog Pro | ~40$/año | La mejor en mapa/ruta multi-ciudad |
| Mindtrip | Gratis | Monetiza RESERVAS en el chat (Sabre/PayPal, may-2026) |
| Vacay | 9,99$/mes | |
| ChatGPT/Gemini | «gratis» | El techo de la categoría: el itinerario se está volviendo commodity |

**2. Audioguías / tours autoguiados** — te guían por la calle, pero no planifican nada.
| Quién | Precio | Nota |
|---|---|---|
| VoiceMap | **5–15$ POR TOUR** | Grabados por guías humanos |
| WeGoTrip | **5–15€ POR ATRACCIÓN** | Los bundles abaratan |
| SmartGuide | Mayormente gratis | Cobertura masiva, calidad dispar |
| Rick Steves Audio | Gratis | Nicho Europa, de memoria |

**3. Guías de museo** — Smartify y Bloomberg Connects son gratis *porque las pagan los
museos* (de memoria): no compiten por el bolsillo del viajero, compiten por su atención.

**4. El clúster híbrido «de fábrica» — encontrado por el dueño el 15-ago, y es el vecino
más cercano.** GuideMapp (y clones: DareMapp, GuiaMapp…) junta planificador día-a-día +
tours autoguiados «estilo free tour» + audio + offline. Dos datos lo definen: (a) contenido
**curado y limitado a ~6 grandes ciudades** (Barcelona, Lisboa, París, Londres, Ámsterdam,
Roma); (b) lo fabrica un **estudio de apps en serie** (MWM — plataforma «convierte ideas en
negocios iOS en minutos»), con suscripción **diaria y mensual** y embudo de paywall
agresivo. Es decir: compiten fuerte en ASO y en las seis ciudades de siempre, y no existen
fuera de ellas.

Lo que este clúster enseña:
- **Valida la demanda del combo** planificar+guiar y la disposición a pagar por él en
  formato acotado al viaje (¡pase diario!) — otro punto para el precio por viaje.
- **El foso de NOMAD contra ellos es la generación**: cualquier pueblo (Santa Marinella,
  Civitavecchia), cualquier tema (un tour de heladerías), cualquier idioma — lo curado no
  puede cubrir la cola larga, y la cola larga es donde el viajero real se queda tirado.
  Más el museo obra a obra y los gastos de grupo, que ninguno lleva.
- **La amenaza real es doble**: en ASO te van a superar en presupuesto («guía de viaje»,
  «free tour»), y EN sus seis ciudades su contenido curado puede ganar en calidad narrativa
  a lo generado — que son justo las ciudades donde `tours_cache` más amortiza y donde el
  banco de calidad de la casa tiene que apretar.

Auxiliares: Splitwise (gastos de grupo, free + Pro de pago), TripIt (logística). Nadie de
esta lista hace más de una categoría a la vez.

## La lectura de precios que lo cambia todo

Los planificadores cobran **suscripción anual (40–49$)**. Las audioguías cobran **por tour
(5–15$)**. NOMAD cobra **por viaje (propuesta: 4,99–7,99€) con tours y guías ilimitados
dentro**. Es decir:

- **Un solo tour de VoiceMap cuesta más que un viaje entero de NOMAD.** El componente más
  caro que NOMAD incluye sin límite es exactamente lo que la competencia vende a 6€ la
  unidad. El precio propuesto no es abusivo: está POR DEBAJO del ancla de mercado.
- Contra la suscripción: el viajero ocasional (1–2 viajes/año, la mayoría) paga en NOMAD
  10–16€/año contra 40–49$ de Layla/Wanderlog — gana NOMAD. El viajero muy frecuente
  saldría mejor con sub ajena, pero ese no compra planificador: viaja con ChatGPT.
- El modelo por-viaje casa además con el modelo mental del gasto («me voy a Roma, me lo
  equipo») en vez de con otra suscripción que recordar cancelar.

## Dónde está el foso — y dónde NO está

**El itinerario ya no es defendible**: ChatGPT y Gemini lo regalan y mejoran cada mes. Si
NOMAD se vende como «planificador con IA», compite contra gratis y pierde.

**El foso es cruzar la puerta**: los planificadores te dejan EN la puerta del sitio; las
audioguías te esperan dentro pero no saben de tu viaje. Nadie más junta las cuatro piezas
— planificar + guiarte a pie por la calle (con clima y tu rastro en el mapa) + guiarte
dentro del museo (con la foto de la obra y dónde ponerte) + los gastos del grupo. Eso es
lo que el paywall y todo el marketing deben vender: **una guía que además planifica, no un
planificador con extras.**

## Amenazas honestas

1. **Google**, gratis y preinstalado, absorbiendo el caso «qué hago hoy aquí». Defensa: la
   profundidad de la visita (paradas, obras, dónde ponerse), que Maps no hace.
2. **Mindtrip gratis monetizando reservas** — valida que lo transaccional funciona en
   viajes, y es una segunda línea de ingresos que NOMAD puede añadir más adelante
   (comisión de reservas de eventos/actividades) sin tocar el precio por viaje.
3. **La calidad humana de VoiceMap**: un tour grabado por un guía local bueno gana en
   narrativa a uno generado. Defensa: cobertura infinita (cualquier pueblo, cualquier
   tema, tu idioma) y precio.

## Implicaciones accionables

1. **El esquema de precios del plan queda validado por mercado**, no solo por coste. Y da
   el copy del paywall gratis: *«Tours y guías de museo ilimitados — un solo tour cuesta
   6€ en otras apps»*.
2. **Influencers: el gancho es el tour a pie, no el itinerario.** Un vídeo siguiendo la
   guía por la calle enseña el foso; una captura de un itinerario enseña lo que ChatGPT
   regala.
3. **ASO/keywords** cuando toque la ficha: «audioguía», «free tour», «guía de viaje» —
   categorías donde el precio de NOMAD sorprende — antes que «planificador IA», donde
   gratis es el estándar.
4. Anotar para después del IAP: **reservas como segunda línea** (modelo Mindtrip), primero
   con los eventos de Ticketmaster que ya están en el plan (los enlaces de entradas tienen
   programas de afiliación).

Fuentes (15-ago-2026): comparativas y tarifas de Layla/Wanderlog/Mindtrip/Vacay, y precios
por tour de VoiceMap/WeGoTrip/SmartGuide — enlaces en el mensaje de la sesión que creó
este documento.
