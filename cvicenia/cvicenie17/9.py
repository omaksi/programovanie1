def sustavy(retazec):
    res = [None] * 17
    for i in range(17):
        try:
            res[i] = int(retazec, i)
        except ValueError:
            pass

    return res


# print(sustavy('11'))

# print(sustavy('1a1'))

# print(sustavy('FF'))

# print(sustavy('x'))
