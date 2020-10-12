import random

def throw_questions():
    file = open("assets/Tp.txt", "r")
    question_data = []

    for line in file:
        e = line.split(",")
        question_data.append({"name": e[0], "symbol": e[1], "number": int(e[2])})

    big_var= question_data[38]["symbol"]
    lil_var = question_data[38]["number"]
    name_var = question_data[38]["name"]
    data=[big_var,lil_var,name_var]

    return data