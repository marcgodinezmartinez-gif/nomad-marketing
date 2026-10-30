# Así funciona: el vídeo único de #18 (30-oct)

Un vídeo de **59,3 s** (todo a 1,15×), 1080×1920, 30 fps, H.264 + AAC, con la voz y la música dentro,
para Instagram (reel e historia) y TikTok. Recorre la app en el orden en que se usa: se monta el viaje,
la portada, el plan del día, la guía de paseos y museos, la foto que pregunta, el asistente, los gastos,
el mapa de lugares, el grupo y la recomendación. Sustituye a la idea de seis vídeos sueltos.

Lo que pidió el dueño (30-oct), por orden:

- **un solo vídeo** y no seis, con un guion que **aporte valor**: funciones concretas que hagan decir
  «me la bajo», no frases vacías;
- **en el orden de la app**: montas el viaje, la home, el itinerario, dentro de él guías y museos, el
  asistente, los gastos, los lugares, y se acaba recomendando;
- el guion de abajo, frase a frase (rechazó «pensado para no cruzar la ciudad dos veces», «y lo pasa»,
  «quién debe a quién», «se acabó echar cuentas al volver» y «cada uno sabe lo que le toca»);
- y lo visual: el logo en vectores que se hace línea (la espiral fue «feísima»; de tres maneras eligió el
  **hilo**), un **calendario** en vez de bolas con días, los puntos del plan unidos por una curva con
  sus horas, los gastos como **personas y una línea con un gasto**, nada de cajitas numeradas, el
  asistente con un **mini robot**, y **los dibujos de la derecha sin una línea que los una a la
  pantalla** («se ve feísimo»).

Lo común con los vídeos A y B (el motor de la línea, por qué no se dibuja un iPhone, cómo se cortan las
tomas, la voz y la cadena de sonido) está explicado en `../incluye-pago/README.md`. Aquí, lo propio.
Cómo se publica, con los pies listos para copiar: `PUBLICAR.md`.

## Tres versiones, que sólo cambian en el cierre

| fichero (en `salida/`) | para |
|---|---|
| `nomad-asi-funciona-historia-1080x1920.mp4` | historia de Instagram: acaba en dos flechas hacia el adhesivo de enlace |
| `nomad-asi-funciona-reel-1080x1920.mp4` | reel de Instagram y TikTok: acaba en «Enlace en el perfil» |
| `nomad-asi-funciona-limpia-1080x1920.mp4` | TikTok sin «Sitio web», o una promoción pagada: sin flechas ni texto |
| `nomad-asi-funciona-portada.jpg` | la portada del reel: el logo haciéndose hilo y «Cuatro días en Lisboa. / ¿Por dónde empiezo?» |

El cierre es el de A y B: «Secuencias acortadas.» y el crédito de Apple, y «Pronto en Android™» con
«Android es una marca comercial de Google LLC.».

## El guion

