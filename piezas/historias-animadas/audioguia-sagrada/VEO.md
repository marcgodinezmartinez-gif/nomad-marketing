# Los planos con IA del reel de la audioguía (5-oct)

El dueño lo quería sin salir de casa: *«¿cómo lo podemos hacer sin movernos de casa en
absoluto? ¿usamos una IA para replicar lo que pienso?»*. Lo que pensaba, hasta el segundo
14: una grabación en primera persona, como desde unas gafas, con los auriculares y el móvil
en la mano; mucho ruido de gente que se corta al ponerse los auriculares; empieza la voz,
«¿Y si tus viajes empiezan a sonar así?»; y la app contando la parada mientras se mira,
con las tres voces y «y tú eliges quién te la cuenta» en pantalla.

Hecho con **Veo 3.1 Fast** por la API de Gemini (`piezas/ia/veo.py`), en vertical, a 1080p y
8 s por toma, que es lo único que admite a 1080p.

## Lo que se aprendió en la primera toma

**Sólo con texto, Veo se inventa la basílica.** La primera toma (sin foto) sacó bien las
manos, el estuche, el móvil con la pantalla apagada y un ruido de gente creíble, pero la
Sagrada Família era una catedral gótica cualquiera con cuatro agujas, y encima con un
ojo de pez con bordes negros. Cualquiera de Barcelona lo ve. **Las tres tomas que se
usan salen de una foto real** como primer fotograma: `banco/fotos/historia/f-sagrada-estanque.jpg`,
CC0, la fachada del Nacimiento desde la plaça de Gaudí con el estanque. De esa primera
toma sólo se usa el sonido (`assets/gente.m4a`), porque es ruido sin palabras (comprobado
transcribiéndolo: no sale ni una).

**La foto es de 2017**: con grúas, y sin las torres centrales que hoy asoman por detrás de
las del Nacimiento. Si la narración habla de la torre de Jesucristo, no casa con la
imagen y hace falta una foto de 2025 o 2026.

## Las tomas

| Toma | Primer fotograma | Qué se pidió | Qué se usa |
|---|---|---|---|
| 1 | — | La plaça de Gaudí llena, las manos sacan un auricular del estuche | Sólo el ruido de la gente |
| 1b | La foto entera, 9:16 | Lo mismo, desde la foto | 0,3-4,3 s a ×1,2: las manos, el auricular hasta la oreja |
| 2 | La foto entera, 9:16 | Ya con los auriculares, la mirada sube despacio del estanque a las torres. Sin manos | 0-6,2 s, con Kore y Puck |
| 3 | Las cuatro torres, recortadas de la foto | La mirada sube por las torres hasta las puntas. Sin manos | 0-6,4 s, con Charon |

En la 1b la mano se queda arriba a la derecha con el auricular y no llega a metérselo: se
corta ahí, a los 3,33 s, que es justo cuando el ruido se apaga. El corte y el silencio a la
vez se leen como «se lo ha puesto».

Los prompts, tal cual (en inglés, que es como mejor responde el modelo):

**1b** (y la 1, igual pero sin foto):
> Vertical first-person POV video at eye level, as if filmed with smart glasses, standing at
> the edge of the pond in the Plaça de Gaudí in Barcelona, looking across the water at the
> Nativity façade of the Sagrada Família. Keep the basilica, the trees and the pond exactly
> as they are in the image. A few tourists walk past along the edge of the pond. The
> viewer's own hands rise into the bottom of the frame: the left hand holds a black
> smartphone with a dark screen; the right hand holds a small open white charging case of
> wireless earbuds, the fingers take one white earbud and lift it up and out of frame
> towards the right ear. Then the gaze rises slowly towards the four spires. Natural,
> gentle handheld motion. Photorealistic, natural colours, normal lens, no distortion.
> Audio: loud, dense crowd chatter of tourists in many languages, footsteps and city noise
> all around. No music, no narration.
>
> NEGATIVO: text, subtitles, captions, logos, watermark, vignette, black borders, fisheye,
> distorted hands, extra fingers, cartoon, illustration, CGI look, music, changing the shape
> of the building

**2**:
> Vertical first-person POV video at eye level. The viewer now has earbuds in and stands
> still at the edge of the pond in the Plaça de Gaudí in Barcelona, quietly contemplating
> the Nativity façade of the Sagrada Família. Very slow, smooth tilt upwards from the pond
> towards the four spires, with a slight push-in. Leaves sway in a light breeze, gentle
> ripples on the water, a couple of birds cross the sky. Keep the basilica, the trees and
> the pond exactly as in the image. Photorealistic, natural colours, calm, normal lens.
> Audio: soft, muffled ambience only. No music, no narration.
>
> NEGATIVO: hands, fingers, phone, text, subtitles, captions, logos, watermark, vignette,
> black borders, fisheye, distortion, changing the shape of the building, cartoon, CGI
> look, music

**3**: el mismo molde, con *«looking up at the four bell towers of the Nativity façade…
the gaze slowly travels up the towers to their tips… A few birds fly past high in the
sky»* y el recorte de las torres (x 708-1468, y 150-1501 de la miniatura de 1920 px).

**Lo que costó**: cuatro tomas de 8 s a 0,96 $ = **3,84 $**. Una quinta, de 6 s a 1080p,
la rechazó la API antes de generar (1080p sólo a 8 s) y no se cobra. Las voces de
prueba, céntimos.

## El sonido

```
gente (assets/gente.m4a) +4 dB hasta 3,333 s
  → a partir de ahí, paso bajo a 220 Hz dos veces y −20 dB, en 0,12 s: la cancelación de ruido
voz 1 a 3,50 s · voz 2 a 6,58 s · voz 3 a 9,53 s (las tres sin silencios delante ni detrás)
todo junto, loudnorm a −14 LUFS
```

El fundido de 0,12 s es lo que hace que suene a cancelación y no a corte de edición.

## Lo que es provisional

**Las tres frases** («Estás delante de la fachada del Nacimiento» / «Es la única que Gaudí
vio levantarse» / «Cuando le preguntaban cuándo la acabaría, decía: "Mi cliente no tiene
prisa"») **no son de la app**: son para ver el montaje, generadas con `piezas/ia/voz.py`
con las mismas tres voces. Lo que se publica es la narración real de la parada, sacada de
la app y comprobada frase a frase (`piezas/videos/RODAJE.md`, clip 2).

## Al publicar

**Etiqueta de IA en Instagram**: Meta exige marcar el vídeo fotorrealista y el audio
realista creados o alterados digitalmente (*«We'll require people to use this disclosure
and label tool when they post organic content with a photorealistic video or
realistic-sounding audio that was digitally created or altered, and we may apply penalties
if they fail to do so»*, Meta, febrero de 2024). Aquí lo son los dos.
