'''ejercicio 1'''


notas = [7, 5, 9, 4, 8, 10, 6, 7, 3, 9]


print("lista de notas:")
for n in notas:
    print(n)


promedio = sum(notas) / len(notas)
print("promedio:", promedio)
print("nota mas alta:", max(notas))
print("nota mas baja:", min(notas))



'''ejercicio 2'''


productos = []
for i in range(5):
    p = input("ingrese un producto: ")
    productos.append(p)

print("lista ordenada:")
for p in sorted(productos):
    print(p)

eliminar = input("que producto desea eliminar?: ")
if eliminar in productos:
    productos.remove(eliminar)
else:
    print("ese producto no esta en la lista")

print("lista actualizada:")
for p in productos:
    print(p)


'''ejercicio 3'''


import random

numeros = [random.randint(1, 100) for i in range(15)]
pares = []
impares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("lista completa:", numeros)
print("pares:", pares)
print("impares:", impares)
print("cantidad de pares:", len(pares))
print("cantidad de impares:", len(impares))

'''ejercicio 4'''

valores = [1, 2, 3, 2, 4, 1, 5, 3]
sin_repetidos = list(set(valores))

print("lista original:", valores)
print("lista sin repetidos:", sin_repetidos)


'''ejercicio 5'''


estudiantes = ["ana", "juan", "mario", "sofia", "lucas", "maria", "pedro", "carla"]

accion = input("desea agregar o eliminar un estudiante? (agregar/eliminar): ")

if accion == "agregar":
    nuevo = input("ingrese el nombre del estudiante: ")
    estudiantes.append(nuevo)
elif accion == "eliminar":
    borrar = input("ingrese el nombre del estudiante a eliminar: ")
    if borrar in estudiantes:
        estudiantes.remove(borrar)
    else:
        print("ese nombre no esta en la lista")
else:
    print("opcion no valida")

print("lista final:")
for e in estudiantes:
    print(e)


'''ejercicio 6'''


numeros = [3, 5, 7, 9, 2, 4, 8]
ultimo = numeros[-1]
rotada = [ultimo] + numeros[:-1]

print("lista original:", numeros)
print("lista rotada:", rotada)


'''ejercicio 7'''


temperaturas = [
    [12, 25],
    [14, 27],
    [10, 23],
    [11, 26],
    [13, 28],
    [9, 22],
    [15, 30]
]

minimas = [fila[0] for fila in temperaturas]
maximas = [fila[1] for fila in temperaturas]

prom_min = sum(minimas) / len(minimas)
prom_max = sum(maximas) / len(maximas)

print("promedio minimas:", prom_min)
print("promedio maximas:", prom_max)

amplitudes = [maximas[i] - minimas[i] for i in range(7)]
dia_max_amplitud = amplitudes.index(max(amplitudes)) + 1

print("dia con mayor amplitud termica:", dia_max_amplitud)



'''ejercicio 8'''


notas = [
    [7, 8, 6],
    [5, 9, 7],
    [8, 6, 9],
    [9, 7, 8],
    [6, 8, 7]
]

for i in range(len(notas)):
    promedio = sum(notas[i]) / len(notas[i])
    print("promedio estudiante", i + 1, ":", promedio)

for j in range(3):
    materia = [notas[i][j] for i in range(5)]
    prom_mat = sum(materia) / len(materia)
    print("promedio materia", j + 1, ":", prom_mat)


'''ejercicio 9'''


tablero = [["-" for j in range(3)] for i in range(3)]

def mostrar_tablero():
    for fila in tablero:
        print(" ".join(fila))

turno = "x"

for i in range(9):
    print("turno de", turno)
    mostrar_tablero()
    fila = int(input("ingrese fila (0-2): "))
    col = int(input("ingrese columna (0-2): "))
    if tablero[fila][col] == "-":
        tablero[fila][col] = turno
        turno = "o" if turno == "x" else "x"
    else:
        print("casilla ocupada")

print("tablero final:")
mostrar_tablero()


# ejercicio 10
ventas = [
    [100, 120, 90, 80, 110, 95, 130],
    [200, 180, 170, 190, 210, 200, 220],
    [150, 140, 130, 160, 155, 145, 165],
    [80, 95, 85, 70, 90, 100, 75]
]

'''total por producto'''


for i in range(4):
    total = sum(ventas[i])
    print("total producto", i + 1, ":", total)


totales_dias = [sum(ventas[i][j] for i in range(4)) for j in range(7)]
dia_mayor = totales_dias.index(max(totales_dias)) + 1
print("dia con mayores ventas:", dia_mayor)


totales_productos = [sum(ventas[i]) for i in range(4)]
producto_mayor = totales_productos.index(max(totales_productos)) + 1
print("producto mas vendido:", producto_mayor)


