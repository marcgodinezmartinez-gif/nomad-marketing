# LAS VOCES DE «TU PRIMER VIAJE, GRATIS» (24-nov): de las tomas crudas a las seis frases en su sitio.
#
# Qué hace, en orden:
# 1. Coge la toma elegida de cada frase (assets/voz/tomas/<id>.rec.flac, ya recortada con
#    ../lanzamiento-trazo/recortar-voz.py). Las tomas que no se eligieron no se versionan.
# 2. Acorta las pausas largas DENTRO de la frase: todo silencio de más de PAUSA_MAX se queda en
#    PAUSA_DEJA. La guía de la app para 0,8 s después de «1755»; en un reel eso es aire muerto. No se
#    toca ninguna palabra: sólo se quita silencio, con un fundido de 8 ms a cada lado del corte.
# 3. La acelera con atempo (WSOLA), no con rubberband: ver ../puente-viena/mezclar.sh, 30-oct.
# 4. La transcribe otra vez, ya acelerada, para sacar cuándo empieza cada palabra.
# 5. Calcula dónde va cada frase en el vídeo y escribe assets/tiempos.js (lo lee index.html) y
#    assets/tiempos.json (lo lee mezclar.sh). Los cortes del vídeo salen de la voz, no al revés.
#
# Uso: python3 -I preparar-voz.py     (desde esta carpeta)
import json, os, re, subprocess, sys
import numpy as np

AQUI = os.path.dirname(os.path.abspath(__file__))
os.chdir(AQUI)
SR = 48000
VEL = 1.15
PAUSA_MAX, PAUSA_DEJA = 0.34, 0.26
# id de la frase, su toma, y el texto tal como se pidió (para comparar con lo que se oye).
FRASES = [
    ('k1', 'k1b-2', 'Una IA te hace la lista en diez segundos.'),
    ('k2', 'k2-2', 'Pero cuando estás allí, ¿quién te cuenta lo que tienes delante?'),
    ('g1', 'g1-2', 'El 1 de noviembre de 1755, un devastador terremoto seguido de un maremoto y un incendio voraz '
                   'destruyó el antiguo Palacio Real que se erigía exactamente en este espacio.'),
    ('k3', 'k3b-2', 'Eso es Nomad. Te guía a pie, parada a parada, y en el museo, obra a obra.'),
    ('k4', 'k4-2', 'Y esta semana, tu primer viaje es gratis.'),
    ('k5', 'k5-2', 'Descárgala en la App Store o en Google Play.'),
]
# El aire entre frases, en segundos del vídeo final. El corte de escena va en medio.
AIRE = {'k1': 0.20, 'k2': 0.22, 'g1': 0.36, 'k3': 0.30, 'k4': 0.30, 'k5': 0.40}
# Lo que se queda quieto después de la última palabra de la oferta (para leer las condiciones) y del cierre.
QUIETO_OFERTA, QUIETO_CIERRE = 1.70, 1.50


def lee(f):
    return np.frombuffer(subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', f, '-f', 'f32le', '-ac', '1', '-ar', str(SR), '-'],
                                        capture_output=True, check=True).stdout, np.float32).copy()


def escribe(x, f, extra=()):
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', '-', *extra, f],
                   input=x.astype(np.float32).tobytes(), check=True)


def sin_pausas_largas(x):
    h = SR // 200                                   # ventanas de 5 ms
    e = np.array([20 * np.log10(np.sqrt(np.mean(x[i:i + h] ** 2)) + 1e-9) for i in range(0, len(x) - h, h)])
    callado = e < -52
    trozos, i, quitado = [], 0, 0.0
    ini = 0
    while i < len(callado):
        if callado[i]:
            j = i
            while j < len(callado) and callado[j]: j += 1
            largo = (j - i) * h / SR
            if largo > PAUSA_MAX and i > 0 and j < len(callado):
                sobra = int((largo - PAUSA_DEJA) * SR)
                a = i * h + int(PAUSA_DEJA * SR / 2)       # se quita el centro del silencio
                trozos.append(x[ini:a]); ini = a + sobra; quitado += sobra / SR
            i = j
        else:
            i += 1
    trozos.append(x[ini:])
    f = int(0.008 * SR)
    for k, t in enumerate(trozos):
        t = t.copy()
        if k > 0: t[:f] *= np.linspace(0, 1, f)
        if k < len(trozos) - 1: t[-f:] *= np.linspace(1, 0, f)
        trozos[k] = t
    return np.concatenate(trozos), quitado


