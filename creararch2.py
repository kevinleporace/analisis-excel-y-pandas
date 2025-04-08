import pandas as pd

ruta='excels/lista_practica.xlsx'
df=pd.read_excel(ruta)


def datos_cliente_por_fecha_compra(fecha, df):
    fecha = pd.to_datetime(fecha, dayfirst=True)  # Convertís la fecha recibida
    df['Fecha de última compra'] = pd.to_datetime(df['Fecha de última compra'], dayfirst=True)  # Convertís la columna de fechas

    # Filtrás el DataFrame completo con las filas que coincidan con la fecha
    coincidencias = df[df['Fecha de última compra'] == fecha]

    cantidad = len(coincidencias)
    print(f"Cantidad de compras en esa fecha: {cantidad}")
    
    # Mostrás nombres y fechas de compra
    if not coincidencias.empty:
        print("Clientes que compraron ese día:")
        print(coincidencias[['Contacto comercial', 'Fecha de última compra']])
    else:
        print("No hubo compras en esa fecha.")


#el excel tiene solo esa columna de fecha: Fecha de última compra'

fecha='10/01/2021'
datos_cliente_por_fecha_compra(fecha,df)