# Cómo publicar la búsqueda de testers de Android

(Copia versionada de la entrega del 26-oct. En el repo, los vídeos y los PNG salen de `render.sh` en
`salida/`; los textos están en `textos/`, y `revision/` es de la entrega.)

Lo que hay en esta carpeta:

| fichero | para qué |
|---|---|
| `nomad-testers-android-es.mp4` | la historia en castellano: 10 s, 1080×1920 |
| `nomad-testers-android-it.mp4` | la misma, en italiano |
| `nomad-testers-android-es.png`, `-it.png` | el último fotograma, por si prefieres una tarjeta fija |
| `grupo-descripcion.txt` | lo que se pega en la descripción del grupo de Google (castellano, italiano e inglés) |
| `grupo-descripcion-corta.txt` | por si la descripción no admite la larga (paso 0) |
| `mensajes-whatsapp.txt` | los mensajes en castellano y en italiano, el de reenviar y el recordatorio del día 7 |
| `revision/` | los fotogramas clave y las zonas seguras, para revisarlo antes |

Pasa los vídeos al teléfono por AirDrop o por Fotos de iCloud. **No los mandes por WhatsApp**: los
comprime y el texto se emborrona.

**Los vídeos no llevan música**, y es a propósito. Tienen una pista de audio en silencio, así que se
suben sin problemas. No hace falta etiqueta de IA porque no hay nada generado: la foto es real, la
pantalla es la de la app y no hay voz ni música. Si quieres música, elígela en Instagram y déjala baja.

---

## 0. Antes de publicar: el grupo (5 minutos, una sola vez)

Entra en https://groups.google.com/g/nomad-testers con la cuenta que lo administra → **Configuración
del grupo** (el engranaje).

1. **Descripción del grupo**: borra lo que haya y pega `grupo-descripcion.txt` entero. Tiene unos
   3.400 caracteres. La documentación de Google pone el límite en 4.096
   ([API de ajustes de grupos](https://developers.google.com/workspace/admin/groups-settings/v1/reference/groups),
   [API de Directory](https://developers.google.com/workspace/admin/directory/reference/rest/v1/groups)),
   pero hay quien ha visto que en la práctica se cortaba a 300
   ([Universidad de Cambridge](https://gitlab.developers.cam.ac.uk/uis/devops/gsuite/synctool/-/issues/12)).
   **Después de guardar, abre la página del grupo y comprueba que se ve hasta el final**, hasta
   `https://travelsnomad.com`. Si se corta, pega en la descripción `grupo-descripcion-corta.txt`
   (259 caracteres) y publica el texto largo como **primera conversación** del grupo: **Nueva
   conversación**, con el asunto «Cómo funciona la prueba · Come funziona il test · How the test works».
   Hazlo antes de que entre nadie, porque la conversación les llega por correo a los miembros.
2. **Quién puede unirse al grupo**: *Cualquier usuario de la web puede pedir unirse*, o mejor, *cualquiera
   puede unirse*. Si cada alta tiene que aprobarla alguien, la gente se queda a medias.
3. **Quién puede ver a los miembros**: *Gestores del grupo*. Son correos de personas: no tienen que
   verlos los demás testers.
4. **Quién puede publicar**: *Propietarios del grupo*. Así nadie usa el grupo para mandar correos a todos.
5. Guarda. Abre el enlace del grupo en un Android **sin haber iniciado sesión como administrador** (o
   pídeselo a alguien) y comprueba que sale el botón para unirse y que el texto se lee entero.

---

## 1. Instagram: las dos historias (@app.nomad)

La mitad de los seguidores son italianos y la app está en italiano, así que se suben **las dos, una
detrás de otra**: primero la castellana y después la italiana. Las dos se suben desde el carrete; no
compartas un reel.

**La castellana:**

1. **+** → **Historia** → elige `nomad-testers-android-es.mp4`.
2. **Adhesivos** → **Enlace** → pega `https://groups.google.com/g/nomad-testers`.
3. **Personalizar el texto del adhesivo**: `Únete a la prueba`.
4. **Dónde colocarlo**: debajo de la cápsula «Toca el enlace», que tiene la flecha hacia abajo y está a
   un 75 % de la altura. Ponlo centrado y justo debajo, más o menos a un 83 % de la altura (entre la
   flecha y la barra de «Enviar mensaje»). Ahí no tapa nada. Déjalo de tamaño normal y en blanco.
   (`revision/zonas-seguras-es.jpg` enseña dónde va).
5. **Tu historia**.

**La italiana**, igual: `nomad-testers-android-it.mp4`, el mismo enlace, y en el adhesivo
`Partecipa al test`.

**En tu cuenta personal**, las mismas dos, también desde el carrete, con una mención a @app.nomad. Tus
amigos con Android están más ahí que en la cuenta de la app.

**Destacada**: cuando estén publicadas, guárdalas en una destacada nueva, «Android», para quien llegue al
perfil más tarde. Quítala cuando acabe la prueba.

**Y aparte de la historia, el mensaje directo**: en Instagram, a los seguidores que conozcas y sepas que
tienen Android, mándales por privado el mensaje de WhatsApp (el castellano o el italiano). Así es como se
apunta la gente de verdad: la historia hace que te conozcan, y el mensaje hace que se apunten.

## 2. WhatsApp

- **Uno por uno, no en un grupo grande.** Un mensaje personal se contesta y uno de grupo se ignora. El
  mensaje 1 en castellano y el 2 en italiano. Empieza por quien sepas que tiene Android.
- **A los que ya estén dentro**, mándales el mensaje 3 y pídeles que lo reenvíen a uno o dos amigos con
  Android. Tiene el italiano debajo.

## Cuándo

**Hoy, lunes 26 de octubre, entre las 20:00 y las 21:00** (Italia está en la misma hora): las dos
historias seguidas, y justo después los WhatsApp. La prueba no empieza a contar hasta que haya 12
apuntados, así que cada día que pase sin publicar es un día más de espera. Si en **Panel profesional →
Estadísticas → Seguidores → Momentos de más actividad** sale otra hora, usa esa. **El miércoles 28**,
repite las historias si no hay 15 dentro.

## Lo que no se dice, para no tener problemas con Google

- Nada a cambio de una valoración o de una reseña. Los testers ni siquiera pueden dejar una reseña.
- Nada prometido para después de la prueba: ni descuentos ni viajes gratis. El gancho es probarla antes
  que nadie y generar los viajes gratis **durante** la prueba, que es cierto porque son testers con licencia.
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
4. **Quien diga que «no tiene acceso» en el paso 2**: que espere unos minutos después de unirse al grupo y
   vuelva a abrirlo. Si sigue igual, es el mismo problema: dos cuentas de Google distintas.

**El día 7** (una semana después de que el grupo pase de 12; si llegáis el 28-oct, el **miércoles 4 de
noviembre**): manda el recordatorio del mensaje 4 a cada uno, con la fecha del día 14 escrita. Sirve para
dos cosas: que no la desinstalen y que te cuenten lo que han visto. Lo que te digan entra en el
cuestionario de Google («qué dijeron los testers y qué cambiaste»).

**Cada fallo que te cuenten**, apúntalo en una issue del repo de la app el mismo día, con quién lo vio y
en qué móvil. Esa lista es la que luego se pega en el cuestionario de acceso a producción.

**El día 14** (si llegáis el 28-oct, el **miércoles 11 de noviembre**): Play Console → **Panel** →
**Solicitar acceso a producción**. No antes. Y hasta que Google conteste, que nadie se salga.
