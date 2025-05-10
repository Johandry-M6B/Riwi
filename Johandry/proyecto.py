import time 
#Aprobacion de materia
while True:   
   try:
         calificacion= float(input("Ingresar su calificacion (de 0 a 100): "))
         if  0 <= calificacion <= 100:
            print("Las notas para aprobar es de 60 en adelante.")
            time.sleep(2)
            if calificacion >= 60:
                print("Aprobado.")
                break
            else:
                print("Desaprobado.")
                break
         else:
            print("Ingresa una nota dentro del rango 0 a 100")
            time.sleep(2)
   except ValueError:
       print("Por favor ingresar calificacion valida, la calificaciones son de 0 a 100")
       time.sleep(2)
#Ingreso de calificaciones por como y promedio
while True:
    try:
        calificaciones = (input("Ingresa su calificaciones separadas por comas: "))
        time.sleep(1)
        calificaciones_sin_coma = calificaciones.split(",")#Split es el separador de la coma


        calificaciones_lista = []#lista
        for calificaciones in calificaciones_sin_coma:
            calificaciones_lista.append(float(calificaciones)) #califaciones
        suma_calificiones = 0
            
        for calificaciones in calificaciones_lista:
            suma_calificiones += calificaciones
                
        promedio = suma_calificiones / len(calificaciones_lista)#operacion para saber el promedio
        print(f"El promedio de las calificacione es {promedio:.2f} ")
        break    
         
    except ValueError:    
        print("Por favor ingresar calificacion valida, asegura que la calificaciones no terminen en coma(,)")
        time.sleep(2)
#Calificaciones mayores a el valor ingresado
while True:
    try:
        contador = 0
        i = 0
        valor = float(input("Ingresar un valor a comparar: "))
        while i < len(calificaciones_lista):
            if calificaciones_lista[i] > valor:#Recorre la lista y cuenta cuantas son mayores al valor 
                contador += 1
            i += 1
        print(f"Hay {contador} calificaciones mayor que {valor}")
        break       

    except ValueError:
        print("Por favor ingresar calificacion valida.")
        time.sleep(2)
#Contar cuantas veces aparece una calificacion
while True:    
    try:
        calificaciones_especiales = float(input("Ingresar una calificacion especial para contar: "))
        contador_2 = 0
        i2 = 0
        for cal in calificaciones_lista:
            if calificaciones_lista[i2] == calificaciones_especiales:
             contador_2 += 1
            i2 += 1
            continue
        if cal < 0:
            print("Ingreso una calificacion no valida")
            break

        print(f"La calificacion {calificaciones_especiales} aparece {contador_2} veces.")
        time.sleep(2)
        break
    except ValueError:
        print("Por favor ingresar calificacion valida.")
        