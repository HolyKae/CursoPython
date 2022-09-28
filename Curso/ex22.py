n = input('Digite seu nome: ').strip()
pn = n.split()
print('{}\n{}\nTem {} letras\nPrimeiro nome tem {} letras'.format(n.upper(), n.lower(), len(n) - n.count(' '), len(pn[0])))
