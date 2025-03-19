año = int(input("Ingresaer un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año es {año} Bisiesto.")
else:
    print
    