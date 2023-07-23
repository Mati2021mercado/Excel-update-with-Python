from update import reemplazar_valores
from excel_a_csv import Convertir_excel_a_csv


#EXCEL
excel_new_price = 'excel\\excel_nuevos_precios.xlsx'
excel_productos = 'excel\\excel_productos.xlsx'

#CSV
csv_new_price = 'nuevos_precios.csv'
csv_mis_productos = 'mis_productos.csv'

#CONVIERTO LOS EXCEL EN ARCHIVOS CSV QUE PUEDO MANIPULAR
Convertir_excel_a_csv(excel_new_price, csv_new_price)
Convertir_excel_a_csv(excel_productos, csv_mis_productos)
    
datos_destino = {}

reemplazar_valores(datos_destino, excel_productos, csv_mis_productos, csv_new_price)

