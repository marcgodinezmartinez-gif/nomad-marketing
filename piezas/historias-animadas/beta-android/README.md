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
| 5 | Si eres mayor de dieciocho, pruébala gratis antes que nadie. | Pruébala gratis, / antes que nadie. | un sello que se traza en círculo, con «18+» dentro |
| 6 | Comenta «Android» y te escribimos con los pasos. | (el cierre) | el icono, el nombre y un bocadillo que se traza desde su pico alrededor de «Comenta / ANDROID»; debajo, «y te escribimos con los pasos», «Prueba cerrada de Android™ · Mayores de 18» y los créditos de marca |

Lo que dice cada frase, comprobado: la app es para mayores de 18 desde el 9-oct (NOMAD#385); Google pide
12 testers en la prueba cerrada durante 14 días seguidos (NOMAD, `docs/GOOGLE-PLAY.md` §8); «te monta el
viaje», «día a día» y «te lo cuenta al oído» son frases de «Así funciona», que ya se comprobaron contra la
app. **«Gratis» sólo es verdad si el grupo `nomadapp-testers` está en Pruebas de licencias** de Play
Console: es el paso 0 de `PUBLICAR.md`, y sin él el vídeo no se sube.

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
| v2 | b2-1 | 7,36 s | la única que dice «iPhone y, para» sin parar (las otras hacen punto tras «iPhone») |
| v3 | b3-1 | 3,54 s | la más ceñida, sin pausas, y acaba bajando |
| v4 | b4-2 | 3,80 s | acaba bajando; la b4-3 sube al final (+3,2 semitonos) y sonaba a pregunta |
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

Medido: **−15,7 LUFS, pico −3,7 dBFS, LRA 1,8 LU**, loudnorm lineal, y las cinco frases enteras en la pista
de voz. Está medido, no oído.

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
- **Las personas de la escena 3 van a 4 px** y no a 5: a su tamaño, con 5 la cabeza se empastaba.
