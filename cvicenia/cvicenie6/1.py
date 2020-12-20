x, y = 'Bratislava', 'Košice'
print(y[1] + x[4] + y[3] + x[-4] + y[-5])
print(x[5:8] + 3 * x[3] + y[2:])
print(y[:2] + x[-2:])
print(x[1::2] + y[2::2] + x[2::3])
print(x.replace('a', 'e') + y.replace('ic', 'm'))
print((y + x).replace('i', '').replace('a', 'xa'))
