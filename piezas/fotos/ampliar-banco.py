# Amplía banco/fotos/ con fotos nuevas CC0 o de dominio público (2-sep).
#
# LA TRAMPA DE COMMONS, CORREGIDA. AGENTS.md decía «Commons devuelve 429 a las descargas
# desde el contenedor». Medido hoy: lo que devuelve 429 es SÓLO la API vieja (w/api.php).
# El servidor de ficheros (upload.wikimedia.org) baja originales de 26 MB sin rechistar, y
# la API REST (w/rest.php) responde. Así que sí se pueden bajar fotos desde aquí; lo único
# que no se puede es usar api.php.
#
# Cómo encuentra candidatas sin machacar Commons: Openverse devuelve la licencia EN EL
# PROPIO RESULTADO, así que una petición por término da una lista ya filtrada a CC0/PD. De
# ahí sólo se conservan las de proveedor `wikimedia`.
#
# Y LA LICENCIA SE VERIFICA IGUAL, foto a foto, contra la página de Commons: la regla del
# repo es «sólo CC0 o dominio público, verificadas foto a foto», y fiarse del agregador
# sería justo lo que esa regla prohíbe. Si la página no dice CC0 ni dominio público, la
# foto se descarta — no se baja.
#
# Los dos tamaños salen SIEMPRE del original, nunca uno del otro (trampa ya pagada: tres
# postales de 980x380 ampliadas cinco veces en una historia). Se recorta con ffmpeg, que
# ya es dependencia del repo, para no volver a meter Pillow.
#
# Uso:  python3 piezas/fotos/ampliar-banco.py            (busca, verifica, baja y recorta)
#       python3 piezas/fotos/ampliar-banco.py --rehacer  (sólo rehace las rotas de post/)
import hashlib, json, os, re, subprocess, sys, time, urllib.parse, urllib.request

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
FOTOS = f'{RAIZ}/banco/fotos'
ORIG = '/tmp/nomad-originales'          # los originales pesan; no entran en el repo
UA = 'NOMAD-marketing/1.0 (https://travelsnomad.com; contacto via GitHub)'
FFMPEG = f'{RAIZ}/node_modules/ffmpeg-static/ffmpeg'
POST, HISTORIA = (1080, 1350), (1080, 1920)

# Lo que le falta al banco para montar ideas nuevas. Once fotos hoy, casi todas de
# ciudades sueltas; esto añade el mercado español —que es EL mercado— y momentos de viaje
# que ninguna de las once cubre.
BUSQUEDAS = [
    ('madrid',      'madrid gran via'),
    ('sevilla',     'sevilla plaza de espana'),
    ('barcelona',   'barcelona park guell'),
    ('toledo',      'toledo spain city'),
    ('cordoba',     'cordoba mezquita'),
    ('valencia',    'valencia city of arts'),
    ('sansebastian','san sebastian donostia'),
    ('bilbao',      'bilbao guggenheim'),
    ('santiago',    'santiago de compostela cathedral'),
    ('segovia',     'segovia aqueduct'),
    ('florencia',   'florence duomo'),
    ('venecia',     'venice canal'),
    ('milan',       'milan duomo'),
    ('napoles',     'naples italy'),
    ('tren',        'train window landscape'),
    ('cafe',        'cafe terrace street'),
    ('calle',       'narrow old town street'),
    ('museo2',      'museum gallery interior'),
    ('mirador',     'viewpoint city sunset'),
    ('mapa',        'travel map paper'),
]

def pide(url, binario=False, reintentos=3):
    for n in range(reintentos):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read() if binario else r.read().decode('utf-8', 'replace')
        except Exception as e:
            if n == reintentos - 1:
                print(f'      fallo: {type(e).__name__}'); return None
            time.sleep(2 ** n)

def candidatas(consulta, n=6):
    """Openverse: una petición por término, con la licencia ya en el resultado."""
    q = urllib.parse.urlencode({'q': consulta, 'license': 'cc0',
                                'page_size': 20, 'mature': 'false'})
    cuerpo = pide(f'https://api.openverse.org/v1/images/?{q}')
    if not cuerpo: return []
    try: datos = json.loads(cuerpo)
    except Exception: return []
    out = []
    for r in datos.get('results', []):
        if r.get('provider') != 'wikimedia': continue
        landing = r.get('foreign_landing_url') or ''
        if 'commons.wikimedia.org' not in landing: continue
        w, h = r.get('width') or 0, r.get('height') or 0
        # Resolución mínima para no ampliar: 1080 de ancho y 1920 de alto en historia.
        if max(w, h) < 1500 or min(w, h) < 1000: continue
        out.append({'landing': landing, 'w': w, 'h': h})
        if len(out) >= n: break
    return out