| escena | Kore dice | abajo | al lado |
|---|---|---|---|
| 1 | ¿Cuatro días en Lisboa y no sabes por dónde empezar? | Cuatro días en Lisboa. / ¿Por dónde empiezo? | el logo: la línea recorre su silueta y sale tirada como un hilo a dibujar la pantalla |
| 2 | Le dices a Nomad a dónde vas y cómo te gusta viajar, y te monta el viaje. | Te monta / el viaje entero. | Lisboa, Cultural y Gastronomía, que se encienden cuando Kore las nombra |
| 3 | En la portada, lo que toca ahora, el tiempo y cómo moverte por la ciudad. | Lo que toca ahora, / de un vistazo. | el calendario del viaje, del sábado 21 al sábado 28 de noviembre |
| 4 | Tu viaje, día a día: qué ver, a qué hora y dónde comer. | Tu viaje, / día a día. | los cinco planes del sábado unidos por una curva, con sus horas |
| 5 | En los paseos y en los museos, una guía que te lo cuenta al oído, como si fuera contigo. | Una guía / que te lo cuenta. | unos auriculares |
| 6 | ¿Y eso qué es? Hazle una foto y pregúntaselo. | ¿Y eso / qué es? | una cámara, cuya lente late al decir «foto» |
| 7 | ¿Te apetece cambiar algo? Pídeselo al asistente y te cambia el plan al momento. | Pídeselo / al asistente. | un robot pequeño |
| 8 | Y los gastos del grupo, apuntados y repartidos. | Los gastos, / repartidos. | tres personas y, debajo, «Cena · 64 €» |
| 9 | ¿Te recomiendan un bar? Lo guardas y lo tenéis todos en el mapa. | Tus sitios, / en el mapa. | un pin |
| 10 | Lo paga uno, se apunta automáticamente en los gastos del grupo y se reparte según os vais uniendo. | Lo paga uno, / se reparte solo. | la pantalla se funde; en un suelo aparece la que paga y se enciende con «uno»; con «se apunta» entra «Itinerario del viaje · 6,99 €», y con «según os vais uniendo» llegan las otras tres, una a una, y cambia «entre 2», «entre 3», «entre 4» |
| 11 | Y cuando vuelvas, recomiéndalo, para que alguien lo disfrute como lo has disfrutado tú. | Recomiéndalo. / Que lo disfruten. | un avión de papel encima de los cuatro |
| 12 | Nomad. Descárgala gratis en la App Store. | (el cierre) | |

Los cortes (`T`, en `index.html`) salen de la voz: cada escena dura su frase más 0,55 s, y la frase
empieza 0,25 s después del corte (la del cierre, 0,2). **Si se mueve un corte, se mueve en `index.html`,
en `mezclar.sh` (`EMPIEZA`) y en `tomas.json`.**

**Los dibujos de la derecha se trazan solos**: cada uno empieza en sí mismo (la esquina del calendario,
el primer plan, la punta del pin…), se queda entero mientras Kore habla y se recoge hacia su principio.
Ninguno sale de la pantalla ni del suelo. La única línea que une cosas es la del arranque, que nace del
logo y dibuja la pantalla, y la que sólo une lo que pertenece junto: las tres opciones del viaje y los
cinco planes del día.

**Los dibujos son el juego «editorial»** (30-oct): el dueño vio los primeros —los auriculares, el robot,
la línea del plan— «muy cutres» y pidió líneas más finas en todo lo que se dibuja. De tres juegos eligió
el tercero: **5 px la línea y 3 px los detalles**, un calendario con anillas, la línea del plan en
punteado redondo (se descubre con una máscara), unos auriculares con almohadillas y ondas, una cámara con
su lente, un robot pequeño con la cabeza ladeada, el pin con su ojo y su sombra, las personas con
hombros, y el avión con una estela punteada. Los datos están en `iconos/editorial.json` (con la hoja de
muestra, `iconos/editorial-hoja.png`) y entran en `index.html` con `iconos/datos.py`; a mano no se
tocan. El hilo del arranque, la pantalla y el cierre van también a 5 px.

**Y respiran.** Con la toma de la app quieta y el dibujo ya entero, el primer render se paraba en 16
tramos de 0,4 s o más (hasta 2,4 s en la guía y 2,3 en el mapa). Como en A y B, cada dibujo late suave
en cada negra de la música mientras espera (`respira()` en `index.html`), sin pisar los latidos, brotes
y recogidas que ya tenía: `M.late`, `M.brota` y `M.encoge` apuntan en `OCUPA` cuándo mueven cada cosa.
Medido en el render con el detector de «Un trazo» (a 270×480 en grises, se mueve si algún píxel cambia
más de 2 niveles): **ningún tramo quieto de 0,4 s o más**; los más largos, de 0,33 s (medido otra vez con los dibujos
editoriales y la voz nueva). Como motas, los tres fotogramas del cierre en que el suelo se recoge en un
punto y sube al icono, que es a propósito, y el primer fotograma en que aparece un detalle suelto de los
dibujos nuevos (la almohadilla de los auriculares, la lente de la cámara, la cara del robot): son piezas
aparte del dibujo, no restos.

