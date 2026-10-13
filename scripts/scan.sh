#!/usr/bin/env bash
set -e

echo "[*] Iniciando proceso de recolección para gob.mx..."
mkdir -p data

# Ejecutar Subfinder
echo "[*] Consultando fuentes pasivas con Subfinder..."
subfinder -d gob.mx -silent -o data/subdominios.txt

# Ejecutar Httpx verificando que el archivo temporal exista y no esté vacío
if [ -s data/subdominios.txt ]; then
    echo "[*] Validando servidores activos con Httpx..."
    httpx -l data/subdominios.txt -silent -o data/dominios_activos.txt
else
    echo "[!] Error: Subfinder no generó resultados o el archivo está vacío."
    exit 1
fi

# Actualizar el README.md automáticamente
echo "[*] Actualizando estadísticas en README.md..."
python3 scripts/update_readme.py

echo "[*] ¡Proceso finalizado con éxito!"
