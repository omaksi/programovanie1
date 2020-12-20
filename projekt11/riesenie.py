# 11. zadanie: turing
# autor: Ondrej Maksi
# datum: 5.12.2020
class Turing:
    def __init__(self, program, obsah=''):
        self.program = {}
        self.koniec = {'end', 'stop'}
        self.stav = None
        self.paska = list(obsah or '_')
        self.poz = 0

        riadky = program.split('\n')
        riadky = map(lambda x: x.split(), riadky)
        riadky = filter(lambda x: len(x) != 0, riadky)
        riadky = list(riadky)

        stavy = riadky.pop(0)
        # self.stav = stavy[0]
        hodnoty = []

        for riadok in riadky:
            hodnoty.append(riadok.pop(0))

        # print('stavy', stavy)
        # print('hodnoty', hodnoty)
        # print('tabulka', riadky)

        prvyPrikaz = len(riadky[0])
        for ri, riadok in enumerate(riadky):
            for si, stlpec in enumerate(riadok):
                if stlpec == '.':
                    continue
                stav1 = stavy[si]
                znak1 = hodnoty[ri]
                pravidlo = self.parsujPravidlo(stlpec)
                znak2 = znak1 if not pravidlo[0] else pravidlo[0]
                smer = pravidlo[1]
                stav2 = stav1 if not pravidlo[2] else pravidlo[2]
                # print('parsujem', stav1, znak1, znak2, smer, stav2)
                # stav1, znak1, znak2, smer, stav2 = riadok
                self.program[stav1, znak1] = znak2, smer, stav2
                if self.stav is None or si < prvyPrikaz:
                    prvyPrikaz = si
                    self.stav = stav1

    # PASKA
    def symbol(self):
        return self.paska[self.poz]

    def zmen_symbol(self, znak):
        self.paska[self.poz] = znak

    def vpravo(self):
        self.poz += 1
        if self.poz == len(self.paska):
            self.paska.append('_')

    def vlavo(self):
        if self.poz > 0:
            self.poz -= 1
        else:
            self.paska.insert(0, '_')

    def text(self):
        return ''.join(self.paska).strip('_')

    symbol = property(symbol, zmen_symbol)
    text = property(text)

    # END PASKA

    def parsujPravidlo(self, pravidlo):
        if pravidlo.count('=') == 1:
            pravidlo = pravidlo.split('=')
            return [pravidlo[0], '=', pravidlo[1]]
        if pravidlo.count('<') == 1:
            pravidlo = pravidlo.split('<')
            return [pravidlo[0], '<', pravidlo[1]]
        if pravidlo.count('>') == 1:
            pravidlo = pravidlo.split('>')
            return [pravidlo[0], '>', pravidlo[1]]

    def __str__(self):
        return ''.join(self.paska) + '\n' + ' '*self.poz + '^' + ' ' + self.stav

    def krok(self):
        stav1, znak1 = self.stav, self.symbol
        try:
            znak2, smer, stav2 = self.program[stav1, znak1]
        except KeyError:
            return False
        self.symbol = znak2
        self.stav = stav2
        if smer == '>':
            self.vpravo()
        elif smer == '<':
            self.vlavo()
        return True

    def rob(self, n=None):
        counter = 0
        # print(self.stav, self.paska, self.poz)
        # print(self)
        while self.stav not in self.koniec:
            if n and counter == n:
                return (False, counter)
            if not self.krok():
                return (False, counter)
            counter = counter + 1
            # print(self)
        return (True, counter)

    def restart(self, stav=None, obsah=None, n=None):
        if stav:
            self.stav = stav
        if obsah != None:
            self.paska = list(obsah or '_')
            self.poz = 0
        return self.rob(n)
        # od noveho stavu (ak nie je None), s novou paskou (ak nie je None) a zavola rob()
        return False, 0


# if __name__ == '__main__':
#     prog = '''
#         s1    s2
#     0    >    1=end
#     1    >    0<
#     _   <s2   1=end
#     '''
#     t = Turing(prog, '1011')
#     # print(t.program)
#     # print(t.rob())
#     # print('vysledok =', t.text)
#     # print(t.restart('s1', '10102010'))
#     # print(t.restart('s1', '1011', 7))
#     print(t.restart('s1', '10102010'))
if __name__ == '__main__':
    # prog = '''
    #    s0   s1   s2   s3   s4   s5   s6   s7
    # 0   .    .    .    >    .    .    .   1>s3
    # 1  <s1   .    .    >    >  _<s6   <   0<
    # _   .   <s2  0>s3 >s4  <s5  <end <s7  1>s3
    # '''
    prog = '''
       s0 s1 s2 s3 s4 s5 s6 s7
     0 . . . > . . . 1>s3
     1 <s1 . . > > _<s6 < 0<
     _ . <s2 0>s3 >s4 <s5 <end <s7 1>s3
     '''
    t = Turing(prog, '1111111111111111111111')
    print(t.rob())
    # print(t.program)
    # print('vysledok =', t.text)
    # print(t.restart('s1', '10102010'))
    # print(t.restart('s1', '1011', 7))
