#Crea un menú interactivo (while True) donde se pregunte continuamente la edad del usuario hasta que una edad mayor o igual a 18 sea ingresada. Usa break adecuadamente.

while True:
    edad = int(input("Ingresar edad: "))
    if edad >= 18:
        print("Adecuada")
        break