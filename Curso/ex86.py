n = [[], [], []]
i = 0
u = 1
for c in range(1, 10):
    num = int(input(f'Digite o {u}º número da {i+1}ª coluna: '))
    n[i].append(num)
    if c % 3 == 0:
        u = 1
        if c != 8:
            i += 1
    else:
        u += 1
print(f'Matriz:\n[{n[0][0]}][{n[0][1]}][{n[0][2]}]\n'
               f'[{n[1][0]}][{n[1][1]}][{n[1][2]}]\n'
               f'[{n[2][0]}][{n[2][1]}][{n[2][2]}]\n')
