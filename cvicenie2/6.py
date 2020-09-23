n = int(input('zadaj n: '))
for i in range(0, n-1):
    if i == 0:
        print(f'{(n-1)*" "}*{(n-1)*" "}')
    if i == n - 2:
        print(((2*n) - 1)*'*')
    else:
        print(f'{(n-i-2)*" "}*{(i)*"-"}-{(i)*"-"}*{(n-i-1)*" "}')
