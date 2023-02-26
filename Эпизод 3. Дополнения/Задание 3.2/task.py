def task_1(L, x):
    return str(L.index(x))

def task_2(x):
    answ = True
    for i in range(1, x):
        if ((x%i==0) and ((i!=x) and (i!=1))):
            answ = False
    return answ