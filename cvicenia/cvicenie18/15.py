# import itertools


def vsetky(prvky):
    # return sorted(list(map(lambda x: set(x), itertools.combinations(prvky, 2))))
    res = []
    for i in prvky:
        for j in prvky:
            if i != j and res.count(set([i, j])) == 0:
                res.append(set([i, j]))
    return sorted(res)


# print(vsetky(set('java')))
# print(vsetky(set(range(5))))
# print(vsetky({3, 1, 'x', 4, 1, 2, 'x'}))
# print(vsetky({'python'}))
