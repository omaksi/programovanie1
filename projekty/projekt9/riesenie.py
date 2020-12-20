# 9. zadanie: sudoku
# autor: Ondrej Makši
# datum: 1.12.2020

class Sudoku:
    def __init__(self, meno_suboru):
        self.tab = []
        s = open(meno_suboru)
        riadky = s.read().split('\n')
        s.close()
        for i in range(9):
            t = []
            for j in riadky[i].split(' '):
                if j == '.':
                    t.append(j)
                else:
                    t.append(int(j))
            self.tab.append(t)

    def __str__(self):
        res = []
        for i in self.tab:
            sub = []
            for j in i:
                if type(j) == set:
                    sub.append('.')
                else:
                    sub.append(str(j))
            res.append(" ".join(sub))
        return "\n".join(res)

    def urob(self):
        res = 0
        frozenTab = []
        for i in self.tab:
            frozenTab.append(i[:])

        for iI, i in enumerate(frozenTab):
            for iJ, j in enumerate(i):
                if j == '.':
                    # print(iI, iJ)
                    row = i[:]
                    # print('r', row)

                    column = []
                    for k in frozenTab:
                        column.append(k[iJ])
                    # print('c', column)

                    sector = []
                    for k in range((iI // 3) * 3, ((iI // 3) * 3) + 3):
                        for l in range((iJ // 3) * 3, ((iJ // 3) * 3) + 3):
                            sector.append(frozenTab[k][l])
                    # print('s', sector)

                    relevantFieldsSet = set()
                    for k in row+column+sector:
                        if k != '.':
                            relevantFieldsSet.add(k)
                    options = set(range(1, 10)) - relevantFieldsSet
                    # print(options)
                    if len(options) == 0:
                        return -1
                    if len(options) == 1:
                        res += 1
                    self.tab[iI][iJ] = options
        return res

    def nahrad(self):
        for iI, i in enumerate(self.tab):
            for iJ, j in enumerate(i):
                if type(j) == set:
                    if len(j) == 1:
                        self.tab[iI][iJ] = list(j)[0]
                    else:
                        self.tab[iI][iJ] = '.'

    def ries(self):
        n = 1
        while n > 0:
            n = self.urob()
            self.nahrad()
            if n == -1:
                return -1
        return self.pocet_nezaplnenych()

    def pocet_nezaplnenych(self):
        res = 0
        for i in self.tab:
            res += i.count('.')
        return res


# s = Sudoku('subor1.txt')
# print(0)

# print(s)
# print(s.pocet_nezaplnenych())
# print(s.urob())
# # for r in s.tab:
# #     print(r)
# s.nahrad()
# print(1)
# print(s)
# print(s.urob())
# s.nahrad()
# print(2)

# # # print(s)
# s = Sudoku('subor2.txt')
# # print(s.ries())
# print(s.urob())
# print(s)
# print(s.urob())
# print(s)
# print(s.urob())
# print(s)
# print(s.urob())
# print(s)
# print(s.urob())
# print(s)
# print(s.urob())
# print(s)
# print(s.urob())
# print(s)
# print(s.urob())
# print(s)
# print(s.urob())
# print(s)
# print(s.urob())
# print(s)
