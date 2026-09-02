# nomad-marketing

Todo lo de NOMAD que **se publica en redes, se gasta en Meta o se mide en la lista de
espera**. Lo que se despliega o se somete a una tienda es código y vive en
`marcgodinezmartinez-gif/NOMAD` (la app, las funciones, la web con su formulario de
lista, los legales, la ficha de la tienda). Esa frase es la frontera; se separó el 1 de
septiembre de 2026 porque los tres trabajos —código, fabricar piezas, llevar la campaña—
vivían en la misma sesión y cada uno pagaba las reglas del otro.

```
campana/         los planes y sus decisiones: PLAN-INSTAGRAM, INSTAGRAM-ARRANQUE,
                 LANZAMIENTO-PUBLICIDAD, MERCADO. Son el porqué; se leen antes de opinar
piezas/          los generadores (reels, destacadas, el taller), preparar.sh, construir-todo.sh
banco/           el kit: fotos con sus créditos, capturas reales, marca, fuentes, iconos, QR
.claude/skills/  siete skills de marketing (Corey Haines, MIT); su README dice por qué siete
salida/          lo generado. No se versiona: se rehace en un minuto
```

**Lo pendiente vive en las GitHub issues de ESTE repo** (regla del dueño, 1-sep: «GitHub
Issues debe ser la biblia de lo que queda pendiente»). Las tres últimas de marketing
quedaron en el repo de la app —#68 subir destacadas y reels, #69 la tabla de parada,
#70 esta separación— y se cierran allí; las nuevas se abren aquí.

## Los números que gobiernan las decisiones

Calculados de costes reales en `campana/LANZAMIENTO-PUBLICIDAD.md`; no se discuten en
cada sesión, se aplican:

- **Un alta vale 0,24 €** (margen esperado de un miembro de la lista).
- **Coste objetivo por alta (TCPL): 0,25 €.** Un alta pagada en Meta en España cuesta
  0,30-1,50 €, así que **lo pagado compra aprendizaje** (qué argumento mueve), no altas.
- **Precio**: 2,99 € el viaje entero, sin suscripción; en la lista, el primero por 1,99 €.
  Siempre en ese orden. El ancla del precio es **el café**, nunca «la audioguía de 6 €»:
  el dueño la ha tirado dos veces y no vuelve por ninguna puerta.

**La tabla de parada** (aritmética, no corazonadas):

| Situación | Qué hacer |
|---|---|
| Un anuncio ha gastado < 0,75 € (3× TCPL) | Esperar. No hay señal todavía |
| Cero altas con ≥ 0,75 € gastados | Matar el CONCEPTO, no iterarlo con otro texto |
| **Hay clics y no hay altas** (< ~3 % de los clics se apuntan) | **No matar todavía**: el fallo está DESPUÉS del clic. Comparar «visitas a la página de destino» con «clics en el enlace» antes de tocar el anuncio |
| Coste por alta ≤ 0,25 € | Candidato a ganador |
| Entre 0,25 y 0,38 € | Vigilar: varianza normal |
| > 0,38 € (1,5× TCPL) | Cambiarlo: fallo estructural |
| Meta apenas le da gasto | Matar ya: el no-reparto ES el veredicto |

Y dos reglas que se salta todo el mundo: al iterar un anuncio muerto por falta de reparto
se cambia el gancho o el visual, **nunca el texto** (nadie llegó a leerlo); y **nunca se
pausa sin reemplazo listo**.

La fila de «hay clics y no hay altas» la pagó la campaña el 2-sep: 20 000 de alcance, 677
clics (3,4 % de CTR, bueno para tráfico frío) y **1 alta** — 0,15 %. La fila de «cero
altas» habría matado el creativo, que era la única parte que funcionaba. El porqué y el
diagnóstico de la portada, en `campana/LANZAMIENTO-PUBLICIDAD.md`.

## Medir antes de opinar

La única tabla de resultados es la base de datos, no lo que Meta se atribuya. Sin píxel,
a propósito. Dos consultas, cada día:

```sql
SELECT coalesce(source, '(directo)') AS origen, count(*) AS altas,
       min(created_at)::date AS primera, max(created_at)::date AS ultima
FROM public.waitlist GROUP BY 1 ORDER BY 2 DESC;

SELECT coalesce(lang, '(sin lang)') AS idioma, coalesce(source, '(directo)') AS origen, count(*)
FROM public.waitlist GROUP BY 1, 2 ORDER BY 3 DESC;
```

Se ejecutan contra el endpoint de consulta de la API de gestión de Supabase con el token
de gestión en la variable `SUPABASE_TOKEN_GESTION` (**nunca se imprime, nunca va a un
fichero del repo**). No existe todavía un rol de sólo lectura de Postgres; el día que
exista, la consulta diaria puede ser una Rutina programada. **El gasto de Meta no se
lee desde una sesión**: no hay conector, se mira en Business Suite y se anota en la
issue de la campaña.

Los orígenes que aparecen: `instagram/referral` (la bio), `meta/paid/lista-a|b|c|e` (los
cuatro anuncios), `invitacion` (/join), `recomendacion` (/r), y lo que lleve UTM propio.
**Lo que decía el 1-sep**: 8 altas, todas del 31-ago, todas `lang = es` — 4 `ig/social`,
3 `invitacion`, 1 `meta/paid/lista-a`; `lista-b`, `-c` y `-e` a cero.

## Instagram: cómo se publica aquí

