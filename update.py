import pandas as pd
from backup import Segurity_copy
# from clean import Clean_data
import csv

def reemplazar_valores(datos_destino, excel_productos, arch_destino, arch_origen):

    #FUNCION PARA CREAR COPIA DE SEGURIDAD y LE PASO EL NOMBRE QUE QUIERO QUE LA COPIA TENGA
    Segurity_copy(arch_destino, "copia_de_seguridad_EXCEL_pruductos")
    Segurity_copy(arch_origen, "copia_de_seguridad_EXCEL_nuevos_precios")
    
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


    df_csv_productos = pd.read_csv(arch_destino)

        # Guardar el DataFrame en un archivo Excel
    df_csv_productos.to_excel(excel_productos, index=False)
