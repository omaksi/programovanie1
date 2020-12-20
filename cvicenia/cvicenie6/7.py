def vyhod_duplikaty(retazec):
    res = retazec[0]
    for i in range(1, len(retazec)):
        if retazec[i] != retazec[i-1]:
            res += retazec[i]
    print(res)


vyhod_duplikaty('Braatisssllavaaaaa')
