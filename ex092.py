print('\033[31m====== DESAFIO 92 ======\033[m')
from datetime import date
dados = dict()
dados['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
dados['idade'] = date.today().year - ano
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['anocont'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados ['idade']+((dados['anocont'] + 35) - date.today().year)
print('-'*30)
for i, v in dados.items():
    print(f' - {i} tem o valor {v}')
