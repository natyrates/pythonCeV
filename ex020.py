print('====== DESAFIO 20 ======')
import random
a1 = input('Primeiro aluno:  ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]
sorteio = random.shuffle(lista)
print('A ordem de apresentação será')
print(lista)