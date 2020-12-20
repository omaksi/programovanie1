# 10. zadanie: pajton
# autor: Ondrej Maksi
# datum: 26.11.2020

class Pajton:
    def __init__(self):
        self.tab = {}

    def prem(self, meno):
        if meno in self.tab:
            return self.tab[meno]
        raise NameError

    def akJePremVratPrem(self, meno):
        m = meno.strip()
        if m.count(' ') > 0:
            raise SyntaxError
        if not (m[0].isdigit() or m[0] == '-'):
            return int(self.prem(m))
        return int(m)

    def aritmetikaPodlaZnaku(self, retazec, znak, funkcia):
        c = list(map(self.akJePremVratPrem, retazec.split(znak)))
        return funkcia(c)

    def vyraz(self, retazec):
        if type(retazec) is int:
            return retazec
        if retazec.count(' + ') == 1:
            return self.aritmetikaPodlaZnaku(retazec, ' + ', lambda c: c[0] + c[1])
        if retazec.count(' - ') == 1:
            return self.aritmetikaPodlaZnaku(retazec, ' - ', lambda c: c[0] - c[1])
        if retazec.count(' * ') == 1:
            return self.aritmetikaPodlaZnaku(retazec, ' * ', lambda c: c[0] * c[1])
        if retazec.count(' / ') == 1:
            return self.aritmetikaPodlaZnaku(retazec, ' / ', lambda c: c[0] // c[1])

        return self.akJePremVratPrem(retazec)

    def prirad(self, meno, hodnota):
        if meno[0].isdigit():
            raise SyntaxError
        for i in meno:
            if not (i.isalnum() or i == '_'):
                raise SyntaxError
        self.tab[meno] = self.vyraz(hodnota)

    def prikaz(self, retazec):
        if retazec == '':
            return
        if retazec == '?':
            self.vypis()
            return
        if retazec == 'dir()':
            return self.dir()
        if retazec.count(' = ') == 1:
            priradenie = retazec.split(' = ')
            self.prirad(priradenie[0].strip(), priradenie[1].strip())
            # print(self.tab)
            return None
        return self.vyraz(retazec)

    def dir(self):
        return set(self.tab.keys())

    def vypis(self):
        for meno, hodnota in self.tab:
            print(meno, '=', hodnota)


# if __name__ == '__main__':
#     p = Pajton()
#     while True:
#         try:
#             hodn = p.prikaz(input('>>> '))
#             if hodn is not None:
#                 print(hodn)
#         except SyntaxError:
#             print('+++ syntakticka chyba +++')
#         except NameError:
#             print('+++ chybne meno premennej +++')
p = Pajton()
p.prem('_ ')
