dox={}
dox.update({"nombre":input("¿Cómo te llamas?")})
dox.update({"años":input("¿Cuántos años tienes?")})
dox.update({"dirección":input("¿Cuál es tu dirección?")})
dox.update({"teléfono":input("¿Cuál es tu número de teléfono?")})
print(dox["nombre"], "tiene", dox ["años"], "años,", "vive en", dox ["dirección"], "y su número de teléfono es", dox ["teléfono"])