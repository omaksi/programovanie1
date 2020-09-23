class Zviera:
    def __init__(self, meno):
        self._meno = meno.capitalize()

    def __str__(self):
        return f'zviera {self._typ} má meno {self._meno} a robí {self._zvuk}'

    def daj_meno(self):
        return self._meno

    def daj_typ(self):
        return self._typ

    def daj_zvuk(self):
        return self._zvuk

    def zmen_typ(self, typ):
        self._typ = typ

    def zmen_zvuk(self, zvuk):
        self._zvuk = zvuk


class Pes(Zviera):
    _typ = 'pes'
    _zvuk = 'haf-haf'


class Macka(Zviera):
    _typ = 'mačka'
    _zvuk = 'mnau-mnau'


class Kacka(Zviera):
    _typ = 'kačka'
    _zvuk = 'ga-ga'


z1 = Pes('dunčo')
z2 = Macka('mica')
z3 = Pes('bono')
z4 = Kacka('gréta')
z3._zvuk = 'vrr-vrr'
for z in z1, z2, z3, z4:
    print(z)

z3.zmen_zvuk('vrr')
z3.daj_zvuk()
print(z3)

z4.zmen_zvuk('GA-GA')
z4.daj_zvuk()
print(z4)
