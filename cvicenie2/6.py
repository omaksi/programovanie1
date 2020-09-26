n = int(input('zadaj n: '))

print(f'{(n-1)*" "}*{(n-1)*" "}')
for i in range(0, n-2):
    print(f'{(n-i-2)*" "}*{(i)*"-"}-{(i)*"-"}*{(n-i-1)*" "}')
print(((2*n) - 1)*'*')
