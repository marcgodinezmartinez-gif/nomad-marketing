# Escribe en index.html, entre las marcas «ICONOS: desde iconos/editorial.json», los datos de los dibujos de
# la derecha de «Pruébalo antes de pagar». Es el datos.py de asi-funciona/ con los dibujos que usa este
# vídeo: el calendario (S3), los auriculares (S4), el cuadro con su marco (S5, nuevo el 7-nov, en el mismo
# juego «editorial»: 5 px la línea y 3 px los detalles), el robot (S6) y las personas con su línea (S7).
# editorial.json es el de asi-funciona/ con la escena «cuadro» añadida. No se tocan a mano: se cambia el
# JSON y se vuelve a correr esto.
# Uso: python3 -I iconos/datos.py
import json, os, re
AQUI = os.path.dirname(os.path.abspath(__file__))
j = json.load(open(os.path.join(AQUI, 'editorial.json'), encoding='utf-8'))['escenas']
def el(e):
    a = {k: v for k, v in e['attrs'].items()}
    return [e['tag'], a] + ([e['texto']] if 'texto' in e else [])
def rol(lista, *roles): return [el(e) for e in lista if e.get('rol') in roles]
s3, s5, s7, s8, cu = (j[k] for k in ('s3', 's5', 's7', 's8', 'cuadro'))
D = {
  'cal': {'d': s3['principal']['d'], 'hoja': rol(s3['detalles'], 'anilla', 'cabecera'),
          'dias': [{'id': d['id'], 'o': d['centro_brote'], 'el': [el(e) for e in d['elementos']]} for d in s3['dias']]},
  'casco': {'d': s5['principal']['d'], 'det': rol(s5['detalles'], 'almohadilla', 'acolchado'), 'ondas': rol(s5['detalles'], 'onda')},
  'cuadro': {'d': cu['principal']['d'], 'colgar': rol(cu['detalles'], 'alambre', 'clavo'),
             'obra': rol(cu['detalles'], 'paspartu', 'montes'), 'sol': rol(cu['detalles'], 'sol')},
  'robot': {'d': s7['principal']['d'], 'cara': rol(s7['detalles'], 'visera', 'ojo', 'sonrisa'), 'antena': rol(s7['detalles'], 'bola', 'señal')},
  # La línea de S7 es la del gasto de asi-funciona (sin las rayas de reparto: aquí no se reparte nada,
  # paga uno y es para todos), subida 32 px porque debajo no va ningún texto.
  'linea': s8['principal']['d'].replace(',840', ',808'),
}
p = j['s8']['layout']['persona']
D['persona'] = {'r': p['r_cabeza'], 'sobre': p['cabeza_sobre_base'], 'hombros': 'M-36,0 L-36,-12 C-36,-36 -21.6,-46 0,-46 C21.6,-46 36,-36 36,-12 L36,0',
                'x': j['s8']['layout']['personas_x'], 'base': j['s8']['layout']['base_y'] - 32}
assert D['persona']['hombros'] in j['s8']['layout']['persona_svg'], 'la forma de los hombros ya no es la del JSON'
assert D['linea'] != s8['principal']['d'], 'la línea del gasto ya no está en y = 840'
INDEX = os.path.join(AQUI, '..', 'index.html')
h = open(INDEX, encoding='utf-8').read()
linea = '        var ICONOS = ' + json.dumps(D, ensure_ascii=False, separators=(',', ':')) + ';'
h2, n = re.subn(r'(        // ICONOS: desde iconos/editorial\.json \(iconos/datos\.py\)\.\n).*?\n', lambda m: m.group(1) + linea + '\n', h, count=1, flags=re.S)
assert n == 1, 'no encuentro la marca de ICONOS en index.html'
open(INDEX, 'w', encoding='utf-8').write(h2)
print('ICONOS escrito:', len(linea), 'caracteres')
