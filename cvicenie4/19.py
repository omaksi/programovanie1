import random
n = int(input('začínam so sumou: '))
t = 0
res = ''
while n > 0 and t < 1000:
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    c = random.randint(1, 20)
    if a == b and b == c and a == c:
        n += 100
        res += '+100'
    elif a == b or b == c or a == c:
        n += 5
        res += '+5'
    else:
        n -= 1
        res += '-1'
    t += 1

print(f'štart {res}')
print(f'zostalo mi {n} euro')
