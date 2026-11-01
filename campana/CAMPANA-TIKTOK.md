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
- **Bloqueado**: TikTok rechaza crear la campaña con *Your account has an outstanding payment or no valid
  payment method* (40002). El saldo es 0. Falta que el dueño añada el método de pago en TikTok Ads Manager.
- En @app.nomad está publicado «Así funciona» (item `7702873582577175830`, 59,3 s), **sin la etiqueta de
  contenido generado por IA** (`is_ai_generated: false`). «Un trazo» **no está publicado** en TikTok.
