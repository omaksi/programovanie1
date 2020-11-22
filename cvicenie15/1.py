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


# obd1 = Obdlznik(20, 7)
# print('obvod =', obd1.obvod())
# # obvod = 54
# print(obd1)
# # Obdlznik(20, 7)
# obd2 = obd1.kopia()
# obd2.zmen_velkost(2)
# print(obd2)
# # Obdlznik(40, 14)
