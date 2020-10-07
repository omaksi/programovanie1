def male(s, i):
    return s[:i] + s[i].lower() + s[i + 1:]


def velke(s, i):
    return s[:i] + s[i].capitalize() + s[i + 1:]


print(male('PYTHON', 3))
print(velke('python', 5))
