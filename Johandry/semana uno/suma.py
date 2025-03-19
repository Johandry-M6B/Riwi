numero = int(input("Ingresa un número: "))


suma = 0


for i in range(1, numero + 1):
    suma += i  


print(f"La suma de los números desde 1 hasta {numero} es: {suma}")