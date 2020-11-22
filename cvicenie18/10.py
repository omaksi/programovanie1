def rozdel(mnozina):
    n = set()
    s = set()
    for i in mnozina:
        if type(i) == str:
            s.add(i)
        else:
            n.add(i)
    return (n, s)


# print(rozdel({7, 7.5, '12', 3, 'python'}))
