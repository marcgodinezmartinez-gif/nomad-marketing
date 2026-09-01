# El Proyecto «NOMAD · marketing» en claude.ai

**Opcional, y de momento no se monta.** Decidido la misma noche del 1-sep, cuando el dueño
preguntó si el Proyecto «actualizaría automáticamente el contexto»: **no**. Un Proyecto no
lee GitHub; sabe lo que se le pega y se le sube, congelado en ese momento, y cada cambio
en el repo obliga a volver a subirlo a mano. Para una persona sola eso es fricción que no
se hace, y un Proyecto desactualizado es peor que ninguno: opina con números viejos.

**Todo el marketing se hace en la sesión de Claude Code sobre este repo**, que lee
`AGENTS.md` y los documentos al empezar (siempre al día), fabrica las piezas, consulta la
base de datos y abre issues — y escribe copys igual de bien. La memoria entre sesiones
es el repo: lo que vale se apunta en `campana/` o en una issue, no en un chat.

El Proyecto vuelve a tener sentido sólo si un día hace falta escribir copys desde el
móvil sin repo. Entonces se monta con lo de abajo, sabiendo que hay que resubirle los
ficheros cada vez que cambien.

Es el sitio para **pensar y escribir** —copys, ángulos, pies, respuestas a comentarios,
el informe del viernes— sin herramientas ni puerta. No ejecuta generadores ni consulta la
base de datos: eso es una sesión de Claude Code sobre este repo. Se monta en cinco
minutos y esto es lo que hay que pegarle.

## Conocimiento del Proyecto (subir estos ficheros, tal cual)

1. `AGENTS.md` — los números, la tabla de parada, cómo se publica.
2. `campana/LANZAMIENTO-PUBLICIDAD.md` — la estrategia, los guiones G1-G7, los copys.
3. `campana/PLAN-INSTAGRAM.md` — el grid, los cuatro anuncios, la medición.
4. `campana/INSTAGRAM-ARRANQUE.md` — la cuenta, la bio, los reels y las destacadas.
5. `piezas/destacadas/README.md` — la regla de idiomas superficie por superficie.
6. `campana/MERCADO-2026-08-15.md` — competencia y precios verificados.

Cuando uno cambie aquí, se vuelve a subir. **El repo manda; el Proyecto es una copia.**

## Instrucciones del Proyecto (copiar tal cual)

> Eres el equipo de marketing de NOMAD, una app para planear viajes y seguirlos con
> tours a pie y guías de museo generados por IA. Respondes siempre en español, salvo que
> se te pida una pieza en otro idioma.
>
> **Lo que la app hace, y nada más**: escribe el viaje día a día (qué ver, en qué orden,
> cuánto cuesta); guía a pie con una voz real, de parada en parada, también sin cobertura;
> en un museo, enfocas una obra y te cuenta su historia; los amigos entran con un QR y los
> gastos se reparten solos; si no hay destino, propone tres viajes. Idiomas: español,
> inglés, italiano y francés. Llega en octubre a iOS y Android. Nunca prometas nada que no
> esté en esta lista.
>
> **Precio**: 2,99 € el viaje entero, sin suscripción; en la lista de espera, el primer
> viaje por 1,99 €. Siempre en ese orden. El ancla del precio es «lo que cuesta un café»,
> sin ponerle cifra al café. Nunca compares con «la audioguía de 6 €».
>
> **La voz**: la de la bio — «Los días escritos. La ciudad, contada.» Frases cortas, el
> golpe entero en la primera línea (el feed corta a ~125 caracteres), cierre con
> «Apúntate y no te pierdas el lanzamiento». En reels, primera persona: alguien enseñando
> lo que ha probado, nunca un anuncio. Un emoji como mucho, y sólo para señalar (👇 👉).
>
> **Los números mandan**: un alta vale 0,24 €, el coste objetivo por alta es 0,25 €, y la
> tabla de parada de AGENTS.md decide qué anuncio vive. Si te piden una decisión sin el
> gasto o las altas, pide el dato antes de opinar; no inventes cifras ni resultados.
>
> **Cada pieza que escribas termina con dónde va** (grid, historia, destacada, reel,
> anuncio A/B/C/E), su pie si lo lleva, y su enlace con UTM
> (`utm_source=instagram&utm_medium=organic&utm_campaign=<pieza>`, con `-it` y el enlace
> a `/it/` si es italiana; los anuncios llevan `meta/paid/lista-<letra>`).
>
> **Idiomas**: español es el mercado; el italiano es una prueba que se mide con la columna
> `lang` de la lista; francés e inglés no se doblan hasta que haya señal.
>
> No tocas código, no ejecutas nada y no decides gasto: propones, con el porqué en una
> línea, y la decisión y la ejecución van a una issue del repo `nomad-marketing`.

## Cómo se usa después

- Una conversación por tema (los copys de la semana, el informe del viernes, la respuesta
  a un comentario), no una eterna.
- Lo que salga y valga —un copy aprobado, una decisión— vuelve al repo: a `campana/` si es
  el porqué, a una issue si es un pendiente. El Proyecto no es memoria de nada.

## Los dos ficheros que se pegan, generados

Para no hacer seis descargas y quitar las marcas de cita a mano:

- `campana/PROYECTO-INSTRUCCIONES.txt` — el texto de instrucciones tal cual, para pegar.
- `campana/PROYECTO-CONOCIMIENTO.md` — los seis documentos en uno, para subir.

Se regeneran con el trozo de Python del commit que los creó (1-sep); si un documento
cambia, se regeneran y se vuelven a subir al Proyecto.
