n = int(input('zadaj n: '))
for i in range(0, n):
    print(f'{(n-i)*" "}{i*"*"}*{i*"*"}{(n-i)*" "}')
