def factorial(n):
    """Función que calcula el factorial de un número entero positivo.
    Parámetros
    n: Es un entero positivo.
    Devuelve el factorial de n.
    """
    a=1
    for i in range(1, int(n)+1):
        a*=i
    return a

print(factorial(4))
# resultado esperado: 24

print(factorial(20))
# resultado esperado: 2432902008176640000
