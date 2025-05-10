#Permite al usuario ingresar números de manera indefinida. Usa un while True que termina si el usuario escribe “salir”, acumulando los números ingresados.
contador = 0
while True:
    numero = input("Ingresar numero o ingresa 'Salir' para terminar: ")
    
    if numero.lower() == "salir":
    
       break
    elif numero is not "salir":
        numero = int(numero)
        contador += numero
        print(f"suma acumulada: {contador}")
    else:
        print("Valor no valido ingrese un numero o 'salir'.")

print(f"La suma total de los numeros es {contador}")