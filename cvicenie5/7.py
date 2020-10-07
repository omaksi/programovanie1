def vyhod_medzery(text):
    res = ''
    for i in text:
        if i != ' ':
            res += i
    print(res)


vyhod_medzery('  mám   rád Python ')
vyhod_medzery('      ')
vyhod_medzery('a  a  b  c')
