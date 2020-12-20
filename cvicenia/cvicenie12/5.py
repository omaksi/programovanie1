def sucet(zoznam):
    if len(zoznam) == 0:
        return 0
    if len(zoznam) == 1:
        return zoznam[0]
    stred = len(zoznam) // 2
    prva = sucet(zoznam[:stred])
    druha = sucet(zoznam[stred:])
    return druha + prva


# print(sucet([2, 4, 6, 8, 1]))
# print(sucet([]))
# print(sucet(list(range(2000))))
