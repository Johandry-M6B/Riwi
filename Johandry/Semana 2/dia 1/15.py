edad = int(input("Ingresar edad: "))
tarjeta = input("Tiene tarjeta Si/No: ")

if edad == (18 <= edad <= 25) or (tarjeta == "si"):
    print("Tiene promocion especial.")
else:
    print("No tiene promocion. ")
    