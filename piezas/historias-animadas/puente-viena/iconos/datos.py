# Escribe en index.html, entre las marcas «ICONOS: desde iconos/editorial.json», los datos de los dibujos de
# la derecha de «El puente, ya organizado». Es el datos.py de asi-funciona/ con los dibujos que usa este
# vídeo, todos del juego «editorial» que eligió el dueño el 30-oct (5 px la línea y 3 px los detalles): el
# pin (S2), el calendario de una fila con los tres días del viaje (S3, el de pruebalo/ con DIC 2026 y el
# sábado 5, el domingo 6 y el lunes 7), los planes del sábado unidos por una curva (S4), los auriculares
# (S5) y el robot (S6). editorial.json es el de pruebalo/ con el calendario cambiado.
# No se tocan a mano: se cambia el JSON y se vuelve a correr esto.
# Uso: python3 -I iconos/datos.py
import json, os, re
AQUI = os.path.dirname(os.path.abspath(__file__))
j = json.load(open(os.path.join(AQUI, 'editorial.json'), encoding='utf-8'))['escenas']
def el(e):
    a = {k: v for k, v in e['attrs'].items()}
    return [e['tag'], a] + ([e['texto']] if 'texto' in e else [])
def rol(lista, *roles): return [el(e) for e in lista if e.get('rol') in roles]
def segs(p): return [[s['o'], s['marca']] for s in p['segmentos']]
s3, s4, s5, s7, s9 = (j[k] for k in ('s3', 's4', 's5', 's7', 's9'))
D = {
  'pin': {'d': s9['principal']['d'], 'ojo': rol(s9['detalles'], 'ojo'), 'suelo': rol(s9['detalles'], 'suelo')},
  'cal': {'d': s3['principal']['d'], 'hoja': rol(s3['detalles'], 'anilla', 'cabecera'),
          'dias': [{'id': d['id'], 'o': d['centro_brote'], 'el': [el(e) for e in d['elementos']]} for d in s3['dias']]},
  'plan': {'segs': segs(s4['principal']), 'paradas': [{'c': p['centro'], 'el': [el(e) for e in p['elementos']]} for p in s4['paradas']],
           'horas_x': s4['layout']['horas']['left'], 'puntos': [e for e in s4['punteado']['svg'] if e['tag'] == 'path'][0]['attrs']['stroke-dasharray'],
           'mascara': [e for e in s4['punteado']['svg'] if e['tag'] == 'mask'][0]['hijo']['attrs']['stroke-width']},
  'casco': {'d': s5['principal']['d'], 'det': rol(s5['detalles'], 'almohadilla', 'acolchado'), 'ondas': rol(s5['detalles'], 'onda')},
  'robot': {'d': s7['principal']['d'], 'cara': rol(s7['detalles'], 'visera', 'ojo', 'sonrisa'), 'antena': rol(s7['detalles'], 'bola', 'señal')},
}
assert [d['id'] for d in D['cal']['dias']] == ['dia5', 'dia6', 'dia7'], 'el calendario ya no es el del 5 al 7'
INDEX = os.path.join(AQUI, '..', 'index.html')
h = open(INDEX, encoding='utf-8').read()
linea = '        var ICONOS = ' + json.dumps(D, ensure_ascii=False, separators=(',', ':')) + ';'
h2, n = re.subn(r'(        // ICONOS: desde iconos/editorial\.json \(iconos/datos\.py\)\.\n).*?\n', lambda m: m.group(1) + linea + '\n', h, count=1, flags=re.S)
assert n == 1, 'no encuentro la marca de ICONOS en index.html'
open(INDEX, 'w', encoding='utf-8').write(h2)
print('ICONOS escrito:', len(linea), 'caracteres')
