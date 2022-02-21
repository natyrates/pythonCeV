print('\033[31m====== DESAFIO 88 ======\033[m')
from random import randint
print('\033[35m-'*30)
print(f'{"JOGAR NA MEGA SENA":^30}')
print('\033[35m-\033[m'*30)
jogos = []
lista = []
quant = int(input('Quantos jogos você quer que eu sorteie: '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in jogos:
            jogos.append(num)
            cont += 1
        if cont >= 6:
            break
    jogos.sort()
    lista.append(jogos[:])
    jogos.clear()
    tot += 1
print('\033[35m-'*5, f' SORTEANDO {quant} JOGOS ', '-' * 5, end='')
print('\033[m')
for i, l in enumerate(lista):
    print(f'Jogo {i+1}: {l}')
print('\033[35m-'*10, f' BOA SORTE ', '-' * 10)
