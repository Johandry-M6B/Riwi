nota = int(input("Ingresar tu nota (0 a 100): "))
faltas = int(input("Cuantas Faltas tuvistes:  "))

if nota >= 60 and faltas < 3:
    print(f"Su nota es {nota} esta Aprobado.")
else:
    print(f"Su nota es {nota} esta Reprobado. ")
    