class Cas:
    def __init__(self, hodiny, minuty):
        self.hodiny = hodiny
        self.minuty = minuty

    def vypis(self):
        print('cas je ' + str(self.hodiny) + ':' + str(self.minuty).zfill(2))


c = Cas(9, 17)
c.vypis()
d = Cas(10, 5)
d.vypis()
