while True:
    n = int(input('Quer a tabuada de qual valor? '))
    if n < 0:
        break
    for t in range(1, 11):
        print(f'{n} * {t:2} = {n * t}')
