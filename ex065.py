print('\033[31m====== DESAFIO 65 ======\033[m')
op = 'S'
cont = media = soma = maior = menor = 0
while op != 'N':
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma/cont
print('A média dos {} números digitados foi {}'.format(cont, media))
print('O maior número foi {} e o menor foi {}'.format(maior, menor))