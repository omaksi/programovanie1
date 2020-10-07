def fibonacci(n):
    a, b = 0, 1
    while n:
        a, b = b, a+b
        n -= 1
    return a


def fib_medzi(od, do):
    n = 1
    res = ''
    lastF = 0
    while lastF < do:
        lastF = fibonacci(n)
        if lastF > od and lastF < do:
            res += str(lastF) + ' '
        n += 1

    print(res)


fib_medzi(10, 100)
fib_medzi(1000, 3000)
