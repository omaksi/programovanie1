counter = 1
sum = 0
while True:
    x = float(input(f'Zadaj {counter}. číslo: '))
    if x == 0:
        print(f'súčet všetkých prečítaných čísel je {sum}')
        break
    sum += x
