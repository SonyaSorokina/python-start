from math import*
def task_1(N):
    n = 5
    x = factorial(n)
    return x


def task_2(N):
    a = 0
    b = 1
    n = 7
    for i in range(3, n+1):
        c = a + b
        a = b
        b = c
    return b


def task_3(N):
    n = 100
    l = [1, n]
    for i in range(2, 1 + int(n ** 0.5)):
        if n%i ==0:
            l.extend({n //  i, i})
    return sorted(l)
