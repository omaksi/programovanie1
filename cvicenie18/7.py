def mnozina1(n):
    m1 = set(range(0, n+1, 3))
    m2 = set(range(6, n+1, 5))
    m3 = set(range(7, n+1, 5))
    return m1 & m2 | m1 & m3


def mnozina2(n1, n2):
    m = mnozina1(n2)
    n = set(range(n1))
    return m - n


# print(mnozina1(21))
# print(mnozina2(20, 100))
