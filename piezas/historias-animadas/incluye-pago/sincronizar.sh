#!/bin/bash
# El motor y lo común se editan en incluye-pago/ y se copian a incluye-dia/.
D="$(cd "$(dirname "$0")" && pwd)"
cp "$D/assets/motor.js" "$D/cortar-tomas.py" "$D/../incluye-dia/assets/" 2>/dev/null
mv "$D/../incluye-dia/assets/cortar-tomas.py" "$D/../incluye-dia/cortar-tomas.py"
