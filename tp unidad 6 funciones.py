'''ejercicio 1'''
def imprimir_hola_mundo():
    print("hola mundo")

imprimir_hola_mundo()


'''ejercicio 2'''

def saludar_usuario(nombre):
    return f"hola {nombre}"

nombre = input("ingresa tu nombre: ")
print(saludar_usuario(nombre))


'''ejercicio 3'''


def informacion_personal(nombre, apellido, edad, residencia):
    print(f"soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("ingresa tu nombre: ")
apellido = input("ingresa tu apellido: ")
edad = input("ingresa tu edad: ")
residencia = input("ingresa tu lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)


'''ejercicio 4:'''

import math
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("ingresa el radio del circulo: "))
print("area:", calcular_area_circulo(radio))
print("perimetro:", calcular_perimetro_circulo(radio))


'''ejercicio 5: '''


def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("ingresa la cantidad de segundos: "))
print("equivale a", segundos_a_horas(segundos), "horas")


'''ejercicio 6: '''


def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)

numero = int(input("ingresa un numero: "))
tabla_multiplicar(numero)


'''ejercicio 7: '''

def operaciones_basicas(a, b):
    return a + b, a - b, a * b, a / b

a = float(input("ingresa el primer numero: "))
b = float(input("ingresa el segundo numero: "))
suma, resta, mult, div = operaciones_basicas(a, b)
print("suma:", suma)
print("resta:", resta)
print("multiplicacion:", mult)
print("division:", div)


'''ejercicio 8:'''


def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("ingresa tu peso en kg: "))
altura = float(input("ingresa tu altura en metros: "))
print("tu imc es:", round(calcular_imc(peso, altura), 2))


'''ejercicio 9:'''


def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

celsius = float(input("ingresa la temperatura en celsius: "))
print("equivale a", celsius_a_fahrenheit(celsius), "fahrenheit")


'''ejercicio 10'''


def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("ingresa el primer numero: "))
b = float(input("ingresa el segundo numero: "))
c = float(input("ingresa el tercer numero: "))
print("el promedio es:", calcular_promedio(a, b, c))
