def stvorec(n, znak):
    return '' + (n*znak + '\n') + ((n-2) * (znak + ((n-2)*' ') + znak + '\n')) + (n*znak + '\n')


print(stvorec(5, '#'))
