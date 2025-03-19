numero1=int(input("Ingresar Un numero: "))
numero2=int(input("Ingresar numero a comparar: "))

if numero1 == numero2:
    print("los numeros son iguales")
elif numero1 > numero2:
    print(f"el primer numero ({numero1}) es mayor que el segundo ({numero2}).")
else:
    print(f"el segundo numero ({numero2}) es mayor que el primero ({numero1}).")
    3