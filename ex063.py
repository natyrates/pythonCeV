print('\033[31m====== DESAFIO 63 ======\033[m')
print('\033[32m-' * 23)
print('Sequência de Fibonacci')
print('\033[32m-\033[m' * 23)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('{} - {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' - {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
