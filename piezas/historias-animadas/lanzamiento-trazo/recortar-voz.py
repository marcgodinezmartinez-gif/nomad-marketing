# Recorta una toma de voz sin comerse finales: por detrás, lo que queda por encima de -64 dB,
# uniendo huecos de menos de 0,15 s (el cierre antes de una «d» o una «t» final), y soltando lo que
# viene después de un silencio más largo (un chasquido o una respiración sueltos). Fundido de 40 ms.
import subprocess, sys, numpy as np
ent, sal = sys.argv[1:3]
sr = 48000
a = np.frombuffer(subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', ent, '-f', 'f32le', '-ac', '1', '-ar', str(sr), '-'],
                                 capture_output=True).stdout, np.float32).copy()
h = sr // 100
e = np.array([20 * np.log10(np.sqrt(np.mean(a[i:i + h] ** 2)) + 1e-9) for i in range(0, len(a) - h, h)])
on = e > -64
seg, i = [], 0
while i < len(on):
    if on[i]:
        j = i
        while j < len(on) and on[j]: j += 1
        if seg and i - seg[-1][1] < 15: seg[-1][1] = j
        else: seg.append([i, j])
        i = j
    else: i += 1
fuerte = np.where(e > -45)[0]
# El principio, a 40 ms de la primera sílaba fuerte: lo de antes es la respiración, y se queda fuera.
ini = max(0, fuerte[0] - 1)
fin = next(s for s in seg if s[0] <= fuerte[-1] < s[1])[1]
x = a[max(0, (ini - 3) * h):min(len(a), (fin + 2) * h)].copy()
n = int(0.04 * sr); x[-n:] *= np.linspace(1, 0, n); m = int(0.005 * sr); x[:m] *= np.linspace(0, 1, m)
subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'f32le', '-ar', str(sr), '-ac', '1', '-i', '-', '-sample_fmt', 's16', sal],
               input=x.astype(np.float32).tobytes(), check=True)
print(f"{sal}: {len(x)/sr:.2f} s (de {ini/100:.2f} a {fin/100+0.02:.2f} en la toma)")
