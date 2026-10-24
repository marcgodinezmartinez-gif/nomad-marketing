# UNA PISTA DE MÚSICA CON LYRIA por la API de Gemini (24-oct, anuncio del lanzamiento).
#
# El 6-oct se hizo a mano para el reel de la Sagrada Família (VEO.md, «La versión final»);
# esto lo deja escrito. `lyria-3-clip-preview` devuelve un clip de unos 30 s, instrumental si
# se pide, con la marca de agua SynthID dentro. Lo que sale es música generada con IA: al
# publicar se marca la etiqueta de IA (Instagram: Configuración avanzada; TikTok: «Contenido
# generado por IA»).
#
# Uso: python3 piezas/ia/musica.py <salida-sin-extensión> <modelo> <prompt.txt>
#      Escribe <salida>.<ext> con la extensión que diga el tipo MIME devuelto, y el texto
#      que acompañe a la pista (si lo hay) en <salida>.txt. La clave sale del entorno y no
#      se imprime nunca.
import base64, json, os, sys, urllib.request, urllib.error

salida, modelo, fichero = sys.argv[1:4]
prompt = open(fichero, encoding='utf-8').read().strip()
cuerpo = {'contents': [{'parts': [{'text': prompt}]}]}
req = urllib.request.Request(
    f'https://generativelanguage.googleapis.com/v1beta/models/{modelo}:generateContent',
    data=json.dumps(cuerpo).encode(),
    headers={'x-goog-api-key': os.environ['GEMINI_API_KEY'], 'Content-Type': 'application/json'})
try:
    with urllib.request.urlopen(req, timeout=300) as r:
        d = json.load(r)
except urllib.error.HTTPError as e:
    sys.exit(f'HTTP {e.code}: {e.read().decode()[:600]}')
EXT = {'audio/mpeg': 'mp3', 'audio/mp3': 'mp3', 'audio/wav': 'wav', 'audio/x-wav': 'wav', 'audio/L16': 'pcm'}
textos = []
for parte in d['candidates'][0]['content']['parts']:
    if 'inlineData' in parte:
        tipo = parte['inlineData'].get('mimeType', 'audio/mpeg').split(';')[0]
        destino = f'{salida}.{EXT.get(tipo, "bin")}'
        open(destino, 'wb').write(base64.b64decode(parte['inlineData']['data']))
        print(destino, tipo, os.path.getsize(destino), 'bytes')
    elif 'text' in parte:
        textos.append(parte['text'])
if textos:
    open(f'{salida}.txt', 'w', encoding='utf-8').write('\n'.join(textos))
    print('texto:', ' '.join(textos)[:300])
