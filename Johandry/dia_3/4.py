# Función para verificar que las calificaciones estén en el rango de 0 a 100
def pedir_calificaciones():
    while True:
        calificaciones = input("Ingrese una lista de calificaciones separadas por comas (0 a 100): ")
        try:
            # Convertimos las calificaciones en una lista de números flotantes
            calificaciones_lista = [float(cal) for cal in calificaciones.split(",")]
            
            # Comprobamos si todas las calificaciones están dentro del rango permitido
            if all(0 <= cal <= 100 for cal in calificaciones_lista):
                return calificaciones_lista
            else:
                print("Por favor, ingrese solo calificaciones entre 0 y 100.")
        except ValueError:
            print("Entrada inválida. Asegúrese de ingresar solo números y que estén separados por comas.")

# Solicitar al usuario una lista de calificaciones válidas
calificaciones_lista = pedir_calificaciones()
while True:
    calificaciones = (input("Ingresa calificaciones, separadas por comas "))
    try:
        promedio = sum(calificaciones_lista) / len(calificaciones_lista)

        print(f"El promedio de las calificaciones es {promedio:.2f}")
        break
    except ValueError:
          print("Entrada invalida. Asegúrese de ingresar solo números.") 

# Solicitar una calificación específica para contar cuántas veces aparece
while True:
    try:
        calificacion_especifica = float(input("Ingrese una calificación específica para contar (0 a 100): "))
        if 0 <= calificacion_especifica <= 100:
            break  # Si la calificación está dentro del rango, salimos del ciclo
        else:
            print("La calificación debe estar entre 0 y 100.")
    except ValueError:
        print("Por favor ingrese un valor numérico válido para la calificación.")
