# La beta de Android: el vídeo de TikTok que busca testers (4-nov)

Un vídeo de **21,7 s** (todo a 1,15×), 1080×1920, 30 fps, H.264 + AAC, con la voz y la música dentro,
para TikTok (y vale igual de reel de Instagram). Busca gente con Android para la prueba cerrada de Google
Play: Google pide 12 testers durante 14 días antes de dejar publicar la app. Acaba pidiendo que comenten
«ANDROID»; a quien comente, el dueño le escribe por mensaje con los pasos (`PUBLICAR.md`).

Lo que pidió el dueño (4-nov): *«quiero que montes tú el vídeo con el diseño como los de Un trazo o el
último que subiste. Con la voz de Kore igual»*. Es la estética de «Así funciona» (`../asi-funciona/`): el
logo se hace hilo, la línea dibuja el borde de la pantalla de la app (no un iPhone, por las normas de
Apple: `../incluye-pago/README.md`), dentro corren las grabaciones reales y al lado cada escena tiene su
dibujo, que se traza solo y se recoge en sí mismo. Lo común (el motor, las tomas, la cadena de sonido)
está explicado en esos dos README; aquí, lo propio.

Cómo se publica, con el texto del post y el mensaje para quien comente: `PUBLICAR.md`.

## El guion

| escena | Kore dice | abajo | al lado |
|---|---|---|---|
| 1 | ¿Tienes Android? ¡Te necesitamos! | ¿Tienes Android™? / Te necesitamos. | el logo, que se hace hilo y dibuja la pantalla |
| 2 | Nomad ya está en iPhone, y para sacarla en Android, Google nos pide… | Ya en iPhone. / Falta Android. | dos píldoras en un collar: «iPhone» se llena al nombrarlo y «Android» sólo enciende su borde, punteado |
| 3 | …doce personas que la prueben durante catorce días. | 12 personas, / 14 días. | dos líneas con seis personas de pie en cada una y, debajo, catorce puntos que se encienden uno a uno |
| 4 | Te monta el viaje día a día y te lo cuenta al oído. | Tu viaje, / contado al oído. | los auriculares de «Así funciona» |
| 5 | Si eres mayor de dieciocho, pruébala gratis antes de que salga. | Pruébala gratis, / antes de que salga. | un sello que se traza en círculo, con «18+» dentro |
| 6 | Comenta «Android» y te escribimos con los pasos. | (el cierre) | el icono, el nombre y un bocadillo que se traza desde su pico alrededor de «Comenta / ANDROID»; debajo, «y te escribimos con los pasos», «Para Android™ · Solo mayores de 18» y los créditos de marca |

