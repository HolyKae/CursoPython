f = input('Digite uma frase: ').strip()
print('A: {}\n1ª: {}\nUrtema: {}'.format(f.upper().count('A'), f.upper().find('A'), f.upper().rfind('A')))
