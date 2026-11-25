# EL SONIDO DE «TU PRIMER VIAJE, GRATIS» (25-nov). Escribe assets/sonido.m4a (con música) y
# assets/sonido-sin-musica.m4a (voz y efectos: para ponerle un audio de tendencias en Instagram).
#
# Tres pistas, cada una colocada con los tiempos de assets/tiempos.json (preparar-voz.py):
# - LA VOZ: Kore narra y Charon es la audioguía, las dos voces de la app, con el modelo de la app
#   (gemini-3.1-flash-tts-preview). Cada frase a -18 LUFS, paso alto a 80 Hz y compresión suave, como
#   en ../puente-viena/mezclar.sh.
# - LOS EFECTOS, hechos aquí con ruido filtrado, sin fichero de nadie: dos tics de reloj en cada cambio
#   de hora, un soplo al pasar del gancho a Lisboa y al llegar la oferta, y un golpe grave y corto en
#   los dos «gratis».
# - LA MÚSICA (assets/musica/m2.mp3, Lyria, 100 BPM): dura 30,8 s y se apaga sola desde el 25,5, así
#   que se le repiten ocho negras por dentro para que llegue entera al cierre. A -33 LUFS, quince por
#   debajo de la voz, y se aparta mientras alguien habla.
# Todo junto, a -14 LUFS y -1,5 dBTP con una ganancia fija (loudnorm lineal, comprobado).
#
# Uso: python3 -I mezclar.py      (desde esta carpeta)
import json, os, subprocess, sys, tempfile
import numpy as np

AQUI = os.path.dirname(os.path.abspath(__file__))
os.chdir(AQUI)
SR = 48000
T = json.load(open('assets/tiempos.json'))
FIN = T['cortes']['fin']
N = int(FIN * SR)
TMP = tempfile.mkdtemp()


def ff(*a, entrada=None):
    return subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', *a], input=entrada, capture_output=True, check=True)


def lee(f, canales=1, filtro=None):
    a = ['-i', f] + (['-af', filtro] if filtro else []) + ['-f', 'f32le', '-ac', str(canales), '-ar', str(SR), '-']
    x = np.frombuffer(subprocess.run(['ffmpeg', '-loglevel', 'error', *a], capture_output=True, check=True).stdout, np.float32).copy()
    return x.reshape(-1, canales) if canales > 1 else x


def escribe(x, f):
    c = 1 if x.ndim == 1 else x.shape[1]
    ff('-f', 'f32le', '-ar', str(SR), '-ac', str(c), '-i', '-', '-c:a', 'pcm_f32le', f, entrada=x.astype(np.float32).tobytes())


def lufs(f):
    s = subprocess.run(['ffmpeg', '-hide_banner', '-i', f, '-af', 'ebur128', '-f', 'null', '-'], capture_output=True, text=True).stderr
    return float([l for l in s.splitlines() if l.strip().startswith('I:')][-1].split()[1])


# ── LA VOZ ────────────────────────────────────────────────────────────────────
voz = np.zeros(N + SR, np.float32)
for ident, d in T['frases'].items():
    f = f'assets/voz/{ident}.flac'
    gan = -18 - lufs(f)
    x = lee(f, 1, f'highpass=f=80,volume={gan:.2f}dB,acompressor=threshold=-24dB:ratio=2.5:attack=8:release=160:makeup=1')
    i = int(d['empieza'] * SR)
    voz[i:i + len(x)] += x
    # Que llegue entera: los 60 ms de antes de su final tienen que sonar.
    cola = voz[i + len(x) - int(0.10 * SR):i + len(x) - int(0.04 * SR)]
    if 20 * np.log10(np.sqrt(np.mean(cola ** 2)) + 1e-12) < -90:
        sys.exit(f'{ident} llega cortada')
voz = voz[:N]
escribe(voz, f'{TMP}/voz.wav')

# ── LOS EFECTOS ───────────────────────────────────────────────────────────────
rng = np.random.default_rng(479)
fx = np.zeros(N, np.float32)


