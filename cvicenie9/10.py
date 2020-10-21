def prerob(cislo):
    sC = str(cislo)
    a = []
    for i in range(len(sC), 0, -3):
        a.insert(0, sC[:i] if (i-3) < 0 else sC[i-3:i])
    return ('_'.join(a))


# print(prerob(12345678))
