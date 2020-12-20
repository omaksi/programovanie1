n = int(input('zadaj číslo: '))
cs = 0
while n > 0:
    cs += n % 10
    n = n//10
print(f'ciferný súčet = {cs}')
