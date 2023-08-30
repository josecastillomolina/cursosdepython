puntuacion=float(input("Introduce tu puntuación:"))
monto = 2400 * puntuacion
Aceptable = 0.4
Meritorio = 0.6
Inaceptable= 0.0
if puntuacion == Aceptable:
    print("Tu nivel de rendimiento es", Aceptable)
elif puntuacion == Meritorio:
    print("Tu nivel de rendimiento es", Meritorio)
elif monto == Inaceptable:
    print(" tu nivel de rendimiento es", Inaceptable)
else:
    print("Esta puntuación no es válida")
