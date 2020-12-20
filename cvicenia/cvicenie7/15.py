def vyrob(meno_suboru, pocet, text):
    with open(f'./{meno_suboru}', 'w') as f:
        for i in range(pocet):
            f.write(f'print(\'{text}\')\n')


vyrob('skript.py', 20, 'Programujem v Pythone')
