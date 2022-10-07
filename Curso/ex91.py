import random

n = {}
s = []
for c in range(4):
    jog = f'Jogador {c + 1}'
    n[jog] = random.randint(1, 6)
for k, v in n.items():
    print(f'|{k}: {v:>2}|')
print('--'*8)
sortn = {}
sortj = sorted(n, key=n.get, reverse=True)
for k in sortj:
    sortn[k] = n[k]
c = 1
for k, v in sortn.items():
    print(f'{c}º lugar:  |{k}: {v:>2}|')
    c += 1
