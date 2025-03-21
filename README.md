mport time 

while True:   
   try:
         calificacion= float(input("Ingresar si calificacion (de 0 a 100): "))
         if  0 <= calificacion <= 100:
            print("Las notas para aprobar es de 60 en adelante.")
            if calificacion >= 60:
                print("Aprobado.")
            elif calificacion <= 60:
                print("Desaprobado.")
                break
         else:
            print("Ingresa una nota dentro del rango 0 a 100")

   except ValueError:
       print("Por favor ingresar calificacion valida.")
while True:
    try:
        calificaciones = (input("Ingresa su calificaciones separadas por comas: "))
        if  0 <= calificacion <= 100:
            print("no se puede ingresar numer ")
            
        else:
            print("Ingresa una calificacion valida")
            break
            

        calificaciones_lista = [float(cal) for cal in calificaciones.split(",")]
        
            
        promedio = sum(calificaciones_lista) / len(calificaciones_lista)

        print(f"El promedio de las calificacione es {promedio:.2f}. ")
        
    except ValueError:    
        print("Por favor ingresar calificacion valida.")
while True:
    try:
        contador = 0
        i = 0
        valor = float(input("Ingresar un valor a comparar: "))
        while i < len(calificaciones_lista):
            if calificaciones_lista[i] > valor:
                contador += 1
            i += 1
        print(f"Hay {contador} calificaciones mayor que {valor}")
        break       

    except ValueError:
        print("Por favor ingresar calificacion valida.")
while True:
    try:
        calificaciones_especiales = float(input("Ingresar una calificacion especial para contar: "))
        contador_2 = 0
        for cal in calificaciones_lista:
            contador_2 += 1
            continue
        if cal < 0:
            print("Ingreso una calificacion no valida")
            break

        print(f"La calificacion {calificaciones_especiales} aparece {contador_2} veces.")
        break


    except ValueError:
        print("Por favor ingresar calificacion valida.")
