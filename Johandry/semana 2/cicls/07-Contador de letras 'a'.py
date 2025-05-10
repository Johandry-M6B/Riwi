palabra = input("Ingresar una palabra: ")
contador = 0
for lentra in palabra:
    if lentra.lower() == "a":
        contador += 1
        
print(f"La letra a aparece {contador} veces en la palabra {palabra}. ")
        