print('\033[31m====== DESAFIO 94 ======\033[m')
dados = dict()
pessoas = list()
soma = media = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
    dados['idade'] = int(input('Idade: '))
    pessoas.append(dados.copy())
    soma += dados['idade']
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('-' * 35)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
media = soma/len(pessoas)
print(f'B) A média de idade é de {media:.1f} anos.')
print('C) As mulheres cadastradas foram ',end='')
for p in pessoas:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in pessoas:
    if p['idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ',end='')
        print()
