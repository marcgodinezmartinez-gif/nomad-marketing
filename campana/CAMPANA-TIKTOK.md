# TikTok: la misma campaña que en Meta (1-nov)

El dueño, el 1-nov: «quiero hacer publi en TikTok también; quiero conectar el MCP para que me hagas tú la
campaña automática también ahí». Este fichero es el encargo para la sesión que tenga el conector
**TikTok for Business** (se conecta en <https://claude.ai/customize/connectors>, y sólo lo ve una sesión
nueva). Lo de Meta, con el porqué de cada decisión, está en `CAMPANA-ASI-FUNCIONA.md`: aquí sólo lo que
cambia.

## Lo que hay que montar, en pausa

- **Campaña de tráfico** (no de promoción de apps), a España, sólo iOS. Meta rechazó el enlace
  directo a la App Store en una campaña de tráfico, y TikTok pide además la app dada de alta y un
  medidor (SKAN/MMP) para la de apps. Se va por la web igual que en Meta.
- **Destino: `https://travelsnomad.com/app`**: su `tienda.js` manda el iPhone a la ficha.
- **Los mismos dos vídeos**: «Así funciona» (59,3 s) y «Un trazo» (33 s). Si el dueño los ha
  publicado en TikTok, se anuncian como **Spark Ads** del post orgánico (hace falta el código de
  autorización del post, que da el dueño desde la app). Si no, se suben los ficheros: el `-limpia-`
  si el anuncio ya lleva botón, para no repetir el adhesivo.
- **Botón «Descargar»**, la etiqueta de contenido generado por IA y el pie de TikTok de
  `piezas/historias-animadas/asi-funciona/PUBLICAR.md` §3.
- **Presupuesto: lo dice el dueño.** TikTok pone mínimos por día más altos que Meta (comprobar en
  el panel al crearla; no inventarlo), y la de Meta va a 15 €/día hasta el 7-nov.
- **Nada se activa sin que el dueño lo diga**, como en Meta.

## Cómo se mide

Como en Meta: en TikTok, el coste por clic y cuánto se ve cada vídeo; en App Store Connect, las
descargas por «Web Referrer» (travelsnomad.com). **Ojo: las dos campañas comparten ese destino**, así
que en la tienda no se distinguen. Sin el `pt` (#14) la comparación entre redes sólo sale de los clics
de cada una.

## Estado (1-nov)

- Cuenta publicitaria «NOMAD_21pubx» (`7693936532474085382`), España, EUR, con @app.nomad enlazada como
  identidad para Spark Ads.
- El primer intento lo rechazó TikTok por no haber método de pago (40002). El dueño lo añadió el 1-nov.
- **Montado y en pausa (1-nov)**: campaña «App Store iPhone · Así funciona» (`1880670465682450`, tráfico,
  sin presupuesto de campaña); grupo «España · iPhone · automático» (`1880670495410833`): solo TikTok,
  España, iOS, de 18 años en adelante, clic a CPC sin puja, **20 €/día** (cifra elegida en la sesión,
  por confirmar con el dueño) del 1-nov a las 17:00 al 5-nov a las 17:00, hora de España: 4 días, unos 80 € como mucho, que es lo que pidió el dueño. El presupuesto total no se puede poner: TikTok no deja cambiar el tipo de presupuesto del grupo después de crearlo; anuncio Spark del post de «Así funciona»
  (`1880670507415714`), con botón «Descargar» a `travelsnomad.com/app`. El anuncio ya está encendido;
  para que salga, el dueño enciende la campaña y el grupo.
- En @app.nomad está publicado «Así funciona» (item `7702873582577175830`, 59,3 s), **sin la etiqueta de
  contenido generado por IA** (`is_ai_generated: false`). «Un trazo» **no está publicado** en TikTok.
- **Decisión del dueño (1-nov): el post se queda sin la etiqueta de IA.** TikTok no deja añadirla después
  de publicar, y el dueño no quiere volver a subirlo. El riesgo es que TikTok rechace el anuncio o le
  ponga la etiqueta automática. Si lo rechaza, la salida es volver a subir el vídeo con la etiqueta y
  montar el anuncio con el post nuevo. A partir de ahora, la etiqueta se pone al subir (PUBLICAR.md §3).

## Cambio a seguidores (2-nov)

El dueño, el 2-nov: «necesito los 1k followers para poder [poner el enlace en la bio], así que apretar con todo en
esta nueva campaña es la mejor opción». La campaña de clics se quedó en 26,55 €, 593 clics y 5 seguidores. Su
grupo `1880670495410833` está pausado. La nueva campaña es «Seguidores · Así funciona» (`1880751865068674`,
objetivo de interacción con la comunidad). El grupo `1880751895088818` optimiza seguidores: España, 18+,
todos los móviles (un seguidor de Android también cuenta para los 1.000), 20 €/día, que es el mínimo de TikTok
(17 €/día lo rechaza), del 2-nov a las 14:15 al 5-nov a las 06:00 de Madrid, lo que da unos 53 € y unos 80 € en
total con lo de antes. El anuncio `1880751937739778` es el mismo post de «Así funciona». Para llegar a 1.000 con
eso, cada seguidor tendría que salir a unos 5 céntimos.

## Cierre (3-nov por la noche)

El dueño paró las campañas el 3-nov por la noche, antes del fin previsto (5-nov a las 6:00), para no pasar de los
80 € que se había puesto de tope. Números finales leídos de TikTok esa noche:

| campaña | gasto | resultado |
|---|---|---|
| «App Store iPhone · Así funciona» (clics) | 27,24 € | 608 clics y 5 seguidores |
| «Seguidores · Así funciona» | 34,81 € | **148 seguidores**, a 0,24 € cada uno |
| **total TikTok** | **62,05 €** | |

Para los 1.000 seguidores que piden el enlace en la bio habría hecho falta unos 5 céntimos por seguidor: salió cinco
veces más caro. Comprar seguidores con anuncios no es el camino a los 1.000; queda para pensar en la sesión de
marketing.
