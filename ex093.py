print('\033[31m====== DESAFIO 93 ======\033[m')
dados = dict()
gol = list()
dados['nome'] = str(input('Nome do jogador: '))
quant = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c in range(0, quant):
    gol.append(int(input(f'  Quantos gols na partida {c}? ')))
dados['gols'] = gol[:]
dados['total'] = sum(gol)
print('-'*33)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-'*33)
print(f'O jogador {dados["nome"]} jogou {len(dados["gols"])} partidas:')
for i, v in enumerate(dados["gols"]):
    print(f'    => Na partida {i}, fez {v} gols')
print('-'*33)
print(f'Foi um total de {dados["total"]} gols.')