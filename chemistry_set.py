import random

def openfile():
    file = open("assets/Tp.txt", "r", encoding='utf-8')
    data=[]

    for line in file:
        e = line.split(",")
        data.append({"name": e[0], "symbol": e[1], "number": int(e[2])})
    file.close()
    return data

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
