def obdlznik(sirka, znak='*'):
    print(sirka * znak)
    print(znak + (sirka-2) * ' ' + znak)
    print(sirka * znak)


obdlznik(30, '#')
obdlznik(6)
obdlznik(19, 'O')
