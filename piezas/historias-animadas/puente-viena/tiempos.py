# Los cortes del vídeo salen de la voz (como en «Así funciona»): cada frase empieza un hueco después de
# que acabe la anterior, y cada foto entra con la palabra que la nombra. Lee voz.json (la duración de
# cada toma y dónde cae cada palabra, a 1×; lo dijo faster-whisper) y escribe assets/tiempos.js, que es
# lo único que lee index.html, e imprime dónde empieza cada frase para mezclar.sh.
import json, os
aqui = os.path.dirname(os.path.abspath(__file__))
v = json.load(open(f'{aqui}/voz.json', encoding='utf-8'))
VEL, HUECO = v['velocidad'], v['hueco']
f = {x['id']: x for x in v['frases']}
emp, t = {}, 0.25
for x in v['frases']:
    emp[x['id']] = round(t, 3); t += x['dura'] / VEL + HUECO
def en(frase, palabra, antes=0.0):
    return round(emp[frase] + f[frase]['palabras'][palabra] / VEL - antes, 3)
T = {
    'respira':     round(emp['v2'] - 0.20, 3),
    'viena':       en('v2', 'Viena', 0.10),
    'montada':     en('v2', 'Ya'),
    'dia1':        round(emp['v3'] - 0.25, 3),
    'catedral':    en('v3', 'la', 0.08),
    'mercadillo1': en('v3', 'Con'),
    'dia2':        round(emp['v4'] - 0.25, 3),
    'museo':       en('v4', 'y', 0.05),
    'mercadillo2': en('v4', 'Con'),
    'dia3':        round(emp['v5'] - 0.25, 3),
    'schonbrunn':  en('v5', 'Schönbrunn'),
    'belvedere':   en('v5', 'Belvedere', 0.10),
    'karlsplatz':  en('v5', 'Karlsplatz', 0.12),
    'lostres':     en('v5', 'los'),
    'app':         round(emp['v6'] - 0.25, 3),
    'copias':      en('v6', 'lo'),
    'cierre':      round(emp['v7'] - 0.25, 3),
    'quenadie':    en('v7', 'que'),
}
fin = emp['v7'] + f['v7']['dura'] / VEL + 1.10
T['fin'] = round(round(fin * 30) / 30, 4)          # fotogramas enteros a 30 fps
open(f'{aqui}/assets/tiempos.js', 'w').write('// Lo escribe tiempos.py desde voz.json. No se toca a mano.\nwindow.TIEMPOS = ' + json.dumps(T) + ';\n')
print('TIEMPOS', json.dumps(T))
print('EMPIEZA', ' '.join(str(emp[x['id']]) for x in v['frases']))
print('DURACION', T['fin'], 'FOTOGRAMAS', round(T['fin'] * 30))
