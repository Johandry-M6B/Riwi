def obtener_dato_numerico(mensaje, minimo=0, maximo=None):
    """
    Solicita al usuario un número y valida que esté dentro del rango especificado.
    """
    while True:
        try:
            valor = float(input(mensaje))
            if valor < minimo or (maximo is not None and valor > maximo):
                print(f"Por favor, ingrese un valor entre {minimo} y {maximo if maximo is not None else 'infinito'}.")
            else:
                return valor
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número válido.")

# Solicitar datos al usuario
nombre_producto = input("Ingrese el nombre del producto: ").strip().title()
precio_unitario = obtener_dato_numerico("Ingrese el precio unitario: ", minimo=0.01)
cantidad = obtener_dato_numerico("Ingrese la cantidad de productos adquiridos: ", minimo=1)
descuento = obtener_dato_numerico("Ingrese el porcentaje de descuento (0-100): ", minimo=0, maximo=100)

# Calcular costos
costo_sin_descuento = precio_unitario * cantidad
monto_descuento = (descuento / 100) * costo_sin_descuento
costo_total = costo_sin_descuento - monto_descuento

# Mostrar resultados
print("\nResumen de la compra:")
print(f"Producto: {nombre_producto}")
print(f"Precio unitario: ${precio_unitario:.2f}")
print(f"Cantidad: {cantidad}")
print(f"Costo sin descuento: ${costo_sin_descuento:.2f}")
print(f"Descuento aplicado: ${monto_descuento:.2f} ({descuento}%)")
print(f"Costo total a pagar: ${costo_total:.2f}")
 
"calcular_costo_total"



