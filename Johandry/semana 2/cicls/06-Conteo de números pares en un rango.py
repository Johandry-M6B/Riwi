#Pide dos números al usuario (inicio y fin) y cuenta cuántos números pares hay entre ellos usando for y if.
numero1 = int(input("Ingresar un numero: "))
numero2 = int(input("Ingresar otro numero: "))

for i in range(numero1, numero2 + 1):
    if i % 2 == 0:
     print(f"los numeros pares entre {numero1} y {numero2} son {i}")
