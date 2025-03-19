palabra = input("Ingresar Un palabra: ")
contador = 0
 
for letra in palabra:
    if letra.lower() == "a":
        contador += 1  
print(f" La letra 'a' aparece {contador} veces  de palabra '{palabra}'.  ")    
    