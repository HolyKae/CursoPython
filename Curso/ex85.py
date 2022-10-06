n = [[], []]
for i in range(7):
    num = int(input(f'Digite o {i + 1}º número: '))
    if num % 2 == 0:
        n[0].append(num)
    elif num % 2 == 1:
        n[1].append(num)
n[0].sort()
n[1].sort()
print(f'Pares:\n{n[0]}\nÍmpares:\n{n[1]}')
