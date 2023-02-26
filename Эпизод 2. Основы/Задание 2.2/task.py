from math import*
# Пример 1
def task_1(A):
    s = 0
    for i in A:
        if i>0:
            s = s + i
    return s


# Пример 2
def task_2(A):
    s = 0
    for i in A:
        s = s + i
    return s/len(A)


# Пример 3
def task_3(A):
    s = 0
    for i in A:
        s = s + i
    sr = s/len(A)
    B = list()
    for i in A:
        j = i - sr
        B.append(j)
    s2=0
    for i in B:
        s2 = s2 + (i**2)
    return sqrt(s2/len(B))
