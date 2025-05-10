##Un cliente ingresa el monto de su compra y si es VIP (“S”/“N”). Aplica el siguiente descuento

monto = float(input("Ingresar el monto de sus compra: "))
VIP = input("Ingresar Si es VIP (S/N): ").upper()
 
if monto >= 500:
    if VIP == "S":    
      descuento = 0.20
    else:
        descuento = 0.10
elif monto < 500:
    if VIP == "S":
        descuento = 0.05
    else:
        descuento = 0.00
else:
    print("Entrada no valida")
    descuento = None

if descuento is not None:
    monto_final = monto * (1 - descuento)
    print(f"Descuento aplicado: {descuento * 100}% ")
    print(f"Monto final a pagar: {monto_final:.2f}")     
        
              
    