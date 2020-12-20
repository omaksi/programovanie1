

def vypis_recept(zoznam):
    print('\n'.join(list((' '.join(str(vec)
                                   for vec in zoznam[i:i+3])) for i in range(0, len(zoznam), 3))))


# recept = ['cukor', 100, 'g', 'vajíčka', 5, 'ks', 'mlieko', 2, 'dcl']
# vypis_recept(recept)
