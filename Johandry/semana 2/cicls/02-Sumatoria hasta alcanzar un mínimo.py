#Solicita al usuario que ingrese números. Sigue sumándolos hasta que la suma sea mayor a 100. Usa un while.

suma = 0

while suma <= 100:
    
   numero = int(input("Ingresar un mumero para sumar: "))
   suma += numero
   print(f"suma actual {numero}")

print(f"La suma a terminado {suma}")   