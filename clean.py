import pandas as pd

def Clean_data(archivo):
    try:
        df = pd.read_csv(archivo, encoding="UTF-8")
        
        df.drop_duplicates(inplace=True)
        df.dropna(inplace=True)
 
    except Exception as e:
        print(f'Error: {e}')
        
    if df is not None:
        # Guardar el DataFrame limpio en un archivo CSV
        df.to_csv("new_data_cleaned.csv", index=False)
        