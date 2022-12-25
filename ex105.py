def notas(*n, sit=False):
    '''
    -> Função para analisar notas e situações de variso alunos.
    Args:
        *n: uma ou mais notas dos alunos
        sit: valor opcional, indicando se deve ou não adicionar a situação.

    Returns: dicionario com varias informações sobre a situação da turma

    '''
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'Boa'
        elif r['media'] >= 5:
            r['situação'] = 'Razoavel'
        else:
            r['situação'] = 'Ruim'
    return r

#programa principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)