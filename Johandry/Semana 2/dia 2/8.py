palabra = input("ingresar palabras:  ")
mayuscula = 0
miniscula = 0

for letra in palabra:
    if letra.isupper():
        mayuscula += 1
    elif letra.islower():
        miniscula += 1
print(f"Letras en mayusculas son {mayuscula}")          
print(f"Letras en minisculas son {miniscula}")          