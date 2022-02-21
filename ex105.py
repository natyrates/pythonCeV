print('\033[31m====== DESAFIO 105 ======\033[m')
def notas(*n, sit=False):
    dados = dict()
    dados['total'] = len(n)
    dados['maior'] = max(n)
    dados['menor'] = min(n)
    dados['media'] = sum(n)/len(n)
    if sit:
        if dados['media'] >= 7:
            dados['situação'] = 'BOA'
        elif dados['media'] >=5:
            dados['situação'] = 'RAZOÁVEL'
        else:
            dados['situação'] = 'RUIM'
    return dados

resp = notas(5.5, 2.5, sit=True)
print(resp)