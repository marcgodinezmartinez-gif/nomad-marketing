# El arranque de Instagram y los primeros 50 €

Escrito el 28 de agosto de 2026, el día que el dueño dijo *«empezar hoy con 50 € de publi,
pero tengo la cuenta vacía: 0 seguidores y 0 seguidos»*. Este doc es la respuesta operativa;
la estrategia y la economía viven en `docs/LANZAMIENTO-PUBLICIDAD.md` y no se repiten aquí.

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
cuatro argumentos (precio, cobertura, producto, urgencia) mueve a la gente, ANTES de
ponerle dinero de verdad en octubre.

**No compres seguidores, nunca.** Meta lo huele, la gente lo huele, y no hay nada que un
perfil con 40 posts honestos no arregle solo.

## Hoy: vestir la cuenta (1-2 horas, todo tuyo)

1. **Pásala a cuenta de empresa** (Ajustes → Cuenta → Cambiar a cuenta profesional →
   Empresa). Sin esto no hay anuncios ni métricas.
2. **Nombre**: `NOMAD` · **Usuario**: `@travelsnomad` (o el libre más cercano — que case
   con el dominio).
3. **Bio** (cópiala tal cual — la eligió el dueño el 29-ago):
   > Los días escritos. La ciudad, contada.
   > Itinerarios, tours al oído y gastos del grupo.
   > 🎟 Apúntate y no te pierdas el lanzamiento ↓
4. **Enlace de la bio** (la atribución depende de él, cópialo exacto):
   `https://travelsnomad.com/?utm_source=instagram&utm_medium=organic&utm_campaign=bio`
5. **Sigue 20-30 cuentas del nicho** — oficinas de turismo, museos (@museodelprado,
   @lelouvre), cuentas de viajes en español. Es señal de vida y te cura el feed para ver
   qué formato funciona nativo, que es de donde salen los anuncios que no parecen anuncios.

## Los 9 posts del grid (diseñados; se exportan del lienzo)

Los nueve están diseñados a 1080×1350 en el lienzo de Claude
(«Posts de Instagram NOMAD» — el enlace que te pasé por chat; también aparece en
claude.ai/code/artifacts). Cada tarjeta tiene su botón de **exportar PNG**; se
publican en el orden 1→9, que es como está pensado el grid.

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
| 4 | El precio — Place du Tertre (Montmartre) de noche, terrazas encendidas | «El viaje entero, por lo que cuesta el café de la plaza: desde 2,99 €. Sin suscripción. Se paga por viaje.» |
| 5 | El museo — mosaico dorado de Santa Prassede (Roma) | «Apunta la cámara a un cuadro y te cuenta su historia.» |
| 6 | La visita — biblioteca de la abadía de Melk + teléfono | «Se acuerda de por dónde has pasado, sin preguntar.» |
| 7 | La lista — San Pedro y el puente de noche | «Tu primer viaje, 1,99 €. Inscríbete y no te pierdas el lanzamiento — el enlace, en la bio.» |
| 8 | El grupo — Fontana di Trevi de noche + tarjeta QR | «Tus amigos se unen con un QR y los gastos se reparten solos.» |
| 9 | El buscador — tres postales: Santorini, Granada, Oporto | «¿Sin destino? Dile qué te apetece y elige entre tres viajes pensados para ti.» |

Publica 3 hoy, 3 mañana, 3 pasado — un grid que nació entero el mismo día también canta.

## Los 50 €, cuando el grid esté (día 2-3)

Meta Business Suite → Crear anuncio → **objetivo Tráfico** (sin píxel a propósito: medimos
por `waitlist.source`, no por lo que Meta se atribuya).

- **1 campaña, 1 conjunto, 4 anuncios** — los copys A-D de
  `LANZAMIENTO-PUBLICIDAD.md` §Copys, con **la misma imagen los cuatro** (la del plan o la
  del precio — Place du Tertre): lo que se mide es el argumento, no la foto.
- **Público: amplio.** España, 20-55, sin intereses apilados — la creatividad es la
  segmentación (skill `ads`, era Andromeda). Ubicaciones automáticas.
- **Presupuesto: 5 €/día.** Tope total 50 €.
- **Enlaces, tal cual** (uno por anuncio):
  `https://travelsnomad.com/?utm_source=meta&utm_medium=paid&utm_campaign=lista-a` (…b/c/d)
- **Reglas de parada**: la tabla de `LANZAMIENTO-PUBLICIDAD.md` §Cuándo parar, anclada en
  TCPL 0,25 €. En corto: nada se juzga antes de 0,75 € gastados; cero altas con 0,75 € =
  concepto muerto; si Meta no le da gasto a uno, ése ya está juzgado.

## El minuto diario de medición

```sql
SELECT coalesce(source, '(directo)') AS origen, count(*) AS altas
FROM public.waitlist GROUP BY 1 ORDER BY 2 DESC;
```

En el SQL editor de Supabase (o el panel). `meta/paid/lista-a` contra `lista-b/c/d` es la
única tabla de resultados que importa. El viernes de la primera semana: coste por alta por
copy, y con eso se decide qué se escala y qué se mata.

## Lo que este doc NO cambia

El plan de septiembre sigue siendo el de `LANZAMIENTO-PUBLICIDAD.md`: **el canal que se
paga solo es el orgánico en vídeo** (un alta orgánica cuesta cero), y los guiones G1-G7
siguen esperando un iPhone y un museo. Estos 50 € adelantan el aprendizaje pagado con el
grid como requisito — no lo sustituyen.
