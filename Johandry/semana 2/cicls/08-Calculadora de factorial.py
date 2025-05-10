#Pide un número al usuario y calcula su factorial usando un ciclo for.

numero = int(input("Ingresar un numero: "))
factorial = 1
for i in range(1, numero + 1):
    factorial *= i

print(f"La factorizcion de {numero} es {factorial}")
    