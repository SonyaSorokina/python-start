def task_1(L):
    m = L.count(L[0])
    for i in L:
        if (L.count(i)>m):
            m = L.count(i)
            answ = i
    return answ

def task_2(L1, L2):
    n = 8
    cor = True
    for i in range(n):
        for j in range(i + 1, n):
            if L1[i] == L1[j] or L2[i] == L2[j] or  abs(L1[i] - L1[j]) == abs(L2[i] - L2[j]):
                cor = False
        if cor:
            return 'NO'
        else:
            return 'YES'

def task_3(x, y, xc, yc, r):
    flag = True
    if ((x - xc) * (x - xc) + (y - yc) * (y - yc) <= r*r):
        flag = True
    else:
        flag = False
    return flag

def task_4(L):
    answ = 0
    for i in range(1, len(L)-1):
        if ((L[i] > L[i + 1]) and (L[i] > L[i - 1])):
            answ = answ + 1
    return answ

alf = 'abcdefghijklmnopqrstuvwxyz'
def task_5(key):
    f = open('file.txt', 'r')
    rez = ''
    answ = []
    for line in f:
        line = line.lower().strip()
        for i in line:
            position = alf.find(i)
            new_position = position + key
            rez = rez + alf[new_position]
        answ.append(rez)
        rez = ''
    return answ