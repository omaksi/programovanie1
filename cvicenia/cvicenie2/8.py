n = int(input('zadaj n: '))

a = ''
for i in range(1, n+1):
    a += i * '*'
    a += ' '

print(f'{a}')
