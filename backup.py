import pandas as pd

def Segurity_copy(df,name):
        copia_de_seguridad = pd.read_csv(df,encoding="UTF-8")
        copia_de_seguridad = copia_de_seguridad.drop_duplicates()
        copia_de_seguridad.to_excel(f'excel\\{name}.xlsx', index=False)
