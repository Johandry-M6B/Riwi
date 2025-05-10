##Una persona ingresa su edad. Clasifica esa edad en una de las siguientes categorías:


edad = int(input("ingresar edad: "))

if edad < 18:
    print("Menor de edad.")
elif edad >= 18 and edad <= 30:
    print("Adulto.")
elif edad >= 31 and edad <= 65:
    print("Adulto maduro")
else:
  print("Adulto mayor")