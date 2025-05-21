import matplotlib.pyplot as plt
from analysis import analizar_datos, porcentaje_por_categoria, data
#Se espera que el archivo CSV tenga el formato: Fechas, Monto, Categoria
#Falta que validadores.py pueda validar categorias

def graficar_pastel_por_categoria(porcentaje_por_categoria):
    etiquetas = porcentaje_por_categoria.index
    valores = porcentaje_por_categoria.values

    plt.figure(figsize=(8, 8))
    plt.pie(valores, labels=etiquetas, autopct='%1.1f%%', startangle=90)
    plt.title("Distribución de Egresos por Categoría")
    plt.axis('equal')  # Hace que el círculo no se vea ovalado
    plt.tight_layout()
    plt.savefig("Grafica de Pastel.png")
    plt.show()
#Esto creara la grafica de pastel de las categorias
#Oviamente el analysis.py debe ser accionado antes que este archivo
#Se espera que los datos tengan esta forma:
#{
#  "Alimentos": 45.0,
#  "Transporte": 30.0,
#  "Entretenimiento": 25.0
#}

def graficar_barras_por_dia(data):
    resumen_por_dia = data.groupby("Fechas")["Monto"].sum()
    fechas = resumen_por_dia.index
    montos = resumen_por_dia.values

    colores = ['blue' if monto > 0 else 'red' for monto in montos]

    plt.figure(figsize=(10, 6))
    plt.barh(fechas.astype(str), montos, color=colores)
    plt.xlabel("Monto")
    plt.ylabel("Fecha")
    plt.title("Ingresos y Egresos por Día")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("Grafica de Barras.png")
    plt.show()
#Se espera que data sea un data frame que tenga esta forma:
#  Fechas       Monto     Categoría
#0 2025-05-01   -500.0     Comida
#1 2025-05-01    1500.0    Sueldo
#2 2025-05-02   -100.0     Transporte
