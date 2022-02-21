print('\033[31m====== DESAFIO 56 ======\033[m')
maior = 0
nomemaisvelho = ''
media = 0
soma = 0
totmulher = 0
for c in range(1, 5):
    print('\033[34m----- {}ª PESSOA -----\033[m'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    soma += idade
    if c == 1 and sexo in 'Mm':
        maior = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > maior:
        maior = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
media = soma / 4
print('A média de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior, nomemaisvelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher))
