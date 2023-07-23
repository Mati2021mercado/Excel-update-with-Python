import pandas as pd

def Convertir_excel_a_csv(ruta_excel, ruta_csv):
    try:
        # Leer el archivo Excel en un DataFrame
        df = pd.read_excel(ruta_excel)

        # Guardar el DataFrame en un archivo CSV
        df.to_csv(ruta_csv, index=False, encoding='utf-8')

        print(f'Archivo CSV guardado en: {ruta_csv}')

    except Exception as e:
        print(f'Error al convertir el archivo Excel a CSV: {e}')

# Rutas de los archivos (ajusta estas rutas según tu caso)





