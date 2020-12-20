# 8. zadanie: stvorce
# autor: Ondrej Makši
# datum: 20.11.2020

class Stvorce:

    def __init__(self, n):
        self.n = n
        self.d = 2**n
        self.a = []
        for i in range(self.d):
            self.a.append([0] * self.d)
        # print(self.n)
        # print(self.d)
        # print(self.a)

    def getCoords(self, quadrant, n, xstart, xend, ystart, yend):
        # print('getCoords', quadrant, n, xstart, xend, ystart, yend)
        q = 0
        if len(quadrant) > 0:
            q = int(quadrant[0])
        else:
            return (xstart, xend, ystart, yend)

        d = 2**n
        # half = d / 2
        # print('d', d)
        # print('half', half)
        if q == 1:
            return self.getCoords(quadrant[1:], n - 1, xstart,
                                  xend - (d//2), ystart, yend - (d//2))
        elif q == 2:
            return self.getCoords(quadrant[1:], n - 1, xstart + (d//2),
                                  xend, ystart, yend - (d//2))
        elif q == 3:
            return self.getCoords(quadrant[1:], n - 1, xstart,
                                  xend - (d//2), ystart + (d//2), yend)
        elif q == 4:
            return self.getCoords(quadrant[1:], n - 1, xstart + (d//2),
                                  xend, ystart + (d//2), yend)

    def urob(self, index):

        if len(index) > self.n:
            return
        # print(index)
        coords = self.getCoords(index, self.n, 0, self.d, 0, self.d)
        # print(coords)
        for i in range(coords[0], coords[1]):
            for j in range(coords[2], coords[3]):
                self.a[i][j] = 1 - self.a[i][j]

    def pocet(self):
        zeros = 0
        ones = 0
        for i in range(self.d):
            for j in range(self.d):
                if self.a[i][j] == 0:
                    zeros += 1
                if self.a[i][j] == 1:
                    ones += 1
        return (zeros, ones)

    def vypis(self):
        for i in range(self.d):
            p = ""
            for j in range(self.d):
                if (self.a[j][i] == 0):
                    p += "-"
                else:
                    p += "X"
            print(p)


# stv = Stvorce(3)
# # stv.vypis()
# stv.urob('2233')
# stv.vypis()

# print('pocet', stv.pocet())
# stv.urob('23')
# stv.vypis()
# print('pocet', stv.pocet())
# stv.urob('2')
# stv.urob('3')
# print('pocet', stv.pocet())
# stv.vypis()

# testa = ['1', '11', '131', '1314', '143', '12', '1233', '1234', '1243', '1244', '23', '234',
#          '2133', '2134', '2143', '2144', '24', '242', '2423', '31', '313', '3132', '32', '324',
#          '3232', '3411', '3412', '3421', '3422', '4', '44', '424', '4241', '413', '4141', '43',
#          '4311', '4312', '4321', '4322']
# testa = ['14', '141', '1412', '1431', '124', '1241', '2', '21', '22', '24', '213', '2113',
#          '2143', '2324', '2433', '3', '31', '3142', '3211', '343', '3441', '3443', '33',
#          '332', '3321', '41', '4213', '4231', '4232', '43', '434', '441', '4423']
# testa = ['2', '23224', '2411', '24123', '24131', '24132', '2422', '24223', '2444', '24441',
#          '212', '21412', '21421', '21422', '211', '2113', '21132', '21143', '22', '2233',
#          '2234', '22342', '14', '14111', '14113', '1433', '14332', '132', '1322', '13223',
#          '134', '1344', '13441', '1312', '13142', '13144', '13322', '13324', '1334', '1134',
#          '11341', '11333', '11334', '11433', '1224', '12243', '12344', '124', '1241', '12421',
#          '12423', '12431', '3112', '31123', '31111', '31112', '31211', '32122', '322', '3223',
#          '32213', '3224', '32242', '411', '412', '4124', '41241', '41234', '4211', '42121',
#          '42122', '42211', '4131', '413114', '41321']

# stv = Stvorce(6)
# for i in testa:
#     stv.urob(i)
# stv.vypis()
