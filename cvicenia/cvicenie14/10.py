class Zoznam:
    def __init__(self):
        self.zoznam = []

    def pridaj(self, prvok):
        if prvok not in self.zoznam:
            self.zoznam.append(prvok)

    def vyhod(self, prvok):
        if prvok in self.zoznam:
            zoznam.pop(self.zoznam.index(prvok))

    def je_v_zozname(self, prvok):
        return prvok in self.zoznam

    def vypis(self):
        s = "zoznam: "
        for c in self.zoznam:
            s += c + ' '
        print(s)


moj = Zoznam()
moj.pridaj('upratat')
moj.pridaj('behat')
moj.pridaj('ucit sa')
if moj.je_v_zozname('behat'):
    print('musis behat')
else:
    print('nebehaj')
moj.pridaj('upratat')
moj.vyhod('spievat')
moj.vypis()
