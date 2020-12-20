def max(*cisla):
    if not cisla or len(cisla) == 0:
        raise TypeError

    if type(cisla[0]) is list or type(cisla[0]) is set or type(cisla[0]) is tuple:
        a = list(reversed(sorted(list(cisla[0]))))
    else:
        a = list(reversed(sorted(list(cisla))))
    return a[0]


print(max(9, 13, 11))
print(max(*'python'))
# print(max())
print(max((3, 'a'), (3, 'b'), (2, 'x')))
