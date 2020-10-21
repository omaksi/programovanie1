import random


def nahodne_body(pocet):
    return [(random.randint(0, 380), random.randint(0, 260)) for x in range(pocet)]


print(nahodne_body(5))
