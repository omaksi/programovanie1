def vsetky_rozne(postupnosť):
    return len(postupnosť) == len(set(postupnosť))


print(vsetky_rozne((2, 5, 7, 'x', 11, 13, 17, 19, 23, 'x', 29)))
