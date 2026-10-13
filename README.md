# Infraestructura Digital de gob.mx

> [!NOTE]
> Este repositorio y su autor **no están afiliados, respaldados ni vinculados** de ninguna forma con el Gobierno de México.

---

## ¿Por qué este proyecto?

Las páginas web del Gobierno de México se agrupan bajo el dominio principal [gob.mx](https://www.gob.mx/). Sin embargo, debido a la descentralización administrativa, cada secretaría, estado, municipio y entidad pública genera y gestiona de manera independiente sus propios subdominios (`*.gob.mx`). 

Actualmente, no existe un directorio oficial, centralizado y unificado que mapee la totalidad de estos activos digitales.

---

## Metodología y Herramientas

El proceso de descubrimiento y filtrado consta de dos etapas:

1. **Enumeración Pasiva:** Se utiliza [**Subfinder**](https://github.com/projectdiscovery/subfinder) mediante registros de transparencia de certificados para extraer los dominios históricos.
2. **Filtrado:** Debido a que muchas entradas corresponden a certificados antiguos o endpoints inactivos, se procesa la lista con [**HTTPx**](https://github.com/projectdiscovery/httpx) para conservar únicamente los servicios web reales que responden peticiones HTTP/HTTPS.

---

## Github Action

Para mantener los datos actualizados este repositorio se actualiza automaticamente.

* **Frecuencia:** El flujo se ejecuta de manera automática el **primer día de cada mes**.

---
## Estado Actual y Limitaciones

Las fuentes pasivas no garantizan un mapeo del 100% de la infraestructura interna, pero ofrecen una visión muy amplia:

<!-- STATS:START -->
- **Fecha de corte:** 13/10/2026

- **Subdominios totales encontrados (Subfinder):** 14,950

- **Dominios activos comprobados (HTTPx):** 4,873
<!-- STATS:END -->

Los dominios activos, contienen portales web activos, infraestructura TI, correo, respuestas 403, 401, 5xx, configuracion inicial de servidores, errores de CDN, DNS y timeouts.

---

## Contribuciones y Política de IA

¡Las contribuciones para mejorar la precisión de la recolección, optimizar scripts o proponer mejoras son bienvenidas!

> [!IMPORTANT]
> Aunque no estoy en contra del uso de la IA, **no se aceptarán Pull Requests generados automáticamente por agentes o de forma 100% automatizada por IA**. Si deseas aportar mejoras al respositorio, asegúrate de revisarlas, entenderlas y justificarlas tú mismo.

Si tienes nuevas ideas para automatizar o refinar la obtención de subdominios, siéntete libre de abrir un *Issue* o enviar un PR.
