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
| 0-3,6 | El verde de la oferta: el icono, «¿Qué es Nomad?» y «Ahora lo puedes probar gratis.» | — | Kore: «¿Qué es Nomad? Ahora lo puedes probar gratis.» |
| 3,6-5,9 | El tranvía de la Bica. «Tu imprescindible para viajar.» | — | «Es tu imprescindible para viajar.» |
| 5,9-8,7 | Una terraza. **09:00 · antes de salir** | El móvil sube. El plan pasa del sábado al domingo y al lunes | «Te organiza el viaje, día a día.» |
| 8,7-15,0 | La Praça do Comércio. **10:30 · en la plaza** | La presentación del paseo, «Empezar el tour», la parada 1 en el mapa y el toque de reproducir la audioguía. Arriba, lo que dice, palabra a palabra | Kore: «Te cuenta lo que tienes delante.» Charon, la audioguía: «Estás en el centro neurálgico de la reconstrucción de Lisboa.» |
| 15,0-17,8 | Pasteles de nata. **13:30 · a la hora de comer** | La lista de Lugares, y el filtro «Comida» | «Te recomienda qué ver y dónde comer.» |
| 17,8-20,2 | El puente al atardecer. **19:30 · al caer la tarde** | Gastos: lo que lleva el grupo, «Para quedar en paz» y el historial | «Lleva las cuentas del grupo.» |
| 20,2-24,1 | El elevador da Glória de noche. **23:00 · antes de dormir** | NOMAD AI: «¿Qué plan tengo mañana?» y su respuesta | «Y tienes un asistente para lo que necesites durante el viaje.» |
| 24,1-28,2 | La oferta, sobre verde: «Tu primer viaje, gratis.» y sus dos condiciones | — | «Esta semana, tu primer viaje es gratis.» |
| 28,2-31,8 | El cierre, quieto: el icono, el nombre, las dos tiendas, la oferta con sus condiciones y el precio de después | — | «Descárgala en la App Store o en Google Play.» |

Arriba, todo el rato, la firma: «Nomad · Primer viaje gratis esta semana». Los cortes salen de la voz
(`preparar-voz.py`), no al revés.

## El guion es del dueño

El 24-nov dio el esquema: «¿Qué es Nomad? Ahora lo puedes probar gratis. Nomad es tu indispensable en todos
tus viajes. Te organiza el viaje, te lo cuenta, te recomienda los mejores lugares y te deja organizar tus
gastos. Además tienes un asistente que te ayuda en todo lo que necesites durante el viaje». Se partió en
nueve frases cortas, una por momento, y lo aprobó así («el guion OK»). Dos cambios que se le dijeron:
«qué ver y dónde comer» en vez de «los mejores lugares», e «imprescindible».

## Qué es de verdad y qué no

- **Lo del móvil es la app grabada el 25-nov**, en el simulador de iPhone de un Mac de GitHub, con la
  cuenta demo y su viaje a Lisboa (guion `reel` de `capturas/` del repo de la app; pasada 45566805840).
  Nadie ha pintado nada encima.
- **Las tomas están cortadas y, alguna, un poco aceleradas.** Cada una dura lo que su frase. El plan va a
  1,23×, los lugares a 1,2× y las otras tres a su velocidad. Cuatro juntan dos trozos de la misma
  grabación, con la pantalla igual a los dos lados del corte. `tomas.json` dice qué trozos son.
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

- **La fecha, «hasta el 3 de diciembre»**, y que no haya tope a la vista. Están escritas en `index.html`
  (la oferta y el cierre). Si cambian, se cambia el texto y se vuelve a renderizar: unos diez minutos.
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

Lo que hay que llevarse: **una captura recortada y animada por encima (paneos, acercamientos, sombras) se
lee como plantilla hecha por una máquina**. La app se enseña en su pantalla, y lo que se mueve es la app,
no la cámara.

## Cómo se revisó

La primera versión la miraron cuatro revisores independientes. De ahí vienen, y siguen en ésta: el cierre
entre x=180 y x=900, las condiciones de «gratis» a la vista desde «viaje», las insignias a 30 px, las dos
líneas de marcas y el golpe de «gratis» saturado para que se oiga en un móvil.

**Esta versión no ha pasado todavía por revisores independientes.** Lo comprobado está en la issue #23:
la página pasa `hyperframes check` sin avisos, se miró un fotograma por escena con la zona segura
encima, y la mezcla se transcribió y se midió.

## Cómo se rehace

```bash
bash ../construir.sh                                  # las fuentes embebidas
python3 -I preparar-voz.py                            # las diez frases, sus tiempos y los cortes
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
- **Una toma tiene que llenar el móvil.** Lo que se ve del móvil son 1.190 px. Si se enseña la pantalla
  desde muy abajo, la grabación se acaba antes y queda un hueco. `cortar-tomas.py` se para si pasa.
- **Un texto centrado no está dentro de la zona segura por estar centrado.** La zona es asimétrica: por
  debajo de y=900 acaba en x=900.
- **Un efecto grave se comprueba en la banda que reproduce un móvil** (de 150 Hz para arriba).
