##Determinar signo y paridad 
#Dado un número entero proporcionado por el usuario, determina primero si es positivo, negativo o cero. Si el número no es cero, establece además si es par o impar.

numero = int(input("Ingresar un numero: "))

if numero > 0:
    print("El Numero es positivo.")
elif numero < 0:
    print("El Numero es negativo.")
else:
    print("El numero fue zero")
    
    
    
if numero != 0:
    if numero % 2 == 0:
        print("Numero es par.")
    else:
        print("El numero es impar.")

