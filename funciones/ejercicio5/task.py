def circle_area(radius):
    """Función que calcula el area de un círculo.
    Parámetros
    radius: Es el radio del círculo.
    Devuelve el área del círculo de radio radius.
    """
    return 3.1415*(radius**2)


def cilinder_volume(radius, high):
    """Función que calcula el volumen de un cilindro.
    Parámetros
    radius: Es el radio de la base del cilindro.
    high: Es la altura del cilindro.
    Devuelve el volumen del clindro de radio radius y altura high.
    """
    return circle_area(radius)*high


print(cilinder_volume(3, 5))
# resultado esperado: 141.3675

print(cilinder_volume(4, 6))
# resultado esperado: 301.584
