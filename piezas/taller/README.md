# El taller de redes — el lienzo editable

Publicado el 1 de septiembre de 2026 (noche), a partir de esta frase del dueño: *«no
quiero que me mandes las fotos, quiero poder editarlas yo antes por si algo no me gusta.
Pensaba en generar un banco de imágenes, tipografías, iconos… para poder generar todo el
contenido usando estas plantillas»*.

**Dónde está**: <https://claude.ai/code/artifact/0fea041b-1676-4675-94ab-fc326d44bdb3>
(también en claude.ai/code/artifacts, «Taller de redes NOMAD»).

**Qué tiene**, en cinco páginas:

| Página | Contenido |
|---|---|
| Kit | Colores (los de `tokens.ts`, sin redondear), tipografía (Instrument Serif / Sans, con los tamaños de historias y los roles de la app), la marca en tres fondos, 28 iconos Lucide (los de la app, ISC), las 11 fotos del banco con su crédito de Commons, las 12 capturas reales (6 pantallas × es/it) |
| Plantillas | Siete arranques: historia con foto, con teléfono, de pasos, plana, escena de reel, post del feed (1080×1350), carátula. Las de foto llevan un chip **«foto»** que elige entre las once del banco; las de teléfono, **«captura»** e **«idioma»** |
| Historias · ES | «Qué es» (7), «La lista» (4), las dos carátulas |
| Historias · IT | «Cos'è» (7), «Lista d'attesa» (4) |
| Reels | Roma (5 escenas), Grupo (5), Roma en italiano (5) |

Cada artboard se retoca en sitio (el texto, con doble clic; el resto, desde el panel) y se
exporta a PNG. Guardar publica la versión nueva para todo el que tenga el enlace.

## Cómo se construye

```bash
SC=<scratchpad> python3 piezas/taller/construir-taller.py    # escribe <scratchpad>/taller/
```

El script no dibuja las piezas: las **copia** de sus generadores (`gen-destacadas.py`,
`gen-reel*.py`) con las rutas de imagen aplanadas al nombre de fichero, y añade encima el
kit y las plantillas. Las fotos se recortan a 1080×1920 desde los originales de Commons;
las tres postales (Oia, Alhambra, Oporto) salían antes de recortes de 980×380 ampliados
cinco veces, y aquí vuelven a cortarse del original. Luego se siembra el lienzo y se
guarda con el mismo enlace.

**La regla de quién manda.** Mientras el dueño no toque el lienzo, manda el generador: se
rehace la pieza, se reconstruye el taller y se vuelve a guardar. En cuanto el dueño edite
algo en el lienzo, **manda el lienzo**: antes de volver a sembrar hay que leerlo, extraer
lo que haya y construir sobre eso, o su edición se pierde sin aviso.

## Dos cosas aprendidas al montarlo

- **La foto elegible por chip funciona, y se ha visto funcionar**: una rama `<sc-if>` por
  foto, cada una con su `src` literal (que es lo único que el lienzo sustituye por la
  imagen), y el chip decide cuál se pinta. Comprobado con el editor montado antes de
  guardar. Lo que NO funciona es poner el nombre en un hueco (`src="{{foto}}"`): el
  lienzo sustituye texto literal, no valores.
- **Los tableros del kit reutilizan los mismos ficheros de imagen que las historias**, así
  que el banco de fotos y el de capturas no pesan nada más. El taller entero pesa 9,9 MB y
  cada guardado lo vuelve a subir entero; el tope es 16.
