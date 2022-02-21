print('\033[31m====== DESAFIO 51 ======\033[m')
print('\033[32m=' * 30)
print('      10 TEMOS DE UMA PA')
print('\033[32m=\033[m' * 30)
p = int(input('Primeiro termo: '))
r = int(input('Rezão: '))
d = p + (10 - 1) * r
for c in range(p, d+r, r):
    print(c, end=' → ')
print('ACABOU')
