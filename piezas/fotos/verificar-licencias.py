# VERIFICA LA LICENCIA DE CADA FOTO DEL BANCO CONTRA COMMONS (6-sep).
#
# POR QUÉ EXISTE: el detector de `ampliar-banco.py` estaba ROTO y daba CC0 a todo. Buscaba
# la cadena «Creative Commons CC0» en el HTML de la página del fichero, y esa cadena
# aparece DOS VECES EN EL PIE DE CUALQUIER PÁGINA de Commons — es la licencia del propio
# sitio y una mención a CC0, no la del fichero. Medido el 6-sep: la página de
# `File:Plaça del Diamant.JPG`, que es GFDL + CC BY-SA 3.0, también la contiene.
#
# Es exactamente la trampa que AGENTS.md ya avisaba —«un grep encuentra la cadena también
# en los comentarios; se sonda el endpoint, no el fichero que lo llama»— aplicada a sí
# misma, y por eso el crédito de las 19 fotos del banco estaba SIN VERIFICAR de verdad.
#
# EL DISCRIMINADOR QUE SÍ VALE: la URL del *deed* (`.../deed.en`) sólo aparece dentro de
# la plantilla de licencia del fichero; el pie del sitio enlaza la licencia sin `deed`.
# Comprobado en dos ficheros de licencia conocida y opuesta, y el script SE NIEGA A
# CORRER si el control no distingue los dos (una aserción se rompe a propósito antes de
# fiarse de ella).
#
# LAS DE UNSPLASH Y PEXELS (regla ampliada el 6-sep) NO SE COMPRUEBAN DESDE AQUÍ: sus
# licencias no llevan deed de Creative Commons, y unsplash.com no sirve la página a un
# script (un muro anti-bot devuelve 401). Se verifican a mano en la página de la foto —«Free
# to use under the Unsplash License» / «Free to use» en Pexels— y se anota la fecha en
# `verificada`. El script las lista con su página para que se pueda repetir la comprobación.
#
# Uso:  python3 piezas/fotos/verificar-licencias.py
import json, os, re, sys, time, urllib.parse, urllib.request

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
UA = 'NOMAD-marketing/1.0 (https://travelsnomad.com; contacto via GitHub)'
PAUSA = 6                                   # Commons limita por ritmo; sin esto, 429

def pide(url, intentos=4):
    for n in range(intentos):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read().decode('utf-8', 'replace')
        except Exception:
            if n == intentos - 1: return None
            time.sleep(PAUSA * (n + 1))

# El deed que declara la plantilla del fichero. El orden importa: se devuelve el primero
# que aparezca de los permisivos, y si hay alguno restrictivo se informa igual.
DEEDS = [
    (r'creativecommons\.org/publicdomain/zero/1\.0/deed',   'CC0',           True),
    (r'creativecommons\.org/publicdomain/mark/1\.0/deed',   'PD Mark',       True),
    (r'creativecommons\.org/licenses/by-sa/([0-9.]+)/deed', 'CC BY-SA {}',   False),
    (r'creativecommons\.org/licenses/by/([0-9.]+)/deed',    'CC BY {}',      False),
]

def licencia(titulo):
    """(lista de licencias declaradas, ¿todas permiten uso sin atribución?)."""
    slug = urllib.parse.quote(titulo.replace(' ', '_'), safe=':/')
    h = pide(f'https://commons.wikimedia.org/wiki/{slug}')
    if not h: return None, None
    encontradas, libres = [], []
    for pat, nombre, sin_atribucion in DEEDS:
        m = re.search(pat, h)
        if m:
            encontradas.append(nombre.format(*m.groups()) if m.groups() else nombre)
            libres.append(sin_atribucion)
    # El dominio público por antigüedad no lleva deed de Creative Commons.
    if not encontradas and re.search(r'PD-old|PD-self|PD-US|public domain because', h, re.I):
        encontradas, libres = ['Dominio público'], [True]
    return encontradas, (bool(libres) and any(libres))

def control():
    """Se rompe a propósito: si el detector no separa estos dos, no vale y se para."""
    casos = [('File:Colosseum of Rome, Italy.jpg', True),      # CC0 de verdad
             ('File:Plaça del Diamant.JPG',        False)]     # GFDL + CC BY-SA 3.0
    for titulo, esperado in casos:
        lics, libre = licencia(titulo)
        print(f'  control  {titulo[:44]:46} → {lics} (libre={libre})')
        if libre != esperado:
            sys.exit(f'\nEL CONTROL FALLA: se esperaba libre={esperado}. '
                     'El detector no vale; no se audita nada con él.')
        time.sleep(PAUSA)
    print('  control OK: el detector distingue los dos casos\n')

def main():
    print('Control del detector:')
    control()
    ruta = f'{RAIZ}/banco/fotos/creditos.json'
    cred = json.load(open(ruta))
    print(f'Auditando {len(cred)} fotos del banco:')
    sospechosas = []
    for nombre, v in sorted(cred.items()):
        if v.get('fuente') in ('unsplash', 'pexels'):
            print(f'  OK  {nombre:18} «{v["lic"]}», verificada a mano el {v.get("verificada", "?")}: {v["url"]}')
            continue
        lics, libre = licencia(v['titulo'])
        marca = 'OK ' if libre else '>>>'
        print(f'  {marca} {nombre:18} dice «{v["lic"]}» → Commons dice {lics}')
        if not libre: sospechosas.append((nombre, lics))
        elif lics: v['lic'] = lics[0]           # se guarda la real, no la supuesta
        time.sleep(PAUSA)
    json.dump(dict(sorted(cred.items())), open(ruta, 'w'), indent=2, ensure_ascii=False)
    if sospechosas:
        print(f'\n{len(sospechosas)} NO cumplen la regla de la casa (CC0, dominio público, Unsplash o Pexels):')
        for n, l in sospechosas: print(f'  {n}: {l}')
        print('\nHay que sustituirlas o cambiar la regla a conciencia. No se borran solas.')
    else:
        print('\nLas ' + str(len(cred)) + ' cumplen la regla de la casa: CC0, dominio público, Unsplash o Pexels.')

if __name__ == '__main__':
    main()
