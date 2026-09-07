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

| Pieza | Sitio | El golpe | Falta |
|---|---|---|---|
| `carmel` | Búnkers del Carmel, Barcelona | Una batería antiaérea de 1938, luego un barrio de barracas | `tourcarmel-900.webp` |
| `debod` | Templo de Debod, Madrid | Egipto lo regaló en 1968 por ayudar a salvar Abu Simbel | `tourdebod-900.webp` |

## Candidatas, con lo que se sabe de sus fotos (7-sep)

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
