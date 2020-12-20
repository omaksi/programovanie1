class Zviera:
    def __init__(self, meno):
        self.meno = meno.capitalize()

    def __str__(self):
        return f'zviera {self.typ} má meno {self.meno} a robí {self.zvuk}'


class Pes(Zviera):
    typ = 'pes'
    zvuk = 'haf-haf'


class Macka(Zviera):
    typ = 'mačka'
    zvuk = 'mnau-mnau'


class Kacka(Zviera):
    typ = 'kačka'
    zvuk = 'ga-ga'


z1 = Pes('dunčo')
z2 = Macka('mica')
z3 = Pes('bono')
z4 = Kacka('gréta')
z3.zvuk = 'vrr-vrr'
for z in z1, z2, z3, z4:
    print(z)
