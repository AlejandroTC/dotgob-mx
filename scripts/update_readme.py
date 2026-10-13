import datetime
import os

def update_readme():
    subdomains_path = "data/subdominios.txt"
    active_path = "data/dominios_activos.txt"

    # Contar líneas
    total_sub = sum(1 for line in open(subdomains_path, encoding="utf-8")) if os.path.exists(subdomains_path) else 0
    total_active = sum(1 for line in open(active_path, encoding="utf-8")) if os.path.exists(active_path) else 0

    # Obtener fecha en formato DD/MM/YYYY
    current_date = datetime.datetime.now().strftime("%d/%m/%Y")

    # Formatear números
    total_sub_str = f"{total_sub:,}"
    total_active_str = f"{total_active:,}"

    new_stats = f"""- **Fecha de corte:** {current_date}

- **Subdominios totales encontrados (Subfinder):** {total_sub_str}

- **Dominios activos comprobados (HTTPx):** {total_active_str}"""

    readme_path = "README.md"
    if not os.path.exists(readme_path):
        print("[!] No se encontró el archivo README.md")
        return

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    start_marker = "<!-- STATS:START -->"
    end_marker = "<!-- STATS:END -->"

    if start_marker in content and end_marker in content:
        start_idx = content.find(start_marker) + len(start_marker)
        end_idx = content.find(end_marker)

        # Reemplazar el contenido
        updated_content = content[:start_idx] + "\n" + new_stats + "\n" + content[end_idx:]

        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(updated_content)

        print("[*] ¡README.md actualizado exitosamente con las nuevas estadísticas!")
    else:
        print("[!] Error: No se encontraron los marcadores de estadísticas en el README.md")

if __name__ == "__main__":
    update_readme()
