# «¿Conocías este lugar?» — la Plaça del Diamant (6-sep)

Idea del dueño: un carrusel sobre **un sitio poco conocido pero con mucho valor cultural**,
con el gancho «¿Conocías este lugar?», y el cierre enseñando **ese mismo sitio explicado en
un tour de la app**. Es el mejor formato que ha salido, por una razón medible: **el post
vale por sí solo aunque nadie se descargue nada**, que es lo que arregla los cero
guardados del reel. Y Barcelona es el mercado; Roma era contenido bonito para gente que no
compra.

## Los hechos, verificados

Tres capas en una plaza de barrio de Gràcia:

1. **Doce metros bajo el suelo hay un refugio antiaéreo, el 232.** Lo cavaron los propios
   vecinos durante la Guerra Civil y cabían más de doscientas personas. **Se descubrió en
   1992, haciendo obras.** Barcelona llegó a tener unos 1.300 refugios, más de 90 sólo en
   Gràcia; fue una de las primeras ciudades del mundo bombardeadas sistemáticamente desde
   el aire. Se visita **los domingos, con reserva**, con el Taller d'Història de Gràcia.
2. **Aquí empieza *La plaça del Diamant*** de Mercè Rodoreda (1962), la novela más leída
   en catalán, traducida a más de treinta idiomas. La escultura de la plaza es **la
   Colometa**, de Xavier Medina-Campeny (hecha en 1984, instalada en 1990): la
   protagonista atrapada contra un muro mientras las palomas levantan el vuelo.
3. **El nombre lo puso un joyero.** En 1860 Josep Rosell compró estos terrenos y bautizó
   las calles de Gràcia con nombres de piedras preciosas.

Fuentes: Ajuntament de Barcelona (visitas al refugio), Taller d'Història de Gràcia,
Wikipedia (Plaza del Diamante). **Nada de esto se escribe de memoria**: si se cambia una
cifra, se vuelve a comprobar.

## Las fotos: de Unsplash y Pexels (decidido el 6-sep, buscadas y puestas el 7-sep)

Se probó CC0 y no da: 370 candidatas de Barcelona en Openverse y lo usable era **un
edificio de Gran de Gràcia fotografiado tres veces**. El dueño, viendo las de Commons de
la plaza: *«se ven cutres todas»* — y tiene razón, porque **Commons es una enciclopedia,
no un banco de imágenes**: sus fotos existen para documentar. Regla ampliada en AGENTS.md.

**De la Plaça del Diamant no hay ni una foto libre, en ningún sitio.** Buscado el 7-sep:
Unsplash devuelve el pomo de una puerta; Pexels y Pixabay rellenan con la Laguna del
Diamante (Argentina), Colonia del Sacramento y glaciares; Flickr con licencia CC0 o
dominio público no tiene ninguna. Las 14 de Commons son CC BY-SA. De **Gràcia**, en
cambio, sí hay: el campanar de la plaça de la Vila entre plátanos, la Casa Vicens y
Barcelona al anochecer desde el Park Güell, que es Gràcia. El resto son calles, balcones y
patios de Barcelona sin barrio declarado. **Cada una se miró antes de entrar** y las nueve
se verificaron en su página («Free to use under the Unsplash License» / «Free to use» en
Pexels); autor y página quedan en `banco/fotos/creditos.json`, en los dos tamaños del
banco, recortadas del original.

| Fichero | Tarjeta | Qué es | Autor · fuente |
|---|---|---|---|
| `f-bcn-plaza.jpg` | 1 · la portada | El campanar de la plaça de la Vila de Gràcia, entre plátanos | Aaron Porras · Pexels |
| `f-bcn-noche.jpg` | 2 · 12 m | Un callejón mojado de noche, con luces | Alex Quezada · Unsplash |
| `f-bcn-patio.jpg` | 3 · 1992 | Los tejados y el patio de una manzana, desde arriba | Deyan Sight · Unsplash |
| `f-bcn-balcon.jpg` | 4 · 1962 | Balcones con plantas al sol: el terrat de la Colometa | Casper van Battum · Unsplash |
| `f-bcn-calle.jpg` | 5 · 1860 | Una calle estrecha con árboles y bolardos: las que bautizó el joyero | Herr Kirlian · Unsplash |
| `f-bcn-paseo.jpg` | 6 · la app | Gente andando bajo un arco del casco antiguo; va detrás del móvil | Lisa van Vliet · Unsplash |
| `f-bcn-cierre.jpg` | 7 · el cierre | Barcelona al anochecer desde el Park Güell | Lief Peng · Unsplash |
| `f-bcn-festa.jpg` | reserva | Un callejón con banderines, para cuando toque la Festa Major | Henrique Ferreira · Unsplash |
| `f-bcn-vicens.jpg` | reserva | La Casa Vicens, la primera casa de Gaudí, en Gràcia | Ogy Kovachev · Pexels |

