def imprimir_Arreglo(arreglo):
  tam=len(arreglo)
  for i in range(tam):
    print(f"[{arreglo[i]}]",end="")

def algoritmo_bus_lineal(arreglo,sueldo):
  resultado=False
  tam=len(arreglo)-1
  for i in range (tam):
    if (arreglo[i]==sueldo):
      resultado=True
      return resultado
  return resultado

listaSueldos=[20.8,150.5,170.5,180.8, 190,30,75.6,200]

imprimir_Arreglo(listaSueldos)
sueldo=float(input("Ingresa el sueldo a buscar: "))
respuesta=algoritmo_bus_lineal(listaSueldos,sueldo)
if respuesta:
  print("El sueldo fue encontrado en nuestro sistema")
else:
  print("El sueldo no fue encontrado en nuestro sistema")
  