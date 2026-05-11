#!/bin/bash
# Lokalny serwer matchujący zachowanie Vercel:
#   - auto-serwuje index.html z katalogów (np. /Dokumentacja/)
#   - linki kończące się slashem działają jak na proda
#
# Użycie:  ./serve.sh
# Otwórz:  http://localhost:8000/ → pełna pracownia, /Dokumentacja/, /hub.html itd.

cd "$(dirname "$0")"
PORT="${1:-8000}"
echo ""
echo "  Schooleo Pracownia · lokalny serwer"
echo "  http://localhost:$PORT/hub.html"
echo "  http://localhost:$PORT/Dokumentacja/"
echo ""
echo "  Ctrl+C żeby zatrzymać."
echo ""
python3 -m http.server "$PORT"
