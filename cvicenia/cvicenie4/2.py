n = int(input('zadaj číslo: '))
s = f'{n}, '

while n != 1:
    if n % 2 == 0:
        n /= 2
        s += f'{int(n)}, '

        continue
    else:
        n = (n*3)+1
        s += f'{int(n)}, '

print(s)
