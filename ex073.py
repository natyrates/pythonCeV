print('\033[31m====== DESAFIO 73 ======\033[m')
times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians',
         'Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos',
         'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá',
         'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')
print(f'Os 5 primeiros são {times[0:5]}')
print(f'Os 4 últimos são {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')