def pon(x, t, gan_db):
    i = int(t * SR)
    if i >= N: return
    x = x[:N - i] * 10 ** (gan_db / 20)
    fx[i:i + len(x)] += x.astype(np.float32)


def ruido_filtrado(dur, f_lo, f_hi):
    n = int(dur * SR)
    X = np.fft.rfft(rng.standard_normal(n))
    fr = np.fft.rfftfreq(n, 1 / SR)
    X[(fr < f_lo) | (fr > f_hi)] = 0
    y = np.fft.irfft(X, n)
    return y / (np.max(np.abs(y)) + 1e-9)


C = T['cortes']
# Los tics del reloj: dos, en cada cambio de hora del día. 14 ms de ruido entre 1,8 y 4,5 kHz que se apaga.
for nombre in ('plan', 'plaza', 'comer', 'cuentas', 'asistente'):
    for k, dt in enumerate((0.0, 0.11)):
        tic = ruido_filtrado(0.014, 1800, 4500) * np.exp(-np.linspace(0, 6, int(0.014 * SR)))
        pon(tic, C[nombre] + dt, -25 - 3 * k)
# Los soplos: medio segundo de ruido que sube y se va, al pasar del gancho a Lisboa y al llegar la oferta.
n = int(0.5 * SR)
env = np.sin(np.linspace(0, np.pi, n)) ** 2
pon(ruido_filtrado(0.5, 300, 2600) * env, C['viajar'] - 0.28, -28)
pon(ruido_filtrado(0.5, 300, 2600) * env, C['oferta'] - 0.28, -28)
# El golpe de «gratis»: una nota grave que baja de 78 a 46 Hz en un tercio de segundo. Saturada, para
# que tenga armónicos: un seno limpio de 46-78 Hz no sale por el altavoz de un móvil (revisión del 24-nov).
n = int(0.34 * SR)
tt = np.arange(n) / SR
fase = 2 * np.pi * np.cumsum(np.linspace(78, 46, n)) / SR
golpe = np.tanh(3 * np.sin(fase)) * np.exp(-tt * 11)
golpe = golpe / np.max(np.abs(golpe))
pon(golpe, T['frases']['n8']['palabras'][6][1] - 0.04, -17)     # el de la oferta
pon(golpe, T['frases']['n1']['palabras'][5][1] - 0.04, -19)     # el del gancho: «gratis» abre el vídeo
escribe(fx, f'{TMP}/fx.wav')

# ── LA MÚSICA ─────────────────────────────────────────────────────────────────
m = lee('assets/musica/m2.mp3', 2)
mono = m.mean(axis=1)
# La negra: se busca el periodo y la fase que mejor casan con los arranques (flujo espectral).
h, w = 256, 1024
tr = np.array([np.abs(np.fft.rfft(mono[i:i + w] * np.hanning(w))) for i in range(0, len(mono) - w, h)])
flujo = np.maximum(0, np.diff(tr, axis=0)).sum(axis=1)
flujo /= flujo.max()
tf = np.arange(len(flujo)) * h / SR
mejor = (0, 0, 0)
for per in np.arange(0.585, 0.625, 0.0002):
    for fase0 in np.arange(0, per, 0.004):
        idx = np.round((np.arange(fase0, 24, per)) * SR / h).astype(int)
        idx = idx[idx < len(flujo)]
        s = flujo[idx].sum()
        if s > mejor[0]: mejor = (s, per, fase0)
