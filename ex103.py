print('\033[31m====== DESAFIO 103 ======\033[m')
def ficha(nomej='<desconhecido>', quantg=0):
    print(f'O jogador {nomej} fez {quantg} gol(s) no campeonato.')

n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(quantg=g)
else:
    ficha(n, g)