def main():
    from faster_whisper import WhisperModel
    modelo = WhisperModel('small', device='cpu', compute_type='int8')
    os.makedirs('assets/voz', exist_ok=True)
    datos, t = {}, 0.20                              # la primera frase empieza en 0,20
    orden = []
    for ident, toma, texto in FRASES:
        x, quitado = sin_pausas_largas(lee(f'assets/voz/tomas/{toma}.rec.flac'))
        tmp = f'/tmp/_{ident}.wav'
        escribe(x, tmp)
        sal = f'assets/voz/{ident}.flac'
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', tmp, '-af', f'atempo={VEL}', '-ar', str(SR), sal], check=True)
        y = lee(sal)
        dur = len(y) / SR
        segs, _ = modelo.transcribe(np.frombuffer(subprocess.run(
            ['ffmpeg', '-loglevel', 'error', '-i', sal, '-f', 'f32le', '-ac', '1', '-ar', '16000', '-'],
            capture_output=True).stdout, np.float32), language='es', beam_size=5, word_timestamps=True)
        palabras = [(w.word.strip(), round(float(w.start), 2)) for s in segs for w in s.words]
        oido = ' '.join(p for p, _ in palabras)
        # La página enciende cada palabra por su número: si whisper parte la frase de otra forma, se para aquí.
        espera = {'k2': 11, 'g1': 29, 'k3': 17, 'k4': 8}.get(ident)
        if espera and len(palabras) != espera:
            sys.exit(f'{ident}: se esperaban {espera} palabras y whisper da {len(palabras)}: {oido}')
        datos[ident] = {'empieza': round(t, 2), 'dura': round(dur, 2), 'acaba': round(t + dur, 2),
                        'palabras': [[p, round(t + a, 2)] for p, a in palabras], 'texto': texto, 'oido': oido}
        print(f'{ident}: {dur:5.2f} s (quitados {quitado:.2f} s de pausa), de {t:6.2f} a {t + dur:6.2f} | {oido}')
        orden.append(ident)
        t = t + dur + AIRE[ident]
        if ident == 'k4': t += QUIETO_OFERTA
    fin = round(datos['k5']['acaba'] + QUIETO_CIERRE, 2)
    # Los cortes: en medio del aire entre dos frases.
    def entre(a, b, hacia=0.5):
        return round(datos[a]['acaba'] + (datos[b]['empieza'] - datos[a]['acaba']) * hacia, 2)
    cortes = {
        'pivote': entre('k1', 'k2', 0.6),            # la lista se apaga y queda una línea
        'nomad': entre('k2', 'g1', 0.45),            # del chat a la app
        'resumen': entre('g1', 'k3', 0.55),          # «Eso es Nomad»
        'oferta': round(datos['k4']['empieza'] - 0.10, 2),
        'cierre': round(datos['k5']['empieza'] - 0.22, 2),
        'fin': fin,
    }
    # El chat suelta sus 14 líneas entre el principio y un poco antes del pivote. mezclar.sh pone un
    # tic en cada una, y nada mientras «piensa» (el fallo más común de este formato es sonar ahí).
    # Las cuatro primeras ya están escritas en el fotograma 0 (tiempo 0): la portada no sale medio vacía.
    n, ya = 14, 4
    a, b = 0.25, cortes['pivote'] - 0.35
    flujo = [0.0] * ya + [round(a + (b - a) * i / (n - ya - 1), 3) for i in range(n - ya)]
    todo = {'vel': VEL, 'frases': datos, 'cortes': cortes, 'flujo': flujo}
    json.dump(todo, open('assets/tiempos.json', 'w'), ensure_ascii=False, indent=1)
    open('assets/tiempos.js', 'w').write('// Lo escribe preparar-voz.py. No se edita a mano.\nwindow.TIEMPOS = '
                                         + json.dumps(todo, ensure_ascii=False) + ';\n')
    print('cortes:', cortes)
    # La duración va escrita en index.html (HyperFrames la lee del HTML, no de un script).
    if os.path.exists('index.html'):
        h = open('index.html', encoding='utf-8').read()
        h2 = re.sub(r'data-duration="[0-9.]+"', f'data-duration="{fin}"', h)
        if h2 != h:
            open('index.html', 'w', encoding='utf-8').write(h2)
            print('index.html: data-duration =', fin)


if __name__ == '__main__':
    main()
