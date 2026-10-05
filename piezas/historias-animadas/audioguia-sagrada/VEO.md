# Los planos con IA del reel de la audioguía (5-oct)

El dueño lo quería sin salir de casa: *«¿cómo lo podemos hacer sin movernos de casa en
absoluto? ¿usamos una IA para replicar lo que pienso?»*. Lo que pensaba, hasta el segundo
14: una grabación en primera persona, como desde unas gafas, con los auriculares y el móvil
en la mano; mucho ruido de gente que se corta al ponerse los auriculares; empieza la voz,
«¿Y si tus viajes empiezan a sonar así?»; y la app contando la parada mientras se mira,
con las tres voces y «y tú eliges quién te la cuenta» en pantalla.

Hecho con **Veo 3.1 Fast** por la API de Gemini (`piezas/ia/veo.py`), en vertical, a 1080p y
8 s por toma, que es lo único que admite a 1080p.

## La regla que salió de la primera toma

**Sólo con texto, Veo se inventa la basílica.** La primera toma (sin foto) sacó bien las
manos, el estuche, el móvil con la pantalla apagada y un ruido de gente creíble, pero la
Sagrada Família era una catedral gótica cualquiera con cuatro agujas, y encima con un ojo
de pez de bordes negros. Cualquiera de Barcelona lo ve. **Las tomas que se usan salen de
una foto real** como primer fotograma, y Veo sólo la anima: las manos, el movimiento, las
nubes, los pájaros. De aquella primera toma se queda el sonido (`assets/gente.m4a`): es ruido
sin palabras (comprobado transcribiéndolo: no sale ni una).

## Dos versiones el mismo día

1. **Con una foto CC0 de 2017** de la fachada del Nacimiento desde el estanque
   (`banco/fotos/*/f-sagrada-estanque.jpg`). Funcionó, pero salían grúas y faltaban las
   torres centrales de hoy.
2. **Con la foto del dueño**, hecha el 4-oct (`banco/fotos/*/f-sagrada-pasion.jpg`): *«ayer
   pasé por la Sagrada Família y hice esta foto, ¿podríamos usarla?»*. Es la que vale. Sale
   la basílica de hoy, es suya y es de verdad. De las cuatro casi iguales se cogió la más
   nítida, medida en las torres. **Es la fachada de la Pasión, no la del Nacimiento**, así
   que las frases de prueba cambiaron con ella, y la narración real tiene que hablar de la
   Pasión o de la basílica en general.

## Las tomas de la versión 2

| Toma | Primer fotograma | Qué se pidió | Qué se usa |
|---|---|---|---|
| t1 | La foto, 9:16 (x 306-1755 de 1932×2576) | Las manos suben con el móvil y el estuche, sacan un auricular y lo llevan a la oreja | 0,4-3,75 s a ×1,2 |
| t2 | La misma | Ya con los auriculares, la mirada sube despacio del pórtico a las torres. Sin manos | 0-5,46 s, con Kore y Puck |
| t3 | Las torres (x 564-1564, y 300-2078) | La mirada sube por las torres hasta las puntas. Sin manos | 2,12-8 s, con Charon: empuja hacia las puntas y se queda en ellas |

El corte de t1 va a los 3,75 s, con la mano subiendo, y ahí mismo se apaga el ruido. El corte
y el silencio a la vez se leen como «se lo ha puesto». Al principio iba a los 4,55 s, cuando
la mano sale por la derecha, pero el 6-oct se adelantó por el defecto de abajo. De paso, la
voz entra 0,7 s antes.

**Dos defectos de t1, por si alguien los ve**:
- La mano no saca un auricular: levanta el estuche entero, y desde los 3,5 s le cuelga algo
  negro. A partir de 3,8 s es un palo largo, y eso es lo que el corte deja fuera. Lo que
  queda, unas dos décimas, pasa por la correa del estuche.
- La pantalla apagada del móvil refleja una silueta oscura. Se lee como el reflejo de
  quien mira, que es lo que sería de verdad.

Si molestan, se repite la toma (0,96 $).

Los prompts de la versión 2, tal cual (en inglés, que es como mejor responde el modelo):

