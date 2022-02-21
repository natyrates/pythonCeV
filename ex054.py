print('\033[31m====== DESAFIO 54 ======\033[m')
from datetime import date
atual = date.today().year
cont1 = 0
cont2 = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = atual - ano
    if idade >= 21:
        cont1 += 1
    else:
        cont2 += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(cont1))
print('E também tivemos {} pessoas menores de idade.'.format(cont2))
