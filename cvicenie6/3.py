def sucet(retazec):
    return sum(map(int, retazec.split('+')))


print(sucet('12+9'))
print(sucet('1+2+3+4'))
print(sucet('1234'))
