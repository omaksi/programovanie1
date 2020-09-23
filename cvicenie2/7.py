n = input('zadaj n: ')

a = 0
for i in range(0, len(n)):
    print(f'cifra {n[i]}')
    a += int(n[i])
print(f'ciferny sucet je {a}')
