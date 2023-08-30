edad = int(input("Introduce tu edad:"))
if edad < 4:
    print("El precio de la entrada es 0 colones")
elif edad > 4 and edad <= 18:
    print("El precio de la entrada es 4 colones")
else:
    print("El precio de la entrada es 10 colones")