## El arranque: el logo se hace hilo

La silueta del logo no está dibujada a ojo: `silueta-del-logo.py` pinta a 2048 px los tres trazos del
logo que ya van en `index.html` (los de `mobile/assets/nomad_soft_swoosh_logo.svg` de la app), cierra los
huecos blancos (miden 22 unidades del viewBox; se cierran con 30), saca el contorno con `contourpy` y lo
suaviza. Vuelto a correr el 30-oct, da los mismos 301 puntos, sin una décima de diferencia. Queda en
`SILUETA`, en unidades del viewBox, empezando en el lado izquierdo de la coma y en el sentido del reloj, y
el vídeo lo lleva a la pantalla con la misma transformación que al logo. La línea recorre la silueta,
el relleno se apaga mientras la cierra, y sigue sin parar hacia arriba (en la dirección en que cerró) a
dibujar el borde de la pantalla, mientras la cola recoge la silueta por el mismo camino. La punta
acelera hasta 1,8 s y frena hasta cerrar el borde, con la misma velocidad a los dos lados.

Se probaron tres (el hilo, una gota que cae y suelta la línea, y la curva de dentro del cuenco), las tres
sin motas ni tramos quietos; el dueño eligió el hilo. Las otras dos están en la historia de git
(`2daaf6e`).

## Las tomas

`tomas.json`, cortadas con `cortar-tomas.py` como las de A y B (las grabaciones no están en el repo:
`banco/metraje/README.md`). Recortadas arriba y abajo, sin la isla ni la barra de inicio.

| toma | de dónde | qué se ve |
|---|---|---|
| s2a, s2b | crear 20,85-23,30 y 25,29-29,16 | el asistente de crear viaje: Lisboa, fechas y cómo te gusta viajar |
| s3 | paseo 20,75-22,35 | la portada del viaje |
| s4 | paseo 24,90-28,91 | el plan del sábado 21 |
| s5a | paseo 57,00-61,00 | la parada 1 del paseo, Praça do Comércio, con su audioguía |
| s5b | museo 39,00-42,60 | la obra 1 del museo, «Paneles de San Vicente», con «Cómo llegar» |
| s6 | museo 45,00-49,00 | la foto de la obra a pantalla completa (el visor de la guía), con su crédito: no es la cámara |
| s7 | asistente 12,00-14,10 | el saludo de NOMAD AI, que dice que puede organizar el itinerario |
| s8 | gastos 34,00-37,60 | «Nuevo gasto»: la cena, repartida entre Tú y María. El punteado rojo del corrector de iOS debajo de «Bairro» se tapa con el color del campo (`#velo-s8`) |
| s9 | lugares 42,00-47,00 | Lugares, en el mapa |

**La toma s5a acaba en una errata del texto de la guía**: «Estás en el centro neurológico de la
reconstrucción» (es *neurálgico*). Se funde con el fondo de la app desde «Fíjate en» hacia abajo
(`#velo-s5a`, sólo mientras corre esa toma), así que no se ve; el texto sigue mal en la app (NOMAD#436,
punto 7).

## La voz

Kore, `gemini-3.1-flash-tts-preview`, con el estilo de A y B (lo que va antes de los dos puntos no se
lee; dentro, «Nomad se pronuncia "nómad"»), y transcrita con faster-whisper para elegir. Una toma por
frase: la primera en v01, v03, v04, v07, v09 y v12, y la segunda en v02, v05, v06, v08 y v11 (v08-1
leyó en voz alta el texto del estilo y v11-1 pronunció mal; v02, v05 y v06 salen de la segunda por
comparación con las tomas crudas, residuo −85 dB, aunque aquí ponía «la primera»). Duran de 3,36 s (el cierre) a 6,44 s (la del pago), a 1×. La del pago (v10) es de después
(ver abajo): la segunda de tres tomas, las tres con todas sus palabras.

