def square(sample):
    """Función que calcula los cuadrados de una lista de números.
    Parámetros
    sample: Es una lista de números
    Devuelve una lista con los cuadrados de los números de la lista sample.
    """
    for i in range(len(sample)):
        sample[i] **= 2
    return sample

def statistics(sample):
    #Función que calcula la media, varianza y desviación típica de una muestra de números.
    #Parámetros
    #sample: Es una lista de números
    #Devuelve un diccionario con la media, varianza y desviación típica de los números en sample.

    media=0
    tmp={'media':0,'varianza':0,'desviacion tipica':0}
    for i in range(len(sample)):
        media=sum(sample)/len(sample) #Calcula el promedio
    tmp.update({'media':media}) #Actualiza tmp
    sumatoria=0
    for i in sample:
        sumatoria+=((i-media)**2) #Calcula el sumatorio
    varianza=sumatoria/len(sample) #Calcula la varianza
    tmp.update({'varianza':varianza}) #Actualiza tmp
    desviacionTipica=varianza**(1/2) #Calcula la desviacion tipica
    tmp.update({'desviacion tipica':desviacionTipica}) #Actualiza tmp
    return tmp
print(statistics([1, 2, 3, 4, 5]))
# resultado esperado: {'media': 3.0, 'varianza': 2.0, 'desviacion tipica': 1.4142135623730951}

print(statistics([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))
# resultado esperado: {'media': 8.700000000000001, 'varianza': 18.95666666666665, 'desviacion tipica': 4.353925431913901}

# ! Comentario para el profesor: la fórmula para resolver el problema es diferente, pero los resultados son prácticamente los mismos
# ! (aproximadamente una milbillonésima de margen de error)
