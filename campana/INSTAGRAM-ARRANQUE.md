# El arranque de Instagram y los primeros 50 €

Escrito el 28 de agosto de 2026, el día que el dueño dijo *«empezar hoy con 50 € de publi,
pero tengo la cuenta vacía: 0 seguidores y 0 seguidos»*. Este doc es la respuesta operativa;
la estrategia y la economía viven en `campana/LANZAMIENTO-PUBLICIDAD.md` y no se repiten aquí.

## La corrección de modelo mental, primero

**Los seguidores no importan para los anuncios.** Meta enseña el anuncio a quien quiere,
tengas 0 o 100.000. Lo que SÍ importa es que **quien toque el perfil desde el anuncio no
encuentre un solar**: un grid vacío huele a estafa y tira los clics pagados. Así que el
orden es: hoy se viste la cuenta, y el dinero arranca con el grid puesto — mañana o pasado,
no dentro de un mes.

**Y los 50 € no se gastan en un día.** El plan ya calculó por qué (un alta vale 0,24 € y
el CPL de Meta en España es 0,30-1,50 €): el pagado de septiembre es presupuesto de
APRENDIZAJE. 50 € son **5 €/día durante 10 días** — exactamente la forma del presupuesto
de aprendizaje del plan, empezado antes. Lo que compran no son altas: es saber cuál de los
cuatro argumentos (precio, cobertura, producto, grupo) mueve a la gente, ANTES de
ponerle dinero de verdad en octubre.

**No compres seguidores, nunca.** Meta lo huele, la gente lo huele, y no hay nada que un
perfil con 40 posts honestos no arregle solo.

## Hoy: vestir la cuenta (1-2 horas, todo tuyo)

1. **Pásala a cuenta de empresa** (Ajustes → Cuenta → Cambiar a cuenta profesional →
   Empresa). Sin esto no hay anuncios ni métricas.
2. **Nombre**: `NOMAD` · **Usuario**: `@app.nomad` (elegido el 29-ago; @travelsnomad no
   quedó libre).
3. **Bio** (cópiala tal cual — la eligió el dueño el 29-ago):
   > Los días escritos. La ciudad, contada.
   > Itinerarios, tours al oído y gastos del grupo.
   > 🎟 Apúntate y no te pierdas el lanzamiento ↓
4. **Enlace de la bio**: `travelsnomad.com` a secas (29-ago: el dueño no quiso UTM a la
   vista). La portada atribuye por referrer y esas altas salen como `instagram/referral`.
5. **Sigue 20-30 cuentas del nicho** — oficinas de turismo, museos (@museodelprado,
   @lelouvre), cuentas de viajes en español. Es señal de vida y te cura el feed para ver
   qué formato funciona nativo, que es de donde salen los anuncios que no parecen anuncios.

## Los 9 posts del grid (diseñados; se exportan del lienzo)

Los nueve están diseñados a 1080×1350 en el lienzo de Claude
(«Posts de Instagram NOMAD» — el enlace que te pasé por chat; también aparece en
claude.ai/code/artifacts). Cada tarjeta tiene su botón de **exportar PNG**.

**Se suben los nueve el mismo día y EN ORDEN INVERSO, del 9 al 1** (decidido el 29-ago):
el grid de Instagram pone lo más reciente arriba a la izquierda, así que para que el
mosaico quede como está diseñado la portada del Coliseo se sube LA ÚLTIMA.

Son fotográficos: fotografía real de viaje, scrim oscuro y titular en serif
encima. **Todas las fotos son CC0 o dominio público** (verificado foto a foto en
Wikimedia Commons el 28-ago): no se debe atribución a nadie, ni en la imagen ni
en el pie — por eso no hay marca de agua. El registro de qué fichero de Commons
es cada una queda guardado con los fuentes del lienzo, por si algún día hay que
demostrar la procedencia.

