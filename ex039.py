print('\033[31m====== DESAFIO 39 ======\033[m')
from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))
if idade < 18:
    d = 18 - idade
    print('Ainda faltam {} anos para o alistamento.\n'
          'Seu alistamento será em {}.'.format(d, atual + d))
elif idade > 18:
    d = idade - 18
    print('Você já deveria ter se alistado há {} anos.\n'
          'Seu alistamento foi em {}.'.format(d, atual - d))
else:
    print('Você tem que se alistar IMEDIATAMENTE!')
