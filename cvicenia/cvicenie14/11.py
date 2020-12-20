class TelefonnyZoznam:
    def __init__(self):
        self.cisla = []

    def pridaj(self, meno, telefon):
        for i, el in enumerate(self.cisla):
            if el[0] == meno:
                self.cisla[i] = (meno, telefon)
                return
        self.cisla.append((meno, telefon))

    def vypis(self):
        for c in self.cisla:
            print(f'{c[0]} {c[1]}')


# tz = TelefonnyZoznam()
# tz.pridaj('Jana', '0901020304')
# tz.pridaj('Juro', '0911111111')
# tz.pridaj('Jozo', '0212345678')
# tz.pridaj('Jana', '0999020304')
# tz.vypis()