| # | Post (imagen del lienzo) | Pie (caption) |
|---|---|---|
| 1 | Portada — Coliseo al atardecer | «Los días escritos. La ciudad, contada. Te escribe el viaje y te lo cuenta al oído. Llega en octubre.» |
| 2 | El plan — tejados de Praga + teléfono | «Dices destino y fechas. Tu viaje, planeado día a día: qué ver, en qué orden y cuánto cuesta.» |
| 3 | El tour — callejón del Albaicín con la ruta 1-2-3 | «Te lleva de una parada a la siguiente y te dice dónde ponerte. Una voz de verdad te lo cuenta al oído, incluso sin cobertura.» |
| 4 | El precio — Place du Tertre (Montmartre) de noche, terrazas encendidas | «El viaje entero, por lo que cuesta un café: desde 2,99 €. Sin suscripción. Se paga por viaje.» |
| 5 | El museo — mosaico dorado de Santa Prassede (Roma) | «Apunta la cámara a un cuadro y te cuenta su historia.» |
| 6 | La visita — biblioteca de la abadía de Melk + teléfono | «Se acuerda de por dónde has pasado, sin preguntar.» |
| 7 | La lista — San Pedro y el puente de noche | «Tu primer viaje, 1,99 €. Inscríbete y no te pierdas el lanzamiento — el enlace, en la bio.» |
| 8 | El grupo — Fontana di Trevi de noche + tarjeta QR | «Tus amigos se unen con un QR y los gastos se reparten solos.» |
| 9 | El buscador — tres postales: Santorini, Granada, Oporto | «¿Sin destino? Dile qué te apetece y elige entre tres viajes pensados para ti.» |

Al terminar, a stories solo los tres fuertes (portada, plan y precio) — nueve seguidas
es ruido. Con el grid entero puesto, la campaña puede arrancar al día siguiente.

## Los 50 €, cuando el grid esté (día 2-3)

Meta Business Suite → Crear anuncio → **objetivo Tráfico** (sin píxel a propósito: medimos
por `waitlist.source`, no por lo que Meta se atribuya).

- **1 campaña, 1 conjunto, 4 anuncios** — los copys **A, B, C y E** de
  `LANZAMIENTO-PUBLICIDAD.md` §Copys (la D, urgencia, queda en reserva para la semana del
  cierre), con **la misma imagen los cuatro** (la del plan o la del precio — Place du
  Tertre): lo que se mide es el argumento, no la foto.
- **Público: amplio.** España, 20-55, sin intereses apilados — la creatividad es la
  segmentación (skill `ads`, era Andromeda). Ubicaciones automáticas.
- **Presupuesto: 5 €/día.** Tope total 50 €.
- **Enlaces, tal cual** (uno por anuncio):
  `https://travelsnomad.com/?utm_source=meta&utm_medium=paid&utm_campaign=lista-a` (…b/c/e)
- **Reglas de parada**: la tabla de `LANZAMIENTO-PUBLICIDAD.md` §Cuándo parar, anclada en
  TCPL 0,25 €. En corto: nada se juzga antes de 0,75 € gastados; cero altas con 0,75 € =
  concepto muerto; si Meta no le da gasto a uno, ése ya está juzgado. **Y la excepción que
  se lleva por delante a la segunda regla** (2-sep): si hay clics y no hay altas, el fallo
  está después del clic — se miran «visitas a la página de destino» contra «clics en el
  enlace» antes de matar nada.

## El minuto diario de medición

```sql
SELECT coalesce(source, '(directo)') AS origen, count(*) AS altas
FROM public.waitlist GROUP BY 1 ORDER BY 2 DESC;
```

En el SQL editor de Supabase (o el panel). `meta/paid/lista-a` contra `lista-b/c/e` es la
única tabla de resultados que importa. El viernes de la primera semana: coste por alta por
copy, y con eso se decide qué se escala y qué se mata.

(Un origen más desde el 30-ago: `instagram/organic/story-personal` — la historia del
Instagram personal del dueño hacia amigos, con su UTM propio
`utm_source=instagram&utm_medium=organic&utm_campaign=story-personal` para que el boca a
boca no se mezcle ni con la bio ni con los anuncios. No compite con los cuatro de arriba:
es gratis.)

## Lo que este doc NO cambia

El plan de septiembre sigue siendo el de `LANZAMIENTO-PUBLICIDAD.md`: **el canal que se
paga solo es el orgánico en vídeo** (un alta orgánica cuesta cero), y los guiones G1-G7
siguen esperando un iPhone y un museo. Estos 50 € adelantan el aprendizaje pagado con el
grid como requisito — no lo sustituyen.

## Los Reels: por qué, y cómo se fabrican sin cámara (31-ago)

Pregunta del dueño esa tarde: «¿consideras añadir más contenido a Instagram?». La
respuesta medida, y la razón de esta sección: **más posts del grid ya no compran nada**.
Con 0 seguidores un post estático no lo ve nadie — el grid es el escaparate de quien
llega del anuncio o de la bio, y con 12 piezas (9 del grid + 3 carruseles de idiomas) ese
trabajo ya está hecho. **Reels es la única superficie de Instagram que enseña algo a
quien NO te sigue**, y la cuenta tenía cero vídeo. Ese era el hueco, no el número de
posts.

