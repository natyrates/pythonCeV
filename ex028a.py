print('====== DESAFIO 28 ======')
import random
import time
c = random.randint(0, 5)
print('-'*40)
print('Olá, sou o computador!\nTente adivinhar o número que pensei...')
print('-'*40)
num = int(input('Digite o seu número entre 0-5: '))
print('PROCESSANDO...')
time.sleep(3)
if c == num:
    print('Parabéns! Você acertou meu número.')
else:
    print('Que pena! Você não acertou meu número.')
    print('Meu número: {}\nSeu número: {}'.format(c, num))
