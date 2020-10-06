def riadok(dlzka, text=''):

    if text == '':
        print(dlzka * '*')
        return
    text_dlzka = len(text)
    hviezdicky = int((dlzka - text_dlzka - 2) / 2) * '*'
    print_text = hviezdicky + ' ' + text + ' ' + hviezdicky
    if len(print_text) < dlzka:
        print_text += '*'

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
