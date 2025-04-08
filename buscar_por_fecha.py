import pandas as pd


ruta='excels/lista_practica.xlsx'
df=pd.read_excel(ruta)


'''suma total de  los saldos pendientes'''
total_saldo_pendiente=df['Saldo pendiente'].sum()
print(total_saldo_pendiente)

print(df.head())

'''Crear un nuevo archivo Excel o CSV 
que contenga solo los proveedores con saldo pendiente, 
ordenados de mayor a menor.'''

# Filtrar solo las columnas que interesan
print('---------------------------')
df_filtrado = df[['Proveedor', 'Saldo pendiente']]
resultado = df_filtrado.groupby('Proveedor').sum()
resultado_ordenado=resultado.sort_values('Saldo pendiente', ascending=False)

resultado_ordenado.to_csv('archs_csv/proveedores_con_saldo.csv')

def verSaldosSegunContacto(df):
    saldos = pd.Series(df['Saldo pendiente'].values, index=df['Contacto comercial'])
    print(saldos)

verSaldosSegunContacto(df)