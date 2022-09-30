s = c = 0
n = 0
while 999 != n:
    n = int(input('Digite um número [999 para parar]: '))
    s += n
    c += 1
print(f'Foram inseridos {c} números\nA soma deles é {s}')