Y hay una segunda razón para el formato: es el sitio natural del **asistente de IA**, que
en la publi estaba callado (de ahí también el copy F de `LANZAMIENTO-PUBLICIDAD.md`). El
gancho del Reel es «le pedí a una IA que me organizara 3 días en Roma» — primera persona,
alguien enseñando lo que ha probado, que es cómo se cuenta una herramienta en el feed. Un
Reel que parece un anuncio se salta.

**Se fabrican desde una sesión, sin grabar nada.** El pipeline vive en `piezas/reels/`:

1. `gen-reel.py` (y `gen-reel-it.py`) escriben 5 escenas HTML de 1080×1920 con el sistema
   visual de la casa — mismo HELMET de fuentes que los carruseles — y el teléfono
   compuesto con las capturas REALES ya parcheadas por idioma (`capplanit.png`…).
2. `exportar-reel.mjs` las convierte en PNG con el chromium de `/opt/pw-browsers`.
3. `montar-reel.sh` las monta en mp4 con **ffmpeg**, que NO viene en el contenedor pero se
   instala en 11 segundos: `npm i ffmpeg-static`.

Las dependencias que no están en el repo (fotos CC0 del banco, `Main.dc.html` con el
HELMET, las capturas parcheadas) se rehacen con los generadores del scratchpad; su
procedencia está en `fotos/bajadas.json`.

**Las dos trampas de ffmpeg, pagadas ya, para que nadie las vuelva a pagar:**

- **`zoompan` genera `d` frames POR CADA FRAME DE ENTRADA.** Con `-loop 1 -t 3` la entrada
  ya son 90 frames y `d=90` los multiplica: el primer montaje salió de **5 minutos y 35
  segundos** en vez de 14,6. La entrada tiene que ser UNA imagen suelta, sin `-loop`.
- **El pre-escalado ×2 antes del `zoompan`** es lo que quita el temblor que ese filtro
  tiene sobre imágenes grandes. Sin él, el movimiento «salta» de píxel en píxel.

**Zona segura**: la interfaz de Instagram tapa ~200 px arriba y ~420 px abajo. Todo el
texto vive entre `y=230` e `y=1480`; lo de abajo es decoración sacrificable.

**Los Reels salen SIN pista de audio, a propósito.** Un audio horneado es un riesgo de
copyright y, sobre todo, renuncia al empujón algorítmico: el audio se elige DENTRO de
Instagram al subir, de la lista de tendencias del día, que es lo que el sistema premia.
Instagram lo ajusta solo a la duración del vídeo.

## Las destacadas, y por qué NO son más posts (1-sep)

Pregunta del dueño esa tarde: *«¿debería seguir subiendo contenido, algo que ayude a los
nuevos followers a entender qué hace la app y cómo se apuntan a la waitlist?»*.

La respuesta larga —qué se sube, en qué orden, con qué texto y dónde va el adhesivo de
enlace— vive en **`piezas/destacadas/README.md`**. Lo que hay que saber sin abrirlo:

- **Más posts del grid ya no compran nada**, por lo mismo que decía la sección de los
  Reels: con doce piezas, el escaparate está hecho. Lo que faltaba eran las dos
  superficies que el grid no cubre.
- **Las destacadas** son el único sitio de Instagram pensado para «acabo de llegar aquí,
  ¿qué es esto?»: viven bajo la bio, no envejecen y no bajan por el feed. Son once
  tarjetas en dos destacadas —`Qué es` (7) y `La lista` (4)— y **se suben primero como
  historias, así que además son el contenido del día**.
- **La tarjeta de los tres pasos es la que convierte.** «¿Y cómo me apunto?» no puede
  tener como respuesta «busca el enlace»: escribir los tres pasos con el adhesivo de
  enlace delante es la diferencia entre entenderlo y hacerlo. Y la cuarta —«Un correo.
  Uno.»— contesta la objeción que frena a quien YA estaba convencido.
- **Un segundo Reel**, `reel-nomad-grupo.mp4`, con el ángulo del grupo: el único de los
  cuatro de la campaña que ningún competidor puede copiar, y el único que no estaba
  contado en vídeo.

**Y el dato que gobierna todo esto** (consulta del minuto diario, 1-sep): ocho altas,
**todas del 31 de agosto y ninguna del 1 de septiembre** — 4 de `ig/social`, 3 de
`invitacion`, 1 de `meta/paid/lista-a`. Lo orgánico trajo cuatro veces más que lo
pagado, y el día que no se publicó nada no entró nadie. Además `lista-b`, `-c` y `-e`
están a cero: **falta mirar el gasto por anuncio en Meta y aplicarles la tabla de
parada**, que con 5 €/día entre cuatro anuncios cruza el umbral de 0,75 € en menos de un
día. Ese dato no se lee desde una sesión.
