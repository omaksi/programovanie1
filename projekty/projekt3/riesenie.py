# 3. zadanie: kalendár
# autor: Ondrej Makši
# datum: 10.10.2020

def pocet_dni_v_mesiaci(mesiac, priestupny=False):
    m = mesiac[:3]
    # print('pocet_dni_v_mesiaci', mesiac, m)
    if m == 'jan' or m == 'mar' or m == 'maj' or m == 'jul' or m == 'aug' or m == 'okt' or m == 'dec':
        return 31
    if m == 'apr' or m == 'jun' or m == 'sep' or m == 'nov':
        return 30
    if priestupny == True:
        return 29
    return 28


months = 'janfebmaraprmajjunjulaugsepoktnovdec'


def pocet_dni_medzi(datum1, datum2):
    m1 = int((months.find(datum1[:-5][:3])) / 3)
    m2 = int((months.find(datum2[:-5][:3])) / 3)
    y1 = int(datum1[-4:])
    y2 = int(datum2[-4:])

    # print(m1, m2, y1, y2)

    if (y1 - y2) == 0:
        days = 0
        for i in range(m1, m2):
            days += pocet_dni_v_mesiaci(months[3*i:(3*i)+3], not bool(y1 % 4))
        return days

    if (y1 - y2) == 1:
        days = 0
        for i in range(m1, 12):
            days += pocet_dni_v_mesiaci(months[3*i:(3*i)+3], not bool(y1 % 4))
        for i in range(0, m2):
            days += pocet_dni_v_mesiaci(months[3*i:(3*i)+3], not bool(y2 % 4))
        return days

    days = 0
    for i in range(m1, 12):
        days += pocet_dni_v_mesiaci(months[3*i:(3*i)+3], not bool(y1 % 4))
    for i in range(0, m2):
        days += pocet_dni_v_mesiaci(months[3*i:(3*i)+3], not bool(y2 % 4))

    for i in range(y1+1, y2):
        if i % 4 == 0:
            days += 366
        else:
            days += 365
    return days


# print(pocet_dni_medzi('sep.2020', 'okt.2020'))
# print(pocet_dni_medzi('okt.2019', 'okt.2020'))
# print(pocet_dni_medzi('januar.1999', 'oktober.2020'))


dni_v_tyzdni = "utostrstvpiasobnedpon"


def den_v_tyzdni(datum):  # 'den.mesiac.rok' # 'pon', 'uto', 'str', 'stv', 'pia', 'sob', 'ned'
    d = int(datum[:datum.find('.')])
    m = datum[datum.find('.')+1:-5][:3]
    y = int(datum[-4:])

    # print(d, m, y)

    # 1.január.1901 utorok

    days = (d - 1)

    for i in range(0, int((months.find(m)) / 3)):
        days += pocet_dni_v_mesiaci(months[3*i:(3*i) + 3], not bool(y % 4))

    for i in range(1901, y):
        if i % 4 == 0:
            days += 366
        else:
            days += 365

    res = dni_v_tyzdni[(days % 7) * 3:((days % 7) + 1) * 3]

    return res


# print(den_v_tyzdni('8.oktober.2020'))
# print(den_v_tyzdni('1.jan.1901'))
# print(den_v_tyzdni('23.jun.1912'))
# print(den_v_tyzdni('23.jun.1912'))
