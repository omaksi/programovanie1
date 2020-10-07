def rozsekaj(text, sirka):
    while len(text) > 0:
        print(text[:sirka])
        text = text[sirka:]


rozsekaj('Anicka dusicka, kde si bola', 10)
