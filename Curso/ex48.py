n = int(input('Digite um número: '))
t = 0
for c in range(1, n+1):
    if c % 2 == 1 and c % 3 == 0:
        t += c
print(t)


