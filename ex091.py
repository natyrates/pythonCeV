print('\033[31m====== DESAFIO 91 ======\033[m')
from random import randint
from time import sleep
from operator import itemgetter
jogadas = {'jog1': randint(1, 6),
           'jog2': randint(1, 6),
           'jog3': randint(1, 6),
           'jog4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogadas.items():
    print(f'    O {k} tirou {v}')
    sleep(1)
print('Ranking dos jogadores:')
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'    {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)

