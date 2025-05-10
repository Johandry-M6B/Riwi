##El usuario crea una contraseña que debe cumplir dos requisitos:
#        1. Tener al menos 8 caracteres.
#       2. Contener al menos el carácter @.
#Si la longitud es insuficiente, informar “Contraseña muy corta”. Si la longitud es correcta pero falta @, informar “La contraseña debe incluir al menos un '@'”. Sólo cuando ambos requisitos se cumplan, mostrar “Contraseña válida”

contraseña = input("Ingresar Contraseña (la contraseña debe 8 caraceteres y un @): ")

if len(contraseña) > 8 or "@" not in contraseña:
     print("Contraseña valida")

else:
     print("Contraseña invalida")
          
