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
| t1 | La foto, 9:16 (x 306-1755 de 1932×2576) | Las manos suben con el móvil y el estuche, sacan un auricular y lo llevan a la oreja | 0,4-4,55 s a ×1,2 |
| t2 | La misma | Ya con los auriculares, la mirada sube despacio del pórtico a las torres. Sin manos | 0-5,46 s, con Kore y Puck |
| t3 | Las torres (x 564-1564, y 300-2078) | La mirada sube por las torres hasta las puntas. Sin manos | 2,12-8 s, con Charon: empuja hacia las puntas y se queda en ellas |

En t1 la mano sale por la derecha a los 4,55 s: ahí se corta, que es justo cuando el ruido
se apaga. El corte y el silencio a la vez se leen como «se lo ha puesto».

**Dos defectos de t1, por si alguien los ve**:
- Entre los 3,9 y los 4,2 s, el auricular de la mano parece llevar un palo negro. A ×1,2
  son unas dos décimas.
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
gente (assets/gente.m4a) +4 dB hasta 3,458 s
  → a partir de ahí, paso bajo a 220 Hz dos veces y −20 dB, en 0,12 s: la cancelación de ruido
Kore a 3,63 s · Puck a 6,35 s · Charon a 8,92 s (las tres sin silencios delante ni detrás)
todo junto hasta 14,8 s, loudnorm a −14 LUFS
```

El fundido de 0,12 s es lo que hace que suene a cancelación y no a corte de edición.

## Lo que es provisional

**Las tres frases no son de la app**: son para ver el montaje, generadas con
`piezas/ia/voz.py` con las mismas tres voces. Aun así, lo que dicen está comprobado:

- Kore: «Estás delante de la fachada de la Pasión.»
- Puck: «Gaudí quería que diera miedo.» Lo dejó escrito así: dura, desnuda, como hecha de
  huesos, y que diera miedo (Cuaderno 07 de la propia basílica,
  <https://sagradafamilia.org/documents/20142/1000558/Cuaderno_07.pdf/5cde86a6-368b-e11b-93c9-842465975f66>).
- Charon: «Busca el cuadrado de números: cada fila suma 33, la edad de Cristo.» Es el
  cuadrado de Subirachs junto al beso de Judas. Suman 33 las filas, las columnas y las
  diagonales (<https://blog.sagradafamilia.org/en/the-magic-square-on-the-passion-facade/>).

La de Puck salió mal en dos de cuatro tomas: una vez «diga miedo», otra «diera a mí». Por
eso cada toma se transcribe antes de usarla.

Lo que se publica es **la narración real de la parada**, sacada de la app y comprobada
frase a frase (`piezas/videos/RODAJE.md`, clip 2).

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
