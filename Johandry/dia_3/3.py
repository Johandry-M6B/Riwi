

calificaciones = (input("Ingresar calificaciones separadas por comas: "))
calificaciones_lista = [float(calificaciones) for calificaciones in calificaciones.split(",")]

promedio = sum(calificaciones_lista) / len(calificaciones_lista)

print(f"El promedio de la calificaciones es {promedio:.2f}")

time.sleep(1)

valor = float(input("Ingresa la calificacion a comparar: "))
 
contador = 0
i = 0
while i < len(calificaciones_lista):
    if calificaciones_lista[i] > valor:
      contador += 1
    i += 1
print(f"hay {contador} calificaciones mayores que {valor}")
time.sleep(1)

calificaciones_especiales = float(input("Ingresar un calificacion especial: "))
contador_2= 0
for cal in calificaciones_lista:
    if cal == calificaciones_especiales:
        contador_2 += 1 
    elif cal < 0:
        print("Se encontro calificacion negativa. \nTerminado el conteo.")
        break
print(f"la calificaciones {calificaciones_especiales} aparecen {contador_2} veces.")