- La cuenta es **@app.nomad**, empresa. Bio y enlace en `campana/INSTAGRAM-ARRANQUE.md`;
  el enlace es `travelsnomad.com` a secas (decisión del dueño): la portada atribuye por
  referrer y **redirige por idioma conservando el UTM**, así que un italiano cae en `/it/`.
- **El grid se sube al revés (9 → 1)**; **las destacadas, en orden (1 → 7)**. Las once
  tarjetas de una destacada se suben primero como historias, así que son el contenido del
  día.
- **Los reels salen sin pista de audio**, a propósito: se elige dentro de Instagram, de
  tendencias, que es lo que el algoritmo premia. Un reel que parece un anuncio se salta:
  primera persona, alguien enseñando lo que ha probado.
- **Zonas seguras**: en una historia la interfaz tapa ~250 px arriba y abajo — el texto
  vive entre y=280 e y=1500 y de 1520 para abajo va el adhesivo de enlace. En un reel,
  entre 230 y 1480.
- **UTM de cada adhesivo**: `utm_source=instagram&utm_medium=organic&utm_campaign=<pieza>`,
  con `-it` al final si es italiano, y entonces el enlace apunta a `travelsnomad.com/it/`
  directamente, no a la raíz.
- **Idiomas**: español es el mercado; el italiano es una prueba con UTM propio (la mitad de
  los seguidores lo son, y ninguno se ha apuntado); francés e inglés no tienen ni una señal
  y no se doblan. La regla superficie por superficie está en `piezas/destacadas/README.md`.
- **No se compran seguidores. Nunca.**

## Las piezas y cómo se fabrican

```bash
npm install                        # ffmpeg-static, una vez
bash piezas/construir-todo.sh      # prepara salida/, escribe todas las piezas y el taller
cd salida && node ../piezas/reels/exportar-reel.mjs && bash ../piezas/reels/montar-reel.sh
```

Los generadores leen de su directorio de trabajo (`Main.dc.html` con las fuentes,
`fotos/`, `plan-900.webp`, `mark.png`…) y no saben de este repo a propósito;
`piezas/preparar.sh` monta `salida/` con eso desde `banco/`. Hasta el 1-sep todo eso vivía
en el scratchpad de una sesión y moría con ella: **el banco existe para que no vuelva a
pasar**.

**El taller** (<https://claude.ai/code/artifact/0fea041b-1676-4675-94ab-fc326d44bdb3>) es
el lienzo editable con el kit, siete plantillas y todas las piezas. **Quién manda**:
mientras el dueño no toque el lienzo, manda el generador —se rehace la pieza, se
reconstruye y se vuelve a guardar—; en cuanto edite algo en el lienzo, manda el lienzo:
antes de sembrar hay que leerlo y construir sobre lo que haya, o su edición se pierde sin
aviso. `piezas/taller/README.md` tiene el detalle.

**Fotos: sólo CC0 o dominio público**, de Wikimedia Commons, verificadas foto a foto. No
se debe atribución y no hay marca de agua, pero el crédito queda en
`banco/fotos/creditos.json` para poder demostrar la procedencia. Una foto nueva entra con
su título de Commons y su licencia en ese fichero, y en los dos tamaños: `post/`
(1080×1350) e `historia/` (1080×1920), recortada del original, no de la otra.

**Capturas: de la app real**, nunca maquetas. Están en `banco/capturas/` por pantalla e
idioma (`plan-900.webp`, `plan-900-it.webp`…). Si la app cambia una pantalla, se vuelven
a capturar; una captura vieja en un anuncio es una promesa que la app no cumple.

## Trampas ya pagadas

- **`zoompan` genera `d` frames POR CADA FRAME DE ENTRADA.** Con `-loop 1 -t 3` el primer
  reel salió de 5 minutos y 35 segundos. La entrada es UNA imagen suelta. Y el
  pre-escalado ×2 antes del `zoompan` es lo que quita el temblor.
- **El HELMET no trae emoji en color**: una carátula con 🎟 salió en blanco y negro. A 60
  px de diámetro sólo se lee una forma; las carátulas llevan la marca y se distinguen por
  el fondo. En el texto, un emoji como mucho y sólo para señalar (👇 👉), como en la bio.
- **Un velo global no basta sobre neón ni piedra labrada**, y subirlo entero deja la foto
  marrón. Va una banda oscura detrás del bloque de texto (`scrim`).
- **En el lienzo, la foto elegible por chip es una rama `<sc-if>` por foto, cada una con
  su `src` literal**: el lienzo sustituye texto literal por la imagen, no valores. Un
  `src="{{foto}}"` sale roto y sin aviso.
- **Tres postales salieron de recortes de 980×380** ampliados cinco veces en una historia.
  Las fotos de historia se recortan del original, y por eso el banco tiene los dos tamaños.
- **Commons devuelve 429 a las descargas desde el contenedor**, con y sin User-Agent. Los
  originales que hay son los que hay; una foto nueva se baja desde fuera.
- **Un `grep` encuentra la cadena también en los comentarios.** Se sonda el endpoint, no
  el fichero que lo llama. Y **una aserción se rompe a propósito antes de fiarse de ella**.

## Al trabajar

- **Commit por pieza y push según se va.** El contenedor se recicla y lo no empujado muere.
- **Nunca `git checkout -- .`, `git restore <fichero>` ni `reset --hard`** como limpieza.
- **Ningún identificador de modelo** en commits ni en ficheros.
- Los tokens (Supabase, Expo) **no se imprimen** y no entran en el repo.
- Al terminar un trabajo la issue se cierra o se comenta con su estado real; al encontrar
  algo pendiente se abre una **antes** de que se pierda en un fichero.
