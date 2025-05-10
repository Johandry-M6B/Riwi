

numero1 = int(input("ingrese primer numero a comparar: "))
numero2 = int(input("ingrese segundo numero a comparar: "))
numero3 = int(input("ingrese tercer numero a comparar: "))

if numero1 > numero2 and numero1 > numero3:
    print(f'{numero1} es mayor que {numero2} y {numero3}')
elif numero2 > numero1 and numero2 > numero3:
    print(f'{numero2} es mayor que {numero1} y {numero3}')
elif numero3 > numero2 and numero3 :
    print(f'{numero3} es mayor que {numero2} y {numero1}')
else:
    print()