'''ejercicio 1:'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("ingrese un numero: "))

for i in range(1, num + 1):
    print("factorial de", i, "=", factorial(i))

'''ejercicio 2:'''


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("ingrese un numero: "))

for i in range(num + 1):
    print(fibonacci(i))

'''ejercicio 3:'''
def potencia(n, m):
    if m == 0:
        return 1
    return n * potencia(n, m - 1)

base = int(input("base: "))
expo = int(input("exponente: "))

print(potencia(base, expo))



'''ejercicio 4:'''

def decimal_a_binario(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_a_binario(n // 2) + str(n % 2)


num = int(input("ingrese un numero decimal: "))
print(decimal_a_binario(num))



'''ejercicio 5:'''

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = input("ingrese una palabra: ")
print(es_palindromo(texto))


'''ejercicio 6:'''
def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

num = int(input("ingrese un numero: "))
print(suma_digitos(num))


'''ejercicio 7:'''

def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

num = int(input("bloques del nivel inferior: "))
print(contar_bloques(num))


'''ejercicio 8:'''

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    ultimo = numero % 10
    return (1 if ultimo == digito else 0) + contar_digito(numero // 10, digito)

num = int(input("numero: "))
d = int(input("digito a buscar: "))

print(contar_digito(num, d))


