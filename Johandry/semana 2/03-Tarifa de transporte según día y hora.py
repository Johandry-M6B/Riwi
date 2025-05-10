##Un usuario indica si el día es laborable (“S”/“N”) y la hora del día (0–23). Calcula la tarifa aplicable:

dia_laboral = input("Ingresar si es un dia laboral (Si o No):").lower()

if dia_laboral == "si":
    horas_de_tranajo = int(input("Inngresar hora del dia (0-23):"))
    if (7 <= horas_de_tranajo <= 9 ) or (17 <= horas_de_tranajo <=19):
        print("Tarifa: Pico")
    else:
        print("Tarifa: Normal")
elif dia_laboral == "no":
    print("Fin de semana")
