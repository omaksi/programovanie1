# 4. zadanie: zarovnaj
# autor: Ondrej Makši
# datum: 16.10.2020

def vypis(meno_suboru, sirka, zarovnat=True, slovo=''):

    with open(meno_suboru, 'r') as subor:

        # parsovanie vstupu do odsekov
        a = [[]]
        for riadok in subor:
            riadok = riadok.replace('\n', '')
            if (riadok.isspace() or len(riadok) == 0) and len(a[-1]) > 0:
                a.append([])
            else:
                x = [i for i in riadok.split(
                    ' ') if not i.isspace() and not i == '']
                a[-1].extend(x)
        if (a[-1] == []):
            a.pop()

        # print(a)
        # exit()
        # riešenie parametra slovo
        if slovo != '':
            b = []
            for i in a:
                for j in i:
                    if slovo == j:
                        b.append(i)
                        break
            a = b

        # print(a)
        # formátovanie na šírku
        buffer = []
        for odsek in a:
            newOdsek = []
            newRiadokLen = 0
            for slovo in odsek:
                # print(slovo)
                # if sirka > len(slovo):

                if sirka + 1 - newRiadokLen >= len(slovo) + 1:
                    if (newRiadokLen == 0):
                        newOdsek.append([])
                    newOdsek[-1].append(slovo)
                    newRiadokLen += 1 + len(slovo)
                else:
                    newOdsek.append([])
                    newOdsek[-1].append(slovo)
                    newRiadokLen = 1 + len(slovo)
                # else:
                #     for chunkIndex in range(0, len(slovo), sirka):
                #         chunk = slovo[chunkIndex:chunkIndex+sirka]
                #         # print(chunk)
                #         newOdsek.append([])
                #         newOdsek[-1].append(chunk)
                #         newRiadokLen = 0

            buffer.append(newOdsek)
        # print(buffer)
        # riešenie zarovnania
        buffer2 = []
        if zarovnat:
            for odsek in buffer:
                for riadok in odsek:
                    # print(riadok)
                    if len(riadok) == 1:
                        # riadok[0] += (sirka - len(riadok[0])) * ' '
                        buffer2.append(riadok)
                        # print(riadok)
                        continue

                    if riadok == odsek[-1]:
                        for i in range(len(riadok) - 1):
                            riadok[i] += ' '
                        buffer2.append(riadok)
                        # print(riadok)
                        continue
                    dlzka_slov = 0
                    # print(riadok)
                    for slovo in riadok:
                        dlzka_slov += len(slovo)
                    # print(dlzka_slov)
                    pocet_medzier_na_rozdelenie = sirka - dlzka_slov
                    pocet_miest_medzi_slovami = len(riadok) - 1
                    while pocet_medzier_na_rozdelenie > 0:
                        for i in range(pocet_miest_medzi_slovami):
                            if(pocet_medzier_na_rozdelenie > 0):
                                riadok[i] += ' '
                                pocet_medzier_na_rozdelenie -= 1
                            else:
                                break
                    buffer2.append(riadok)
                    # print(riadok)
                if odsek != buffer[-1]:
                    buffer2.append([''])
            # print(buffer2)
            # print('\n'.join(list(map(lambda riadok: ''.join(riadok), buffer2))))
            for riadok in buffer2:
                print(''.join(riadok))

        else:
            for odsek in buffer:
                for riadok in odsek:
                    buffer2.append(' '.join(riadok))
                if odsek != buffer[-1]:
                    buffer2.append('')
            # print(buffer2)
            for riadok in buffer2:
                print(riadok)


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