def ficha(landing):
    """Openverse da `index.php?curid=N` para Wikimedia, no /wiki/File:. Esa página trae
    el título Y la licencia, así que una sola petición resuelve las dos cosas — y la
    licencia sale de Commons, no del agregador, que es lo que manda la regla."""
    html = pide(landing)
    if not html: return None, None
    m = re.search(r'<title>\s*(File:[^<]+?)\s*(?:-|–|—)\s*Wikimedia Commons\s*</title>', html)
    if not m: return None, None
    titulo = re.sub(r'&#39;', "'", m.group(1)).replace('&amp;', '&').strip()
    if not titulo.lower().endswith(('.jpg', '.jpeg', '.png')): return None, None
    if re.search(r'CC0 1\.0|Creative Commons CC0|CC0 waiver', html): return titulo, 'CC0'
    if re.search(r'public domain|Public Domain Mark|PD-self|PD-old', html, re.I):
        return titulo, 'Dominio público'
    return titulo, None

def licencia_verificada(titulo):
    """La regla del repo: sólo CC0 o dominio público, verificadas foto a foto.
    Se lee de la página de Commons, no del agregador."""
    slug = urllib.parse.quote(titulo.replace(' ', '_'), safe=':/')
    html = pide(f'https://commons.wikimedia.org/wiki/{slug}')
    if not html: return None
    if re.search(r'CC0 1\.0|Creative Commons CC0|CC0 waiver', html): return 'CC0'
    if re.search(r'public domain|Public Domain Mark|PD-self|PD-old', html, re.I):
        return 'Dominio público'
    return None                                   # cualquier otra cosa: se descarta

def url_original(titulo):
    slug = urllib.parse.quote(titulo.replace(' ', '_'), safe=':/')
    cuerpo = pide(f'https://commons.wikimedia.org/w/rest.php/v1/file/{slug}')
    if cuerpo:
        try: return json.loads(cuerpo)['original']['url'].split('?')[0]
        except Exception: pass
    # Plan B sin API: la ruta de upload se calcula del MD5 del nombre de fichero.
    fn = titulo.split(':', 1)[1].replace(' ', '_')
    h = hashlib.md5(fn.encode()).hexdigest()
    return (f'https://upload.wikimedia.org/wikipedia/commons/{h[0]}/{h[:2]}/'
            + urllib.parse.quote(fn))

def recorta(origen, destino, ancho, alto):
    """Escala hasta cubrir y recorta al centro. SIEMPRE desde el original."""
    subprocess.run([FFMPEG, '-y', '-loglevel', 'error', '-i', origen, '-vf',
                    f'scale={ancho}:{alto}:force_original_aspect_ratio=increase,'
                    f'crop={ancho}:{alto}', '-q:v', '2', destino], check=True)

def incorpora(clave, titulo, lic, creditos):
    """Baja el original y escribe los dos tamaños. Devuelve True si entró."""
    os.makedirs(ORIG, exist_ok=True)
    url = url_original(titulo)
    datos = pide(url, binario=True)
    if not datos or len(datos) < 40_000:
        print(f'      original no descargado ({url[:70]})'); return False
    ext = '.png' if url.lower().endswith('.png') else '.jpg'
    ruta = f'{ORIG}/{clave}{ext}'
    open(ruta, 'wb').write(datos)
    nombre = f'f-{clave}.jpg'
    recorta(ruta, f'{FOTOS}/post/{nombre}', *POST)
    recorta(ruta, f'{FOTOS}/historia/{nombre}', *HISTORIA)
    creditos[nombre] = {'lic': lic, 'titulo': titulo}
    print(f'      OK  {len(datos)//1024} KB  →  post/ e historia/')
    return True

def main():
    creditos = json.load(open(f'{FOTOS}/creditos.json'))
    solo_rehacer = '--rehacer' in sys.argv

    # 1. Las tres de post/ que se quedaron en 980x380 (trampa documentada, nunca
    #    arreglada). Se rehacen DESDE EL ORIGINAL, que es la única forma permitida.
    rotas = [('alhambra', 'f-alhambra.jpg'), ('oia', 'f-oia.jpg'), ('porto', 'f-porto.jpg')]
    print('Rehaciendo las tres postales de 980x380 desde su original:')
    for clave, nombre in rotas:
        titulo = creditos[nombre]['titulo']
        print(f'  {nombre}  ({titulo})')
        lic = licencia_verificada(titulo)
        if not lic:
            print('      licencia NO verificable: se deja como está'); continue
        incorpora(clave, titulo, lic, creditos)
        time.sleep(1)

    # 2. Fotos nuevas.
    if not solo_rehacer:
        print('\nBuscando fotos nuevas:')
        ya = {v['titulo'] for v in creditos.values()}
        for clave, consulta in BUSQUEDAS:
            if f'f-{clave}.jpg' in creditos: continue
            print(f'  {clave:14} «{consulta}»')
            for c in candidatas(consulta):
                titulo, lic = ficha(c['landing'])
                if not titulo or titulo in ya: time.sleep(0.4); continue
                if not lic:
                    print(f'      descartada (no CC0/PD): {titulo[:62]}')
                    time.sleep(0.4); continue
                print(f'      {lic}: {titulo[:65]}  [{c["w"]}x{c["h"]}]')
                if incorpora(clave, titulo, lic, creditos):
                    ya.add(titulo); break
                time.sleep(0.4)
            time.sleep(1)

    json.dump(dict(sorted(creditos.items())), open(f'{FOTOS}/creditos.json', 'w'),
              indent=2, ensure_ascii=False)
    print(f'\ncreditos.json: {len(creditos)} fotos')

if __name__ == '__main__':
    main()
