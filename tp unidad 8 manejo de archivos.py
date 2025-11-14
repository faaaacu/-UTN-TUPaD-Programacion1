with open("productos.txt", "w") as f:
    f.write("lapicera,120.5,30\n")
    f.write("regla,200,15\n")
    f.write("goma,80,25\n")


print("lista de productos:")
with open("productos.txt", "r") as f:
    lineas = f.readlines()

productos = []

for linea in lineas:
    linea = linea.strip()
    nombre, precio, cantidad = linea.split(",")
    print("producto:", nombre, "| precio: $", precio, "| cantidad:", cantidad)

    productos.append({
        "nombre": nombre,
        "precio": float(precio),
        "cantidad": int(cantidad)
    })

print("ingresar producto nuevo")
nom = input("nombre: ")
pre = input("precio: ")
can = input("cantidad: ")

with open("productos.txt", "a") as f:
    f.write(f"{nom},{pre},{can}\n")



productos.append({
    "nombre": nom,
    "precio": float(pre),
    "cantidad": int(can)
})


buscar = input("ingresa el nombre de un producto para buscar: ")

encontro = False
for p in productos:
    if p["nombre"] == buscar:
        print("producto encontrado:", p)
        encontro = True
        break

if not encontro:
    print("no existe ese producto")



with open("productos.txt", "w") as f:
    for p in productos:
        f.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
