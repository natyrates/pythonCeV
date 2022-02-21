print('\033[31m====== DESAFIO 49 ======\033[m')
n = int(input('Digite um número para vê sua tabuada: '))
for c in range(1, 11):
    result = n * c
    print('{} x {:2} = {}'.format(n, c, result))