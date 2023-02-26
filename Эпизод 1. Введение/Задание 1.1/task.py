from math import*
# Пример 1
def task_1(a, d, c):
    answ = (c-(d/5)+sqrt(321))/(1+ a*3)
    return answ


# Пример 2
def task_2(a, d, c):
    answ = (log10(c/3)-d+25)/(a*5 - 1)
    return answ


# Пример 3
def task_3(a, d, c):
    answ = (c/2 + log(d) - 35)/(a*5 + 1)
    return answ


# Пример 4
def task_4(a, d, c):
    answ = (tan(c) + (d/32)) / ((a/3)+1)
    return answ


# Пример 5
def task_5(a, d, c):
    answ = ((c/5)-d + 1)/(c + tan(2*a))
    return answ


# Пример 6
def task_6(a, d, c):
    answ = (sqrt(25*c) + d -3)/(d - a * a + 1)
    return answ


# Пример 7
def task_7(a, d, c):
    answ = (5*log10(c)+ 3*d -32)/(a*a + 1)
    return answ


# Пример 8
def task_8(a, d, c):
    answ = (c*d - log(4*3*a))/(c+a-1)
    return answ
