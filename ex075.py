print('\033[31m====== DESAFIO 75 ======\033[m')
n = (int(input(f'1º valor: ')),
     int(input(f'2º valor: ')),
     int(input(f'3º valor: ')),
     int(input(f'4º valor: ')))
print(f'Você digitou os valores: {n}')
print(f'O número 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O número 3 está na {n.index(3)+1}ª posição')
else:
    print('O valor 3 não foi encontrado em nenhuma posição')
print(f'Os valores pares digitados foram: ',end='')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')



