p = [[str(input('Nome: '))], [float(input('Nota 1: ')), float(input('Nota 2: '))]]
m = (p[1][0] + p[1][1]) / 2
p.append([m])
al = [p[:]]
while True:
    d = input('Quer continuar? [S/N]').upper()
    if d not in 'SN':
        print('buro')
        d = input('Quer continuar? [S/N]').upper()
    elif d in 'S':
        p = [[str(input('Nome: '))], [float(input('Nota 1: ')), float(input('Nota 2: '))]]
        m = (p[1][0] + p[1][1]) / 2
        p.append([m])
        al.append(p[:])
    else:
        break
while True:
    d = input('Quer escolher um aluno especifico? [S/N]').upper()
    if d not in 'SN':
        print('buro')
        d = input('Quer escolher um aluno especifico? [S/N]').upper()
    elif d in 'S':
        d = input('Digite o nome do aluno: ')
        for i in range(len(al)):
            if d in al[i][0]:
                print('--' * 50)
                print(f'Nome: {al[i][0][0]:.<20} -+-+-+- Notas: 1ª- {al[i][1][0]:2.1f} -+- 2ª- {al[i][1][1]:2.1f} -+-+-+- Média: {al[i][2][0]:2.1f}')
                print('--' * 50)
        break
    else:
        print('--' * 50)
        for i in range(len(al)):
            print(
                f'Nome: {al[i][0][0]:.<20} -+-+-+- Notas: 1ª- {al[i][1][0]:2.1f} -+- 2ª- {al[i][1][1]:2.1f} -+-+-+- Média: {al[i][2][0]:2.1f}')
            print('--' * 50)
        break

