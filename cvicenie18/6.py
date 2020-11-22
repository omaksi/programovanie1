
class Cas:

    def __init__(self, hodiny=0, minuty=0, sekundy=0):
        self.sek = abs(3600*hodiny + 60*minuty + sekundy)

    def __str__(self):
        return f'{self.sek // 3600}:{self.sek // 60 % 60:02}:{self.sek % 60:02}'

    __repr__ = __str__

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

    def __lt__(self, iny):
        return self.sek < iny.sek

    def __eq__(self, iny):
        return self.sek == iny.sek


# zoznam = [Cas(20, 15), Cas(7), Cas(11), Cas(11, 1, 1), Cas(11, 0, 1)]

# zoznam1 = sorted(zoznam)

# print(zoznam1)
