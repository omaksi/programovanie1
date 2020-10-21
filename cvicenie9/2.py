def vyhod_none(ntica):
    return tuple(filter(lambda x: x is not None, ntica))


def vyhod_none(ntica):
    return tuple(x for x in ntica if x is not None)


# print(vyhod_none((None, 1, None, None)))
