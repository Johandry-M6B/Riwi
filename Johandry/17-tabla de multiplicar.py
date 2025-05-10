numero = int(input("Ingresar un numero para ver su tabla: "))

multiplicar = 1
print(f" tabla de multiplicacion del {numero}")
for i in range(1,11):
    resultado = numero * i
    print(f"{numero} X {i} = {resultado}")