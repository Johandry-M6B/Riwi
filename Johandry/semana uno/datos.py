#pida un cantidad de votantes y registre sus votos entre 2 candidatos
#diga quien gano y cuantos votos obtuvo cada uno

votos_participate1=int(input("ingrese numeros de votos del participante uno: "))
votos_participate2=int(input("ingrese numeros de votos del participante dos: "))

print(f"la cantidad de votos del primer candidato es:{votos_participate1}")
print(f"la cantidad de votos del segundo candidato es:{votos_participate2}")

if votos_participate1 > votos_participate2:
    print(f"el canditado uno a ganado con {votos_participate1} votos.")

elif votos_participate1 < votos_participate2: 
    print(f"el candidato dos a ganado con {votos_participate2} votos.") 
else:
    print(f"el resultado es un empate los dos candidatos tienen {votos_participate1} votos.")
    
