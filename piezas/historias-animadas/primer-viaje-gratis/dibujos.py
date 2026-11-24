# Los dibujos de la derecha, los del molde de «Así funciona» y «Pruébalo» (el juego «editorial» que eligió
# el dueño el 30-oct: 5 px la línea, 3 px los detalles). Salen de ../puente-viena/iconos/editorial.json, que
# es lo que entregó el diseñador y revisó la dirección de arte; aquí no se dibuja nada nuevo.
# Escribe assets/dibujos.js. Uso: python3 -I dibujos.py
import json, os
AQUI = os.path.dirname(os.path.abspath(__file__))
E = json.load(open(os.path.join(AQUI, '..', 'puente-viena', 'iconos', 'editorial.json'), encoding='utf-8'))['escenas']
def el(e): return [e['tag'], dict(e['attrs'])] + ([e['texto']] if 'texto' in e else [])
def rol(lista, *roles): return [el(e) for e in lista if e.get('rol') in roles]
s5, s9, cu = E['s5'], E['s9'], E['cuadro']
D = {
    'casco': {'d': s5['principal']['d'], 'det': rol(s5['detalles'], 'almohadilla', 'acolchado'), 'ondas': rol(s5['detalles'], 'onda'),
              'o': s5['layout']['origen_latido']},
    'pin': {'d': s9['principal']['d'], 'ojo': rol(s9['detalles'], 'ojo'), 'suelo': rol(s9['detalles'], 'suelo'),
            'o': s9['layout']['ojo_centro']},
    'cuadro': {'d': cu['principal']['d'], 'det': rol(cu['detalles'], 'alambre', 'clavo', 'paspartu', 'montes'), 'sol': rol(cu['detalles'], 'sol'),
               'o': cu['layout']['origen_sol']},
}
for k, v in D.items():
    print(k, {kk: (len(vv) if isinstance(vv, list) else '…') for kk, vv in v.items()})
open(os.path.join(AQUI, 'assets', 'dibujos.js'), 'w', encoding='utf-8').write(
    '// Lo escribe dibujos.py desde ../puente-viena/iconos/editorial.json. No se edita a mano.\nwindow.DIBUJOS = '
    + json.dumps(D, ensure_ascii=False, separators=(',', ':')) + ';\n')
