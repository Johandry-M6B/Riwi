
import time
calificacion = float(input("Ingrese Un calificion (de 0 a 100):"))


if calificacion >= 60:
    print("Aprobado")
elif calificacion <= 59:
    print("No Aprobado")
time.sleep(2)
calificaciones = input("Ingrese Su calificaciones separadas por comas: ")
calificaciones_lista = [float(cal) for cal in calificaciones.split(",") ]

promedio = sum(calificaciones_lista) / len(calificaciones_lista)

print(f"El promedio de las calificaciones es {promedio:.2f}")
time.sleep(2)

valor = float(input("Ingresar Un valor a conmpar: "))

contador = 0
 
i = 0
while i < len(calificaciones_lista):
    if calificaciones_lista[i] > valor:
        contador += 1
    i += 1
print(f"Hay {contador} califcaiones mayores que {valor}.")
time.sleep(2)
calificacion_especial = float(input("Ingresar una calificacion especial para contar: "))

for cal in calificaciones_lista:
    if cal == calificacion_especial:
        contador += 1
        continue
    if cal < 0:
        print("Se Econtro con una calificacion negativa. Terminando el conteo. ")
        break
print(f"la calificacion {calificacion_especial} aparece {contador} veces.")