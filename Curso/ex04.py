n = input('Digite algo: ')
print(type(n))
if n.isalpha():
    print('É alfabetico')
else:
    if n.isnumeric():
        print('É numerico')
if n.isalpha(): print('É alfanumerico')
if n.isprintable(): print('É printavel')
if n.isupper(): print('Está em maiusculas')
if n.islower(): print('Está em minusculas')
if n.istitle(): print('Está capitalizada')
