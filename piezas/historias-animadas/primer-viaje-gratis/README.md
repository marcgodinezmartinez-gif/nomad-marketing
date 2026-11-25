# Tu primer viaje, gratis (25-nov) — el reel del Black Friday

Un reel de **32 s** para la semana del Black Friday: el primer viaje de cada cuenta es gratis (NOMAD#479).
Los textos de la campaña están en la issue #23.

**Lo pidió el dueño así** (24-nov): montado entero aquí, sin ningún vídeo suyo, antes de tocar la app, y que
enganche. Por eso la pantalla de pago con «Gratis» no sale: todavía no existe en ningún móvil, y una
captura inventada sería una maqueta. La oferta va en una tarjeta de texto.

## La idea: un día de viaje

Un día en Lisboa, de la mañana a la noche. En cada momento del día, una foto de la ciudad, la hora, lo que
hace Nomad en ese momento y, en un móvil, **la app haciéndolo de verdad** (grabada, no capturas quietas).

| seg. | la foto y la hora | en el móvil | qué se oye |
|---|---|---|---|
| 0-2,9 | **El gancho**, sobre el verde de la oferta, ya en el fotograma 0: el icono, «Tu primer viaje con Nomad, **gratis.**» y debajo sus dos condiciones. «gratis» late cuando suena | — | Kore: «Tu primer viaje con Nomad, gratis.» |
| 2,9-6,3 | El tranvía de la Bica. «¿Qué es Nomad?» y, con su voz, «Tu imprescindible para viajar.» | — | «¿Qué es Nomad? Tu imprescindible para viajar.» |
| 6,3-9,1 | Una terraza. **09:00 · antes de salir** | El móvil sube. El plan pasa del sábado al domingo y al lunes | «Te organiza el viaje, día a día.» |
| 9,1-15,4 | La Praça do Comércio. **10:30 · en la plaza** | El plan del sábado, «Iniciar tour», «¿Qué visita quieres?», y la parada 1 en el mapa con el toque de reproducir la audioguía. Arriba, lo que dice, palabra a palabra | Kore: «Te cuenta lo que tienes delante.» Charon, la audioguía: «Estás en el centro neurálgico de la reconstrucción de Lisboa.» |
| 15,4-18,2 | Pasteles de nata. **13:30 · a la hora de comer** | La lista de Lugares y, al tocar «Comida», sólo los sitios para comer | «Te recomienda qué ver y dónde comer.» |
| 18,2-20,6 | El puente al atardecer. **19:30 · al caer la tarde** | Gastos: lo que lleva el grupo, «Para quedar en paz» y el historial | «Lleva las cuentas del grupo.» |
| 20,6-24,5 | El elevador da Glória de noche. **23:00 · antes de dormir** | NOMAD AI: «¿Qué plan tengo mañana?» y su respuesta | «Y tienes un asistente para lo que necesites durante el viaje.» |
| 24,5-28,6 | La oferta, sobre verde: «Tu primer viaje, gratis.» y sus dos condiciones | — | «Esta semana, tu primer viaje es gratis.» |
| 28,6-32,2 | El cierre, quieto: el icono, el nombre, las dos tiendas, la oferta con sus condiciones y el precio de después | — | «Descárgala en la App Store o en Google Play.» |

Arriba, durante el día de viaje (del 2,9 al 24,5), la firma: «Nomad · Primer viaje gratis hasta el 3 de
diciembre». Los cortes salen de la voz (`preparar-voz.py`), no al revés.

## El guion es del dueño

El 24-nov dio el esquema: «¿Qué es Nomad? Ahora lo puedes probar gratis. Nomad es tu indispensable en todos
tus viajes. Te organiza el viaje, te lo cuenta, te recomienda los mejores lugares y te deja organizar tus
gastos. Además tienes un asistente que te ayuda en todo lo que necesites durante el viaje». Se partió en
nueve frases cortas, una por momento, y lo aprobó así («el guion OK»). Dos cambios que se le dijeron:
«qué ver y dónde comer» en vez de «los mejores lugares», e «imprescindible».

**Y el 25-nov, al ver la cuarta versión: «el gancho de que es gratis tiene que ser lo primero para retener
a la gente».** Antes abría con «¿Qué es Nomad? Ahora lo puedes probar gratis.», y «gratis» se oía en el
segundo 2,9 y se leía en el 2,4. Ahora la primera frase es la oferta, «Tu primer viaje con Nomad,
gratis.», y está entera en pantalla desde el fotograma 0, con sus condiciones. La pregunta pasa a la
segunda frase, con su respuesta: «¿Qué es Nomad? Tu imprescindible para viajar.»

## Qué es de verdad y qué no

- **Lo del móvil es la app grabada el 25-nov**, en el simulador de iPhone de un Mac de GitHub, con la
  cuenta demo y su viaje a Lisboa (guion `reel` de `capturas/` del repo de la app; pasada 45566805840).
  Nadie ha pintado nada encima.
- **Las tomas están cortadas y, alguna, un poco aceleradas.** Cada una dura lo que su frase. El plan va a
  1,23×, los lugares a 1,2× y las otras tres a su velocidad. Tres juntan dos trozos de la misma
  grabación. En dos (el plan y el asistente), la pantalla es la misma a los dos lados del corte.
  `tomas.json` dice qué trozos son.
- **La del paseo da un salto.** Pasa de «¿Qué visita quieres?» a la parada 1. En medio, en la app, se
  elige la duración, se espera a que el tour esté hecho y sale su presentación. Eso no está en el vídeo.
- **La espera de NOMAD AI está acortada.** En la grabación, la respuesta tarda 2,8 s desde la pregunta.
  En el vídeo, 1,6 s: se quitaron 1,2 s de «Pensando…». La pregunta y la respuesta son las de verdad.
- **La voz de la audioguía no es el sonido del simulador**, que graba sin sonido. Es la misma voz de la
  app (Charon), con el modelo de la app y su instrucción de tono, diciendo la primera frase de «La
  historia» de esa parada, que se lee al pie de la pantalla. En el móvil se ve el toque de reproducir.
- **Las horas son del relato, no de la app.** Las 10:30 y las 13:30 coinciden con el plan del sábado que
  sale en el móvil (el paseo y la comida); las demás las pone el vídeo. Lo que enseña cada pantalla es lo
  que tenía el viaje demo ese día: el asistente contesta por «mañana jueves, 26 de noviembre».
- **Las fotos son de Lisboa, de Unsplash y de Pexels**, y van quietas y a sangre. Su origen está en
  `banco/fotos/creditos.json` (las seis `f-lisboa-*`). No son de la app ni del viaje demo.
- **Las dos voces son voces de la app** (`mobile/src/lib/narrationVoices.ts`: Kore, Puck y Charon), con el
  modelo de la app (`gemini-3.1-flash-tts-preview`), a 1,15×.
- **La música es de Lyria** (`lyria-3-clip-preview`, `musica-prompt.txt`) y las voces son sintéticas. Al
  publicar se marca la etiqueta de contenido hecho con IA.
- **No sale ningún código de invitación, correo ni apellido.** Las grabaciones empiezan y acaban en
  «Hoy», donde está el código del viaje demo: de ahí no se usa nada. En Gastos sale «María», el nombre
  de pila de la otra cuenta de la demo.

## Lo que el vídeo no puede dar a entender

- Que «gratis» es para siempre o para todos los viajes: las dos condiciones van escritas en la oferta y
  otra vez en el cierre (un viaje por cuenta, hasta el 3 de diciembre).
- Nada de «lista de espera» ni de 1,99 €. El precio, «desde 2,99 € el viaje».

## Lo que falta por confirmar (es del dueño)

- **La fecha, «hasta el 3 de diciembre».** Está escrita en `index.html` (la firma, la oferta y el
  cierre). Si cambia, se cambia el texto y se vuelve a renderizar: unos diez minutos. La voz dice «esta
  semana», que es su frase; si la promoción dura bastante más de una semana, hay que regrabarla.
- **El tope de 300 viajes gratis.** La migración de NOMAD#479 corta la promoción al llegar a 300, y el
  vídeo no lo dice. O se sube a un número que no se alcance, o el vídeo y el anuncio tienen que decir
  «para los 300 primeros».
- **«Tu primer viaje» deja fuera a quien ya compró uno.** Así lo hace la app. El vídeo dice «un viaje
  gratis por cuenta»; el pie lo aclara.
- **Que una instalación nueva vea «Gratis» en su primera sesión.** La app de las tiendas espera 5 s a la
  actualización al abrirse por primera vez; con mala red, enseña el precio hasta la segunda apertura
  (está apuntado en NOMAD#479). Se comprueba instalando desde la tienda en un móvil limpio.
- **El vídeo no se publica hasta que la promoción esté encendida** (NOMAD#479). Antes, anuncia algo que
  la app no hace.
- **Cómo suena.** Las voces, la música y los efectos están transcritos y medidos, pero no los ha oído una
  persona.

## Cómo se llegó hasta aquí (24 y 25-nov)

Cuatro vueltas, y en cada una mandó lo que dijo el dueño al verla:

1. La app en recuadros con sombra, con la vista bajando y acercándose. **«No se ve guay así como en
   cuadrados las capturas de la app. Se notan demasiado con IA».**
2. La pantalla entera en el molde de «Así funciona», con capturas quietas. Pidió otro gancho: **«¿Qué es
   Nomad? … esta semana tienes la oportunidad de conocerlo gratis. Eso hará que la gente se quede de
   primeras».**
3. Con ese gancho y un chat de IA de contraste. **«El guion no me gusta»**, y dio el suyo. Después, del
   montaje: **«el que me habías montado no me gusta»**.
4. Se le enseñaron tres estilos en un fotograma cada uno. Dijo **«haz lo que creas que será mejor»**. Se
   eligió éste, y grabar la app en vez de usar capturas.
5. Con éste montado: **«el gancho de que es gratis tiene que ser lo primero para retener a la gente»**.
   El vídeo abre con la oferta, y la pregunta va después.

Lo que hay que llevarse: **una captura recortada y animada por encima (paneos, acercamientos, sombras) se
lee como plantilla hecha por una máquina**. La app se enseña en su pantalla, y lo que se mueve es la app,
no la cámara.

## Cómo se revisó

La primera versión la miraron cuatro revisores independientes. De ahí vienen, y siguen en ésta: el cierre
entre x=180 y x=900, las condiciones de «gratis» a la vista desde «viaje», las insignias a 30 px, las dos
líneas de marcas y el golpe de «gratis» saturado para que se oiga en un móvil.

Esta versión la miraron otros cuatro, cada uno con una cosa: quien la ve sin sonido, las reglas de la
casa, lo que promete frente a lo que hace la app, y que la pieza cuadre por dentro. Los siete hallazgos
serios los intentó tumbar un escéptico cada uno: los siete se sostuvieron, casi todos con matices. Lo
que se cambió:

- **La línea de marcas de Google se salía por la derecha** («LLC.» caía bajo los botones). Las tres
  líneas van ahora en la columna del resto del cierre.
- **La respuesta del asistente quedaba por debajo de la zona segura.** La toma se enseña desde más
  abajo y caben la pregunta y cuatro de los cinco planes.
- **El filtro de «Comida» se veía medio segundo.** Fuera el arrastre de la lista: ahora se ve la lista
  un segundo y el filtro casi dos.
- **Encima del plan asomaba una franja de mapa con rótulos partidos.** El plan, los lugares y los
  gastos arrancan en su cabecera.
- **La firma decía «esta semana» y la oferta «hasta el 3 de diciembre».** La firma lleva la fecha.
- **«Tu primer» y «viaje,» salían antes de oírse.** La oferta entra palabra a palabra con la voz.
- **Las palabras de la audioguía que aún no han sonado** se leían poco sobre la fachada: del 40 al 55 %.
- **`preparar-voz.py` pisaba la duración de las tomas** al volver a pasarlo. Ya sólo escribe la del
  vídeo y la del sonido.

Dos hallazgos más los resolvió después el dueño al pedir «gratis» lo primero: el gancho ya no dice
«gratis» sin sus condiciones, y ya no tarda tres segundos en decir qué se ofrece.

Lo que dijeron y se deja, porque es de gusto o del dueño: que la app no se ve hasta el segundo 6; que
seis escenas con la misma composición se leen como
plantilla; que el cierre cambia de fondo de golpe; que «Lugares · 14 guardados» parece una lista de
favoritos más que de recomendaciones; y lo de «Lo que falta por confirmar», más arriba.

**Lo que nadie ha comprobado**: cómo suena, y cómo se ve en un móvil.

## Cómo se rehace

```bash
bash ../construir.sh                                  # las fuentes embebidas
python3 -I preparar-voz.py                            # las diez frases, sus tiempos y los cortes (y la
                                                      # duración del vídeo en index.html)
python3 -I mezclar.py                                 # assets/sonido.m4a y assets/sonido-sin-musica.m4a
METRAJE=<carpeta> python3 -I cortar-tomas.py          # sólo si cambian las tomas o los cortes
bash variantes.sh <salida>                            # los vídeos, la portada y los fotogramas de revisión
```

Para cambiar un texto (la fecha) basta el último paso. Las cinco tomas cortadas están en `assets/tomas/`.
Las grabaciones enteras no están en el repo (ver `banco/metraje/README.md`): se sacan otra vez con el
flujo «Capturas de la app» del repo de la app, guion `reel`. Si cambian los cortes de la voz, las tomas
hay que cortarlas otra vez, porque cada una dura lo que su frase.

Las tomas crudas de voz que no se eligieron no se versionan: se regraban con `../../ia/voz.py`.

## Lo que se aprendió montándolo

- **Una grabación del simulador sólo guarda un fotograma cuando la pantalla cambia.** Pedirle a ffmpeg «el
  fotograma del segundo 30» devuelve el siguiente que haya, que puede ser de dos segundos después. Y un
  trozo que empieza con la pantalla quieta pierde esa espera. Antes de buscar momentos o de cortar, se
  pasa a ritmo fijo (`fps=30`).
- **Grabar no obliga a compilar la app.** El flujo de capturas guarda la app compilada. Con `app_de` se le
  pide la de un commit que ya esté guardada. Esta pasada fueron 11 minutos de Mac, y cada minuto de Mac
  cuenta por diez.
- **El plan se abre en HOY cuando el viaje está en curso**, no en el primer día. El guion de la grabación
  toca el día que quiere enseñar.
- **Dentro de una hoja que se arrastra, Maestro no ve casi nada**: los toques van por coordenadas.
- **Los momentos se buscan en la grabación entera, no en una copia reducida.** Se buscaron en copias a
  10 fotogramas por segundo y a 240 px, y el toque de reproducir salía 1,7 s más tarde de donde está.
  Medido otra vez sobre la grabación (`fps=30` y la diferencia entre fotogramas), cuadró a la primera.
  Y la toma cortada se mira entera, en una hoja de fotogramas, antes de renderizar.
- **La portada de un tour en la app es una foto de Commons, y puede ser CC BY-SA.** La del paseo por la
  Baixa lo es (se lee su crédito en la pantalla). En este repo esas fotos sólo entran si lo decide el
  dueño, así que la presentación del paseo no sale: la toma arranca antes y sigue después.
- **Una toma tiene que llenar el móvil.** Lo que se ve del móvil son 1.190 px. Si se enseña la pantalla
  desde muy abajo, la grabación se acaba antes y queda un hueco. `cortar-tomas.py` se para si pasa.
  Alargarla repitiendo su última fila no vale: esa fila lleva texto y salen rayas.
- **La zona segura se mira en cada escena, no sólo en las de texto.** Se miró en la oferta y en el
  cierre, y lo que quedaba fuera era la respuesta del asistente, dentro del móvil. `variantes.sh` saca
  ya ese fotograma con la zona encima.
- **Quitarle un aviso al comprobador no arregla lo que avisaba.** Las líneas de marcas llevan
  `data-layout-ignore` porque su letra es pequeña a propósito. Con eso tampoco se vio que una se salía.
- **Dos elementos con el mismo id no avisan.** El gancho nuevo se escribió con `#h-1` y `#h-2`, y `#h-2`
  ya era la hora «09:00 · antes de salir». Su estilo se aplicó a las dos: la hora salió enorme encima del
  título y «con Nomad,» desapareció del gancho. `hyperframes check` pasó. Se vio en los fotogramas.
- **Un texto centrado no está dentro de la zona segura por estar centrado.** La zona es asimétrica: por
  debajo de y=900 acaba en x=900.
- **Un efecto grave se comprueba en la banda que reproduce un móvil** (de 150 Hz para arriba).
