#!/bin/bash
# La cadena entera, en orden: prepara salida/, escribe todas las piezas y construye el
# taller. Es lo que hay que ejecutar antes de sembrar el lienzo, porque el constructor
# del taller COPIA las piezas que los generadores hayan escrito y falla si falta una.
# No exporta PNG ni monta mp4: eso es `exportar-*.mjs` y `montar-*.sh`, cuando toque.
set -e
R="$(cd "$(dirname "$0")/.." && pwd)"
bash "$R/piezas/preparar.sh"
cd "$R/salida"
python3 ../piezas/destacadas/gen-destacadas.py
python3 ../piezas/destacadas/gen-destacadas.py it
python3 ../piezas/reels/gen-reel.py
python3 ../piezas/reels/gen-reel-it.py
python3 ../piezas/reels/gen-reel-grupo.py
cd "$R" && python3 piezas/taller/construir-taller.py
echo "todo en salida/ ($(ls "$R/salida"/*.dc.html | wc -l) piezas, $(ls "$R/salida/taller"/*.dc.html | wc -l) artboards del taller)"
