import time

def validar_entrada_numerica(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            return float(entrada)
        except ValueError:
            print('❌ Error. Por favor, ingresa un número válido.')

def agregar_producto(inventario):

    while True:
        nombre = input('Ingrese el nombre del producto: ').strip()
        nombre = (nombre)
        if not nombre:
            print('❌ Error. El nombre del producto no puede estar vacío.')
            continue
        if nombre in inventario:
            print(f'⚠️ Advertencia. El producto ({nombre}) ya existe en el inventario.')
            return
        if nombre.isdigit():  # Verifica si el nombre consiste solo en dígitos
            print('❌ Error. El nombre del producto debe contener letras, no solo números.')
            continue
        else:
            break  # El nombre es válido, salimos del bucle para pedir precio y cantidad

    while True:
        precio_str = input('Ingrese el precio del producto: ')
        try:
            precio = float(precio_str)
            if precio < 0:
                print('❌ Error. El precio no puede ser negativo.')
                continue
            break
        except ValueError:
            print('❌ Error. Por favor, introduce un número válido para el precio.')

    while True:
        cantidad_str = input('Ingrese la cantidad disponible: ')
        try:
            cantidad = int(cantidad_str)
            if cantidad < 0:
                print('❌ Error. La cantidad no puede ser negativa.')
                continue
            break
        except ValueError:
            print('❌ Error. Por favor, introduce un número entero válido para la cantidad.')

    inventario[nombre] = (precio, cantidad)
    print(f'El producto ({nombre}) ha sido añadido al inventario.✅')

def consultar_producto(inventario, nombre_producto):

    if nombre_producto in inventario:
        precio, cantidad = inventario[nombre_producto]
        print(f'Detalles de ({nombre_producto}): Precio = ${precio:.2f}, Cantidad = {cantidad}')
    else:
        print(f'❌ Error. El producto ({nombre_producto}) no se encuentra en el inventario.')

def actualizar_precio(inventario, nombre_producto):

    if nombre_producto in inventario:
        nuevo_precio = validar_entrada_numerica(f'Ingrese el nuevo precio para ({nombre_producto}): ')
        precio_anterior, cantidad = inventario[nombre_producto]
        inventario[nombre_producto] = (nuevo_precio, cantidad)
        print(f'El precio de ({nombre_producto}) ha sido actualizado de ${precio_anterior:.2f} a ${nuevo_precio:.2f}.')
    else:
        print(f'Error: El producto ({nombre_producto}) no se encuentra en el inventario.')

def eliminar_producto(inventario, nombre_producto):
    # Elimina un producto del inventario.
    if nombre_producto in inventario:
        del inventario[nombre_producto]
        print(f'El producto ({nombre_producto}) ha sido eliminado del inventario.🗑️')
    else:
        print(f'Error: El producto ({nombre_producto})no se encuentra en el inventario.🚫')

def calcular_valor_total(inventario):
    # Calcula el valor total del inventario utilizando una función lambda.
    valor_total = sum(precio * cantidad for precio, cantidad in inventario.values())
    return valor_total

def mostrar_inventario(inventario):
    # Muestra el inventario actual (para fines de depuración o visualización).
    if not inventario:
        print('El inventario está vacío.🔦')
        return
    print('\n--- Inventario Actual ---')
    for nombre, (precio, cantidad) in inventario.items():
        print(f'- {nombre}: Precio = ${precio:.2f}, Cantidad = {cantidad}')
    print('-------------------------\n')

def ejecutar_operacion(opcion, inventario):
    # Ejecuta la operación seleccionada por el usuario.
    if opcion == "1":
        agregar_producto(inventario)
    elif opcion == "2":
        nombre = input('Ingrese el nombre del producto a consultar: ').strip()
        consultar_producto(inventario, nombre)
    elif opcion == "3":
        nombre = input('Ingrese el nombre del producto para actualizar el precio: ').strip()
        actualizar_precio(inventario, nombre)
    elif opcion == "4":
        nombre = input('Ingrese el nombre del producto a eliminar: ').strip()
        eliminar_producto(inventario, nombre)
    elif opcion == "5":
        valor_total = calcular_valor_total(inventario)
        print(f'El valor total del inventario es: ${valor_total:.2f}')
    elif opcion == "6":
        mostrar_inventario(inventario)
    elif opcion == "7":
        print('Saliendo del programa', end='')
        for s in range(3):
            print(".", end="", flush=True)
            time.sleep(0.8)
        print()  # Salto de línea al final de los puntos
        return False
    else:
        print('❌ Error: Por favor, selecciona una opción válida del menú (un número del 1 al 7).')
        return True

def main():
    inventario = {}
    ejecutando = True
    while ejecutando:
        print('\n--- Hola, bienvenidos a mi tienda Riwi.  ---')
        print('\n--- Gestión de Inventario ---')
        print('1. Añadir producto')
        print('2. Consultar producto')
        print('3. Actualizar precio')
        print('4. Eliminar producto')
        print('5. Calcular valor total del inventario')
        print('6. Mostrar inventario')
        print('7. Salir')
        opcion = input('Seleccione una opción: ')
        resultado_operacion = ejecutar_operacion(opcion, inventario)
        if resultado_operacion is False:
            ejecutando = False

if __name__ == '__main__':
    main()