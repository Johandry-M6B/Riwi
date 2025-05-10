inventario = {}

while True:
    print("1 Agregar producto.  ")
    print("2 Monstrar lista. ")
    print("3 Actualizar producto. ")
    print("4 Eliminar producto. ")
    print("5 salir. ")
    
    opciones = input("Ingresar que quiere realizar: ")
    
    match opciones:
    
        case "1":
            id = input("ingresar ID del producto: ")
            nombre = input("Ingresar nombre: ")
            cantidad = int(input("Ingresar cantidad: "))
            color = input("Ingresar color: ")
            talla = input("Ingresar talla (S,M,L,XL.): ").upper()
            precio = float(input("Ingresar precio"))
            
            prenda = {
                "nombre" : nombre,
                "cantidad" : cantidad,
                "color" : color,
                "talla" : talla,
                "precio" : precio
            }
            inventario[id] = prenda
            print(f"Prenda Agrega correctamente con la ID {id}")
            
        case "2":
            if not inventario:
                print("Inventario vacio.")
            else:
                for id, producto in inventario:
                    print(f"ID : {id} {producto['nombre']} - {producto['cantida']} - {producto['color']} - {producto['talla']} - {producto['precio']} ") 
                    
        case "3":
            if not inventario:
                print("Inventario Vacio.")
            else:
                id = input("Ingresar la ID del producrto para actualizar: ")
                for id in inventario:
                    producto = inventario[id]
                    producto['nombre'] = input(f"Ingresar nuevo nombre({producto['nombre']}) ")
                    producto['cantidad'] = input(f"Ingresar la nueva cantidad({producto}['cantidad']) ")
                    producto['color'] = input(f"Ingresar nuevo color ({producto['color']}) ")   
                    producto['talla'] = input(f"Ingresar nueva talla ({producto['talla']}) ")
                    producto['precio'] = input(f"Ingresar nuevo precio: ({producto['precio']})")
                    print("Producto actualizado correctamente")
        case "4":
            if not inventario:
                
                    
                
                    
            
                        
             
        