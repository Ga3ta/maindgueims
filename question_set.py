import chemistry_set,orthography_set,physics_set,math_set

def var_answers(set):
    data_a=[]
    if set==1:
        data_a = [1, 2, 3]
    elif set==2:
        data_a = [1, 2, 3]
    elif set==3:
        data_a=chemistry_set.element_variables()
        return data_a
    elif set==4:
        data_a = math_set.new_quadratic()
        return data_a
    else:
        data_a=[1,2,3]
    return data_a