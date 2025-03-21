def saludar():
    print("Hola Como Estas.")
def despedir(): 
    print("Adios")

while True:
    print("\n Menu")
    print("1 Saludar")
    print("2 Despedir")
    print("3 Salir")
        

    opcion = input("ELigue una de las siguntes opciones (1, 2, 3):")
    
    if opcion == "1":
     saludar()
    elif opcion == "2":
        despedir()  
    elif opcion == "3":
        print("A salido del Menu.")
        break
    else:
        print("Opcion no valida.") 