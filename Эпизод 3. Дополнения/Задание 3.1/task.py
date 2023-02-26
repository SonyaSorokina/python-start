from math import*
def task_1(text):
    s = text.rstrip('.').split('.')
    D = {i.strip(): len(i.strip().split(' ')) for i in s}
    return D

def task_2(x1, y1, x2, y2):
    answ = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return answ