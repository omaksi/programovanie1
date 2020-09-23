w = input('zadaj slovo: ')
n = int(input('zadaj n: '))

for i in range(0, n):
    print(f'{i % 4*4*" "}{w}')
