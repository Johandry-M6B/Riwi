#Diseña un programa donde el usuario debe adivinar un número secreto entre 1 y 10. Limítale a un máximo de 5 intentos usando while.

intentos = 4
numeros_secretos = 1
contador_intentos = 0


while contador_intentos != intentos:
    numero = int(input("Ingresar un numero: "))
    if numero == numeros_secretos:
        print("Adivinsate el numero secreto.")
        break
    elif numero > numeros_secretos :
        print(f"Fallaste no es el numero tienes {intentos - 1}") 
    else:
        ("ese no es numero secreto")
        
    
    intentos -= 1
else:
    print("Te quedaste sin intentos 1")    