**t1**:
> Vertical first-person POV video at eye level, as if filmed with smart glasses, standing on
> the pavement in front of the Passion façade of the Sagrada Família in Barcelona on an
> overcast day, looking up at it. Keep the basilica, its towers and the sky exactly as they
> are in the image. The viewer's own hands rise into the bottom of the frame: the left hand
> holds a black smartphone with a dark screen; the right hand holds a small open white
> charging case of wireless earbuds, the fingers take one white earbud and lift it up and
> out of frame towards the right ear. Then the gaze rises slowly up the towers. Natural,
> gentle handheld motion. Photorealistic, natural colours, normal lens, no distortion.
> Audio: loud, dense crowd chatter of tourists in many languages, footsteps and city noise
> all around. No music, no narration.
>
> NEGATIVO: text, subtitles, captions, logos, watermark, vignette, black borders, fisheye,
> distorted hands, extra fingers, cartoon, illustration, CGI look, music, changing the shape
> of the building, blue sky

**t2**:
> Vertical first-person POV video at eye level. The viewer now has earbuds in and stands
> still on the pavement in front of the Passion façade of the Sagrada Família in Barcelona,
> quietly contemplating it on an overcast day. Very slow, smooth tilt upwards from the
> sculpted portal and its bone-like columns towards the towers, with a slight push-in. Grey
> clouds drift slowly, a couple of birds cross the sky. Keep the basilica, its towers and the
> sky exactly as in the image. Photorealistic, natural colours, calm, normal lens.
> Audio: soft, muffled ambience only. No music, no narration.
>
> NEGATIVO: hands, fingers, phone, text, subtitles, captions, logos, watermark, vignette,
> black borders, fisheye, distortion, changing the shape of the building, blue sky, cartoon,
> CGI look, music

**t3**: el mismo molde, con *«looking up at the bell towers of the Passion façade… The gaze
slowly travels up the towers to their colourful tips… Keep the towers, the cranes and the
sky exactly as in the image»*.

**Lo que costó**: siete tomas de 8 s a 0,96 $: cuatro de la versión 1 y tres de la 2, en
total **6,72 $**. Una de 6 s a 1080p la rechazó la API antes de generar (1080p sólo a 8 s)
y no se cobra. Las voces de prueba, céntimos.

## El sonido

```
gente (assets/gente.m4a) +4 dB hasta 2,792 s
  → a partir de ahí, paso bajo a 220 Hz dos veces y −20 dB, en 0,12 s: la cancelación de ruido,
    que se apaga del todo en la segunda mitad
Kore a 2,962 s · Puck a 7,838 s · Charon a 11,354 s (sin silencios delante ni detrás, a ×1,12)
la segunda mitad (desde 16,4 s) sin voz: la música se pone en Instagram
todo junto hasta 28,6 s, loudnorm a −14 LUFS
```

El fundido de 0,12 s es lo que hace que suene a cancelación y no a corte de edición.

## Lo que dijeron las voces hasta la versión 4: el texto de la app

Del 6-oct hasta la versión final, **el texto fue el de la parada de la app**, leído de la grabación del dueño
(«La historia» y el dato curioso de la Pasión):

- Kore: «Esta fachada representa la agonía, crucifixión y muerte de Jesús.»
- Puck: «Las columnas inclinadas recuerdan a huesos o troncos secos.»
- Charon: «Suma los números del cuadrado mágico: siempre da 33, la edad de Cristo.»

