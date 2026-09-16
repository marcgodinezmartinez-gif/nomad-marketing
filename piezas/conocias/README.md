# «¿Conocías este lugar?», la serie

Un sitio muy fotografiado, una historia que casi nadie sabe, y la app contándola en la
parada del tour. Seis tarjetas de 1080×1350 con el molde de `piezas/tarjetas.py`: portada
con la pregunta, el golpe con un número grande, dos de profundidad, el móvil con la captura,
y el cierre del reel. Nació el 7-sep del carrusel de la Plaça del Diamant
(`piezas/barcelona`), que se quedó sin fotos del sitio.

## Los tres filtros, en este orden

1. **Una historia que sorprenda y se pueda comprobar.** Cada cifra, contra dos fuentes; lo
   que sólo tiene una, no va a la tarjeta. Las fuentes, en el `.md` de cada pieza.
2. **Un sitio muy fotografiado.** Unsplash y Pexels sólo tienen lo famoso: de una plaza de
   barrio no hay ni una foto libre (la pasada exhaustiva, en `piezas/barcelona/GUION.md`).
   La portada tiene que SER el sitio para poder preguntar «¿conocías este lugar?».
3. **Parada de un tour de la app.** La tarjeta del móvil es la prueba; sin ella el cierre
   es una promesa que la app no cumple.

Sin crédito en ninguna tarjeta ni en el pie: todas las fotos son Unsplash o Pexels, y el
crédito de cada una vive en `banco/fotos/creditos.json`.

## Cómo se fabrica una

```bash
bash piezas/preparar.sh
cd salida && python3 ../piezas/conocias/gen-conocias.py carmel
node ../piezas/roma/exportar-plan.mjs carmel 6
```

Las piezas viven en `PIEZAS` dentro de `gen-conocias.py`: fotos, textos y el nombre de la
captura que espera en `banco/capturas/`. Mientras no esté, la tarjeta 5 pinta el hueco en
naranja.

## Las que hay

| Pieza | Sitio | El golpe | Estado |
|---|---|---|---|
| `carmel` | Búnkers del Carmel, Barcelona | Una batería antiaérea de 1938, luego un barrio de barracas | **Publicada** (7-sep) |
| `debod` | Templo de Debod, Madrid | Egipto lo regaló en 1968 por ayudar a salvar Abu Simbel | **Publicada** (13-sep) |
| `panteon` | Panteón de Agripa, Roma | Llueve dentro y está calculado; y la cúpula sigue sin superarse | **Lista para publicar** (16-sep) |

## Candidatas comprobadas el 16-sep: historia Y fotos, a la vez

Se comprueban las dos cosas antes de proponer nada, que es lo que costó el carrusel de la
Plaça del Diamant: allí la historia era buena y las fotos no existían.

| Sitio | El golpe, verificado | Fotos libres |
|---|---|---|
| **Panteón de Roma** ✅ montada | La cúpula de hormigón en masa más grande de la historia, 43,44 m, **1.900 años después**. El óculo de 9 m está abierto: llueve dentro, y el suelo es convexo con drenaje perimetral, o sea que estaba calculado. La fachada dice «Agripa lo hizo», pero los ladrillos son del 123-125: lo reconstruyó Adriano y mantuvo el nombre del otro. Se salvó porque en 608 lo donaron al papa: el único edificio de la Roma antigua intacto y en uso ininterrumpido | **Diez verticales libres del interior** en Unsplash, con la cúpula y el óculo. Lo mejor que se ha encontrado para esta serie |
| **Piazza Navona, Roma** | Debajo está el estadio de Domiciano, del año 85: 276 × 106 m y **30.000 espectadores**. La plaza conserva su forma exacta, por eso es alargada. Y de 1652 a 1866 se inundaba cada sábado y domingo de agosto, para jugar con barcas | Ocho claras en Pexels y unas cuantas en Unsplash, **casi todas apaisadas**: hay que recortar de originales grandes |
| **Park Güell, Barcelona** | No iba a ser un parque: era una urbanización de sesenta viviendas. **Se vendieron dos parcelas**, y una se la quedó Gaudí, que vivió allí de 1906 a 1925. El proyecto se abandonó y abrió como parque público en 1926 | El banco del mosaico y los detalles, **casi todo apaisado**; dos verticales de detalle en Pexels. Recortando, sale |

Fuentes: Wikipedia (Panteón de Agripa, Piazza Navona, Park Güell), comprobadas una a una el
16-sep. Cada cifra va a la tarjeta sólo si aparece en la fuente, como en Carmel y Debod.

### Descartadas, y por qué

| Sitio | Motivo |
|---|---|
| Sagrada Família | El dato bueno —la torre se queda un metro por debajo de Montjuïc a propósito— **no está en la fuente**; la altura (172,5 m) sí. Sin segunda fuente, no va a una tarjeta |
| Plaça Reial | Unsplash no devuelve ni una foto de la plaza; las farolas de Gaudí no salen en ninguna |
| Pont del Bisbe | Sólo Unsplash+ (de pago) |
| Plaça de Sant Felip Neri | Ninguna foto clara de la plaza |

## Candidatas antiguas, con lo que se sabía de sus fotos (7-sep)

| Sitio | El golpe | Fotos libres |
|---|---|---|
| Pont del Bisbe, Barcelona | El puente «medieval» es de 1928, con una calavera y un puñal | Sólo Unsplash+ (de pago): **no** por ahora |
| Plaça de Sant Felip Neri, Barcelona | Las marcas de la fachada son de una bomba de 1938, 42 muertos | Ninguna clara en Unsplash: por comprobar en Pexels |
| Park Güell | Urbanización fracasada: de 60 parcelas se vendieron 2 | De sobra (una ya en el banco) |
| Sagrada Família | La torre más alta, un metro por debajo de Montjuïc a propósito | De sobra |
| La Barceloneta | Barrio de 1753 para los desalojados por la Ciutadella | De sobra |
| Gran Vía, Madrid | Más de 300 casas derribadas; Telefónica, primer rascacielos de Europa | De sobra (una en el banco) |
| Plaza Mayor, Madrid | Se quemó tres veces | De sobra |
| Malasaña, Madrid | El nombre de una costurera de 15 años, 2 de mayo de 1808 | Por comprobar |
| Piazza Navona, Roma | Debajo, el estadio de Domiciano, 30.000 espectadores | El dueño las hace esta semana |
| Panteón, Roma | Llueve dentro, y está calculado | El dueño las hace esta semana |
| Largo di Torre Argentina, Roma | Donde mataron a César; hoy, refugio de gatos | El dueño las hace esta semana |
| Campo de' Fiori, Roma | La estatua de un hereje quemado en medio del mercado | El dueño las hace esta semana |
