def len_raz(retazec):
    vsetky = set(retazec)
    viac = set()
    for i in vsetky:
        if retazec.count(i) > 1:
            viac.add(i)
    return vsetky - viac


# print(len_raz('anicka dusicka kde si bola'))

# print(len_raz('mama ma emu a ema ma mamu'))
