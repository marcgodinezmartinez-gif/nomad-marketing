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
| campaña | «App Store iPhone · Así funciona vs Un trazo»: tráfico, presupuesto de campaña de 3 €/día, máximo volumen |
| conjunto | «España · iPhone · público automático»: España, sólo iOS, Advantage+ público y ubicaciones |
| anuncio 1 | «Un trazo · reel orgánico · App Store»: el reel publicado del 27-oct, con botón **Descargar** a `apps.apple.com/app/id6797973945` y la etiqueta de IA |
| anuncio 2 | «Así funciona»: **falta**. Se hace del reel en cuanto esté publicado (abajo) |

Los dos anuncios salen de los posts orgánicos, no de copias: así los «me gusta» y los comentarios del
anuncio se suman al post y el post llega con los que ya tiene. El anuncio viejo de «Un trazo» («Un trazo ·
reel · web») se queda en pausa. Era una copia del vídeo sin esos «me gusta» y con un destino que no se
lee desde aquí, y el nuevo lo sustituye.

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
- **En App Store Connect, para la campaña entera**: Analítica → Fuentes → «App Referrer», las descargas
  que llegan desde Instagram y Facebook, día a día, y las compras de esos días. Eso dice si la gente que
  llega **se la baja**.
- **No hay todavía una unidad como el «alta = 0,24 €» de la lista**, y por eso no hay tabla de parada
  propia (lo dice `AGENTS.md`). Las cuentas: un viaje de 2,99 € deja 2,10 € netos después de Apple y el
  IVA (`admin_ventas`). Con, por decir, uno de cada diez que se la bajan comprando, una descarga vale
  unos 0,25 €. En España una descarga pagada en iOS cuesta bastante más, así que, como la de la lista,
  **esta campaña compra aprendizaje, no ventas**: qué vídeo mueve, y qué parte de los que llegan a la
  ficha compran.

## Calendario

| día | qué |
|---|---|
| 0 | el dueño publica el reel y la historia de «Así funciona»; se monta el anuncio 2 |
| 1 | el dueño activa con el presupuesto que diga |
| 4 | primera lectura: si uno de los dos apenas recibe gasto, Meta ya ha votado (la regla de siempre: el no-reparto es el veredicto) |
| 7 | se cierra: el que tenga el clic más barato, y no peor retención, se queda con todo el presupuesto la semana siguiente; el otro se pausa **sólo** si hay un sustituto listo |

Dos reglas de `AGENTS.md` que valen aquí: un anuncio muerto por falta de reparto se itera cambiando el
gancho o el vídeo, nunca el texto; y se promociona desde Ads Manager o desde aquí, **nunca desde la app
de Instagram del iPhone**, que cobra la comisión de Apple.
