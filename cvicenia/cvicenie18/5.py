import time


class Cas:

    def __init__(self, hodiny=0, minuty=0, sekundy=0):
        self.sek = abs(3600*hodiny + 60*minuty + sekundy)

    def __str__(self):
        return f'{self.sek // 3600}:{self.sek // 60 % 60:02}:{self.sek % 60:02}'

    def __add__(self, iny):
        if type(iny) == int:
            return Cas(sekundy=self.sek+iny)
        if type(iny) == tuple:
            s = 0
            try:
                s += iny[0] * 3600
                s += iny[1] * 60
                s += iny[2]
            except IndexError:
                pass
            return Cas(sekundy=self.sek+s)
        return Cas(sekundy=self.sek+iny.sek)

    def __radd__(self, iny):
        if type(iny) == int:
            return Cas(sekundy=self.sek+iny)
        if type(iny) == tuple:
            s = 0
            try:
                s += iny[0] * 3600
                s += iny[1] * 60
                s += iny[2]
            except IndexError:
                pass
            return Cas(sekundy=self.sek+s)
        return Cas(sekundy=self.sek+iny.sek)

    def __sub__(self, iny):
        if type(iny) == int:
            return Cas(sekundy=self.sek-iny)
        return Cas(sekundy=self.sek-iny.sek)

    def __gt__(self, iny):
        return self.sek > iny.sek

    def __eq__(self, iny):
        return self.sek == iny.sek


def teraz():
    t = time.localtime()[3:6]
    return Cas(t[0], t[1], t[2])
    print(t)


# c = teraz()
# print(type(c))
# print(c)
# print(teraz())
# c = Cas(8, 10, 34)
# print(c)
# print(c + 640)
# print((1, 55) + c)
# print(c - 100)
