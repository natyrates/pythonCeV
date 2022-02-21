print('\033[31m====== DESAFIO 60 ======\033[m')
from math import factorial
n = int(input('Digite um número para calcular o seu fatorial: '))
c = n
f = factorial(n)
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
print('{}'.format(f))
