usuario = input("ingresar usuario: ")
contaseña = input("ingresar contraseña: ")

confirmacion_U = input("Repita Usuario: ")
confirmacion_C = input("Repita Contraseña: ")

if contaseña == confirmacion_U and confirmacion_C:
    print("Acceso Permitido")
else:
    print("Acceso Denegado ")