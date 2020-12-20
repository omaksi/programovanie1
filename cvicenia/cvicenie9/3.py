import random


def throw(): return sum([random.randint(1, 6), random.randint(1, 6)])


def dve_kocky(pocet):
    res = [0] * 13
    for i in range(pocet):
        res[throw()] += 1
    return res


# print(dve_kocky(1000))
