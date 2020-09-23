class Cas:
    def __init__(self, hodiny, minuty):
        self.hodiny = hodiny
        self.minuty = minuty

    def vypis(self):
        print('cas je ' + str(self.hodiny) + ':' + str(self.minuty).zfill(2))

    def str(self):
        return str(self.hodiny) + ':' + str(self.minuty).zfill(2)

    def pridaj(self, hodiny, minuty):
        self.minuty = int(self.minuty)+int(minuty)
        self.hodiny = (int(self.hodiny)+int(hodiny) % 24) + self.minuty // 60
        self.minuty = self.minuty % 60


# c = Cas(9, 17)
# c.vypis()
d = Cas(10, 50)
d.vypis()
d.pridaj(1, 20)
d.vypis()
