s = open('skladatelia.txt')
skladatelia = {}

for i in map(lambda x: x.split(' '), s.read().split('\n')):
    skladatelia[i[0]] = i[1]

s.close()

print()