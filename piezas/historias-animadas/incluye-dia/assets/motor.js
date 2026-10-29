// EL MOTOR DE «LO QUE INCLUYE TU VIAJE» (29-oct), compartido por incluye-pago/ (A) e incluye-dia/ (B).
// Se edita aquí, en incluye-pago/assets/, y sincronizar.sh lo copia a incluye-dia/assets/.
//
// Es el de «Un trazo» (lanzamiento-trazo/index.html) con dos cambios:
// - LA LÍNEA DIBUJA EL BORDE DE LA PANTALLA de la app, pegada a ella, y dentro corre la grabación. No
//   es un iPhone dibujado: las normas de marketing de Apple no dejan ilustrar un producto de Apple, y
//   el dueño eligió esto el 29-oct al saberlo (README.md).
// - Las salidas: del borde derecho de la pantalla sale un trazo que dibuja en la columna de la derecha
//   lo que la toma no deja leer, se queda entero y vuelve a meterse en el borde. Cada trazo tiene su
//   COLA y su PUNTA en largo de recorrido, calculadas fotograma a fotograma ANTES de reproducir:
//   HyperFrames salta a cada instante con los eventos apagados, así que nada depende de un onUpdate.
//
// Todo se escribe a 1× (los tiempos de la voz, medidos) y al final se estira entre VELOCIDAD, como en
// «Un trazo». Los <video> llevan su tiempo final escrito en el HTML (cortar-tomas.py lo imprime).
window.Motor = function (tl, VELOCIDAD) {
  var F = 1 / 30, FPS = 30;
  var SVGNS = "http://www.w3.org/2000/svg";
  var a = document.getElementById.bind(document);
  var IN = { autoAlpha: 1, y: 0, duration: 0.4, ease: "power3.out" };
  var ARR = { autoAlpha: 1, y: 0, duration: 0.6, ease: "power3.out" };
  function corta(sel, t) { tl.to(sel, { autoAlpha: 0, duration: 0 }, t); }
  function aparece(sel, t) { tl.fromTo(sel, { autoAlpha: 0 }, { autoAlpha: 1, duration: 0 }, t); }
  function funde(sel, t, d) { tl.fromTo(sel, { autoAlpha: 0 }, { autoAlpha: 1, duration: d || 0.15, ease: "none" }, t); }
  function entra(sel, t, dy, vars) { tl.fromTo(sel, { autoAlpha: 0, y: dy }, vars || IN, t); }
  function apaga(sel, t, dur) { tl.fromTo(sel, { autoAlpha: 1 }, { autoAlpha: 0, duration: dur || 0.2, ease: "power1.out", immediateRender: false }, t); }
  function brota(sel, t, ease) { tl.fromTo(sel, { autoAlpha: 0, scale: 0 }, { autoAlpha: 1, scale: 1, duration: 0.32, ease: ease || "back.out(3)" }, t); }
  function encoge(sel, t) { tl.fromTo(sel, { scale: 1, autoAlpha: 1 }, { scale: 0, autoAlpha: 0, duration: 0.12, ease: "power2.in", immediateRender: false }, t); }
  // Un latido: crece un poco y vuelve. Va en las pausas, para que el dibujo entero no sea un fotograma fijo.
  function late(sel, t, amp, dur) {
    var s = 1 + (amp || 0.04);
    tl.fromTo(sel, { scale: 1 }, { scale: s, duration: 0.12, ease: "power2.out", immediateRender: false }, t);
    tl.fromTo(sel, { scale: s }, { scale: 1, duration: (dur || 0.6) - 0.12, ease: "power1.inOut", immediateRender: false }, t + 0.12);
  }
  // La frase de cada escena, siempre en el mismo sitio, abajo (y=1300): entra en el corte y se va en el siguiente.
  function frase(ids, t0, t1) {
    ids.forEach(function (id, k) { entra("#" + id, t0 + 0.08 * k, 24); });
    corta(ids.map(function (id) { return "#" + id; }), t1);
  }

  // Un trazado que se escribe orden a orden, con marcas medidas sobre el trazado hasta ahí.
  function Camino() { this.c = []; this.m = {}; }
  Camino.prototype.o = function (s) { this.c.push(s); return this; };
  Camino.prototype.marca = function (n) { this.m[n] = this.c.length; return this; };
  Camino.prototype.d = function () { return this.c.join(" "); };
  function mide(cam, el) {
    var tmp = document.createElementNS(SVGNS, "path"), out = {};
    el.parentNode.appendChild(tmp);
    for (var n in cam.m) { tmp.setAttribute("d", cam.c.slice(0, cam.m[n]).join(" ")); out[n] = cam.m[n] > 0 ? tmp.getTotalLength() : 0; }
    el.parentNode.removeChild(tmp);
    return out;
  }
  // Pone el trazado en su <path> y devuelve su largo y sus marcas.
  function pon(cam, el) { el.setAttribute("d", cam.d()); var m = mide(cam, el); m.L = el.getTotalLength(); return m; }

  var CURVAS = {};
  function curva(n) { return CURVAS[n] || (CURVAS[n] = n ? gsap.parseEase(n) : function (q) { return q; }); }
  // keys: [[hora, largo, curva para llegar ahí], …]
  function valor(keys, t) {
    if (t <= keys[0][0]) return keys[0][1];
    for (var i = 1; i < keys.length; i++) {
      if (t <= keys[i][0]) {
        var p = keys[i - 1], q = keys[i], d = q[0] - p[0];
        if (d <= 0) return q[1];
        return p[1] + (q[1] - p[1]) * curva(q[2])((t - p[0]) / d);
      }
    }
    return keys[keys.length - 1][1];
  }
  // El primer instante, desde t0, en que la punta pasa (hacia arriba o hacia abajo) por un largo.
  function cuando(keys, largo, t0, baja) {
    for (var t = t0 || 0; t < 120; t += 1 / 300) {
      var v = valor(keys, t);
      if (baja ? v <= largo : v >= largo) return t;
    }
    return 120;
  }
  // Lo que se ve de un trazado: un solo guion, de la cola a la punta. Vacío, el guion va más allá
  // del final (con el remate redondo, un guion de largo cero pinta un punto).
  function ventana(L, ini, c, p) {
    var lo = Math.max(c - ini, 0), hi = Math.min(p - ini, L);
    if (hi - lo < 0.5) return { "stroke-dasharray": "0.01 " + (L + 60).toFixed(1), "stroke-dashoffset": (-(L + 25)).toFixed(1) };
    return { "stroke-dasharray": (hi - lo).toFixed(2) + " " + (L + 60).toFixed(1), "stroke-dashoffset": (-lo).toFixed(2) };
  }
  // Una cadena de trazados seguidos (cada uno empieza donde acaba el anterior), con una cola y una
  // punta en largo de recorrido sobre todos, uno detrás de otro. tramos: [[el, L], …]. Devuelve el
  // comienzo de cada tramo en la cadena.
  function cadena(tramos, COLA, PUNTA, tA, tB) {
    var S = 0, ini = [];
    tramos.forEach(function (t) { ini.push(S); S += t[1]; });
    tramos.forEach(function (t, i) {
      var el = t[0], L = t[1], prev = null;
      var k0 = Math.floor(tA * FPS), k1 = Math.ceil(tB * FPS);
      for (var k = k0; k <= k1; k++) {
        var v = ventana(L, ini[i], valor(COLA, k / FPS), valor(PUNTA, k / FPS));
        if (k === k0) { el.setAttribute("stroke-dasharray", v["stroke-dasharray"]); el.setAttribute("stroke-dashoffset", v["stroke-dashoffset"]); }
        else if (v["stroke-dasharray"] !== prev["stroke-dasharray"] || v["stroke-dashoffset"] !== prev["stroke-dashoffset"]) {
          tl.fromTo(el, { attr: prev }, { attr: v, duration: F, ease: "none", immediateRender: false }, (k - 1) / FPS);
        }
        prev = v;
      }
    });
    return ini;
  }
  // Una salida: sale del borde, se dibuja (de t0 a t1), se queda entera y vuelve a meterse en el borde
  // (de t2 a t3). Con la cola clavada en el borde, la línea nunca se suelta del papel.
  function salida(el, cam, t0, t1, t2, t3, ease) {
    var m = pon(cam, el);
    var PUNTA = [[t0, 0], [t1, m.L, ease || "power2.inOut"], [t2, m.L], [t3, 0, "power1.in"]];
    cadena([[el, m.L]], [[0, 0]], PUNTA, t0 - F, t3 + F);
    m.PUNTA = PUNTA;
    m.llega = function (n) { return cuando(PUNTA, m[n], t0); };
    m.vuelve = function (n) { return cuando(PUNTA, m[n] - 0.5, t2, true); };
    return m;
  }
  // Un punto que brota cuando la punta llega a su marca y se va cuando la punta, de vuelta, lo pasa.
  function nodo(sel, m, marcaN, x, y, latidos) {
    gsap.set(sel, { svgOrigin: x + " " + y });
    var tb = m.llega(marcaN);
    brota(sel, tb - 0.03);
    (latidos || []).forEach(function (t) { late(sel, t, 0.07, 0.4); });
    encoge(sel, m.vuelve(marcaN));
    return tb;
  }

  // —— LA PANTALLA. Un rectángulo de esquinas redondas alrededor de la grabación, a 7 px de ella (el
  // centro del trazo de 10 px), recorrido en sentido contrario al reloj desde el lado izquierdo: baja,
  // la base, sube por la derecha, el borde de arriba y vuelve a bajar 20 px por la izquierda, para
  // cerrar sin hueco. Delante, la llegada desde donde acaba la espiral del logo.
  var P = { w: 404, h: 806, r: 36, y: 400, gap: 7 };
  function borde(cam, x, desde) {
    var x0 = x - P.gap, y0 = P.y - P.gap, w = P.w + 2 * P.gap, h = P.h + 2 * P.gap, r = P.r + P.gap, YB = 470;
    cam.o("C" + (desde[0] - 120).toFixed(1) + "," + (desde[1] + 12).toFixed(1) + " " + x0 + "," + (YB - 80) + " " + x0 + "," + YB).marca("borde");
    cam.o("L" + x0 + "," + (y0 + h - r)).o("A" + r + "," + r + " 0 0 0 " + (x0 + r) + "," + (y0 + h)).marca("abajo")
       .o("L" + (x0 + w - r) + "," + (y0 + h)).o("A" + r + "," + r + " 0 0 0 " + (x0 + w) + "," + (y0 + h - r))
       .o("L" + (x0 + w) + "," + (y0 + r)).o("A" + r + "," + r + " 0 0 0 " + (x0 + w - r) + "," + y0)
       .o("L" + (x0 + r) + "," + y0).o("A" + r + "," + r + " 0 0 0 " + x0 + "," + (y0 + r))
       .o("L" + x0 + "," + (YB + 20)).marca("fin");
    return { x0: x0, x1: x0 + w, y0: y0, y1: y0 + h };
  }

  // —— 0 · EL LOGO, la espiral de «Un trazo» tal cual: nace dentro del cuenco (un círculo de centro
  // (540,3, 661,3) y radio 143,6, medido sobre el PNG), tangente a su borde, y se despega en media
  // vuelta. Devuelve el trazado, para que la pantalla siga desde su punta.
  function espiral() {
    var BX = 540.3, BY = 661.3, BR = 143.6, esp = new Camino(), NE = 160, PH0 = 72, PH1 = -112, x, y;
    for (var i = 0; i <= NE; i++) {
      var u = i / NE, ph = (PH0 + (PH1 - PH0) * u) * Math.PI / 180, r = BR - 8 + 138 * Math.pow(u, 1.3);
      x = BX + r * Math.cos(ph); y = BY + r * Math.sin(ph);
      esp.o((i ? "L" : "M") + x.toFixed(1) + "," + y.toFixed(1));
      if (r - 5 >= BR + 1.5 && esp.m.fuera === undefined) esp.marca("fuera");
    }
    esp.marca("fin");
    esp.punta = [x, y];
    return esp;
  }
  // La escena del logo, de 0 a T1: el logo respira en la primera nota y, en T1, vuela a la cabecera,
  // donde se queda hasta el cierre con «Ya en la App Store, para iPhone».
  function logo(T1) {
    gsap.set("#logo", { transformOrigin: "50% 50%" });
    tl.fromTo("#logo", { scale: 1 }, { scale: 1.025, duration: 0.14, ease: "power2.out", immediateRender: false }, 0.3125);
    tl.fromTo("#logo", { scale: 1.025 }, { scale: 1, duration: 0.45, ease: "power1.inOut", immediateRender: false }, 0.4525);
    var mc = a("marca"), mimg = mc.querySelector("img");
    var dx = mc.offsetLeft + mimg.offsetLeft + mimg.offsetWidth / 2 - 540;
    var dy = mc.offsetTop + mimg.offsetTop + mimg.offsetHeight / 2 - 640;
    tl.fromTo("#logo", { x: 0, y: 0, scale: 1 }, { x: dx, y: dy, scale: mimg.offsetHeight / 330, duration: 0.3, ease: "power3.inOut", immediateRender: false }, T1);
    corta("#logo", T1 + 0.3);
    aparece("#marca img", T1 + 0.3);
    aparece("#marca p", T1 + 0.3);
    apaga(["#o-nombre", "#o-anuncio"], T1, 0.12);
  }

  // —— LAS PERSONAS DEL GRUPO (A6 y B5): de un subrayado bajan cuatro hebras, una por persona, de
  // izquierda a derecha, y en cada una brota la persona (cabeza y hombros, sin cara, como los gastos
  // de «Un trazo»). Devuelve cuándo llega cada una.
  function grupo(Y, YC, llegan, desde) {
    var XP = [285, 455, 625, 795];
    XP.forEach(function (x, i) {
      var el = a("hb" + i), xm = 540 + (x - 540) * 0.5, y1 = YC - 46;
      el.setAttribute("d", "M540," + Y + " C540," + (Y + 40) + " " + xm + "," + (Y + 30) + " " + xm + "," + ((Y + y1) / 2) +
                           " C" + xm + "," + (y1 - 20) + " " + x + "," + (y1 - 30) + " " + x + "," + y1);
      var L = el.getTotalLength();
      el.setAttribute("stroke-dasharray", L + " " + (L + 20));
      el.setAttribute("stroke-dashoffset", L);
      tl.fromTo(el, { attr: { "stroke-dashoffset": L } }, { attr: { "stroke-dashoffset": 0 }, duration: llegan[i] - desde, ease: "power1.inOut" }, desde);
      var g = a("g" + i);
      g.querySelector("circle").setAttribute("cx", x); g.querySelector("circle").setAttribute("cy", YC);
      g.querySelector("path").setAttribute("d", "M" + (x - 52) + "," + (YC + 108) + " C" + (x - 52) + "," + (YC + 52) + " " + (x + 52) + "," + (YC + 52) + " " + (x + 52) + "," + (YC + 108));
      gsap.set("#g" + i, { svgOrigin: x + " " + (YC + 108) });
      brota("#g" + i, llegan[i], "back.out(2.4)");
    });
    return XP;
  }
  function recogeGrupo(t) {
    [0, 1, 2, 3].forEach(function (i) {
      var el = a("hb" + i), L = el.getTotalLength();
      tl.fromTo(el, { attr: { "stroke-dashoffset": 0 } }, { attr: { "stroke-dashoffset": L + 2 }, duration: 0.24, ease: "power1.in", immediateRender: false }, t);
      encoge("#g" + i, t + 0.02 * i);
    });
  }

  // —— EL CIERRE que aprobó el dueño en «Un trazo», sin cambios salvo el aviso de Apple de que las
  // secuencias van acortadas («If app sequences are shortened, display a 'sequences shortened'
  // disclaimer»), delante del crédito de marcas. La insignia aparece ENTERA de un fotograma a otro y
  // no se mueve nunca.
  function cierre(T8, FIN, VERSION) {
    aparece("#papel", T8);
    tl.fromTo("#c-icono", { autoAlpha: 0, scale: 0.06 }, { autoAlpha: 1, scale: 1, duration: 0.6, ease: "back.out(1.4)" }, T8 + 0.2);
    entra("#c-nombre", T8 + 0.35, 24, ARR);
    aparece("#c-insignia", T8 + 0.6);
    entra("#c-android", T8 + 0.8, 16, ARR);
    tl.fromTo("#c-credito", { autoAlpha: 0 }, { autoAlpha: 1, duration: 0.4, ease: "none" }, T8 + 1.0);
    var TIEMPO = 0.8;   // la negra de la música (75 BPM)
    for (var tp = T8 + 1.25; tp < FIN - 0.25; tp += TIEMPO) {
      tl.fromTo("#c-icono", { scale: 1 }, { scale: 1.04, duration: 0.16, ease: "power2.out", immediateRender: false }, tp);
      tl.fromTo("#c-icono", { scale: 1.04 }, { scale: 1, duration: TIEMPO - 0.2, ease: "power1.inOut", immediateRender: false }, tp + 0.16);
    }
    if (VERSION === "limpia") {
      tl.set(["#c-flecha", "#c-perfil"], { autoAlpha: 0 }, 0);
    } else if (VERSION === "reel") {
      gsap.set("#c-perfil", { top: 1256 });
      gsap.set("#c-credito", { top: 1324 });
      entra("#c-perfil", T8 + 1.0, 12, ARR);
      tl.set("#c-flecha", { autoAlpha: 0 }, 0);
    } else {
      tl.set("#c-perfil", { autoAlpha: 0 }, 0);
      tl.fromTo("#c-flecha", { autoAlpha: 0, y: -8 }, { autoAlpha: 1, y: 0, duration: 0.25, ease: "power2.out" }, T8 + 0.95);
      for (var tb = T8 + 1.25; tb < FIN - 0.25; tb += TIEMPO) {
        tl.fromTo("#c-flecha", { y: 0 }, { y: 12, duration: 0.18, ease: "power2.out", immediateRender: false }, tb);
        tl.fromTo("#c-flecha", { y: 12 }, { y: 0, duration: TIEMPO - 0.2, ease: "power1.inOut", immediateRender: false }, tb + 0.18);
      }
    }
    tl.set({}, {}, FIN);
  }

  // El estirado: todo se escribió a 1× y el vídeo va a VELOCIDAD. Misma línea de tiempo plana, con
  // otros comienzos y otras duraciones.
  function acelera() {
    tl.getChildren(false, true, true).forEach(function (c) {
      var s0 = c.startTime(), d0 = c.duration();
      if (d0 > 0) c.duration(d0 / VELOCIDAD);
      c.startTime(s0 / VELOCIDAD);
    });
  }

  return { F: F, FPS: FPS, a: a, P: P, Camino: Camino, mide: mide, pon: pon, valor: valor, cuando: cuando,
           cadena: cadena, salida: salida, nodo: nodo, borde: borde, espiral: espiral, logo: logo, grupo: grupo,
           recogeGrupo: recogeGrupo, cierre: cierre, acelera: acelera, corta: corta, aparece: aparece, funde: funde,
           entra: entra, apaga: apaga, brota: brota, encoge: encoge, late: late, frase: frase, IN: IN, ARR: ARR };
};
