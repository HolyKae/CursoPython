e = list(input('Digite uma expressão: '))
c = 0
v = True
if e.count('(') != e.count(')'):
    print('A expressão é inválida.')
if e.count('(') == e.count(')'):
    for i in range(len(e)):
        if '(' in e[i]:
            if ')' not in e[i:]:
                v = False
    if not v:
        print('A expressão é inválida.')
    else:
        print('A expressão é válida.')
