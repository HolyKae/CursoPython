v = int(input('Qual a velocidade do carro? '))
if v > 80:
    print('Multa: R${:.2f}'.format((v-80)*7))
