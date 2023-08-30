datos = {}
while True:
    pregunta = input("¿Qué dato quieres introducir?")
    valor = input(f"{pregunta}: ")
    datos[pregunta] = valor
    print(datos)
    continuar = input("¿Quieres añadir más información (Si/No)?")
    if continuar.lower() != "si":
        break