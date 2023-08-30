frutas = {'Plátano':50, 'Manzana': 60, 'Pera':70, 'Naranja': 80}
jiji = input("¿Qué fruta quieres?")
dox = float(input("¿Cuántos kilos?"))
if jiji in frutas:
    print(f"{frutas[jiji]} kilos de Manzana valen {dox*frutas[jiji]}")
else:
    print("Lo siento, la fruta Uva no está disponible.")
