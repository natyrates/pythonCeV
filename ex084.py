print('\033[31m====== DESAFIO 84 ======\033[m')
galera = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(galera) == 0:
        menor = maior = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    galera.append(dados[:])
    dados.clear()
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Você cadastrou {len(galera)} pessoas.')
print(f'O maior peso foi de {maior}kg das pessoas: ', end='')
for p in galera:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor}kg das pessoas: ', end='')
for p in galera:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()