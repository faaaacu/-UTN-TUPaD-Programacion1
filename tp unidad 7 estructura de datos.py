'''ejercicio 1:'''
precios_frutas = {'banana': 1200, 'anana': 2500, 'melon': 3000, 'uva': 1450}

precios_frutas['naranja'] = 1200
precios_frutas['manzana'] = 1500
precios_frutas['pera'] = 2300

'''ejercicio 2:'''
precios_frutas['banana'] = 1330
precios_frutas['manzana'] = 1700
precios_frutas['melon'] = 2800

'''ejercicio 3:'''
lista_frutas = list(precios_frutas.keys())
print(lista_frutas)

'''ejercicio 4:'''
contactos = {}

for i in range(5):
    nombre = input('ingresa nombre ')
    numero = input('ingresa numero ')
    contactos[nombre] = numero

buscar = input('ingresa el nombre a buscar ')

if buscar in contactos:
    print(contactos[buscar])
else:
    print('no existe el contacto')

'''ejercicio 5:'''
frase = input('ingresa una frase ')
palabras = frase.split()

palabras_unicas = set(palabras)
print(palabras_unicas)

conteo = {}
for p in palabras:
    if p in conteo:
        conteo[p] += 1
    else:
        conteo[p] = 1

print(conteo)

'''ejercicio 6:'''
alumnos = {}

for i in range(3):
    nombre = input('ingresa nombre del alumno ')
    n1 = float(input('nota 1 '))
    n2 = float(input('nota 2 '))
    n3 = float(input('nota 3 '))
    alumnos[nombre] = (n1, n2, n3)

for a in alumnos:
    notas = alumnos[a]
    prom = (notas[0] + notas[1] + notas[2]) / 3
    print(a, prom)

'''ejercicio 7:'''
parcial1 = {1, 2, 3, 4}
parcial2 = {3, 4, 5, 6}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print(ambos)
print(solo_uno)
print(al_menos_uno)

'''ejercicio 8:'''
stock = {}

prod = input('ingresa producto ')
if prod in stock:
    suma = int(input('cuantas unidades agregar '))
    stock[prod] += suma
else:
    nuevo = int(input('producto no existe ingresa stock inicial '))
    stock[prod] = nuevo

print(stock)

'''ejercicio 9:'''
agenda = {}

dia = input('dia ')
hora = input('hora ')
evento = input('evento ')

agenda[(dia, hora)] = evento

consulta_dia = input('dia a consultar ')
consulta_hora = input('hora a consultar ')

clave = (consulta_dia, consulta_hora)

if clave in agenda:
    print(agenda[clave])
else:
    print('no hay evento')

'''ejercicio 10:'''
paises = {'argentina': 'buenos aires', 'chile': 'santiago', 'uruguay': 'montevideo'}

invertido = {}

for pais in paises:
    cap = paises[pais]
    invertido[cap] = pais

print(invertido)

