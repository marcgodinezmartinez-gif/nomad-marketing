#!/bin/bash
# El motor y lo común se editan en incluye-pago/ y se copian a incluye-dia/.
set -e
D="$(cd "$(dirname "$0")" && pwd)"
cp "$D/assets/motor.js" "$D/../incluye-dia/assets/motor.js"
cp "$D/cortar-tomas.py" "$D/../incluye-dia/cortar-tomas.py"
