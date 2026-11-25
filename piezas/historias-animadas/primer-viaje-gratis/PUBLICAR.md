# Publicar «Tu primer viaje, gratis»

**No se publica hasta que la promoción esté encendida en la app** (NOMAD#479: la migración, `unlock-trip`,
la OTA y el interruptor). Antes, el vídeo anuncia algo que la app no hace.

## Los ficheros (`bash variantes.sh <salida>`)

| fichero | para qué |
|---|---|
| `nomad-primer-viaje-gratis-reel-1080x1920.mp4` | El reel de Instagram y TikTok: acaba en «Enlace en el perfil». Con voz y música |
| `nomad-primer-viaje-gratis-reel-sin-musica-1080x1920.mp4` | El mismo con la voz y los efectos solos, por si se le quiere poner un audio de tendencias dentro de Instagram (bajo, para que no tape la voz) |
| `nomad-primer-viaje-gratis-anuncio-1080x1920.mp4` | Para Meta: sin «Enlace en el perfil», porque el anuncio lleva su botón |
| `nomad-primer-viaje-gratis-portada-1080x1920.png` | La portada: la tarjeta de la oferta |

1080 × 1920, 30 fps, 32 s, H.264 y AAC a -14 LUFS.

## Antes de subirlo

1. **La fecha.** El vídeo dice «hasta el 3 de diciembre» en la firma, en la oferta y en el cierre. Si la
   promoción acaba otro día, se cambia en `index.html` y se vuelve a renderizar.
2. **El tope.** La promoción se corta sola al llegar a 300 viajes gratis (NOMAD#479) y el vídeo no lo
   dice. Antes de publicar, o se sube el tope a un número que no se alcance, o el vídeo y el anuncio
   dicen «para los 300 primeros».
3. **Una instalación nueva.** Instalar la app desde la tienda en un móvil limpio y ver que sale «Gratis»
   en la primera sesión. Con mala red puede salir el precio hasta la segunda apertura.
4. **Verlo con sonido en el móvil.** Las voces y la música son sintéticas y nadie las ha oído aún: una
   sesión las transcribe y las mide, pero no las oye.
5. **La etiqueta de IA.** Al subirlo se marca «Contenido hecho con IA» (Instagram: Configuración
   avanzada; TikTok: «Contenido generado por IA»): la música y las voces lo son.

## El pie

La primera línea es la que se ve sin abrirlo, y lleva lo primero lo mismo que el vídeo: «gratis».

> Tu primer viaje con Nomad, gratis hasta el 3 de diciembre.
>
> ¿Qué es Nomad? Tu imprescindible para viajar. Te organiza el viaje día a día. Te cuenta lo que tienes delante, con audioguía. Te recomienda qué ver y dónde comer. Lleva las cuentas del grupo. Y tiene un asistente para lo que necesites durante el viaje.
>
> 👉 Enlace en el perfil.
>
> Un viaje gratis por cuenta, para quien aún no ha comprado ninguno. Después, desde 2,99 € el viaje, sin suscripción.

## Los enlaces

- Perfil e historias: `travelsnomad.com/app?utm_source=instagram&utm_medium=organic&utm_campaign=bf-gratis`
- Anuncio de Meta: `travelsnomad.com/app?utm_source=meta&utm_medium=paid&utm_campaign=bf-gratis-pago`

Cada móvil cae en su tienda. Los textos del anuncio están en la issue #23.

## Lo que no se hace

- No se escribe nada de la promoción en la ficha de la App Store (decisión del dueño, NOMAD#479).
- No se promociona desde la app de Instagram del iPhone: cobra la comisión de Apple (AGENTS.md).
- El 4 de diciembre se retira o se archiva: un vídeo que dice «gratis» con la promoción apagada es una
  promesa que la app no cumple. Lo mismo si se apaga antes o se llega al tope: se retira ese día.
- No se manda a «Viajes listos» como destino de la campaña mientras NOMAD#469 siga abierta.
