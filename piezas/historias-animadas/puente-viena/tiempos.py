# Los cortes del vídeo salen de la voz (como en «Así funciona»): cada frase empieza un hueco después de
# que acabe la anterior, y cada foto entra con la palabra que la nombra. Lee voz.json (la duración de
# cada toma, su hueco y dónde cae cada palabra, a 1×; lo dijo faster-whisper) y escribe assets/tiempos.js,
# que es lo único que lee index.html, e imprime dónde empieza cada frase para mezclar.sh.
import json, os
aqui = os.path.dirname(os.path.abspath(__file__))
v = json.load(open(f'{aqui}/voz.json', encoding='utf-8'))
VEL = v['velocidad']
f = {x['id']: x for x in v['frases']}
emp, t = {}, 0.25
for x in v['frases']:
    emp[x['id']] = round(t, 3); t += x['dura'] / VEL + x['hueco']
def en(frase, palabra, antes=0.0):
    return round(emp[frase] + f[frase]['palabras'][palabra] / VEL - antes, 3)
T = {
    'viena':    round(emp['v2'] - 0.20, 3),    # la respuesta: Viena, 3 días, ya organizada
    'dia1':     round(emp['v3'] - 0.25, 3),
    'catedral': en('v3', 'la', 0.08),
    'dia2':     round(emp['v4'] - 0.25, 3),
    'museo':    en('v4', 'y', 0.05),
    'd3a':      round(emp['v5'] - 0.25, 3),    # Schönbrunn
    'd3b':      round(emp['v6'] - 0.18, 3),    # Belvedere: entra en cuanto acaba la frase de Schönbrunn
    'd3c':      round(emp['v7'] - 0.04, 3),    # Karlsplatz
    'cierre':   round(emp['v8'] - 0.45, 3),    # la tarjeta de guardar
    'nomad':    en('v8', 'Nomad', 0.25),
    'mandaselo': en('v8', 'Mándaselo'),
}
fin = emp['v8'] + f['v8']['dura'] / VEL + 1.9      # la tarjeta se queda: es lo que se guarda
T['fin'] = round(round(fin * 30) / 30, 4)           # fotogramas enteros a 30 fps
open(f'{aqui}/assets/tiempos.js', 'w').write('// Lo escribe tiempos.py desde voz.json. No se toca a mano.\nwindow.TIEMPOS = ' + json.dumps(T) + ';\n')
print('TIEMPOS', json.dumps(T))
print('EMPIEZA', ' '.join(str(emp[x['id']]) for x in v['frases']))
print('DURACION', T['fin'], 'FOTOGRAMAS', round(T['fin'] * 30))
