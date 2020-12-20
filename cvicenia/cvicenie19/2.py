zoo = {
    'lev': 190,
    'tiger': 300,
    'hyena': 50,
    'gorila': 160,
    'zirafa': 800,
    'simpanz': 50,
    'hroch': 1500,
    'medved': 300,
    'buvol': 590,
    'antilopa': 200,
    'pyton': 90,
    'slon': 5000,
    'gibon': 10,
    'jaguar': 120,
    'jelen': 280,
    'kengura': 80,
}


def tazsie_ako(zviera):
    res = {}
    for i in zoo:
        if zoo[i] > zoo[zviera]:
            print(i)
            # res[i] = zoo[i]
    # return res


def vyber_lahsie(zviera):
    res = {}
    for i in zoo:
        if zoo[i] < zoo[zviera]:
            # print(i)
            res[i] = zoo[i]
    return res


# tazsie_ako('zirafa')
# print(vyber_lahsie('pyton'))
