from random import randint
from math import sqrt

def new_quadratic():
    values=[]
    a = float(randint(-5, 5))
    while(a==0):
        a = float(randint(-5, 5))
    b = float(randint(-10, 10))
    c = float(randint(-20, 20))
    d = b**2-4*a*c
    a = int(a)
    b = int(b)
    c = int(c)
    if(d<0):
        values=[a, b, c,["No hay soluciones"], -1]
        return values
    elif(d==0):
        values=[a,b,c,[round(-b/(2*a), 2)], 0]
        return values
    else:
        values=[a,b,c,[round(-b-sqrt(d)/(2*a), 2),round(-b+sqrt(d)/(2*a), 2)], 1]
        return values