**La voz se acelera con `atempo` y no con `rubberband` (30-oct).** El dueño la oyó «algo rara en algunos
momentos o palabras». La causa era la aceleración: `rubberband` con sus opciones de fábrica es un vocoder
de fase, y medido sobre las doce tomas subía la desviación de fase entre armónicos de 0,44 a 0,70 rad (un
vocoder sin bloqueo de fase, de control, da 0,90), ponía un pre-eco agudo de +24 dB de mediana delante de
las consonantes que siguen a un silencio («**Y** los gastos», «**t**iempo», «dis**f**rute») y le quitaba
1,35 dB a cada toma. Ninguna opción del motor R2 lo arregla; el R3 queda a medio camino. `atempo` (WSOLA)
deja la fase y los ataques como en la toma (0,44 y −0,3 dB), la potencia igual y cada toma a ±20 ms de
su duración entre 1,15. Descartados con medida: el compresor y el limitador (como mucho 2,9 dB, y más de
1 dB sólo 0,15 s en total), el AAC, los cortes y las juntas. Lo midió una revisión de cuatro lentes, cada
una con otra que intentó refutarla; el oyente artificial (Gemini) no distinguía a ciegas la voz de antes
de la de ahora, así que **lo que decidió fue el oído del dueño**, con la mezcla de antes y la de después.
Whisper oye todas las palabras de las doce frases, y «recomiéndalo» vuelve a tener su /d/.

Lo que queda, y es del TTS, no de la mezcla: «cómo te gusta **viajar,**» sube +11 semitonos y casi suena
a pregunta, y en siete frases Kore para 0,2-0,4 s antes de una «y» sin coma («pídeselo al asistente · y
te cambia el plan»). Se arregla, si molesta, con otra toma de esa frase.

## La música y la mezcla

La de «Un trazo», con la cadena de A y B (`mezclar.sh`): la voz a −18 LUFS, la música a −33 y
apartándose cuando habla Kore, y todo a −16 LUFS lineal. Medido con la voz de `atempo`: **−16,0 LUFS, pico
−3,5 dBFS, LRA 1,7 LU**, y las doce frases enteras en la pista de voz. La música sigue estirándose con
`rubberband`, y su pasada se escribe en coma flotante: en s24 se recortaba, porque al estirarla sube hasta
+2,4 dBFS (1.551 muestras, que no se oían).

**Aquí la pista se alarga, no se acorta**: dura 60,7 s y el vídeo pide 68,2 a 1×. Se repiten **dos veces dos
compases justos** (6,407 s cada vez): hasta el 11,26 de la pista tal cual; desde ahí, la misma pista 6,407 s
antes hasta el 11,26 otra vez; y desde ahí, otra vez 6,407 s antes y ya hasta el final. Las dos juntas se
funden en dos segundos donde los acordes se parecen más (croma 0,916): la primera en 9,26-11,26 a 1×
(8,1-9,8 en el vídeo, encima del corte de la escena 2 a la 3) y la segunda en 15,67-17,67 (13,6-15,4,
encima del de la 3 a la 4). Sólo casan las repeticiones de dos compases: con uno, el croma da 0,73 como
mucho; con tres, 0,6; con cuatro seguidos, 0,68. Así **el último acorde cae en el cierre, como en A y B**:
el arranque más fuerte del final de la pista (51,25) cae en 64,06 a 1× (55,7 en el vídeo), 1,27 s después
del corte del cierre, debajo de «Descárgala gratis», y se apaga con el vídeo. Comprobado contra la pista
original: la larga casa con ella corrida dos y cuatro compases, con correlación 1,0. Después de cada junta
vuelve a sonar la pausa que la pieza tiene en su segundo 5 (un bajón de unos 15 dB): es de la música, no
del fundido. **Está medido, no oído**: las juntas y el final hay que escucharlos en el altavoz del iPhone
y con auriculares.

