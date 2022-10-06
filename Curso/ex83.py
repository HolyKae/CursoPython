e = input('Digite uma expressão: ')
li = list(e)
print(li)
print(li.count('('))
if li.count('(') == li.count(')'):
    print('A expressão é válida.')
else:
    print('A lista é inválida.')
