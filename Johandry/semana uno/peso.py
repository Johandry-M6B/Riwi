peso = float(input("Ingrese su peso en kilogramos (kg): "))

altura = float(input("Ingrese su altura en metros (m): "))

imc = peso / (altura ** 2)

print(f"tu indice de masa corporal (IMC) es: {imc: .2f}")

if imc < 18.5 :
    print("Estas bajo peso :1.")
    
elif 18.5 <= imc < 24.9:
    print("Tienes un estandar :). ")
    
elif 25 <= imc < 29.9:
    print("Tienes sobre peso :/. ")
else: 
    print("Tienes obesidad :( .)")
    