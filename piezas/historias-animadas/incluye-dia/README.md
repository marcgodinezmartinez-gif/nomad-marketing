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
| 2,1-7,2 | «Le dices a dónde vas, cuántos días y cómo te gusta viajar.» | «Tú eliges.» | los pasos 1 y 2 de crear un viaje: Lisboa, las fechas y las preferencias | el collar de «Un trazo» en vertical: Lisboa, 3 días, Cultural y Gastronomía, que se ponen verdes cuando Kore las nombra y laten juntas al final |
| 7,2-11,7 | «Te propone los imprescindibles, y el que no quieras, lo quitas.» | «Te propone / los imprescindibles.» | el paso 4: «Imprescindibles de Lisboa · Todos marcados. Toca uno para dejarlo fuera del plan.» | una estrella que se rellena de verde, como la de imprescindible del plan, y se vacía en «lo quitas» |
| 11,7-15,9 | «Y te escribe el viaje entero, día a día.» | «Y te sale el plan entero, / día a día.» | el plan del jueves 26 | un raíl con las cinco horas de ese plan: 10:00, 12:30, 13:45, 15:30 y 20:30 |
| 15,9-20,6 | «Cada día, en su orden, para no cruzar la ciudad dos veces.» | «Cada día, en su orden, / para no dar vueltas.» | el plan del sábado 21: Baixa, Comercio, Santa Justa y Chiado, todo a mano | un camino que baja por cinco paradas numeradas, en su orden y sin volver atrás |
| 20,6-25,9 | «Y lo pagas una vez, para todo el grupo: desde dos noventa y nueve.» | «Un pago, / para todo el grupo.» | se apaga; la línea se come el borde | un subrayado del que bajan cuatro personas, que brotan en «para todo el grupo»; en «desde», «desde» / «2,99 €» / «por viaje, sin suscripción» |
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
| b1a | crear 20,85-23,30 | Lisboa ya elegida, sin teclado: 29 oct-31 oct, llegada y salida |
| b1b | crear 25,29-29,16 | el paso 2: estilo, deportes, ritmo y presupuesto |
| b2 | crear 47,65-49,65 | el paso 4, con los imprescindibles y el resumen, a media velocidad |
| b3 | museo 11,08-12,42 | el plan del jueves 26, quieto, a cámara lenta |
| b4 | paseo 24,90-28,91 | el plan del sábado 21 (la misma pantalla que en A) |

Lo de antes de 20,85 en crear queda fuera: «Sin resultados», la carga y **el teclado**, que es el de
iOS 18 (el simulador de esa pasada) y Apple pide pantallas del sistema más nuevo. También queda fuera
Mis viajes, que sale de 46,7 a 47,1 y desde 49,9 con el código de invitación.

## Lo que dijo la revisión (29-oct)

Lo común con A, en `../incluye-pago/README.md` (las motas de la línea, el crédito de Android, la frase
18 px más arriba). Lo propio de B:

- **El día de «para no cruzar la ciudad dos veces» era el jueves 26**, que vuelve 3 km al oeste para
  cenar en Alcântara, pasado el museo de la mañana: lo contrario de lo que dice Kore, para quien conozca
  Lisboa. Se cambiaron las tomas: el jueves va en «te escribe el viaje entero» y el sábado, compacto,
  en «en su orden». Y el camino de esa escena baja en orden en vez de ir de lado a lado, que además era
  el mismo dibujo que el paseo de A.
- **El teclado de iOS 18** asomaba 0,3 s al encenderse la pantalla. La toma empieza ahora cuando ya ha
  bajado.
- **«Lo quitas» no pasaba en ningún sitio**: la estrella se vacía ahora en esa palabra.
- **Las personas llegaban antes de «para todo el grupo»**, y el subrayado se quedaba solo 2,8 s: ahora
  las hebras bajan despacio y las personas brotan en esas palabras.
- **Tramos quietos** de 0,8-1,1 s (el collar entero, el precio): laten.
- El subrayado se cruzaba con el borde al apagarse la pantalla, y la pantalla se encendía un fotograma
  antes de su toma.

## Lo que queda a la vista, y es sabido

- **Salen dos viajes distintos**: la creación es «Fin de semana en Lisboa», del 29 al 31 de octubre, y
  el plan es el del viaje de ejemplo, del 21 al 28 de noviembre. El dueño lo aceptó para montar ya
  («Monta ya con lo que hay»). Lo arregla grabar la creación con el 21-28 nov en la próxima pasada de
  capturas, que el vídeo C necesita de todas formas.
- **Cuatro de las cinco tomas están quietas**: b1a, b2 a 0,44×, b3 a 0,32× y b4 a 0,86× (en ésta sólo
  se oscurece el botón «Iniciar tour»). Sólo se mueve b1b, con los dos toques. Las sostiene la línea,
  que late en las pausas.
- **En la app se paga antes de ver el plan**: al tocar «Generar viaje» sale la hoja de pago. El vídeo
  se la salta (con «Secuencias acortadas») y no dice cuándo se paga; el pie dice «se paga al generarlo».
- La letra de la app, pequeña; el mapa del plan con nombres de comercios. Lo mismo que en A.
