from time import sleep
n = int(input('Digite um número: '))
for c in range(n, -1, -1):
    sleep(1)
    print(c)
print('FIM')
