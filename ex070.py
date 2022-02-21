print('\033[31m====== DESAFIO 70 ======\033[m')
print('\033[36m-'*25)
print('   LOJA SUPER BARATÃO')
print('\033[36m-\033[m'*25)
soma = contp = menor = cont = 0
nomeb = ''
while True:
    nomep = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    print('\033[36m-\033[m'*25)
    soma += preco
    if preco > 1000:
        contp += 1
    if cont == 1 or preco < menor: #MENOR
        menor = preco
        nomeb = nomep
    if resp == 'N':
        break
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {contp} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeb} que custa R${menor:.2f}')