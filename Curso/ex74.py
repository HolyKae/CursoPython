import random
n = tuple(random.randint(1, 10) for c in range(5))
print(f'{n}\nMaior: {sorted(n)[-1]}\nMenor: {sorted(n)[0]}')
