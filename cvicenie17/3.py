# def desatinne(n):
#     n = n.lstrip()
#     n = n.rstrip()
#     if n.count('.') > 1:
#         return False
#     for i in n:
#         if i not in '1234567890.':
#             return False
#     return True


def desatinne(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


# print(desatinne('123'))
# print(desatinne('  22.7 '))
# print(desatinne('22/7'))
