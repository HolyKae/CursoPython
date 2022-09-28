import datetime
a = int(input('Em que ano você nasceu? '))
h = datetime.datetime.now()
i = h.year - a
if i <= 9:
    print('MIRIM')
elif i <= 14:
    print('INFANTIL')
elif i <= 19:
    print('JUNIOR')
elif i > 20:
    print('MASTER')
else:
    print('SENIOR')
