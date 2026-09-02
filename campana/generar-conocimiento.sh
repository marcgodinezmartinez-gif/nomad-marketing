#!/bin/bash
# Regenera campana/PROYECTO-CONOCIMIENTO.md — los seis documentos que se le suben al
# Proyecto de claude.ai, uno detrás de otro.
#
# Existe porque hasta el 2-sep esa copia se montaba A MANO, y una copia a mano de una
# tabla que vive en cuatro sitios se desfasa sola. El día que la tabla de parada cambió
# —la fila de «hay clics y no hay altas»— había que acordarse de tocar cinco ficheros.
# Ahora se tocan las fuentes y se ejecuta esto.
#
# El repo manda; PROYECTO-CONOCIMIENTO.md es una copia y se regenera, no se edita.
# Uso: bash campana/generar-conocimiento.sh
set -e
R="$(cd "$(dirname "$0")/.." && pwd)"
DESTINO="$R/campana/PROYECTO-CONOCIMIENTO.md"

# El orden es el de campana/PROYECTO-CLAUDE.md §«Conocimiento del Proyecto». No se
# reordena sin cambiar también ese documento.
FICHEROS=(
  "AGENTS.md"
  "campana/LANZAMIENTO-PUBLICIDAD.md"
  "campana/PLAN-INSTAGRAM.md"
  "campana/INSTAGRAM-ARRANQUE.md"
  "piezas/destacadas/README.md"
  "campana/MERCADO-2026-08-15.md"
)

python3 - "$R" "$DESTINO" "${FICHEROS[@]}" <<'PY'
import sys
raiz, destino, ficheros = sys.argv[1], sys.argv[2], sys.argv[3:]
partes = ['# Conocimiento del Proyecto «NOMAD · marketing»\n\nGenerado desde el repo '
          '`nomad-marketing` por `campana/generar-conocimiento.sh` '
          '(`campana/PROYECTO-CLAUDE.md` dice qué es y cuándo se sube). Seis documentos, '
          'uno detrás de otro. **El repo manda; esto es una copia: se regenera, no se '
          'edita.**']
for f in ficheros:
    cuerpo = open(f'{raiz}/{f}').read().rstrip('\n')
    partes.append(f'<!-- {f} -->\n\n{cuerpo}')
open(destino, 'w').write('\n\n\n---\n\n'.join(partes) + '\n')
print(f'  PROYECTO-CONOCIMIENTO.md — {len(ficheros)} documentos, '
      f'{sum(1 for _ in open(destino))} líneas')
PY
