import random


def hadanie(od, do):
    n = random.randint(od, do)
    for i in range(0, 11):
        x = int(input('tvoj tip: '))
        if x < n:
            print('pridaj')
        elif x > n:
            print('uber')
        else:
            print(f'Uhádol si na {i}. pokus. Gratulujem.')
            return
    print(f'Neuhádol si ani na 10 pokusov.')
    print(f'Myslel som si číslo {n}.')


hadanie(1, 500)
