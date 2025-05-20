def pedir_datos():
    '''Solicita al usuario los datos y devuelve un diccionario con fecha, monto y categoría'''
    fecha_input = input("Ingrese la fecha (dd/mm/aaaa): ")
    fecha = entrada_fecha(fecha_input)

    monto_input = input("Ingrese el monto (puede ser positivo o negativo): ")
    monto = entrada_gasto(monto_input)

    categoria_input = input("Ingrese la categoría: ")
    categoria = entrada_categoria(categoria_input)

    registro = {
        "fecha": fecha,
        "monto": monto,
        "categoria": categoria
    }
    print("Datos capturados correctamente:", registro)
    return registro
