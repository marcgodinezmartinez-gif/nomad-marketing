# Así funciona: el vídeo único de #18 (30-oct)

Un vídeo de **56,9 s** (todo a 1,15×), 1080×1920, 30 fps, H.264 + AAC, con la voz y la música dentro,
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
| 6 | ¿Y eso qué es? Hazle una foto y pregúntaselo. | ¿Y eso / qué es? | una cámara; la pantalla destella al decir «foto» |
| 7 | ¿Te apetece cambiar algo? Pídeselo al asistente y te cambia el plan al momento. | Pídeselo / al asistente. | un robot pequeño |
| 8 | Y los gastos del grupo, apuntados y repartidos. | Los gastos, / repartidos. | tres personas y, debajo, «Cena · 64 €» |
| 9 | ¿Te recomiendan un bar? Lo guardas y lo tenéis todos en el mapa. | Tus sitios, / en el mapa. | un pin |
| 10 | Lo paga uno y el viaje es de todo el grupo. | Lo paga uno, / es de todos. | la pantalla se va; cuatro personas en un suelo: se enciende la que paga y luego las demás |
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

## El arranque: el logo se hace hilo

La silueta del logo no está dibujada a ojo: un guion de Python rasterizó los tres trazos de
`mobile/assets/nomad_soft_swoosh_logo.svg` (el de la app) a 2048 px, cerró los huecos blancos (miden
22 unidades del viewBox; se cerraron con 30), sacó el contorno con `contourpy` y lo suavizó. Queda en
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
| s6 | museo 45,00-49,00 | la cámara de la guía del museo |
| s7 | asistente 12,00-14,10 | el saludo de NOMAD AI, que dice que puede organizar el itinerario |
| s8 | gastos 34,00-37,60 | «Nuevo gasto»: la cena, repartida entre Tú y María |
| s9 | lugares 42,00-47,00 | Lugares, en el mapa |

**La toma s5a acaba en una errata del texto de la guía**: «Estás en el centro neurológico de la
reconstrucción» (es *neurálgico*). Se funde con el fondo de la app desde «Fíjate en» hacia abajo
(`#velo-s5a`, sólo mientras corre esa toma), así que no se ve; el texto sigue mal en la app.

## La voz

Kore, `gemini-3.1-flash-tts-preview`, con el estilo de A y B (lo que va antes de los dos puntos no se
lee; dentro, «Nomad se pronuncia "nómad"»), y transcrita con faster-whisper para elegir. Una toma por
frase, la primera, salvo v08 y v11, la segunda: v08-1 leyó en voz alta el texto del estilo y v11-1
pronunció mal. Duran de 3,36 s (el cierre) a 6,38 s (la de la guía), a 1×.

## La música y la mezcla

La de «Un trazo», con la cadena de A y B (`mezclar.sh`): la voz a −18 LUFS, la música a −33 y
apartándose cuando habla Kore, y todo a −16 LUFS lineal. Medido: **−16,0 LUFS, pico −2,9 dBFS, LRA
1,5 LU**, y las doce frases enteras en la pista de voz.

**Aquí la pista se alarga, no se acorta**: dura 60,7 s y el vídeo pide 65,4 a 1×. Se repiten **dos
compases justos** (6,407 s): hasta el 11,26 de la pista tal cual y, desde ahí, la misma pista 6,407 s
antes, fundidas en dos segundos (9,26-11,26 a 1×, encima del corte de la escena 2 a la 3) donde los
acordes se parecen más (croma 0,916). Con tres compases no hay junta buena (0,6 como mucho: la armonía va
de dos en dos) y con uno, 0,73. Por eso **el último acorde no cae en el cierre, como en A y B**: el
arranque más fuerte del final de la pista (51,25) cae en 57,66 a 1×, debajo de «…como lo has disfrutado
tú», y el cierre suena sobre su cola, que se apaga sola. Después de la junta vuelve a sonar la pausa que
la pieza tiene en su segundo 5 (un bajón de unos 15 dB, 1,5 s después del corte): es de la música, no del
fundido. **Está medido, no oído**: la junta y ese final hay que escucharlos en el altavoz del iPhone y con
auriculares.

## Cómo se rehace

```bash
METRAJE=<carpeta> python3 -I cortar-tomas.py         # las tomas (una vez)
bash mezclar.sh                                      # assets/sonido.m4a, si cambian voz o tiempos
VERSIONES="historia reel limpia" bash variantes.sh   # los tres vídeos en salida/ y revision/*.png
bash portada.sh ../../../salida/nomad-asi-funciona-portada.jpg
```

`assets/motor.js` es una copia del de `../incluye-pago/` con dos cambios que aquél no necesita: `borde()`
acepta la dirección en que sale la línea (el hilo sale hacia arriba, sin esquina), y la vuelta de un
dibujo encuentra una marca en el largo 0 (los dibujos ya no empiezan en el borde de la pantalla).
`sincronizar.sh` de `incluye-pago/` no lo toca.

## Lo que queda a la vista, y es sabido

- **La letra de la app no se lee entera** dentro de la pantalla, como en A y B: se leen los títulos y la
  forma de cada pantalla.
- **«Nomad AI» y «NOMAD AI»** en la misma pantalla del asistente (NOMAD#436, punto 9).
- **La toma del asistente es el saludo, no un cambio de plan**: el saludo dice que puede organizar el
  itinerario, y Kore dice que te cambia el plan. Es cierto de la app, pero la toma no lo enseña hecho.
- **«la App Store»** en la voz contra **«el App Store»** de la insignia, y si «Pronto en Android» se
  queda en el cierre (#13): las mismas decisiones abiertas que en «Un trazo».
