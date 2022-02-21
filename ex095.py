print('\033[31m====== DESAFIO 95 ======\033[m')
dados = dict()
gol = list()
galera = list()
while True:
    dados.clear()
    dados['nome'] = str(input('Nome do jogador: '))
    quant = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    gol.clear()
    for c in range(0, quant):
        gol.append(int(input(f'  Quantos gols na partida {c+1}? ')))
    dados['gols'] = gol[:]
    dados['total'] = sum(gol)
    galera.append(dados.copy())
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('-' * 33)
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<12}', end='')
print()
print('-' * 33)
for i, a in enumerate(galera):
    print(f'{i:>3} ', end='')
    for d in a.values():
        print(f'{str(d):<12}', end='')
    print()
print('-'*33)
while True:
    op = int(input('Mostrar dados de qual jogador? [999 interrompe] '))
    if op == 999:
        print('FINALIZANDO...')
        break
    if op >= len(galera):
        print(f'ERRO! Não exite jogador com o código {op}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {galera[op]["nome"]}')
        for i, g in enumerate(galera[op]["gols"]):
            print(f'    No jogo {i+1} fez {g} gols.')
print('<<< VOLTE SEMPRE >>>')