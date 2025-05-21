
import os 
import pandas as pd 
"""Seccion hecha por Jose Luis Rodriguez Fuentes por si acaso"""

"""El resultado del registro de datos debe ser un diccionario de listas, 
cada categoria es una lista de datos"""

def guardar_en_csv(datos, nombre_archivo: str = "datos.csv") -> bool:
    
    directorio_actual = os.path.dirname(os.path.abspath(__file__))

    #crea la ruta completa de la carpeta y el archivo
    ruta = os.path.join(directorio_actual, nombre_archivo)
    
    #Comprueba que el tipo de dato de los datos a recibir sean un diccionario, para poder hacer el Dataframe
    try:
        df = pd.DataFrame(datos)
        print(df)  
    except Exception:
        print(" Error al convertir los datos a DataFrame")
        return False

    # Si el archivo ya existe (isfile), agregar sin encabezado
    try:
        if os.path.isfile(ruta):
            df.to_csv(ruta, mode='a', header=False, index=False)
        else:
            df.to_csv(ruta, mode='w', header=True, index=False)
        print(" Datos guardados correctamente.")
        return True
    except Exception:
        print("Error al guardar el archivo")
        return False

