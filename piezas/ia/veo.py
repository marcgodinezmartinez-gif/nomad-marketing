# UNA TOMA CON VEO 3.1 por la API de Gemini, a partir de un texto y, si se le da, de una
# FOTO REAL como primer fotograma (5-oct, reel de la audioguía).
#
# LA FOTO NO ES OPCIONAL CUANDO SALE UN SITIO DE VERDAD. Medido el 5-oct: sólo con texto,
# Veo pintó una catedral gótica con cuatro agujas y la llamó Sagrada Família; las manos, el
# estuche y el ruido de la gente, en cambio, salieron bien. Con la foto CC0 de la fachada
# del Nacimiento como primer fotograma, la basílica es la de verdad. La foto entra en el
# banco como cualquier otra (`banco/fotos/creditos.json`).
#
# Lo que cuesta (página de precios de la API, 5-oct): 1080p sólo admite 8 s, y son 0,96 $
# la toma con `veo-3.1-fast-generate-preview`, 0,64 $ con `-lite` y 3,20 $ con el
# estándar. No hay capa gratuita. La clave sale del entorno y no se imprime nunca.
#
# Lo que sale va etiquetado como IA en Instagram: Meta lo exige para vídeo fotorrealista y
# audio realista creados o alterados digitalmente.
#
# Uso, desde salida/:
#   python3 ../piezas/ia/veo.py <nombre> <modelo> <prompt.txt> [segundos] [resolución] [foto.jpg]
# El prompt.txt lleva el texto y, si hace falta, una línea «NEGATIVO:» con lo que no debe salir.
# La foto, a 1080×1920 (9:16) y en JPEG. Deja <nombre>.mp4 en el directorio de trabajo.
import base64, json, os, sys, time, urllib.request, urllib.error

nombre, modelo, fichero = sys.argv[1:4]
segundos = int(sys.argv[4]) if len(sys.argv) > 4 else 8
resolucion = sys.argv[5] if len(sys.argv) > 5 else '1080p'
imagen = sys.argv[6] if len(sys.argv) > 6 else None
CLAVE = os.environ['GEMINI_API_KEY']
BASE = 'https://generativelanguage.googleapis.com/v1beta'
prompt, _, negativo = open(fichero).read().partition('\nNEGATIVO:')

def pide(url, cuerpo=None):
    req = urllib.request.Request(url, data=json.dumps(cuerpo).encode() if cuerpo else None,
                                 headers={'x-goog-api-key': CLAVE, 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f'HTTP {e.code}: {e.read().decode()[:800]}')

parametros = {'aspectRatio': '9:16', 'resolution': resolucion, 'durationSeconds': segundos}
if negativo.strip():
    parametros['negativePrompt'] = negativo.strip()
instancia = {'prompt': prompt.strip()}
if imagen:
    instancia['image'] = {'bytesBase64Encoded': base64.b64encode(open(imagen, 'rb').read()).decode(),
                          'mimeType': 'image/jpeg'}
op = pide(f'{BASE}/models/{modelo}:predictLongRunning',
          {'instances': [instancia], 'parameters': parametros})
print('operación', op.get('name', op), flush=True)
t0 = time.time()
while not op.get('done'):
    time.sleep(10)
    op = pide(f'{BASE}/{op["name"]}')
    if time.time() - t0 > 600:
        sys.exit('más de 10 minutos esperando')
if 'error' in op:
    sys.exit(f'ERROR {json.dumps(op["error"])[:800]}')
muestras = op.get('response', {}).get('generateVideoResponse', {}).get('generatedSamples') or []
if not muestras:
    sys.exit('sin vídeo: ' + json.dumps(op.get('response'))[:800])
for i, m in enumerate(muestras):
    req = urllib.request.Request(m['video']['uri'], headers={'x-goog-api-key': CLAVE})
    destino = f'{nombre}{"-" + str(i) if i else ""}.mp4'
    with urllib.request.urlopen(req, timeout=300) as resp, open(destino, 'wb') as f:
        f.write(resp.read())
    print('bajado', destino, os.path.getsize(destino), 'bytes', f'{time.time() - t0:.0f} s', flush=True)
