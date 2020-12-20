
def vypis(zoznam, pocet):
    print('\n'.join(list((' '.join(str(vec)
                                   for vec in zoznam[i:i+pocet])) for i in range(0, len(zoznam), pocet))))

# recept = ['cukor', 100, 'g', 'vajíčka', 5, 'ks', 'mlieko', 2, 'dcl']
# zoz = list(range(1, 19))


# vypis(recept, 3)
# vypis(zoz, 4)
# vypis(list('Python'), 2)
