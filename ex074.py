print('\033[31m====== DESAFIO 74 ======\033[m')
from random import randint
num = (randint(1,5), randint(1,5), randint(1,5), randint(1,5), randint(1,5))
print('Os valores sorteados foram: ',end='')
for c in num:
    print(f'{c} ', end='')
print(f'\nO maior valor sorteado foi: {max(num)}')
print(f'O menor valor sorteado foi: {min(num)}')
