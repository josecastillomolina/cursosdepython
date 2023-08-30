p= input("Introduce el precio del producto con dos decimales:")
print(p[:p.find(".")], "colones y", p[p.find(".")+1:], "céntimos.")