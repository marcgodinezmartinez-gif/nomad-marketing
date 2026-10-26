# Cómo publicar la búsqueda de testers de Android

(Copia versionada de la entrega del 26-oct. En el repo, los vídeos y los PNG salen de `render.sh` en
`salida/`; los textos están en `textos/`, y `revision/` es de la entrega.)

Lo que hay en esta carpeta:

| fichero | para qué |
|---|---|
| `nomad-testers-android-es.mp4` | la historia en castellano: 10 s, 1080×1920, con la pantalla real del itinerario |
| `nomad-testers-android-it.mp4` | la italiana: el mismo texto en italiano, **sin pantalla** (abajo, por qué) |
| `nomad-testers-android-es.png`, `-it.png` | el último fotograma, por si prefieres una tarjeta fija |
| `grupo-bienvenida.txt` | los pasos (castellano, italiano e inglés): van en el **Mensaje de bienvenida** del grupo |
| `grupo-descripcion.txt` | una línea para la **Descripción** del grupo |
| `mensajes-whatsapp.txt` | los mensajes en castellano y en italiano, el de reenviar y el recordatorio del día 7 |
| `revision/` | los fotogramas clave y las zonas seguras, para revisarlo antes |

Pasa los vídeos al teléfono por AirDrop o por Fotos de iCloud. **No los mandes por WhatsApp**: los
comprime y el texto se emborrona.

**Los vídeos no llevan música**, y es a propósito. Tienen una pista de audio en silencio, así que se
suben sin problemas. No hace falta etiqueta de IA porque no hay nada generado: la foto es real, la
pantalla de la castellana es una captura de la app y no hay voz ni música. Si quieres música, elígela
en Instagram y déjala baja.

**La italiana va sin pantalla porque no hay una captura real de la app en italiano.** La que había en
el banco (`plan-900-it.webp`) es la castellana con los textos cambiados a mano y en otra fuente, y al
lado del titular se notaba. Si quieres la pantalla también en la italiana: pon la app en italiano,
abre un viaje a Roma por el día del Coliseo, haz la captura y pásamela; en dos minutos está.

---

## 0. Antes de publicar (10 minutos, una sola vez)

**Si algo de este paso falla, no se publica**: la historia mandaría a la gente a una página que no
pueden ver o a pagar de verdad.

### 0.1 Play Console (1 minuto)

1. **Configuración → Pruebas de licencias**: tiene que estar `nomad-testers@googlegroups.com`. Si no está,
   los testers **pagan de verdad**, y la historia dice que es gratis.
