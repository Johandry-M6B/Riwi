contraseña_correcta = "python123"

for intento in range(3):
    contraseña = input("Ingresar Contraseña: ")
    if contraseña == contraseña_correcta:
        print("Acceso concedido")
        break
    else:
        print("Contraseña incorrecta. Intento", intento + 1, "de 3.")
if contraseña != contraseña_correcta:
    print("Acceso denegado. Demasiados intentos. ")        
    