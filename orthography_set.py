'''
Importamos la función randint del módulo random para nuestro generador
'''
from random import randint

'''
Con esta función, abrimos el archivo donde se encuentra el diccionario que usamos para
nuestros problemas y escogemos un set de palabras homófonas, seleccionamos una al azar
y regresamos la palabra correcta, su definición, y el resto de las palabras homófonas
'''
def get_word():
    file = open("assets/diccionario.txt", "r", encoding='utf-8')
    palabras = file.read().split("\n")
    rand = randint(0, len(palabras)-1)
    palabra=palabras[rand].split(",")
    size = len(palabra)//2
    rand2 = randint(0, size-1)
    correct = palabra[rand2]
    description = palabra[rand2+size]
    bank = palabra[:size]
    return[correct, description, bank]

