asignaturas = {}
asignaturas.update({"Matemáticas": int(input("Ingrese el valor del crédito para Matemáticas"))})
asignaturas.update({"Física": int(input("Ingrese el valor del crédito para Física"))})
asignaturas.update({"Química": int(input("Ingrese el valor del crédito para Química"))})
print("Matemáticas", "tiene", asignaturas["Matemáticas"], "créditos")
print("Física", "tiene", asignaturas["Física"], "créditos")
print("Química", "tiene", asignaturas["Química"], "créditos")
print("Número total de créditos del curso:", sum(asignaturas.values()))