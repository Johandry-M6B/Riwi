import time 

while True:   
   try:
         calificacion= float(input("Ingresar si calificacion (de 0 a 100): "))
         if  0 <= calificacion <= 100:
          print()
          break
         else:("El nuemro de de estar dentro del rango(0 a 100).")
         print
         
         
         if calificacion >= 60:
          print("Aprobado.")
         elif calificacion <= 60:
          print("Desaprobado.")
          break
         else:
          print("Calificacion .")
         
         
         
         
         
         
         
         
   except ValueError:
       print("Por favor ingresar calificacion valida.")