Comprobado: las esculturas son de Subirachs, el cuadrado está junto al beso de Judas y suma
33 en filas, columnas y diagonales
(<https://blog.sagradafamilia.org/en/the-magic-square-on-the-passion-facade/>).

La grabación de la app viene sin sonido, así que las frases se generan con `piezas/ia/voz.py`,
con las mismas tres voces. Van a ×1,12 porque a su ritmo la primera mitad pasaba de 17 s.
Cada toma se transcribe antes de usarla: Puck dijo una vez «diga miedo» y otra «diera a mí».

**La app tiene tres fallos en esa parada**, y la voz dice la versión buena:
- «Colócate aquí: En **la cera** de Carrer de Sardenya…», donde tendría que decir «la acera».
- «**Sume** los números…», de usted, cuando el resto de la app habla de tú.
- «…del **cuadro** mágico…», donde tendría que decir «cuadrado».
La pantalla del dato curioso sí sale tal cual en el reel. Hasta que la app los arregle, ahí
se lee «Sume» y «cuadro».

## Tres versiones el mismo día, y la que vale (6-oct)

1. **Velos oscuros, cápsula y móvil con marco** sobre la foto: *«se ve demasiado cutre»*.
2. **Estilo Apple** (fondo crema, la imagen recogida en una ventana con zoom, la app en
   capturas recortadas): *«sigue siendo horrible. El zoom innecesario a la foto hace que se
   vea mal; el recortar y no mostrar el móvil completo también es un error»*. Antes, el dueño
   probó a pedírselo a Claude Design con un prompt, y salió *«bastante mal también»*.
3. **La que pidió él**, y es la buena:
   - *«La primera parte, con la imagen al completo, el texto legible en tarjetas como las que
     solemos usar en la app, de color blanco roto; el verde de la app para el icono de que
     suena audio y el nombre del audio, y los otros textos en negro.»*
   - *«La segunda, un teléfono y dentro un trozo del vídeo donde se muestre lo verdaderamente
     relevante: no capturas, mini vídeos enseñando.»*

### Cómo está hecha la 3

- **La imagen, a sangre y quieta.** Ni máscara, ni zoom, ni velos: sólo se mueven las tarjetas.
- **Las tarjetas son las de la app**: blanco roto (#FEFCF9, la crema de la app), borde fino,
  esquinas de 34 y sombra para despegarlas de la foto.
  - Arriba, el titular en serif negro: «¿Y si tus viajes empiezan a sonar así?» y, con la
    segunda voz, «Y tú eliges quién te la cuenta.».
  - Abajo, la tarjeta de la audioguía. Lleva el icono que suena (un círculo verde con barras
    que se mueven sólo mientras habla la voz), el nombre de la voz en verde y «Audioguía ·
    Fachada de la Pasión» en gris. Debajo, la frase en negro: cada palabra se enciende cuando
    la dice la voz, con los tiempos sacados de la propia voz con `faster-whisper`.
  - El verde es el de la app (#106A63, medido en la captura).
- **El móvil, entero** (664×1436, la pantalla a 624), sobre la última imagen de las torres
  desenfocada. Dentro, cinco trozos de la grabación del dueño a su velocidad
  (`assets/pantalla.mp4`, 9,3 s):

| Trozo | De la grabación | Qué enseña |
|---|---|---|
| 0-1,6 s | 21,5-23,1 s | El mapa del tour y la primera parada que sube |
| 1,6-3,0 s | 24,2-25,6 s | «Siguiente parada» dos veces, hasta la Pasión |
| 3,0-4,8 s | 27,6-29,4 s | La historia de la Pasión, deslizando hasta el dato curioso |
| 4,8-6,9 s | 32,9-34,2 s, y 0,8 s quieto | El toque que abre el dato curioso |
| 6,9-9,3 s | 30,0-31,8 s, y 0,3 s quieto | El chat de la parada: las preguntas sugeridas y «Pregunta o envía una foto…» |

  Encima del móvil, otra tarjeta: «Te lleva de parada en parada.», «Con su dato curioso.» y
  «Y le preguntas lo que quieras.».
- La barra de estado se tapa como en Córdoba: `crop=518:14:0:94,vflip,scale=624:83,gblur=sigma=12`
  sobre la grabación a 624×1356.

**La portada y el cierre (6-oct, tarde).** El dueño vio la portada en el estilo del feed
(su foto, VELO_FOTO, «Barcelona · la Sagrada Família», el título en serif blanca y la
marca) y pidió *«fusionarla con algún efecto con el vídeo y usarla de cierre también, sin la
cajita»*, y *«Muy pronto»* en vez de «Llega en octubre». Así queda:
- **El primer fotograma del reel es la portada**, quieta 0,8 s con el ruido de la gente.
  Como la toma de las manos sale de esa misma foto, al arrancar el vídeo la foto cobra vida
  sin corte. El kicker y la marca se van, y el título se queda hasta que se apaga el ruido.
- **El cierre es la misma foto**, que pasa de desenfocada a nítida sobre las torres
  desenfocadas, con «Lista de espera abierta», «Muy pronto.», «Tu primer viaje por 1,99 €*»
  (en menta, como en el feed), la nota y la marca. El velo es más oscuro que VELO_FOTO,
  porque sobre el gris de ese día el menta no llegaba a 3:1.
- La portada para subir a Instagram es ese primer fotograma
  (`salida/reel-sagrada-portada.jpg`).

Tiempos: la portada quieta hasta 0,8 s; el gancho hasta 3,592; las voces, de 3,762 a
16,832; el móvil, de 17,2 a 26,2; el cierre, hasta 29,4. El sonido es el de arriba
desplazado 0,8 s.

**Lo que falta**: el chat se ve, pero nadie le pregunta nada. Una grabación con una pregunta
escribiéndose y la respuesta entera sustituiría al último trozo. Y en la parada de la Pasión
se lee, pequeño, «En la cera» (issue #10).

## La versión final (6-oct, noche)

Con la cuarta, el dueño pidió tres cambios *«y con esos cambios daría el reel por
finalizado»*:

1. **Otro texto para las voces.** *«No me gusta el texto que leen las voces; que lean algo
   más y que sea interesante.»* Ya no es el texto de la app. Son tres detalles de la Pasión,
   comprobados:
   - Kore: «Gaudí la dibujó en 1911, enfermo en Puigcerdà y convencido de que se moría.
     Quería que diera miedo.» Fiebres de Malta, hizo testamento y la proyectó entonces
     (<https://blog.sagradafamilia.org/en/?p=4176>,
     <https://bellesguardgaudi.com/en/one-of-the-first-works-one-of-the-last/>). Lo del
     miedo está en el Cuaderno 07 de la basílica.
   - Puck: «Fíjate en los soldados romanos: sus cascos son las chimeneas de La Pedrera.»
     (<https://www.sagradafamiliatickets.info/hidden-symbols-passion-facade-sagrada-familia-decoder>)
   - Charon: «Y junto a la Verónica, ese hombre que toma notas es el propio Gaudí.» Es el
     homenaje de Subirachs
     (<https://homepages.bluffton.edu/~SULLIVANM/spain/barcelona/sagrada/sagradapassion2.html>).
   El dato del cuadrado mágico, que es el de la app, se queda en el móvil.
2. **Música de fondo sin derechos de nadie**: generada con **Lyria 3** por la API de Gemini
   (`lyria-3-clip-preview`, 30,8 s, instrumental, con la marca de agua SynthID). Prompt:
   *«Instrumental background music for a 30-second travel app video about an audio guide in
   Barcelona. Warm, cinematic and minimal: soft felt piano and gentle nylon-string Spanish
   guitar, light airy strings, Mediterranean feel, calm, curious and elegant, about 80 BPM,
   no drums, no vocals. Starts softly, builds a little in the middle, and resolves gently at
   the end.»* Entra con la cancelación de ruido: a 0,22 debajo de las voces (unos 13 dB por
   debajo, y el transcriptor saca las tres frases enteras de la mezcla), sube a 0,52 con el
   móvil y se funde al final. **Al subirlo no se le añade música de Instagram**: ya la lleva.
3. **El móvil, sólo con la parada 3.** *«Se ve feo que pase de la parada 1 a la 3 así, como
   deprisa.»* `assets/pantalla.mp4` son cuatro trozos montados uno a uno, para saber dónde
   cae cada corte: la parada (25,5-27,6 de la grabación, 0-2,43 en el clip), la historia
   (27,6-29,4, hasta 4,23), el dato curioso (32,9-34,2 y 0,8 s quieto, hasta 6,63) y el chat
   (30,0-31,8 y 0,3 s quieto, hasta 8,93). El primer texto pasa a «Cada parada, con su
   audioguía.».

Tiempos: la portada quieta hasta 0,8 s; la cancelación a 3,592; Kore a 3,762, Puck a
11,165 y Charon a 15,578 (a ×1,06), hasta 20,101; el móvil de 20,551 a 29,151; el cierre,
hasta 32,35. La tarjeta de la audioguía crece a 340 de alto (de 1130 a 1470), porque la
frase de Kore ocupa tres líneas.

Para rehacer el sonido sin volver a generar nada están en `assets/` la música, las tres
voces (`voz-k/p/c.m4a`), la gente y la mezcla final (`sonido-final.m4a`). El vídeo final es
el render de `index.html` con `sonido-final.m4a` encima.

**El pie** (con «Muy pronto», como pidió el dueño):

> ¿Y si tus viajes empiezan a sonar así? Nos plantamos delante de la fachada de la Pasión y
> se la pedimos a NOMAD.
>
> Gaudí la dibujó enfermo, convencido de que se moría. Los soldados llevan de casco las
> chimeneas de La Pedrera. Y junto a la Verónica, el que toma notas es el propio Gaudí. Cada
> parada, con su audioguía, su dato curioso y un chat al que preguntarle lo que quieras. La
> voz, la eliges tú.
>
> Muy pronto. Desde 2,99 € el viaje entero, sin suscripción, y en la lista el primero por
> 1,99 €, dure lo que dure. El enlace, en la bio.
>
> #sagradafamilia #barcelona #gaudi #audioguia #viajar #viajes

## Al publicar

**Etiqueta de IA en Instagram**: Meta exige marcar el vídeo fotorrealista y el audio
realista creados o alterados digitalmente (*«We'll require people to use this disclosure
and label tool when they post organic content with a photorealistic video or
realistic-sounding audio that was digitally created or altered, and we may apply penalties
if they fail to do so»*, Meta, febrero de 2024). Aquí lo son las dos cosas.

**Dónde está el interruptor** (buscado el 5-oct, guía de Storrito:
<https://storrito.com/help-center/how-to-label-ai-generated-content/>): en el reel, en la
última pantalla antes de publicar, dentro de «Configuración avanzada»; en la historia, en el
menú de los tres puntos del editor, arriba a la derecha. **Las dos cosas se marcan antes de
publicar**, en la cuenta de NOMAD y en la personal.

**Lo demás, como se publicó Córdoba** (`piezas/videos/RODAJE.md`, «Cómo se publica»: el reel
con su portada, y la historia subida desde el carrete con adhesivo de enlace), con dos
cambios:
- **Sin música de Instagram**: el reel ya lleva la suya.
- **El adhesivo, pequeño y justo debajo del móvil** (y ≈ 1590-1670). Más arriba tapa la barra
  del chat («Pregunta o envía una foto…», en y ≈ 1530) justo cuando la tarjeta dice «Y le
  preguntas lo que quieras». Más abajo lo tapa la barra de responder.

Portada: `salida/reel-sagrada-portada.jpg`. UTM `reel-sagrada` en @app.nomad y
`reel-sagrada-personal` en la cuenta del dueño.

## Y Kling (5-oct)

El dueño quiso probar Kling AI (Video 3.0) para el plano de las manos, con su foto vertical
de primer fotograma. Lo que hay que saber antes de usar nada de ahí:

- **Los vídeos del plan gratis no se pueden publicar**: llevan la marca de Kling y, según las
  guías de precios, son sólo para uso personal. Recortar la marca no lo arregla, sólo
  esconde de dónde sale. La prueba gratis sirve para comparar con Veo, y para nada más.
- **Si se paga**, antes hay que comprobar en la página de precios que el plan quita la marca
  **a 1080p** (alguno, según esas guías, sólo a 720p) y que da uso comercial. A 720p no
  compensa frente a Veo a 1080p.
- **La cuenta**: 1080p y 5 s son 60 créditos en Video 3.0 (pantalla del dueño, con el audio
  propio encendido). Los 660 del plan de 7 € dan para unos 11 planos al mes, de 0,15 $ el
  segundo a 0,12 $ en Veo Fast. Es parecido, así que lo que decide es cuál hace mejor las
  manos.

**Lo que salió (6-oct)**: peor que Veo, y el dueño lo vio antes que nadie: *«muy flojito, la
imagen de la Sagrada Família no tiene animación ni nada»*. Medido:
- **La basílica no se mueve.** La diferencia media entre fotogramas en la mitad de arriba es
  de 0,53, frente a 12,82 en la toma de Veo. Son unas manos pegadas encima de una foto quieta.
- **Las manos no sacan el auricular**: suben con el móvil y el estuche, lo tocan y se van.
- **Lleva la marca de agua «KlingAI 3.0»** abajo a la derecha.

**Parte es culpa del consejo**: se le puso la misma foto de fotograma inicial y final para que
no se inventara la basílica, y con dos extremos iguales Kling entiende que la cámara no se
mueve. Si se vuelve a probar, sólo con el inicial. Con este resultado no se paga el plan, y la
toma de las manos sigue siendo la de Veo.
