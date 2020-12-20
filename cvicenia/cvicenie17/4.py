def zoznam(z):
    z = z.lstrip('[')
    z = z.rstrip(']')
    a = z.split(',')
    res = []
    for i in a:
        try:
            res.append(float(i))
        except ValueError:
            pass
    return res


# print(zoznam('[0, 1., 2, 3.14]'))
# print(zoznam('[0, -.1, None, +2, [7], a5, -3.14, "8"]'))
