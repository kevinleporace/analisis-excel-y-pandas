# Análisis de Saldos con Pandas

Este proyecto permite analizar datos financieros desde un archivo Excel usando Python y pandas.  
Entre las funcionalidades actuales:

- Cálculo del total de saldos pendientes
- Filtrado de proveedores con saldo
- Exportación a CSV
- Visualización de saldos por contacto comercial

## Requisitos
- Python 3.10+
- pandas

## Ejecución
Ubicarse en la raíz del proyecto y ejecutar:

```bash
python analisis_saldos.py



## 🔍 Buscar clientes por fecha de compra

Se agregó una función que permite ingresar una fecha específica (en formato `dd/mm/aaaa`) y muestra:

- La cantidad de clientes que realizaron una compra ese día.
- Los nombres de esos clientes.
- La fecha de última compra de cada uno (para confirmar coincidencias).

Ejemplo de uso:

```python
fecha = '04/09/2018'
datos_cliente_por_fecha_compra(fecha, df['Fecha de última compra'])
python buscar_por_fecha.py
