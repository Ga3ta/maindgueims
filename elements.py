from random import randint

file = open("assets/Tp.txt", "r")
elements=[]
for line in file:
    e=line.split(",")
    elements.append({"name": e[0], "symbol": e[1], "number": int(e[2])})

def random_element():
    return elements[randint(0, len(elements)-1)]