2. **Pruebas → Prueba cerrada → Testers**: tiene que estar el mismo grupo.
3. **Qué versión sirve hoy la prueba cerrada.** Si es la 1.0.1 (2), la primera compra de una instalación
   nueva falla hasta cerrar y volver a abrir la app (#326), y por eso el texto del grupo y los WhatsApp
   piden hacerlo antes del primer viaje. Si ya sirve la 1.0.2 aprobada, ese paso sobra: quítalo de
   `grupo-bienvenida.txt` y de los mensajes 1 y 2 (o dímelo y lo quito yo).

### 0.2 El grupo: lo que ve quien llega

Entra en https://groups.google.com/g/nomad-testers con la cuenta que lo administra → **Configuración
del grupo** (el engranaje). Los nombres son los de la pantalla en español:

1. **Quién puede ver el grupo**: *Cualquier usuario en la Web*. **Hoy no es así**: sin sesión de Google,
   el enlace del grupo da la página de error de acceso (comprobado el 26-oct: responde 302 a
   `access-error`, igual que un grupo que no existe). Quien toque el adhesivo desde Instagram abre el
   navegador de Instagram, que no tiene tu sesión de Google, así que no vería ni los pasos.
2. **Quién puede unirse al grupo**: *Cualquier usuario en la Web puede unirse al grupo*. No «pedir
   unirse»: con eso, a quien no hayas aprobado el paso 2 le dice que no tiene acceso.
3. **Quién puede ver las conversaciones**: *Cualquier usuario en la Web*. No hay conversaciones ni las
   habrá (punto 5), así que no enseña nada; es para que la página de entrada se cargue sin sesión.
4. **Quién puede ver los miembros**: *Propietarios y administradores de grupos*. Son correos de personas.
5. **Quién puede publicar**: *Propietarios del grupo*. Así nadie usa el grupo para escribir a todos.
6. **Mensaje de bienvenida**: pega `grupo-bienvenida.txt` entero. Es lo que sale arriba de la página a la
   que lleva el enlace, encima de la lista de conversaciones; la descripción, en cambio, sólo sale en la
   pestaña *Información*, que en el móvil está escondida. Después de pegarlo, **mira que los tres
   enlaces salgan en azul**: si alguno sale como texto, selecciónalo y ponle el enlace con el botón de
   enlace del editor. Si el campo no deja pegarlo entero (no he encontrado su límite), quita el bloque
   «— ENGLISH —» y vuelve a probar.
7. **Descripción del grupo**: pega `grupo-descripcion.txt` (una línea).
8. Guarda.

### 0.3 Comprobarlo como lo verá un tester

1. Desde cualquier ordenador, sin sesión:
   `curl -s -o /dev/null -w '%{http_code}\n' https://groups.google.com/g/nomad-testers` tiene que dar
   **200**, no 302. (O pídemelo y lo miro yo.)
2. **El camino de verdad**: con un Android que no tenga tu cuenta, abre Instagram, manda el enlace del
   grupo por mensaje directo a esa cuenta (o mira una historia de prueba en «Mejores amigos») y tócalo.
   Tiene que salir la página del grupo con el mensaje de bienvenida y el botón para unirse, y los dos
   enlaces de Play tienen que poder tocarse.
3. Si en el navegador de Instagram no deja iniciar sesión en Google, es lo esperado: por eso el mensaje
   dice en su segunda línea que se abra en Chrome (menú ⋮).

---

## 1. Instagram: las dos historias (@app.nomad)

Instagram no separa las historias por idioma: todos los seguidores verían las dos seguidas, y la segunda
parecería repetida. Por eso van **en días distintos**:

- **Hoy, lunes 26 de octubre, entre las 20:00 y las 21:00**: la castellana.
- **Mañana, martes 27, entre las 13:00 y las 14:00**: la italiana. Quien vio la castellana anoche sólo
  verá ésta, y además es distinta a primera vista: sin pantalla, con el Coliseo entero.

Las dos se suben desde el carrete; no compartas un reel.

**La castellana:**

1. **+** → **Historia** → elige `nomad-testers-android-es.mp4`.
2. **Adhesivos** → **Enlace** → pega `https://groups.google.com/g/nomad-testers`.
3. **Personalizar el texto del adhesivo**: `Únete a la prueba`. **Exactamente ése**: la historia dice
   «Toca «Únete a la prueba»». Si cambias uno, cambia el otro (`preparar.py`, tabla TEXTOS).
4. **Dónde colocarlo**: centrado, justo debajo de los dos chevrones que botan, a un 83 % de la altura
   más o menos (entre los chevrones y la barra de «Enviar mensaje»). Ahí no tapa nada. Tamaño normal y en
   blanco. `revision/zonas-seguras-es.jpg` enseña dónde va.
5. **Tu historia**.

**La italiana**, igual: `nomad-testers-android-it.mp4`, el mismo enlace, y en el adhesivo
`Partecipa al test` (la historia dice «Tocca «Partecipa al test»»).

**En tu cuenta personal**, cada una el mismo día que en @app.nomad, también desde el carrete, con una
mención a @app.nomad. Tus amigos con Android están más ahí que en la cuenta de la app.

**Destacada**: guárdalas en una destacada nueva, «Android», para quien llegue al perfil más tarde. Quítala
cuando acabe la prueba.

**Y aparte de la historia, el mensaje directo**: en Instagram, a los seguidores que conozcas y sepas que
tienen Android, mándales por privado el mensaje de WhatsApp (el castellano o el italiano). Así es como se
apunta la gente de verdad: la historia hace que te conozcan, y el mensaje hace que se apunten.

## 2. WhatsApp

- **Uno por uno, no en un grupo grande.** Un mensaje personal se contesta y uno de grupo se ignora. El
  mensaje 1 en castellano y el 2 en italiano. Empieza por quien sepas que tiene Android.
- **A los que ya estén dentro**, mándales el mensaje 3 y pídeles que lo reenvíen a uno o dos amigos con
  Android. Tiene el italiano debajo.

## Cuándo

La castellana **hoy, lunes 26, de 20:00 a 21:00**, y justo después los WhatsApp en castellano. La
italiana **mañana, martes 27, de 13:00 a 14:00** (Italia está en la misma hora), y justo después los
WhatsApp en italiano. La prueba no empieza a contar hasta que haya 12 apuntados, así que cada día que
pase sin publicar es un día más de espera. Si en **Panel profesional → Estadísticas → Seguidores →
Momentos de más actividad** sale otra hora, usa esa. **El miércoles 28**, si no hay 15 dentro, repite
la que haya traído menos gente.

## Lo que no se dice, para no tener problemas con Google

- Nada a cambio de una valoración o de una reseña. Los testers ni siquiera pueden dejar una reseña.
- Nada prometido para después de la prueba: ni descuentos ni viajes gratis. El gancho es probarla antes
  de que salga en Android y generar los viajes gratis **durante** la prueba, que es cierto sólo si el
  grupo está en Pruebas de licencias (paso 0.1).
- Ninguna fecha de salida en Android. Si alguien pregunta: «Pronto, sin fecha. Primero esta prueba.»

---

## 3. Cuando la gente se apunte

**Cada noche, durante los primeros tres días**:

1. **El grupo**: en https://groups.google.com/g/nomad-testers → **Miembros**, cuenta cuántos hay. Hacen
   falta **12 como mínimo durante 14 días seguidos**; apunta a 15-20, porque siempre se cae alguno.
2. **El paso 2 no sale en el grupo.** Estar en el grupo no es haber pulsado «Convertirse en tester».
   A quien conozcas, pregúntale si ya la tiene instalada desde Google Play. Si en la ficha de Nomad
   de la Play Store le sale el aviso de que es tester, ya está dentro.
3. **Quien diga que le cobran**: que cancele y que te diga con qué cuenta entró. Casi siempre es que
   instaló con una cuenta de Google y se unió al grupo con otra.
4. **Quien diga que «no tiene acceso» en el paso 2, o que la Play Store no encuentra la app en el 3**: que
   espere unos minutos y vuelva a abrirlo. Si sigue igual, es el mismo problema: dos cuentas de Google
   distintas.
5. **Quien diga que no le deja pagar el primer viaje**: que cierre la app del todo y la vuelva a abrir
   (#326, paso 0.1).

**El día 7** (una semana después de que el grupo pase de 12; si llegáis el 28-oct, el **miércoles 4 de
noviembre**): manda el recordatorio del mensaje 4 a cada uno, con la fecha del día 14 escrita. Sirve para
dos cosas: que no la desinstalen y que te cuenten lo que han visto. Lo que te digan entra en el
cuestionario de Google («qué dijeron los testers y qué cambiaste»).

**Cada fallo que te cuenten**, apúntalo en una issue del repo de la app el mismo día, con quién lo vio y
en qué móvil. Esa lista es la que luego se pega en el cuestionario de acceso a producción.

**El día 14** (si llegáis el 28-oct, el **miércoles 11 de noviembre**): Play Console → **Panel** →
**Solicitar acceso a producción**. No antes. Y hasta que Google conteste, que nadie se salga.
