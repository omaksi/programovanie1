def bez_parnych(mnozina):
    p = set()
    for i in mnozina:
        if type(i) == int and i % 2 == 0:
            p.add(i)
    mnozina -= p


a = {7, 6.0, '12', 4, 'python', 124}
bez_parnych(a)
print(a)
b = set(range(4, 100, 2))
bez_parnych(b)
print(b)
