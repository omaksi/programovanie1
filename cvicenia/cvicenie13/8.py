def pascalov_trojuholnik(n):
    a = []
    for i in range(n):
        if len(a) == 0:
            a.append([1])
        elif len(a) == 1:
            a.append([1, 1])
        else:
            b = [1]
            for j in range(len(a[-1]) - 1):
                b.append(a[-1][j] + a[-1][j+1])
            b.append(1)
            a.append(b)
    return a


print(pascalov_trojuholnik(10))
