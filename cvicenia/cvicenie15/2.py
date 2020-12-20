class TelefonnyZoznam:
    def __init__(self, meno_suboru):
        self.cisla = []
        self.meno_suboru = meno_suboru

    def pridaj(self, meno, telefon):
        for i, el in enumerate(self.cisla):
            if el[0] == meno:
                self.cisla[i] = (meno, telefon)
                return
        self.cisla.append((meno, telefon))

    def vypis(self):
        for c in self.cisla:
            print(f'{c[0]} {c[1]}')
