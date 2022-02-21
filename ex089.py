print('\033[31m====== DESAFIO 89 ======\033[m')
dados = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2 ) / 2
    dados.append([nome, [n1, n2], media])
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('-' * 23)
print(f'{"Nº":<4}{"NOME":<10}{"MEDIA":>8}')
print('-' * 23)
for i, a in enumerate(dados):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*30)
    op = int(input('Mostrar notas de qual aluno? [999 interrompe] '))
    if op == 999:
        print('FINALIZANDO...')
        break
    if op <= len(dados) - 1:
        print(f'Notas de {dados[op][0]} são {dados[op][1]}')
print('<<< VOLTE SEMPRE >>>')