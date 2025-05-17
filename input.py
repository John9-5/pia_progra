import re

def entrada_gasto(str_gasto):
    '''Esta funcion recine un string y valida si se puede 
    convertir a un entero, en caso de que no, solicita un
    nuevp numero'''
    try:
        flt_gasto = float(str_gasto)
    except ValueError:
        nuevo_str_gasto = input("Ingrese un gasto valido")
        entrada_gasto(nuevo_str_gasto)
    else:
        return flt_gasto
    
def entrada_fecha(str_fecha):
    patron = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"
    patron_fecha = re.compile(patron)
    if patron_fecha.search(str_fecha):
        return str_fecha
    else:
        nueva_fecha = input("Fecha inválida, intente de nuevo: ")
        entrada_fecha(nueva_fecha)
    
fecha = input("Fecha prueba")
entrada_fecha(fecha)
    


def entrada_categoria(str_categoria):
    pass