print('\033[31m====== DESAFIO 61 ======\033[m')
print('\033[32m=' * 30)
print('      10 TEMOS DE UMA PA')
print('\033[32m=\033[m' * 30)
p = int(input('Primeiro termo: '))
r = int(input('Rezão: '))
termo = p
cont = 1
while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += r
    cont += 1
print('ACABOU')