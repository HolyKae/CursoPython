p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 0
m = 10
while c != m:
    c += 1
    print(p + (c * r), end=' ')
    if c == m:
        print('')
        m += int(input('Quer mais quantos termos? '))
