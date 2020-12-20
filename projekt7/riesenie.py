# 7. zadanie: zoznamy
# autor: Ondrej Makši
# datum: 6.11.2020

def pocet_zoznamov(param):
    c = 1
    for i in param:
        if type(i) is list:
            c += pocet_zoznamov(i)
    return c

# def pocet_zoznamov(param): return sum([pocet_zoznamov(i) for i in param if type(i) is list]) + 1


def zoznam_prvkov(zoznam):
    r = []
    for i in zoznam:
        if type(i) is list:
            r.extend(zoznam_prvkov(i))
        else:
            r.append(i)
    return r


def splosti(zoznam):
    zoznam[:] = zoznam_prvkov(zoznam)


def nahradeny_zoznam(zoznam, hodnota1, hodnota2):
    r = []
    for i in zoznam:
        if i == hodnota1:
            r.append(hodnota2)
        elif type(i) is list:
            r.append(nahradeny_zoznam(i, hodnota1, hodnota2))
        else:
            r.append(i)
    return r


def nahrad(zoznam, hodnota1, hodnota2):
    zoznam[:] = nahradeny_zoznam(zoznam, hodnota1, hodnota2)


# def splosti(zoznam):
#     for i, el in enumerate(zoznam):
#         if type(el) is list:
#             splosti(el)
#             zoznam[i:i+1] = el


# def nahrad(zoznam, hodnota1, hodnota2):
#     for i, el in enumerate(zoznam):
#         if el == hodnota1:
#             zoznam[i] = hodnota2
#         elif type(el) is list:
#             nahrad(el, hodnota1, hodnota2)

# print(type([]) is list)
# print(pocet_zoznamov([1, 'a', 2]))
# print(pocet_zoznamov([[], 1, 'a', [3], 2]))
# print(pocet_zoznamov(['a', ['dom', [2], 3], [], [[[2]]], 'b']))


# print(zoznam_prvkov([1, 2, 3, [4, 5], 6, [[[7]]], [], 8]))
# print(zoznam_prvkov(['a', ['dom', [2], 3], [], [[[2]]], 'b']))
# print(zoznam_prvkov([[], [[[]]], []]))
# print(zoznam_prvkov([[], 1, 'a', 3, 2]))
# zoz = [[[7]], 8]
# print(zoznam_prvkov(zoz))
# print(zoz)


# zoz = [[[7]], 8]
# print(splosti(zoz))
# print(zoz)
# p = [1, 2, 3, [4, 5], 6, [[[7]]], [], 8]
# splosti(p)
# print(p)


# zoz = [[[7]], 8]
# print(nahradeny_zoznam(zoz, 7, 'a'))
# print(zoz)
# print(nahradeny_zoznam([1, 2, 3, [1, 2], 3, [[[1]]], [], 2], 1, 'x'))
# print(nahradeny_zoznam([3, [33, [333, [13], 13]], 36], 3, 'q'))
# print(nahradeny_zoznam([3, [33, [333, [13], 13]], 36], [13], 'm'))


# p = ['a', ['dom', [2], 3], [], [[[2]]], 'b']
# print(p)
# nahrad(p, 2, 'abc')
# print(p)
# assert p == ['a', ['dom', ['abc'], 3], [], [[['abc']]], 'b']


# zoz = [[[7]], 8]
# print(nahrad(zoz, 7, 'a'))
# print(zoz)
# assert zoz == [[['a']], 8]
# p = [1, 2, 3, [1, 2], 3, [[[1]]], [], 2]
# nahrad(p, 1, 'x')
# print(p)
# assert p == ['x', 2, 3, ['x', 2], 3, [[['x']]], [], 2]
# p = [1, 2, 3, [1, 2], 3, [[[1]]], [], 2]
# nahrad(p, 4, 'z')
# print(p)
# assert p == [1, 2, 3, [1, 2], 3, [[[1]]], [], 2]
