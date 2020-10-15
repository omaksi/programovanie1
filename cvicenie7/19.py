def vyhod_riadok(meno_suboru, index):
    with open(f'./{meno_suboru}', 'r+') as f:
        b = ''
        c = 0
        for i in f:
            b = b + i if c != index else b
            c += 1
        f.seek(0)
        f.truncate()
        f.write(b)


vyhod_riadok('subor.txt', 1)
