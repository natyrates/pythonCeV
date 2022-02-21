print('\033[31m====== DESAFIO 79 ======\033[m')
num = list()
while True:
    n = (int(input('Digite um valor: ')))
    if n not in num:
        num.append(n)
        print('Número adicionado com sucesso!')
    else:
        print('Número duplicado, não será adicionado!')
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
num.sort()
print(f'Você digitou os valores: {num}')
