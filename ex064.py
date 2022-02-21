print('\033[31m====== DESAFIO 64 ======\033[m')
cont = soma = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um número [999 para parar]: '))
print('Foram digitados {} números.'.format(cont))
print('A soma dos números digitados é {}'.format(soma))