Lo que dice cada frase, comprobado: la app es para mayores de 18 desde el 9-oct (NOMAD#385); Google pide
12 testers en la prueba cerrada durante 14 días seguidos (NOMAD, `docs/GOOGLE-PLAY.md` §8); «te monta el
viaje», «día a día» y «te lo cuenta al oído» son frases de «Así funciona», que ya se comprobaron contra la
app. **«Gratis» sólo es verdad si el grupo `nomadapp-testers` está en Pruebas de licencias** de Play
Console: es el paso 0 de `PUBLICAR.md`, y sin él el vídeo no se sube.

Tres reglas que ya había escritas para esta misma campaña (`../testers-android/README.md`, 26-oct) y que la
primera versión se saltó, hasta que lo cazó la revisión:

- **«antes de que salga» y no «antes que nadie»**: el propio vídeo dice que Nomad ya está en iPhone.
- **nunca «prueba cerrada»**, que es jerga de Play Console. La cabecera y el cierre dicen «Para Android™»: las
  normas de marca de Android piden «for Android» junto al logo propio, y el ™ la primera vez.
- **un emoji como mucho, y sólo para señalar**, en los textos de `PUBLICAR.md`.

Los cortes (`T`, en `index.html`) salen de la voz, como en «Así funciona»: cada escena dura su frase más
0,55 s, y la frase empieza 0,25 s después del corte (la del cierre, 0,2). **S2 y S3 son una sola toma de
Kore**, partida 0,2 s antes de «doce» para que la entonación siga entera; partida antes, en «Google», la
píldora de Android se encendía 0,15 s antes de recogerse (lo cazó `hyperframes check`). **Si se mueve un
corte, se mueve en `index.html`, en `mezclar.sh` (`EMPIEZA`) y en `tomas.json`.**

El cierre no es el de A, B y «Así funciona»: no hay insignia de la App Store ni «Enlace en el perfil»,
porque lo que se pide es un comentario. Por eso hay una sola versión, sin «historia» ni «limpia». El
crédito nombra iPhone (lo dice Kore y lo pone la escena 2), y Google y Android; «Android™» lleva el
símbolo la primera vez que sale, en el gancho, y en el cierre.

## Las tomas

`tomas.json`, cortadas con `cortar-tomas.py` (la de `../asi-funciona/`, sin cambios) desde las
grabaciones de la 9.ª pasada de capturas (no están en el repo: `banco/metraje/README.md`). Son ventanas
de «Así funciona», ya miradas allí fotograma a fotograma: sin código de invitación ni datos personales.

| toma | de dónde | qué se ve | velocidad |
|---|---|---|---|
| s3 | paseo 20,75-22,35 | la portada del viaje a Lisboa | 0,40× (es una pantalla quieta) |
| s4 | paseo 24,90-28,91 | el plan del sábado 21 | 1,41× |
| s5a | paseo 57,00-61,00 | la parada 1 del paseo, Praça do Comércio, con su audioguía | 1,13× |
| s5b | museo 39,00-42,60 | la obra 1 del museo, «Paneles de San Vicente» | 0,95× |

La toma s5a acaba en la errata «centro neurológico» de la guía (NOMAD#436, punto 7) y lleva el mismo velo
que en «Así funciona» (`#velo-s5a`).

## La voz

Kore, `gemini-3.1-flash-tts-preview` (`piezas/ia/voz.py`), con el estilo «Locuta un vídeo corto para
redes, cercana y con energía tranquila, con naturalidad de conversación real, en español de España; Nomad
se pronuncia «nómad»:» (lo de antes de los dos puntos no se lee). Tres tomas por frase, recortadas con
`../lanzamiento-trazo/recortar-voz.py` y transcritas con faster-whisper (medium): **las quince dicen todas
sus palabras.** Se eligió por medida, no de oído:

| frase | toma | dura (1×) | por qué |
|---|---|---|---|
| v1 | b1-1 | 2,47 s | la pregunta sube y «te necesitamos» baja; las otras dos, casi planas |
| v2 | b2-1 | 7,36 s | la más corta, y la única que whisper puntúa «iPhone y, para» (para 0,14 s; las otras, 0,30-0,36 y con punto) |
| v3 | b3-1 | 3,54 s | la más ceñida, y acaba bajando; para 0,29 s antes de la «y» (las otras, 0,37 y 0,43), el rasgo del TTS que ya describe «Así funciona» |
| v4 | c4-3 | 3,84 s | «…antes de que salga», regrabada tras la revisión: la más corta de tres, y acaba bajando (−4,4 semitonos) |
| v5 | b5-2 | 2,86 s | la b5-3 va a 6,7 sílabas por segundo (7,7 a 1,15×), demasiado deprisa para la llamada; la b5-1 sube +6,5 al final |

La voz se acelera con `atempo`, como en «Así funciona». **Nadie la ha oído todavía**: lo decide el oído
del dueño, en el altavoz del móvil y con auriculares.

## La música y la mezcla

La de «Un trazo», con la cadena de «Así funciona» (`mezclar.sh`). Aquí la pista sobra (60,7 s para 25 a
1×), así que **no hay junta**: empieza **9 compases dentro** (36 negras justas, 28,830 s), con un fundido
de entrada de 0,3 s. Así su último acorde (el 51,25 de la pista) cae en 22,42 a 1×, justo cuando Kore
acaba «con los pasos», y la rejilla de negras de «Así funciona» vale tal cual para los latidos. En el
28,83 la pista no está en ningún bajón (−15 dB, subiendo a −10 en el 29). Se miraron antes las juntas de
9 y 10 compases desde el principio: el croma no pasaba de 0,79 (en «Así funciona», 0,916), y empezar
dentro de la pista evita la junta entera.

Medido: **−15,8 LUFS, pico −3,7 dBFS, LRA 1,8 LU**, loudnorm lineal, y las cinco frases enteras en la pista
de voz. Entre S4 y S5 (12,8-13,25 s) la música cae unos 10 dB: es un final de frase de la propia pista,
como la pausa del segundo 5 que ya conoce «Así funciona», y vuelve con «Si eres». Está medido, no oído.

## Cómo se rehace

```bash
METRAJE=<carpeta> python3 -I cortar-tomas.py tomas.json   # las tomas (una vez)
bash mezclar.sh                                           # assets/sonido.m4a, si cambian voz o tiempos
bash render.sh                                            # el vídeo en salida/ y revision/*.png
bash portada.sh ../../../salida/nomad-beta-android-portada.jpg
```

`render.sh` pasa `hyperframes check`, saca un fotograma por escena a `revision/` y dos con las zonas que
tapa TikTok dibujadas encima, y renderiza. `assets/motor.js` es la copia del de `../asi-funciona/`, sin
cambios.

## Lo que queda a la vista, y es sabido

- **La letra de la app no se lee entera** dentro de la pantalla, como en los demás: se leen los títulos y
  la forma de cada pantalla.
- **El museo trata de usted** en «Cómo llegar» (toma s5b; NOMAD#436, punto 8).
- **La portada del viaje dice «Faltan 23 días»**, la fecha de la grabación.
- **Las personas de la escena 3 van a 4 px** y no a 5: a su tamaño, con 5 la cabeza se empastaba. Quedan a
  2 px unas de otras, y en el rebote se tocan los hombros: se leen como una fila de gente.
- **Las tomas son de la app de iPhone**, con Apple Maps y un McDonald's en el mapa del plan (s4), en un vídeo
  para quien tiene Android. El vídeo no dice que sean de Android; grabarlas en un Android sería lo limpio.
- **«Te lo cuenta al oído» está comprobado en iPhone.** En Android la audioguía con la voz por defecto ya se
  quedó muda una vez sin explicación (NOMAD#391); el mensaje a los testers pide que avisen si no suena.
- **Las normas de marca de Android piden que su equipo apruebe cada pieza** que nombre Android o Google
  («All creatives that include or reference Android or Google trademarks must be reviewed and fully approved
  by the Android brand team», developer.android.com/distribute/marketing-tools/brand-guidelines; tardan al
  menos una semana). La casa se ha quedado hasta ahora en el ™ y la atribución. Pedirla o no es del dueño.

## Lo que dijo la revisión (4-nov)

Cuatro revisores (líneas y dibujos; voz, música y sincronía; lo que se afirma y las normas; fluidez y lectura),
cada uno con un verificador que intentó tumbar sus hallazgos. De 29, 14 confirmados, ninguno de los que rompen
el vídeo, y arreglados todos:

- «antes que nadie» → «antes de que salga», en la voz (otra toma de Kore), en pantalla y en el post.
- La cabecera y el cierre decían «Prueba cerrada de Android», sin ™ en la cabecera: ahora «Para Android™», y la
  portada igual.
- El «18+» tocaba el aro de dentro en el rebote y en los latidos: a 112 en vez de 124.
- Dos tramos quietos: 0,53 s en S3 (la respiración de las personas llega ahora hasta los días) y 0,40 s en S5
  (un latido corto antes de recoger el sello).
- PUBLICAR: la etiqueta de contenido comercial además de la de IA (la música también es de IA), la portada
  no es «lo mismo» que el primer fotograma, fuera los emojis que no señalan, el mensaje pide no salir del grupo
  ni de la prueba y avisar si la audioguía no suena, y el saldo de IA era menor que el techo (#303).
- Este README: lo que decía de las tomas de v2 y v3 no casaba con lo medido.

Lo que se dejó, con el verificador en contra: el collar de S2 se ve solo cinco fotogramas al recogerse, las
ondas de los auriculares cruzan las almohadillas dos fotogramas al brotar, y el lado derecho de la pantalla
cruza un fotograma el logo que la cola aún no ha recogido. Los tres vienen tal cual de «Así funciona».
