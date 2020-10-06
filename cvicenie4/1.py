n = float(input('zadaj km pre prvý deň: '))
f = float(input('zadaj cieľové km: '))
counter = 0
while n < f:
    counter += 1
    n = (n*1.1)
print(f'na {counter}. deň prebehne {round(n, 2)} km')
 