'''
Importamos el módulo random para generar preguntas aleatorias
'''
import random

'''
Aquí abrimos el archivo que contiene todos los elementos de la tabla periódica con número y símbolo
para después generar una lista de diccionarios que contengan estos tres atributos de cada elemento
'''
def openfile():
    file = open("assets/Tp.txt", "r", encoding='utf-8')
    data=[]

    for line in file:
        e = line.split(",")
        data.append({"name": e[0], "symbol": e[1], "number": int(e[2])})
    file.close()
    return data

'''
Esta función regresa las variables necesarias para el juego en una lista data_q, estas
variables son símbolo, número y nombre del elemento correcto y el nombre de otros tres elementos
'''
def element_variables():
    data_q=[]
    data=openfile()
    random_num=int(random.randrange(0,117))
    data_q.append(data[random_num]["symbol"])
    data_q.append(data[random_num]["number"])
    data_q.append(data[random_num]["name"])
    data_q.append(data[random.randrange(0, 117)]["name"])
    data_q.append(data[random.randrange(0, 117)]["name"])


    return data_q
