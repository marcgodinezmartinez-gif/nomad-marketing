# Brief para reformular la captación (2-sep-2026)

Escrito para llevarlo a otra sesión de IA fuera de este repo. **Es autocontenido**: no hace
falta el repo para entenderlo. Los números son reales y medidos; lo que no está medido,
está marcado como tal.

El dueño ha parado la línea de trabajo actual con estas palabras: *«no me gusta nada de lo
que hemos pensado, hay que reformular la idea de lo que quiero»*. Este documento existe
para que otra IA pueda ayudar **sin dar por buenas las conclusiones anteriores**.

---

## 1. El producto

**NOMAD**, app de viajes. Sale en **octubre de 2026** en iOS y Android. Hoy **no se puede
usar ni repartir** — no hay beta viable en septiembre.

Lo que hace, y nada más:

- Le dices destino y fechas y **te escribe el viaje día a día**: qué ver, en qué orden y
  cuánto cuesta. Si no tienes destino, te propone tres. Si cambias de idea, se lo pides al
  asistente y lo reescribe.
- **Tour a pie guiado por voz**, de parada en parada, también sin cobertura.
- **En el museo**: enfocas una obra y te cuenta su historia.
- **Grupo**: los amigos entran con un QR y los gastos se reparten solos.

Idiomas: español, inglés, italiano, francés.

**Precio**: 2,99 € el viaje entero, sin suscripción. Nunca se compara con «la audioguía de
6 €» — el ancla es lo que cuesta un café, sin ponerle cifra.

## 2. Qué se está intentando conseguir

Antes del lanzamiento, la **única conversión que existe es la lista de espera**: un correo.
La oferta actual es **el primer viaje por 1,99 € en vez de 2,99 €** para quien esté en la
lista el día que se abra.

Un alta vale **0,24 €** (margen esperado). El coste objetivo por alta es **0,25 €**.

## 3. Los números, que son el corazón del problema

**La lista de espera, total histórico: 8 altas.** Todas del 31 de agosto, todas en español.
Origen: 4 de Instagram orgánico, 3 de invitaciones directas, **1 de publicidad pagada**.

**La campaña de Meta** (4 anuncios, misma imagen, un solo conjunto «ES 20-55 amplio»,
objetivo *tráfico*, 5 €/día, tope 50 €, **sin píxel a propósito**):

| | |
|---|---|
| Alcance | 20 000 |
| Clics en el enlace (última semana) | **794** |
| Visitas reales a la página | **457** (58 % de los clics — ratio normal) |
| Altas | **1** |
| Conversión de visita a alta | **0,22 %** |
| CTR | 3,4 % — bueno para tráfico frío |

Una página de lista de espera que funciona convierte del 10 al 30 % de las visitas. Una
mala, un 3 %. Con 457 visitas tocaban entre 45 y 135 altas. Hay una.

**Gasto exacto por anuncio: NO MEDIDO todavía.** Sin él no hay coste por alta real.

## 4. Qué se ha descartado ya, con evidencia

Esto ahorra repetir trabajo. **Cada punto está comprobado, no supuesto.**

- **No es la página.** Comprobada en producción: responde 200 en 0,25 s, pesa 36 KB, las
  doce imágenes cargan, el formulario viene en el HTML servido (no depende de JS) y en un
  iPhone 13 el campo de correo está a 259 px del borde — **visible sin bajar**, con el
  precio debajo. La atribución sobrevive al salto de idioma y un correo repetido no se
  pierde.
- **No es tráfico basura.** Llega el 58 % de los clics, que es el ratio normal. La gente
  llega de verdad.
- **No es el argumento del anuncio.** Se probaron **cuatro ángulos distintos** —precio,
  cobertura geográfica, producto y grupo— con la misma imagen para aislar la variable.
  **Fallaron los cuatro por igual.** Cuando las cuatro ramas de un test caen a la vez, lo
  que se estaba probando no era el cuello de botella.
- **No es congruencia anuncio-página**: el anuncio cuyo título es idéntico al titular de
  la web convirtió **0 de 135 visitas**.

**Lo que queda en pie**: 457 personas reales cargaron una página rápida, con el formulario
a la vista y el precio delante, y 456 se fueron.

## 5. Las restricciones reales

- **No hay beta en septiembre.** No se puede dejar probar el producto.
- **Sin píxel, por decisión.** Consecuencia: Meta **no puede optimizar por altas en la
  web**; el único objetivo disponible es *tráfico*, que optimiza por clics baratos.
- **5 €/día.** Muy por debajo de las ~50 conversiones/semana que Meta necesita para salir
  de la fase de aprendizaje en cualquier objetivo de conversión.
- **Una sola persona** lo hace todo. Cualquier propuesta con trabajo manual por lead tiene
  que ser sostenible para una persona.
- **Instagram `@app.nomad`**, cuenta pequeña. Aproximadamente la mitad de los seguidores
  son italianos y **ninguno se ha apuntado nunca**. No se compran seguidores.
- **La base de datos es la única tabla de resultados.** Nada de fiarse de lo que Meta se
  atribuya.

## 6. Lo que ya está fabricado y sin usar

- 22 tarjetas para dos destacadas de Instagram (español e italiano), sin subir.
- 2 reels montados; uno lleva sin subir desde el 31 de agosto.
- Una historia animada de los tres pasos de la lista.
- **Una grabación de pantalla de 46 s con la app real funcionando**: escribir el destino,
  el resumen, el plan generado, el tour a pie y el museo.

## 7. Lo que se estaba proponiendo, y que el dueño ha parado

Para que no se vuelva a proponer sin más: formularios instantáneos de Meta dentro del
anuncio, cambiar la oferta para entregar algo inmediato (un plan de un día gratis por
correo), y un vídeo de demostración de 32 s montado a partir de la grabación de 46 s.

**El dueño no está convencido de nada de eso.** Trátalo como contexto de lo intentado, no
como el punto de partida.

## 8. La pregunta abierta

**¿Qué le pedimos a un desconocido, y a cambio de qué, cuando el producto no se puede usar
hasta octubre?**

Está permitido cuestionar la premisa entera: que la lista de espera sea la métrica, que el
correo sea lo que hay que pedir, que Instagram y Meta sean los canales, y que 1,99 € sea
un incentivo. Nada de eso es sagrado. Lo único fijo son las restricciones del punto 5.
