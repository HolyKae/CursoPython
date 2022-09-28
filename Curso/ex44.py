p = float(input('Preço do produto: R$'))
c = int(input('Condição de pagamento:\n1- Em dinheiro\n2- No cartão'))
if c == 1:
    print(f'O valor com 15% de desconto ficou: R${p-(p*0.15)}')
elif c == 2:
    c = int(input('Em quantas vezes no cartão? '))
    if c == 1:
        print(f'O valor com 5% de desconto ficou: R${p-(p*0.05)}')
    elif c < 3:
        print(f'O valor com 20% de juros ficou: R${p+(p*0.2)}')
    else:
        print(f'Mesmo valor: R${p}')
