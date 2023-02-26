def task_1(str):
    # A = list(str)
    # B = list()
    # D = dict()
    # for i in A:
    #     if (i not in B) and (i!=' '):
    #         B.append(i)
    # for i in B:
    #     key = i
    #     value = A.count(i)
    #     D[key] = value]

    D = dict()
    for i in str:
        if i.isalpha():
            if i.lower() in D:
                D[i.lower()] += 1
            else:
                D[i.lower()] = 1
    return D


def task_2(list):
    A = set(list)
    return sum(A)


def task_3(cities):
    s = ''
    for i in cities:
        s = s + i + ', '
    s1 = s[:len(s)-2:]
    return s1 + '.'


def task_4(a, b):
    A = set(a)
    B = set(b)
    C = A.intersection(B)
    c = list(C)
    return c
