# Campaña de noviembre: «Así funciona» contra «Un trazo» (30-oct)

Lo que pidió el dueño el 30-oct: «monta una campaña de marketing con este vídeo y el otro, el que
consideres mejor; yo creo que este». *Este* es «Así funciona» (#18) y *el otro*, «Un trazo»
(`piezas/historias-animadas/lanzamiento-trazo/`, publicado en el feed el 27-oct).

## Cuál va delante, y por qué

**«Así funciona»**, la misma apuesta que el dueño. Enseña la app de verdad, pantalla a pantalla y en el
orden en que se usa. La primera frase plantea un problema que se reconoce («¿Cuatro días en Lisboa y no
sabes por dónde empezar?»), y el vídeo acaba en «Descárgala gratis en la App Store». A alguien que no
conoce Nomad le contesta qué hace. «Un trazo» cuenta lo mismo con dibujos y es más corto (33 s contra
59 s), pero tiene un dato a favor que no se puede ignorar: es el reel orgánico que más ha respondido de
la cuenta (32 «me gusta» y 8 comentarios, contados el 30-oct). Por eso entra como rival y no se queda
fuera: si el corto gana al largo, es una lección que vale más que el gasto.

## Cómo está montada en Meta (todo en pausa)

| nivel | qué |
|---|---|
| campaña | «App Store iPhone · Así funciona vs Un trazo»: tráfico, presupuesto de campaña de 15 €/día (decisión del dueño, 31-oct: «dale de primeras a 15-20 € al día»; antes 3 y 6), máximo volumen, y el conjunto acaba el 7-nov a las 23:59. El tope de gasto de campaña no se pudo poner: Meta pide 100 € como mínimo |
| conjunto | «España · iPhone · público automático»: España, sólo iOS, Advantage+ público y ubicaciones |
| anuncio 1 | «Un trazo · reel orgánico · web a la tienda»: el reel publicado del 27-oct, con botón **Descargar** a `travelsnomad.com/app` (en un iPhone salta a la App Store) y la etiqueta de IA |
| anuncio 2 | «Así funciona · reel orgánico · web a la tienda»: el reel publicado el 31-oct, con el mismo botón, el mismo enlace y la etiqueta de IA |

Los dos anuncios salen de los posts orgánicos, no de copias: así los «me gusta» y los comentarios del
anuncio se suman al post y el post llega con los que ya tiene. El anuncio viejo de «Un trazo» («Un trazo ·
reel · web») se queda en pausa. Era una copia del vídeo sin esos «me gusta» y con un destino que no se
lee desde aquí, y el nuevo lo sustituye.

**El enlace no puede ser el de la App Store (31-oct).** El primer anuncio llevaba el botón directo a
`apps.apple.com` y Meta lo bloqueó: *App Url is only supported by App Installs objective*. En una campaña
de tráfico, un enlace a una tienda de apps no vale. Por eso va a `travelsnomad.com/app`, cuyo `tienda.js`
manda el iPhone a la ficha con `location.replace` (comprobado: lleva `apps.apple.com/app/id6797973945`).
La otra salida sería una campaña de promoción de apps, que pide dar de alta la app en Meta y no mediría
mejor sin su SDK. El anuncio fallido está archivado.

## Lo que le toca al dueño, en orden

1. **Publicar el reel de «Así funciona»** (#19) con su pie y la etiqueta de IA (`piezas/historias-animadas/
   asi-funciona/PUBLICAR.md` §1), y la historia con el adhesivo (§2). Dicho eso, el anuncio 2 se monta
   en un minuto.
2. **Decir el presupuesto y «actívala»**. Ninguna sesión la activa sin eso. **Propuesta, que es una
   suposición y se cambia en una línea: 6 €/día durante 7 días, 42 € como mucho**, para que cada vídeo
   tenga unos 3 €/día. Con los 3 €/día de ahora, cada uno se queda en ~1,5 € y en una semana no hay
   señal.
3. Si se quiere medir cada vídeo por separado en la App Store: el **token de proveedor** (`pt`, #14).
   Sin él, la tienda sólo dice cuántas descargas vinieron de Instagram y Facebook, no de qué anuncio.

## Cómo se mide, y qué no se sabe todavía

- **En Meta, por anuncio**: coste por clic en el enlace, % de clics y cuánto se ve el vídeo (los tres
  primeros segundos y la reproducción completa). Eso dice cuál de los dos **lleva gente a la tienda**.
- **En App Store Connect, para la campaña entera**: Analítica → Fuentes → «Web Referrer», las descargas
  que llegan desde `travelsnomad.com`, día a día, y las compras de esos días. Eso dice si la gente que
  llega **se la baja**. Ahí cuentan también las que vienen de la bio, así que se compara con la semana
  anterior a la campaña.
- **No hay todavía una unidad como el «alta = 0,24 €» de la lista**, y por eso no hay tabla de parada
  propia (lo dice `AGENTS.md`). Las cuentas: un viaje de 2,99 € deja 2,10 € netos después de Apple y el
  IVA (`admin_ventas`). Con, por decir, uno de cada diez que se la bajan comprando, una descarga vale
  unos 0,25 €. En España una descarga pagada en iOS cuesta bastante más, así que, como la de la lista,
  **esta campaña compra aprendizaje, no ventas**: qué vídeo mueve, y qué parte de los que llegan a la
  ficha compran.

## Calendario

| día | qué |
|---|---|
| 0 (31-oct) | el dueño publica el reel y la historia de «Así funciona»; se monta el anuncio 2. Hecho |
| 1 | el dueño activa con el presupuesto que diga |
| 4 | primera lectura: si uno de los dos apenas recibe gasto, Meta ya ha votado (la regla de siempre: el no-reparto es el veredicto) |
| 7 | se cierra: el que tenga el clic más barato, y no peor retención, se queda con todo el presupuesto la semana siguiente; el otro se pausa **sólo** si hay un sustituto listo |

Dos reglas de `AGENTS.md` que valen aquí: un anuncio muerto por falta de reparto se itera cambiando el
gancho o el vídeo, nunca el texto; y se promociona desde Ads Manager o desde aquí, **nunca desde la app
de Instagram del iPhone**, que cobra la comisión de Apple.

## Cambio a seguidores de Instagram (2-nov)

El dueño, el 2-nov, después de pasar la de TikTok a seguidores: «¿crees que deberíamos plantear también la
de Instagram para aumentar en seguidores e interacciones con el contenido? Dale, la dejamos a 15 € al día
como la que habíamos hecho». La campaña de tráfico a la tienda se paró ese día con **37,12 € gastados**,
el total desde el 31-oct, y su anuncio a la App Store se queda en pausa con ella.

| nivel | qué |
|---|---|
| campaña | «Instagram · seguidores · Así funciona» (`120248849784920710`): tráfico, 15 €/día de presupuesto de campaña, máximo volumen |
| conjunto | «España · 18+ · visitas al perfil de Instagram» (`120248849786750710`): optimiza **visitas al perfil**, con destino el perfil de @app.nomad. Va a España, de 18 años en adelante, sólo en las ubicaciones de Instagram (feed, historias, reels, explorar y el feed del perfil), con Advantage+ público. Acaba el 7-nov a las 23:59, como la de antes |
| anuncio | «Así funciona · reel orgánico · visitas al perfil» (`120248849856830710`): el mismo reel orgánico del 31-oct (creativo `988035950393562`), con la etiqueta de IA y sin enlace, porque el destino es el perfil |

Meta no tiene un objetivo que compre «seguidores» de Instagram. Lo más cerca es pagar por visitas al
perfil: la campaña se mide en **visitas al perfil** (Meta) y en **seguidores nuevos** de @app.nomad
(Instagram, Estadísticas). **Punto de partida: 135 seguidores el 2-nov**, contados por el dueño al encenderla. Las descargas
siguen saliendo de la bio (`travelsnomad.com`), así que el «Web Referrer» de App Store Connect sigue
valiendo. **Activarla no lo puede hacer una sesión**: el clasificador lo deniega, como el 31-oct. La
encendió el dueño en Ads Manager el 2-nov, y se comprobó: campaña y anuncio en ACTIVE, configurado y efectivo.

## Cierre (3-nov por la noche)

El dueño paró también la de Instagram el 3-nov por la noche. Números finales de Meta:

| campaña | gasto | resultado |
|---|---|---|
| «App Store iPhone · Así funciona vs Un trazo» (tráfico, 31-oct → 2-nov) | 37,26 € | 537 clics en el enlace, a 0,07 € |
| «Instagram · seguidores · Así funciona» (2-nov → 3-nov) | 18,29 € | 179 visitas al perfil, a 0,10 € |
| **total Meta en esta ronda** | **55,55 €** | |

Los seguidores nuevos de Instagram no los da Meta: hay que compararlos a mano con los 135 del 2-nov. Y lo que deja
la ronda entera (Meta y TikTok, unos 118 €): muchos clics baratos y casi ninguna descarga. En la semana de la campaña
hubo unos 1.030 clics hacia la App Store y 13 instalaciones de iPhone, así que el problema no es el anuncio, es lo que
pasa después del clic.

Queda activa en la cuenta «lista-lead-g» (de la lista de espera, 5 €/día), que no ha gastado nunca nada: pausarla es
cosa del dueño.
