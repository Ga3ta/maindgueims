'''
Del módulo random, importamos la función randint para nuestro generador
'''
from random import randint
'''
Creamos una tupla que indica el tipo de vehículo del problema
'''
vehiculos = ('tren', 'barco', 'auto')

'''
Creamos una función que de manera aleatoria crea un problema que involucra
velocidad, tiempo y distancia con valores aleatorios y regresa el enunciado
del problema que se extrae de un txt, el tipo de vehículo y la respuesta
'''
def get_prob(): 
    file = open("assets/problemasv.txt", "r", encoding='utf-8')
    a = randint(1,3)
    v = randint(0,2)
    for i in range (a):
        e = file.readline()
        e = e.split("\n")[0]
    if a==1:
        b = randint(1,10)*10
        c = randint(1, 20)*10
    else:
        b = randint(1, 10)*10
        c = randint(1,5)
    if a==1:
        ans = round(c/b, 2)
    elif a ==2:
        ans = round(b/c, 2)
    else:
        ans = float(b*c)
    file.close()
    e=e.format(vehiculos[v], b, c)
    p = e.split(',')[0]
    q = e.split(',')[1]
    return[v, p, q, ans]