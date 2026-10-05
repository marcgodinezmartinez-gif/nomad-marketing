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
todo junto hasta 26,8 s, loudnorm a −14 LUFS
```

El fundido de 0,12 s es lo que hace que suene a cancelación y no a corte de edición.

## Lo que dicen las voces: el texto de la app

Desde el 6-oct, **el texto es el de la parada de la app**, leído de la grabación del dueño
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

## La segunda mitad: la app (6-oct)

De la grabación del dueño, `ScreenRecording_10-05-2026_19-15-50` (35 s, 1206×2622, HEVC,
sin sonido): del itinerario al tour, la espera de «Diseñando tu tour» (13 s), la parada y
el dato curioso. Él mismo lo pidió: *«no creo que lo mejor sea ponerlo a cámara rápida sino
recortarlo con lo necesario y útil, e incluso usar screenshots»*. Primero se montó con tres
trozos de vídeo dentro del móvil de la casa. En la versión 2 se queda en **tres capturas
fijas** de esa grabación, sin barra de estado, a 940 de ancho dentro de la ventana:

| Captura | Fotograma | Qué se ve en la ventana |
|---|---|---|
| `app-parada.png` | 26,0 s | La parada desde y=330: el título, «Monumento» y el reproductor de la audioguía. Se para justo antes de la caja de «Colócate aquí», que dice «la cera» |
| `app-dato.png` | 33,6 s | El dato curioso abierto, centrado en y=800 |
| `app-chat.png` | 32,4 s | El chat de la parada pegado abajo: las preguntas sugeridas y «Pregunta o envía una foto…» |

**Lo que falta**: el chat se ve, pero nadie le pregunta nada. Una grabación con una pregunta
escribiéndose y la respuesta entera sustituiría a la tercera captura.

## La versión 2: el diseño (6-oct)

El dueño vio la primera *«demasiado cutre»* y pidió algo como *«las presentaciones de Apple,
la publi de Vicio o de Estrella Damm»*. Probó a pedírselo a Claude Design con un prompt y
salió *«bastante mal también»*. Así que se rehizo aquí. El porqué de cada cambio está
en la cabecera de `index.html`:

- **Fuera las capas**: ni velos oscuros por todas partes, ni cápsula, ni móvil con marco.
- **El fondo es la crema de la app (#FEFCF9)** y el texto, noche. El verde es el de la app
  (#106A63, medido en la captura). El menta de la casa no llega a 3:1 sobre crema.
- **La cancelación de ruido se ve.** Con la gente, la imagen va a sangre. Al ponerse los
  auriculares, el mundo se recoge en una ventana de 940×700 con esquinas de 40, y alrededor
  aparece la crema. Está hecho con una máscara (`clip-path`) sobre el vídeo a pantalla
  completa, así que no se reencuadra nada.
- **Los subtítulos se encienden palabra a palabra.** Los tiempos de cada palabra se sacan de
  la propia voz con `faster-whisper`, y la frase entera se ve tenue desde el principio.
- **Una idea por plano, letra grande y centrada**: titular arriba (230-430), ventana en medio
  (450-1150), voz y frase debajo (1188-1430). Todo cabe en la zona segura.

Tiempos: el gancho hasta 2,792 s; las voces, de 2,962 a 16,032; la app desde 16,4 (parada),
18,7 (dato) y 21,2 (chat); el cierre en crema, de 23,4 a 26,8.

## Al publicar

**Etiqueta de IA en Instagram**: Meta exige marcar el vídeo fotorrealista y el audio
realista creados o alterados digitalmente (*«We'll require people to use this disclosure
and label tool when they post organic content with a photorealistic video or
realistic-sounding audio that was digitally created or altered, and we may apply penalties
if they fail to do so»*, Meta, febrero de 2024). Aquí lo son las dos cosas.

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
