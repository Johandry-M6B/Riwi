numero1 = int(input("Ingresar un numero: "))
numero2 = int(input(" Ingresar otro numero: "))
operacion = input("Ingresar Operacion a Realizar (+, -, *, /): ")
 

if operacion == "+":
    resultado = numero1 + numero2
    print(f"el resultado de {numero1} + {numero2} es {resultado}")
elif operacion == "-":
    resultado = numero1 - numero2
    print(f"el resultado de {numero1} - {numero2} es {resultado}")
elif operacion == "*":
    resultado = numero1 * numero2
    print(f"el resultado de {numero1} * {numero2} es {resultado}") 
elif operacion == "/":
    if numero2 != 0:
     resultado = numero1 / numero2
    print(f"el resultado de {numero1} / {numero2} es {resultado}")
else:
    print("Error: Operaracion no valida. Usa (+,-,*,/)")