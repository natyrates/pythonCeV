print('====== DESAFIO 32 ======')
from datetime import date
ano = int(input('Digite algum ano. (Digite 0 para analisar o ano atual): '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 00 or ano % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} não é BISSEXTO!'.format(ano))