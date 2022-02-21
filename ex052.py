print('\033[31m====== DESAFIO 52 ======\033[m')
n = int(input('Digite um número: '))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[36m', end='')
        tot = tot + 1
    else:
        print('\033[m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi dividível {} vezes'.format(n, tot))
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')