**Y una trampa de ffmpeg, por si se toca**: con `asplit`, el trozo del medio (el que lleva `atrim` con
`end`) se perdía entero, sin aviso, y la pista salía de 65 s en vez de 73,5. Por eso `mezclar.sh` lee la
pista tres veces.

## Cómo se rehace

```bash
METRAJE=<carpeta> python3 -I cortar-tomas.py         # las tomas (una vez)
python3 -I iconos/datos.py                           # los dibujos de la derecha, de iconos/editorial.json
bash mezclar.sh                                      # assets/sonido.m4a, si cambian voz o tiempos
VERSIONES="historia reel limpia" bash variantes.sh   # los tres vídeos en salida/ y revision/*.png
bash portada.sh ../../../salida/nomad-asi-funciona-portada.jpg
python3 -I silueta-del-logo.py                       # comprueba SILUETA contra el logo (--escribir, la rehace)
```

`assets/motor.js` es una copia del de `../incluye-pago/` con cambios que aquél no necesita: `borde()`
acepta la dirección en que sale la línea (el hilo sale hacia arriba, sin esquina) y cierra solapando
60 px y no 20 (la punta pasa deprisa por donde empezó la línea y no se ve el pellizco de dos remates
tocándose); la vuelta de un dibujo encuentra una marca en el largo 0 (los dibujos ya no empiezan en el
borde de la pantalla); y los latidos del cierre van en la negra de la música, que aquí sigue en su
rejilla porque la junta repite 8 negras justas.
`sincronizar.sh` de `incluye-pago/` no lo toca.

## Lo que queda a la vista, y es sabido

- **La letra de la app no se lee entera** dentro de la pantalla, como en A y B: se leen los títulos y la
  forma de cada pantalla.
