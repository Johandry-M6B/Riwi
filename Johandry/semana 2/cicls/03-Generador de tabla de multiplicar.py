#Pide al usuario un número y muestra su tabla de multiplicar del 1 al 10 utilizando for y range().
numero = int(input("Ingresar un numero para ver su tabla de multilicacion"))

for i in range(1,11):
    resultado = numero * i
    print(f"{numero} X {i} = {resultado}")
