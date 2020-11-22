# import itertools


def kartez_sucin(m1, m2):
    # return sorted(set(itertools.product(m1, m2)))
    res = set()
    for i in m1:
        for j in m2:
            res.add((i, j))
    return res


print(kartez_sucin({1, 2, 3, 4}, {'a', 'b', 'c'}))
