import random


def nahodne_cisla(meno_suboru, pocet):
    with open(f'./{meno_suboru}', 'w') as f:
        for i in range(pocet):
            f.write(str(random.randint(100, 999)) + '\n')
