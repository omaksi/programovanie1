# 5. zadanie: najcastejsie
# autor: Ondrej Makši
# datum: 23.10.2020

tab = []


def citaj(meno_suboru):
    with open(meno_suboru, 'r') as subor:
        slova = list(filter(lambda x: x != '',
                            subor.read().replace('\n', ' ').split(' ')))
        pocet = []
        while len(slova) > 0:
            pocet.append((slova[0], slova.count(slova[0])))
            slova = list(filter(lambda x: x != slova[0], slova))
        tab.extend(pocet)


def pocet_vyskytov(slovo):
    filtered = list(filter(lambda x: x[0] == slovo, tab))
    if len(filtered) == 0:
        return 0
    return filtered[0][1]


def najcastejsie():
    zoradene = sorted(tab, reverse=True, key=lambda x: x[1])
    return s_poctom(zoradene[0][1])


def s_poctom(n):
    return tuple(x[0] for x in filter(lambda x: x[1] == n, tab))


def najdlhsie():
    zoradene = sorted(tab, reverse=True, key=lambda x: len(x[0]))
    return s_dlzkou(len(zoradene[0][0]))


def najkratsie():
    zoradene = sorted(tab, key=lambda x: len(x[0]))
    return s_dlzkou(len(zoradene[0][0]))


def s_dlzkou(n):
    return tuple(x[0] for x in filter(lambda x: len(x[0]) == n, tab))


# citaj('text1.txt')
# print('pocet vyskytov "the":', pocet_vyskytov('the'))
# print('najcastejsie:', najcastejsie())
# print('najdlhsie:', najdlhsie())
# print('najkratsie:', najkratsie())
# print('len s poctom 5:', s_poctom(5))
# print('len s poctom 10:', s_poctom(10))
# print('len s dlzkou 10:', s_dlzkou(10))
# print('pocet roznych slov =', len(tab))