- **«Nomad AI» y «NOMAD AI»** en la misma pantalla del asistente (NOMAD#436, punto 9).
- **El museo trata de usted** en «Cómo llegar» («Suba a la planta 3… y diríjase…»), en la toma s5b,
  y el resto de la app va de tú (NOMAD#436, punto 8).
- **La voz dice «cuatro días» y lo que se ve son ocho**: el gancho es «¿Cuatro días en Lisboa…?», pero
  el calendario grande dibuja del sábado 21 al sábado 28 y la portada de la app dice «21 nov – 28 nov ·
  8 días», que es el viaje de ejemplo. Y la toma de crear viaje (s2a) enseña otras fechas, «29 oct — 31
  oct · 2 noches», en letra que no se lee. El gancho es del guion que aprobó el dueño; cambiarlo a «¿Una
  semana en Lisboa…?» es otra toma de Kore y unos minutos de render. Lo decide él.
- **La toma de la foto no enseña la cámara**: es la foto de archivo de la obra, a pantalla completa, con
  su crédito. Por eso no hay destello encima (lo había, y la hacía pasar por una foto recién hecha). La
  función existe (`scan-artwork`), pero el simulador no tiene cámara: para enseñarla hace falta grabarla
  en un iPhone.
- **La toma del asistente es el saludo, no un cambio de plan**: el saludo dice que puede organizar el
  itinerario, y Kore dice que te cambia el plan. Es cierto de la app, pero la toma no lo enseña hecho.
- **«la App Store»** en la voz contra **«el App Store»** de la insignia, y si «Pronto en Android» se
  queda en el cierre (#13): las mismas decisiones abiertas que en «Un trazo».

## Lo que dijo la revisión (30-oct)

Cinco revisores independientes sobre el render de la historia (líneas y dibujos; sincronía y sonido;
normas y privacidad; documentos y afirmaciones; fluidez y lectura), cada uno con un verificador que
intentó tumbar sus hallazgos. Diecinueve confirmados, ninguno grave, y arreglados todos menos los que
decide el dueño y uno de gusto (al final):

- «Cena · 64 €» iba 26 px a la izquierda de las personas y su línea: centrado en 752.
- Las casillas del calendario tocaban el marco: el marco se abre a 600-900 (10 px de aire a cada lado,
  como entre casillas) y el brote rebota menos, para no pisar la raya de «NOV 2026».
- Las tres píldoras de S2 desaparecían de golpe en el corte: encogen antes, como los demás dibujos.
- Al cerrar el borde, la punta alcanzaba despacio a la cola y se veían 3 fotogramas de dos remates
  tocándose: la cola llega antes y el cierre solapa 60 px.
- La persona que paga se encendía cuando aún no se veía: ahora brotan antes y la que paga se enciende
  con «uno». La pantalla, además, se funde en vez de cortarse, y el suelo nace cuando su borde ya se ha
  ido (antes salía un punto suelto dentro del marco vacío).
- El destello sobre la foto de archivo de S6, fuera (arriba, «Lo que queda a la vista»).
- El punteado rojo del corrector bajo «Bairro», tapado.
- Tres tramos quietos de 0,40 s justos (S5, S6 y el final): la respiración empieza antes y los latidos de
  la lente y del cierre llegan más lejos.
- Comentarios de A y B que no valían aquí (el calendario «empieza en lunes», la junta «salta 28
  negras»), corregidos, y el guion de la silueta, que vivía fuera del repo, en `silueta-del-logo.py`.

**Lo que se dejó:** los hombros de las tres personas de S8 se cruzan (van a 90 px y miden ±50), así que
el grupo se lee como una cadena; las cuatro de S10, a 120 px, no se tocan. Así las vio el dueño en el
storyboard y no lo pidió cambiar. Si molesta, es darle a `persona()` un medio ancho de 38 en S8.

Lo que comprobaron y estaba bien: ninguna línea une un dibujo con la pantalla en ningún fotograma; el
calendario dice NOV 2026 con S D L M X J V S para el 21-28 (comprobado con el calendario); las horas de
los cinco planes son las del sábado 21 de la toma; las doce frases de Kore suenan enteras, cada una con
su escena; no se ve ningún código de invitación, correo ni dato personal; el cierre lleva los avisos de
Apple y de Android, y las zonas seguras se respetan.

## Lo que cambió después: el pago, apuntado y repartido (30-oct)

Al ver el vídeo, el dueño: *«lo único que no me gusta es el lo paga uno y lo disfrutan todos, ahí se
debería aclarar que el gasto se incluye automáticamente en los gastos y conforme se unen se divide»*.
Comprobado en la app antes de decirlo: la compra crea un gasto del grupo, «NOMAD · Itinerario del viaje»,
con reparto automático (`compra_como_gasto`, en `20260906150000_compra_como_gasto_del_grupo.sql`), y cada
vez que alguien se une o se va se vuelve a repartir entre los aceptados
(`reparto_automatico_al_cambiar_miembros`), a partes iguales y con el céntimo que sobra para quien paga.

- **La voz**: «Lo paga uno, se apunta automáticamente en los gastos del grupo y se reparte según os vais
  uniendo.» (6,44 s, antes 3,65). **Abajo**: «Lo paga uno, / se reparte solo.»
- **El dibujo**: la que paga aparece y se enciende con «uno»; con «se apunta» entra «Itinerario del viaje
  · 6,99 €» (el precio de un viaje de 8 a 30 días, como el de ejemplo) y, con «según os vais uniendo»,
  llegan las otras tres una a una y cambia «entre 2», «entre 3», «entre 4». No se pinta lo que toca a
  cada una porque la app no lo reparte exacto (1,77 para quien paga y 1,74 para las demás, entre cuatro).
- **La escena dura 2,79 s más**, así que los cortes de después se corren (`T`, `EMPIEZA`) y el vídeo pasa
  de 56,9 a 59,3 s; la música se alarga dos compases más (arriba) y su último acorde vuelve al cierre.
