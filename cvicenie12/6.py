def sucet2(zoznam):
    if len(zoznam) == 0:
        return (0, 0)
    if len(zoznam) == 1:
        if zoznam[0] < 0:
            return (zoznam[0], 0)
        else:
            return (0, zoznam[0])
    stred = len(zoznam) // 2
    prva = sucet2(zoznam[:stred])
    druha = sucet2(zoznam[stred:])
    return (prva[0]+druha[0], prva[1]+druha[1])


# print(sucet2([0, 1, -2, 3, 4, -5, -6, 7]))
# print(sucet2(list(range(100)) + list(range(0, -100, -1))))
# print(sucet2([0]*1000+[1]+[0]*1000+[-1]+[0]*1000))
