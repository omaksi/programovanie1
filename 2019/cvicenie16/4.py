class Ucet:
    def __init__(self, meno, suma=0):
        self._suma = suma
        self._meno = meno

    def __str__(self):
        return f'ucet {self._meno} -> {self._suma} euro'

    def stav(self):
        return self._suma

    def vklad(self, suma):
        self._suma += suma

    def vyber(self, suma):
        if suma > 0:
            if suma > self._suma:
                r = self._suma
                self._suma = 0
                return r
            else:
                self._suma -= suma
                return suma


class UcetHeslo(Ucet):
    def __init__(self, meno, heslo, suma=0):
        self._suma = suma
        self._meno = meno
        self._heslo = heslo

    def vklad(self, suma):
        # TODO: finish me
