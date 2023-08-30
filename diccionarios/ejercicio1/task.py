monedas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}
xd = input("Introduce una divisa:")
if xd in monedas:
	print(monedas.get(xd))
else:
	print("La divisa no está.")