"""ejercicio 1"""
print("hola mundo")

"""ejercicio 2""" 
nombre = input("Cual es tu nombre:")
print(f"Hola {nombre}!")

"""ejercicio 3"""
nombre = input("Cual es tu nombre?: ")
apellido = input("Cual es tu apellido?: ")
edad = input("Cuantos años tenes?: ") 
pais = input("De que pais sos?: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {pais}")

"""ejercicio 4"""
import math

radio = int(input("Ingrese el radio: "))
area = math.pi * (radio**2)
perimetro = 2 * math.pi * radio


print(f"El área del círculo es {area:.2f} y el perímetro es {perimetro:.2f}")

"""ejercicio 5"""
segundos = int(input("Ingrese la cantidad de segundos: "))
conversion_a_hora = segundos / 360

print(f"{segundos} equivale a {conversion_a_hora} horas ")

"""ejercicio 6"""

numero = int(input("Ingrese el numero a multiplicar: "))

for i in range (1, 11):
    multiplicacion = numero * i
    print(f"{numero}x{i} = {multiplicacion}")

"""ejercicio 7"""

num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))
suma = num1 + num2
resta = num1 - num2
division = num1 / num2
multiplicacion = num1 * num2
if (num1 == 0) or (num2 == 0):
    
    print("Numero invalido, ingrese un numero distinto de cero ")
else:
    print(f"El resultado de la suma es de {suma}, el de la division {division}, el de la resta {resta}, y la multiplicacion {multiplicacion} ")
    
"""ejercicio 8"""

peso = int(input("Ingrese su peso en kg: ")) 
altura = float(input("Ingrese su altura en metros: "))

IMC = peso / (altura)**2

print(f"Su indice de masa corporal es de {IMC}")

"""ejercicio 9"""

temp_celsius = int(input("Ingrese la temperatura en grados celsius que quieres convertir: "))
temp_far = (9 / 5) * temp_celsius + 32 

print(f"Su temperatura es equivalente a {temp_far} en grados fahrenheit")

"""ejercicio 10"""

num1 = int(input("ingrese el primer numero:"))
num2 = int(input("ingrese el segundo numero:"))
num3 = int(input("ingrese el tercer numero:"))

promedio = (num1 + num2 + num3) / 3

print(f"El promedio entre los 3 numeros es de {promedio}")

