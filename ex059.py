print('\033[31m====== DESAFIO 59 ======\033[m')
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
op = 0
while op != 5:
    print('\033[35m-'*25)
    print('[ 1 ] Somar\n'
          '[ 2 ] Multiplicar\n'
          '[ 3 ] Maior\n'
          '[ 4 ] Novos números\n'
          '[ 5 ] Sair do programa')
    print('\033[35m-\033[m'*25)
    op = int(input('>>>>> Qual é a sua opção? '))
    if op == 1:
        soma = n1 + n2
        print('O resultado de {} + {} = {}'.format(n1, n2, soma))
    elif op == 2:
        mult = n1 * n2
        print('O resultado de {} x {} = {}'.format(n1, n2, mult))
    elif op == 3:
        if n1 > n2:
            print('Entre {} e {} o maior valor é {}.'.format(n1, n2, n1))
        else:
            print('Entre {} e {} o maior valor é {}.'.format(n1, n2, n2))
    elif op == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('Opção invália, tente novamente!')
    sleep(2)
print('\033[35m-\033[m' * 31)
print('Fim do programa. Volte sempre!')