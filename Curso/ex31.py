d = float(input('Distância: '))
if d < 200:
    print('Preço: R${:.2f}'.format(d*0.5))
else:
    print('Preço: R${:.2f}'.format(d * 0.45))
