# Las fotos, la voz y la música de «El puente en Viena»

## Las fotos

Diez fotos de Unsplash, todas con «Free to use under the Unsplash License» en su página (leída el 18-nov-2026).
Esa licencia deja usarlas gratis, también con fines comerciales, y no pide atribución. Ninguna es de Unsplash+
(las de pago salen de `plus.unsplash.com` y se descartaron al buscar).

Los recortes son de 1080×1920 y salen del original (4.200 px de ancho), nunca de otro recorte.

| fichero | qué es | autor | página |
|---|---|---|---|
| `graben.jpg` | Las lámparas del Graben | Anton (@uniqueton) | unsplash.com/photos/JE2pF2mcR9g |
| `torre.jpg` | La torre sur de la Catedral de San Esteban | Egemen Şahin (@egemensahiin) | unsplash.com/photos/wvhOnSE8R54 |
| `estrella.jpg` | La estrella «Willkommen» del mercadillo de Schönbrunn | Mario Tuzon (@mazatrazz) | unsplash.com/photos/OvxiucrIIgk |
| `kohlmarkt.jpg` | El Kohlmarkt hacia la puerta del Hofburg | Ahmed Slimene (@ahmed_sl___) | unsplash.com/photos/L1OC2FjR8Wc |
| `catedral.jpg` | La Catedral de San Esteban con el mercadillo, Stephansplatz | Kate K (@kkrut) | unsplash.com/photos/1tpOhNxrJyE |
| `hofburg.jpg` | El Hofburg (la Neue Burg) al anochecer | Dmitrii E. (@dmitriielj) | unsplash.com/photos/ppK1lpIc5Fc |
| `mtplatz.jpg` | Un puesto del mercadillo ante uno de los dos museos, Maria-Theresien-Platz | Andie K (@kolbecka) | unsplash.com/photos/PExw0-jG90o |
| `schonbrunn.jpg` | El árbol y el mercadillo ante el Palacio de Schönbrunn (también es la portada) | Mario Tuzon (@mazatrazz) | unsplash.com/photos/WDrkOQpagfQ |
| `belvedere.jpg` | El Belvedere Superior de noche, con las luces del mercadillo | Dmitrii E. (@dmitriielj) | unsplash.com/photos/FUWKzBdZclQ |
| `karlsplatz.jpg` | La Karlskirche con nieve y las casetas del Art Advent | Scorn Pion (@scornpion) | unsplash.com/photos/5bZ0BJL5_J0 |

Lo que se miró, foto a foto:

- **Que cada una es el sitio que dice su rótulo.** Se reconocen por el edificio. Dos que pedían mirarlas dos veces:
  - `mtplatz.jpg`: su autora la describe como «at Rathaus Wien», pero el edificio de detrás es uno de los dos
    museos gemelos de la Maria-Theresien-Platz (el tambor con ventanas de arco y la torrecilla de esquina con
    cúpula oscura), no el Ayuntamiento, que es neogótico. Se comparó con otra foto de esa plaza.
  - `torre.jpg`: es la torre sur de la Catedral (el remate es el águila bicéfala con la cruz), no la del
    Ayuntamiento, que acaba en un caballero con estandarte.
- **Que no salga nadie reconocible de cerca.** La licencia de Unsplash no trae permiso de las personas que salen.
  En el Graben se movió el recorte para dejar fuera a una pareja que venía de frente. El Kohlmarkt se recortó por
  arriba: abajo había dos caras de frente. En `mtplatz.jpg` se desenfocó la foto de la pizarra para abajo. En las
  demás, la gente está de espaldas, en silueta o lejos, y el velo oscurece el tercio de abajo.
- **Que no se lea la pizarra del puesto de ponche.** Lleva precios de otro invierno. Va desenfocada.
- **La Catedral sale iluminada en rojo.** Es la foto real de un día con esa iluminación, con los puestos del
  mercadillo debajo.

**Ninguna foto es del mercadillo del Ayuntamiento (Rathausplatz), a propósito.** El primer corte abría con su arco, y
ese mercadillo no es uno de los cinco que cuenta el vídeo: no queda en la puerta de ninguna parada del viaje.

No están en `banco/fotos/`: el banco pide cada foto en los dos tamaños y con su entrada en `creditos.json`.

## La voz

Kore, la voz de la app, por Gemini TTS (`gemini-3.1-flash-tts-preview`, `piezas/ia/voz.py`). Es voz sintética.
El estilo y las frases están en `voz.json`.

## La música

`assets/musica-calma.mp3` es la de «Un trazo» (`../lanzamiento-trazo/README.md`): Lyria 3 Pro, por la API de
Gemini, el 27-oct. Es música generada con IA, sin derechos de terceros.

**Al publicar:** como en «Un trazo» y en «Así funciona», la voz y la música son generadas, así que se marca la
etiqueta de contenido de IA al subirlo. Las fotos son reales y no cuentan.
