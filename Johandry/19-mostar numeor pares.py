# Pedir al usuario un número N
numero = int(input("Ingresa un número N: "))

print(f"\nLos primeros {numero} números pares son:")


contador = 0
numeros = 2


while contador < numero:
    print(numeros)
    numeros += 2
    contador += 1

    
