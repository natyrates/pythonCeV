print('\033[31m====== DESAFIO 50 ======\033[m')
soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Número {}: '.format(c)))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print('Você informou {} números pares e a soma deles foi: {}'.format(cont, soma))