_, per, fase0 = mejor
# Se repiten ocho negras a partir de la primera negra después del segundo 12.
b = fase0 + np.ceil((12.0 - fase0) / per) * per
i0, i1 = int(b * SR), int((b + 8 * per) * SR)
x = int(0.03 * SR)
r = np.linspace(0, 1, x)[:, None]
cola = m[i1 - x:i1] * (1 - r) + m[i0 - x:i0] * r          # fundido de 30 ms en la junta
larga = np.concatenate([m[:i1 - x], cola, m[i0:]])
print(f'música: negra de {per:.4f} s ({60 / per:.1f} BPM), se repite de {b:.2f} a {b + 8 * per:.2f}; queda de {len(larga) / SR:.1f} s')
if len(larga) < N: sys.exit('la música no llega al final')
larga = larga[:N]
escribe(larga, f'{TMP}/mus.wav')
mus = larga
# Entra con un fundido corto y se va en los últimos 0,8 s, cuando ya ha vuelto a subir detrás de la voz.
ent, sal = int(0.15 * SR), int(0.8 * SR)
mus[:ent] *= np.linspace(0, 1, ent)[:, None]
mus[-sal:] *= np.linspace(1, 0, sal)[:, None]
escribe(mus, f'{TMP}/mus2.wav')
gm = -33 - lufs(f'{TMP}/mus2.wav')


def mezcla(salida, con_musica):
    crudo = f'{TMP}/mezcla.wav'
    if con_musica:
        grafo = (f"[0:a]volume={gm:.2f}dB[mus];[1:a]asplit=2[v1][sc];"
                 "[mus][sc]sidechaincompress=threshold=0.04:ratio=3:attack=60:release=550[dk];"
                 "[v1]pan=stereo|c0=c0|c1=c0[vs];[2:a]pan=stereo|c0=c0|c1=c0[fx];"
                 "[dk][vs][fx]amix=inputs=3:normalize=0,alimiter=limit=0.22:attack=3:release=60:level=false[mx]")
        ff('-i', f'{TMP}/mus2.wav', '-i', f'{TMP}/voz.wav', '-i', f'{TMP}/fx.wav', '-filter_complex', grafo,
           '-map', '[mx]', '-c:a', 'pcm_s24le', crudo)
    else:
        grafo = ("[0:a]pan=stereo|c0=c0|c1=c0[vs];[1:a]pan=stereo|c0=c0|c1=c0[fx];"
                 "[vs][fx]amix=inputs=2:normalize=0,alimiter=limit=0.22:attack=3:release=60:level=false[mx]")
        ff('-i', f'{TMP}/voz.wav', '-i', f'{TMP}/fx.wav', '-filter_complex', grafo, '-map', '[mx]', '-c:a', 'pcm_s24le', crudo)
    # loudnorm en dos pasadas y LINEAL (una ganancia fija). Si no queda lineal, se para: ver
    # ../lanzamiento-ios/mezclar.sh.
    def mide(extra=''):
        s = subprocess.run(['ffmpeg', '-hide_banner', '-i', crudo, '-af', f'loudnorm=I=-14:TP=-1.5:LRA=20{extra}:print_format=json',
                            '-f', 'null', '-'], capture_output=True, text=True).stderr
        return json.loads(s[s.rindex('{'):s.rindex('}') + 1])
    a = mide()
    ln = (f":measured_I={a['input_i']}:measured_TP={a['input_tp']}:measured_LRA={a['input_lra']}"
          f":measured_thresh={a['input_thresh']}:offset={a['target_offset']}:linear=true")
    tipo = mide(ln)['normalization_type']
    if tipo != 'linear': sys.exit(f'loudnorm no queda lineal ({tipo}) en {salida}: baja el limit del alimiter')
    ff('-i', crudo, '-af', f'loudnorm=I=-14:TP=-1.5:LRA=20{ln},aresample=48000', '-ar', '48000', '-ac', '2', '-c:a', 'aac', '-b:a', '256k', salida)
    s = subprocess.run(['ffmpeg', '-hide_banner', '-i', salida, '-af', 'ebur128=peak=true', '-f', 'null', '-'], capture_output=True, text=True).stderr
    datos = [l.strip() for l in s.splitlines() if l.strip().startswith(('I:', 'Peak:', 'LRA:'))][-3:]
    print(salida, '|', ' · '.join(datos))


mezcla('assets/sonido.m4a', True)
mezcla('assets/sonido-sin-musica.m4a', False)
