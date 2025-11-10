'''Actividad cierre unidad 4'''

'''Alumno: Facundo De La Rosa'''

'''Ejercicio 1:'''

for i in range(101):
    print(i)



'''ejercicio 2:'''

numero = int(input("ingrese un numero entero: "))


cant_digitos = len(str(abs(numero)))


print(f"el numero tiene {cant_digitos} digitos.")

'''ejercicio 3:'''

a = int(input("ingrese el primer numero: "))
b = int(input("ingrese el segundo numero: "))


inicio = min(a, b) + 1
fin = max(a, b)


suma = 0
for i in range(inicio, fin):
    suma += i


print(f"la suma de los numeros entre {a} y {b} es: {suma}")





'''ejercicio 4:'''

suma = 0
while True:
    n = int(input("ingrese un numero (0 para terminar): "))
    if n == 0:
        break
    suma += n


print(f"la suma total es: {suma}")

'''ejercicio 5:'''

import random


numero_secreto = random.randint(0, 9)
intentos = 0


while True:
    intento = int(input("adivine el numero (0-9): "))
    intentos += 1
    if intento == numero_secreto:
        print(f"correcto! lo lograste en {intentos} intentos.")
        break
    else:
        print("incorrecto, intente nuevamente.")



'''ejercicio 6:'''

for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)



'''ejercicio 7:'''

n = int(input("ingrese un numero entero positivo: "))
suma = 0


for i in range(n + 1):
    suma += i


print(f"la suma de los numeros de 0 a {n} es: {suma}")



'''ejercicio 8:'''
pares = impares = positivos = negativos = 0


for i in range(100):  # cambiar este valor si queres probar con menos
    num = int(input(f"ingrese el numero {i+1}: "))


    if num % 2 == 0:
        pares += 1
    else:
        impares += 1


    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1


print(f"pares: {pares}")
print(f"impares: {impares}")
print(f"positivos: {positivos}")
print(f"negativos: {negativos}")



'''ejercicio 9:'''

total = 0
cantidad = 100  # cambiar si queres probar con menos


for i in range(cantidad):
    num = int(input(f"ingrese el numero {i+1}: "))
    total += num


media = total / cantidad
print(f"la media de los numeros ingresados es: {media}")



'''ejercicio 10:'''


numero = input("ingrese un numero: ")
invertido = numero[::-1]
print(f"el numero invertido es: {invertido}")
