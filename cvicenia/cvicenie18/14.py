# import itertools


def vsetky(a, b, c, d):
    # return list(map(lambda x: set(x), itertools.combinations([a, b, c, d], 2)))
    prvky = [a, b, c, d]
    res = []
    for i in prvky:
        for j in prvky:
            if i != j and res.count(set([i, j])) == 0:
                res.append(set([i, j]))
    return sorted(res)


print(vsetky(1, 2, 3, 4))
