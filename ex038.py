print('\033[31m====== DESAFIO 38 ======\033[m')
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('Primeiro valor é maior!')
elif n2 > n1:
    print('Segundo valor é maior.')
else:
    print('Nenhum valor é maior, os dois são iguais.')