**La portada no es la plaza, y por eso no dice «¿Conocías este lugar?»**: enseñar otra
plaza y decir «este lugar» es lo único que no se puede. Dice «Aquí hay algo que casi nadie
sabe» —«aquí» es el barrio, y el campanar lo reconoce cualquiera de Gràcia— y la plaza se
nombra en la tarjeta 2. **Si el dueño la fotografía él** (diez minutos en Gràcia, y de paso
la Colometa y la boca del refugio), se cambia `FOTOS[1]` en `gen-diamant.py` y vuelve la
pregunta original.

**El plano del refugio ya no va.** Es CC BY-SA 3.0: exige atribución y ShareAlike, y la
regla ampliada lo sigue dejando fuera. La tarjeta 3 lleva foto como las demás.

## Qué pedirle a la app

El objetivo es **una captura donde la Plaça del Diamant salga como parada de un tour, con
su texto de LA HISTORIA**. Esa captura es la tarjeta 6, y es lo que convierte el cierre en
una prueba en vez de una promesa.

1. **Nuevo viaje → destino `Barcelona`**, tres días.
2. En el asistente: **estilo Cultural**, ritmo indiferente, presupuesto Moderado. Lo demás
   da igual, pero **no lo dejes en Relax**: baja el peso de lo cultural.
3. Cuando esté el plan, busca **un tour a pie que pase por Gràcia**. Si el plan lo trae,
   perfecto. Si no, **pídeselo al asistente**: *«añade un tour a pie por el barrio de
   Gràcia»*, o *«quiero un paseo por Gràcia con las plazas del barrio»*.
4. Abre el tour, ve a la parada de la **Plaça del Diamant** y **despliega LA HISTORIA**.

**Y aquí está la parte honrada**: si la app **no** menciona el refugio, el cierre no puede
decir «con NOMAD no te lo hubieses perdido» — sería exactamente la promesa que la app no
cumple, que es lo que la regla prohíbe. En ese caso hay dos caminos, los dos buenos:

- **Se cambia el cierre** a lo que la app sí diga de esa parada.
- **O se cambia de sitio**: se mira qué parada del tour es la menos obvia y se monta el
  carrusel sobre esa. Entonces el sitio lo ha elegido el producto, que es aún mejor
  argumento.

## Las capturas que hay que mandar

1. **El tour a pie con la lista de paradas** (donde se vea «X paradas · Y min»).
2. **La parada de la Plaça del Diamant con LA HISTORIA desplegada.** Es la importante.
3. El «Dato curioso» de esa parada, si lo tiene.
4. El día del plan donde aparece el tour, para la tarjeta de contexto.

En vertical, sin recortar y **con la barra de estado**, como siempre.

## Las siete tarjetas (copia ya escrita)

| # | Kicker | Titular | Debajo |
|---|---|---|---|
| 1 | Barcelona · Gràcia | **Aquí hay algo que casi nadie sabe.** | Una plaza de barrio con tres historias debajo |
| 2 | Plaça del Diamant · bajo tus pies | **12 m · Hay un refugio antiaéreo.** | Lo cavaron los propios vecinos durante la Guerra Civil. Cabían más de doscientas personas. Es el refugio 232 |
| 3 | Y nadie lo sabía | **1992 · Apareció haciendo obras.** | Barcelona llegó a tener unos 1.300 refugios, más de 90 sólo en Gràcia. Se visita los domingos, con reserva |
| 4 | Arriba, en la plaza | **Empieza la novela más leída en catalán.** | *La plaça del Diamant*, de Mercè Rodoreda (1962), en más de treinta idiomas. La escultura es la Colometa: la protagonista, atrapada contra un muro mientras las palomas levantan el vuelo |
| 5 | Y el nombre | **Se lo puso un joyero.** | En 1860 Josep Rosell compró estos terrenos y bautizó las calles de Gràcia con nombres de piedras preciosas |
| 6 | Cómo se entera uno de esto | **Te lo cuenta al oído, mientras lo andas.** | *(la captura del tour, en el móvil)* |
| 7 | Lista de espera abierta | **Llega en octubre.** | Tu primer viaje por 1,99 €* · *Si te apuntas a la lista de espera en travelsnomad.com |

**El golpe va en la 2, a propósito.** En un carrusel la gente se va pronto: si el refugio
estuviera en la quinta, no lo vería casi nadie. El gancho pregunta y la segunda responde;
de la tres a la cinco es la profundidad para quien se quedó.

## El pie

La primera línea es la que se ve en el feed sin abrir, así que lleva el golpe.

