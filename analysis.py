import pandas as panda

def analizar_datos(path="datos/datos.csv")
  data = panda.leer_csv(path, fechas=["Fechas"])
  egresos = data[data["Monto"] < 0 ]
  total_egresos = egresos["Monto"].sum()
  porcentaje_por_categoria = (
        egresos.groupby("Categoría")["Monto"].sum() / total_egresos * 100
    ).abs().round(2)
  resumen_por_dia = df.groupby("Fecha")["Monto"].sum()
  max_fecha = resumen_por_dia.idxmax()
  min_fecha = resumen_por_dia.idxmin()
  return porcentaje_por_categoria, max_fecha, min_fecha, data
