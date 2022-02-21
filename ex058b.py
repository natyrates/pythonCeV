print('\033[31m====== DESAFIO 58 ======\033[m')
import random
c = random.randint(0, 10)
print('-'*40)
print('Olá, sou o computador!\nTente adivinhar o número que pensei...')
print('-'*40)
acertou = False
tent = 0
while not acertou:
    num = int(input('Digite o seu número entre 0-10: '))
    tent += 1
    if num == c:
        acertou = True
    else:
        if c > num:
           print('Mais... Tente mais uma vez!')
        else:
            print('Menos... Tente mais uma vez!')
print('Acertou com {} tentativas. Parabéns!'.format(tent))
