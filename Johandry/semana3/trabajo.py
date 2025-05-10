inventario = {}

def menu():
    while True:
        print("1 Agregar producto. ")
        print("2 Buscar producto.")
        print("3 Actualizar precio.")
        print("4 Actualizar cantidad")
        print("5 Eliminar producto")
        print("6 Calcular valor total.")
        print("7 Salir")
    
        opcion = input("Ingresar que quiere hacer.")
        
        match opcion: 
            
            case "1":
                agregar_producto:
            
            
            
            

def agregar(nombre,precio,cantidad):
   for 



















    nombre = input("ingresar nombre del producto: ")
    precio = int(input("Ingresar precio: "))
    cantidad = int(input("Ingresar cantidad: "))
    agregar(nombre,precio,cantidad)

    inventario[nombre] = (precio, cantidad)


menu("1","2","3","4","5","6","7" )
print("1 Agregar producto. ")
print("2 Buscar producto.")
print("3 Actualizar precio.")
print("4 Actualizar cantidad")
print("5 Eliminar producto")
print("6 Calcular valor total.")
print("7 Salir")
return(menu)