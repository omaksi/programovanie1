def nsd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def nsn(a, b):
    n = int(a * b / nsd(a, b))
    print(f'nsn({a}, {b}) =', n)


nsn(129, 162)
nsn(60, 168)
