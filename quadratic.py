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
    if(d<0):
        print("No")
        return("No hay soluciones")
    elif(d==0):
        print(-b/(2*a))
        values=[a,b,c,(-b/(2*a)),0]
        return values
    else:
        print([(-b-sqrt(d)/(2*a)), (-b+sqrt(d)/(2*a))])
        values=[a,b,c,(-b-sqrt(d)/(2*a)), (-b+sqrt(d)/(2*a))]
        return values