# Tu viaje, día a día: el vídeo B de «Lo que incluye tu viaje» (29-oct)

Un vídeo de **30,5 s** (todo a 1,15×), 1080×1920, 30 fps, H.264 + AAC, con la voz y la música dentro,
para Instagram (reel e historia) y TikTok. Es el segundo de la serie de la issue #18. **Lo común con el
vídeo A está explicado en `../incluye-pago/README.md`**: el encargo, por qué la línea dibuja la pantalla
y no un iPhone, por qué las tomas van recortadas, de dónde salen las grabaciones, la voz, la música y su
junta, y cómo se rehace. Aquí va lo propio de B.

La idea: le dices a dónde vas, cuántos días y cómo te gusta viajar; te propone los imprescindibles y
quitas los que no quieras; y te sale el viaje entero, día a día y en su orden.

Cómo se publica, con los pies listos para copiar: `PUBLICAR.md`.

## Tres versiones, que sólo cambian en el cierre

| fichero (en `salida/`) | para |
|---|---|
| `nomad-dia-historia-1080x1920.mp4` | historia de Instagram: acaba en dos flechas hacia el adhesivo de enlace |
| `nomad-dia-reel-1080x1920.mp4` | reel de Instagram y TikTok: acaba en «Enlace en el perfil» |
| `nomad-dia-limpia-1080x1920.mp4` | TikTok sin el campo «Sitio web», o una promoción pagada: sin flechas ni texto |
| `nomad-dia-portada.jpg` | la portada del reel: «Tu viaje, / día a día.» |

## El guion

Los segundos son los del vídeo final. La pantalla está a la izquierda todo el rato, y la línea dibuja a
su derecha.

| segundos | Kore | texto abajo | la pantalla | lo que dibuja la línea al lado |
|---|---|---|---|---|
| 0-2,1 | «Esto es Nomad.» | «Nomad: guía de viajes» / «Ya en la App Store, para iPhone» | — | la espiral de «Un trazo» |
| 2,1-7,2 | «Le dices a dónde vas, cuántos días y cómo te gusta viajar.» | «Tú eliges.» | los pasos 1 y 2 de crear un viaje: Lisboa, las fechas y las preferencias | el collar de «Un trazo» en vertical: Lisboa, 3 días, Cultural y Gastronomía, que se ponen verdes cuando Kore las nombra |
| 7,2-11,7 | «Te propone los imprescindibles, y el que no quieras, lo quitas.» | «Te propone / los imprescindibles.» | el paso 4: «Imprescindibles de Lisboa · Todos marcados. Toca uno para dejarlo fuera del plan.» | una estrella que se rellena de verde, como la de imprescindible del plan |
| 11,7-15,9 | «Y te escribe el viaje entero, día a día.» | «Y te sale el plan entero, / día a día.» | el plan del sábado 21 | un raíl con las cinco horas del plan: 10:30, 13:30, 15:15, 16:30 y 20:30 |
| 15,9-20,6 | «Cada día, en su orden, para no cruzar la ciudad dos veces.» | «Cada día, en su orden, / para no dar vueltas.» | el plan del jueves 26 | un camino que pasa por cinco paradas numeradas |
| 20,6-25,9 | «Y lo pagas una vez, para todo el grupo: desde dos noventa y nueve.» | «Un pago, / para todo el grupo.» | se apaga; la línea se come el borde | un subrayado y cuatro personas; cuando Kore dice «desde», «desde» / «2,99 €» / «por viaje, sin suscripción» |
| 25,9-30,5 | «Nomad. Ya en la App Store, para iPhone.» | el cierre de «Un trazo» | — | el cierre aprobado, con «Secuencias acortadas.» |

`f1`, `f2`, `f3` y `f9` son tomas de «Un trazo», comprobadas allí. Como B0 y B1 duran lo mismo que la
apertura y «Tú eliges» de «Un trazo», los tiempos de las palabras de `f2` (`TELIGE` en `index.html`)
sirven tal cual. Las nuevas:

| frase | toma | dura (1×) |
|---|---|---|
| «Te propone los imprescindibles, y el que no quieras, lo quitas.» | b3-3 | 4,42 s |
| «Cada día, en su orden, para no cruzar la ciudad dos veces.» | b5-1 | 4,51 s |
| «Y lo pagas una vez, para todo el grupo: desde dos noventa y nueve.» | b6-3 | 5,33 s |

Lo comprobado contra el código de la app: los imprescindibles salen todos marcados y se quita uno con un
toque (es lo que dice el paso 4 en pantalla); el plan va por días y con su hora
(`_shared/itinerarySchema.ts`); el pago es del viaje y vale para todo el grupo (`_shared/premium.ts`);
los tramos, 2,99 / 4,99 / 6,99 € (`comprasSueltasReglas.ts`). Dos frases cambiaron en la revisión de
verdad: «tú decides cuáles entran» pasó a «el que no quieras, lo quitas» (todos entran de salida), y
«sin dar vueltas», a «para no dar vueltas».

## Las tomas

Salen de `recorrido-crear`, `recorrido-paseo` y `recorrido-museo` (cómo bajarlas y cortarlas, en el
README de A). `tomas.json`:

| toma | de dónde | qué se ve |
|---|---|---|
| b1a | crear 20,35-22,80 | se elige Lisboa, baja el teclado: 29 oct-31 oct, llegada y salida |
| b1b | crear 25,29-29,16 | el paso 2: estilo, deportes, ritmo y presupuesto |
| b2 | crear 47,65-49,65 | el paso 4, con los imprescindibles y el resumen, a media velocidad |
| b3 | paseo 24,90-28,91 | el plan del sábado 21 (la misma pantalla que en A) |
| b4 | museo 11,08-12,42 | el plan del jueves 26, quieto, a cámara lenta |

Lo de antes de 20,30 en crear («Sin resultados» y la carga) queda fuera, y también Mis viajes, que
sale de 46,7 a 47,1 y desde 49,9 con el código de invitación.

## Lo que queda a la vista, y es sabido

- **Salen dos viajes distintos**: la creación es «Fin de semana en Lisboa», del 29 al 31 de octubre, y
  el plan es el del viaje de ejemplo, del 21 al 28 de noviembre. El dueño lo aceptó para montar ya
  («Monta ya con lo que hay»). Lo arregla grabar la creación con el 21-28 nov en la próxima pasada de
  capturas, que el vídeo C necesita de todas formas.
- **Dos pantallas quietas a cámara lenta**: b2 a 0,44× y b4 a 0,29×. Medido, no se mueve nada; las
  sostiene la línea. Si se sienten paradas, se acorta la frase o se quita la toma.
- La letra de la app, pequeña; el mapa del plan con nombres de comercios. Lo mismo que en A.
