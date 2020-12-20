
def a(x, m):
    assert type(x) == int and x > -1 and x < 256, m


def rgb(r, g, b):
    a(r, "chybny prvy parameter r")
    a(g, "chybny druhy parameter g")
    a(b, "chybny treti parameter b")
    return f'#{r:02x}{g:02x}{b:02x}'


# print(rgb(100, 150, 20.0))


# print(rgb(100, 350, 20.0))


# print(rgb('100', 350, 20.0))


# print(rgb(100, 150, 200))