> Debajo de la Plaça del Diamant, en Gràcia, hay un refugio antiaéreo a doce metros.
>
> Lo cavaron los propios vecinos durante la Guerra Civil, cabían más de doscientas personas
> y nadie se acordaba de él hasta que apareció haciendo obras, en 1992. Es el refugio 232
> y se visita los domingos, con reserva.
>
> Arriba, la plaza da nombre a la novela más leída en catalán, y el nombre se lo puso un
> joyero en 1860.
>
> Esto es lo que NOMAD te cuenta en la parada del tour, al oído y mientras andas. Sale en
> octubre, y el primer viaje sale por 1,99 € para quien esté en la lista de espera. El
> enlace, en la bio.
>
> #barcelona #gracia #placadeldiamant #refugio232 #viajar #viajes #historia #catalunya

## Ya está montado: sólo falta la captura

`gen-diamant.py` escribe las siete tarjetas **con sus fotos**, y lo único que pinta como
hueco naranja es la prueba: una tarjeta a la que le falta la captura **no puede parecer
terminada**, y por eso el aviso es chillón.

| Fichero | Dónde va | Qué tiene que ser |
|---|---|---|
| `tourdiamant-900.webp` | `banco/capturas/` | El tour de la app con la parada de la plaza y LA HISTORIA desplegada. **Tarjeta 6, la que no se puede saltar** |

```bash
bash piezas/preparar.sh
cd salida && python3 ../piezas/barcelona/gen-diamant.py
node ../piezas/roma/exportar-plan.mjs diamant 7
```

El molde es el mismo que el carrusel de Roma y vive en `piezas/tarjetas.py`, compartido
por los dos: 1080×1350, velos de la casa, kicker a y=110, titular a y=180, marca a y=1200.

### Dónde están las fotos, una por una

**Histórico (6-sep): ninguna de éstas entró.** Son CC BY-SA y la regla las deja fuera; se
quedan apuntadas por si algún día se decide a conciencia lo contrario. Las que sí entraron
están en la tabla de arriba.

Todas en **Wikimedia Commons, categoría [Plaça del Diamant](https://commons.wikimedia.org/wiki/Category:Pla%C3%A7a_del_Diamant)**
(34 ficheros, de los que 20 son de un acto político y no sirven). **Las catorce
aprovechables son CC BY-SA**, ninguna CC0: por eso siguen sin entrar al banco.

| Para | Fichero en Commons | Licencia | Visto |
|---|---|---|---|
| `f-diamant-plaza.jpg` | [Vista de la Plaça del Diamant.JPG](https://commons.wikimedia.org/wiki/File:Vista_de_la_Pla%C3%A7a_del_Diamant.JPG) | CC BY-SA 3.0 | **Sí**: la plaza entera de día, con los edificios y la terraza al fondo |
| `f-diamant-plano.jpg` | [M101 R0232 G.jpg](https://commons.wikimedia.org/wiki/File:M101_R0232_G.jpg) | CC BY-SA 3.0 | **Sí**: el proyecto original del refugio, planta y sección |
| `f-diamant-colometa.jpg` | [Plaça del Diamant P1140971.JPG](https://commons.wikimedia.org/wiki/File:Pla%C3%A7a_del_Diamant_P1140971.JPG) · [P1140972](https://commons.wikimedia.org/wiki/File:Pla%C3%A7a_del_Diamant_P1140972.JPG) | CC BY-SA 3.0 | **No** |
| ídem, alternativas | [Plaza del Diamante.JPG](https://commons.wikimedia.org/wiki/File:Plaza_del_Diamante.JPG) · [La plaça del Diamant - panoramio](https://commons.wikimedia.org/wiki/File:La_pla%C3%A7a_del_Diamant%2C_Gr%C3%A0cia_%28Barcelona%29_-_panoramio.jpg) | CC BY-SA 4.0 / 3.0 | **No** |
| `f-diamant-calle.jpg` | [Barcelona Gràcia 141](https://commons.wikimedia.org/wiki/File:Barcelona_Gr%C3%A0cia_141_%288338729440%29.jpg) · [Bandera de Gràcia a la plaça del Diamant](https://commons.wikimedia.org/wiki/File:Bandera_de_Gr%C3%A0cia_a_la_pla%C3%A7a_del_Diamant.jpg) | CC BY-SA 2.0 / 4.0 | **No** |

**Las marcadas «No» hay que mirarlas antes de darlas por buenas** — la regla de mirar foto
a foto no es opcional, y este mes ya coló un grabado del XVIII y la fachada equivocada.
Desde una sesión no se pueden bajar en tanda: Wikimedia devuelve 429 al tercer fichero.
Desde un navegador se abren y se descargan en un clic, sin límite.

**El plano del refugio ya lo tenemos localizado**: `File:M101 R0232 G.jpg` en Commons es
el proyecto original —«Refugi… construït a la Plaça del Diamant»— con su planta y su
sección, marcado R232. Vale más que una foto para la tarjeta 3, y por eso va presentado
**como documento enmarcado**, no a sangre: un plano de fondo se lee como textura y no se
entiende qué es. Es CC BY-SA 3.0, o sea que entra en la misma decisión de licencia que
las demás.
