numero1 = float(input("Ingresese un numero: "))


while True:
    numero2 = float(input("Ingresese otro numero: "))
    if  numero2 == 0:           
        print("el numero no valido")
                
    else:
        break
        
        
resultado = numero1 / numero2
residuio = numero1 % numero2  
print(resultado)

print(residuio)