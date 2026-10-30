# Escribe en index.html, entre las marcas «ICONOS: desde iconos/editorial.json», los datos de los dibujos de
# la derecha (el juego «editorial» que eligió el dueño el 30-oct: 5 px la línea, 3 px los detalles). Los
# trazos principales van por escena; los detalles, como [etiqueta, atributos, texto]. Los saca de
# iconos/editorial.json, que es lo que entregó el diseñador y revisó la dirección de arte (sus capturas, en
# iconos/editorial-hoja.png). No se tocan a mano: se cambia el JSON y se vuelve a correr esto.
# Uso: python3 -I iconos/datos.py
import json, os, re
AQUI = os.path.dirname(os.path.abspath(__file__))
j = json.load(open(os.path.join(AQUI, 'editorial.json'), encoding='utf-8'))['escenas']
def el(e):
    a = {k: v for k, v in e['attrs'].items()}
    return [e['tag'], a] + ([e['texto']] if 'texto' in e else [])
def rol(lista, *roles): return [el(e) for e in lista if e.get('rol') in roles]
def segs(p): return [[s['o'], s['marca']] for s in p['segmentos']]
s3, s4, s5, s6, s7, s8, s9, s11 = (j[k] for k in ('s3', 's4', 's5', 's6', 's7', 's8', 's9', 's11'))
D = {
  's2': {'segs': segs(j['s2']['principal'])},
  's3': {'d': s3['principal']['d'], 'hoja': rol(s3['detalles'], 'anilla', 'cabecera'),
         'dias': [{'id': d['id'], 'o': d['centro_brote'], 'el': [el(e) for e in d['elementos']]} for d in s3['dias']]},
  's4': {'segs': segs(s4['principal']), 'paradas': [{'c': p['centro'], 'el': [el(e) for e in p['elementos']]} for p in s4['paradas']],
         'horas_x': s4['layout']['horas']['left'], 'puntos': [e for e in s4['punteado']['svg'] if e['tag'] == 'path'][0]['attrs']['stroke-dasharray'],
         'mascara': [e for e in s4['punteado']['svg'] if e['tag'] == 'mask'][0]['hijo']['attrs']['stroke-width']},
  's5': {'d': s5['principal']['d'], 'det': rol(s5['detalles'], 'almohadilla', 'acolchado'), 'ondas': rol(s5['detalles'], 'onda')},
  's6': {'d': s6['principal']['d'], 'lente': rol(s6['detalles'], 'lente', 'brillo'), 'det': rol(s6['detalles'], 'disparador', 'flash', 'piloto')},
  's7': {'d': s7['principal']['d'], 'cara': rol(s7['detalles'], 'visera', 'ojo', 'sonrisa'), 'antena': rol(s7['detalles'], 'bola', 'señal')},
  's8': {'d': s8['principal']['d'], 'det': rol(s8['detalles'], 'reparto')},
  's9': {'d': s9['principal']['d'], 'ojo': rol(s9['detalles'], 'ojo'), 'suelo': rol(s9['detalles'], 'suelo')},
  's11': {'d': s11['principal']['d'], 'estela': rol(s11['detalles'], 'estela')},
}
# La persona (S8 y S10-S11): hombros y cabeza, relativos a (x, base).
p = j['s8']['layout']['persona']
D['persona'] = {'r': p['r_cabeza'], 'sobre': p['cabeza_sobre_base'], 'hombros': 'M-36,0 L-36,-12 C-36,-36 -21.6,-46 0,-46 C21.6,-46 36,-36 36,-12 L36,0',
                'x8': j['s8']['layout']['personas_x'], 'base8': j['s8']['layout']['base_y'], 'base10': j['s10']['layout']['base_y']}
assert D['persona']['hombros'] in j['s8']['layout']['persona_svg'], 'la forma de los hombros ya no es la del JSON'
INDEX = os.path.join(AQUI, '..', 'index.html')
h = open(INDEX, encoding='utf-8').read()
linea = '        var ICONOS = ' + json.dumps(D, ensure_ascii=False, separators=(',', ':')) + ';'
h2, n = re.subn(r'(        // ICONOS: desde iconos/editorial\.json \(iconos/datos\.py\)\.\n).*?\n', lambda m: m.group(1) + linea + '\n', h, count=1, flags=re.S)
assert n == 1, 'no encuentro la marca de ICONOS en index.html'
open(INDEX, 'w', encoding='utf-8').write(h2)
print('ICONOS escrito:', len(linea), 'caracteres')
