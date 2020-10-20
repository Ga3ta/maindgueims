from random import randint

def get_palabra():
    file = open("assets/diccionario.txt", "r", encoding='utf-8')
    palabras = file.read().split("\n")
    rand = randint(0, len(palabras)-1)
    palabra=palabras[rand].split(",")
    size = len(palabra)//2
    rand2 = randint(0, size-1)
    correct = palabra[rand2]
    description = palabra[rand2+size]
    bank = palabra[:size]
    return(correct, description, bank)