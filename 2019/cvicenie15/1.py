class Obdlznik:

    def __init__(self, a, b):
        # inicializuje
        self.a = a
        self.b = b

    def __str__(self):
        # vráti reťazec v tvare 'Obdlznik(100, 70)'
        return f'Obdlznik({self.a}, {self.b})'

    def obsah(self):
        # vráti obsah
        return self.a * self.b

    def obvod(self):
        # vráti obvod
        return (2*self.a) + (2*self.b)

    def zmen_velkost(self, pomer):
        # vynásobí obe veľkosti strán zadaným pomerom
        self.a *= pomer
        self.b *= pomer

    def kopia(self):
        # vyrobí kópiu samého seba
        return Obdlznik(self.a, self.b)
