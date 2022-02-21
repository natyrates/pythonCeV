print('\033[31m====== DESAFIO 69 ======\033[m')
print('\033[34m-'*25)
print('   CADASTRO DE PESSOAS')
print('\033[34m-\033[m'*25)
contp = conth = contm = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    print('\033[34m-\033[m'*25)
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    print('\033[34m-\033[m'*25)
    if idade >= 18:
        contp += 1
    if sexo == 'M':
        conth += 1
    if sexo == 'F' and idade < 20:
        contm +=1
    if resp == 'N':
        break
print(f'Mais de 18 anos tem:\033[36m {contp} pessoas\033[m')
print(f'Total de homens cadastrados:\033[36m {conth} pessoas\033[m')
print(f'Total de mulheres menores de 20 anos:\033[36m {contm} pessoas\033[m')