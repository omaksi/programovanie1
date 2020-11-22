def iba_cisla(meno_suboru):
    try:
        s = open(meno_suboru).read()
        a = []
        t = ""
        for i in s:
            if i in '1234567890-.':
                t += i
            elif len(t) != 0:
                a.append(t)
                t = ""

        # print(a)

        res = []
        for i in a:
            if i.count('.') == 0:
                try:
                    res.append(int(i))
                except (ValueError, TypeError):
                    pass
        return res

    except FileNotFoundError:
        return []


# print(iba_cisla('xx.txt'))
print(iba_cisla('subor.txt'))
