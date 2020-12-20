
def binary(n): return bin(n).replace("0b", "")


def dvojkova(cislo):
    return list(map(int, binary(cislo)))


# print(dvojkova(11213))
