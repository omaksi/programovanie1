def sucet(post):
    try:
        typ = type(post[0])
        suma = typ()
        for i in post:
            try:
                suma += i
            except TypeError:
                try:
                    suma += typ(i)
                except (ValueError, TypeError):
                    pass
    except IndexError:
        return None
    return suma


# print(sucet([2, '3', 4.0, 'päť']))

# print(sucet(['1', 2, 0.3, 'abc']))

# print(sucet([[1, 2], 3, '4x']))

# print(sucet([(1, 2), (3, 4), [5]]))

# print(sucet([]))     # pre prázdnu postupnosť
