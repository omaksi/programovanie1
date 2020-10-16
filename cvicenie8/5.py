def najdlhsie(zoznam):
    return sorted(zoznam, key=lambda x: len(x))[-1]


# zoz = ['prvy', 'druhy', 'treti', 'stvrty', 'piaty']
# print(najdlhsie(zoz))
