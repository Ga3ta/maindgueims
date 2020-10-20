from random import randint
vehiculos = ('tren', 'barco', 'auto')
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
        ans = b*c
    file.close()
    e=e.format(vehiculos[v], b, c)
    p = e.split(',')[0]
    q = e.split(',')[1]
    print({"problema": p, "pregunta": q, "respuesta": ans})
    return({"problema": p, "pregunta": q, "respuesta": ans})
get_prob()