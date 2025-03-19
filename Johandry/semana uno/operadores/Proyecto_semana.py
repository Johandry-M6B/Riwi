## Sistema que va a adivinar un numero que estoy pensando

numero = input("Adivina el numero que estoy pensando del 0 al 100")
numero = float(numero)

mi_numero = 8 

intentos = 3
for intento in range(intentos):
    numero = input("Adivina el numero que estoy pensasndo del 1 al 20: ")
    numero = float(numero)
    
if numero == mi_numero:
    print(f"Lo adivinaste mi numeor es {numero}")
elif intento == intentos:
    
else:
    print("estas equivocado ")