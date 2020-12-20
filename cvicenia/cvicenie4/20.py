a = [1, 2, 5, 10, 20, 50, 100]
n = int(input('zadaj cislo:'))

for i in reversed(a):
    x = n//i
    if x > 0:
        print(f'{x} krát hodnota {i}')
    n = n % i
