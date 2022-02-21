print('\033[31m====== DESAFIO 100 ======\033[m')
from random import randint
def sorteia():
    for c in range(0, 5):
        aleat = randint(1, 10)
        numeros.append(aleat)
    print(f'Sorteando os 5 valores da lista: {numeros}')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}.')

numeros = list()
sorteia()
somaPar(numeros)
