def notas(*n, sit=False):
    """
    Função para analisar notas e situação de vários alunos
    :param n: Uma ou mais notas
    :param sit: (opcional) Indica se deve ou não adicionar a situação
    :return: Dicionário com várias informações sobre a situação
    """
    l = dict()
    l['Total'] = len(n)
    l['Maior'] = max(n)
    l['Menor'] = min(n)
    l['Média'] = sum(n) / len(n)
    if sit:
        if l['Média'] < 5:
            l['Situação'] = 'Ruim'
        if l['Média'] < 7:
            l['Situação'] = 'Razoável'
        else:
            l['Situação'] = 'Boa'
    return l


r = notas(9.5, 8.5, 10, 5.5, sit=True)
print(r)
