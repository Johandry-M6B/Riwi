
while True:
    numero1=input("ingrese un numero a comparar: ")
    numero2=input("ingrese otro numero a comparar: ")
    
    if not numero1.isdigit() or not numero2.isdigit():
        print('Ingresa datos tipo númericos')
        continue
    umero1=(numero1)
    numero2=(numero2)

    if numero1 >= numero2:
        print(f'{numero1} es mayor que {numero2}')
    if numero1 < numero2:
        print(f'{numero1} es menor que {numero2}')
    if numero1 == numero2:
        print(f'{numero1} es igual que {numero2}')
    else:
        ()
    break               