membresia = input("Tiene Menbrsia (si o no): ")
valor_de_compra =float(input("Ingresar valor de compra: $"))

descuento = valor_de_compra * 0.20
descuento_total = valor_de_compra - descuento


if membresia == "si" or valor_de_compra >= 500:
    print(f"""
          Ustede a recibido un descuento del 20%
          Total a pagar es: ${descuento_total}
          """) 
else:
    print(f"""
          
          Total a pagar es: ${valor_de_compra}
          """)