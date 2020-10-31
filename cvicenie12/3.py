def palindrom(str):
    str = str.replace(' ', '')
    str = str.lower()
    if str[0] == str[-1]:
        if len(str) > 2:
            return palindrom(str[1:len(str)-1])
        else:
            return True
    return False


# print(palindrom('Jelenovi Pivo Nelej'))
