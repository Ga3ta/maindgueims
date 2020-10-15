import random

def openfile():
    file = open("assets/Tp.txt", "r", encoding='utf-8')
    data=[]

    for line in file:
        e = line.split(",")
        data.append({"name": e[0], "symbol": e[1], "number": int(e[2])})
    file.close()
    return data

def throw_questions():
    data=openfile()
    random_num=random.randrange(0,117)
    big_var= data[random_num]["symbol"]
    lil_var = data[random_num]["number"]
    name_var = data[random_num]["name"]
    random_num = random.randrange(0, 117)
    ans1_var= data[random_num]["name"]
    random_num = random.randrange(0, 117)
    ans2_var = data[random_num]["name"]
    random_num = random.randrange(0, 117)
    ans3_var = data[random_num]["name"]
    data_q=[big_var,lil_var,name_var]
    return data_q

def throw_answers():
    data=openfile()
    random_num = random.randrange(0, 117)
    ans1_var= data[random_num]["name"]
    random_num = random.randrange(0, 117)
    ans2_var = data[random_num]["name"]
    random_num = random.randrange(0, 117)
    ans3_var = data[random_num]["name"]
    data_a=[ans1_var,ans2_var,ans3_var]
    return data_a