import csv
from excel_a_csv import convertir_excel_a_csv
import pandas as pd

#EXCEL
excel_new_price = 'excel\\excel_nuevos_precios.xlsx'
excel_productos = 'excel\\excel_productos.xlsx'

#CSV
csv_new_price = 'nuevos_precios.csv'
mis_productos = 'mis_productos.csv'



datos_destino = {}

# Leer los datos del archivo destino en un diccionario

def reemplazar_valores(arch_destino, arch_origen):
    
    #CONVIERTO LOS EXCEL EN ARCHIVOS CSV QUE PUEDO MANIPULAR
    convertir_excel_a_csv(excel_new_price, csv_new_price)
    
    convertir_excel_a_csv(excel_productos, mis_productos)
    # Abrir los archivos CSV en modo lectura y escritura
    with open(arch_destino, 'r') as f_destino:
        lector_destino = csv.DictReader(f_destino)
        for fila in lector_destino:
            datos_destino[fila['Producto']] = fila['Precio']

    # Leer los datos del archivo origen y actualizar el diccionario si el producto coincide
    with open(arch_origen, 'r') as f_origen:
        lector_origen = csv.DictReader(f_origen)
        for fila in lector_origen:
            producto = fila['Producto']
            precio = fila['Precio']
            if producto in datos_destino:
                datos_destino[producto] = precio

    # Escribir los datos actualizados en el archivo destino
    with open(arch_destino, 'w', newline='') as f_destino:
        campos = ['Producto', 'Precio']  # Cambia los productos de las columnas según tu estructura
        escritor_destino = csv.DictWriter(f_destino, fieldnames=campos)
        escritor_destino.writeheader()
        for producto, precio in datos_destino.items():
            escritor_destino.writerow({'Producto': producto, 'Precio': precio})  # Cambia los valores de las columnas según tu estructura


    df_csv_productos = pd.read_csv(mis_productos)

        # Guardar el DataFrame en un archivo Excel
    df_csv_productos.to_excel(excel_productos, index=False)



reemplazar_valores("mis_productos.csv", "nuevos_precios.csv")

