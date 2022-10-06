n = [[], [], []]
i = 0
u = 0
sm = 0
col = 0
lin = 0
for c in range(1, 10):
    num = int(input(f'Digite o {u + 1}º número da {i + 1}ª linha: '))
    n[i].append(num)
    if u == 2:
        col += num
    if i == 1:
        if num > n[1][u-1] or lin == 0:
            lin = num
    if num % 2 == 0:
        sm += num
    if c % 3 == 0:
        u = 0
        if c != 8:
            i += 1
    else:
        u += 1
print(f'Matriz:\n[{n[0][0]}][{n[0][1]}][{n[0][2]}]\n'
               f'[{n[1][0]}][{n[1][1]}][{n[1][2]}]\n'
               f'[{n[2][0]}][{n[2][1]}][{n[2][2]}]\n')
print(f'Soma dos pares: {sm}\nSoma da 3ª coluna: {col}\nMaior número da 2ª linha: {lin}')
