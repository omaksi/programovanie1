def riadok(d, t=''):
    print(f'{((d - len(t) - 2) // 2) * "*"} {t} {(((d - len(t) - 2) // 2) + ((d - len(t) - 2) % 2 > 0)) * "*"}' if t != '' else d * '*')


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
