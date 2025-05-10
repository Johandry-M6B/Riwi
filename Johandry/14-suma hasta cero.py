
suma = 0

while True:
    numero = int(input("Ingresar un numero para (o Cero para terminar.): "))
    if numero == 0:
        break
    suma += numero  
print(f"la suma total es {suma}")