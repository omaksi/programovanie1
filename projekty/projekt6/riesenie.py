# 6. zadanie: logo
# autor: Ondrej Makši
# datum: 30.10.2020

def preloz(meno_suboru, tab=4):

    unaryCommands = ['pu', 'pd']
    pyUnaryCommands = ['t.pu()', 't.pd()']

    binaryCommands = ['fd',  'rt', 'lt',  'setpc', 'setpw']
    pyBinaryCommands = ['t.fd', 't.rt', 't.lt', 't.pencolor', 't.pensize']

    subor = open("./"+meno_suboru, 'r')
    text = list(subor.read())
    subor.close()

    # print(text)
    text2 = []
    for i in text:
        if i == '[' or i == ']':
            text2.append(' ')
            text2.append(i)
            text2.append(' ')
        else:
            text2.append(i)
    # print(text2)

    a = list(filter(lambda x: x != '', ''.join(
        text2).replace('\n', ' ').split(' ')))

    # print(a)
    result = "import turtle\nt = turtle.Turtle()\n"

    tabs = 0
    pointer = 0
    while pointer < len(a):
        line = ""
        line += tabs * tab * ' '
        if a[pointer] in unaryCommands:
            line += pyUnaryCommands[unaryCommands.index(a[pointer])]
            line += '\n'
            result += line
            pointer += 1
            continue
        if a[pointer] in binaryCommands:
            line += pyBinaryCommands[binaryCommands.index(a[pointer])]
            line += f'({a[pointer+1]})'
            line += '\n'
            result += line
            pointer += 2
            continue
        if a[pointer] == '[':
            tabs += 1
            pointer += 1
            continue
        if a[pointer] == ']':
            tabs -= 1
            pointer += 1
            continue
        if a[pointer] == 'repeat':
            line += f'for _ in range({a[pointer+1]}):'
            line += '\n'
            result += line
            pointer += 2
            continue
        pointer += 1

    result += "turtle.mainloop()"

    subor = open("./"+meno_suboru.replace('.txt', '.py'), 'w')
    subor.write(result)
    subor.close()

    # print(result)


# preloz('subor2.txt')
