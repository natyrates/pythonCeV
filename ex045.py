print('\033[31m====== DESAFIO 45 ======\033[m')
import random
import time
lista = ('PEDRA', 'PAPEL', 'TESOURA')
comp = random.randint(0, 2)
print('\033[36m-' * 20)
print('Suas opções:\n'
      '[ 0 ] PEDRA\n'
      '[ 1 ] PAPEL\n'
      '[ 2 ] TESOURA')
print('\033[36m-\033[m' * 20)
jogada = int(input('Qual a sua jogada? '))
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PÔ!')
print('\033[35mO computador jogou {}'.format(lista[comp]))
print('Você jogou {}\033[m'.format(lista[jogada]))
if comp == 0:
      if jogada == 0:#PEDRA
            print('DEU EMPATE!')
      elif jogada == 1:
            print('VOCÊ VENCEU!')
      elif jogada == 2:
            print('COMPUTADOR VENCEU!')
      else:
            print('OPÇÃO INVÁLIDA!')
elif comp == 1:#PAPEL
      if jogada == 0:
            print('COMPUTADOR VENCEU!')
      elif jogada == 1:
            print('DEU EMPATE')
      elif jogada == 2:
            print('VOCÊ VENCEU!')
      else:
            print('OPÇÃO INVÁLIDA!')
elif comp == 2:#TESOURA
      if jogada == 0:
            print('VOCÊ VENCEU!')
      elif jogada == 1:
            print('COMPUTADOR VENCEU!')
      elif jogada == 2:
            print('DEU EMPATE!')
      else:
            print('OPÇÃO INVÁLIDA!')
