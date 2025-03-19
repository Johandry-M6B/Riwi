numero = int(input("ingresar un numero"))

if numero % 3 == 0 and numero % 5 == 0:
    print("Divisible Entre 3 y 5.")
elif numero % 3 == 0:
    print("Divisible solo entre 3")
elif numero % 5 == 0:
    print("Divisible solo entre 5")
else:
    print("No divisible ni entre 3 ni 5")