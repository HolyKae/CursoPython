import random
v = []
for i in range(5):
    n = random.randint(1, 99)
    v.append(n)
li = v[:]
v.sort()
print(li)
print(f'O menor número apareceu na {li.index(v[0])+1}ª posição e foi: {v[0]}\nO maior apareceu na '
      f'{li.index(v[-1])+1}ª posição e foi : {v[-1]}')