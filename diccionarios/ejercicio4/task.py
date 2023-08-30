meses = {1:"Enero", 2:"Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 6:"Junio", 7:"Julio", 8:"agosto", 9:"Septiembre", 10: "Octubre", 11:"Novienbre", 12:"Diciembre"}
jiji = input("Introduce una fecha en formato dd/mm/aaaa:")
jiji = jiji.split("/")
print(jiji[0], "de", meses[int(jiji[1])], "de", jiji[2])

