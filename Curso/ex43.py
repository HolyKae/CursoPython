a = float(input('Sua Altura: '))
p = float(input('Seu peso: '))
imc = p / (a**2)
print(imc)
if imc < 18.5:
    print('Abaixo do Peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')
