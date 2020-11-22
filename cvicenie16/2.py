class Zviera:
    def __init__(self, meno):
        self._meno = meno.capitalize()

    def __str__(self):
        return f'zviera {self._typ} má meno {self._meno} a robí {self._zvuk}'

    def daj_zvuk(self):
        return self._zvuk

    def daj_typ(self):
        return self._typ

    def daj_meno(self):
        return self._meno

    def zmen_meno(self, meno):
        self._meno = meno.capitalize()

    def zmen_zvuk(self, zvuk):
        if (zvuk.count('-') > 0):
            self._zvuk += '-' + zvuk
        else:
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
