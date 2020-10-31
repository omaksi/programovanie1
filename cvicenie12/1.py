def mocnina(n, k):
    return 1 if k == 0 else n * mocnina(n, k-1)


# print(mocnina(2, 900) == 2**900)
