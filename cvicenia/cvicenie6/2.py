def sucet(retazec):
    return sum(map(int, retazec.split('+')))


print(sucet('12+9'))
print(sucet('987654321+99999'))
