# Metraje de la app

Grabaciones de la app de verdad, una por función, con sus capturas. Salen del simulador de iPhone
en un Mac de GitHub (`capturas/` del repo de la app, NOMAD#431). Sirven de recursos para montar
los vídeos de redes, como la serie «Lo que incluye tu viaje» (#18).

**Los vídeos no están en este repo, y es a propósito.** Este repo es público, y el código de
invitación del viaje demo sale en casi todas las tomas: en «Mis viajes», donde empiezan y acaban,
en Inicio, en la hoja del QR y en Miembros. Con ese código cualquiera podría pedir unirse al viaje
demo. Por eso viven en una página privada del dueño:

**https://claude.ai/artifact/Fa16vHpJfhQcMcWnE9nL8M**

Una sesión los baja con la herramienta Artifact (`action: "read"`, la URL de arriba y
`path: "videos/recorrido-<bloque>.mp4"` o `"capturas/<nombre>.webp"`). La página tiene un índice
de momentos por bloque, con sus tiempos.

## 29-oct-2026, 9.ª pasada

Viaje demo a Lisboa (21-28 nov), iPhone 16 Pro, iOS en español, a las 9:41. Vídeos verticales
de 1206 × 2622, a 60 fps fijos y sin sonido, y 41 capturas en WebP.

| bloque | duración | qué enseña |
|---|---|---|
| `paseo` | 1:36 | «Paseo por la Baixa y el Chiado»: la presentación y la parada 1 en el mapa, con su historia |
| `museo` | 1:38 | Museo Nacional de Arte Antiguo: la presentación, la obra 1 con su foto, en grande y su historia |
| `bienvenida` | 1:16 | la guía de bienvenida, las voces y los avisos |
| `inicio` | 1:15 | la portada del viaje, el tiempo, la cartelera, el QR, Miembros y «Qué hay esos días» |
| `gastos` | 0:51 | el balance, un pago pendiente y un gasto nuevo a medias |
| `lugares` | 1:01 | la lista, el filtro de comida, la ficha de un lugar y el mapa |
| `asistente` | 0:51 | NOMAD AI contesta qué día va más cargado |
| `crear` | 0:56 | los cuatro pasos de crear un viaje y la hoja del precio |

**Antes de usar una toma:**

- **Tapa el código de invitación y el QR**, en todas las tomas donde salgan.
- Los correos ya vienen tapados: los de los miembros en Inicio (40-50 s) y el de la cuenta demo,
  que asoma medio segundo en la bienvenida (61,5-62,4 s) al cerrarse la guía. Ese trozo se corta.
  Están comprobados fotograma a fotograma.
- En la bienvenida y en crear, el precio sale en dólares («$2.99»), porque el simulador no tiene
  App Store. En la tienda española es 2,99 €. No se usa tal cual.
- En el paseo no suena ni avanza la audioguía, y el museo no llega a la segunda obra. Los toques
  ya están corregidos para la próxima pasada.
