class Paska:
    def __init__(self, obsah=''):
        self.paska = list(obsah or '_')
        self.poz = 0

    def symbol(self):
        return self.paska[self.poz]

    def zmen_symbol(self, znak):
        self.paska[self.poz] = znak

    def __str__(self):
        return ''.join(self.paska) + '\n' + ' '*self.poz + '^'

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


class Turing:
    def __init__(self, program, obsah='', start=None, koniec={'end', 'stop'}):
        self.program = {}
        self.stav = start
        for riadok in program.split('\n'):
            riadok = riadok.split()
            if len(riadok) == 5:
                stav1, znak1, znak2, smer, stav2 = riadok
                self.program[stav1, znak1] = znak2, smer, stav2
                if self.stav is None:
                    self.stav = stav1
        self.paska = Paska(obsah)
        self.koniec = koniec

    def __str__(self):
        return str(self.paska) + ' ' + self.stav

    def krok(self):
        stav1, znak1 = self.stav, self.paska.symbol
        try:
            znak2, smer, stav2 = self.program[stav1, znak1]
        except KeyError:
            return False
        self.paska.symbol = znak2
        self.stav = stav2
        if smer == '>':
            self.paska.vpravo()
        elif smer == '<':
            self.paska.vlavo()
        return True

    def rob(self, vypis=True):
        if vypis:
            print(self)
        while self.stav not in self.koniec:
            if not self.krok():
                return False
            if vypis:
                print(self)
        return True


prog = '''
parny x x > neparny
neparny x x > parny
neparny _ _ = end
'''
print(Turing(prog, 'xxxxx').rob(False))
print(Turing(prog, 'x').rob(False))
print(Turing(prog, 'xx').rob(False))

print(Turing(prog, 'xx' * 5).rob(False))
