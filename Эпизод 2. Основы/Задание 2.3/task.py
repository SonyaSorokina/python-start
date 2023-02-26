# todo: replace this with an actual task
def task_1(str):
    A = list()
    A = str.split()
    return len(A[len(A)-1])


def task_2(str):
    A = list()
    A = str.split()
    for i in range(0, len(A) - 1, 2):
        A[i], A[i + 1] = A[i + 1], A[i]
    return " ".join(A)


def task_3(str):
    A = list()
    A = str.split()
    i = 1
    c = 1
    for i in range(len(A)-1):
        s = list(A[i])
        s2 = list(A[i-1])
        if (s[0]) == (s2[len(s2)-1]):
            c = c+1
    return c
