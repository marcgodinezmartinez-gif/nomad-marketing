# UNA FRASE CON UNA VOZ DE LA APP (Kore, Puck, Charon…) por Gemini TTS, a WAV (5-oct).
#
# Para ensayar montajes, no para publicar: lo que suena en un reel es la narración REAL de
# la app (RODAJE.md, regla 3). Sirve también para el relevo de voces si al cambiar de voz
# la app lee el mismo texto: entonces la misma frase con las tres voces es lo que la app
# haría. La primera indicación de estilo NO se lee en voz alta (comprobado transcribiendo).
#
# OJO, medido el 5-oct: una de cuatro tomas se comió una palabra («Estás de la fachada» por
# «Estás delante de la fachada»). Cada toma se transcribe antes de usarla
# (`faster-whisper`, modelo medium: el small no lo detectó).
#
# Uso: python3 piezas/ia/voz.py <salida.wav> <voz> <modelo> "<texto>"
#      p. ej. gemini-2.5-flash-preview-tts. La clave sale del entorno y no se imprime.
import base64, json, os, subprocess, sys, urllib.request, urllib.error

salida, voz, modelo, texto = sys.argv[1:5]
FF = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'node_modules', 'ffmpeg-static', 'ffmpeg')
cuerpo = {'contents': [{'parts': [{'text': texto}]}],
          'generationConfig': {'responseModalities': ['AUDIO'],
                               'speechConfig': {'voiceConfig': {'prebuiltVoiceConfig': {'voiceName': voz}}}}}
req = urllib.request.Request(
    f'https://generativelanguage.googleapis.com/v1beta/models/{modelo}:generateContent',
    data=json.dumps(cuerpo).encode(),
    headers={'x-goog-api-key': os.environ['GEMINI_API_KEY'], 'Content-Type': 'application/json'})
try:
    with urllib.request.urlopen(req, timeout=180) as r:
        d = json.load(r)
except urllib.error.HTTPError as e:
    sys.exit(f'HTTP {e.code}: {e.read().decode()[:600]}')
parte = d['candidates'][0]['content']['parts'][0]['inlineData']
pcm = base64.b64decode(parte['data'])          # PCM 16 bits, 24 kHz, mono
subprocess.run([FF, '-nostdin', '-loglevel', 'error', '-y', '-f', 's16le', '-ar', '24000', '-ac', '1',
                '-i', 'pipe:0', salida], input=pcm, check=True)
print(salida, f'{len(pcm) / 48000:.2f} s')
