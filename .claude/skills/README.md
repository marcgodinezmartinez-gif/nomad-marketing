# Las skills de marketing, y las cuarenta que no están

De <https://github.com/coreyhaines31/marketingskills> (Corey Haines, **MIT**), copiadas el
24 de agosto de 2026. El repo trae **47 skills**; aquí hay **siete**.

## Por qué siete y no cuarenta y siete

Este repo ya tiene escrito lo que pasa cuando se guardan ficheros que nunca se ejecutan:
`mobile/.maestro/` fueron once flujos de prueba que no habían corrido nunca contra esta
app, y se borraron el 7 de agosto porque *«doce ficheros que nunca corren no son un activo:
son un directorio que aparece en cada inventario reclamando una cobertura que nadie
tiene»*.

Cuarenta skills de marketing sin una tarea a la que aplicarlas serían lo mismo. Así que
está copiado lo que tiene **un uso nombrado en las próximas seis semanas** —el testeo, la
campaña de septiembre y el lanzamiento de octubre— y nada más.

| Skill | Para qué, aquí |
|---|---|
| `product-marketing` | Mantiene `.agents/product-marketing.md`, que **todas las demás leen antes de preguntar nada**. Es la que más rinde: sin ella cada skill empieza pidiendo que le expliques la app. |
| `aso` | La ficha de App Store y Google Play, que está sin tocar (issue #4). Trae los límites reales de Apple —30 caracteres de título, 30 de subtítulo, 170 de texto promocional— y un método de auditoría. Aquí no hay ni una línea de conocimiento de ASO. |
| `launch` | El lanzamiento de octubre. |
| `ads` | La campaña de pago de septiembre. |
| `ad-creative` | Las piezas de esa campaña. |
| `signup` | La conversión de la landing a alta en la lista de espera — **la única métrica de septiembre**. |
| `social` | El orgánico durante la campaña. |

## Lo que se dejó fuera, y por qué

`revops`, `sales-enablement`, `prospecting`, `cold-email` — no hay equipo de ventas ni
clientes B2B. `churn-prevention` — no hay suscripción de la que darse de baja: se paga por
viaje. `ab-testing`, `attribution`, `analytics` — hacen falta usuarios primero, y la
atribución básica ya está hecha (`source` en `waitlist`). `programmatic-seo`, `schema`,
`site-architecture`, `seo-audit`, `ai-seo` — la web son cuatro páginas estáticas y el
producto se descubre en las tiendas, no en Google. `pricing`, `offers` — los precios están
decididos y medidos en `docs/ECONOMIA.md`. El resto —`co-marketing`, `referrals`,
`community-marketing`, `influencer-marketing`, `free-tools`, `directory-submissions`,
`events`, `public-relations`— son buenas ideas para cuando haya algo que promocionar y
alguien a quien promocionárselo.

**Ninguna se ha descartado por mala.** Se han descartado por no tener todavía una tarea. El
repo original está a un `git clone` de distancia el día que la tengan.

## Una advertencia sobre lo que estas skills dan por hecho

Están escritas para SaaS: hablan de trials, de MRR, de ICP y de ciclos de venta. NOMAD
vende **un viaje suelto a 2,99-6,99 €** en una tienda de aplicaciones, sin suscripción y
con Apple y Google quedándose el 15 % y recaudando el IVA. Cuando una skill proponga una
métrica de SaaS, la traducción no siempre existe — y forzarla es peor que no tenerla.

`.agents/product-marketing.md` lo dice desde la primera línea para que no haya que
repetirlo en cada conversación.
