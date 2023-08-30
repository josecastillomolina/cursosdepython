palabra = input("Introduce una palabra:")
reversed_palabra = palabra
palabra = list(palabra)
reversed_word = list(reversed_palabra)
reversed_word.reverse()
if palabra == reversed_palabra:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
