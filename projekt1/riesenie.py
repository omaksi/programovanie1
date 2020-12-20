# 1. zadanie: retazec
# autor: Ondrej Maksi
# datum: 25.9.2020

a = input('?')
print(f'dlzka = {len(a)}')

rev = ''
for i in reversed(a):
    rev += i

print(f'prevrat = {rev}')

for i in a:
    r = ''
    s = ''
    for j in a:
        r += j + ' * '
        s += '* ' + j + ' '
    print(r)
    print(s)

# print(f'prevrat = {"".join(reversed(a))}')

# for i in range(len(a)*2):
#     r = ''
#     for j in range(len(a)):
#         if i % 2 == 0:
#             r += a[j] + ' * '
#         else:
#             r += '* ' + a[j] + ' '
#     print(r)
