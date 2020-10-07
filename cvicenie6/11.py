def riadky(s):
    s = s.split('\n')
    for i in range(len(s)):
        print(f'{i+1}. {s[i]}')


riadky('prvy riadok\n\ntreti je posledny')
