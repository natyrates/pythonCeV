print('\033[31m====== DESAFIO 99 ======\033[m')
def maior(*num):
    print('-' * 35)
    cont = maior = 0
    print('Analisando os valores passados...')
    for c in num:
        print(f'{c} ', end='')
        if cont == 0:
            maior = c
        else:
            if c > maior:
                maior = c
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi o {maior}.')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()