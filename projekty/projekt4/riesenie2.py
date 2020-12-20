
def vypis(meno_suboru, sirka, zarovnat=True, slovo=''):

    subor = open(meno_suboru, 'r')
    text = subor.read()
    subor.close()

    def niejePrazdny(str):
        return True if str != '' else False

    odseky = list(filter(niejePrazdny, text.split('\n\n')))

    def obsahujeSlovo(odsek):
        return True if slovo in odsek else False

    if slovo != '':
        odseky = list(filter(obsahujeSlovo, odseky))

    def parseSlovo(odsek):
        return list(filter(niejePrazdny, odsek.replace('\n', ' ').split(' ')))

    odsekySlova = list(map(parseSlovo, odseky))

    def vlozMedzeryAkoTreba(a, x):
        x += len(a) - 1
        if (zarovnat == True):
            i = 0
            while x > 0:
                a[i] += ' '
                i = i + 1 if i < len(a) - 2 else 0
                x -= 1
            return ''.join(a)
        return ' '.join(a)

    for odsek in odsekySlova:
        sirkaRiadku = 0
        riadok = []
        for slovo in odsek:
            if len(riadok) == 0:
                riadok.append(slovo)
                sirkaRiadku += len(slovo)
            elif (len(slovo) + 1 + sirkaRiadku) <= sirka:
                riadok.append(slovo)
                sirkaRiadku += len(slovo) + 1
            else:
                riadokSMedzerami = vlozMedzeryAkoTreba(
                    riadok, sirka - sirkaRiadku)
                print(riadokSMedzerami)
                sirkaRiadku = len(slovo)
                riadok = [slovo]
        print(' '.join(riadok))
        print('')


# vypis('subor1.txt', 20)
# vypis('subor1.txt', 60)
# vypis('subor1.txt', 45, False)
# vypis('subor1.txt', 45, True, 'kvety')
# vypis('subor1.txt', 30, True, 'a')
# vypis('subor3.txt', 10)
# vypis('subor3.txt', 99)
# vypis('subor3.txt', 10)
# vypis('subor1.txt', 3)
# vypis('subor2.txt', 10)
