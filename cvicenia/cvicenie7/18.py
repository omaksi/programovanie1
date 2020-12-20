def pridaj(meno_suboru, text):
    with open(f'./{meno_suboru}', 'a') as f:
        f.write(f'{text}\n')


pridaj('subor.txt', 'predposledný')
pridaj('subor.txt', 'posledný riadok')
