import random

def throw_questions():
    file = open("assets/Tp.txt", "r")
    question_data = []

    for line in file:
        e = line.split(",")
        question_data.append({"name": e[0], "symbol": e[1], "number": int(e[2])})

    random_num=random.randrange(0,len(e))
    big_var= question_data[random_num]["symbol"]
    lil_var = question_data[random_num]["number"]
    name_var = question_data[random_num]["name"]
    data=[big_var,lil_var,name_var]

    return data