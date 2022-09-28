import datetime
a = int(input('Em que ano você nasceu? '))
h = datetime.datetime.now()
i = h.year - a
if i <= 17:
    print(f'Ainda vai se alistar.\nFaltam {18-i} anos.')
elif i > 18:
    print(f'Já passou do tempo de alistamento.\nPassaram {i-18} anos do prazo.')
else:
    print('Está na hora de se alistar!')
