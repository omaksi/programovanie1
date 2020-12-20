filename = input()

with open(f'./{filename}', 'r') as f:
    count = 0
    length = 0
    r = f.readline()
    while r != '':
        count += 1
        length = len(r) if len(r) > length else length
        r = f.readline()

    print(f'počet riadkov súboru: {count}')
    print(f'najdlhší riadok má {length} znakov')

with open(f'./{filename}', 'r') as f:
    count = 0
    length = 0
    for r in f:
        count += 1
        length = len(r) if len(r) > length else length

    print(f'počet riadkov súboru: {count}')
    print(f'najdlhší riadok má {length} znakov')

with open(f'./{filename}', 'r') as f:
    content = f.read()
    count = 0
    length = 0
    n = content.find('\n')
    while n != -1:
        count += 1
        length = n+1 if n+1 > length else length
        content = content[n+1:]
        n = content.find('\n')

    print(f'počet riadkov súboru: {count}')
    print(f'najdlhší riadok má {length} znakov')
