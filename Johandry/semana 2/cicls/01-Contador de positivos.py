#Plantea un programa que permita ingresar 10 números y cuente cuántos de ellos son mayores que cero.
numeros_a_contar = 0

for i in range(10):
    numero = float(input(f"Ingresa el numero {i + 1}:  "))
    if numero > 0:
        numeros_a_contar += 1
print(f"CAntidad de numeros mayores a 0 son {numeros_a_contar}")