pi = 3.141592653589793

a1 = 223 / 71
a2 = (22/17) + (37/47) + (88/83)
a3 = (99**2) / (2206 * (2**(1/2)))
a4 = ((((5**(1/2)) + 6) ** (1/2))+7)**(1/2)
a5 = ((10 ** 100) / 11222.11122) ** (1/193)


def countdiff(n):
    return abs(pi - n)


values = [a1, a2, a3, a4, a5]
diffs = list(map(countdiff, values))
smallest = min(diffs)
smallestIndex = diffs.index(smallest)
print('a' + str(smallestIndex+1) + ' = ' + str(smallest))
