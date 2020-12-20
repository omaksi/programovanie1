def mocnina(n, k):
    if k == 0:
        return 1
    elif k % 2 == 0:
        return mocnina(n, k//2) ** 2
    else:
        return mocnina(n, k-1) * n


# print(mocnina(2, 10000) == 2**10000)
