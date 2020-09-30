counter = 1
vysky = []
print('zadávaj výšky žiakov')
while True:
    x = input(f'výška {counter}. žiaka: ')
    counter += 1
    if x == '':
        for i in range(1, len(vysky)):
            if vysky[i] <= vysky[i-1]:
                print('žiaci nie sú správne zoradení')
                exit()

        print('žiaci sú správne zoradení')
        break
    vysky.append(float(x))
