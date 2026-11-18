# El puente, ya organizado (18-nov) — EN OBRAS

Un reel de unos **30 s** para el puente de diciembre: «Viajes listos» y el viaje de Viena, con la app de
verdad en pantalla, la voz de Kore y la música de «Un trazo». Es el molde de «Así funciona»
(`../asi-funciona/`): el logo que se hace hilo, las tomas de la app dentro del borde, un dibujo editorial
por escena a la derecha, el texto de abajo en dos líneas y el cierre.

**Estado, 18-nov por la tarde:** montado entero menos las tomas. La página, los dibujos, la voz y la mezcla
están; donde va la app hay rectángulos provisionales (`tomas.json` dice «PROVISIONAL» en cada una). Las
tomas salen de `capturas/viena.sh` del repo de la app, en dos pasadas (NOMAD, `capturas/README.md`).

## Por qué se rehízo

La primera versión (esa mañana, commits `1e6568d` y `0e2fe19`) era de fotos de Viena con texto encima y
una voz que enumeraba los días. El dueño la vio y dijo: «la idea está bien, el texto que se narra deja que
desear y sólo fotos se nota que es pura IA. Tampoco hay nada de la app real». Lo que cambia:

- **La app de verdad, grabada**, en el molde que él ya aprobó frase a frase. Sin fotos.
- **Otra narración**, escrita por un panel de cuatro guionistas y tres jueces (el oído, el gancho y la
  verdad) con las frases de «Así funciona» como listón. Siete frases, en segunda persona, cada una con
  una cosa que la app hace.
- **La voz, con el estilo de la casa** («Locuta un vídeo corto para redes, cercana…»). La primera versión
  se grabó sin él.

## El guion

Los cortes salen de la voz: cada escena dura su frase más 0,55 s (a 1×).

| n | Kore dice | abajo | a la derecha | toma de la app |
|---|---|---|---|---|
| 1 | ¿Llega el puente de diciembre y nadie del grupo ha organizado nada? | ¿Puente de diciembre / y nada organizado? | el logo que se hace hilo y dibuja el borde | — |
| 2 | En Nomad hay viajes listos, como Viena en tres días. | Viajes listos, / como Viena en 3 días. | el pin; late con «Viena» | «Viajes listos», bajando hasta Viena |
| 3 | Le pones tu fecha, lo pagas una vez y vale para todo el grupo. | Tu fecha y un pago / para todo el grupo. | el calendario: DIC 2026, sábado 5, domingo 6 y lunes 7 | la hoja de Viena con el 5 de diciembre, y la de pago |
| 4 | Ahí lo tienes: qué ver, a qué hora y dónde comer. | Qué ver, a qué hora / y dónde comer. | los cinco planes del sábado unidos por una curva, con sus horas | el itinerario del sábado 5 |
| 5 | En los paseos y en los museos, una audioguía te cuenta lo que tienes delante. | Una audioguía / en paseos y museos. | los auriculares | la guía del paseo por el centro histórico |
| 6 | ¿Te apetece un mercadillo de Navidad? Pídeselo al asistente y te lo añade. | ¿Un mercadillo? / Pídeselo al asistente. | el robot pequeño | NOMAD AI con la petición y su tarjeta |
| 7 | Nomad. Descárgala gratis en la App Store. | (el cierre) | | |

`assets/voz/v6b.flac` es la frase de reserva de la escena 6 («¿Quieres cambiar algo? Pídeselo al asistente y
te cambia el plan al momento.»), por si la toma no enseña el mercadillo añadido.

## Lo que el vídeo no puede dar a entender

- Que el plan se ve o se copia gratis: el pago va en la misma frase que la fecha, antes del plan.
- Que los mercadillos vienen en el viaje: se le piden al asistente.
- Ninguna fecha cerrada del puente: el lunes 7 sólo es festivo en diez comunidades.

## Cómo se rehace

```bash
bash ../construir.sh                                    # las fuentes embebidas
python3 -I iconos/datos.py                              # los dibujos, desde iconos/editorial.json
METRAJE=<carpeta> python3 -I cortar-tomas.py            # las tomas, desde tomas.json
python3 -I poner-tomas.py                               # los <video> de index.html, desde tomas.json
bash mezclar.sh                                         # assets/sonido.m4a: voz y música
bash variantes.sh <salida>                              # las versiones y los fotogramas de revisión
```
