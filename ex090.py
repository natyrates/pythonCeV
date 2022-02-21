print('\033[31m====== DESAFIO 90 ======\033[m')
situacao = {}
situacao['nome'] = str(input('Nome: '))
situacao['media'] = float(input(f'Média de {situacao["nome"]}: '))
if situacao["media"] >= 7:
    situacao['situação'] = 'Aprovado'
elif 5 <= situacao["media"] < 7:
    situacao['situação'] = 'Recuperação'
else:
    situacao['situação'] = 'Rerovado'
for k, v in situacao.items():
    print(f' - {k} é igual a {v}')

