def riadok(d, text=''):

    h1 = ((d - len(text) - 2) // 2)
    h2 = (h1 + ((d - len(text) - 2) % 2 > 0))
    print_text = f'{h1 * "*"} {text} {h2 * "*"}' if text != '' else d * '*'

    print(print_text)


sir = 40
riadok(sir)
riadok(sir, 'Ján Botto')
riadok(sir, 'Žltá ľalija')
riadok(sir, '-')
riadok(sir, 'Stojí stojí mohyla')
riadok(sir, 'Na mohyle zlá chvíľa')
riadok(sir, 'na mohyle tŕnie chrastie')
riadok(sir, 'a v tom tŕní chrastí rastie')
riadok(sir)
